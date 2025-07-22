# Resonance Chess AI

**Resonance-logic based Chess AI with Snapshot Evaluation**  
Project Lead: Dominic-René Schu  
License: [Schu License v1.4](https://github.com/DominicReneSchu/public/blob/main/de/lizenz/schu-lizenz_v1.4.md) © Dominic Schu, 2025

---

## 📖 What does this program do?

This system implements an experimental, learning chess AI based on resonance field theory.  
After each game, the AI stores weighted experiences, learns from its successes and failures, and regularly exports snapshots of its state.  
Included evaluation tools analyze these snapshots and generate a learning curve (`learning_curve.png`) as well as tabular progress data (`learning_progress.csv`).  
The interface allows for both human-vs-AI (GUI) and AI-vs-AI self-play for accelerated learning.  
All data, logs, and evaluations are systemically grouped and transparently stored.

---

## 🧠 Main Features

- **Interactive Chess (GUI):** Human vs. AI with visual feedback
- **AI-vs-AI Mode:** Automatic execution and evaluation of many games
- **Resonance-logic Experience Storage:** Weighted move sequences, snapshots
- **Snapshot Export:** Periodic saving of the learning state (`/snapshots/`)
- **Learning Curve Analysis:** Aggregation and visualization of AI quality
- **CSV Evaluation:** Progress of all snapshots in tabular form
- **Systemic Logging:** Logs in the `/logs/` directory

---

## 🚀 Installation

### Prerequisites

- Python **3.8** or newer (recommended: 3.8–3.13)
- Virtual environment recommended (optional)

### Step-by-step Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/DominicReneSchu/public.git
cd public/en/facts/simulations/resonance_chess/ResoChess
```

#### 2. Install dependencies

**Systemic (recommended):**

```bash
pip install .
```

> Alternatively, for testing only:  
> `pip install -r requirements.txt`

#### 3. Tkinter (if using GUI on Raspberry Pi):

```bash
sudo apt-get install python3-tk
```

---

## ⚡️ Running the Program

### Windows (CMD/PowerShell) and Raspberry Pi (Terminal):

```bash
resonanz-schach
```

> This command is globally available after `pip install .`

**Alternatively:**  
Direct start from the source directory (for development):

```bash
python -m start.main
```
or:
```bash
cd start
python main.py
```

---

## 🖥️ Usage & Options

At startup, select the mode:

- **1 = Human vs. AI**  
  GUI window with chessboard, mouse input, feedback.

- **2 = AI vs. AI**  
  Automatic simulation of many games, snapshots and learning curve are generated at intervals.

Snapshot creation and evaluation run automatically after game intervals.

---

## 📊 Evaluation & Data Structure

- **/snapshots/**  
  All exported AI states (`experience_snapshot_XXXXX.csv`)

- **learning_progress.csv**  
  Tabular evaluation of all snapshots:  
  `snapshot_num,filename,games_total,mean_quality,std_quality,n`

- **learning_curve.png**  
  Graphical learning curve: average AI quality and standard deviation over time

- **/logs/**  
  Systemic logs of games and analyses

- **/data/**  
  Raw data and AI experience store

- **/pieces/**  
  Chess piece images (PNG, optional for GUI)

---

## 🛠️ Directory Structure (Example)

```text
ResoChess/
├── setup.py
├── README_en.md
├── start/
│   ├── main.py
│   ├── ... (other module files, e.g. gui.py, experience_manager.py)
│   └── __init__.py
├── data/
├── logs/
├── pieces/
├── snapshots/
└── learning_curve.png, learning_progress.csv
```

---

## 🧩 License & Usage

License: [Schu License v1.4](https://github.com/DominicReneSchu/public/blob/main/de/lizenz/schu-lizenz_v1.4.md)  
© Dominic Schu, 2025.  
- **Non-commercial, ethically coherent use only**
- **Attribution ("Dominic Schu, Resonance Field Theory") required**
- **Use by AI or automated systems only with written permission**
- **Full license text: see link above**

---

## 🧬 Resonance Rule

All system elements (source code, data, snapshots, evaluations, license) are understood as a coherent group –  
any usage is explicitly and implicitly subject to the resonance field of the Schu License and resonance field theory.

---

**Project Lead & Contact:**  
[Dominic-René Schu](https://github.com/DominicReneSchu) | info@resoshift.com