# Resonance Field Theory – Python Toolkit

Welcome to the official documentation of the Python toolkit for **Resonance Field Theory**.  
This package enables the numerical simulation, analysis, and visualization of resonance phenomena according to the theory of Dominic-René Schu.

---

## Overview

- **Calculation of resonance energy** based on normalized amplitude (A), temperature (T), eigenfrequency (omega₀), and damping (gamma).
- **Entropy calculation** as a measure of order in the resonance field.
- **Batch and parameter studies**: Systematic scans and export of results.
- **Modular structure**: Easily extendable for new models, couplings, and visualizations.
- **Scientific standard**: Typing, error checking, and clear documentation.
- **Interactive notebooks** and visualization options.

---

## Installation

```bash
pip install numpy matplotlib pandas
```

(Optional visualization: `seaborn`)

---

## Getting Started

### 1. Import

```python
from schu_resonanzfeld import (
    berechne_resonanzenergie,
    berechne_resonanzentropie,
    plot_resonanzfeld,
)
```

### 2. Example: Calculate and plot resonance field

```python
import numpy as np

A = np.linspace(0.1, 5.0, 500)
T = np.linspace(0.1, 5.0, 500)

E_res, T_grid, A_grid = berechne_resonanzenergie(A, T)
S = berechne_resonanzentropie(E_res)

plot_resonanzfeld(T_grid, A_grid, E_res, S)
```

### 3. Batch studies and CSV export

See [examples/demo_batch_study.ipynb](../examples/demo_batch_study.ipynb) for a step-by-step guide.

---

## API Reference

### `berechne_resonanzenergie(A, T, omega_0=1.0, gamma=0.2)`

Computes the resonance field for the grids of $A$ and $T$.

**Parameters:**
- `A` (`ndarray`): Amplitudes (1D, positive)
- `T` (`ndarray`): Temperatures (1D, positive)
- `omega_0` (`float`): Eigenfrequency (default: 1.0)
- `gamma` (`float`): Damping (default: 0.2)

**Returns:**
- `E_res` (`ndarray`): Resonance energy
- `T_grid`, `A_grid` (`ndarray`): Grids for $T$ and $A$

---

### `berechne_resonanzentropie(E_res)`

Computes the resonance entropy S = –E_res · ln(E_res).

**Parameters:**  
- `E_res` (`ndarray`): Resonance energy (must be > 0)

**Returns:**  
- `S` (`ndarray`): Entropy

---

### `plot_resonanzfeld(T_grid, A_grid, E_res, S, save_path=None, show=True)`

3D visualization of resonance energy and entropy.

**Parameters:**  
- `T_grid`, `A_grid`: Grids (as from `berechne_resonanzenergie`)
- `E_res`, `S`: Fields
- `save_path` (optional): Filename for PNG export
- `show` (optional): Show plot (default: `True`)

---

## License

Your contribution is provided under the same license as the main project (see [README.md](../../../../README.en.md)).

© Dominic Schu, 2025 – All rights reserved.  
Use permitted for research and educational purposes.

---

➡️ [back to overview](../README.md)