"""
Resonanz-Analyse V9.4 — FFT, Amplitude, Posteriors, Backtests.

MA-Parameter werden aus config.py importiert (Single Source of Truth).
V9.4: Fee aus config.KRAKEN_FEE_PCT (nicht mehr eigener ALPHA-Wert).

V11.1: CLI-Parameter für abschnittsweises Training.
  python resonance_analysis.py                                    # Standard: letzte 180 Tage
  python resonance_analysis.py --start 2024-08-01 --end 2025-08-01
  python resonance_analysis.py --start 2023-08-01 --end 2024-08-01
"""
import os
import sys
import argparse
from datetime import datetime
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.signal import find_peaks
from scipy.fft import rfft, rfftfreq

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from config import (
    MA_SHORT_WINDOW as MA_SHORT,
    MA_LONG_WINDOW as MA_LONG,
    VOLATILITY_WINDOW as VOL_WINDOW,
    KRAKEN_FEE_PCT,
)

# ====== CONFIG ======
SYMBOL = "BTC-USD"
PERIOD = "180d"
INTERVAL = "1h"

# resonance params (Stundenbasis)
FFT_WINDOW = 336
AMP_WINDOW = 72
TIMECOMP_WINDOW = 336
G_TARGET = 0.05
GRID_LEVELS = 5

# V9.4: Fee konsistent aus config — ALPHA abgeleitet
ALPHA = 2.0 * KRAKEN_FEE_PCT  # Fee pro Roundtrip (Buy + Sell)

# traditional params
RSI_WINDOW = 14
RSI_OVERSOLD = 30
RSI_OVERBOUGHT = 70

# stop-loss param
STOP_PCT = 0.10

# output
OUTPUT_DIR = "resonance_output_v2"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HOURS_PER_YEAR = 365 * 24


# ====== CLI ARGUMENT PARSING ======

def parse_args():
    """
    Parst Kommandozeilen-Argumente für abschnittsweises Training.

    Nutzung:
      python resonance_analysis.py                                  # letzte 180d
      python resonance_analysis.py --start 2024-08-01 --end 2025-08-01
      python resonance_analysis.py --start 2023-08-01 --end 2024-08-01
    """
    parser = argparse.ArgumentParser(
        description="Resonanz-Analyse V9.4 — Abschnittsweises Training"
    )
    parser.add_argument(
        "--start", type=str, default=None,
        help="Startdatum (YYYY-MM-DD). Wenn gesetzt, wird --end benötigt."
    )
    parser.add_argument(
        "--end", type=str, default=None,
        help="Enddatum (YYYY-MM-DD). Wenn gesetzt, wird --start benötigt."
    )
    parser.add_argument(
        "--period", type=str, default=PERIOD,
        help=f"Zeitraum (z.B. '180d', '730d'). Nur wenn --start/--end nicht gesetzt. Default: {PERIOD}"
    )
    parser.add_argument(
        "--symbol", type=str, default=SYMBOL,
        help=f"Symbol. Default: {SYMBOL}"
    )
    return parser.parse_args()


# ====== UTILITIES ======

def _flatten_columns(df):
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    return df


def load_data(symbol=SYMBOL, period=PERIOD, interval=INTERVAL,
              start=None, end=None):
    """
    Lädt Daten von yfinance. Bei älteren Daten (>730d) oder Fehler:
    Fallback auf Binance (Stundendaten seit 2017).
    """
    try:
        if start and end:
            print(f"[Data] Lade {symbol} von {start} bis {end} ({interval})...")
            df = yf.download(
                symbol, start=start, end=end, interval=interval,
                progress=False, auto_adjust=False,
            )
        else:
            print(f"[Data] Lade {symbol} Zeitraum {period} ({interval})...")
            df = yf.download(
                symbol, period=period, interval=interval,
                progress=False, auto_adjust=False,
            )

        df = _flatten_columns(df)

        if df.empty:
            raise RuntimeError("yfinance hat leeren DataFrame zurückgegeben")

        df = df[['Close', 'Volume']].dropna()
        df.rename(columns={'Close': 'price', 'Volume': 'volume'}, inplace=True)
        df['price'] = df['price'].astype(float)

        if len(df) < 100:
            raise RuntimeError(f"Nur {len(df)} Datenpunkte — zu wenig für Analyse")

        print(f"[Data] yfinance: {len(df)} Datenpunkte geladen, "
              f"Zeitraum: {df.index.min()} bis {df.index.max()}")
        print(f"[Data] MA-Parameter aus config.py: MA_SHORT={MA_SHORT}, "
              f"MA_LONG={MA_LONG}, VOL_WINDOW={VOL_WINDOW}")
        return df

    except Exception as e:
        print(f"[Data] ⚠ yfinance fehlgeschlagen: {e}")
        if start and end:
            print("[Data] Versuche Binance-Fallback für Stundendaten...")
            return _load_data_binance_hourly(start, end)
        print("[Data] Versuche Fallback über data_loader.py ...")
        return _load_data_fallback()


def _load_data_binance_hourly(start: str, end: str):
    """
    Fallback: Lädt Stundendaten von Binance (BTCUSDT).
    Binance hat Daten seit 2017 — keine 730-Tage-Begrenzung.
    """
    from datetime import datetime as dt, timedelta, timezone
    import requests

    BINANCE_URL = "https://api.binance.com/api/v3/klines"

    start_dt = dt.strptime(start, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    end_dt = dt.strptime(end, "%Y-%m-%d").replace(tzinfo=timezone.utc)

    print(f"[Data] Binance: Lade BTCUSDT 1h von {start} bis {end}...")

    rows = []
    cur_start = start_dt
    limit = 1000  # Binance max pro Request

    while cur_start < end_dt:
        params = {
            "symbol": "BTCUSDT",
            "interval": "1h",
            "startTime": int(cur_start.timestamp() * 1000),
            "endTime": int(end_dt.timestamp() * 1000),
            "limit": limit,
        }
        resp = requests.get(BINANCE_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        if not data:
            break

        for k in data:
            open_time_ms = k[0]
            close_price = float(k[4])
            volume = float(k[5])
            ts = dt.fromtimestamp(open_time_ms / 1000.0, tz=timezone.utc)
            rows.append({"ts": ts, "price": close_price, "volume": volume})

        # Nächster Batch: nach letzter Kerze
        last_open_ms = data[-1][0]
        cur_start = dt.fromtimestamp(last_open_ms / 1000.0, tz=timezone.utc) + timedelta(hours=1)

        if len(data) < limit:
            break  # Keine weiteren Daten

    if not rows:
        raise RuntimeError(f"Binance hat keine Daten für {start} bis {end} geliefert")

    df = pd.DataFrame(rows)
    df = df.set_index("ts").sort_index()

    # Duplikate entfernen (Binance liefert manchmal Überlappungen)
    df = df[~df.index.duplicated(keep='first')]

    print(f"[Data] Binance: {len(df)} Stundendaten geladen, "
          f"Zeitraum: {df.index.min()} bis {df.index.max()}")
    print(f"[Data] MA-Parameter aus config.py: MA_SHORT={MA_SHORT}, "
          f"MA_LONG={MA_LONG}, VOL_WINDOW={VOL_WINDOW}")
    return df

        
def _load_data_fallback():
    """
    Fallback: Nutzt data_loader.py (Binance → CoinGecko → Stooq → Synthetisch).
    Konvertiert das Ergebnis in das von resonance_analysis erwartete Format
    mit DatetimeIndex.
    """
    from data_loader import load_or_download_btc_history

    raw = load_or_download_btc_history(days=180, force_download=True)

    if raw.empty:
        raise RuntimeError("Auch Fallback-Datenquellen haben keine Daten geliefert")

    df = raw.copy()

    # Zeitindex rekonstruieren
    if "ts" in df.columns:
        df["ts"] = pd.to_datetime(df["ts"], errors="coerce")
        df = df.dropna(subset=["ts"])
        df = df.set_index("ts").sort_index()
    elif "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.dropna(subset=["Date"])
        df = df.set_index("Date").sort_index()

    # Spalten normalisieren
    if "price" not in df.columns:
        for col in ["Close", "close", "CLOSE"]:
            if col in df.columns:
                df["price"] = df[col]
                break

    if "price" not in df.columns:
        raise RuntimeError("Keine 'price'-Spalte in Fallback-Daten")

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])

    # Volume-Spalte (wird von einigen Funktionen erwartet)
    if "volume" not in df.columns:
        df["volume"] = 0.0

    df = df[["price", "volume"]]

    print(f"[Data] Fallback: {len(df)} Datenpunkte geladen, "
          f"Zeitraum: {df.index.min()} bis {df.index.max()}")
    print(f"[Data] MA-Parameter aus config.py: MA_SHORT={MA_SHORT}, "
          f"MA_LONG={MA_LONG}, VOL_WINDOW={VOL_WINDOW}")
    return df


def rolling_volatility(series, window):
    returns = series.pct_change().fillna(0)
    return returns.rolling(window).std() * np.sqrt(window)


def fft_period_proxy(series, window):
    x = series[-window:].ffill().values.flatten()
    if len(x) < window:
        return np.nan
    x_detr = x - np.mean(x)
    yf_freq = np.abs(rfft(x_detr))
    freqs = rfftfreq(window, d=1.0)
    yf_freq[0] = 0
    idx = np.argmax(yf_freq)
    if freqs[idx] == 0:
        return np.nan
    return 1.0 / freqs[idx]


def amplitude_proxy(series, window):
    seg = series[-window:].ffill()
    if len(seg) == 0:
        return np.nan
    return seg.max() - seg.min()


def time_compression(series, window):
    seg = series[-window:].values
    if len(seg) < 10:
        return np.nan
    peaks, _ = find_peaks(seg, distance=2)
    if len(peaks) < 2:
        return np.nan
    return np.mean(np.diff(peaks))


def compute_grid_spacing(alpha, g):
    denom = (1 - alpha / 2)
    if denom == 0:
        denom = 1e-9
    q = ((1 + alpha / 2) * (1 + g)) / denom - 1
    return q


def _get_scalar_from_row(row, key, default=np.nan):
    if isinstance(row, dict):
        val = row.get(key, default)
    else:
        try:
            val = row.get(key, default)
        except Exception:
            val = default

    if isinstance(val, pd.Series):
        try:
            return val.iloc[0]
        except Exception:
            arr = np.asarray(val)
            return arr.flatten()[0] if arr.size else default
    if isinstance(val, (np.ndarray, list, tuple)):
        arr = np.asarray(val)
        return arr.flatten()[0] if arr.size else default
    return val


def compute_dynamic_grid_levels(row, q_base, grid_levels=GRID_LEVELS):
    price = _get_scalar_from_row(row, 'price', np.nan)
    try:
        price = float(price)
    except Exception:
        price = np.nan

    M_val = _get_scalar_from_row(row, 'ma_short', np.nan)
    try:
        M = float(M_val) if not pd.isna(M_val) else price
    except Exception:
        M = price

    amp = _get_scalar_from_row(row, 'amplitude', np.nan)
    amp_med = _get_scalar_from_row(row, 'amp_med', np.nan)

    if pd.isna(amp) or pd.isna(amp_med) or amp_med == 0:
        scale = 1.0
    else:
        scale = 1.0 + 0.6 * max(0.0, (float(amp) / float(amp_med)) - 1.0)
        scale = float(np.clip(scale, 0.6, 3.0))

    q_row = float(q_base) * scale
    if pd.isna(M):
        M = price if not pd.isna(price) else 1.0

    buy_prices = [M * (1 - q_row * (i + 1)) for i in range(grid_levels)]
    sell_prices = [M * (1 + q_row * (i + 1)) for i in range(grid_levels)]
    return buy_prices, sell_prices, q_row, scale


# ====== TRADITIONAL SIGNALS ======

def compute_rsi(series, window=RSI_WINDOW):
    delta = series.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.rolling(window).mean()
    ma_down = down.rolling(window).mean()
    ma_down = ma_down.replace(0, np.nan)
    rs = ma_up / ma_down
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)


def compute_traditional_signals(df):
    df = df.copy()
    df['ma_short'] = df['price'].rolling(MA_SHORT).mean()
    df['ma_long'] = df['price'].rolling(MA_LONG).mean()
    df['rsi'] = compute_rsi(df['price'], RSI_WINDOW)
    df['trad_signal'] = 'hold'
    cross_up = (
        (df['ma_short'] > df['ma_long'])
        & (df['ma_short'].shift(1) <= df['ma_long'].shift(1))
    )
    cross_down = (
        (df['ma_short'] < df['ma_long'])
        & (df['ma_short'].shift(1) >= df['ma_long'].shift(1))
    )
    df.loc[cross_up & (df['rsi'] < RSI_OVERBOUGHT), 'trad_signal'] = 'buy'
    df.loc[cross_down & (df['rsi'] > RSI_OVERSOLD), 'trad_signal'] = 'sell'
    df['trad_signal_trend'] = 'hold'
    df.loc[
        (df['ma_short'] > df['ma_long']) & (df['rsi'] < RSI_OVERBOUGHT),
        'trad_signal_trend',
    ] = 'buy'
    df.loc[
        (df['ma_short'] < df['ma_long']) & (df['rsi'] > RSI_OVERSOLD),
        'trad_signal_trend',
    ] = 'sell'
    return df


# ====== RESONANCE SIGNALS ======

def compute_resonance_signals(df):
    df = df.copy()
    df['ma_short'] = df['price'].rolling(MA_SHORT).mean()
    df['ma_long'] = df['price'].rolling(MA_LONG).mean()
    df['vol'] = rolling_volatility(df['price'], VOL_WINDOW)
    prices = df['price'].values.flatten()

    fft_list = [np.nan] * len(df)
    amp_list = [np.nan] * len(df)
    tc_list = [np.nan] * len(df)

    for i in range(len(df)):
        if i + 1 >= FFT_WINDOW:
            fft_list[i] = fft_period_proxy(pd.Series(prices[:i + 1]), FFT_WINDOW)
        if i + 1 >= AMP_WINDOW:
            amp_list[i] = amplitude_proxy(pd.Series(prices[:i + 1]), AMP_WINDOW)
        if i + 1 >= TIMECOMP_WINDOW:
            tc_list[i] = time_compression(pd.Series(prices[:i + 1]), TIMECOMP_WINDOW)

    df['fft_period'] = fft_list
    df['amplitude'] = amp_list
    df['time_comp'] = tc_list
    df['drift'] = df['ma_short'] - df['ma_long']

    df['amp_med'] = df['amplitude'].rolling(AMP_WINDOW).median()
    df['vol_med'] = df['vol'].rolling(VOL_WINDOW).median()
    df['tc_med'] = df['time_comp'].rolling(TIMECOMP_WINDOW).median()

    with np.errstate(divide='ignore', invalid='ignore'):
        df['resonance_score'] = (
            (df['amplitude'] / df['amp_med'])
            * (df['vol'] / df['vol_med'])
            * (df['tc_med'] / df['time_comp'])
        )
    df['resonance_score'] = (
        df['resonance_score'].replace([np.inf, -np.inf], np.nan).fillna(0)
    )
    df['use_grid'] = df['resonance_score'] > 1.2
    df['direction_hint'] = np.sign(df['drift'].fillna(0))
    df['res_signal'] = 'hold'
    df.loc[(df['use_grid']) & (df['direction_hint'] < 0), 'res_signal'] = 'buy'
    df.loc[(df['use_grid']) & (df['direction_hint'] > 0), 'res_signal'] = 'sell'
    return df


# ====== BACKTEST METRICS ======

def compute_metrics_from_nav(nav_series):
    nav = nav_series.dropna().astype(float)
    if nav.empty:
        return {
            'total_return': np.nan, 'annual_return': np.nan,
            'sharpe': np.nan, 'max_drawdown': np.nan,
        }
    total_return = nav.iloc[-1] / nav.iloc[0] - 1.0
    ret = nav.pct_change().fillna(0)
    mean_r = ret.mean()
    std_r = ret.std()
    if std_r == 0 or np.isnan(std_r):
        sharpe = np.nan
    else:
        sharpe = (mean_r / std_r) * np.sqrt(HOURS_PER_YEAR)
    cummax = nav.cummax()
    drawdown = (cummax - nav) / cummax
    maxdd = drawdown.max()
    n_steps = len(nav)
    try:
        annual_return = (
            (1.0 + total_return) ** (HOURS_PER_YEAR / n_steps) - 1.0
            if total_return > -1 else np.nan
        )
    except Exception:
        annual_return = np.nan
    return {
        'total_return': total_return, 'annual_return': annual_return,
        'sharpe': sharpe, 'max_drawdown': maxdd,
    }


# ====== BACKTESTS (FIFO lots, stop-loss stored, nav_series) ======

def backtest_traditional(df, capital=10000.0):
    fiat = capital
    btc = 0.0
    trades = []
    lots = []
    realized_pnl_total = 0.0
    nav_records = []

    for t, row in df.iterrows():
        p_raw = _get_scalar_from_row(row, 'price', np.nan)
        try:
            p = float(p_raw)
        except Exception:
            nav_records.append(
                (t, fiat + btc * (nav_records[-1][1] if nav_records else 0))
            )
            continue
        sig = str(_get_scalar_from_row(row, 'trad_signal', 'hold'))

        if sig == 'buy' and fiat > 1:
            spend = fiat * 0.5
            qty = (spend * (1 - ALPHA / 2)) / p
            if qty > 0:
                fiat -= spend
                btc += qty
                stop_loss = p * (1 - STOP_PCT)
                lots.append([qty, p, stop_loss, t])
                trades.append({
                    'type': 'buy', 'ts': t, 'price': round(p, 2),
                    'size': round(qty, 8), 'cash': -round(spend, 2),
                    'realized_pnl': 0.0, 'stop_loss': round(stop_loss, 2),
                })

        elif sig == 'sell' and btc > 1e-9:
            size = btc * 0.5
            if size > 0:
                proceeds = size * p * (1 - ALPHA / 2)
                btc -= size
                fiat += proceeds
                remaining = size
                cost_basis = 0.0
                while remaining > 1e-12 and lots:
                    lot_qty, lot_price, lot_sl, lot_ts = lots[0]
                    consume = min(lot_qty, remaining)
                    cost_basis += consume * lot_price
                    lots[0][0] -= consume
                    remaining -= consume
                    if lots[0][0] <= 1e-12:
                        lots.pop(0)
                realized = proceeds - cost_basis
                realized_pnl_total += realized
                trades.append({
                    'type': 'sell', 'ts': t, 'price': round(p, 2),
                    'size': round(size, 8), 'cash': round(proceeds, 2),
                    'realized_pnl': round(realized, 2), 'stop_loss': np.nan,
                })

        nav = fiat + btc * p
        nav_records.append((t, nav))

    nav_series = pd.Series(
        [v for _, v in nav_records], index=[ts for ts, _ in nav_records]
    )
    open_lots = [
        {
            'qty': float(l[0]), 'entry_price': float(l[1]),
            'stop_loss': float(l[2]), 'ts': l[3],
        }
        for l in lots
    ]
    trades_df = pd.DataFrame(trades)
    metrics = compute_metrics_from_nav(nav_series)
    return {
        'nav': nav_series.iloc[-1] if not nav_series.empty else fiat,
        'fiat': fiat, 'btc': btc, 'trades': trades_df,
        'nav_series': nav_series, 'realized_pnl': realized_pnl_total,
        'metrics': metrics, 'open_lots': open_lots,
    }


def backtest_resonance_grid(df, capital=10000.0):
    q_base = compute_grid_spacing(ALPHA, G_TARGET)
    start_price = df['price'].iloc[0]
    if isinstance(start_price, (pd.Series, np.ndarray)):
        start_price = _get_scalar_from_row({'price': start_price}, 'price', np.nan)
    try:
        start_price = float(start_price)
    except Exception:
        start_price = float(df['price'].iloc[-1])

    fiat = capital * 0.5
    btc = (capital * 0.5) / start_price
    lots = (
        [[btc, start_price, start_price * (1 - STOP_PCT), df.index[0]]]
        if btc > 0 else []
    )
    trades = []
    realized_pnl_total = 0.0
    nav_records = []

    for t, row in df.iterrows():
        p_raw = _get_scalar_from_row(row, 'price', np.nan)
        try:
            p = float(p_raw)
        except Exception:
            nav_records.append(
                (t, fiat + btc * (nav_records[-1][1] if nav_records else 0))
            )
            continue

        buy_prices, sell_prices, q_row, scale = compute_dynamic_grid_levels(
            row, q_base, GRID_LEVELS
        )
        rs_raw = _get_scalar_from_row(row, 'resonance_score', 0.0)
        try:
            rs = float(rs_raw)
        except Exception:
            rs = 0.0

        base_frac = 0.12
        buy_frac = float(np.clip(base_frac * (1.0 + rs), 0.05, 0.5))
        sell_frac = float(np.clip(base_frac * (1.0 + rs), 0.05, 0.5))

        # SELL
        for sp in sell_prices:
            if p >= sp and btc > 1e-9:
                size = btc * sell_frac
                if size <= 0:
                    continue
                proceeds = size * p * (1 - ALPHA / 2)
                btc -= size
                fiat += proceeds
                remaining = size
                cost_basis = 0.0
                while remaining > 1e-12 and lots:
                    lot_qty, lot_price, lot_sl, lot_ts = lots[0]
                    consume = min(lot_qty, remaining)
                    cost_basis += consume * lot_price
                    lots[0][0] -= consume
                    remaining -= consume
                    if lots[0][0] <= 1e-12:
                        lots.pop(0)
                realized = proceeds - cost_basis
                realized_pnl_total += realized
                trades.append({
                    'type': 'sell', 'ts': t, 'price': round(p, 2),
                    'size': round(size, 8), 'cash': round(proceeds, 2),
                    'realized_pnl': round(realized, 2), 'stop_loss': np.nan,
                })

        # BUY
        for bp in buy_prices:
            if p <= bp and fiat > 1e-6:
                spend = fiat * buy_frac
                if spend <= 1.0:
                    continue
                qty = (spend * (1 - ALPHA / 2)) / p
                fiat -= spend
                btc += qty
                stop_loss = p * (1 - STOP_PCT)
                lots.append([qty, p, stop_loss, t])
                trades.append({
                    'type': 'buy', 'ts': t, 'price': round(p, 2),
                    'size': round(qty, 8), 'cash': -round(spend, 2),
                    'realized_pnl': 0.0, 'stop_loss': round(stop_loss, 2),
                })

        nav = fiat + btc * p
        nav_records.append((t, nav))

    nav_series = pd.Series(
        [v for _, v in nav_records], index=[ts for ts, _ in nav_records]
    )
    open_lots = [
        {
            'qty': float(l[0]), 'entry_price': float(l[1]),
            'stop_loss': float(l[2]), 'ts': l[3],
        }
        for l in lots
    ]
    trades_df = pd.DataFrame(trades)
    metrics = compute_metrics_from_nav(nav_series)
    return {
        'nav': nav_series.iloc[-1] if not nav_series.empty else fiat,
        'fiat': fiat, 'btc': btc, 'trades': trades_df,
        'nav_series': nav_series, 'realized_pnl': realized_pnl_total,
        'metrics': metrics, 'open_lots': open_lots,
    }


# ====== SIGNAL EVALUATION ======

def evaluate_signal_probabilities(
    df,
    signal_cols=('res_signal', 'trad_signal'),
    horizons=('1D', '3D', '7D'),
    thresholds=(0.01, 0.03, 0.05),
    output_dir=OUTPUT_DIR,
):
    os.makedirs(output_dir, exist_ok=True)
    horizons_td = [pd.to_timedelta(h) for h in horizons]
    idx = df.index
    horizon_pos = {}
    for td in horizons_td:
        targets = idx + td
        pos = idx.get_indexer(targets, method='bfill')
        horizon_pos[td] = pos

    results_rows = []
    price_arr = np.asarray(df['price'].to_numpy()).reshape(-1)
    now_price_series = pd.Series(price_arr, index=idx)

    for sigcol in signal_cols:
        if sigcol not in df.columns:
            continue
        for td in horizons_td:
            pos = horizon_pos[td]
            future_price = pd.Series(np.nan, index=idx, dtype='float64')
            matched = pos >= 0
            if matched.any():
                future_vals = price_arr[pos[matched]]
                future_price.iloc[matched] = future_vals

            ret = (future_price / now_price_series) - 1.0
            signals = df[sigcol].fillna('hold')
            mask_active = signals.isin(['buy', 'sell'])

            for thr in thresholds:
                buy_mask = (signals == 'buy') & mask_active & (~ret.isna())
                if buy_mask.any():
                    buy_arr = np.asarray(ret[buy_mask].to_numpy()).ravel()
                    buy_count = int(buy_arr.size)
                    buy_win = int(np.sum(buy_arr > thr))
                    buy_mean = float(np.nanmean(buy_arr))
                    buy_median = float(np.nanmedian(buy_arr))
                    buy_prob = float(buy_win / buy_count)
                else:
                    buy_count = buy_win = 0
                    buy_mean = buy_median = buy_prob = np.nan

                sell_mask = (signals == 'sell') & mask_active & (~ret.isna())
                if sell_mask.any():
                    sell_arr = np.asarray(ret[sell_mask].to_numpy()).ravel()
                    sell_count = int(sell_arr.size)
                    sell_win = int(np.sum(sell_arr < -thr))
                    sell_mean = float(np.nanmean(sell_arr))
                    sell_median = float(np.nanmedian(sell_arr))
                    sell_prob = float(sell_win / sell_count)
                else:
                    sell_count = sell_win = 0
                    sell_mean = sell_median = sell_prob = np.nan

                results_rows.append({
                    'signal_col': sigcol,
                    'horizon': str(td),
                    'threshold': thr,
                    'buy_count': buy_count, 'buy_win': buy_win,
                    'buy_winrate': buy_prob,
                    'buy_mean_ret': buy_mean, 'buy_median_ret': buy_median,
                    'sell_count': sell_count, 'sell_win': sell_win,
                    'sell_winrate': sell_prob,
                    'sell_mean_ret': sell_mean, 'sell_median_ret': sell_median,
                })

            raw_df = pd.DataFrame({
                'ts': df.index,
                'price_now': now_price_series,
                'price_future': future_price,
                'ret': ret,
                'signal': signals,
            })
            raw_fn = os.path.join(
                output_dir,
                f"raw_{sigcol}_h{int(td.total_seconds() / 3600)}h_"
                f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            )
            try:
                raw_df.to_csv(raw_fn, index=True)
            except Exception:
                pass

    summary_df = pd.DataFrame(results_rows)
    summary_fn = os.path.join(
        output_dir,
        f"signal_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
    )
    summary_df.to_csv(summary_fn, index=False)
    print(f"Saved summary -> {summary_fn}")
    return summary_df


def add_posterior_probs_from_summary(
    df, summary_df,
    signal_cols=('res_signal', 'trad_signal'),
    horizons=('1D', '3D', '7D'),
    threshold=0.01,
    output_dir=OUTPUT_DIR,
):
    """
    Fügt Posterior-Wahrscheinlichkeiten aus der Signal-Evaluation
    als neue Spalten an den DataFrame an.
    """
    sel = summary_df[summary_df['threshold'] == threshold].copy()
    prob_map = {}
    for _, r in sel.iterrows():
        sig = r['signal_col']
        try:
            hd = pd.to_timedelta(r['horizon'])
        except Exception:
            try:
                hd = pd.to_timedelta(str(r['horizon']))
            except Exception:
                continue
        prob_map[(sig, str(hd))] = (
            r.get('buy_winrate', np.nan),
            r.get('sell_winrate', np.nan),
        )

    for h in horizons:
        td = pd.to_timedelta(h)
        hkey = str(td)
        for sig in signal_cols:
            col_buy = f"prob_{sig}_buy_{h}"
            col_sell = f"prob_{sig}_sell_{h}"
            df[col_buy] = np.nan
            df[col_sell] = np.nan
            buy_prob, sell_prob = prob_map.get((sig, hkey), (np.nan, np.nan))
            if sig not in df.columns:
                continue
            mask_buy = df[sig] == 'buy'
            mask_sell = df[sig] == 'sell'
            if not np.isnan(buy_prob):
                df.loc[mask_buy, col_buy] = float(buy_prob)
            if not np.isnan(sell_prob):
                df.loc[mask_sell, col_sell] = float(sell_prob)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    outfn = os.path.join(output_dir, f"signals_with_posteriors_{ts}.csv")
    try:
        df.to_csv(outfn)
        print(f"Saved signals with posteriors -> {outfn}")
    except Exception:
        print("Could not save signals_with_posteriors CSV.")
    return df


# ====== PLOTTING / OUTPUT ======

def align_nav_to_index(nav_series, target_index):
    if nav_series is None or getattr(nav_series, "empty", True):
        return None
    nav = pd.Series(nav_series.values, index=pd.to_datetime(nav_series.index))
    tgt = pd.to_datetime(target_index)
    try:
        nav_full = nav.reindex(tgt, method='ffill')
    except Exception:
        nav_df = nav.reset_index().rename(columns={'index': 'ts', 0: 'nav'})
        tgt_df = pd.DataFrame({'ts': tgt})
        nav_df['ts'] = pd.to_datetime(nav_df['ts'])
        nav_df = nav_df.sort_values('ts')
        tgt_df = tgt_df.sort_values('ts')
        merged = pd.merge_asof(tgt_df, nav_df, on='ts', direction='backward')
        nav_full = pd.Series(merged['nav'].values, index=tgt)
    return nav_full


def _plot_zoom_generic(sub, trad_res=None, res_res=None, title=None, outpath=None):
    if sub is None or sub.empty:
        return False
    fig, ax = plt.subplots(figsize=(14, 6))
    try:
        ax.plot(sub.index, sub['price'], label='price', color='black')
    except Exception:
        ax.plot(sub.index, np.asarray(sub['price'].to_list()), label='price', color='black')
    if 'ma_short' in sub.columns:
        ax.plot(sub.index, sub['ma_short'], label=f'MA{MA_SHORT}', color='orange', alpha=0.8)
    if 'ma_long' in sub.columns:
        ax.plot(sub.index, sub['ma_long'], label=f'MA{MA_LONG}', color='green', alpha=0.8)

    if 'trad_signal' in sub.columns:
        trad_buy = sub[sub['trad_signal'] == 'buy']
        trad_sell = sub[sub['trad_signal'] == 'sell']
        if not trad_buy.empty:
            ax.scatter(trad_buy.index, trad_buy['price'], marker='P', color='blue',
                       s=120, edgecolors='black', zorder=6, label='trad BUY')
        if not trad_sell.empty:
            ax.scatter(trad_sell.index, trad_sell['price'], marker='X', color='navy',
                       s=120, edgecolors='black', zorder=6, label='trad SELL')
    if 'res_signal' in sub.columns:
        res_buy = sub[sub['res_signal'] == 'buy']
        res_sell = sub[sub['res_signal'] == 'sell']
        if not res_buy.empty:
            ax.scatter(res_buy.index, res_buy['price'], marker='^', color='magenta',
                       s=100, edgecolors='k', zorder=7, label='res BUY')
        if not res_sell.empty:
            ax.scatter(res_sell.index, res_sell['price'], marker='v', color='orange',
                       s=100, edgecolors='k', zorder=7, label='res SELL')

    plot_start = sub.index.min()
    plot_end = sub.index.max()

    # Open lots (trad)
    trad_open_lots = trad_res.get('open_lots', []) if trad_res else []
    for lot in trad_open_lots:
        try:
            entry_ts = pd.to_datetime(lot['ts'])
            sl = float(lot['stop_loss'])
            entry_price = float(lot.get('entry_price', np.nan))
        except Exception:
            continue
        if entry_ts <= plot_end:
            start_x = max(entry_ts, plot_start)
            ax.hlines(sl, start_x, plot_end, colors='red', linestyles='dashed',
                      alpha=0.6, linewidth=1.0)
            ax.scatter(start_x, entry_price, marker='o', color='red', s=30,
                       alpha=0.6, zorder=5)

    # Open lots (res)
    res_open_lots = res_res.get('open_lots', []) if res_res else []
    for lot in res_open_lots:
        try:
            entry_ts = pd.to_datetime(lot['ts'])
            sl = float(lot['stop_loss'])
            entry_price = float(lot.get('entry_price', np.nan))
        except Exception:
            continue
        if entry_ts <= plot_end:
            start_x = max(entry_ts, plot_start)
            ax.hlines(sl, start_x, plot_end, colors='darkred', linestyles='dashed',
                      alpha=0.5, linewidth=1.0)
            ax.scatter(start_x, entry_price, marker='o', color='darkred', s=24,
                       alpha=0.6, zorder=5)

    ax.set_title(title if title else 'ZOOM')
    ax.legend(loc='upper left', fontsize='small')
    ax.grid(True)
    plt.xticks(rotation=30)
    try:
        fig.tight_layout()
        fig.savefig(outpath, dpi=150, bbox_inches='tight')
        plt.close(fig)
        print("Zoom plot saved:", outpath)
        return True
    except Exception as e:
        print("Zoom plot save error:", e)
        return False


def combine_and_output(df, trad_res, res_res, lookback=300, recent_hours=168):
    """
    Erzeugt Plots und CSV-Ausgaben.
    recent_hours: Zoom-Fenster in Stunden (168h = 7 Tage).
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    sig_fn = os.path.join(OUTPUT_DIR, f"signals_{ts}.csv")
    try:
        df.to_csv(sig_fn)
    except Exception:
        pass

    trades_trad_df = trad_res.get('trades', pd.DataFrame()) if trad_res else pd.DataFrame()
    trades_res_df = res_res.get('trades', pd.DataFrame()) if res_res else pd.DataFrame()
    try:
        trades_trad_df.to_csv(os.path.join(OUTPUT_DIR, f"trades_traditional_{ts}.csv"), index=False)
        trades_res_df.to_csv(os.path.join(OUTPUT_DIR, f"trades_resonance_{ts}.csv"), index=False)
    except Exception:
        pass

    try:
        if trad_res and 'nav_series' in trad_res and not trad_res['nav_series'].empty:
            trad_res['nav_series'].to_csv(
                os.path.join(OUTPUT_DIR, f"nav_traditional_{ts}.csv"), header=['nav']
            )
        if res_res and 'nav_series' in res_res and not res_res['nav_series'].empty:
            res_res['nav_series'].to_csv(
                os.path.join(OUTPUT_DIR, f"nav_resonance_{ts}.csv"), header=['nav']
            )
    except Exception:
        pass

    now = df.index.max()
    recent_td = pd.Timedelta(hours=recent_hours)
    recent_start = now - recent_td
    recent_mask = df.index >= recent_start
    diag_lines = [
        f"Diagnostics generated at {datetime.now().isoformat()}",
        f"Data timeframe: {df.index.min()} .. {df.index.max()} ({len(df)} rows)",
        f"Zoom window: last {recent_hours}h -> {recent_start} .. {now}",
        f"MA params (from config.py): MA_SHORT={MA_SHORT}, MA_LONG={MA_LONG}, VOL={VOL_WINDOW}",
    ]
    if 'trad_signal' in df.columns:
        diag_lines.append(
            f"Trad signals (last {recent_hours}h): "
            f"{df.loc[recent_mask, 'trad_signal'].value_counts().to_dict()}"
        )
    if 'res_signal' in df.columns:
        diag_lines.append(
            f"Res signals  (last {recent_hours}h): "
            f"{df.loc[recent_mask, 'res_signal'].value_counts().to_dict()}"
        )

    summary_path = os.path.join(OUTPUT_DIR, f"summary_{ts}.txt")
    try:
        with open(summary_path, "w") as f:
            f.write("\n".join(diag_lines))
    except Exception:
        pass
    print("\n".join(diag_lines))

    # --- ZOOM plot (recent_hours) ---
    if recent_mask.any():
        sub = df.loc[recent_mask].copy()
    else:
        sub = df.tail(lookback).copy()

    if not sub.empty:
        title = (
            f'ZOOM ({recent_hours}h): Price with Traditional vs Resonance signals '
            f'({sub.index.min()} .. {sub.index.max()})'
        )
        plot_zoom = os.path.abspath(
            os.path.join(OUTPUT_DIR, f"combined_signals_zoom_{ts}.png")
        )
        _plot_zoom_generic(sub, trad_res=trad_res, res_res=res_res,
                           title=title, outpath=plot_zoom)

    # --- EXTRA ZOOM: last 24h ---
    h24_td = pd.Timedelta(hours=24)
    h24_start = now - h24_td
    mask_24h = df.index >= h24_start
    if mask_24h.any():
        sub_24h = df.loc[mask_24h].copy()
    else:
        sub_24h = df.tail(min(len(df), 48)).copy()

    if not sub_24h.empty:
        title_24h = (
            f'ZOOM (24h): Last 24 hours Price & Signals '
            f'({sub_24h.index.min()} .. {sub_24h.index.max()})'
        )
        plot_24h = os.path.abspath(
            os.path.join(OUTPUT_DIR, f"combined_signals_24h_zoom_{ts}.png")
        )
        _plot_zoom_generic(sub_24h, trad_res=trad_res, res_res=res_res,
                           title=title_24h, outpath=plot_24h)

    # --- FULL plot ---
    fig2, ax_top = plt.subplots(figsize=(16, 8))
    try:
        ax_top.plot(df.index, df['price'], label='price', color='black', linewidth=0.8)
    except Exception:
        ax_top.plot(df.index, np.asarray(df['price'].to_list()),
                    label='price', color='black', linewidth=0.8)
    if 'ma_short' in df.columns:
        ax_top.plot(df.index, df['ma_short'], label=f'MA{MA_SHORT}',
                    color='orange', alpha=0.8)
    if 'ma_long' in df.columns:
        ax_top.plot(df.index, df['ma_long'], label=f'MA{MA_LONG}',
                    color='green', alpha=0.8)

    if 'trad_signal' in df.columns:
        tb_full = df[df['trad_signal'] == 'buy']
        ts_full = df[df['trad_signal'] == 'sell']
        if not tb_full.empty:
            ax_top.scatter(tb_full.index, tb_full['price'], marker='P', color='blue',
                           s=40, edgecolors='black', zorder=6, label='trad BUY')
        if not ts_full.empty:
            ax_top.scatter(ts_full.index, ts_full['price'], marker='X', color='navy',
                           s=40, edgecolors='black', zorder=6, label='trad SELL')
    if 'res_signal' in df.columns:
        rb_full = df[df['res_signal'] == 'buy']
        rs_full = df[df['res_signal'] == 'sell']
        if not rb_full.empty:
            ax_top.scatter(rb_full.index, rb_full['price'], marker='^', color='magenta',
                           s=30, edgecolors='k', zorder=7, label='res BUY')
        if not rs_full.empty:
            ax_top.scatter(rs_full.index, rs_full['price'], marker='v', color='orange',
                           s=30, edgecolors='k', zorder=7, label='res SELL')

    ax_top.set_title('FULL: Price with signals (hourly)')
    ax_top.legend(loc='upper left', fontsize='small')
    ax_top.grid(True)

    ax_eq = ax_top.twinx()
    trad_nav_full = align_nav_to_index(
        trad_res.get('nav_series') if trad_res else None, df.index
    )
    res_nav_full = align_nav_to_index(
        res_res.get('nav_series') if res_res else None, df.index
    )
    plotted_any = False
    if trad_nav_full is not None:
        ax_eq.plot(df.index, trad_nav_full.values, label='Equity Traditional',
                   color='blue', alpha=0.9, linewidth=1.2)
        plotted_any = True
    if res_nav_full is not None:
        ax_eq.plot(df.index, res_nav_full.values, label='Equity Resonance',
                   color='magenta', alpha=0.9, linewidth=1.2)
        plotted_any = True
    if plotted_any:
        ax_eq.set_ylabel('NAV')
        ax_eq.legend(loc='upper right', fontsize='small')

    plt.xticks(rotation=30)
    plot_full = os.path.abspath(
        os.path.join(OUTPUT_DIR, f"combined_signals_full_{ts}.png")
    )
    try:
        fig2.tight_layout()
        fig2.savefig(plot_full, dpi=150, bbox_inches='tight')
        plt.close(fig2)
        print("Full plot saved:", plot_full)
    except Exception as e:
        print("Full plot save error:", e)

    print("Outputs written to:", os.path.abspath(OUTPUT_DIR))


# ====== MAIN ======

def main():
    args = parse_args()

    # Zeitfenster-Info
    if args.start and args.end:
        print(f"\n{'=' * 60}")
        print(f"Resonanz-Analyse: Abschnitt {args.start} bis {args.end}")
        print(f"{'=' * 60}")
    else:
        print(f"\n{'=' * 60}")
        print(f"Resonanz-Analyse: letzte {args.period}")
        print(f"{'=' * 60}")

    try:
        df = load_data(
            symbol=args.symbol,
            period=args.period,
            interval=INTERVAL,
            start=args.start,
            end=args.end,
        )
    except Exception as e:
        print(f"\n❌ Keine Datenquelle verfügbar: {e}")
        print("Prüfe Internetverbindung und versuche es erneut.")
        return

    if df.empty:
        print("\n❌ Keine Daten geladen — Analyse abgebrochen.")
        return

    print(f"Data loaded: {len(df)} rows, {df.index.min()} to {df.index.max()}")

    print("Computing traditional signals...")
    df_trad = compute_traditional_signals(df)
    print("Computing resonance signals...")
    df_res = compute_resonance_signals(df)

    # merge
    df_merged = df.copy()
    trad_cols = ['ma_short', 'ma_long', 'rsi', 'trad_signal', 'trad_signal_trend']
    for col in trad_cols:
        if col in df_trad.columns:
            df_merged[col] = df_trad[col]

    res_cols = ['amplitude', 'time_comp', 'fft_period', 'resonance_score',
                'use_grid', 'direction_hint', 'res_signal']
    for col in res_cols:
        if col in df_res.columns:
            df_merged[col] = df_res[col]

    df_merged['trad_signal'] = df_merged['trad_signal'].fillna('hold')
    df_merged['res_signal'] = df_merged['res_signal'].fillna('hold')

    print("Running backtests...")
    trad_res = backtest_traditional(df_merged)
    res_res = backtest_resonance_grid(df_merged)

    trad_metrics = trad_res.get('metrics', {})
    res_metrics = res_res.get('metrics', {})

    print("Traditional NAV: {:.2f}, trades: {}".format(
        trad_res.get('nav', np.nan), len(trad_res.get('trades', pd.DataFrame()))
    ))
    print("Resonance NAV: {:.2f}, trades: {}".format(
        res_res.get('nav', np.nan), len(res_res.get('trades', pd.DataFrame()))
    ))

    print("\n--- Backtest Metrics ---")
    print(f"  Traditional:")
    print(f"    Total Return:  {trad_metrics.get('total_return', np.nan):.4f}")
    print(f"    Annual Return: {trad_metrics.get('annual_return', np.nan):.4f}")
    print(f"    Sharpe Ratio:  {trad_metrics.get('sharpe', np.nan):.4f}")
    print(f"    Max Drawdown:  {trad_metrics.get('max_drawdown', np.nan):.4f}")
    print(f"  Resonance:")
    print(f"    Total Return:  {res_metrics.get('total_return', np.nan):.4f}")
    print(f"    Annual Return: {res_metrics.get('annual_return', np.nan):.4f}")
    print(f"    Sharpe Ratio:  {res_metrics.get('sharpe', np.nan):.4f}")
    print(f"    Max Drawdown:  {res_metrics.get('max_drawdown', np.nan):.4f}")

    combine_and_output(df_merged, trad_res, res_res, lookback=300, recent_hours=168)

    print("\nEvaluating historical predictive power...")
    summary = evaluate_signal_probabilities(
        df_merged,
        signal_cols=('res_signal', 'trad_signal'),
        horizons=('1D', '3D', '7D'),
        thresholds=(0.01, 0.03, 0.05),
        output_dir=OUTPUT_DIR,
    )

    df_with_posteriors = add_posterior_probs_from_summary(
        df_merged, summary,
        signal_cols=('res_signal', 'trad_signal'),
        horizons=('1D', '3D', '7D'),
        threshold=0.01,
        output_dir=OUTPUT_DIR,
    )

    print("\nPosterior probabilities added. Sample:")
    prob_cols = [c for c in df_with_posteriors.columns if isinstance(c, str) and c.startswith('prob_')]
    show_cols = ['res_signal', 'trad_signal'] + prob_cols[:4]
    show_cols = [c for c in show_cols if c in df_with_posteriors.columns]
    print(df_with_posteriors[show_cols].tail(5))

    print(f"\nLetzter Datenpunkt: {df_with_posteriors.index[-1]}")
    last_price = df_with_posteriors['price'].iloc[-1]
    if isinstance(last_price, pd.Series):
        last_price = last_price.iloc[0]
    print(f"Letzter Preis: {float(last_price):.2f} USD")

    # Abschnitt-Info am Ende
    if args.start and args.end:
        print(f"\n{'=' * 60}")
        print(f"✅ Abschnitt {args.start} bis {args.end} abgeschlossen.")
        print(f"   {len(df)} Datenpunkte analysiert.")
        print(f"   Nächster Schritt: python main.py 20 500")
        print(f"{'=' * 60}")


if __name__ == "__main__":
    main()