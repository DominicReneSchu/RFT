#!/bin/bash
# ============================================================
# ResoTrade V11.1 - Multi-Zyklus-Training (2024-2026)
# ============================================================
# Jeder Zyklus durchlaeuft alle 4 Abschnitte.
# Mehrere Zyklen festigen die Erfahrung abschnittuebergreifend.
# Am Ende: Alle 4 Abschnitte deterministisch plotten.
# ============================================================

set -e  # Bei Fehler abbrechen

ZYKLEN=3

echo ""
echo "============================================================"
echo "ResoTrade V11.1 - Multi-Zyklus-Training"
echo "============================================================"
echo ""

for z in $(seq 1 $ZYKLEN); do

    echo ""
    echo "############################################################"
    echo "# ZYKLUS $z von $ZYKLEN"
    echo "############################################################"
    echo ""

    # --- Abschnitt 4: Sideways (Maerz 2024 - Sep 2024) ---
    echo ">>> Zyklus $z - ABSCHNITT 4: Maerz 2024 - Sep 2024"
    python3 resonance_analysis.py --start 2024-03-01 --end 2024-09-01
    python3 main.py 20 500
    cp data/training_progress.png "data/training_progress_z${z}_abschnitt4.png"

    # --- Abschnitt 3: Bullrun (Sep 2024 - Maerz 2025) ---
    echo ">>> Zyklus $z - ABSCHNITT 3: Sep 2024 - Maerz 2025"
    python3 resonance_analysis.py --start 2024-09-01 --end 2025-03-01
    python3 main.py 20 500
    cp data/training_progress.png "data/training_progress_z${z}_abschnitt3.png"

    # --- Abschnitt 2: Top + Korrektur (Maerz 2025 - Sep 2025) ---
    echo ">>> Zyklus $z - ABSCHNITT 2: Maerz 2025 - Sep 2025"
    python3 resonance_analysis.py --start 2025-03-01 --end 2025-09-01
    python3 main.py 20 500
    cp data/training_progress.png "data/training_progress_z${z}_abschnitt2.png"

    # --- Abschnitt 1: Aktuell (Sep 2025 - Feb 2026) ---
    echo ">>> Zyklus $z - ABSCHNITT 1: Sep 2025 - Feb 2026"
    python3 resonance_analysis.py --start 2025-09-01 --end 2026-02-23
    python3 main.py 20 500
    cp data/training_progress.png "data/training_progress_z${z}_abschnitt1.png"

    echo ""
    echo ">>> Zyklus $z abgeschlossen."
    mkdir -p data/backups
    cp data/trade_experience_offline.csv "data/backups/experience_z${z}_$(date +%Y%m%d_%H%M%S).csv"
    cp data/trade_experience_weighted.csv "data/backups/weighted_z${z}_$(date +%Y%m%d_%H%M%S).csv"
    echo ">>> Backup Zyklus $z gesichert."
    echo ""

done

TOTAL=$(( ZYKLEN * 4 * 10000 ))

echo ""
echo "============================================================"
echo "Multi-Zyklus-Training abgeschlossen."
echo "Gesamt: $TOTAL Episoden ueber $ZYKLEN Zyklen"
echo "============================================================"
echo ""

# ============================================================
# Finale Plots: Alle 4 Abschnitte deterministisch plotten
# ============================================================
echo "============================================================"
echo "Erzeuge finale Trade-Plots fuer alle Abschnitte..."
echo "============================================================"

# Alte Signal-Dateien entfernen damit keine Verwechslung
echo ">>> Raeume alte Signal-Dateien auf..."
rm -f resonance_output_v2/signals_with_posteriors_*.csv

# Signal-Dateien fuer alle 4 Abschnitte neu erzeugen (mit Pause fuer eindeutige Timestamps)
echo ">>> Erzeuge Signal-Datei Abschnitt 4..."
python3 resonance_analysis.py --start 2024-03-01 --end 2024-09-01
sleep 2

echo ">>> Erzeuge Signal-Datei Abschnitt 3..."
python3 resonance_analysis.py --start 2024-09-01 --end 2025-03-01
sleep 2

echo ">>> Erzeuge Signal-Datei Abschnitt 2..."
python3 resonance_analysis.py --start 2025-03-01 --end 2025-09-01
sleep 2

echo ">>> Erzeuge Signal-Datei Abschnitt 1..."
python3 resonance_analysis.py --start 2025-09-01 --end 2026-02-23
sleep 2

# Pruefen ob alle 4 Dateien existieren
SIGNAL_COUNT=$(ls -1 resonance_output_v2/signals_with_posteriors_*.csv 2>/dev/null | wc -l)
echo ">>> $SIGNAL_COUNT Signal-Dateien in resonance_output_v2/"

if [ "$SIGNAL_COUNT" -lt 4 ]; then
    echo ">>> WARNUNG: Weniger als 4 Signal-Dateien! Plots koennten unvollstaendig sein."
fi

# Alle Abschnitte plotten
python3 plot_final_trades_all.py

echo ""
echo "============================================================"
echo "Alles fertig."
echo "  Plots:   data/final_trades_abschnitt_*.png"
echo "  Kombi:   data/final_trades_all_combined.png"
echo "  Backup:  data/backups/"
echo "============================================================"
echo ""