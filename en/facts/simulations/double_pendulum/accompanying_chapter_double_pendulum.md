# Double Pendulum — Interactive Simulation

Interactive simulation of a double pendulum with dynamic
coupling efficiency ε(Δφ) = cos²(Δφ/2) according to Axiom 4.
Demonstrates chaotic dynamics, energy exchange, and
resonance coupling.

<p align="center">
  <img src="doppelpendel.gif" alt="Animation Double Pendulum" width="800"/>
</p>

---

## Axiom Reference

| Axiom | Implementation |
|-------|---------------|
| A1 Oscillation | Both pendulum arms oscillate at their natural frequency |
| A2 Superposition | Interference of oscillation patterns in the trails |
| A4 Coupling efficiency | ε(Δφ) = cos²((θ₂−θ₁)/2) is calculated dynamically from the state |

---

## 1. Coupling Efficiency (Axiom 4)

The coupling efficiency ε determines the fraction of transferred
resonance energy and is calculated **dynamically** from the phase
difference of the pendulum arms:

$$
\varepsilon(\Delta\varphi) = \cos^2\!\left(\frac{\theta_2 - \theta_1}{2}\right) \in [0, 1]
$$

### Limiting Cases

| Δφ = θ₂ − θ₁ | ε | Meaning |
|---------------|---|---------|
| 0 | 1.0 | Perfect coupling — pendulums in phase |
| π/2 | 0.5 | Half coupling |
| π | 0.0 | No coupling — pendulums in antiphase |

### Effective Coupling Term

The resonance coupling term in the equations of motion is:

$$
\tau_{\text{coupling}} = \pm\, A \cdot \varepsilon(\theta_2 - \theta_1) \cdot \sin(\theta_2 - \theta_1)
$$

- **A** (Slider): Coupling amplitude — scales the strength
- **ε** (dynamic): Coupling efficiency — determines the fraction
- **sin(Δφ)**: Direction of the coupling torque

Since ε is maximal at phase equality and vanishes at antiphase,
energy is preferentially transferred when the pendulums have
similar phase — exactly as Axiom 4 requires.

---

## 2. Interactive Controls

| Slider | Meaning |
|--------|---------|
| θ₁, θ₂ | Initial angles of both pendulum arms |
| ω₁, ω₂ | Initial angular velocities |
| m₁, m₂ | Masses |
| L₁, L₂ | Pendulum lengths |
| A | Coupling amplitude (strength of the resonance term) |
| Trail length | Trail length (last N positions) |

**Important:** ε is not a slider — the coupling efficiency is
calculated automatically from the current state at every time
step and displayed live.

---

## 3. Energy Display

Live above the pendulum:

- **T** — Kinetic energy
- **V** — Potential energy
- **E_coupling** — Coupling energy (scaled with A · ε)
- **κ** = E_coupling / |E_total| — Coupling ratio
- **ε** — Current coupling efficiency + phase difference Δφ

---

## 4. Trails and Chaos

The colored traces of the mass points visualize the
chaotic dynamics:

- **A = 0:** Pure double pendulum without additional coupling
- **A small:** Weak resonance coupling, classical chaos
- **A large:** Strong synchronization tendency, trails become
  more regular when ε ≈ 1 (pendulums in phase)

---

## 5. Physical Background

The double pendulum is a classical nonlinear, chaotic
system. The equations of motion follow from Lagrangian mechanics
and are derived in standard literature (e.g., Goldstein, "Classical
Mechanics").

The **natural mechanical coupling** is already contained in the
Lagrange equations (shared suspension point). The resonance
coupling term A · ε · sin(Δφ) models an **additional** interaction
that enables the interpretation as a resonance system in the
sense of RFT.

---

## 6. Execution

```bash
pip install numpy matplotlib scipy
python double_pendulum.py
```

---

## 7. Extension Possibilities

- Energy plot as time series (T, V, E_coupling, ε)
- Poincaré sections for chaos analysis
- Pendulum chain (more than two pendulums)
- FFT of the angular motions
- Damping term
- Axiom 5: Energy direction as vector

---

## Source Code

[double_pendulum.py](double_pendulum.py)

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

⬅️ [back to overview](../../../README.md#simulations)
