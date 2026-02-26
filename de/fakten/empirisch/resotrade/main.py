"""
ResoTrade V9.4 — Multi-Pass-Training mit getrennten Speichern.

Schreibt nach: trade_experience_offline.csv
Merged am Ende jedes Passes: Offline + Live → trade_experience_weighted.csv
"""
from pathlib import Path

from config import TRAINING_WINDOW_LENGTH
from train_offline import train_offline, plot_progress
from diagnostics import summarize_episode_trades
from experience import merge_status

DIAG_DIR = Path("data/diagnostics")


def run_training_passes(
    num_passes: int = 5,
    episodes_per_pass: int = 500,
    start_btc: float = 1.0,
    trade_fraction_small: float = 0.10,
    trade_fraction_medium: float = 0.25,
    hodl_share: float = 0.10,
    min_btc_for_full_sell: float = 0.1,
    min_btc_trade_fraction: float = 0.05,
    start_cash_share: float = 0.2,
):
    """
    Multi-Pass-Training: Mehrere Durchläufe hintereinander.

    V9.4: window_length aus config.TRAINING_WINDOW_LENGTH (720 Steps = 30 Tage).
    """
    total_episodes = num_passes * episodes_per_pass

    print(f"\n{'=' * 60}")
    print(f"ResoTrade V9.4 — Multi-Pass-Training (getrennte Speicher)")
    print(f"{'=' * 60}")
    print(f"  Passes:            {num_passes}")
    print(f"  Episoden/Pass:     {episodes_per_pass}")
    print(f"  Gesamt-Episoden:   {total_episodes}")
    print(f"  Window-Length:     {TRAINING_WINDOW_LENGTH} Steps")
    print(f"  HODL-Share:        {hodl_share * 100:.0f}%")
    print(f"  Start-Cash-Share:  {start_cash_share * 100:.0f}%")
    print(f"{'=' * 60}")
    print(f"\nSpeicher-Status vor Training:")
    merge_status()
    print()

    # V9.4: Diagnostik-Log nur einmal vor dem ersten Pass löschen
    diag_log = DIAG_DIR / "episode_log.csv"
    if diag_log.exists():
        diag_log.unlink()

    for p in range(1, num_passes + 1):
        print(f"\n{'#' * 60}")
        print(f"# PASS {p}/{num_passes} "
              f"(Episode {(p - 1) * episodes_per_pass + 1}"
              f"–{p * episodes_per_pass} von {total_episodes})")
        print(f"{'#' * 60}\n")

        train_offline(
            num_episodes=episodes_per_pass,
            start_btc=start_btc,
            trade_fraction_small=trade_fraction_small,
            trade_fraction_medium=trade_fraction_medium,
            hodl_share=hodl_share,
            min_btc_for_full_sell=min_btc_for_full_sell,
            min_btc_trade_fraction=min_btc_trade_fraction,
            start_cash_share=start_cash_share,
        )

        print(f"\n[Multi-Pass] Pass {p}/{num_passes} abgeschlossen.")

    # Finaler Plot + Diagnostik (vom letzten Pass)
    plot_progress()

    print(f"\n{'=' * 60}")
    print(f"RESONANZFELD-DIAGNOSTIK (letzter Pass)")
    print(f"{'=' * 60}")
    summarize_episode_trades()

    print(f"\n{'=' * 60}")
    print(f"Multi-Pass-Training abgeschlossen: {total_episodes} Episoden "
          f"in {num_passes} Passes")
    print(f"{'=' * 60}")
    print(f"\nSpeicher-Status nach Training:")
    merge_status()
    print(f"\nErfahrungsspeicher bereit für Live-Betrieb.")
    print(f"Nächster Schritt: python live_signal.py status")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    import sys

    num_passes = 5
    episodes = 500

    if len(sys.argv) > 1:
        try:
            num_passes = int(sys.argv[1])
        except ValueError:
            print(f"Ungültiger Wert für Passes: {sys.argv[1]}")
            sys.exit(1)
    if len(sys.argv) > 2:
        try:
            episodes = int(sys.argv[2])
        except ValueError:
            print(f"Ungültiger Wert für Episoden: {sys.argv[2]}")
            sys.exit(1)

    run_training_passes(
        num_passes=num_passes,
        episodes_per_pass=episodes,
        start_btc=1.0,
        trade_fraction_small=0.10,
        trade_fraction_medium=0.25,
        hodl_share=0.1,
        min_btc_for_full_sell=0.1,
        min_btc_trade_fraction=0.05,
        start_cash_share=0.2,
    )