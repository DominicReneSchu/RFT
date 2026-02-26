"""
Resonanzlogische Episoden-Diagnostik V9.
Erweitert um Blockade-Quellen-Analyse.
"""
import csv
from pathlib import Path

import numpy as np
import pandas as pd

DIAG_DIR = Path("data/diagnostics")
DIAG_DIR.mkdir(parents=True, exist_ok=True)


def log_episode_step(
    episode: int,
    step: int,
    state: dict,
    policy_action: str,
    effective_action: str,
    btc_before: float,
    btc_after: float,
    cash_before: float,
    cash_after: float,
    price: float,
    block_reason: str = "none",
    log_file: str = "episode_log.csv",
):
    """
    V9: Zusätzliche Spalte 'block_reason' im Log.
    """
    path = DIAG_DIR / log_file
    exists = path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow([
                "episode", "step", "price", "e_long", "e_short",
                "trend", "vol_bin", "pos",
                "policy_action", "effective_action", "block_reason",
                "btc_before", "btc_after",
                "cash_before", "cash_after",
                "delta_btc", "delta_cash",
                "total_usd_before", "total_usd_after",
            ])
        e_long = float(state.get("e_long", 0.0) or 0.0)
        e_short = float(state.get("e_short", 0.0) or 0.0)
        total_before = cash_before + btc_before * price
        total_after = cash_after + btc_after * price
        w.writerow([
            episode, step, f"{price:.2f}",
            f"{e_long:.6f}", f"{e_short:.6f}",
            state.get("trend_bin", "none"),
            state.get("vol_bin", "mid"),
            state.get("pos", "FLAT"),
            policy_action, effective_action, block_reason,
            f"{btc_before:.8f}", f"{btc_after:.8f}",
            f"{cash_before:.2f}", f"{cash_after:.2f}",
            f"{btc_after - btc_before:.8f}",
            f"{cash_after - cash_before:.2f}",
            f"{total_before:.2f}", f"{total_after:.2f}",
        ])


def summarize_episode_trades(log_file: str = "episode_log.csv"):
    """
    Resonanzlogische Episoden-Auswertung V9.
    Erweitert um Blockade-Quellen-Analyse.
    """
    path = DIAG_DIR / log_file
    if not path.exists():
        print("Kein Diagnostik-Log vorhanden.")
        return

    df = pd.read_csv(path)
    if df.empty:
        print("Diagnostik-Log ist leer.")
        return

    total = len(df)
    episodes = df["episode"].nunique()

    print(f"\nGeloggte Schritte: {total} über {episodes} Episoden")

    # --- Policy-Aktionen ---
    policy_counts = df["policy_action"].value_counts().to_dict()
    effective_counts = df["effective_action"].value_counts().to_dict()

    print(f"\nPolicy-Entscheidungen:")
    for action, count in sorted(policy_counts.items(), key=lambda x: -x[1]):
        print(f"  {action:15s}: {count:6d} ({count / total * 100:5.1f}%)")

    print(f"\nEffektiv ausgeführt:")
    for action, count in sorted(effective_counts.items(), key=lambda x: -x[1]):
        print(f"  {action:15s}: {count:6d} ({count / total * 100:5.1f}%)")

    # --- Blockade-Analyse ---
    blocked = df[df["policy_action"] != df["effective_action"]]
    print(f"\nBlockierte Trades: {len(blocked)} ({len(blocked) / max(1, total) * 100:.1f}%)")

    if not blocked.empty:
        print("\nBlockade-Muster (Policy → Effektiv):")
        pairs = blocked.groupby(["policy_action", "effective_action"]).size()
        for (pa, ea), count in pairs.items():
            print(f"  {pa:15s} → {ea:15s}: {count:5d}")

        print("\nBlockade nach Trend:")
        trend_block = blocked.groupby("trend").size()
        for trend, count in trend_block.items():
            print(f"  {trend:15s}: {count:5d}")

        # V9: Blockade-Quellen-Analyse
        if "block_reason" in df.columns:
            blocked_with_reason = df[
                (df["policy_action"] != df["effective_action"])
                & (df["block_reason"] != "none")
            ]
            if not blocked_with_reason.empty:
                print("\n--- Blockade-Quellen (V9) ---")
                reason_counts = blocked_with_reason["block_reason"].value_counts()
                for reason, count in reason_counts.items():
                    pct = count / len(blocked) * 100
                    print(f"  {reason:20s}: {count:5d} ({pct:5.1f}% der Blockaden)")

                # Blockade-Quelle × Policy-Aktion
                print("\nBlockade-Quelle × Policy-Aktion:")
                cross = blocked_with_reason.groupby(
                    ["block_reason", "policy_action"]
                ).size()
                for (reason, pa), count in cross.items():
                    print(f"  {reason:20s} × {pa:15s}: {count:5d}")

                # Blockade-Quelle × Trend
                print("\nBlockade-Quelle × Trend:")
                cross_trend = blocked_with_reason.groupby(
                    ["block_reason", "trend"]
                ).size()
                for (reason, trend), count in cross_trend.items():
                    print(f"  {reason:20s} × {trend:12s}: {count:5d}")
                # V11.1: Downtrend-Pause Statistik
                pause_blocks = blocked_with_reason[
                    blocked_with_reason["block_reason"] == "downtrend_pause"
                ]
                if not pause_blocks.empty:
                    print(f"\n--- Downtrend-Pause-Gate (V11.1) ---")
                    print(f"  Pausierte Schritte: {len(pause_blocks)}")
                    print(f"  Anteil an allen Blockaden: "
                          f"{len(pause_blocks)/len(blocked)*100:.1f}%")
                    
                    # Welche Aktionen wurden pausiert?
                    paused_actions = pause_blocks["policy_action"].value_counts()
                    print(f"  Pausierte Aktionen:")
                    for act, cnt in paused_actions.items():
                        print(f"    {act:15s}: {cnt:5d}")

    # --- BTC/USD-Fluss ---
    trades_only = df[df["effective_action"] != "HOLD"]
    if not trades_only.empty:
        # V9.4: .str.startswith statt == (effective_action ist SELL_SMALL etc.)
        sells = trades_only[trades_only["effective_action"].str.startswith("SELL")]
        buys = trades_only[trades_only["effective_action"].str.startswith("BUY")]

        print(f"\n--- Trade-Fluss ---")
        print(f"Verkäufe (BTC→USD): {len(sells)}")
        if not sells.empty:
            print(f"  Ø BTC verkauft:   {sells['delta_btc'].astype(float).mean():.8f}")
            print(f"  Ø USD erhalten:   {sells['delta_cash'].astype(float).mean():.2f}")
            print(f"  Ø e_long bei SELL:{sells['e_long'].astype(float).mean():.4f}")

        print(f"Käufe (USD→BTC):    {len(buys)}")
        if not buys.empty:
            print(f"  Ø BTC gekauft:    {buys['delta_btc'].astype(float).mean():.8f}")
            print(f"  Ø USD ausgegeben: {buys['delta_cash'].astype(float).mean():.2f}")
            print(f"  Ø e_long bei BUY: {buys['e_long'].astype(float).mean():.4f}")
    else:
        print("\n⚠ KEINE TRADES AUSGEFÜHRT — System handelt nicht.")

    # --- e_long-Zonen × Trend ---
    print("\n--- e_long / Trend-Resonanz ---")
    try:
        df["e_long"] = df["e_long"].astype(float)
        bins = [-1.0, -0.05, -0.02, 0.02, 0.05, 1.0]
        labels = ["<< -5%", "-5..-2%", "-2..+2%", "+2..+5%", ">> +5%"]
        df["e_long_zone"] = pd.cut(
            df["e_long"], bins=bins, labels=labels, include_lowest=True
        )
        trades_for_zone = df[df["effective_action"] != "HOLD"]
        if not trades_for_zone.empty:
            grouped = trades_for_zone.groupby(
                ["trend", "e_long_zone", "effective_action"],
                observed=True,
            ).size()
            for (trend, zone, act), cnt in grouped.items():
                print(f"  trend={trend:10s}, e_long={str(zone):8s}, "
                      f"act={act:4s}: {cnt:5d}")
        else:
            print("  Keine Trades — keine Zonen-Auswertung.")
    except Exception as e:
        print(f"  Fehler: {e}")

    # --- Trades pro Episode ---
    print("\n--- Trades pro Episode ---")
    trades_per_episode = df[df["effective_action"] != "HOLD"].groupby("episode").size()
    if trades_per_episode.empty:
        print("  Keine Episoden mit Trades.")
    else:
        for ep, cnt in trades_per_episode.items():
            print(f"  Episode {int(ep):4d}: {cnt:4d} Trades")
        print(f"\n  Ø Trades/Episode: {trades_per_episode.mean():.1f}")
        print(f"  Min: {trades_per_episode.min()}, Max: {trades_per_episode.max()}")

        all_eps = df["episode"].unique()
        with_trades = set(trades_per_episode.index)
        without = set(all_eps) - with_trades
        if without:
            print(f"  Episoden ohne Trades: {len(without)} von {len(all_eps)}")