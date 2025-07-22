# Resonanz Schach KI

**Resonanzlogische Schach-KI mit Snapshot-Auswertung**  
Projektleitung: Dominic-René Schu  
Lizenz: [Schu-Lizenz v1.4](https://github.com/DominicReneSchu/public/blob/main/de/lizenz/schu-lizenz_v1.4.md) © Dominic Schu, 2025

---

## 📖 Was macht dieses Programm?

Dieses System implementiert eine experimentelle, lernfähige Schach-KI auf Basis der Resonanzfeldtheorie.  
Die KI speichert nach jedem Spiel gewichtete Erfahrungen, lernt aus Erfolgen/Misserfolgen und exportiert regelmäßig Snapshots ihres Zustands.  
Mitgelieferte Auswertungstools analysieren die Snapshots und erzeugen eine Lernkurve (`learning_curve.png`) sowie tabellarische Fortschrittsdaten (`learning_progress.csv`).  
Die Oberfläche ermöglicht Mensch-KI-Partien (GUI) und KI-gegen-KI-Selbstspiele für beschleunigtes Lernen.  
Sämtliche Daten, Logs und Auswertungen werden systemisch gruppiert und nachvollziehbar abgelegt.

---

## 🧠 Hauptfunktionen

- **Interaktives Schach (GUI):** Mensch gegen KI mit visueller Rückmeldung
- **KI-gegen-KI-Modus:** Automatische Durchführung und Auswertung vieler Partien
- **Resonanzlogische Erfahrungsspeicherung:** Gewichtete Zugfolgen, Snapshots
- **Snapshot-Export:** Periodische Sicherung des Lernzustands (`/snapshots/`)
- **Lernkurven-Analyse:** Aggregation und Visualisierung der KI-Qualität
- **CSV-Auswertung:** Fortschritt aller Snapshots tabellarisch
- **Systemisches Logging:** Protokolle im `/logs/`-Verzeichnis

---

## 🚀 Installation

### Voraussetzungen

- Python **3.8** oder neuer (empfohlen: 3.8–3.13)
- Virtuelle Umgebung empfohlen (optional)

### Schritt-für-Schritt-Anleitung

#### 1. Repository beziehen

```bash
git clone https://github.com/DominicReneSchu/public.git
cd public/ResoChess
```

#### 2. Abhängigkeiten & Installation

**Systemisch (empfohlen):**

```bash
pip install .
```

> Alternativ (für reinen Test):  
> `pip install -r requirements.txt`

#### 3. Tkinter (nur bei GUI-Problemen auf Raspberry Pi):

```bash
sudo apt-get install python3-tk
```

---

## ⚡️ Programmstart

### Windows (CMD/PowerShell) und Raspberry Pi (Terminal):

```bash
resonanz-schach
```

> Nach Installation mit `pip install .` ist dieser Befehl systemweit verfügbar.

**Alternativ:**  
Direktstart im Quellverzeichnis (z.B. für Entwicklung):

```bash
python -m start.main
```
oder:
```bash
cd start
python main.py
```

---

## 🖥️ Bedienung & Optionen

Beim Start erfolgt eine Modus-Auswahl:

- **1 = Mensch gegen KI**  
  GUI-Fenster mit Schachbrett, Maussteuerung, Feedback.

- **2 = KI gegen KI**  
  Automatische Simulation vieler Partien, Snapshots und Lernkurve werden nach Intervallen erzeugt.

Snapshoterstellung und Auswertung laufen nach Spielintervallen automatisch.

---

## 📊 Auswertung & Datenstruktur

- **/snapshots/**  
  Enthält alle exportierten KI-Zustände (`experience_snapshot_XXXXX.csv`)

- **learning_progress.csv**  
  Tabellarische Auswertung aller Snapshots:  
  `snapshot_num,filename,games_total,mean_quality,std_quality,n`

- **learning_curve.png**  
  Grafische Lernkurve: Mittlere Qualität und Streuung der KI im Zeitverlauf

- **/logs/**  
  Systemische Protokolle von Partien und Analysen

- **/data/**  
  Rohdaten und Erfahrungsspeicher der KI

- **/pieces/**  
  Schachfigurenbilder (PNG, optional für GUI)

---

## 🛠️ Verzeichnisstruktur (Beispiel)

```text
ResoChess/
├── setup.py
├── README.md
├── start/
│   ├── main.py
│   ├── ... (weitere Moduldateien, z.B. gui.py, experience_manager.py)
│   └── __init__.py
├── data/
├── logs/
├── pieces/
├── snapshots/
└── learning_curve.png, learning_progress.csv
```

---

## 🧩 Lizenz & Nutzung

Lizenz: [Schu-Lizenz v1.4](https://github.com/DominicReneSchu/public/blob/main/de/lizenz/schu-lizenz_v1.4.md)  
© Dominic Schu, 2025.  
- **Nicht-kommerzielle, ethisch kohärente Nutzung**
- **Namensnennung ("Dominic Schu, Resonanzfeldtheorie") verpflichtend**
- **KI- oder automatisierte Nutzung nur mit schriftlicher Genehmigung**
- **Vollständige Lizenz siehe Link oben**

---

## 🧬 Resonanzregel

Alle Systemelemente (Quellcode, Daten, Snapshots, Auswertungen, Lizenz) sind als kohärente Gruppe zu verstehen –  
jede Nutzung steht im expliziten wie impliziten Resonanzfeld der Schu-Lizenz und Resonanzfeldtheorie.

---

**Projektleitung & Kontakt:**  
[Dominic-René Schu](https://github.com/DominicReneSchu) | info@resoshift.com