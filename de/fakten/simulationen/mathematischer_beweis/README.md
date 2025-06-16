# Resonanzfeldtheorie – Python Toolkit

## Überblick

Dieses Toolkit bietet eine vollständige, wissenschaftlich fundierte Implementierung der Resonanzfeldtheorie in Python – von der numerischen Simulation bis zur Visualisierung, Batch-Analyse und Anbindung an LaTeX-Theorie-Pakete.

- **Numerische Simulation** der Resonanzenergie und Resonanzentropie
- **Batch-Studien** und automatisierter Parameter-Sweep
- **Visualisierung als 3D-Plot oder Heatmap**
- **Modular, robust, forschungstauglich**
- **Unit-Tests und Jupyter-Beispiele**
---

## Installation

```bash
pip install numpy matplotlib pandas
# Optional für Heatmaps:
pip install seaborn
```

---

### 1. Dokumentation

- [Resonanzfeldtheorie – Python Toolkit](docs/index.md)  
  - Dokumentation des Python-Toolkits

- [Begleitkapitel zur Simulation](begleitkapitel_resonanzfeld.md)  
  - Ein kompakter numerischer Beweis der Resonanzfeldtheorie

- [Beitrag zur Resonanzfeldtheorie – Python Toolkit](CONTRIBUTING.md)  
  - Hier findest du Hinweise, wie du beitragen kannst – egal ob als Wissenschaftler, Entwickler oder Interessierter.

## Schnelleinstieg

### Resonanzfeld berechnen und plotten

```python
import numpy as np
from schu_resonanzfeld import (
    berechne_resonanzenergie,
    berechne_resonanzentropie,
    plot_resonanzfeld,
)

A = np.linspace(0.1, 5.0, 500)
T = np.linspace(0.1, 5.0, 500)

E_res, T_grid, A_grid = berechne_resonanzenergie(A, T)
S = berechne_resonanzentropie(E_res)

plot_resonanzfeld(T_grid, A_grid, E_res, S)
```

### Batch-Studien durchführen & Ergebnisse speichern

Siehe [examples/demo_batch_study.ipynb](examples/demo_batch_study.ipynb).

---

## API-Referenz

Alle Funktionen sind mit Docstrings dokumentiert.  
Siehe [docs/index.md](docs/index.md) für Details.

---

## Tests

```bash
pytest tests/
```

---

## Dateistruktur

```plaintext
schu_resonanzfeld.py             # Hauptmodul
tests/test_schu_resonanzfeld.py  # Unit-Tests
examples/demo_batch_study.ipynb  # Jupyter-Notebook für Batch-Analysen
docs/index.md                    # Dokumentation
requirements.txt                 # Abhängigkeiten
README.md                        # Dieses Dokument
```

---

## Weiterentwicklung & Mitmachen

- **Eigene Modelle und Batch-Analysen** einfach durch Anpassung/Erweiterung der Python-Module.
- **Einbindung in größere Workflows** (z.B. HPC, Cloud, Jupyter, Streamlit) ist vorbereitet.
- **Mitarbeit willkommen!** Siehe CONTRIBUTING.md (bei Bedarf anlegen).

---

## Lizenz

Dein Beitrag steht unter derselben Lizenz wie das Hauptprojekt (siehe [README.md](../../../../README.md)).

---

*© Dominic Schu, 2025 – Alle Rechte vorbehalten.*

---

⬅️ [zurück](../README.md)
