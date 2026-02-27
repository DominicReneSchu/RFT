# Resonanzfeldtheorie — Numerische Analyse

Numerische Simulation und Visualisierung der Resonanzfeldtheorie:
Resonanzenergie, Kopplungseffizienz und Resonanzentropie über dem
(A, τ)-Parameterraum.

---

## Axiom-Bezug

| Axiom | Was demonstriert wird |
|-------|----------------------|
| A3 Resonanzbedingung | Lorentz-Profil: Peak bei ω_ext ≈ ω₀ |
| A4 Kopplungseffizienz | ε = E_res / A ∈ (0, 1] |
| A5 Stabiles Feld | Entropie S = −ε·ln(ε) ≥ 0 |

---

## Schnelleinstieg

```bash
pip install numpy matplotlib
python resonanzfeld.py
```

Erzeugt `plot.png` und Konsolen-Output:

```
Resonanzfeldtheorie — Numerische Analyse
==================================================
A ∈ [0.1, 5.0], τ ∈ [0.1, 5.0]
E_res ∈ [0.0000, 5.0000]
ε ∈ [0.0000, 1.0000]
S ∈ [0.0000, 0.3679]
==================================================
```

---

## Dateistruktur

| Datei | Funktion |
|-------|----------|
| [`resonanzfeld.py`](resonanzfeld.py) | Hauptmodul: Berechnung + Visualisierung |
| [`begleitkapitel_resonanzfeld.md`](begleitkapitel_resonanzfeld.md) | Physikalische Erläuterung |
| [`requirements.txt`](requirements.txt) | Abhängigkeiten |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Beitragsrichtlinien |

---

## API

```python
from resonanzfeld import (
    berechne_resonanzenergie,
    berechne_kopplungseffizienz,
    berechne_resonanzentropie,
    plot_resonanzfeld,
)

A = np.linspace(0.1, 5.0, 500)
tau = np.linspace(0.1, 5.0, 500)

E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
eps = berechne_kopplungseffizienz(E_res, A_grid)
S = berechne_resonanzentropie(eps)

plot_resonanzfeld(tau_grid, A_grid, E_res, eps, S,
                  save_path="plot.png")
```

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück](../README.md)