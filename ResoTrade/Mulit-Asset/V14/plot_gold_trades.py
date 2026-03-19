"""
plot_gold_trades.py — Visualisierung der Gold-Trainingsergebnisse (ResoTrade V14)

Nutzt die re-exportierten Funktionen aus train_gold_offline.py, um
Handelsentscheidungen und AC/DC-Zerlegung für Gold zu visualisieren.
"""

import logging
import pandas as pd
import matplotlib.pyplot as plt

from train_gold_offline import prepare_asset_data, train_asset, _ensure_columns
from asset_config import GOLD_CONFIG

logger = logging.getLogger(__name__)


def plot_gold_trades() -> None:
    """Visualise price data, AC/DC decomposition and energy direction for Gold."""
    df = prepare_asset_data(GOLD_CONFIG)

    fig, axes = plt.subplots(3, 1, figsize=(14, 10), sharex=True)
    fig.suptitle("ResoTrade V14 — Gold (XAUUSD) Trainingsdaten", fontsize=14)

    # --- Price + MA ---
    ax1 = axes[0]
    ax1.plot(df.index, df["close"], label="Close", linewidth=0.8, color="gold")
    ax1.plot(df.index, df["ma_short"], label=f"MA-Short ({GOLD_CONFIG['ma_short']}h)", linewidth=1.0, color="orange")
    ax1.plot(df.index, df["ma_long"], label=f"MA-Long ({GOLD_CONFIG['ma_long']}h)", linewidth=1.2, color="red")
    ax1.set_ylabel("Preis (USD)")
    ax1.legend(loc="upper left", fontsize=8)
    ax1.grid(True, alpha=0.3)

    # --- AC component ---
    ax2 = axes[1]
    ax2.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    ax2.fill_between(df.index, df["ac"], 0, where=(df["ac"] >= 0), color="green", alpha=0.4, label="AC > 0 (Peak)")
    ax2.fill_between(df.index, df["ac"], 0, where=(df["ac"] < 0), color="red", alpha=0.4, label="AC < 0 (Trough)")
    ax2.set_ylabel("AC-Komponente")
    ax2.legend(loc="upper left", fontsize=8)
    ax2.grid(True, alpha=0.3)

    # --- Energy direction ---
    ax3 = axes[2]
    ax3.axhline(0, color="gray", linewidth=0.8, linestyle="--")
    ax3.axhline(GOLD_CONFIG["energy_buy_threshold"], color="green", linewidth=0.8, linestyle=":", label="Buy-Schwelle")
    ax3.axhline(GOLD_CONFIG["energy_sell_threshold"], color="red", linewidth=0.8, linestyle=":", label="Sell-Schwelle")
    ax3.plot(df.index, df["energy_dir"], linewidth=0.7, color="blue", label="energy_dir")
    ax3.set_ylabel("Energierichtung")
    ax3.set_xlabel("Zeitindex (Stunden)")
    ax3.legend(loc="upper left", fontsize=8)
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    out_path = "gold_trades_plot.png"
    plt.savefig(out_path, dpi=120)
    logger.info("Plot gespeichert: %s", out_path)
    plt.show()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    plot_gold_trades()
