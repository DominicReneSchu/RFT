"""
Daten-Pipeline V9.3 mit flexiblem Intervall-Handling.

Änderungen V9.3:
  - load_or_download_btc_history akzeptiert interval-Parameter
  - Cache-Datei mit Interval-Suffix (btc_history_1d.csv, btc_history_1h.csv)
  - _generate_synthetic_btc unterstützt 1h- und 24h-Kerzen
  - _fetch_from_binance gibt interval durch
"""
import math
from datetime import datetime, timedelta, timezone
from io import StringIO
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import requests

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# V9.3: Legacy-Pfad bleibt als Fallback
BTC_HISTORY_CSV = DATA_DIR / "btc_history.csv"

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
STOOQ_URL = "https://stooq.com/q/d/l/"
BINANCE_URL = "https://api.binance.com/api/v3/klines"

ANALYSIS_OUTPUT_DIR = Path("resonance_output_v2")


def _cache_path_for_interval(interval: str) -> Path:
    """V9.3: Cache-Datei mit Interval-Suffix."""
    safe_interval = interval.replace(" ", "").lower()
    return DATA_DIR / f"btc_history_{safe_interval}.csv"


def _fetch_from_coingecko(days: int = 365 * 3) -> pd.DataFrame:
    params = {"vs_currency": "usd", "days": days}
    resp = requests.get(COINGECKO_URL, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    prices = data.get("prices", [])
    if not prices:
        raise RuntimeError("Keine Preisdaten von CoinGecko erhalten")

    rows = []
    for ts_ms, price in prices:
        ts = datetime.fromtimestamp(ts_ms / 1000.0, tz=timezone.utc)
        rows.append({"ts": ts.isoformat(), "price": float(price)})

    df = pd.DataFrame(rows)
    df = df.sort_values("ts").reset_index(drop=True)
    return df


def _fetch_from_stooq() -> pd.DataFrame:
    params = {"s": "BTCUSD.US", "i": "d"}
    resp = requests.get(STOOQ_URL, params=params, timeout=30)
    resp.raise_for_status()
    csv_buf = StringIO(resp.text)
    df = pd.read_csv(csv_buf)

    possible_date_cols = ["Date", "date"]
    possible_close_cols = ["Close", "close", "CLOSE"]

    date_col = next((c for c in possible_date_cols if c in df.columns), None)
    close_col = next((c for c in possible_close_cols if c in df.columns), None)

    if date_col is None or close_col is None:
        raise RuntimeError(f"Unerwartetes Format von stooq.com, Spalten: {list(df.columns)}")

    df = df.sort_values(date_col).reset_index(drop=True)
    df["ts"] = (
        pd.to_datetime(df[date_col])
        .dt.tz_localize("UTC")
        .dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")
    )
    df["price"] = df[close_col].astype(float)
    df = df[["ts", "price"]].dropna()
    df = df.sort_values("ts").reset_index(drop=True)
    return df


def _fetch_from_binance(days: int = 365 * 3, interval: str = "1d") -> pd.DataFrame:
    """
    Holt BTCUSDT-Kerzen von Binance (Spot). Keine API-Keys nötig.
    V9.3: interval-Parameter wird durchgereicht.
    """
    limit = 1000

    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(days=days)

    def to_ms(dt: datetime) -> int:
        return int(dt.timestamp() * 1000)

    rows = []
    cur_start = start_time
    while cur_start < end_time:
        cur_end = min(cur_start + timedelta(days=limit), end_time)
        params = {
            "symbol": "BTCUSDT",
            "interval": interval,
            "startTime": to_ms(cur_start),
            "endTime": to_ms(cur_end),
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
            ts = datetime.fromtimestamp(open_time_ms / 1000.0, tz=timezone.utc)
            rows.append({"ts": ts.isoformat(), "price": close_price})

        last_open_ms = data[-1][0]
        last_open_dt = datetime.fromtimestamp(last_open_ms / 1000.0, tz=timezone.utc)
        cur_start = last_open_dt + timedelta(milliseconds=1)

    if not rows:
        raise RuntimeError("Keine Daten von Binance erhalten")

    df = pd.DataFrame(rows)
    df = df.sort_values("ts").reset_index(drop=True)
    return df


def _generate_synthetic_btc(days: int = 365 * 3, interval_hours: int = 24) -> pd.DataFrame:
    """
    Fallback: künstlicher BTC-Chart (sinusförmig + Rauschen).
    V9.3: Unterstützt verschiedene Kerzenintervalle (1h, 4h, 24h).
    """
    print(f"[Data] Erzeuge synthetischen BTC-Chart (Fallback, {interval_hours}h-Kerzen).")
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(days=days)

    times = []
    prices = []
    n = days * 24 // interval_hours
    base_price = 20000.0
    amp = 20000.0
    rng = np.random.default_rng(42)

    for i in range(n):
        t = start_time + timedelta(hours=i * interval_hours)
        phase = 2 * math.pi * i / (365 * 24 / interval_hours)
        price = base_price + amp * math.sin(phase) + rng.normal(0, 1000)
        price = max(1000.0, price)
        times.append(t.isoformat())
        prices.append(price)

    df = pd.DataFrame({"ts": times, "price": prices})
    df = df.sort_values("ts").reset_index(drop=True)
    return df


def _interval_to_hours(interval: str) -> int:
    """Konvertiert Binance-Interval-String in Stunden."""
    mapping = {
        "1h": 1, "2h": 2, "4h": 4, "6h": 6, "8h": 8, "12h": 12,
        "1d": 24, "3d": 72, "1w": 168,
    }
    return mapping.get(interval.lower(), 24)


def load_or_download_btc_history(
    days: int = 365 * 3,
    force_download: bool = False,
    interval: str = "1d",
) -> pd.DataFrame:
    """
    Lädt BTC-Historie aus lokaler CSV oder versucht mehrere Quellen:
      1. lokale CSV (falls vorhanden und nicht force_download)
      2. Binance (BTCUSDT, mit interval)
      3. CoinGecko
      4. Stooq
      5. synthetischer Fallback

    V9.3: Cache-Datei mit Interval-Suffix, interval wird an Binance durchgereicht.
    """
    cache_file = _cache_path_for_interval(interval)

    # 0) Lokale CSV (interval-spezifisch)
    if cache_file.exists() and not force_download:
        try:
            df = pd.read_csv(cache_file)
            if not df.empty and {"ts", "price"}.issubset(df.columns):
                print(f"[Data] Lade BTC-Historie aus {cache_file.name} ({len(df)} Zeilen).")
                return df
        except Exception:
            pass

    # Fallback: Legacy-Pfad (ohne Interval-Suffix)
    if BTC_HISTORY_CSV.exists() and not force_download and not cache_file.exists():
        try:
            df = pd.read_csv(BTC_HISTORY_CSV)
            if not df.empty and {"ts", "price"}.issubset(df.columns):
                print(f"[Data] Lade BTC-Historie aus Legacy-Datei ({len(df)} Zeilen).")
                return df
        except Exception:
            pass

    last_error = None

    # 1) Binance
    try:
        print(f"[Data] Versuche Download von Binance (BTCUSDT, {interval}) ...")
        df = _fetch_from_binance(days=days, interval=interval)
        df.to_csv(cache_file, index=False)
        print(f"[Data] BTC-Historie von Binance geladen, Zeilen: {len(df)}")
        return df
    except Exception as e:
        print(f"[Data] Binance fehlgeschlagen ({e}), versuche CoinGecko ...")
        last_error = e

    # 2) CoinGecko
    try:
        df = _fetch_from_coingecko(days=days)
        df.to_csv(cache_file, index=False)
        print(f"[Data] BTC-Historie von CoinGecko geladen, Zeilen: {len(df)}")
        return df
    except Exception as e:
        print(f"[Data] CoinGecko fehlgeschlagen ({e}), versuche stooq.com ...")
        last_error = e

    # 3) Stooq
    try:
        df = _fetch_from_stooq()
        df.to_csv(cache_file, index=False)
        print(f"[Data] BTC-Historie von stooq.com geladen, Zeilen: {len(df)}")
        return df
    except Exception as e:
        print(f"[Data] stooq.com fehlgeschlagen ({e}), verwende synthetischen Chart ...")
        last_error = e

    # 4) synthetischer Fallback
    interval_hours = _interval_to_hours(interval)
    df = _generate_synthetic_btc(days=days, interval_hours=interval_hours)
    df.to_csv(cache_file, index=False)
    print(f"[Data] Synthetischer BTC-Chart erzeugt, Zeilen: {len(df)}")
    return df


# ===== Loader für Analysetool-CSV mit Posteriors =====

def _find_latest_signals_with_posteriors() -> Optional[Path]:
    """
    Sucht in resonance_output_v2 nach der neuesten Datei
    'signals_with_posteriors_*.csv'.
    """
    if not ANALYSIS_OUTPUT_DIR.exists():
        return None
    candidates = sorted(ANALYSIS_OUTPUT_DIR.glob("signals_with_posteriors_*.csv"))
    if not candidates:
        return None
    return candidates[-1]


def load_analysis_signals(path: Optional[str] = None) -> pd.DataFrame:
    """
    Lädt die vom resonance_analysis.py erzeugte CSV mit Posterior-Infos.

    Reihenfolge:
      1) Wenn path angegeben: nutze diesen Pfad.
      2) Sonst: suche im Ordner resonance_output_v2 nach der neuesten
         signals_with_posteriors_*.csv.

    Erwartet mindestens Spalten:
      - 'price'
      - 'res_signal', 'trad_signal'
      - prob_res_signal_*_* (Posterior-Spalten)
    """
    if path is not None:
        csv_path = Path(path)
    else:
        csv_path = _find_latest_signals_with_posteriors()
        if csv_path is None:
            raise FileNotFoundError(
                "Keine signals_with_posteriors_*.csv gefunden. "
                "Bitte zuerst resonance_analysis.py ausführen."
            )

    df = pd.read_csv(csv_path)

    # Zeitindex rekonstruieren
    for ts_col in ["ts", "timestamp", "datetime", "Date"]:
        if ts_col in df.columns:
            df[ts_col] = pd.to_datetime(df[ts_col])
            df = df.set_index(ts_col).sort_index()
            break

    if "price" not in df.columns:
        raise ValueError(f"'price'-Spalte fehlt in {csv_path}")

    # Robust: Strings wie 'BTC-USD' -> NaN, dann verwerfen
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df.dropna(subset=["price"])

    return df


def has_analysis_signals() -> bool:
    """Prüft ob Resonanz-Analyse-Daten vorhanden sind."""
    return _find_latest_signals_with_posteriors() is not None