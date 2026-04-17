# Resonanzfeldtheorie — Numerische Demonstration (API-Dokumentation)

Python-Toolkit zur numerischen Demonstration der
Resonanzfeldtheorie: Resonanzenergie (Lorentz-Profil),
Kopplungseffizienz und Resonanzentropie.

---

## Installation

```bash
pip install numpy matplotlib
```

---

## Schnellstart

```python
import numpy as np
from numerische_demonstration import (
    berechne_resonanzenergie,
    berechne_kopplungseffizienz,
    berechne_resonanzentropie,
    plot_numerische_demonstration,
)

A = np.linspace(0.1, 5.0, 500)
tau = np.linspace(0.1, 5.0, 500)

E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
eps = berechne_kopplungseffizienz(E_res, A_grid)
S = berechne_resonanzentropie(eps)

plot_numerische_demonstration(tau_grid, A_grid, E_res, eps, S,
                  save_path="plot.png")
```

---

## API-Referenz

### `berechne_resonanzenergie(A, tau, omega_0=1.0, gamma=0.2)`

Resonanzenergie als Lorentz-Profil über dem (A, τ)-Gitter.

$$
E_{\mathrm{res}} = \frac{A}{1 + \left(\frac{\omega_{\mathrm{ext}} - \omega_0}{\gamma}\right)^2}
$$

mit ω_ext = ω₀ · (1 + sin(τ)).

| Name | Typ | Beschreibung |
|------|-----|-------------|
| `A` | ndarray (1D) | Amplituden, positiv |
| `tau` | ndarray (1D) | Verstimmungsparameter, positiv |
| `omega_0` | float | Eigenfrequenz (Default: 1.0) |
| `gamma` | float | Dämpfungskonstante (Default: 0.2) |

**Rückgabe:** `(E_res, tau_grid, A_grid)`

**Raises:** `ValueError` bei negativen Werten oder nicht-1D-Input

---

### `berechne_kopplungseffizienz(E_res, A_grid)`

Kopplungseffizienz als normierte Resonanzenergie (Axiom A4).

$$
\varepsilon = \frac{E_{\mathrm{res}}}{A} \in (0, 1]
$$

| Name | Typ | Beschreibung |
|------|-----|-------------|
| `E_res` | ndarray | Resonanzenergie |
| `A_grid` | ndarray | Amplituden-Gitter |

**Rückgabe:** `eps` — geclippt auf (1e-8, 1.0]

---

### `berechne_resonanzentropie(eps)`

Resonanzentropie als Informationsmaß (Axiom A5).

$$
S = -\varepsilon \cdot \ln(\varepsilon), \quad \varepsilon \in (0, 1]
$$

| Name | Typ | Beschreibung |
|------|-----|-------------|
| `eps` | ndarray | Kopplungseffizienz ∈ (0, 1] |

**Rückgabe:** `S` — ndarray, S ≥ 0

---

### `plot_numerische_demonstration(tau_grid, A_grid, E_res, eps, S, save_path=None, show=True)`

Drei 3D-Oberflächen: E_res, ε, S.

| Name | Typ | Beschreibung |
|------|-----|-------------|
| `tau_grid` | ndarray | Verstimmungs-Gitter |
| `A_grid` | ndarray | Amplituden-Gitter |
| `E_res` | ndarray | Resonanzenergie |
| `eps` | ndarray | Kopplungseffizienz |
| `S` | ndarray | Resonanzentropie |
| `save_path` | str, optional | PNG-Dateipfad |
| `show` | bool | Plot anzeigen (Default: True) |

---

## Tests

```bash
cd numerische_demonstration
python tests/test_numerische_demonstration.py
# oder:
pytest tests/ -v
```

---

## Axiom-Bezug

| Funktion | Axiom | Was wird demonstriert |
|----------|-------|---------------------|
| `berechne_resonanzenergie` | A3 | Lorentz-Resonanzkurve |
| `berechne_kopplungseffizienz` | A4 | ε = E_res / A |
| `berechne_resonanzentropie` | A5 | S = −ε·ln(ε) |

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück](../README.md)