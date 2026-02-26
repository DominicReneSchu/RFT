"""
Finaler Trade-Plot fuer ALLE Abschnitte.
Erzeugt 4 einzelne Plots + einen kombinierten Uebersichtsplot.
Nutzt den aktuellen Erfahrungsspeicher (nach Training) deterministisch.
"""
import sys
from pathlib import Path
from datetime import datetime

import numpy as np
import pandas as pd

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("matplotlib nicht installiert: pip install matplotlib")
    raise SystemExit(1)

from config import KRAKEN_FEE_PCT, HODL_SHARE, TRAINING_WINDOW_LENGTH
from env import TradingEnv
from experience import load_experience, EXPERIENCE_CSV
from policy import resonance_learning_policy, make_chain
from data_loader import load_analysis_signals

DATA_DIR = Path("data")

# Die 4 Trainings-Abschnitte
SECTIONS = [
    {"name": "Abschnitt 4", "label": "Sideways + ETF", "start": "2024-03-01", "end": "2024-09-01"},
    {"name": "Abschnitt 3", "label": "Bullrun 60k-110k", "start": "2024-09-01", "end": "2025-03-01"},
    {"name": "Abschnitt 2", "label": "Top + Korrektur",  "start": "2025-03-01", "end": "2025-09-01"},
    {"name": "Abschnitt 1", "label": "Aktuell",          "start": "2025-09-01", "end": "2026-02-23"},
]


def prepare_section_df(start: str, end: str) -> pd.DataFrame:
    """
    Laedt die passende signals_with_posteriors_*.csv fuer einen Abschnitt.
    Sucht in data/ UND resonance_output_v2/.
    Behandelt Timezone-aware vs naive Datetime korrekt.
    """
    search_dirs = [
        DATA_DIR,
        Path("resonance_output_v2"),
    ]

    signal_files = []
    for d in search_dirs:
        if d.exists():
            signal_files.extend(sorted(d.glob("signals_with_posteriors_*.csv")))

    if not signal_files:
        raise FileNotFoundError(
            "Keine signals_with_posteriors_*.csv gefunden.\n"
            "Gesucht in: " + ", ".join(str(d) for d in search_dirs)
        )

    start_dt = pd.to_datetime(start, utc=True)
    end_dt = pd.to_datetime(end, utc=True)

    best_file = None
    best_overlap = 0

    for f in signal_files:
        try:
            df_tmp = pd.read_csv(f, nrows=5)
            dt_col = None
            for col in ["Datetime", "Unnamed: 0"]:
                if col in df_tmp.columns:
                    dt_col = col
                    break
            if dt_col is None:
                continue

            # Volle Datei laden fuer min/max
            dt_series = pd.read_csv(f, usecols=[dt_col])[dt_col]
            dt_parsed = pd.to_datetime(dt_series, utc=True)
            file_start = dt_parsed.min()
            file_end = dt_parsed.max()

            overlap_start = max(file_start, start_dt)
            overlap_end = min(file_end, end_dt)
            overlap = max(0, (overlap_end - overlap_start).total_seconds())

            if overlap > best_overlap:
                best_overlap = overlap
                best_file = f
                best_dt_col = dt_col

        except Exception as e:
            print(f"  [Debug] Fehler bei {f.name}: {e}")
            continue

    if best_file is None:
        raise FileNotFoundError(
            f"Keine passende Signal-Datei fuer {start} - {end} gefunden.\n"
            f"Gefundene Dateien: {[f.name for f in signal_files]}\n"
            f"Bitte: python resonance_analysis.py --start {start} --end {end}"
        )

    print(f"[Data] Lade: {best_file} (Overlap: {best_overlap/3600:.0f}h)")
    df = pd.read_csv(best_file)

    # Datetime-Spalte normalisieren
    if best_dt_col != "Datetime":
        df = df.rename(columns={best_dt_col: "Datetime"})

    df["Datetime"] = pd.to_datetime(df["Datetime"], utc=True)

    # Nach Zeitraum filtern
    mask = (df["Datetime"] >= start_dt) & (df["Datetime"] < end_dt)
    df = df[mask].reset_index(drop=True)

    if len(df) == 0:
        raise ValueError(
            f"Keine Daten fuer {start} - {end} in {best_file.name}."
        )

    df["price"] = df["price"].astype(float)

    if "ma_short" not in df.columns:
        df["ma_short"] = df["price"].rolling(7, min_periods=1).mean()
    if "ma_long" not in df.columns:
        df["ma_long"] = df["price"].rolling(50, min_periods=1).mean()
    if "trend_bin" not in df.columns:
        diff = (df["ma_short"] - df["ma_long"]) / (df["ma_long"].abs() + 1e-8)
        df["trend_bin"] = diff.apply(
            lambda x: "uptrend" if x > 0.01 else ("downtrend" if x < -0.01 else "sideways")
        )

    print(f"[Data] {best_file.name}: {len(df)} Zeilen fuer {start} - {end}")
    return df

    print(f"[Data] Lade: {best_file}")
    df = pd.read_csv(best_file)

    # Datetime-Spalte finden und normalisieren
    dt_col = None
    if "Datetime" in df.columns:
        dt_col = "Datetime"
    elif "Unnamed: 0" in df.columns:
        dt_col = "Unnamed: 0"
    else:
        # Index war Datetime → reset_index hat ihn als erste Spalte
        first_col = df.columns[0]
        try:
            pd.to_datetime(df[first_col].iloc[0])
            dt_col = first_col
        except Exception:
            pass

    if dt_col and dt_col != "Datetime":
        df = df.rename(columns={dt_col: "Datetime"})

    df["Datetime"] = pd.to_datetime(df["Datetime"])

    # Nach Zeitraum filtern
    mask = (df["Datetime"] >= start_dt) & (df["Datetime"] < end_dt)
    df = df[mask].reset_index(drop=True)

    if len(df) == 0:
        raise ValueError(
            f"Keine Daten fuer {start} - {end} in {best_file.name}.\n"
            f"Bitte: python resonance_analysis.py --start {start} --end {end}"
        )

    df["price"] = df["price"].astype(float)

    if "ma_short" not in df.columns:
        df["ma_short"] = df["price"].rolling(7, min_periods=1).mean()
    if "ma_long" not in df.columns:
        df["ma_long"] = df["price"].rolling(50, min_periods=1).mean()
    if "trend_bin" not in df.columns:
        diff = (df["ma_short"] - df["ma_long"]) / (df["ma_long"].abs() + 1e-8)
        df["trend_bin"] = diff.apply(
            lambda x: "uptrend" if x > 0.01 else ("downtrend" if x < -0.01 else "sideways")
        )

    print(f"[Data] {best_file.name}: {len(df)} Zeilen fuer {start} - {end}")
    return df


def run_section_episode(df: pd.DataFrame, exp: dict):
    """Eine deterministische Episode ueber einen Abschnitt."""
    total_rows = len(df)

    start_btc = 1.0
    start_cash_share = 0.2
    start_price = float(df["price"].iloc[0])
    start_value_usd = start_btc * start_price
    start_cash = start_value_usd * start_cash_share
    start_btc_effective = (start_value_usd * (1.0 - start_cash_share)) / start_price
    hodl_core_btc = start_btc_effective * HODL_SHARE

    env = TradingEnv(
        df,
        start_btc=start_btc_effective,
        start_cash=start_cash,
        fee_pct=KRAKEN_FEE_PCT,
        price_col="price",
        trend_col="trend_bin",
        trade_fraction_small=0.10,
        trade_fraction_medium=0.25,
        ath_buffer_pct=0.0,
        window_length=total_rows - 1,
        hodl_core_btc=hodl_core_btc,
        min_btc_for_full_sell=0.1,
        min_btc_trade_fraction=0.05,
    )

    state = env.reset()

    prices = []
    btc_equivs = []
    buys_small = {"idx": [], "price": []}
    buys_medium = {"idx": [], "price": []}
    sells_small = {"idx": [], "price": []}
    sells_medium = {"idx": [], "price": []}

    step = 0
    while True:
        price = float(state.get("price", 0.0))
        btc = env.current_portfolio().btc
        cash = env.current_portfolio().cash
        btc_equiv = btc + (cash / price if price > 0 else 0)

        prices.append(price)
        btc_equivs.append(btc_equiv)

        btc_before = btc
        action = resonance_learning_policy(state, exp, epsilon=0.0)
        next_state, done = env.step(action)

        btc_after = env.current_portfolio().btc
        delta_btc = btc_after - btc_before

        if abs(delta_btc) > 1e-10:
            if delta_btc > 0:
                if "MEDIUM" in action:
                    buys_medium["idx"].append(step)
                    buys_medium["price"].append(price)
                else:
                    buys_small["idx"].append(step)
                    buys_small["price"].append(price)
            else:
                if "MEDIUM" in action:
                    sells_medium["idx"].append(step)
                    sells_medium["price"].append(price)
                else:
                    sells_small["idx"].append(step)
                    sells_small["price"].append(price)

        step += 1
        if done:
            price = float(next_state.get("price", price))
            btc = env.current_portfolio().btc
            cash = env.current_portfolio().cash
            btc_equiv = btc + (cash / price if price > 0 else 0)
            prices.append(price)
            btc_equivs.append(btc_equiv)
            break
        state = next_state

    return {
        "prices": prices,
        "btc_equivs": btc_equivs,
        "buys_small": buys_small,
        "buys_medium": buys_medium,
        "sells_small": sells_small,
        "sells_medium": sells_medium,
        "start_btc": start_btc_effective,
    }


def plot_single_section(result: dict, section: dict, out_path: Path):
    """Einzelplot fuer einen Abschnitt."""
    prices = result["prices"]
    btc_equivs = result["btc_equivs"]
    buys_s = result["buys_small"]
    buys_m = result["buys_medium"]
    sells_s = result["sells_small"]
    sells_m = result["sells_medium"]
    start_btc = result["start_btc"]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True,
                                    gridspec_kw={"height_ratios": [3, 1]})
    x = np.arange(len(prices))

    ax1.plot(x, prices, color="#444444", linewidth=0.6, alpha=0.8, label="BTC Preis")

    if buys_s["idx"]:
        ax1.scatter(buys_s["idx"], buys_s["price"],
                    marker="^", color="#2ecc71", s=30, alpha=0.8,
                    label=f"BUY small ({len(buys_s['idx'])})", zorder=5)
    if buys_m["idx"]:
        ax1.scatter(buys_m["idx"], buys_m["price"],
                    marker="^", color="#006400", s=60, alpha=0.9,
                    label=f"BUY medium ({len(buys_m['idx'])})", zorder=5)
    if sells_s["idx"]:
        ax1.scatter(sells_s["idx"], sells_s["price"],
                    marker="v", color="#e74c3c", s=30, alpha=0.8,
                    label=f"SELL small ({len(sells_s['idx'])})", zorder=5)
    if sells_m["idx"]:
        ax1.scatter(sells_m["idx"], sells_m["price"],
                    marker="v", color="#8b0000", s=60, alpha=0.9,
                    label=f"SELL medium ({len(sells_m['idx'])})", zorder=5)

    total_trades = (len(buys_s["idx"]) + len(buys_m["idx"]) +
                    len(sells_s["idx"]) + len(sells_m["idx"]))
    total_buys = len(buys_s["idx"]) + len(buys_m["idx"])
    total_sells = len(sells_s["idx"]) + len(sells_m["idx"])

    ax1.set_ylabel("BTC Preis (USD)")
    ax1.set_title(f"ResoTrade V11.1 -- {section['name']}: {section['label']}\n"
                  f"{section['start']} bis {section['end']} | "
                  f"{total_trades} Trades ({total_buys} Buys, {total_sells} Sells)")
    ax1.legend(loc="upper left", fontsize=8)
    ax1.grid(True, alpha=0.3)

    ax2.plot(x[:len(btc_equivs)], btc_equivs, color="#2980b9", linewidth=1.0,
             label="BTC-Aequivalent (Bot)")
    ax2.axhline(y=start_btc, color="#e67e22", linewidth=1.0, linestyle="--",
                label=f"HODL ({start_btc:.4f} BTC)")

    final_equiv = btc_equivs[-1] if btc_equivs else start_btc
    performance = ((final_equiv / start_btc) - 1) * 100

    ax2.set_ylabel("BTC-Aequivalent")
    ax2.set_xlabel("Step (Stunden)")
    ax2.set_title(f"Performance: {final_equiv:.6f} BTC-equiv ({performance:+.2f}% vs HODL)")
    ax2.legend(loc="upper left", fontsize=8)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"  Plot gespeichert: {out_path}")


def plot_combined(all_results: list, sections: list):
    """Kombinierter 4x2-Plot: Alle Abschnitte untereinander."""
    n = len(all_results)
    fig, axes = plt.subplots(n, 2, figsize=(20, 5 * n),
                              gridspec_kw={"width_ratios": [3, 1]})

    if n == 1:
        axes = [axes]

    for i, (result, section) in enumerate(zip(all_results, sections)):
        prices = result["prices"]
        btc_equivs = result["btc_equivs"]
        buys_s = result["buys_small"]
        buys_m = result["buys_medium"]
        sells_s = result["sells_small"]
        sells_m = result["sells_medium"]
        start_btc = result["start_btc"]

        ax_price = axes[i][0]
        ax_equiv = axes[i][1]

        x = np.arange(len(prices))

        # Preis + Trades
        ax_price.plot(x, prices, color="#444444", linewidth=0.5, alpha=0.8)
        if buys_s["idx"]:
            ax_price.scatter(buys_s["idx"], buys_s["price"],
                             marker="^", color="#2ecc71", s=20, alpha=0.7, zorder=5)
        if buys_m["idx"]:
            ax_price.scatter(buys_m["idx"], buys_m["price"],
                             marker="^", color="#006400", s=40, alpha=0.8, zorder=5)
        if sells_s["idx"]:
            ax_price.scatter(sells_s["idx"], sells_s["price"],
                             marker="v", color="#e74c3c", s=20, alpha=0.7, zorder=5)
        if sells_m["idx"]:
            ax_price.scatter(sells_m["idx"], sells_m["price"],
                             marker="v", color="#8b0000", s=40, alpha=0.8, zorder=5)

        total = (len(buys_s["idx"]) + len(buys_m["idx"]) +
                 len(sells_s["idx"]) + len(sells_m["idx"]))

        final_equiv = btc_equivs[-1] if btc_equivs else start_btc
        perf = ((final_equiv / start_btc) - 1) * 100

        ax_price.set_title(f"{section['name']}: {section['label']} "
                           f"({section['start']} - {section['end']})\n"
                           f"{total} Trades | {perf:+.1f}% vs HODL",
                           fontsize=10)
        ax_price.set_ylabel("USD")
        ax_price.grid(True, alpha=0.2)

        # BTC-Aequivalent
        ax_equiv.plot(x[:len(btc_equivs)], btc_equivs, color="#2980b9", linewidth=1.0)
        ax_equiv.axhline(y=start_btc, color="#e67e22", linewidth=1.0, linestyle="--")
        ax_equiv.set_title(f"{perf:+.1f}% vs HODL", fontsize=10)
        ax_equiv.set_ylabel("BTC-eq")
        ax_equiv.grid(True, alpha=0.2)

        if i == n - 1:
            ax_price.set_xlabel("Step (Stunden)")
            ax_equiv.set_xlabel("Step")

    plt.suptitle("ResoTrade V11.1 -- Alle Abschnitte (deterministische Policy)",
                 fontsize=14, fontweight="bold", y=1.01)
    plt.tight_layout()

    out_path = DATA_DIR / "final_trades_all_combined.png"
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\nKombinierter Plot gespeichert: {out_path}")


def main():
    print("=" * 60)
    print("FINALER TRADE-PLOT -- Alle 4 Abschnitte (epsilon=0)")
    print("=" * 60)

    # Erfahrungsspeicher laden
    if not EXPERIENCE_CSV.exists():
        print(f"Kein Erfahrungsspeicher: {EXPERIENCE_CSV}")
        print("Bitte erst trainieren: python main.py 10 500")
        raise SystemExit(1)

    exp = load_experience(path=EXPERIENCE_CSV)
    print(f"[Plot] Erfahrungsspeicher: {len(exp)} Eintraege\n")

    all_results = []
    summary = []

    for section in SECTIONS:
        print(f"\n--- {section['name']}: {section['label']} ---")
        print(f"    Zeitraum: {section['start']} bis {section['end']}")

        try:
            df = prepare_section_df(section["start"], section["end"])
        except (FileNotFoundError, ValueError) as e:
            print(f"    UEBERSPRUNGEN: {e}")
            continue

        result = run_section_episode(df, exp)
        all_results.append(result)

        # Einzelplot
        safe_name = section["name"].lower().replace(" ", "_")
        out_path = DATA_DIR / f"final_trades_{safe_name}.png"
        plot_single_section(result, section, out_path)

        # Statistik
        start_btc = result["start_btc"]
        final_equiv = result["btc_equivs"][-1] if result["btc_equivs"] else start_btc
        perf = ((final_equiv / start_btc) - 1) * 100
        total_trades = (len(result["buys_small"]["idx"]) +
                        len(result["buys_medium"]["idx"]) +
                        len(result["sells_small"]["idx"]) +
                        len(result["sells_medium"]["idx"]))

        summary.append({
            "section": section["name"],
            "label": section["label"],
            "period": f"{section['start']} - {section['end']}",
            "steps": len(result["prices"]),
            "trades": total_trades,
            "start_btc": start_btc,
            "end_btc_equiv": final_equiv,
            "performance": perf,
        })

    # Kombinierter Plot (nur fuer erfolgreich geladene Abschnitte)
    if len(all_results) > 1:
        successful_sections = [s for s in SECTIONS
                               if any(s["name"] == sm["section"] for sm in summary)]
        plot_combined(all_results, successful_sections)

    # Zusammenfassung
    print("\n" + "=" * 70)
    print("ZUSAMMENFASSUNG")
    print("=" * 70)
    print(f"{'Abschnitt':<15} {'Zeitraum':<25} {'Trades':>7} "
          f"{'Start':>10} {'Ende':>10} {'vs HODL':>10}")
    print("-" * 70)

    total_perf = 0
    for s in summary:
        print(f"{s['section']:<15} {s['period']:<25} {s['trades']:>7} "
              f"{s['start_btc']:>10.4f} {s['end_btc_equiv']:>10.4f} "
              f"{s['performance']:>+9.2f}%")
        total_perf += s["performance"]

    if summary:
        avg_perf = total_perf / len(summary)
        print("-" * 70)
        print(f"{'Durchschnitt':<15} {'':<25} {'':<7} "
              f"{'':>10} {'':>10} {avg_perf:>+9.2f}%")

    print("=" * 70)


if __name__ == "__main__":
    main()