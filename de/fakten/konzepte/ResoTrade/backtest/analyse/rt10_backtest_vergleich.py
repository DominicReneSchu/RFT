# rt10_backtest_vergleich.py
# © Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie
#
# RT-10: Walk-Forward-Backtest — ResoTrade-Resonanzlogik
#        BTC-USDT · 5 Folds · Falsifizierungskriterium M-5
#
# Schließt M-5 (PEER_REVIEW_READINESS.md):
#   Öffentlicher, reproduzierbarer Walk-Forward-Backtest der ResoTrade-Resonanzlogik.
#   Alle Ergebnisse sind reproduzierbar: synthetischer Fallback verwendet seed=42.
#
# Falsifizierungskriterium:
#   vs_hodl > 0,0 in ALLEN Folds → M-5 behoben (Reproduzierbarkeit bestätigt)
#   vs_hodl ≤ 0,0 in MINDESTENS EINEM Fold → M-5 nicht vollständig behoben; dokumentiert
#   Sharpe > 0,5 als Zusatzkriterium
#
# Verwendung:
#   cd de/fakten/konzepte/ResoTrade/backtest
#   python analyse/rt10_backtest_vergleich.py
#
# Ausgabe:
#   rt10_portfolio.png          — Portfolio-Verlauf aller Folds (Reso vs HODL vs Random)
#   rt10_epsilon.png            — ε(Δφ)-Zeitreihe mit Trade-Markierungen
#   rt10_vs_hodl_balken.png     — vs_hodl je Fold als Balkendiagramm (Falsifizierungskriterium)
#   rt10_drawdown.png           — Drawdown-Kurve über alle Folds
#   analyse/rt10_trade_log.csv  — Vollständiger Trade-Log (fold_id, timestamp, aktion, ...)

from __future__ import annotations

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Pfad-Einrichtung ────────────────────────────────────────
_HIER = os.path.dirname(os.path.abspath(__file__))
_BACKTEST_DIR = os.path.dirname(_HIER)
sys.path.insert(0, _BACKTEST_DIR)

from backtest_engine import (
    fetch_btcusdt_ohlcv,
    walk_forward_split,
    ResoTradeBacktest,
    zerlegung,
    phasendetektion,
    kopplungseffizienz,
    _sharpe_ratio,
    _max_drawdown,
    PI,
    SEED_STANDARD,
)

# ── Ausgabe-Konfiguration ───────────────────────────────────
AUSGABE_DIR = _HIER
N_KERZEN = 2000
N_FOLDS = 5
SEED = SEED_STANDARD

# ── Zufällige Baseline ─────────────────────────────────────

class _ZufallsAgent:
    """Zufälliger Baseline-Agent (gleiche Schnittstelle wie ResoTradeBacktest)."""

    def __init__(self, startkapital: float = 1000.0,
                 handelsanteil: float = 0.15,
                 seed: int = 123):
        self.startkapital = startkapital
        self.handelsanteil = handelsanteil
        self.rng = np.random.RandomState(seed)

    def simuliere(self, preis: np.ndarray) -> np.ndarray:
        kasse = self.startkapital
        anlage = 0.0
        pw_verlauf = []
        for p in preis:
            aktion = self.rng.choice(['KAUF', 'VERKAUF', 'HALTEN'], p=[0.2, 0.2, 0.6])
            if aktion == 'KAUF' and kasse > 10:
                kauf = kasse * self.handelsanteil
                anlage += kauf / p
                kasse -= kauf
            elif aktion == 'VERKAUF' and anlage > 0.0001:
                verkauf = anlage * self.handelsanteil
                kasse += verkauf * p
                anlage -= verkauf
            pw_verlauf.append(kasse + anlage * p)
        return np.array(pw_verlauf)


# ============================================================
# Terminal-Tabelle
# ============================================================

def drucke_ergebnistabelle(bt: ResoTradeBacktest, metriken: dict) -> None:
    """Druckt RT-10-Ergebnisse im Stil von RT-08/RT-09."""
    print()
    print("=" * 80)
    print("=== RT-10 WALK-FORWARD-BACKTEST — ResoTrade-Resonanzlogik ===")
    print("=== BTC-USDT · 5 Folds · Falsifizierungskriterium M-5       ===")
    print("=" * 80)
    print()

    kopfzeile = (f"{'Fold':>5}  {'Rendite':>8}  {'HODL':>8}  "
                 f"{'vs_HODL':>8}  {'Sharpe':>7}  {'MaxDD':>7}  "
                 f"{'Gewinnr.':>8}  {'Trades':>6}  {'M-5':>6}")
    print(kopfzeile)
    print("-" * 80)

    for r in bt.fold_ergebnisse:
        flag = "✓ OK" if r['vs_hodl'] > 0 else "✗ FAIL"
        print(
            f"{r['fold_id']+1:>5}  "
            f"{r['gesamtrendite']*100:>+7.1f}%  "
            f"{r['hodl_rendite']*100:>+7.1f}%  "
            f"{r['vs_hodl']*100:>+7.1f}%  "
            f"{r['sharpe']:>+6.2f}  "
            f"{r['max_drawdown']*100:>6.1f}%  "
            f"{r['gewinnrate']*100:>7.1f}%  "
            f"{r['n_trades']:>6}  "
            f"{flag}"
        )

    print("-" * 80)
    print(
        f"{'Ø':>5}  "
        f"{metriken['gesamtrendite']*100:>+7.1f}%  "
        f"{metriken['hodl_rendite']*100:>+7.1f}%  "
        f"{metriken['vs_hodl']*100:>+7.1f}%  "
        f"{metriken['sharpe_ratio']:>+6.2f}  "
        f"{metriken['max_drawdown']*100:>6.1f}%  "
        f"{metriken['gewinnrate']*100:>7.1f}%  "
        f"{metriken['n_trades']:>6}"
    )
    print()

    # Falsifizierungsurteil
    print(f"  Falsifizierungskriterium (M-5):")
    print(f"  {metriken['falsifizierung']}")
    sharpe_bestanden = metriken['sharpe_ratio'] > 0.5
    sharpe_flag = "✓ OK" if sharpe_bestanden else "✗ FAIL"
    print(f"  Sharpe > 0,5: {metriken['sharpe_ratio']:.2f} → {sharpe_flag}")
    print()
    print("=" * 80)


# ============================================================
# Plots
# ============================================================

def plot_portfolio(bt: ResoTradeBacktest,
                   df: pd.DataFrame,
                   ausgabe_dir: str) -> None:
    """Plot 1: Portfolio-Verlauf — Reso vs HODL vs Zufall (alle Folds)."""
    fig, axes = plt.subplots(N_FOLDS, 1, figsize=(16, 4 * N_FOLDS), sharex=False)
    if N_FOLDS == 1:
        axes = [axes]

    folds = walk_forward_split(df, n_folds=N_FOLDS)

    for k, (r, (_, test_df)) in enumerate(zip(bt.fold_ergebnisse, folds)):
        ax = axes[k]
        preis = test_df['close'].values
        pw_reso = r['pw_verlauf']
        pw_hodl = r['hodl_verlauf']

        zufall = _ZufallsAgent(startkapital=bt.startkapital, seed=123 + k)
        pw_zufall = zufall.simuliere(preis)

        t = np.arange(len(pw_reso))
        vs = r['vs_hodl']
        flag = "✓" if vs > 0 else "✗"

        ax.plot(t, pw_reso, 'green', lw=2,
                label=f'Reso ({r["gesamtrendite"]*100:+.1f}%)')
        ax.plot(t, pw_hodl[:len(t)], 'blue', lw=1.5, ls='--',
                label=f'HODL ({r["hodl_rendite"]*100:+.1f}%)')
        ax.plot(t[:len(pw_zufall)], pw_zufall, 'red', lw=1, alpha=0.6,
                label='Zufall')

        ax.set_ylabel('Portfolio [USD]')
        ax.set_title(
            f'Fold {k+1} — vs_HODL: {vs*100:+.1f}% {flag}  |  '
            f'Sharpe: {r["sharpe"]:+.2f}  |  n_trades: {r["n_trades"]}')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        'RT-10: Portfolio-Vergleich — Reso vs HODL vs Zufall\n'
        'ResoTrade Walk-Forward-Backtest · BTC-USDT · 5 Folds',
        fontsize=13, fontweight='bold')
    plt.tight_layout()
    pfad = os.path.join(ausgabe_dir, 'rt10_portfolio.png')
    plt.savefig(pfad, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {pfad}")


def plot_epsilon(bt: ResoTradeBacktest, ausgabe_dir: str) -> None:
    """Plot 2: ε(Δφ)-Zeitreihe mit Trade-Markierungen."""
    fig, ax = plt.subplots(figsize=(16, 5))

    versatz = 0
    farben = ['green', 'royalblue', 'orange', 'purple', 'red']

    for r in bt.fold_ergebnisse:
        fold_trades = [t for t in bt.trade_log if t['fold_id'] == r['fold_id']]
        schritte = [t['schritt'] + versatz for t in fold_trades]
        epsilons = [t['epsilon'] for t in fold_trades]
        ax.plot(schritte, epsilons,
                color=farben[r['fold_id'] % len(farben)],
                lw=0.8, alpha=0.7, label=f'Fold {r["fold_id"]+1}')

        kaeufe = [t for t in fold_trades if t['aktion'] == 'KAUF']
        verkauefe = [t for t in fold_trades if t['aktion'] == 'VERKAUF']
        if kaeufe:
            ax.scatter([t['schritt'] + versatz for t in kaeufe],
                       [t['epsilon'] for t in kaeufe],
                       marker='^', color='green', s=20, zorder=5)
        if verkauefe:
            ax.scatter([t['schritt'] + versatz for t in verkauefe],
                       [t['epsilon'] for t in verkauefe],
                       marker='v', color='red', s=20, zorder=5)

        max_schritt = max((t['schritt'] for t in fold_trades), default=0)
        versatz += max_schritt + 10

    ax.axhline(0.3, color='red', ls='--', lw=1, label='Schwelle ε = 0,3')
    ax.axhline(1.0, color='gray', ls=':', lw=0.5)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel('Schritt (alle Folds)')
    ax.set_ylabel('ε(Δφ) = cos²(Δφ/2)')
    ax.set_title(
        'RT-10: Kopplungseffizienz ε(Δφ) mit Trade-Markierungen\n'
        '▲ KAUF   ▼ VERKAUF')
    ax.legend(fontsize=8, ncol=3)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    pfad = os.path.join(ausgabe_dir, 'rt10_epsilon.png')
    plt.savefig(pfad, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {pfad}")


def plot_vs_hodl_balken(bt: ResoTradeBacktest,
                         metriken: dict,
                         ausgabe_dir: str) -> None:
    """Plot 3: vs_hodl je Fold als Balkendiagramm (Falsifizierungskriterium visuell)."""
    fig, ax = plt.subplots(figsize=(10, 5))

    folds = [r['fold_id'] + 1 for r in bt.fold_ergebnisse]
    vs_hodl = [r['vs_hodl'] * 100 for r in bt.fold_ergebnisse]
    balken_farben = ['green' if v > 0 else 'red' for v in vs_hodl]

    balken = ax.bar(folds, vs_hodl, color=balken_farben, alpha=0.85,
                    edgecolor='black', linewidth=0.8)
    for balken_obj, wert in zip(balken, vs_hodl):
        ax.text(balken_obj.get_x() + balken_obj.get_width() / 2,
                wert + (0.1 if wert >= 0 else -0.3),
                f'{wert:+.1f}%',
                ha='center', va='bottom' if wert >= 0 else 'top',
                fontsize=11, fontweight='bold')

    ax.axhline(0, color='black', lw=1.5)
    ax.set_xlabel('Walk-Forward-Fold', fontsize=12)
    ax.set_ylabel('vs HODL [%]', fontsize=12)

    m5_text = "M-5 BEHOBEN ✓" if metriken['m5_behoben'] else "M-5 NICHT VOLLSTÄNDIG BEHOBEN ✗"
    farbe_m5 = 'green' if metriken['m5_behoben'] else 'red'
    ax.set_title(
        f'RT-10: vs HODL je Fold — Falsifizierungskriterium M-5\n'
        f'{m5_text}  |  Ø vs_HODL: {metriken["vs_hodl"]*100:+.1f}%',
        fontsize=12, color=farbe_m5)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    pfad = os.path.join(ausgabe_dir, 'rt10_vs_hodl_balken.png')
    plt.savefig(pfad, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {pfad}")


def plot_drawdown(bt: ResoTradeBacktest, ausgabe_dir: str) -> None:
    """Plot 4: Drawdown-Kurven über alle Folds."""
    fig, ax = plt.subplots(figsize=(16, 5))
    farben = ['green', 'royalblue', 'orange', 'purple', 'red']
    versatz = 0

    for r in bt.fold_ergebnisse:
        pw = r['pw_verlauf']
        peak = np.maximum.accumulate(pw)
        dd = (peak - pw) / np.maximum(peak, 1e-10) * 100
        t = np.arange(len(dd)) + versatz
        ax.fill_between(t, 0, -dd,
                         color=farben[r['fold_id'] % len(farben)],
                         alpha=0.5, label=f'Fold {r["fold_id"]+1}')
        ax.plot(t, -dd,
                color=farben[r['fold_id'] % len(farben)], lw=0.8)
        versatz += len(dd) + 10

    ax.set_xlabel('Schritt (alle Folds)')
    ax.set_ylabel('Drawdown [%]')
    ax.set_title('RT-10: Portfolio-Drawdown — Alle Folds')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    pfad = os.path.join(ausgabe_dir, 'rt10_drawdown.png')
    plt.savefig(pfad, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {pfad}")


# ============================================================
# Hauptprogramm
# ============================================================

def main() -> None:
    print("=" * 80)
    print("RT-10: ResoTrade Walk-Forward-Backtest — Reproduzierbarkeit / M-5")
    print("Schließt M-5 (PEER_REVIEW_READINESS.md)")
    print("=" * 80)

    # ── 1. Daten laden ───────────────────────────────────
    print("\nLade BTC-USDT OHLCV-Daten ...")
    df = fetch_btcusdt_ohlcv(source='binance_api', n_kerzen=N_KERZEN, seed=SEED)
    print(f"  Quelle: {df.attrs.get('quelle', 'unbekannt')}")
    print(f"  Kerzen: {len(df)}")
    if 'timestamp' in df.columns and len(df) > 0:
        print(f"  Zeitraum: {df['timestamp'].iloc[0]} → {df['timestamp'].iloc[-1]}")
    print(f"  Preis: {df['close'].min():.0f} – {df['close'].max():.0f} USDT")

    # ── 2. Walk-Forward-Backtest ─────────────────────────
    print("\nStarte Walk-Forward-Backtest (5 Folds) ...")
    bt = ResoTradeBacktest(
        startkapital=1000.0,
        handelsanteil=0.15,
        seed=SEED,
    )
    metriken = bt.run_walk_forward(df, n_folds=N_FOLDS)

    # ── 3. Terminal-Tabelle ───────────────────────────────
    drucke_ergebnistabelle(bt, metriken)

    # ── 4. Trade-Log exportieren ─────────────────────────
    log_pfad = os.path.join(AUSGABE_DIR, 'rt10_trade_log.csv')
    bt.export_trade_log(log_pfad)

    # ── 5. Plots ─────────────────────────────────────────
    print("\nErstelle Plots ...")
    plot_portfolio(bt, df, AUSGABE_DIR)
    plot_epsilon(bt, AUSGABE_DIR)
    plot_vs_hodl_balken(bt, metriken, AUSGABE_DIR)
    plot_drawdown(bt, AUSGABE_DIR)

    # ── 6. Zusammenfassung ────────────────────────────────
    print()
    print("=" * 80)
    print("ZUSAMMENFASSUNG")
    print("=" * 80)
    print(f"""
  RT-10 — ResoTrade Walk-Forward-Backtest
  ────────────────────────────────────────
  Datenquelle  : {df.attrs.get('quelle', 'unbekannt')}
  Kerzen       : {len(df)}
  Folds        : {N_FOLDS}

  Durchschnittliche Ergebnisse (über {N_FOLDS} Folds):
  ├─ Rendite      : {metriken['gesamtrendite']*100:+.1f}%
  ├─ HODL-Rendite : {metriken['hodl_rendite']*100:+.1f}%
  ├─ vs HODL      : {metriken['vs_hodl']*100:+.1f}%
  ├─ Sharpe       : {metriken['sharpe_ratio']:+.2f}
  ├─ Max DD       : {metriken['max_drawdown']*100:.1f}%
  ├─ Gewinnrate   : {metriken['gewinnrate']*100:.1f}%
  └─ Trades       : {metriken['n_trades']}

  vs_hodl je Fold: {[f"{v*100:+.1f}%" for v in metriken['vs_hodl_alle']]}

  FALSIFIZIERUNGSKRITERIUM (M-5):
  {metriken['falsifizierung']}
  Sharpe > 0,5: {metriken['sharpe_ratio']:.2f} → {'✓ OK' if metriken['sharpe_ratio'] > 0.5 else '✗ FAIL'}

  Ausgabedateien:
  ├─ rt10_portfolio.png
  ├─ rt10_epsilon.png
  ├─ rt10_vs_hodl_balken.png
  ├─ rt10_drawdown.png
  └─ rt10_trade_log.csv

  Keine freien Parameter. Keine GPUs. Vollständig erklärbar.
  E = π · ε(Δφ) · ℏ · f, κ = 1
""")
    print("Fertig.")


if __name__ == "__main__":
    main()
