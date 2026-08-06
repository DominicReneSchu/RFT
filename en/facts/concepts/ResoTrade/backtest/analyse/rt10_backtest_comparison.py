# rt10_backtest_comparison.py
# © Dominic-René Schu, 2025/2026 — Resonance Field Theory
#
# RT-10: Walk-Forward Backtest — ResoTrade Resonance Logic
#        BTC-USDT · 5 Folds · Falsification Criterion M-5
#
# Closes M-5 (PEER_REVIEW_READINESS.md):
#   Public, reproducible walk-forward backtest of the ResoTrade resonance logic.
#   All results are reproducible: synthetic fallback uses seed=42.
#
# Falsification criterion:
#   vs_hodl > 0.0 in ALL folds → M-5 closed (reproducibility confirmed)
#   vs_hodl ≤ 0.0 in ANY fold  → M-5 not fully closed; documented, not hidden
#   Sharpe > 0.5 as secondary criterion
#
# Usage:
#   cd en/facts/concepts/ResoTrade/backtest
#   python analyse/rt10_backtest_comparison.py
#
# Output:
#   rt10_portfolio.png         — Portfolio curves (Reso vs HODL vs Random), all folds
#   rt10_epsilon.png           — ε(Δφ) time series with trade markers
#   rt10_vs_hodl_bars.png      — vs_hodl per fold (bar chart, falsification criterion)
#   rt10_drawdown.png          — Drawdown curve across all folds
#   analyse/rt10_trade_log.csv — Full trade log (fold_id, timestamp, action, ...)

from __future__ import annotations

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Path setup ────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))
_BACKTEST_DIR = os.path.dirname(_HERE)
sys.path.insert(0, _BACKTEST_DIR)

from backtest_engine import (
    fetch_btcusdt_ohlcv,
    walk_forward_split,
    ResoTradeBacktest,
    decomposition,
    detect_phase,
    coupling_efficiency,
    _sharpe_ratio,
    _max_drawdown,
    PI,
    SEED_DEFAULT,
)

# ── Output configuration ──────────────────────────────────
OUTPUT_DIR = _HERE
N_CANDLES = 2000
N_FOLDS = 5
SEED = SEED_DEFAULT

# ── Random baseline ────────────────────────────────────────

class _RandomAgent:
    """Baseline random agent (same interface as ResoTradeBacktest)."""

    def __init__(self, start_capital: float = 1000.0,
                 trade_fraction: float = 0.15,
                 seed: int = 123):
        self.start_capital = start_capital
        self.trade_fraction = trade_fraction
        self.rng = np.random.RandomState(seed)

    def simulate(self, price: np.ndarray) -> np.ndarray:
        cash = self.start_capital
        asset = 0.0
        pv_hist = []
        for p in price:
            action = self.rng.choice(['BUY', 'SELL', 'HOLD'], p=[0.2, 0.2, 0.6])
            if action == 'BUY' and cash > 10:
                buy = cash * self.trade_fraction
                asset += buy / p
                cash -= buy
            elif action == 'SELL' and asset > 0.0001:
                sell = asset * self.trade_fraction
                cash += sell * p
                asset -= sell
            pv_hist.append(cash + asset * p)
        return np.array(pv_hist)


# ============================================================
# Terminal table
# ============================================================

def print_results_table(bt: ResoTradeBacktest, metrics: dict) -> None:
    """Print RT-10 results in the style of RT-08/RT-09."""
    print()
    print("=" * 80)
    print("=== RT-10 WALK-FORWARD BACKTEST — ResoTrade Resonance Logic ===")
    print("=== BTC-USDT · 5 Folds · Falsification Criterion M-5         ===")
    print("=" * 80)
    print()

    # Per-fold table
    header = (f"{'Fold':>5}  {'Return':>8}  {'HODL':>8}  "
              f"{'vs_HODL':>8}  {'Sharpe':>7}  {'MaxDD':>7}  "
              f"{'WinRate':>7}  {'Trades':>6}  {'M-5':>6}")
    print(header)
    print("-" * 80)

    for r in bt.fold_results:
        flag = "✓ PASS" if r['vs_hodl'] > 0 else "✗ FAIL"
        print(
            f"{r['fold_id']+1:>5}  "
            f"{r['total_return']*100:>+7.1f}%  "
            f"{r['hodl_return']*100:>+7.1f}%  "
            f"{r['vs_hodl']*100:>+7.1f}%  "
            f"{r['sharpe']:>+6.2f}  "
            f"{r['max_drawdown']*100:>6.1f}%  "
            f"{r['win_rate']*100:>6.1f}%  "
            f"{r['n_trades']:>6}  "
            f"{flag}"
        )

    print("-" * 80)
    print(
        f"{'Avg':>5}  "
        f"{metrics['total_return']*100:>+7.1f}%  "
        f"{metrics['hodl_return']*100:>+7.1f}%  "
        f"{metrics['vs_hodl']*100:>+7.1f}%  "
        f"{metrics['sharpe_ratio']:>+6.2f}  "
        f"{metrics['max_drawdown']*100:>6.1f}%  "
        f"{metrics['win_rate']*100:>6.1f}%  "
        f"{metrics['n_trades']:>6}"
    )
    print()

    # Falsification verdict
    print(f"  Falsification criterion (M-5):")
    print(f"  {metrics['falsification']}")
    sharpe_pass = metrics['sharpe_ratio'] > 0.5
    sharpe_flag = "✓ PASS" if sharpe_pass else "✗ FAIL"
    print(f"  Sharpe > 0.5: {metrics['sharpe_ratio']:.2f} → {sharpe_flag}")
    print()
    print("=" * 80)


# ============================================================
# Plots
# ============================================================

def plot_portfolio(bt: ResoTradeBacktest,
                   df: pd.DataFrame,
                   output_dir: str) -> None:
    """Plot 1: Portfolio curves — Reso vs HODL vs Random (all folds)."""
    fig, axes = plt.subplots(N_FOLDS, 1, figsize=(16, 4 * N_FOLDS), sharex=False)
    if N_FOLDS == 1:
        axes = [axes]

    folds = walk_forward_split(df, n_folds=N_FOLDS)

    for k, (r, (_, test_df)) in enumerate(zip(bt.fold_results, folds)):
        ax = axes[k]
        price = test_df['close'].values
        pv_reso = r['pv_history']
        pv_hodl = r['hodl_history']

        # Random baseline
        rand = _RandomAgent(start_capital=bt.start_capital, seed=123 + k)
        pv_rand = rand.simulate(price)

        t = np.arange(len(pv_reso))

        vs = r['vs_hodl']
        flag = "✓" if vs > 0 else "✗"
        ax.plot(t, pv_reso, 'green', lw=2,
                label=f'Reso ({r["total_return"]*100:+.1f}%)')
        ax.plot(t, pv_hodl[:len(t)], 'blue', lw=1.5, ls='--',
                label=f'HODL ({r["hodl_return"]*100:+.1f}%)')
        ax.plot(t[:len(pv_rand)], pv_rand, 'red', lw=1, alpha=0.6,
                label='Random')

        ax.set_ylabel('Portfolio [USD]')
        ax.set_title(
            f'Fold {k+1} — vs_HODL: {vs*100:+.1f}% {flag}  |  '
            f'Sharpe: {r["sharpe"]:+.2f}  |  n_trades: {r["n_trades"]}')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        'RT-10: Portfolio Comparison — Reso vs HODL vs Random\n'
        'ResoTrade Walk-Forward Backtest · BTC-USDT · 5 Folds',
        fontsize=13, fontweight='bold')
    plt.tight_layout()
    path = os.path.join(output_dir, 'rt10_portfolio.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {path}")


def plot_epsilon(bt: ResoTradeBacktest, output_dir: str) -> None:
    """Plot 2: ε(Δφ) time series with trade markers."""
    fig, ax = plt.subplots(figsize=(16, 5))

    offset = 0
    colors = ['green', 'royalblue', 'orange', 'purple', 'red']

    for r in bt.fold_results:
        fold_trades = [t for t in bt.trade_log if t['fold_id'] == r['fold_id']]
        steps = [t['step'] + offset for t in fold_trades]
        epsilons = [t['epsilon'] for t in fold_trades]
        ax.plot(steps, epsilons,
                color=colors[r['fold_id'] % len(colors)],
                lw=0.8, alpha=0.7, label=f'Fold {r["fold_id"]+1}')

        buys = [t for t in fold_trades if t['action'] == 'BUY']
        sells = [t for t in fold_trades if t['action'] == 'SELL']
        if buys:
            ax.scatter([t['step'] + offset for t in buys],
                       [t['epsilon'] for t in buys],
                       marker='^', color='green', s=20, zorder=5)
        if sells:
            ax.scatter([t['step'] + offset for t in sells],
                       [t['epsilon'] for t in sells],
                       marker='v', color='red', s=20, zorder=5)

        max_step = max((t['step'] for t in fold_trades), default=0)
        offset += max_step + 10

    ax.axhline(0.3, color='red', ls='--', lw=1, label='Threshold ε = 0.3')
    ax.axhline(1.0, color='gray', ls=':', lw=0.5)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel('Step (across all folds)')
    ax.set_ylabel('ε(Δφ) = cos²(Δφ/2)')
    ax.set_title(
        'RT-10: Coupling Efficiency ε(Δφ) with Trade Markers\n'
        '▲ BUY   ▼ SELL')
    ax.legend(fontsize=8, ncol=3)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(output_dir, 'rt10_epsilon.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {path}")


def plot_vs_hodl_bars(bt: ResoTradeBacktest,
                       metrics: dict,
                       output_dir: str) -> None:
    """Plot 3: vs_hodl per fold as bar chart (falsification criterion visual)."""
    fig, ax = plt.subplots(figsize=(10, 5))

    folds = [r['fold_id'] + 1 for r in bt.fold_results]
    vs_hodl = [r['vs_hodl'] * 100 for r in bt.fold_results]
    bar_colors = ['green' if v > 0 else 'red' for v in vs_hodl]

    bars = ax.bar(folds, vs_hodl, color=bar_colors, alpha=0.85,
                  edgecolor='black', linewidth=0.8)
    for bar, val in zip(bars, vs_hodl):
        ax.text(bar.get_x() + bar.get_width() / 2,
                val + (0.1 if val >= 0 else -0.3),
                f'{val:+.1f}%',
                ha='center', va='bottom' if val >= 0 else 'top',
                fontsize=11, fontweight='bold')

    ax.axhline(0, color='black', lw=1.5)
    ax.set_xlabel('Walk-Forward Fold', fontsize=12)
    ax.set_ylabel('vs HODL [%]', fontsize=12)

    m5_text = "M-5 CLOSED ✓" if metrics['m5_closed'] else "M-5 NOT FULLY CLOSED ✗"
    color_m5 = 'green' if metrics['m5_closed'] else 'red'
    ax.set_title(
        f'RT-10: vs HODL per Fold — Falsification Criterion M-5\n'
        f'{m5_text}  |  Avg vs_HODL: {metrics["vs_hodl"]*100:+.1f}%',
        fontsize=12, color=color_m5)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    path = os.path.join(output_dir, 'rt10_vs_hodl_bars.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {path}")


def plot_drawdown(bt: ResoTradeBacktest, output_dir: str) -> None:
    """Plot 4: Drawdown curves across all folds."""
    fig, ax = plt.subplots(figsize=(16, 5))
    colors = ['green', 'royalblue', 'orange', 'purple', 'red']
    offset = 0

    for r in bt.fold_results:
        pv = r['pv_history']
        peak = np.maximum.accumulate(pv)
        dd = (peak - pv) / np.maximum(peak, 1e-10) * 100
        t = np.arange(len(dd)) + offset
        ax.fill_between(t, 0, -dd,
                         color=colors[r['fold_id'] % len(colors)],
                         alpha=0.5, label=f'Fold {r["fold_id"]+1}')
        ax.plot(t, -dd,
                color=colors[r['fold_id'] % len(colors)], lw=0.8)
        offset += len(dd) + 10

    ax.set_xlabel('Step (across all folds)')
    ax.set_ylabel('Drawdown [%]')
    ax.set_title('RT-10: Portfolio Drawdown — All Folds')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    path = os.path.join(output_dir, 'rt10_drawdown.png')
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {path}")


# ============================================================
# Main
# ============================================================

def main() -> None:
    print("=" * 80)
    print("RT-10: ResoTrade Walk-Forward Backtest — Reproducibility / M-5")
    print("Closes M-5 (PEER_REVIEW_READINESS.md)")
    print("=" * 80)

    # ── 1. Load data ─────────────────────────────────────
    print("\nLoading BTC-USDT OHLCV data ...")
    df = fetch_btcusdt_ohlcv(source='binance_api', n_candles=N_CANDLES, seed=SEED)
    print(f"  Source: {df.attrs.get('source', 'unknown')}")
    print(f"  Candles: {len(df)}")
    if 'timestamp' in df.columns and len(df) > 0:
        print(f"  Period: {df['timestamp'].iloc[0]} → {df['timestamp'].iloc[-1]}")
    print(f"  Price: {df['close'].min():.0f} – {df['close'].max():.0f} USDT")

    # ── 2. Walk-forward backtest ──────────────────────────
    print("\nRunning walk-forward backtest (5 folds) ...")
    bt = ResoTradeBacktest(
        start_capital=1000.0,
        trade_fraction=0.15,
        seed=SEED,
    )
    metrics = bt.run_walk_forward(df, n_folds=N_FOLDS)

    # ── 3. Terminal table ─────────────────────────────────
    print_results_table(bt, metrics)

    # ── 4. Export trade log ───────────────────────────────
    log_path = os.path.join(OUTPUT_DIR, 'rt10_trade_log.csv')
    bt.export_trade_log(log_path)

    # ── 5. Plots ──────────────────────────────────────────
    print("\nGenerating plots ...")
    plot_portfolio(bt, df, OUTPUT_DIR)
    plot_epsilon(bt, OUTPUT_DIR)
    plot_vs_hodl_bars(bt, metrics, OUTPUT_DIR)
    plot_drawdown(bt, OUTPUT_DIR)

    # ── 6. Summary ────────────────────────────────────────
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"""
  RT-10 — ResoTrade Walk-Forward Backtest
  ────────────────────────────────────────
  Data source  : {df.attrs.get('source', 'unknown')}
  Candles      : {len(df)}
  Folds        : {N_FOLDS}

  Average results (across {N_FOLDS} folds):
  ├─ Return      : {metrics['total_return']*100:+.1f}%
  ├─ HODL return : {metrics['hodl_return']*100:+.1f}%
  ├─ vs HODL     : {metrics['vs_hodl']*100:+.1f}%
  ├─ Sharpe      : {metrics['sharpe_ratio']:+.2f}
  ├─ Max DD      : {metrics['max_drawdown']*100:.1f}%
  ├─ Win rate    : {metrics['win_rate']*100:.1f}%
  └─ Trades      : {metrics['n_trades']}

  Per-fold vs_hodl: {[f"{v*100:+.1f}%" for v in metrics['vs_hodl_all']]}

  FALSIFICATION CRITERION (M-5):
  {metrics['falsification']}
  Sharpe > 0.5: {metrics['sharpe_ratio']:.2f} → {'✓ PASS' if metrics['sharpe_ratio'] > 0.5 else '✗ FAIL'}

  Output files:
  ├─ rt10_portfolio.png
  ├─ rt10_epsilon.png
  ├─ rt10_vs_hodl_bars.png
  ├─ rt10_drawdown.png
  └─ rt10_trade_log.csv

  Zero free parameters. Zero GPUs. Fully explainable.
  E = π · ε(Δφ) · ℏ · f, κ = 1
""")
    print("Done.")


if __name__ == "__main__":
    main()
