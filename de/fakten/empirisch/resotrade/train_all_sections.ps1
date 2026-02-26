# ============================================================
# ResoTrade V11.1 - Abschnittsweises Training (2024-2026)
# ============================================================
# yfinance liefert max 730 Tage Stundendaten zurueck.
# 4 Abschnitte a 6 Monate, aelteste zuerst.
# Am Ende: Alle 4 Abschnitte deterministisch plotten.
# ============================================================

Write-Host ""
Write-Host "============================================================"
Write-Host "ResoTrade V11.1 - Abschnittsweises Training (2024-2026)"
Write-Host "============================================================"
Write-Host ""

# --- Abschnitt 4 ---
Write-Host ">>> ABSCHNITT 4: Maerz 2024 - Sep 2024"
python resonance_analysis.py --start 2024-03-01 --end 2024-09-01
python main.py 20 500
Copy-Item data\training_progress.png data\training_progress_abschnitt4.png

# --- Abschnitt 3 ---
Write-Host ">>> ABSCHNITT 3: Sep 2024 - Maerz 2025"
python resonance_analysis.py --start 2024-09-01 --end 2025-03-01
python main.py 20 500
Copy-Item data\training_progress.png data\training_progress_abschnitt3.png

# --- Abschnitt 2 ---
Write-Host ">>> ABSCHNITT 2: Maerz 2025 - Sep 2025"
python resonance_analysis.py --start 2025-03-01 --end 2025-09-01
python main.py 20 500
Copy-Item data\training_progress.png data\training_progress_abschnitt2.png

# --- Abschnitt 1 ---
Write-Host ">>> ABSCHNITT 1: Sep 2025 - Feb 2026"
python resonance_analysis.py --start 2025-09-01 --end 2026-02-23
python main.py 20 500
Copy-Item data\training_progress.png data\training_progress_abschnitt1.png

Write-Host ""
Write-Host "============================================================"
Write-Host "Training abgeschlossen. Erzeuge finale Plots..."
Write-Host "============================================================"
Write-Host ""

# Alte Signal-Dateien entfernen damit keine Verwechslung
Write-Host ">>> Raeume alte Signal-Dateien auf..."
Get-ChildItem resonance_output_v2 -Filter "signals_with_posteriors_*" -ErrorAction SilentlyContinue | Remove-Item -Force

# Signal-Dateien fuer alle 4 Abschnitte neu erzeugen (mit Pause fuer eindeutige Timestamps)
Write-Host ">>> Erzeuge Signal-Datei Abschnitt 4..."
python resonance_analysis.py --start 2024-03-01 --end 2024-09-01
Start-Sleep -Seconds 2

Write-Host ">>> Erzeuge Signal-Datei Abschnitt 3..."
python resonance_analysis.py --start 2024-09-01 --end 2025-03-01
Start-Sleep -Seconds 2

Write-Host ">>> Erzeuge Signal-Datei Abschnitt 2..."
python resonance_analysis.py --start 2025-03-01 --end 2025-09-01
Start-Sleep -Seconds 2

Write-Host ">>> Erzeuge Signal-Datei Abschnitt 1..."
python resonance_analysis.py --start 2025-09-01 --end 2026-02-23
Start-Sleep -Seconds 2

# Pruefen ob alle 4 Dateien existieren
$signalCount = (Get-ChildItem resonance_output_v2 -Filter "signals_with_posteriors_*").Count
Write-Host ">>> $signalCount Signal-Dateien in resonance_output_v2/"

if ($signalCount -lt 4) {
    Write-Host ">>> WARNUNG: Weniger als 4 Signal-Dateien! Plots koennten unvollstaendig sein."
}

# Alle Abschnitte plotten
python plot_final_trades_all.py

Write-Host ""
Write-Host "============================================================"
Write-Host "Alles fertig."
Write-Host "  Plots:   data\final_trades_abschnitt_*.png"
Write-Host "  Kombi:   data\final_trades_all_combined.png"
Write-Host "============================================================"
Write-Host ""