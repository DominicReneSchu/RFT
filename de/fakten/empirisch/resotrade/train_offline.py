"""
Resonanzlogisches Offline-Training V9.4.

Änderungen V9.4:
  - Fee aus config.KRAKEN_FEE_PCT (nicht hartkodiert)
  - HOLD-Bewertungs-Schwelle aus config.HOLD_NOISE_PCT (nicht hartkodiert)
  - Bugfix V9.2 bleibt: Erfahrung nur für effektiv ausgeführte Aktion

Speicher-Architektur:
  - Liest:    trade_experience_offline.csv (eigener Speicher)
  - Schreibt: trade_experience_offline.csv
  - Am Ende:  merge_experience() → trade_experience_weighted.csv
"""
from pathlib import Path
from typing import Optional

import csv
import numpy as np
import pandas as pd

from config import (
    HOLD_NOISE_PCT,
    KRAKEN_FEE_PCT,
    EXPERIENCE_DECAY_PER_PASS,
    TRAINING_WINDOW_LENGTH,
)
from data_loader import (
    load_analysis_signals,
    load_or_download_btc_history,
    has_analysis_signals,
)
from env import TradingEnv
from experience import (
    load_experience,
    persist_experience,
    add_experience,
    decay_experience,
    merge_experience,
    merge_status,
    EXPERIENCE_OFFLINE_CSV,
    EXPERIENCE_CSV,
)
from policy import resonance_learning_policy, make_chain
from diagnostics import log_episode_step


DATA_DIR = Path("data")
PROGRESS_CSV = DATA_DIR / "training_progress.csv"


def prepare_price_df_from_analysis() -> pd.DataFrame:
    if has_analysis_signals():
        try:
            df = load_analysis_signals()
            df = df.copy()
            df["price"] = df["price"].astype(float)
            print(f"[Data] Resonanz-Analyse-Signale geladen ({len(df)} Zeilen).")
        except Exception as e:
            print(f"[Data] Fehler beim Laden der Analyse-Signale: {e}")
            print("[Data] Fallback auf rohe BTC-Preisdaten.")
            df = _prepare_from_raw_history()
    else:
        print("[Data] Keine signals_with_posteriors_*.csv gefunden.")
        print("[Data] Lade rohe BTC-Preisdaten (Binance/CoinGecko/Fallback).")
        df = _prepare_from_raw_history()

    if "ma_short" not in df.columns:
        df["ma_short"] = df["price"].rolling(7, min_periods=1).mean()
    if "ma_long" not in df.columns:
        df["ma_long"] = df["price"].rolling(50, min_periods=1).mean()

    if "trend_bin" not in df.columns:
        diff = (df["ma_short"] - df["ma_long"]) / (df["ma_long"].abs() + 1e-8)
        trend_bins = []
        for x in diff:
            if x > 0.01:
                trend_bins.append("uptrend")
            elif x < -0.01:
                trend_bins.append("downtrend")
            else:
                trend_bins.append("sideways")
        df["trend_bin"] = trend_bins

    print(f"[Data] DataFrame bereit: {len(df)} Zeilen, "
          f"Spalten: {sorted(df.columns.tolist())}")
    return df


def _prepare_from_raw_history() -> pd.DataFrame:
    raw = load_or_download_btc_history(days=365 * 3)
    df = raw.copy()

    if "price" not in df.columns:
        for col in ["Close", "close", "CLOSE"]:
            if col in df.columns:
                df["price"] = df[col]
                break
    if "price" not in df.columns:
        raise ValueError("Keine 'price'-Spalte in den Rohdaten gefunden.")

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])

    for ts_col in ["ts", "timestamp", "datetime", "Date"]:
        if ts_col in df.columns:
            df[ts_col] = pd.to_datetime(df[ts_col], errors="coerce")
            df = df.dropna(subset=[ts_col])
            df = df.set_index(ts_col).sort_index()
            break

    df = df.reset_index(drop=True)
    return df


def _evaluate_step(
    btc_before: float,
    btc_after: float,
    cash_before: float,
    cash_after: float,
    price: float,
    price_next: Optional[float],
) -> str:
    """
    Schritt-Bewertung V9.4.

    Trade-Bewertung:
      Fee-neutralisiert mit 25% Fee als Schwelle (Kompromiss).
      Zu hoch (50%) → alles draw. Zu niedrig (0%) → alles failure.

    HOLD-Bewertung:
      Moderater Korridor (65%/35% statt 80%/20%).
      Normale LONG-Position (60-65%) bei Rückgang → draw.
      Starke LONG (>65%) bei Rückgang → failure (zu exponiert).
    """
    if price <= 0:
        return "draw"

    btc_equiv_before = btc_before + cash_before / price
    btc_equiv_after = btc_after + cash_after / price

    delta_immediate = btc_equiv_after - btc_equiv_before

    # --- Trade-Schritt ---
    traded = abs(delta_immediate) > 1e-12
    if traded:
        if price_next is not None and price_next > 0:
            btc_equiv_after_next = btc_after + cash_after / price_next
            btc_equiv_hold_next = btc_before + cash_before / price_next
            delta_prospective = btc_equiv_after_next - btc_equiv_hold_next
        else:
            delta_prospective = 0.0

        delta = delta_immediate + 0.5 * delta_prospective

        fee_cost = btc_equiv_before * KRAKEN_FEE_PCT
        threshold = max(1e-8, fee_cost * 0.25)

        if delta > threshold:
            return "success"
        elif delta < -threshold:
            return "failure"
        return "draw"

    # --- HOLD-Schritt ---
    if price_next is None or price_next <= 0:
        return "draw"

    price_change_pct = (price_next - price) / price

    hold_threshold = HOLD_NOISE_PCT

    if abs(price_change_pct) < hold_threshold:
        return "draw"

    if btc_equiv_before <= 1e-8:
        return "draw"

    btc_value = btc_before * price
    total_value = btc_value + cash_before
    if total_value <= 0:
        return "draw"

    btc_share = btc_value / total_value

    if price_change_pct > hold_threshold:
        if btc_share > 0.65:
            return "success"
        elif btc_share < 0.35:
            return "failure"
        return "draw"
    else:
        if btc_share < 0.35:
            return "success"
        elif btc_share > 0.65:
            return "failure"
        return "draw"


def _evaluate_position_transition(
    pos_before: str,
    pos_after: str,
    e_long: float,
) -> Optional[str]:
    if pos_before == pos_after:
        return None

    if pos_before == "LONG" and pos_after == "PARTIAL":
        return "success" if e_long > 0 else "failure"

    if pos_before == "PARTIAL" and pos_after == "FLAT":
        return "success" if e_long > 0.01 else "failure"

    if pos_before == "PARTIAL" and pos_after == "LONG":
        return "success" if e_long < 0 else "failure"

    if pos_before == "FLAT" and pos_after == "PARTIAL":
        return "success" if e_long < -0.01 else "failure"

    return None


def _determine_effective_action(
    btc_before: float,
    btc_after: float,
    cash_before: float,
    cash_after: float,
    policy_action: str,
) -> str:
    """
    V9.2 Bugfix: Bestimmt die tatsächlich ausgeführte Aktion anhand der
    Portfolio-Deltas. Wenn die Env die Aktion blockiert hat,
    gibt diese Funktion "HOLD" zurück — nicht die gewünschte Aktion.
    """
    delta_btc = btc_after - btc_before
    delta_cash = cash_after - cash_before

    if abs(delta_btc) < 1e-10 and abs(delta_cash) < 1e-4:
        return "HOLD"

    if delta_btc > 1e-10:
        if "MEDIUM" in policy_action:
            return "BUY_MEDIUM"
        return "BUY_SMALL"

    if "MEDIUM" in policy_action:
        return "SELL_MEDIUM"
    return "SELL_SMALL"


def run_long_episode(
    env: TradingEnv,
    exp: dict,
    btc_hodl: float,
    episode_num: int = 0,
    enable_diagnostics: bool = True,
    epsilon: float = 0.05,
) -> float:
    """
    V9.4: window_length wird NICHT mehr überschrieben.
    Jede Episode nutzt ein zufälliges Fenster aus den Gesamtdaten.
    Das erzeugt Trainings-Diversität über verschiedene Marktphasen.
    """

    state = env.reset()
    step_counter = 0

    prev_chain: Optional[str] = None
    prev_btc: float = env.current_portfolio().btc
    prev_cash: float = env.current_portfolio().cash
    prev_price: float = float(state.get("price", 0.0))
    prev_pos: str = state.get("pos", "FLAT")

    episode_chains: list = []

    while True:
        btc_before = env.current_portfolio().btc
        cash_before = env.current_portfolio().cash
        price = float(state.get("price", 0.0))
        pos_before = state.get("pos", "FLAT")

        policy_action = resonance_learning_policy(state, exp, epsilon=epsilon)

        next_state, done = env.step(policy_action)

        btc_after = env.current_portfolio().btc
        cash_after = env.current_portfolio().cash

        block_reason = env.last_block_reason

        effective_action = _determine_effective_action(
            btc_before, btc_after, cash_before, cash_after, policy_action,
        )

        chain = make_chain(state, effective_action)

        episode_chains.append(chain)

        if prev_chain is not None:
            result = _evaluate_step(
                prev_btc, btc_before, prev_cash, cash_before,
                prev_price, price,
            )
            add_experience(prev_chain, result, exp)

            current_pos = state.get("pos", "FLAT")
            trans_result = _evaluate_position_transition(
                prev_pos, current_pos,
                float(state.get("e_long", 0.0) or 0.0),
            )
            if trans_result is not None:
                add_experience(prev_chain, trans_result, exp)

        if enable_diagnostics:
            log_episode_step(
                episode=episode_num,
                step=step_counter,
                state=state,
                policy_action=policy_action,
                effective_action=effective_action,
                btc_before=btc_before,
                btc_after=btc_after,
                cash_before=cash_before,
                cash_after=cash_after,
                price=price,
                block_reason=block_reason,
            )

        prev_chain = chain
        prev_btc = btc_before
        prev_cash = cash_before
        prev_price = price
        prev_pos = pos_before

        step_counter += 1

        if done:
            break
        state = next_state

    if prev_chain is not None:
        btc_final = env.current_portfolio().btc
        cash_final = env.current_portfolio().cash
        result = _evaluate_step(
            prev_btc, btc_final, prev_cash, cash_final,
            prev_price, None,
        )
        add_experience(prev_chain, result, exp)

    btc_end = env.current_portfolio().btc
    cash_end = env.current_portfolio().cash
    final_price = prev_price
    btc_equiv_end = btc_end + (cash_end / final_price if final_price > 0 else 0)

    if btc_equiv_end >= btc_hodl:
        ep_result = "success"
    elif btc_equiv_end >= btc_hodl * 0.95:
        ep_result = "draw"
    else:
        ep_result = "failure"

    for c in episode_chains[::10]:
        add_experience(c, ep_result, exp)

    return btc_end


def append_progress_row(episode: int, btc_end: float, cash_end: float, price: float):
    DATA_DIR.mkdir(exist_ok=True)
    file_exists = PROGRESS_CSV.exists()
    btc_equiv = btc_end + (cash_end / price if price > 0 else 0)
    with PROGRESS_CSV.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["episode", "btc_end", "cash_end", "btc_equiv", "price"])
        writer.writerow([
            episode,
            f"{btc_end:.10f}",
            f"{cash_end:.2f}",
            f"{btc_equiv:.10f}",
            f"{price:.2f}",
        ])


def train_offline(
    num_episodes: int = 200,
    window_length: int = TRAINING_WINDOW_LENGTH,
    start_btc: float = 1.0,
    trade_fraction_small: float = 0.10,
    trade_fraction_medium: float = 0.25,
    hodl_share: float = 0.10,
    min_btc_for_full_sell: float = 0.1,
    min_btc_trade_fraction: float = 0.05,
    start_cash_share: float = 0.2,
):
    """
    Resonanzlogisches Offline-Training V9.4.

    Speicher-Architektur:
      - Liest/schreibt: trade_experience_offline.csv
      - Am Ende: merge mit Live → trade_experience_weighted.csv

    V9.4: fee_pct aus config.KRAKEN_FEE_PCT (Single Source of Truth).
    V9.4: hodl_share Default korrigiert auf 0.10 (konsistent mit config.HODL_SHARE).
    V9.4: Decay pro Pass statt pro Episode (EXPERIENCE_DECAY_PER_PASS aus config).
    """
    df = prepare_price_df_from_analysis()
    btc_hodl = float(start_btc)

    start_price = float(df["price"].iloc[0])
    start_value_usd = start_btc * start_price
    start_cash = start_value_usd * start_cash_share
    start_btc_effective = (start_value_usd * (1.0 - start_cash_share)) / start_price

    hodl_core_btc = start_btc_effective * hodl_share

    print(f"[Config] start_btc_effective={start_btc_effective:.6f}, "
          f"start_cash={start_cash:.2f} USD, "
          f"hodl_core_btc={hodl_core_btc:.6f}, "
          f"start_price={start_price:.2f}")
    print(f"[Config] Speicher: {EXPERIENCE_OFFLINE_CSV.name} "
          f"(getrennt von Live)")
    print(f"[Config] HOLD-Noise-Schwelle: {HOLD_NOISE_PCT * 100:.2f}%")
    print(f"[Config] Fee: {KRAKEN_FEE_PCT * 100:.3f}% (aus config.py)")
    print(f"[Config] Decay: {EXPERIENCE_DECAY_PER_PASS:.2f} pro Pass "
          f"(nicht pro Episode)")

    env = TradingEnv(
        df,
        start_btc=start_btc_effective,
        start_cash=start_cash,
        fee_pct=KRAKEN_FEE_PCT,
        price_col="price",
        trend_col="trend_bin",
        trade_fraction_small=trade_fraction_small,
        trade_fraction_medium=trade_fraction_medium,
        ath_buffer_pct=0.0,
        window_length=window_length,
        hodl_core_btc=hodl_core_btc,
        min_btc_for_full_sell=min_btc_for_full_sell,
        min_btc_trade_fraction=min_btc_trade_fraction,
    )

    exp = load_experience(path=EXPERIENCE_OFFLINE_CSV)
    print(f"[Train] Offline-Erfahrungsspeicher geladen: {len(exp)} Einträge")

    if PROGRESS_CSV.exists():
        PROGRESS_CSV.unlink()

    for episode in range(1, num_episodes + 1):
        epsilon = max(0.03, 0.20 * (1.0 - episode / num_episodes))

        enable_diag = (episode <= 3) or (episode == num_episodes)
        btc_end = run_long_episode(
            env, exp, btc_hodl=btc_hodl,
            episode_num=episode,
            enable_diagnostics=enable_diag,
            epsilon=epsilon,
        )

        cash_end = env.current_portfolio().cash
        last_price = env.current_portfolio().price
        append_progress_row(episode, btc_end, cash_end, last_price)

        if episode % 5 == 0:
            btc_equiv = btc_end + (cash_end / last_price if last_price > 0 else 0)
            print(f"[Train] Episode {episode}: "
                  f"btc={btc_end:.6f}, cash={cash_end:.0f}, "
                  f"btc_equiv={btc_equiv:.6f}, ε={epsilon:.3f}")
            persist_experience(exp, path=EXPERIENCE_OFFLINE_CSV)

    decay_experience(exp, decay_factor=EXPERIENCE_DECAY_PER_PASS, min_threshold=1)

    persist_experience(exp, path=EXPERIENCE_OFFLINE_CSV)
    print(f"\nOffline-Training abgeschlossen. "
          f"Offline-Speicher: {len(exp)} Einträge")

    print(f"\n--- Merge Offline + Live → Weighted ---")
    merged = merge_experience()

    print(f"\nSpeicher-Status nach Merge:")
    merge_status()

    summarize_training(btc_hodl)


def summarize_training(btc_hodl: float):
    print("\n=== Trainingsauswertung ===")
    if not PROGRESS_CSV.exists():
        print("Keine training_progress.csv gefunden.")
        return

    df = pd.read_csv(PROGRESS_CSV)
    if df.empty:
        print("training_progress.csv ist leer.")
        return

    btc_vals = df["btc_end"].astype(float).values
    equiv_vals = df["btc_equiv"].astype(float).values

    print(f"HODL-Benchmark:                        {btc_hodl:.6f} BTC")
    print(f"Ø BTC am Ende:                         {np.mean(btc_vals):.6f}")
    print(f"Ø BTC-Äquivalent (BTC+Cash/Preis):     {np.mean(equiv_vals):.6f}")
    print(f"Median BTC-Äquivalent:                 {np.median(equiv_vals):.6f}")
    print(f"Min BTC-Äquivalent:                    {np.min(equiv_vals):.6f}")
    print(f"Max BTC-Äquivalent:                    {np.max(equiv_vals):.6f}")
    print(f"Episoden mit btc_equiv > HODL:         "
          f"{np.mean(equiv_vals > btc_hodl) * 100:.1f}%")

    n = len(equiv_vals)
    split = max(1, n // 5)
    early = equiv_vals[:split]
    late = equiv_vals[-split:]
    print(f"\nLernfortschritt:")
    print(f"  Erste  {split} Episoden Ø btc_equiv: {np.mean(early):.6f}")
    print(f"  Letzte {split} Episoden Ø btc_equiv: {np.mean(late):.6f}")
    delta = np.mean(late) - np.mean(early)
    print(f"  Veränderung:                         {delta:+.6f} "
          f"({'↑ Lernerfolg' if delta > 0 else '↓ Regression'})")

    exp = load_experience()
    success = failure = draw = 0
    for (chain, result), count in exp.items():
        if result == "success":
            success += count
        elif result == "failure":
            failure += count
        elif result == "draw":
            draw += count

    total = success + failure + draw
    print(f"\nErfahrungszähler (merged):")
    print(f"  success: {success} ({(success / total * 100 if total > 0 else 0):.1f}%)")
    print(f"  failure: {failure} ({(failure / total * 100 if total > 0 else 0):.1f}%)")
    print(f"  draw:    {draw} ({(draw / total * 100 if total > 0 else 0):.1f}%)")


def plot_progress():
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib nicht installiert — Überspringe Plot.")
        return

    if not PROGRESS_CSV.exists():
        print("Keine training_progress.csv gefunden.")
        return

    df = pd.read_csv(PROGRESS_CSV)
    if df.empty:
        return

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(df["episode"], df["btc_equiv"], marker=".", linewidth=0.8, alpha=0.7,
             label="BTC-Äquivalent", color="tab:blue")
    ax1.plot(df["episode"], df["btc_end"], linewidth=0.5, alpha=0.5,
             label="Nur BTC", color="tab:orange")
    ax1.axhline(y=1.0, color="red", linestyle="--", alpha=0.5, label="HODL (1.0)")
    ax1.set_ylabel("BTC / BTC-Äquivalent")
    ax1.set_title("ResoTrade V9.4: Resonanzlogische Lernkurve")
    ax1.legend(fontsize="small")
    ax1.grid(True, alpha=0.2)

    window = max(1, len(df) // 10)
    ax2.plot(df["episode"],
             df["btc_equiv"].rolling(window, min_periods=1).mean(),
             linewidth=2, color="tab:blue", label=f"Ø btc_equiv (MA{window})")
    ax2.axhline(y=1.0, color="red", linestyle="--", alpha=0.5)
    ax2.set_xlabel("Episode")
    ax2.set_ylabel("BTC-Äquivalent (geglättet)")
    ax2.set_title("Lerntrend")
    ax2.legend(fontsize="small")
    ax2.grid(True, alpha=0.2)

    plt.tight_layout()
    out_png = DATA_DIR / "training_progress.png"
    plt.savefig(out_png, dpi=150)
    print(f"Plot gespeichert: {out_png}")


if __name__ == "__main__":
    train_offline(
        num_episodes=200,
        window_length=TRAINING_WINDOW_LENGTH,
        start_btc=1.0,
    )
    plot_progress()