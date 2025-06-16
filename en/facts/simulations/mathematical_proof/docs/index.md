# Resonanzfeldtheorie – Python Toolkit

Willkommen zur offiziellen Dokumentation des Python-Toolkits zur **Resonanzfeldtheorie**.  
Dieses Paket ermöglicht die numerische Simulation, Analyse und Visualisierung von Resonanzphänomenen gemäß der Theorie von Dominic-René Schu.

---

## Übersicht

- **Berechnung der Resonanzenergie** auf Basis normierter Amplitude (A), Temperatur (T), Eigenfrequenz (omega₀) und Dämpfung (gamma).
- **Entropie-Berechnung** als Maß für die Ordnung im Resonanzfeld.
- **Batch- und Parameterstudien**: Systematische Scans und Export der Ergebnisse.
- **Modulare Struktur**: Leicht erweiterbar für neue Modelle, Kopplungen und Visualisierungen.
- **Wissenschaftlicher Standard**: Typisierung, Fehlerprüfung und klare Dokumentation.
- **Interaktive Notebooks** und Visualisierungsmöglichkeiten.

---

## Installation

```bash
pip install numpy matplotlib pandas
```

(Optionale Visualisierung: `seaborn`)

---

## Erste Schritte

### 1. Import

```python
from schu_resonanzfeld import (
    berechne_resonanzenergie,
    berechne_resonanzentropie,
    plot_resonanzfeld,
)
```

### 2. Beispiel: Resonanzfeld berechnen und plotten

```python
import numpy as np

A = np.linspace(0.1, 5.0, 500)
T = np.linspace(0.1, 5.0, 500)

E_res, T_grid, A_grid = berechne_resonanzenergie(A, T)
S = berechne_resonanzentropie(E_res)

plot_resonanzfeld(T_grid, A_grid, E_res, S)
```

### 3. Batch-Studien und CSV-Export

Siehe [examples/demo_batch_study.ipynb](../examples/demo_batch_study.ipynb) für eine Schritt-für-Schritt-Anleitung.

---

## API-Referenz

### `berechne_resonanzenergie(A, T, omega_0=1.0, gamma=0.2)`

Berechnet das Resonanzfeld für die Gitter aus $A$ und $T$.

**Parameter:**
- `A` (`ndarray`): Amplituden (1D, positiv)
- `T` (`ndarray`): Temperaturen (1D, positiv)
- `omega_0` (`float`): Eigenfrequenz (Standard: 1.0)
- `gamma` (`float`): Dämpfung (Standard: 0.2)

**Rückgabe:**
- `E_res` (`ndarray`): Resonanzenergie
- `T_grid`, `A_grid` (`ndarray`): Gitter für $T$ und $A$

---

### `berechne_resonanzentropie(E_res)`

Berechnet die Resonanzentropie S = –E_res · ln(E_res).

**Parameter:**  
- `E_res` (`ndarray`): Resonanzenergie (muss > 0 sein)

**Rückgabe:**  
- `S` (`ndarray`): Entropie

---

### `plot_resonanzfeld(T_grid, A_grid, E_res, S, save_path=None, show=True)`

3D-Visualisierung der Resonanzenergie und Entropie.

**Parameter:**  
- `T_grid`, `A_grid`: Gitter (wie aus `berechne_resonanzenergie`)
- `E_res`, `S`: Felder
- `save_path` (optional): Dateiname für PNG-Speicherung
- `show` (optional): Anzeigeplot (Standard: `True`)

---

## Lizenz

Dein Beitrag steht unter derselben Lizenz wie das Hauptprojekt (siehe [README.md](../../../../README.md)).

© Dominic Schu, 2025 – Alle Rechte vorbehalten.  
Nutzung für Forschungs- und Bildungszwecke gestattet.

---

➡️ [zurück](../README.md)