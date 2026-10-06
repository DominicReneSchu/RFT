# Resonance Field Theory — Numerical Demonstration (API Documentation)

Python toolkit for the numerical demonstration of
Resonance Field Theory: resonance energy (Lorentz profile),
coupling efficiency and resonance entropy.

---

## Installation

```bash
pip install numpy matplotlib
```

---

## Quick Start

```python
import numpy as np
from numerical_demonstration import (
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

## API Reference

### `berechne_resonanzenergie(A, tau, omega_0=1.0, gamma=0.2)`

Resonance energy as a Lorentz profile over the (A, τ) grid.

$$
E_{\mathrm{res}} = \frac{A}{1 + \left(\frac{\omega_{\mathrm{ext}} - \omega_0}{\gamma}\right)^2}
$$

with ω_ext = ω₀ · (1 + sin(τ)).

| Name | Type | Description |
|------|------|-------------|
| `A` | ndarray (1D) | Amplitudes, positive |
| `tau` | ndarray (1D) | Detuning parameter, positive |
| `omega_0` | float | Natural frequency (default: 1.0) |
| `gamma` | float | Damping constant (default: 0.2) |

**Returns:** `(E_res, tau_grid, A_grid)`

**Raises:** `ValueError` for negative values or non-1D input

---

### `berechne_kopplungseffizienz(E_res, A_grid)`

Coupling efficiency as normalised resonance energy (Axiom A4).

$$
\varepsilon = \frac{E_{\mathrm{res}}}{A} \in (0, 1]
$$

| Name | Type | Description |
|------|------|-------------|
| `E_res` | ndarray | Resonance energy |
| `A_grid` | ndarray | Amplitude grid |

**Returns:** `eps` — clipped to (1e-8, 1.0]

---

### `berechne_resonanzentropie(eps)`

Resonance entropy as an information measure (Axiom A5).

$$
S = -\varepsilon \cdot \ln(\varepsilon), \quad \varepsilon \in (0, 1]
$$

| Name | Type | Description |
|------|------|-------------|
| `eps` | ndarray | Coupling efficiency ∈ (0, 1] |

**Returns:** `S` — ndarray, S ≥ 0

---

### `plot_numerische_demonstration(tau_grid, A_grid, E_res, eps, S, save_path=None, show=True)`

Three 3D surfaces: E_res, ε, S.

| Name | Type | Description |
|------|------|-------------|
| `tau_grid` | ndarray | Detuning grid |
| `A_grid` | ndarray | Amplitude grid |
| `E_res` | ndarray | Resonance energy |
| `eps` | ndarray | Coupling efficiency |
| `S` | ndarray | Resonance entropy |
| `save_path` | str, optional | PNG file path |
| `show` | bool | Display plot (default: True) |

---

## Tests

```bash
cd numerical_demonstration
python tests/test_numerical_demonstration.py
# or:
pytest tests/ -v
```

---

## Axiom Reference

| Function | Axiom | What is demonstrated |
|----------|-------|---------------------|
| `berechne_resonanzenergie` | A3 | Lorentz resonance curve |
| `berechne_kopplungseffizienz` | A4 | ε = E_res / A |
| `berechne_resonanzentropie` | A5 | S = −ε·ln(ε) |

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

⬅️ [back](../README.md)
