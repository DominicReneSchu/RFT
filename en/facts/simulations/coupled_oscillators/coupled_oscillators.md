# Simulation of Coupled Oscillators

Interactive Python simulation of two coupled harmonic
oscillators. Demonstrates coupling effects, energy exchange,
resonance detection, and energy balance within the framework of
Resonance Field Theory (Axioms A1–A4).

<p align="center">
  <img src="animation.gif" alt="Coupled Oscillators" width="800"/>
</p>

---

## Axiom Reference

| Axiom | Implementation |
|-------|----------------|
| A1 Oscillation | Two harmonic oscillators with ω₁, ω₂ |
| A2 Superposition | Superposition of displacements |
| A3 Resonance Condition | f₁/f₂ ≈ n/m is checked and displayed live |
| A4 Coupling Energy | ε = exp(−α·\|f₁−f₂\|), E_res = π·ε·h·f |

---

## Core Formula (Axiom 4)

$$
E_{\text{res}} = \pi \cdot \varepsilon \cdot h \cdot f
$$

The coupling operator ε = exp(−α·|f₁−f₂|) models the
frequency-dependent coupling: maximum at f₁ = f₂ (perfect
resonance), exponential decay with frequency difference.

---

## Features

* Numerical solution of coupled ODEs (`solve_ivp`)
* Interactive live animation with trajectory tracking
* Resonance detection (Axiom 3) with visual indicator
* Sliders: frequencies, coupling sharpness α, tolerance, speed
* Energy plot: kinetic, potential, coupling, total
* Coupling operator ε and resonance energies E_res(f₁), E_res(f₂)
* Resonance divergence |E_mech − E_res|
* Export: CSV and GIF

---

## Structure

| File | Function |
|------|----------|
| [`run.py`](run.py) | Entry point, UI, sliders, animation |
| [`parameters_and_functions.py`](parameters_and_functions.py) | Physics: ODE, coupling operator, energy |
| [`animation.py`](animation.py) | Plot update, energy lines |
| [`coupled_oscillators.py`](coupled_oscillators.py) | Minimal example (standalone) |
| [`export_csv.py`](export_csv.py) | CSV export |

---

## Usage

```bash
pip install numpy matplotlib scipy
python run.py
```

Standalone minimal example (without sliders):

```bash
python coupled_oscillators.py
```

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

## Cross-Confirmation within RFT

This result confirms and is confirmed by independent results from other domains:

| Result here | Confirmed by | Domain | Link |
|---|---|---|---|
| Energy exchange at resonance, ε = exp(−α·|f₁−f₂|) | Schrödinger simulation: quantum-mechanical counterpart, Fidelity = 1.000000000000 | Quantum mechanics | [→ Schrödinger](../schrodinger/README.md) |
| Nonlinear coupling of two oscillators | Double pendulum: nonlinear extension of the same coupling logic | Classical mechanics | [→ Double pendulum](../double_pendulum/accompanying_chapter_double_pendulum.md) |
| PCI and MI from coupling logic | Resonance field simulation: PCI → MI shows directional energy flow control | Field theory | [→ Resonance field](../resonance_field/simulation_resonance_field_theory.md) |
| E_res = π·ε·h·f, classical coupling | ResoCalc: torque as a special case of oscillator coupling | Engineering | [→ ResoCalc](../../concepts/ResoCalc/resocalc.md) |

> **One equation — E = π·ε(Δφ)·ℏ·f — confirmed across quantum mechanics, cosmology, nuclear physics, and spacetime geometry.**

---

⬅️ [Back to Overview](../../../README.md#simulations)
