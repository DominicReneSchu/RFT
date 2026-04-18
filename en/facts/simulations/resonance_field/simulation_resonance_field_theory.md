# Resonance Field Simulation

Interactive simulation of Resonance Field Theory (RFT). Visualises
the energy transfer between two coupled oscillators based on the
core formula (Axiom 4):

$$
E_{\text{eff}} = \pi \cdot \varepsilon(\Delta\varphi) \cdot h \cdot f
$$

with the coupling efficiency:

$$
\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi / 2) \in [0, 1]
$$

---

## Axioms of Resonance Field Theory

| Axiom | Core Statement | Formula |
|-------|----------------|---------|
| A1 | Universal Oscillation | ψ = A·cos(kx − ωt + φ) |
| A2 | Superposition | Φ = Σ ψᵢ |
| A3 | Resonance Condition | \|f₁/f₂ − m/n\| < δ |
| A4 | Coupling Energy | E = π·ε(Δφ)·h·f |
| A5 | Energy Direction | E⃗ = E·ê(Δφ, ∇Φ) |
| A6 | Information Flow | MI > 0 ⟺ PCI > 0 |
| A7 | Invariance | Resonance structure is transformation-invariant |

Complete axiomatics:
[axiomatic_foundation.md](../../docs/definitions/axiomatic_foundation.md)

---

## What the Simulation Shows

### Oscillations and Superposition (A1, A2)

Two oscillators with frequencies f₁ and f₂ oscillate independently.
Their superposition generates interference patterns — constructive
at resonance, destructive at detuning.

### Resonance Condition (A3)

The simulation automatically checks whether f₁/f₂ forms a rational
ratio n/m (within a tolerance δ = 1%).
At resonance the coupling is activated.

### Coupling Efficiency (A4)

The coupling efficiency ε(Δφ) = cos²(Δφ/2) determines the
fraction of transmitted resonance energy:

- Δφ = 0 → ε = 1 (perfect coupling, phase equality)
- Δφ = π/2 → ε = 0.5 (half coupling)
- Δφ = π → ε = 0 (no coupling, antiphase)

### Energy Direction (A5)

The energy direction vector is computed as the difference of
instantaneous energies on two time scales and shows
in which direction energy flows.

### Coupling Types

Three models of energy transfer:

- **Linear:** E_trans = ε · ψ₁ · ψ₂
- **Quadratic:** E_trans = ε · ψ₁² · ψ₂
- **Trigonometric:** E_trans = ε · sin(ψ₁) · sin(ψ₂)

---

## Boundary Cases of Coupling Efficiency

| Condition | ε | Energy | Physics |
|-----------|---|--------|---------|
| Perfect coupling (Δφ = 0) | 1 | π·h·f | Maximum resonance energy |
| Classical limit (ε = 1/π) | 0.318 | h·f | Planck equation |
| Natural damping (ε = 1/e) | 0.368 | (π/e)·h·f | After relaxation time |
| Half coupling (Δφ = π/2) | 0.5 | π·h·f/2 | 90° phase shift |
| No coupling (Δφ = π) | 0 | 0 | Decoupled systems |

---

<p align="center">
  <img src="images/simulation_rft.png" alt="RFT" width="800"/>
</p>

---

## Requirements

- Python ≥ 3.8
- Installed packages:

```bash
pip install numpy matplotlib
```

---

## Usage

```bash
python simulation_resonance_field_theory.py
```

The interactive sliders in the matplotlib window allow
real-time variation of all parameters:

- **f₁, f₂** — Frequencies of the two oscillators
- **Δφ** — Phase difference (determines ε via cos²(Δφ/2))
- **t_max** — Simulation duration
- **Coupling** — Coupling model (linear, quadratic, trigonometric)

---

## Source Code

[simulation_resonance_field_theory.py](simulation_resonance_field_theory.py)

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

## Cross-Confirmation within RFT

This result confirms and is confirmed by independent results from other domains:

| Result here | Confirmed by | Domain | Link |
|---|---|---|---|
| PCI → MI, directional energy flow control via ε(Δφ) | Coupled oscillators: more detailed oscillator coupling with resonance detection | Classical mechanics | [→ Coupled oscillators](../coupled_oscillators/coupled_oscillators.md) |
| ε(Δφ) = cos²(Δφ/2) in resonance field dynamics | FLRW simulation: same coupling efficiency at cosmological scale | Cosmology | [→ FLRW](../FLRW_simulations/README.md) |
| Coupling efficiency controls energy exchange | Schrödinger simulation: quantum-mechanical version of the same coupling | Quantum mechanics | [→ Schrödinger](../schrodinger/README.md) |

> **One equation — E = π·ε(Δφ)·ℏ·f — confirmed across quantum mechanics, cosmology, nuclear physics, and spacetime geometry.**

---

⬅️ [Back to Overview](../../../README.md#simulations)
