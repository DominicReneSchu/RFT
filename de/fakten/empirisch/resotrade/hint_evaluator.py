"""
ResoTrade V11.1 - Hint Evaluator
==================================
Bewertet rueckblickend, ob die menschlichen Hinweise korrekt waren.
Das System lernt dadurch, wie zuverlaessig die Mensch-Hinweise sind,
und kann das Gewicht langfristig anpassen.

Aufruf: python hint_evaluator.py
"""

import os
import json
import pandas as pd
from datetime import datetime, timezone, timedelta


HINT_LOG_PATH = os.path.join("data", "human_hint_log.csv")
EVAL_PATH = os.path.join("data", "human_hint_evaluation.csv")


def evaluate_hints():
    """
    Prueft fuer jeden vergangenen Hinweis:
    War der Markt danach tatsaechlich bullish/bearish?
    """
    if not os.path.exists(HINT_LOG_PATH):
        print("[HintEval] Kein Hint-Log vorhanden.")
        return

    log = pd.read_csv(HINT_LOG_PATH)
    log['timestamp'] = pd.to_datetime(log['timestamp'])

    # Brauchen Preisdaten fuer Bewertung
    signals_files = sorted(
        [f for f in os.listdir("data") if f.startswith("signals_with_posteriors")],
        reverse=True
    )
    if not signals_files:
        print("[HintEval] Keine Signaldaten fuer Bewertung vorhanden.")
        return

    signals = pd.read_csv(os.path.join("data", signals_files[0]))
    if 'Datetime' in signals.columns:
        signals['Datetime'] = pd.to_datetime(signals['Datetime'])
        signals = signals.set_index('Datetime')

    results = []
    for _, hint in log.iterrows():
        ts = hint['timestamp']
        bias = hint['bias']

        if bias == 'neutral':
            continue

        # Preis zum Zeitpunkt des Hints
        try:
            idx = signals.index.get_indexer([ts], method='nearest')[0]
            price_at_hint = signals['price'].iloc[idx]

            # Preis 24h spaeter
            ts_24h = ts + timedelta(hours=24)
            idx_24h = signals.index.get_indexer([ts_24h], method='nearest')[0]
            price_24h = signals['price'].iloc[idx_24h]

            # Preis 72h spaeter
            ts_72h = ts + timedelta(hours=72)
            idx_72h = signals.index.get_indexer([ts_72h], method='nearest')[0]
            price_72h = signals['price'].iloc[idx_72h]

            change_24h = (price_24h - price_at_hint) / price_at_hint
            change_72h = (price_72h - price_at_hint) / price_at_hint

            # War der Hint korrekt?
            if bias == "bullish":
                correct_24h = change_24h > 0
                correct_72h = change_72h > 0
            else:  # bearish
                correct_24h = change_24h < 0
                correct_72h = change_72h < 0

            results.append({
                "timestamp": ts,
                "bias": bias,
                "reason": hint.get('reason', ''),
                "price_at_hint": price_at_hint,
                "change_24h_pct": change_24h * 100,
                "change_72h_pct": change_72h * 100,
                "correct_24h": correct_24h,
                "correct_72h": correct_72h,
            })
        except (IndexError, KeyError):
            continue

    if not results:
        print("[HintEval] Keine bewertbaren Hints gefunden.")
        return

    df = pd.DataFrame(results)
    df.to_csv(EVAL_PATH, index=False)

    # Statistik
    n = len(df)
    correct_24 = df['correct_24h'].sum()
    correct_72 = df['correct_72h'].sum()

    print("============================================================")
    print("Human Hint Bewertung")
    print("============================================================")
    print(f"  Bewertete Hints:    {n}")
    print(f"  Korrekt nach 24h:   {correct_24}/{n} ({correct_24/n*100:.0f}%)")
    print(f"  Korrekt nach 72h:   {correct_72}/{n} ({correct_72/n*100:.0f}%)")
    print(f"")

    if correct_72 / n >= 0.6:
        print("  Empfehlung: Hint-Gewicht ERHOEHEN (Mensch liegt oft richtig)")
        print("  -> python human_hint.py bullish \"grund\" 0.5")
    elif correct_72 / n <= 0.4:
        print("  Empfehlung: Hint-Gewicht SENKEN (Mensch liegt oft falsch)")
        print("  -> python human_hint.py bullish \"grund\" 0.15")
    else:
        print("  Empfehlung: Gewicht beibehalten (0.3)")

    print("============================================================")


if __name__ == "__main__":
    evaluate_hints()