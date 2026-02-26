"""
Auswertung der Live-Signal-Logs mit Portfolio-Simulation und Plot.

V9.4: Imports direkt aus config (nicht aus live_signal).
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from experience import merge_status
from config import HODL_SHARE, TRADE_FRACTION_SMALL, TRADE_FRACTION_MEDIUM, KRAKEN_FEE_PCT
from kraken_client import KrakenClient

df = pd.read_csv("data/live_logs/signal_log.csv")
print(f"Zyklen: {len(df)}")

ts_first = str(df.iloc[0]["timestamp"])[:16]
ts_last = str(df.iloc[-1]["timestamp"])[:16]
print(f"Zeitraum: {ts_first} bis {ts_last}")

if "skipped" in df.columns:
    active = len(df[df["skipped"] != "yes"])
    skipped = len(df[df["skipped"] == "yes"])
    total = active + skipped
    print(f"Aktiv: {active}, Skip: {skipped}, Nutzrate: {active/total*100:.0f}%")

print(f"\nAktionen:")
print(df["final_action"].value_counts().to_string())

print(f"\nTrend-Verteilung:")
print(df["trend"].value_counts().to_string())

print(f"\nAktion x Trend:")
print(pd.crosstab(df["final_action"], df["trend"]).to_string())

buys = df[df["final_action"].str.startswith("BUY")]
sells = df[df["final_action"].str.startswith("SELL")]

if len(buys) > 0:
    avg_e = buys["e_long"].astype(float).mean()
    print(f"\nBUYs: {len(buys)}, Avg e_long: {avg_e:.4f}")
if len(sells) > 0:
    avg_e = sells["e_long"].astype(float).mean()
    print(f"SELLs: {len(sells)}, Avg e_long: {avg_e:.4f}")

# Divergenz-Check
if "rule_action" in df.columns and "final_action" in df.columns:
    active_df = df[df.get("skipped", "no") != "yes"] if "skipped" in df.columns else df
    divergent_active = active_df[active_df["rule_action"] != active_df["final_action"]]
    print(f"\nRegel-Policy-Divergenz:")
    print(f"  Aktiv: {len(divergent_active)} von {len(active_df)} ({len(divergent_active)/len(active_df)*100:.1f}%)")
    if len(divergent_active) > 0:
        print(f"  Muster:")
        pairs = divergent_active.groupby(["rule_action", "final_action"]).size()
        for (rule, final), count in pairs.items():
            print(f"    {rule:14s} -> {final:14s}: {count}")

if "live_eval" in df.columns:
    evals = df["live_eval"].value_counts().to_dict()
    s = evals.get("success", 0)
    f = evals.get("failure", 0)
    d = evals.get("draw", 0)
    total_eval = s + f + d
    if total_eval > 0:
        print(f"\nLive-Lernen ({total_eval} Bewertungen):")
        print(f"  success: {s} ({s/total_eval*100:.1f}%)")
        print(f"  failure: {f} ({f/total_eval*100:.1f}%)")
        print(f"  draw:    {d} ({d/total_eval*100:.1f}%)")
        if f > 0:
            print(f"  S:F = {s/f:.2f}:1")


# ============================================================
# PORTFOLIO-SIMULATION
# ============================================================

print(f"\n{'=' * 60}")
print(f"PORTFOLIO-SIMULATION (Dry-Run -> simulierte Ausführung)")
print(f"{'=' * 60}")

# Echtes Portfolio
try:
    client = KrakenClient()
    real_btc, real_usd = client.get_btc_usd_balance()
    ticker = client.get_ticker()
    current_price = ticker["last"]
    print(f"\nEchtes Portfolio (jetzt):")
    print(f"  BTC: {real_btc:.8f}")
    print(f"  USD: {real_usd:.2f}")
    print(f"  Preis: {current_price:.2f}")
    print(f"  Total: {real_btc * current_price + real_usd:.2f} USD")
except Exception as e:
    print(f"\nKraken nicht erreichbar: {e}")

# Startpunkt
first_active = df[df.get("skipped", "no") != "yes"].iloc[0] if "skipped" in df.columns else df.iloc[0]
start_btc = float(first_active["btc_balance"])
start_usd = float(first_active["usd_balance"])
start_price = float(first_active["price"])
start_total_usd = start_btc * start_price + start_usd
start_btc_equiv = start_btc + start_usd / start_price

print(f"\nStartpunkt (erster Log-Eintrag):")
print(f"  BTC: {start_btc:.8f}")
print(f"  USD: {start_usd:.2f}")
print(f"  Preis: {start_price:.2f}")
print(f"  BTC-Äquivalent: {start_btc_equiv:.8f}")

# Simulation mit Zeitreihe
sim_btc = start_btc
sim_usd = start_usd
hodl_btc = start_btc
hodl_usd = start_usd

# V9.4: Fester HODL-Kern (schrumpft nicht mit Verkäufen)
hodl_core_fixed = start_btc * HODL_SHARE
print(f"  HODL-Kern (fest): {hodl_core_fixed:.8f} BTC")

# V9.4: Fairer Benchmark — alles in BTC zum Startpreis
allin_btc = start_btc + (start_usd / start_price if start_price > 0 else 0)
print(f"  All-In-BTC Benchmark: {allin_btc:.8f} BTC")

trade_log = []
num_buys = 0
num_sells = 0
total_fees_usd = 0.0

# Zeitreihen für Plot
timestamps = []
delta_btc_equiv_series = []
price_series = []
sim_btc_equiv_series = []
hodl_btc_equiv_series = []
trade_markers = []  # (ts, action, price)

active_rows = df[df.get("skipped", "no") != "yes"] if "skipped" in df.columns else df

for _, row in active_rows.iterrows():
    action = str(row["final_action"])
    price = float(row["price"])
    ts = pd.to_datetime(row["timestamp"])
    hodl_core = hodl_core_fixed  # V9.4: Fester Kern statt zirkulär

    if action in ("BUY_SMALL", "BUY_MEDIUM"):
        fraction = TRADE_FRACTION_SMALL if action == "BUY_SMALL" else TRADE_FRACTION_MEDIUM
        spend_usd = sim_usd * fraction
        if spend_usd > 5.0 and price > 0:
            fee_usd = spend_usd * KRAKEN_FEE_PCT
            btc_bought = (spend_usd - fee_usd) / price
            sim_usd -= spend_usd
            sim_btc += btc_bought
            total_fees_usd += fee_usd
            num_buys += 1
            trade_markers.append((ts, "BUY", price))
            trade_log.append({
                "ts": row["timestamp"], "action": action, "price": price,
                "btc_delta": btc_bought, "usd_delta": -spend_usd,
                "fee_usd": fee_usd, "sim_btc": sim_btc, "sim_usd": sim_usd,
                "e_long": float(row.get("e_long", 0)),
                "trend": str(row.get("trend", "?")),
            })

    elif action in ("SELL_SMALL", "SELL_MEDIUM"):
        fraction = TRADE_FRACTION_SMALL if action == "SELL_SMALL" else TRADE_FRACTION_MEDIUM
        free_btc = max(0.0, sim_btc - hodl_core)
        btc_to_sell = free_btc * fraction
        if btc_to_sell > 0.0001 and price > 0:
            gross_usd = btc_to_sell * price
            fee_usd = gross_usd * KRAKEN_FEE_PCT
            net_usd = gross_usd - fee_usd
            sim_btc -= btc_to_sell
            sim_usd += net_usd
            total_fees_usd += fee_usd
            num_sells += 1
            trade_markers.append((ts, "SELL", price))
            trade_log.append({
                "ts": row["timestamp"], "action": action, "price": price,
                "btc_delta": -btc_to_sell, "usd_delta": net_usd,
                "fee_usd": fee_usd, "sim_btc": sim_btc, "sim_usd": sim_usd,
                "e_long": float(row.get("e_long", 0)),
                "trend": str(row.get("trend", "?")),
            })

    # Zeitreihe aufzeichnen
    sim_btc_eq = sim_btc + sim_usd / price if price > 0 else sim_btc
    hodl_btc_eq = hodl_btc + hodl_usd / price if price > 0 else hodl_btc
    delta = sim_btc_eq - hodl_btc_eq
    delta_pct = (delta / hodl_btc_eq * 100) if hodl_btc_eq > 0 else 0

    timestamps.append(ts)
    delta_btc_equiv_series.append(delta_pct)
    price_series.append(price)
    sim_btc_equiv_series.append(sim_btc_eq)
    hodl_btc_equiv_series.append(hodl_btc_eq)

# Endwerte
end_price = float(df.iloc[-1]["price"])
sim_total_usd = sim_btc * end_price + sim_usd
sim_btc_equiv = sim_btc + sim_usd / end_price
hodl_total_usd = hodl_btc * end_price + hodl_usd
hodl_btc_equiv = hodl_btc + hodl_usd / end_price
delta_btc_equiv = sim_btc_equiv - hodl_btc_equiv
delta_pct_final = (delta_btc_equiv / hodl_btc_equiv * 100) if hodl_btc_equiv > 0 else 0
delta_usd = sim_total_usd - hodl_total_usd

# V9.4: Fairer Benchmark — All-In-BTC
allin_btc_equiv = allin_btc  # BTC-Menge ändert sich nie
delta_vs_allin = sim_btc_equiv - allin_btc_equiv
delta_vs_allin_pct = (delta_vs_allin / allin_btc_equiv * 100) if allin_btc_equiv > 0 else 0

print(f"\n{'─' * 50}")
print(f"SIMULATION: {num_buys} BUYs + {num_sells} SELLs = {num_buys + num_sells} Trades")
print(f"{'─' * 50}")

print(f"\n  Simuliertes Portfolio (Ende):")
print(f"    BTC:            {sim_btc:.8f}")
print(f"    USD:            {sim_usd:.2f}")
print(f"    Total USD:      {sim_total_usd:.2f}")
print(f"    BTC-Äquivalent: {sim_btc_equiv:.8f}")

print(f"\n  HODL-Benchmark (Start gehalten):")
print(f"    BTC:            {hodl_btc:.8f}")
print(f"    USD:            {hodl_usd:.2f}")
print(f"    Total USD:      {hodl_total_usd:.2f}")
print(f"    BTC-Äquivalent: {hodl_btc_equiv:.8f}")

print(f"\n  Performance vs. HODL (BTC+USD gehalten):")
print(f"    Δ BTC-Äquivalent: {delta_btc_equiv:+.8f} ({delta_pct_final:+.4f}%)")
print(f"    Δ USD:            {delta_usd:+.2f}")

print(f"\n  Performance vs. All-In-BTC (fairer Benchmark):")
print(f"    Δ BTC-Äquivalent: {delta_vs_allin:+.8f} ({delta_vs_allin_pct:+.4f}%)")

print(f"\n  Kosten:")
print(f"    Fees bezahlt:     {total_fees_usd:.2f} USD")

print(f"\n  Preisentwicklung:")
print(f"    Start: {start_price:.2f}")
print(f"    Ende:  {end_price:.2f}")
price_change = (end_price - start_price) / start_price * 100
print(f"    Δ:     {price_change:+.2f}%")

# Trade-Details
if trade_log:
    tdf = pd.DataFrame(trade_log)

    print(f"\n{'─' * 50}")
    print(f"TRADE-DETAILS")
    print(f"{'─' * 50}")

    buy_trades = tdf[tdf["action"].str.startswith("BUY")]
    sell_trades = tdf[tdf["action"].str.startswith("SELL")]

    if len(buy_trades) > 0:
        avg_buy_price = (buy_trades["usd_delta"].abs() / buy_trades["btc_delta"]).mean()
        total_btc_bought = buy_trades["btc_delta"].sum()
        total_usd_spent = buy_trades["usd_delta"].abs().sum()
        print(f"\n  Käufe:")
        print(f"    Anzahl:         {len(buy_trades)}")
        print(f"    BTC gekauft:    {total_btc_bought:.8f}")
        print(f"    USD ausgegeben: {total_usd_spent:.2f}")
        print(f"    Ø Kaufpreis:    {avg_buy_price:.2f}")
        print(f"    Ø e_long:       {buy_trades['e_long'].mean():.4f}")
        print(f"    Trends:         {buy_trades['trend'].value_counts().to_dict()}")

    if len(sell_trades) > 0:
        avg_sell_price = (sell_trades["usd_delta"] / sell_trades["btc_delta"].abs()).mean()
        total_btc_sold = sell_trades["btc_delta"].abs().sum()
        total_usd_received = sell_trades["usd_delta"].sum()
        print(f"\n  Verkäufe:")
        print(f"    Anzahl:         {len(sell_trades)}")
        print(f"    BTC verkauft:   {total_btc_sold:.8f}")
        print(f"    USD erhalten:   {total_usd_received:.2f}")
        print(f"    Ø Verkaufpreis: {avg_sell_price:.2f}")
        print(f"    Ø e_long:       {sell_trades['e_long'].mean():.4f}")
        print(f"    Trends:         {sell_trades['trend'].value_counts().to_dict()}")

    if len(buy_trades) > 0 and len(sell_trades) > 0:
        spread = avg_sell_price - avg_buy_price
        spread_pct = spread / avg_buy_price * 100 if avg_buy_price > 0 else 0
        print(f"\n  Spread Verkauf-Kauf:")
        print(f"    Ø Sell - Ø Buy: {spread:+.2f} USD ({spread_pct:+.2f}%)")

    # Trade-Chronologie
    print(f"\n{'─' * 50}")
    print(f"TRADE-CHRONOLOGIE (letzte 20)")
    print(f"{'─' * 50}")
    show = tdf.tail(20)
    for _, t in show.iterrows():
        ts_short = str(t["ts"])[11:16]
        act = t["action"]
        if act.startswith("BUY"):
            symbol = "🟢"
            detail = f"+{t['btc_delta']:.6f} BTC | -{abs(t['usd_delta']):.0f} USD"
        else:
            symbol = "🔴"
            detail = f"-{abs(t['btc_delta']):.6f} BTC | +{t['usd_delta']:.0f} USD"
        print(f"  {ts_short} {symbol} {act:12s} @ {t['price']:.0f} | {detail} | e={t['e_long']:.3f} {t['trend']}")

else:
    print(f"\n  Keine Trades im Zeitraum — reine HOLD-Phase.")

# ============================================================
# PLOT: Performance-Grafik
# ============================================================

if len(timestamps) >= 2:
    fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True,
                             gridspec_kw={"height_ratios": [2, 1, 1]})

    ts_arr = pd.to_datetime(timestamps)
    delta_arr = np.array(delta_btc_equiv_series)
    price_arr = np.array(price_series)
    sim_arr = np.array(sim_btc_equiv_series)
    hodl_arr = np.array(hodl_btc_equiv_series)

    # --- Panel 1: Δ BTC-Äquivalent vs. HODL ---
    ax1 = axes[0]
    ax1.fill_between(ts_arr, 0, delta_arr,
                     where=(delta_arr >= 0), color="green", alpha=0.3, label="über HODL")
    ax1.fill_between(ts_arr, 0, delta_arr,
                     where=(delta_arr < 0), color="red", alpha=0.3, label="unter HODL")
    ax1.plot(ts_arr, delta_arr, color="black", linewidth=1.5)
    ax1.axhline(y=0, color="gray", linestyle="--", linewidth=0.8)

    # Trade-Marker
    for t_ts, t_act, t_price in trade_markers:
        idx = ts_arr.searchsorted(t_ts)
        idx = min(idx, len(delta_arr) - 1)
        if t_act == "BUY":
            ax1.scatter(t_ts, delta_arr[idx], marker="^", color="green",
                        s=80, edgecolors="black", zorder=5)
        else:
            ax1.scatter(t_ts, delta_arr[idx], marker="v", color="red",
                        s=80, edgecolors="black", zorder=5)

    ax1.set_ylabel("Δ BTC-Äquiv. vs. HODL (%)")
    ax1.set_title(f"ResoTrade V11 — Live-Performance  |  "
                  f"vs HODL: {delta_pct_final:+.4f}%  |  "
                  f"vs All-In: {delta_vs_allin_pct:+.4f}%  |  "
                  f"{num_buys} BUYs + {num_sells} SELLs  |  "
                  f"Fees: {total_fees_usd:.2f} USD")
    ax1.legend(loc="upper left", fontsize="small")
    ax1.grid(True, alpha=0.3)

    # --- Panel 2: BTC-Äquivalent absolut ---
    ax2 = axes[1]
    ax2.plot(ts_arr, sim_arr, color="blue", linewidth=1.2, label="Simuliert")
    ax2.plot(ts_arr, hodl_arr, color="gray", linewidth=1.0, linestyle="--", label="HODL")
    ax2.set_ylabel("BTC-Äquivalent")
    ax2.legend(loc="upper left", fontsize="small")
    ax2.grid(True, alpha=0.3)

    # --- Panel 3: BTC-Preis ---
    ax3 = axes[2]
    ax3.plot(ts_arr, price_arr, color="orange", linewidth=1.0)

    for t_ts, t_act, t_price in trade_markers:
        if t_act == "BUY":
            ax3.scatter(t_ts, t_price, marker="^", color="green",
                        s=60, edgecolors="black", zorder=5)
        else:
            ax3.scatter(t_ts, t_price, marker="v", color="red",
                        s=60, edgecolors="black", zorder=5)

    ax3.set_ylabel("BTC/USD")
    ax3.set_xlabel("Zeit")
    ax3.grid(True, alpha=0.3)

    plt.xticks(rotation=30)
    fig.tight_layout()

    out_path = Path("data/live_logs/performance.png")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\n📊 Performance-Plot gespeichert: {out_path}")

else:
    print(f"\nZu wenig Datenpunkte für Plot ({len(timestamps)}).")

print(f"\nSpeicher-Status:")
merge_status()