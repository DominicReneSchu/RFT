"""
Finaler Trade-Plot: Zeigt wie der Bot mit gelernter Erfahrung handeln würde.
Eine deterministische Episode über den gesamten Datensatz (epsilon=0).
"""
from pathlib import Path
import pandas as pd
import numpy as np

try:
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
except ImportError:
    print("matplotlib nicht installiert: pip install matplotlib")
    raise SystemExit(1)

from config import KRAKEN_FEE_PCT, HODL_SHARE
from train_offline import prepare_price_df_from_analysis
from env import TradingEnv
from experience import load_experience, EXPERIENCE_CSV
from policy import resonance_learning_policy, make_chain

DATA_DIR = Path("data")


def run_final_episode():
    """Eine Episode über den GESAMTEN Datensatz, epsilon=0."""
    df = prepare_price_df_from_analysis()
    total_rows = len(df)

    # Erfahrungsspeicher laden (merged/weighted)
    exp_path = EXPERIENCE_CSV
    if not exp_path.exists():
        print(f"Kein Erfahrungsspeicher gefunden: {exp_path}")
        print("Bitte erst trainieren: python main.py 10 500")
        raise SystemExit(1)

    exp = load_experience(path=exp_path)
    print(f"[Plot] Erfahrungsspeicher: {len(exp)} Einträge")

    # Start-Werte (wie im Training)
    start_btc = 1.0
    start_cash_share = 0.2
    start_price = float(df["price"].iloc[0])
    start_value_usd = start_btc * start_price
    start_cash = start_value_usd * start_cash_share
    start_btc_effective = (start_value_usd * (1.0 - start_cash_share)) / start_price
    hodl_core_btc = start_btc_effective * HODL_SHARE

    # Env über GESAMTEN Datensatz (window_length = alle Zeilen)
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

    # Daten sammeln
    prices = []
    timestamps = []
    buys_small = {"idx": [], "price": []}
    buys_medium = {"idx": [], "price": []}
    sells_small = {"idx": [], "price": []}
    sells_medium = {"idx": [], "price": []}
    btc_equivs = []

    step = 0
    while True:
        price = float(state.get("price", 0.0))
        btc = env.current_portfolio().btc
        cash = env.current_portfolio().cash
        btc_equiv = btc + (cash / price if price > 0 else 0)

        prices.append(price)
        btc_equivs.append(btc_equiv)

        btc_before = btc
        cash_before = cash

        # Deterministische Policy (epsilon=0)
        action = resonance_learning_policy(state, exp, epsilon=0.0)
        next_state, done = env.step(action)

        btc_after = env.current_portfolio().btc
        cash_after = env.current_portfolio().cash
        delta_btc = btc_after - btc_before

        # Effektiv ausgeführte Aktion erkennen
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

    return prices, btc_equivs, buys_small, buys_medium, sells_small, sells_medium, start_btc_effective


def plot_trades(prices, btc_equivs, buys_s, buys_m, sells_s, sells_m, start_btc_eff):
    """Zwei-Panel-Plot: BTC-Preis mit Trades + BTC-Äquivalent."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True,
                                    gridspec_kw={"height_ratios": [3, 1]})

    x = np.arange(len(prices))

    # --- Panel 1: BTC-Preis + Trades ---
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
    ax1.set_title(f"ResoTrade V11.1 — Finaler Trade-Plot (deterministische Policy)\n"
                  f"{total_trades} Trades ({total_buys} Buys, {total_sells} Sells) "
                  f"über {len(prices)} Steps")
    ax1.legend(loc="upper left", fontsize=8)
    ax1.grid(True, alpha=0.3)

    # --- Panel 2: BTC-Äquivalent vs HODL ---
    ax2.plot(x[:len(btc_equivs)], btc_equivs, color="#2980b9", linewidth=1.0,
             label="BTC-Äquivalent (Bot)")
    ax2.axhline(y=start_btc_eff, color="#e67e22", linewidth=1.0, linestyle="--",
                label=f"HODL ({start_btc_eff:.4f} BTC)")

    final_equiv = btc_equivs[-1] if btc_equivs else start_btc_eff
    performance = ((final_equiv / start_btc_eff) - 1) * 100

    ax2.set_ylabel("BTC-Äquivalent")
    ax2.set_xlabel("Step (Stunden)")
    ax2.set_title(f"Performance: {final_equiv:.6f} BTC-equiv "
                  f"({performance:+.2f}% vs HODL)")
    ax2.legend(loc="upper left", fontsize=8)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    out_path = DATA_DIR / "final_trades.png"
    DATA_DIR.mkdir(exist_ok=True)
    plt.savefig(out_path, dpi=150)
    print(f"\nPlot gespeichert: {out_path}")
    plt.close()


if __name__ == "__main__":
    print("=" * 60)
    print("FINALER TRADE-PLOT — Deterministische Policy (epsilon=0)")
    print("=" * 60)

    prices, btc_equivs, buys_s, buys_m, sells_s, sells_m, start_btc = run_final_episode()

    total = len(buys_s["idx"]) + len(buys_m["idx"]) + len(sells_s["idx"]) + len(sells_m["idx"])
    print(f"\nGesamt: {total} effektive Trades über {len(prices)} Steps")
    print(f"  BUY small:  {len(buys_s['idx'])}")
    print(f"  BUY medium: {len(buys_m['idx'])}")
    print(f"  SELL small: {len(sells_s['idx'])}")
    print(f"  SELL medium:{len(sells_m['idx'])}")

    final_equiv = btc_equivs[-1] if btc_equivs else start_btc
    print(f"\nStart: {start_btc:.6f} BTC-equiv")
    print(f"Ende:  {final_equiv:.6f} BTC-equiv")
    print(f"Performance: {((final_equiv / start_btc) - 1) * 100:+.2f}% vs HODL")

    plot_trades(prices, btc_equivs, buys_s, buys_m, sells_s, sells_m, start_btc)