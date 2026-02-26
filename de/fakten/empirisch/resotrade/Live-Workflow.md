# ResoTrade V11.1 — Workflow

## === Initiales Training (Linux) ===
```bash
cd ~/Schreibtisch/Resotrade
source .venv/bin/activate
chmod +x train_all_sections_multi.sh
sed -i 's/\r$//' train_all_sections_multi.sh

# Suspend verhindern bei zugeklapptem Deckel
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

./train_all_sections_multi.sh

# Suspend danach wieder aktivieren
sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

## === Initiales Training (PowerShell) ===
```powershell
del data\trade_experience_offline.csv
del data\trade_experience_weighted.csv
pwsh -ExecutionPolicy Bypass -File .\train_all_sections.ps1
```

## === Trainings-Ergebnis prüfen ===
```bash
python3 plot_final_trades_all.py       # Alle 4 Abschnitte plotten
# Erwartung: Alle Abschnitte positiv vs HODL
```

## === Erststart Live (Laptop oder Desktop) ===
```bash
cd ~/Schreibtisch/Resotrade
source .venv/bin/activate
python3 live_signal.py status          # Kraken-Verbindung + Portfolio prüfen
python3 live_signal.py once            # Ein Zyklus testen
python3 live_signal.py loop            # Dry-Run Dauerbetrieb
```

## === Tägliche Kontrolle ===
```bash
python3 live_signal.py status          # Portfolio + Hint-Status
python3 live_signal.py expectation     # System-Erwartung anzeigen
python3 analyze_logs.py                # Performance-Plot + Statistik
tail -20 data/live_signal_log.csv      # Letzte Signale prüfen
```

## === Human-Hint setzen (bei Nachrichtenlage) ===
```bash
# System-Erwartung anzeigen — VOR dem Hint
python3 live_signal.py expectation

# Hinweise setzen
python3 human_hint.py bullish "EZB senkt Zinsen um 25bp"
python3 human_hint.py bearish "SEC verklagt Coinbase" 0.5
python3 human_hint.py pause 12 "FOMC-Meeting heute Abend"
python3 human_hint.py neutral "Markt unklar, keine Aktion"

# Status prüfen
python3 human_hint.py status

# Hinweis aufheben
python3 human_hint.py clear

# Rückblickend: Waren meine Hinweise gut?
python3 hint_evaluator.py
```

## === Nachtraining (alle 3-7 Tage) ===
```bash
# 1. Frische Marktdaten analysieren
python3 resonance_analysis.py

# 2. Nachtrainieren mit aktuellen Daten
python3 main.py 5 500

# 3. Live-Erfahrung mit Offline-Training zusammenführen
python3 live_signal.py merge

# 4. Ergebnis prüfen
python3 live_signal.py status
python3 plot_final_trades_all.py
```

## === Wöchentliche Auswertung ===
```bash
# Performance vs HODL seit Start
python3 analyze_logs.py

# Hint-Qualität bewerten
python3 hint_evaluator.py

# Backup der Erfahrungsdaten
mkdir -p data/backups
cp data/trade_experience_offline.csv "data/backups/offline_$(date +%Y%m%d).csv"
cp data/trade_experience_weighted.csv "data/backups/weighted_$(date +%Y%m%d).csv"
```

## === Dateien zwischen Linux ↔ Windows synchronisieren ===
```bash
# Nach Training auf Linux → Windows (per SCP/USB)
scp dominic@laptop:~/Schreibtisch/Resotrade/data/trade_experience_offline.csv data/

# Dann auf Windows mergen
python live_signal.py merge
```

## === Wenn bereit für echten Handel ===
```bash
# Checkliste vor Echtbetrieb:
#   ✅ Paper-Trading positiv über 2+ Wochen
#   ✅ Kein Overtrading (< 5 Trades/Tag)
#   ✅ Drawdown nie unter -10% vs HODL
#   ✅ Human-Hint getestet und bewertet
#   ✅ Backup der Erfahrungsdaten angelegt

export RESOTRADE_DRY_RUN=false
python3 live_signal.py loop
```

## === Notfall: System stoppen ===
```bash
# Sofort alle Trades blockieren
python3 human_hint.py pause 999 "NOTFALL: System gestoppt"

# Oder Prozess beenden
pkill -f "live_signal.py"             # Linux
# PowerShell: Get-Process python | Stop-Process
```