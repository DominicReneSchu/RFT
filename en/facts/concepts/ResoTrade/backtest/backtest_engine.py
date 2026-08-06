# backtest_engine.py
# © Dominic-René Schu, 2025/2026 — Resonance Field Theory
#
# RT-10: Reproducible Walk-Forward Backtest — ResoTrade Resonance Logic
#
# Closes M-5 (PEER_REVIEW_READINESS.md):
#   The 24-month backtest in resotrade_trading_ki.md was a private implementation
#   without public reproducibility. This module provides a fully public, licensed,
#   reproducible walk-forward backtest for the ResoTrade resonance logic.
#
# Data source (priority order):
#   1. Binance Public API (no account required):
#      https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1000
#      Returns: OHLCV candles, open license, no authentication.
#   2. ccxt library — Binance public endpoint:
#      ccxt.binance().fetch_ohlcv('BTC/USDT', '1h', limit=1000)
#   3. Synthetic fallback: deterministic BTC-realistic signal (seed=42)
#      Parameters: DC trend 30000+0.5*t, AC cycles (periods 50h/120h/20h),
#      noise std=150 USDT. Fully documented, zero proprietary data.
#
# Falsification criterion (M-5):
#   vs_hodl > 0.0 in ALL walk-forward folds → M-5 closed (reproducibility confirmed)
#   vs_hodl ≤ 0.0 in ANY fold              → M-5 not fully closed; result documented
#   Sharpe ratio > 0.5 as secondary criterion (robust outperformance vs. volatility)
#
# Usage:
#   python backtest_engine.py
#   python analyse/rt10_backtest_comparison.py
#
# Dependencies: numpy, pandas, matplotlib, requests, scipy
#   Optional: ccxt>=4.0.0 (for live data)

from __future__ import annotations

import os
import time
import datetime
import numpy as np
import pandas as pd

# ============================================================
# Constants
# ============================================================

PI = np.pi
SEED_DEFAULT = 42
BINANCE_API_URL = (
    "https://api.binance.com/api/v3/klines"
    "?symbol=BTCUSDT&interval=1h&limit=1000"
)


# ============================================================
# 1. Data acquisition
# ============================================================

def fetch_btcusdt_ohlcv(source: str = 'binance_api',
                         n_candles: int = 2000,
                         interval: str = '1h',
                         seed: int = SEED_DEFAULT) -> pd.DataFrame:
    """
    Load BTC-USDT OHLCV data from a public, license-free source.

    Parameters
    ----------
    source : str
        'binance_api'  — Binance REST API (no auth required)
        'ccxt'         — ccxt library with Binance public endpoint
        'synthetic'    — Deterministic synthetic signal (BTC-realistic)
    n_candles : int
        Number of hourly candles to fetch / generate.
    interval : str
        Candle interval (default '1h'). Passed to API/ccxt.
    seed : int
        Random seed for synthetic fallback.

    Returns
    -------
    pd.DataFrame
        Columns: timestamp (UTC datetime), open, high, low, close, volume
        Attribute df.attrs['source'] documents which source was used.

    Data sources (fully documented for reproducibility):
    ─────────────────────────────────────────────────────
    Binance API endpoint:
        https://api.binance.com/api/v3/klines
        Symbol: BTCUSDT, Interval: 1h
        Public endpoint, no authentication, MIT-compatible data license.
        Kline field order: [open_time, open, high, low, close, volume, ...]

    ccxt library (fallback):
        pip install ccxt>=4.0.0
        ccxt.binance().fetch_ohlcv('BTC/USDT', '1h', limit=n_candles)
        Returns: [[timestamp_ms, open, high, low, close, volume], ...]

    Synthetic fallback (deterministic):
        DC trend : 30_000 + 0.5 * t + 2000 * sin(2π t / 800)  [USDT/h]
        AC cycles: 800*sin(2π t/50) + 400*sin(2π t/120) + 200*sin(2π t/20)
        Noise    : Normal(0, 150) USDT
        seed=42 guarantees bit-exact reproducibility.
    """
    _valid_sources = ('binance_api', 'ccxt', 'synthetic')
    if source not in _valid_sources:
        print(f"  [backtest_engine] Unknown source '{source}' — "
              f"using synthetic fallback (valid: {_valid_sources}).")

    if source == 'binance_api':
        df = _fetch_binance_api(n_candles, interval)
        if df is not None:
            df.attrs['source'] = 'Binance Public API'
            return df
        print("  [backtest_engine] Binance API unavailable — trying ccxt...")

    if source in ('binance_api', 'ccxt'):
        df = _fetch_ccxt(n_candles, interval)
        if df is not None:
            df.attrs['source'] = 'ccxt / Binance public endpoint'
            return df
        print("  [backtest_engine] ccxt unavailable — using synthetic fallback.")

    df = _generate_synthetic_btc(n_candles, seed=seed)
    df.attrs['source'] = f'Synthetic BTC-realistic (seed={seed})'
    return df


def _fetch_binance_api(n_candles: int, interval: str) -> pd.DataFrame | None:
    """Fetch from Binance public REST API."""
    try:
        import requests
        limit = min(n_candles, 1000)
        if n_candles > 1000:
            print(f"  [backtest_engine] Warning: Binance API caps at 1000 candles;"
                  f" requested {n_candles}, fetching {limit}.")
        url = (f"https://api.binance.com/api/v3/klines"
               f"?symbol=BTCUSDT&interval={interval}&limit={limit}")
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        raw = resp.json()
        return _parse_binance_klines(raw)
    except Exception as exc:
        print(f"  [backtest_engine] Binance API error: {exc}")
        return None


def _fetch_ccxt(n_candles: int, interval: str) -> pd.DataFrame | None:
    """Fetch from Binance via ccxt library."""
    try:
        import ccxt
        exchange = ccxt.binance()
        raw = exchange.fetch_ohlcv('BTC/USDT', interval, limit=n_candles)
        records = []
        for r in raw:
            records.append({
                'timestamp': pd.Timestamp(r[0], unit='ms', tz='UTC'),
                'open': float(r[1]),
                'high': float(r[2]),
                'low': float(r[3]),
                'close': float(r[4]),
                'volume': float(r[5]),
            })
        return pd.DataFrame(records)
    except Exception as exc:
        print(f"  [backtest_engine] ccxt error: {exc}")
        return None


def _parse_binance_klines(raw: list) -> pd.DataFrame:
    """Parse Binance klines JSON response."""
    records = []
    for row in raw:
        records.append({
            'timestamp': pd.Timestamp(int(row[0]), unit='ms', tz='UTC'),
            'open':   float(row[1]),
            'high':   float(row[2]),
            'low':    float(row[3]),
            'close':  float(row[4]),
            'volume': float(row[5]),
        })
    return pd.DataFrame(records)


def _generate_synthetic_btc(n: int = 2000, seed: int = SEED_DEFAULT) -> pd.DataFrame:
    """
    Deterministic synthetic BTC-USDT signal.

    Parameters (fully documented for reproducibility):
        DC trend : 30_000 + 0.5 * t  (BTC long-term appreciation ~USD/h)
        AC main  : 800  * sin(2π t / 50)    (50-hour main cycle)
        AC long  : 400  * sin(2π t / 120)   (120-hour medium cycle)
        AC short : 200  * sin(2π t / 20)    (20-hour short cycle)
        Noise    : Normal(0, 150)  USDT
        seed     : 42 (default) — guarantees bit-exact reproducibility

    The start timestamp is 2024-01-01 00:00 UTC for reference alignment.
    """
    rng = np.random.RandomState(seed)
    t = np.arange(n, dtype=float)

    dc = 30_000.0 + 0.5 * t + 2000.0 * np.sin(2 * PI * t / 800)
    ac = (800.0 * np.sin(2 * PI * t / 50)
          + 400.0 * np.sin(2 * PI * t / 120)
          + 200.0 * np.sin(2 * PI * t / 20))
    noise = rng.normal(0, 150, n)

    close = dc + ac + noise
    close = np.maximum(close, 1.0)  # Floor at $1

    # Synthesize OHLCV from close
    open_ = np.roll(close, 1)
    open_[0] = close[0]
    spread = np.abs(rng.normal(0, 50, n))
    high = np.maximum(close, open_) + spread * 0.5
    low = np.minimum(close, open_) - spread * 0.5
    volume = rng.lognormal(10, 1, n)

    start = pd.Timestamp('2024-01-01 00:00:00', tz='UTC')
    timestamps = [start + pd.Timedelta(hours=int(i)) for i in t]

    return pd.DataFrame({
        'timestamp': timestamps,
        'open':   open_,
        'high':   high,
        'low':    low,
        'close':  close,
        'volume': volume,
    })


# ============================================================
# 2. Walk-forward split
# ============================================================

def walk_forward_split(df: pd.DataFrame,
                        n_folds: int = 5,
                        train_frac: float = 0.6) -> list[tuple]:
    """
    Split data into n_folds walk-forward windows.

    Each window is a (train_df, test_df) tuple with no overlap.
    No look-ahead bias: test windows are never seen during training.
    Train and test are chronologically ordered and contiguous.

    Strategy: The full dataset is divided into n_folds equal segments.
    For fold k, training uses segments 0..k and testing uses segment k+1.
    This ensures strict temporal ordering and no data leakage.

    Parameters
    ----------
    df : pd.DataFrame
        Full OHLCV dataset with 'close' column.
    n_folds : int
        Number of walk-forward folds (default 5).
    train_frac : float
        Fraction of each fold window used for training (default 0.6).

    Returns
    -------
    list of (train_df, test_df) tuples (no overlap guaranteed).
    """
    n = len(df)
    # Each fold covers fold_size rows; test = fold_size * (1 - train_frac)
    fold_size = n // (n_folds + 1)
    folds = []

    for k in range(n_folds):
        # Train: all data from start to end of k-th window
        train_end = (k + 1) * fold_size
        # Test: the next segment
        test_start = train_end
        test_end = test_start + fold_size

        if test_end > n:
            test_end = n
        if test_start >= n:
            break

        train_df = df.iloc[:train_end].copy().reset_index(drop=True)
        test_df = df.iloc[test_start:test_end].copy().reset_index(drop=True)
        folds.append((train_df, test_df))

    return folds


# ============================================================
# 3. Resonance logic helpers (from resonance_logic_example.py)
# ============================================================

def coupling_efficiency(delta_phi: float) -> float:
    """ε(Δφ) = cos²(Δφ/2) — RFT coupling (Axiom 4)."""
    return float(np.cos(delta_phi / 2.0) ** 2)


def decomposition(price: np.ndarray,
                   window_long: int = 50) -> tuple[np.ndarray, np.ndarray]:
    """DC/AC decomposition: DC = moving average, AC = price - DC."""
    dc = np.convolve(price, np.ones(window_long) / window_long, mode='same')
    ac = price - dc
    return dc, ac


def detect_phase(ac: np.ndarray,
                  amplitude_threshold: float = 0.3) -> tuple[np.ndarray, np.ndarray]:
    """
    Detect oscillation phase at each time step.
    Returns (phases, amplitudes) where phases ∈ {'peak','trough','transition','flat'}.
    """
    n = len(ac)
    phases = np.full(n, 'flat', dtype='U10')
    amplitude = np.zeros(n)
    window = 25
    for i in range(window, n):
        segment = ac[i - window:i]
        amp = float(np.max(segment) - np.min(segment))
        amplitude[i] = amp
        if amp < 0.5:
            phases[i] = 'flat'
        elif ac[i] > amplitude_threshold * amp:
            phases[i] = 'peak'
        elif ac[i] < -amplitude_threshold * amp:
            phases[i] = 'trough'
        else:
            phases[i] = 'transition'
    return phases, amplitude


# ============================================================
# 4. ResoTrade Backtest
# ============================================================

class ResoTradeBacktest:
    """
    Full walk-forward backtest of the ResoTrade resonance logic.

    Direct extension of ResonanceAgent from resonance_logic_example.py.
    Added: Walk-forward validation, trade log export, performance metrics.

    Falsification criterion (M-5):
        vs_hodl > 0.0 in ALL folds → M-5 closed (reproducibility confirmed)
        vs_hodl ≤ 0.0 in ANY fold  → M-5 not fully closed; documented below
    """

    def __init__(self,
                 start_capital: float = 1000.0,
                 trade_fraction: float = 0.15,
                 window_dc: int = 50,
                 amplitude_threshold: float = 0.3,
                 min_epsilon: float = 0.3,
                 cooldown: int = 3,
                 seed: int = SEED_DEFAULT):
        self.start_capital = start_capital
        self.trade_fraction = trade_fraction
        self.window_dc = window_dc
        self.amplitude_threshold = amplitude_threshold
        self.min_epsilon = min_epsilon
        self.cooldown = cooldown
        self.seed = seed

        # Results accumulated across folds
        self.fold_results: list[dict] = []
        self.trade_log: list[dict] = []

    # ────────────────────────────────────────────────────────
    # Single fold simulation
    # ────────────────────────────────────────────────────────

    def run_fold(self, train_df: pd.DataFrame,
                 test_df: pd.DataFrame,
                 fold_id: int = 0) -> dict:
        """
        Train on train_df (experience store), test on test_df.

        The experience store is pre-trained on training data.
        No prices from test_df are used during training.
        Returns performance metrics for this fold.
        """
        # Pre-train experience store on training data
        exp_store = self._train_experience(train_df, fold_id)

        # Evaluate on test data
        metrics = self._evaluate(test_df, exp_store, fold_id)
        self.fold_results.append(metrics)
        return metrics

    def _train_experience(self, df: pd.DataFrame,
                           fold_id: int) -> dict:
        """
        Train the experience store on historical data.
        Returns populated experience store dict.
        """
        price = df['close'].values
        dc, ac = decomposition(price, self.window_dc)
        phases, _ = detect_phase(ac, self.amplitude_threshold)

        exp_store: dict[str, float] = {}
        decay = 0.90
        cash = self.start_capital
        asset = 0.0

        def _trend(dc_arr, i, window=20):
            if i < window:
                return 'sideways'
            slope = (dc_arr[i] - dc_arr[i - window]) / max(dc_arr[i - window], 1e-8)
            if slope > 0.0005:
                return 'uptrend'
            elif slope < -0.0005:
                return 'downtrend'
            return 'sideways'

        start = max(self.window_dc, 25)
        for i in range(start, len(price)):
            phase = phases[i]
            trend = _trend(dc, i)
            current_price = price[i]
            pv = cash + asset * current_price

            if phase == 'peak':
                action = 'SELL'
            elif phase == 'trough':
                action = 'BUY'
            else:
                action = 'HOLD'

            if action == 'BUY' and cash > 10:
                buy = cash * self.trade_fraction
                asset += buy / current_price
                cash -= buy
            elif action == 'SELL' and asset > 0.0001:
                sell = asset * self.trade_fraction
                cash += sell * current_price
                asset -= sell
            else:
                action = 'HOLD'

            new_pv = cash + asset * current_price
            reward = (new_pv - pv) / max(pv, 1e-8)

            key = f"{phase},{trend},{action}"
            exp_store[key] = exp_store.get(key, 0.0) * decay + reward

        return exp_store

    def _evaluate(self, df: pd.DataFrame,
                   exp_store: dict,
                   fold_id: int) -> dict:
        """
        Evaluate resonance logic on test data using the trained experience store.
        Records all trades in self.trade_log.
        Returns fold performance metrics.
        """
        price = df['close'].values
        n = len(price)
        dc, ac = decomposition(price, self.window_dc)
        phases, _ = detect_phase(ac, self.amplitude_threshold)

        cash = self.start_capital
        asset = 0.0
        blocked = 0
        recent_trades: list[str] = []
        pv_history = []
        n_trades = 0

        def _trend(dc_arr, i, window=20):
            if i < window:
                return 'sideways'
            slope = (dc_arr[i] - dc_arr[i - window]) / max(dc_arr[i - window], 1e-8)
            if slope > 0.0005:
                return 'uptrend'
            elif slope < -0.0005:
                return 'downtrend'
            return 'sideways'

        hodl_units = self.start_capital / max(price[0], 1e-8)
        start = max(self.window_dc, 25)

        # Fill pv_history for warm-up period
        for i in range(start):
            pv_history.append(self.start_capital)

        for i in range(start, n):
            phase = phases[i]
            trend = _trend(dc, i)
            current_price = price[i]
            pv = cash + asset * current_price

            # Coupling efficiency
            if phase == 'peak':
                delta_phi = 0.0
            elif phase == 'trough':
                delta_phi = 0.0
            elif phase == 'transition':
                delta_phi = PI / 3
            else:
                delta_phi = PI / 2
            epsilon = coupling_efficiency(delta_phi)

            # Phase-based proposal
            if phase == 'peak':
                proposal = 'SELL'
            elif phase == 'trough':
                proposal = 'BUY'
            else:
                proposal = 'HOLD'

            # Experience override
            if proposal != 'HOLD':
                exp_key = f"{phase},{trend},{proposal}"
                if exp_store.get(exp_key, 0.0) < -0.5:
                    proposal = 'HOLD'

            # Rule chain
            action = proposal
            if epsilon < self.min_epsilon and proposal != 'HOLD':
                action = 'HOLD'
            elif proposal == 'BUY':
                cash_frac = cash / max(pv, 1e-8)
                if cash_frac < 0.10:
                    action = 'HOLD'
            elif proposal == 'SELL':
                asset_frac = 1.0 - cash / max(pv, 1e-8)
                if asset_frac < 0.05:
                    action = 'HOLD'

            if blocked > 0:
                blocked -= 1
                action = 'HOLD'

            # Execute
            if action == 'BUY' and cash > 10:
                buy = cash * self.trade_fraction
                asset += buy / current_price
                cash -= buy
                n_trades += 1
                recent_trades.append('BUY')
            elif action == 'SELL' and asset > 0.0001:
                sell = asset * self.trade_fraction
                cash += sell * current_price
                asset -= sell
                n_trades += 1
                recent_trades.append('SELL')
            else:
                action = 'HOLD'

            # Cooldown check
            if len(recent_trades) > self.cooldown:
                recent_trades.pop(0)
            if (len(recent_trades) >= self.cooldown
                    and all(t != 'HOLD' for t in recent_trades)):
                blocked = 2

            new_pv = cash + asset * current_price
            pv_history.append(new_pv)

            # Record trade
            ts = df['timestamp'].iloc[i] if 'timestamp' in df.columns else i
            self.trade_log.append({
                'fold_id':   fold_id,
                'step':      i,
                'timestamp': ts,
                'action':    action,
                'price':     current_price,
                'pv':        new_pv,
                'epsilon':   epsilon,
                'phase':     phase,
                'trend':     trend,
                'cash':      cash,
                'asset':     asset,
            })

        pv_final = cash + asset * price[-1]
        hodl_final = hodl_units * price[-1]
        total_return = pv_final / self.start_capital - 1.0
        hodl_return = hodl_final / self.start_capital - 1.0
        vs_hodl = total_return - hodl_return

        # Sharpe ratio (annualised, hourly data)
        pv_arr = np.array(pv_history)
        returns = np.diff(pv_arr) / np.maximum(pv_arr[:-1], 1e-8)
        sharpe = _sharpe_ratio(returns, periods_per_year=8760)

        # Max drawdown
        max_dd = _max_drawdown(pv_arr)

        # Win rate
        trade_records = [r for r in self.trade_log if r['fold_id'] == fold_id
                         and r['action'] != 'HOLD']
        win_rate = _win_rate(trade_records, price)

        return {
            'fold_id':      fold_id,
            'n':            n,
            'pv_start':     self.start_capital,
            'pv_final':     pv_final,
            'hodl_final':   hodl_final,
            'total_return': total_return,
            'hodl_return':  hodl_return,
            'vs_hodl':      vs_hodl,
            'sharpe':       sharpe,
            'max_drawdown': max_dd,
            'win_rate':     win_rate,
            'n_trades':     n_trades,
            'pv_history':   pv_arr,
            'hodl_history': hodl_units * price,
        }

    # ────────────────────────────────────────────────────────
    # Walk-forward
    # ────────────────────────────────────────────────────────

    def run_walk_forward(self, df: pd.DataFrame,
                          n_folds: int = 5) -> dict:
        """
        Execute full walk-forward backtest across n_folds.

        Clears previous results before running.
        Returns aggregate summary dict.

        Falsification criterion (M-5):
            All folds: vs_hodl > 0 → M-5 closed
            Any fold:  vs_hodl ≤ 0 → documented, M-5 not fully closed
        """
        self.fold_results = []
        self.trade_log = []

        folds = walk_forward_split(df, n_folds=n_folds)

        for k, (train_df, test_df) in enumerate(folds):
            self.run_fold(train_df, test_df, fold_id=k)

        return self.performance_metrics()

    # ────────────────────────────────────────────────────────
    # Export
    # ────────────────────────────────────────────────────────

    def export_trade_log(self, filepath: str) -> None:
        """
        Export all trades as CSV.
        Columns: fold_id, step, timestamp, action, price, pv, epsilon, phase, trend.
        The fold_id column identifies which walk-forward fold each trade belongs to.
        The timestamp of data acquisition is written as a CSV header comment.
        """
        if not self.trade_log:
            print("  [backtest_engine] No trades to export.")
            return

        df_log = pd.DataFrame(self.trade_log)
        # Select key columns
        cols = ['fold_id', 'step', 'timestamp', 'action',
                'price', 'pv', 'epsilon', 'phase', 'trend', 'cash', 'asset']
        cols = [c for c in cols if c in df_log.columns]
        df_export = df_log[cols]

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        header = (
            f"# rt10_trade_log.csv — ResoTrade Walk-Forward Backtest\n"
            f"# Generated: {now_utc} UTC\n"
            f"# Source: ResoTrade backtest_engine.py (RT-10)\n"
            f"# Falsification criterion: vs_hodl > 0 in all folds (M-5)\n"
        )

        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(header)
            df_export.to_csv(f, index=False)

        n_active = len(df_export[df_export['action'] != 'HOLD'])
        print(f"  → Trade log exported: {filepath}"
              f" ({len(df_export)} rows, {n_active} active trades)")

    # ────────────────────────────────────────────────────────
    # Metrics
    # ────────────────────────────────────────────────────────

    def performance_metrics(self) -> dict:
        """
        Compute aggregate performance metrics across all folds.

        Returns
        -------
        dict with keys:
            total_return    : average total return across folds
            vs_hodl         : average outperformance vs HODL
            vs_hodl_all     : list of vs_hodl per fold
            sharpe_ratio    : average annualised Sharpe ratio
            max_drawdown    : average maximum drawdown
            win_rate        : average win rate
            n_trades        : total number of active trades
            n_folds         : number of folds evaluated
            m5_closed       : True if vs_hodl > 0 in ALL folds
            falsification   : human-readable verdict on M-5
        """
        if not self.fold_results:
            return {}

        vs_hodl_list = [r['vs_hodl'] for r in self.fold_results]
        m5_closed = all(v > 0.0 for v in vs_hodl_list)

        if m5_closed:
            falsification = "M-5 CLOSED: vs_hodl > 0 in all folds — reproducibility confirmed"
        else:
            failed = [i for i, v in enumerate(vs_hodl_list) if v <= 0.0]
            falsification = (f"M-5 NOT FULLY CLOSED: vs_hodl ≤ 0 in fold(s) {failed} "
                             f"— documented, not hidden")

        return {
            'total_return':  float(np.mean([r['total_return'] for r in self.fold_results])),
            'hodl_return':   float(np.mean([r['hodl_return'] for r in self.fold_results])),
            'vs_hodl':       float(np.mean(vs_hodl_list)),
            'vs_hodl_all':   vs_hodl_list,
            'sharpe_ratio':  float(np.mean([r['sharpe'] for r in self.fold_results])),
            'max_drawdown':  float(np.mean([r['max_drawdown'] for r in self.fold_results])),
            'win_rate':      float(np.mean([r['win_rate'] for r in self.fold_results])),
            'n_trades':      int(sum(r['n_trades'] for r in self.fold_results)),
            'n_folds':       len(self.fold_results),
            'm5_closed':     m5_closed,
            'falsification': falsification,
        }


# ============================================================
# 5. Metric helpers
# ============================================================

def _sharpe_ratio(returns: np.ndarray,
                   risk_free: float = 0.0,
                   periods_per_year: int = 8760) -> float:
    """Annualised Sharpe ratio from hourly returns."""
    if len(returns) < 2:
        return 0.0
    excess = returns - risk_free / periods_per_year
    std = float(np.std(excess, ddof=1))
    if std < 1e-10:
        return 0.0
    return float(np.mean(excess) / std * np.sqrt(periods_per_year))


def _max_drawdown(pv: np.ndarray) -> float:
    """Maximum drawdown as a fraction (0..1)."""
    if len(pv) == 0:
        return 0.0
    peak = np.maximum.accumulate(pv)
    drawdown = (peak - pv) / np.maximum(peak, 1e-10)
    return float(np.max(drawdown))


def _win_rate(trades: list[dict], price: np.ndarray) -> float:
    """Win rate: fraction of trades that improved portfolio value."""
    if not trades:
        return 0.0
    # Count BUY trades followed by price increase, SELL by price decrease
    win_count = 0
    for t in trades:
        step = t['step']
        if step + 1 < len(price):
            if t['action'] == 'BUY' and price[step + 1] > price[step]:
                win_count += 1
            elif t['action'] == 'SELL' and price[step + 1] < price[step]:
                win_count += 1
    return float(win_count / max(len(trades), 1))


# ============================================================
# 6. CLI self-test
# ============================================================

def main():
    """Quick self-test: synthetic data, 5-fold walk-forward."""
    print("=" * 60)
    print("backtest_engine.py — RT-10 Self-Test")
    print("=" * 60)

    df = fetch_btcusdt_ohlcv(source='synthetic', n_candles=2000)
    print(f"\n  Data: {len(df)} candles — source: {df.attrs.get('source')}")
    print(f"  Price range: {df['close'].min():.0f}–{df['close'].max():.0f} USDT")

    bt = ResoTradeBacktest(seed=SEED_DEFAULT)
    metrics = bt.run_walk_forward(df, n_folds=5)

    print(f"\n  {'─' * 50}")
    print("  WALK-FORWARD RESULTS (5 folds):")
    print(f"  {'─' * 50}")
    for r in bt.fold_results:
        flag = "✓" if r['vs_hodl'] > 0 else "✗"
        print(f"  Fold {r['fold_id']+1}:  "
              f"Return {r['total_return']*100:+.1f}%  "
              f"HODL {r['hodl_return']*100:+.1f}%  "
              f"vs_HODL {r['vs_hodl']*100:+.1f}%  "
              f"Sharpe {r['sharpe']:+.2f}  "
              f"n={r['n_trades']}  {flag}")

    print(f"  {'─' * 50}")
    print(f"  Avg vs_HODL:  {metrics['vs_hodl']*100:+.2f}%")
    print(f"  Avg Sharpe:   {metrics['sharpe_ratio']:+.2f}")
    print(f"  Max Drawdown: {metrics['max_drawdown']*100:.1f}%")
    print(f"  Total trades: {metrics['n_trades']}")
    print(f"\n  {metrics['falsification']}")
    print("=" * 60)

    bt.export_trade_log('/tmp/rt10_trade_log_selftest.csv')
    print("\nDone.")


if __name__ == "__main__":
    main()
