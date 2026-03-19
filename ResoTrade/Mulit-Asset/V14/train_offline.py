"""
train_offline.py — Resonanzfeldtheoretisches Multi-Asset Offline-Trainingspipeline

ResoTrade V14 — Asset-invariante Implementierung (BTC / ETH / Gold)

Kernfunktionen:
    prepare_asset_data(config)          → Lädt und bereitet OHLCV-Daten vor
    _ensure_columns(df, required)       → Validiert / ergänzt DataFrame-Spalten
    train_offline(config)               → Einzelner Trainingslauf
    train_asset_multi_pass(config, n)   → Multi-Pass-Training (n Zyklen)

Aliase für Rückwärtskompatibilität:
    train_asset = train_offline
"""

from __future__ import annotations

import os
import csv
import math
import random
import logging
from pathlib import Path
from typing import Any

import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def _ensure_columns(df: pd.DataFrame, required: list[str]) -> pd.DataFrame:
    """Ensure all *required* columns exist in *df*.

    Columns that are missing and can be derived from standard OHLCV columns
    (open, high, low, close, volume) are computed automatically; otherwise a
    ``ValueError`` is raised listing the still-missing columns.

    Parameters
    ----------
    df:
        Input DataFrame (modified in-place and returned).
    required:
        List of column names that must be present.

    Returns
    -------
    pd.DataFrame
        The (potentially augmented) DataFrame.

    Raises
    ------
    ValueError
        If required columns cannot be derived.
    """
    missing = [c for c in required if c not in df.columns]
    if not missing:
        return df

    # Auto-derive common columns
    for col in list(missing):
        if col == "typical_price" and all(c in df.columns for c in ("high", "low", "close")):
            df["typical_price"] = (df["high"] + df["low"] + df["close"]) / 3.0
            missing.remove(col)
        elif col == "hl2" and all(c in df.columns for c in ("high", "low")):
            df["hl2"] = (df["high"] + df["low"]) / 2.0
            missing.remove(col)

    if missing:
        raise ValueError(
            f"Required columns still missing after auto-derivation: {missing}. "
            f"Available columns: {list(df.columns)}"
        )
    return df


def prepare_asset_data(config: dict[str, Any]) -> pd.DataFrame:
    """Load and prepare OHLCV price data for the given asset config.

    Looks for a CSV file named ``<ASSET>_<interval>.csv`` (case-insensitive)
    in the current working directory or the directory given by the environment
    variable ``RESOTRADE_DATA_DIR``.

    The returned DataFrame always contains the columns:
        ``timestamp``, ``open``, ``high``, ``low``, ``close``, ``volume``,
        ``ma_short``, ``ma_long``, ``ac``, ``energy_dir``

    Parameters
    ----------
    config:
        Asset configuration dict as defined in ``asset_config.py``.

    Returns
    -------
    pd.DataFrame
        Prepared DataFrame indexed by integer position (reset_index).

    Raises
    ------
    FileNotFoundError
        If no matching data file can be located.
    """
    asset = config["asset"]
    interval = config["data_interval"]
    ma_short_w = config["ma_short"]
    ma_long_w = config["ma_long"]

    data_dir = Path(os.environ.get("RESOTRADE_DATA_DIR", "."))
    candidates = [
        data_dir / f"{asset}_{interval}.csv",
        data_dir / f"{asset.lower()}_{interval}.csv",
        data_dir / f"{asset.upper()}_{interval}.csv",
    ]

    csv_path: Path | None = None
    for candidate in candidates:
        if candidate.exists():
            csv_path = candidate
            break

    if csv_path is None:
        raise FileNotFoundError(
            f"No data file found for asset '{asset}' with interval '{interval}'. "
            f"Searched: {[str(c) for c in candidates]}"
        )

    logger.info("[%s] Loading data from %s", asset, csv_path)
    df = pd.read_csv(csv_path)

    # Normalise column names
    df.columns = [c.strip().lower() for c in df.columns]

    required_ohlcv = ["open", "high", "low", "close"]
    _ensure_columns(df, required_ohlcv)

    if "volume" not in df.columns:
        df["volume"] = 0.0

    df = df.reset_index(drop=True)
    close = df["close"].astype(float)

    # AC/DC decomposition (Resonanzfeldtheorie Axiom 1)
    df["ma_short"] = close.rolling(ma_short_w, min_periods=1).mean()
    df["ma_long"] = close.rolling(ma_long_w, min_periods=1).mean()
    df["ac"] = close - df["ma_long"]                       # AC = Preis - DC

    # Energy direction vector (Axiom 5): e_short - e_long
    df["e_short"] = (close - df["ma_short"]) / df["ma_short"].replace(0, float("nan"))
    df["e_long"] = (close - df["ma_long"]) / df["ma_long"].replace(0, float("nan"))
    df["energy_dir"] = df["e_short"] - df["e_long"]

    df.dropna(subset=["ma_long"], inplace=True)
    df = df.reset_index(drop=True)

    logger.info("[%s] Data prepared: %d rows", asset, len(df))
    return df


# ---------------------------------------------------------------------------
# Phase detection
# ---------------------------------------------------------------------------

def _detect_phase(ac: float, prev_ac: float, amplitude: float) -> str:
    """Classify the current AC phase as peak / trough / transition / flat."""
    if amplitude < 1e-8:
        return "flat"
    norm = ac / amplitude
    prev_norm = prev_ac / amplitude
    if norm > 0.6 and norm >= prev_norm:
        return "peak"
    if norm < -0.6 and norm <= prev_norm:
        return "trough"
    return "transition"


# ---------------------------------------------------------------------------
# Experience storage (CSV-based)
# ---------------------------------------------------------------------------

def _load_experience(path: str) -> dict[tuple, float]:
    """Load the chain→score experience table from a CSV file."""
    experience: dict[tuple, float] = {}
    if not os.path.exists(path):
        return experience
    with open(path, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue
            key = tuple(row[:-1])
            try:
                experience[key] = float(row[-1])
            except ValueError:
                pass
    return experience


def _save_experience(path: str, experience: dict[tuple, float]) -> None:
    """Persist the experience table to CSV."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        for key, score in experience.items():
            writer.writerow(list(key) + [score])


# ---------------------------------------------------------------------------
# Core training function
# ---------------------------------------------------------------------------

def train_offline(config: dict[str, Any]) -> dict[str, Any]:
    """Run one offline training pass for a single asset.

    Iterates over all available training windows in the prepared price data,
    simulates the resonance-field policy (AC/DC + energy direction), and
    updates the experience store (CSV).

    Parameters
    ----------
    config:
        Asset configuration dict as defined in ``asset_config.py``.

    Returns
    -------
    dict
        Summary metrics: ``asset``, ``episodes``, ``trades``, ``final_score``.
    """
    asset = config["asset"]
    window = config["training_window"]
    fee_pct = config["fee_pct"]
    hold_fraction = config["hold_fraction"]
    energy_buy_thr = config["energy_buy_threshold"]
    energy_sell_thr = config["energy_sell_threshold"]
    min_trade_frac = config["min_trade_fraction"]
    exp_file = config["experience_file"]

    df = prepare_asset_data(config)
    experience = _load_experience(exp_file)

    n_rows = len(df)
    if n_rows < window:
        logger.warning(
            "[%s] Not enough data (%d rows) for training window %d — skipping.",
            asset, n_rows, window,
        )
        return {"asset": asset, "episodes": 0, "trades": 0, "final_score": 0.0}

    episode_count = 0
    total_trades = 0
    scores: list[float] = []

    # Slide over all available windows
    for start in range(0, n_rows - window, window // 2):
        end = start + window
        window_df = df.iloc[start:end].reset_index(drop=True)

        # Portfolio state: fraction of capital in asset
        asset_frac = 0.5
        score = 0.0
        trade_count = 0
        prev_ac = float(window_df.loc[0, "ac"])

        ac_vals = window_df["ac"].values.astype(float)
        amplitude = float(np.std(ac_vals)) * 2.0 if len(ac_vals) > 1 else 1.0

        for i in range(1, len(window_df)):
            row = window_df.iloc[i]
            price = float(row["close"])
            ac = float(row["ac"])
            energy_dir = float(row["energy_dir"])

            phase = _detect_phase(ac, prev_ac, amplitude)
            prev_ac = ac

            # Resonance-field policy
            allow_buy = energy_dir > energy_buy_thr
            allow_sell = energy_dir < energy_sell_thr
            available_to_sell = asset_frac - hold_fraction  # never sell the HODL core

            action = "HOLD"
            if phase == "trough" and allow_buy and asset_frac < (1.0 - min_trade_frac):
                # BUY: increase asset fraction
                buy_frac = min(min_trade_frac * 2, 1.0 - asset_frac)
                cost = buy_frac * (1.0 + fee_pct)
                if cost <= (1.0 - asset_frac + 1e-9):
                    asset_frac += buy_frac
                    score -= fee_pct * buy_frac
                    action = "BUY"
                    trade_count += 1

            elif phase == "peak" and allow_sell and available_to_sell > min_trade_frac:
                # SELL: reduce asset fraction (but keep hold_fraction)
                sell_frac = min(min_trade_frac * 2, available_to_sell)
                asset_frac -= sell_frac
                score += sell_frac * (1.0 - fee_pct) - sell_frac
                action = "SELL"
                trade_count += 1

            # Experience key: (asset, phase, energy_bin)
            e_bin = "pos" if energy_dir >= 0 else "neg"
            key = (asset, phase, e_bin, action)
            old_score = experience.get(key, 0.0)
            experience[key] = old_score * 0.9 + score * 0.1  # exponential smoothing

        scores.append(score)
        total_trades += trade_count
        episode_count += 1

    _save_experience(exp_file, experience)

    final_score = float(np.mean(scores)) if scores else 0.0
    logger.info(
        "[%s] Training complete: %d episodes, %d trades, score=%.4f",
        asset, episode_count, total_trades, final_score,
    )
    return {
        "asset": asset,
        "episodes": episode_count,
        "trades": total_trades,
        "final_score": final_score,
    }


# ---------------------------------------------------------------------------
# Multi-pass training
# ---------------------------------------------------------------------------

def train_asset_multi_pass(
    config: dict[str, Any],
    passes: int | None = None,
) -> list[dict[str, Any]]:
    """Run multiple sequential training passes for a single asset.

    Parameters
    ----------
    config:
        Asset configuration dict.
    passes:
        Number of passes to run.  Defaults to 3 (standard
        ``TRAINING_PASSES`` value defined in ``asset_config``).

    Returns
    -------
    list of dict
        One summary dict per pass (as returned by :func:`train_offline`).
    """
    _DEFAULT_PASSES = 3
    n = passes if passes is not None else _DEFAULT_PASSES
    results = []
    for i in range(n):
        logger.info("[%s] Starting pass %d/%d", config["asset"], i + 1, n)
        result = train_offline(config)
        result["pass"] = i + 1
        results.append(result)
    return results


# ---------------------------------------------------------------------------
# Backward-compatibility alias
# ---------------------------------------------------------------------------

#: Alias so that legacy code importing ``train_asset`` still works.
train_asset = train_offline


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    from asset_config import BTC_CONFIG, ETH_CONFIG, GOLD_CONFIG

    _CONFIGS = {
        "BTC": BTC_CONFIG,
        "ETH": ETH_CONFIG,
        "GOLD": GOLD_CONFIG,
    }

    parser = argparse.ArgumentParser(description="ResoTrade V14 Offline Training")
    parser.add_argument(
        "--asset",
        choices=list(_CONFIGS.keys()),
        default="BTC",
        help="Asset to train (default: BTC)",
    )
    parser.add_argument(
        "--passes",
        type=int,
        default=None,
        help="Number of training passes (default: from config)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    cfg = _CONFIGS[args.asset]
    results = train_asset_multi_pass(cfg, passes=args.passes)
    for r in results:
        print(
            f"Pass {r['pass']}: episodes={r['episodes']}, "
            f"trades={r['trades']}, score={r['final_score']:.4f}"
        )
