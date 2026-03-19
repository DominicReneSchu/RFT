"""
asset_config.py — Multi-Asset configuration for ResoTrade V14

All three assets (BTC, ETH, Gold) are configured with data_interval="1h"
so they run identically through the train_offline.py pipeline (asset-invariant).

MA windows are designed for hourly data:
  ma_short=48  → 48h  ≈ 2 days
  ma_long=336  → 336h ≈ 14 days
"""

# ---------------------------------------------------------------------------
# Global training parameters
# ---------------------------------------------------------------------------

TRAINING_WINDOW_LENGTH = 720   # Number of hourly candles per training window (~30 days)
TRAINING_PASSES = 3            # Number of multi-pass cycles


# ---------------------------------------------------------------------------
# BTC configuration (reference asset)
# ---------------------------------------------------------------------------

BTC_CONFIG = {
    "asset": "BTC",
    "symbol": "XBTUSD",
    "data_interval": "1h",
    "ma_short": 48,            # 48h ≈ 2 days
    "ma_long": 336,            # 336h ≈ 14 days
    "training_window": TRAINING_WINDOW_LENGTH,
    "fee_pct": 0.0026,
    "min_trade_fraction": 0.05,
    "hold_fraction": 0.10,     # DC core — never traded
    "energy_buy_threshold": -0.005,
    "energy_sell_threshold": 0.005,
    "experience_file": "btc_experience.csv",
}

# ---------------------------------------------------------------------------
# ETH configuration
# ---------------------------------------------------------------------------

ETH_CONFIG = {
    "asset": "ETH",
    "symbol": "ETHUSD",
    "data_interval": "1h",
    "ma_short": 48,
    "ma_long": 336,
    "training_window": TRAINING_WINDOW_LENGTH,
    "fee_pct": 0.0026,
    "min_trade_fraction": 0.05,
    "hold_fraction": 0.10,
    "energy_buy_threshold": -0.005,
    "energy_sell_threshold": 0.005,
    "experience_file": "eth_experience.csv",
}

# ---------------------------------------------------------------------------
# Gold configuration
# Fixed: was data_interval="1d" (daily), now aligned to "1h" (hourly)
# like BTC and ETH, so that MA windows (ma_short=48, ma_long=336) retain
# their intended time-scale meaning (2 days / 14 days) and
# TRAINING_WINDOW_LENGTH=720 covers ~30 days rather than ~2 years.
# ---------------------------------------------------------------------------

GOLD_CONFIG = {
    "asset": "GOLD",
    "symbol": "XAUUSD",
    "data_interval": "1h",    # Fixed: was "1d" — aligned to "1h" like BTC/ETH
    "ma_short": 48,
    "ma_long": 336,
    "training_window": TRAINING_WINDOW_LENGTH,
    "fee_pct": 0.0020,
    "min_trade_fraction": 0.05,
    "hold_fraction": 0.10,
    "energy_buy_threshold": -0.005,
    "energy_sell_threshold": 0.005,
    "experience_file": "gold_experience.csv",
}
