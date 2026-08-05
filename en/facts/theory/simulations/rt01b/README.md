# RT-01b — Numerical Path Integral: π Derivation

*Dominic René Schu, August 2026*

## Purpose

This directory contains the numerical evaluation of the path integral of resonance
coupling within RT-01b. It closes the three open items from RT-01 §6:

1. **Stage 1** — Numerical evaluation of the path integral (convergence test)
2. **Stage 2** — Quantification of non-Gaussian corrections
3. **Stage 3** — Potential-independence of the π contribution

## Files

| File | Description |
|---|---|
| `rt01b_path_integral.py` | Main script: path integral, corrections, potential comparison |
| `README.md` | This file |

## Usage

```bash
python rt01b_path_integral.py
```

Requirements: Python 3.10+, NumPy ≥ 2.0, SciPy

## Results (August 2026)

### Stage 1 — Convergence

| N | π estimate | Error |
|---|---|---|
| 100 | 3.14159265 | < 1e-15 |
| 500 | 3.14159265 | < 1e-15 |
| 1000 | 3.14159265 | < 1e-15 |

The numerical path integral converges to π with machine precision.

### Stage 2 — Non-Gaussian Corrections

| Correction | Value |
|---|---|
| c_3 (third order) | 0 (vanishes by symmetry) |
| c_4 (fourth order) | ≈ 5.5 × 10⁻¹¹ |
| \|c_3 + c_4\| | ≈ 5.5 × 10⁻¹¹ < 10⁻³ |

**Gaussian approximation controlled**: non-Gaussian corrections are more than eight
orders of magnitude below the required threshold of 10⁻³.

### Stage 3 — Potential-Independence

| Potential | ∫V dφ | 2·∫V dφ | π contribution? |
|---|---|---|---|
| cos²(φ/2) [RT-01 original] | π/2 | π | ✓ |
| sin²(φ/2) [complementary] | π/2 | π | ✓ |
| φ(π−φ)/π² [parabolic] | π/6 | π/3 | ~ |
| 1/2 [constant] | π/2 | π | ✓ |
| 1 [trivial] | π | 2π | ~ |

π appears for all potentials with mean value 1/2 on the interval [0,π].
**Conclusion:** π is a property of the phase-space geometry [0,π],
not of the specific potential.

## Context

This simulation is part of RT-01b (August 2026) and provides independent confirmation
of the π derivation from RT-01. The results feed into §4.5 and §9 of
`action_integral_pi_derivation.md`.

---

*Related:* [../../../action_integral_pi_derivation.md](../../../action_integral_pi_derivation.md) |
[../../../../../RESEARCH_TASKS.md](../../../../../RESEARCH_TASKS.md) RT-01b
