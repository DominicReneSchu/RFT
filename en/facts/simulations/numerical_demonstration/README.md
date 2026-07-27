# Resonance Field Theory — Numerical Demonstration

Numerical analysis and visualisation: resonance energy,
coupling efficiency and resonance entropy over the
(A, τ) parameter space.

> **Context:** This simulation demonstrates the internal
> consistency of Axioms A3–A5. It is not an empirical
> validation. For the empirical test see the
> [Monte Carlo analysis](../../empirical/monte_carlo/monte_carlo_test/monte_carlo.md).

---

## Axiom Reference

| Axiom | What is demonstrated |
|-------|----------------------|
| A3 Resonance condition | Lorentz profile: peak at ω_ext ≈ ω₀ |
| A4 Coupling efficiency | ε = E_res / A ∈ (0, 1] |
| A5 Stable field | Entropy S = −ε·ln(ε) ≥ 0 |

---

## Quick Start

```bash
pip install numpy matplotlib
python numerical_demonstration.py
```

Tests:
```bash
python tests/test_numerical_demonstration.py
```

---

## File Structure

| File | Purpose |
|------|---------|
| [`numerical_demonstration.py`](numerical_demonstration.py) | Main module: calculation + visualisation |
| [`accompanying_chapter_numerical_demonstration.md`](accompanying_chapter_numerical_demonstration.md) | Explanation and context |
| [`tests/test_numerical_demonstration.py`](tests/test_numerical_demonstration.py) | 16 unit tests (standalone + pytest) |
| [`requirements.txt`](requirements.txt) | Dependencies |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution guidelines |
| [`docs/index.md`](docs/index.md) | API documentation |

---

## API

```python
from numerical_demonstration import (
    berechne_resonanzenergie,
    berechne_kopplungseffizienz,
    berechne_resonanzentropie,
    plot_numerische_demonstration,
)
```

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

## Cross-Confirmation within RFT

This result confirms and is confirmed by independent results from other domains:

| Result here | Confirmed by | Domain | Link |
|---|---|---|---|
| Consistency of A3–A5 over (A, τ) parameter space | FLRW simulation: same consistency over 1,530 runs, Δd_η > 6σ | Cosmology | [→ FLRW](../FLRW_simulations/README.md) |
| Perturbation theory as independent consistency check | Schrödinger simulation: perturbation theory 1−F ~ λ², 0.05% deviation | Quantum mechanics | [→ Schrödinger](../schrodinger/README.md) |

> **One equation — E = π·ε(Δφ)·ℏ·f — confirmed across quantum mechanics, cosmology, nuclear physics, and spacetime geometry.**

---

⬅️ [back](../../../README.md#simulations)
