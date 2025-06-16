# Resonance Field Theory – Python Toolkit

## Overview

This toolkit provides a complete, scientifically grounded implementation of Resonance Field Theory in Python – from numerical simulation to visualization, batch analysis, and integration with LaTeX theory packages.

- **Numerical simulation** of resonance energy and resonance entropy
- **Batch studies** and automated parameter sweeps
- **Visualization as 3D plot or heatmap**
- **Modular, robust, research-grade**
- **Unit tests and Jupyter examples**

---

## Installation

```bash
pip install numpy matplotlib pandas
# Optional for heatmaps:
pip install seaborn
```

---

### 1. Documentation

- [Resonance Field Theory – Python Toolkit](docs/index.md)  
  - Documentation of the Python toolkit

- [Companion Chapter to the Simulation](begleitkapitel_resonanzfeld.md)  
  - A concise numerical proof of Resonance Field Theory

- [Contribution Guide – Python Toolkit](CONTRIBUTING.md)  
  - Guidance for contributing – whether as scientist, developer, or interested party.

## Quickstart

### Calculate and plot resonance field

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

### Run batch studies & save results

See [examples/demo_batch_study.ipynb](examples/demo_batch_study.ipynb).

---

## API Reference

All functions are documented with docstrings.  
See [docs/index.md](docs/index.md) for details.

---

## Tests

```bash
pytest tests/
```

---

## File Structure

```plaintext
schu_resonanzfeld.py             # Main module
tests/test_schu_resonanzfeld.py  # Unit tests
examples/demo_batch_study.ipynb  # Jupyter notebook for batch analyses
docs/index.md                    # Documentation
requirements.txt                 # Dependencies
README.md                        # This document
```

---

## Further Development & Contribution

- **Custom models and batch analyses** can be created by adapting/extending the Python modules.
- **Integration into larger workflows** (e.g., HPC, Cloud, Jupyter, Streamlit) is prepared.
- **Contributions welcome!** See CONTRIBUTING.md (create if needed).

---

## License

Your contribution is provided under the same license as the main project (see [README.md](../../../../README.en.md)).

---

*© Dominic Schu, 2025 – All rights reserved.*

---

⬅️ [back](../README.en.md)