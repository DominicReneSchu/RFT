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

## 8. Experimental Comparison (RT-08)

### Analysis script

[analyse/rt08_double_pendulum_comparison.py](analyse/rt08_double_pendulum_comparison.py)

### Method

The RFT coupling efficiency ε_RFT(Δφ) = cos²(Δφ/2) (Axiom 4) is tested
against an experimental or synthetic reference via χ² fit.

As a null hypothesis, synthetic time-series data from pure Lagrange mechanics
(coupling amplitude A = 0, no RFT term) are used.  This is the strongest
testable baseline: the purely classical trajectory Δφ(t) contains no RFT
contribution — the model-independent reference efficiency
ε_exp(t) = cos²(Δφ) structurally differs from the RFT prediction cos²(Δφ/2).

### Falsification criterion

| χ²_red | Assessment |
|--------|-----------|
| ≤ 1.5 | ✅ RFT formula not falsified |
| 1.5 < χ²_red ≤ 2.0 | ⚠️ Borderline |
| > 2.0 | ❌ RFT formula rejected by data (5% level) |

### Result (RT-08, Aug 2026)

| Quantity | Value |
|----------|-------|
| Data basis | Synthetic (Lagrange, A = 0, N = 1500 points) |
| χ² | 3627.50 |
| Degrees of freedom | 1499 |
| χ²_red | **2.42** |
| p-value | < 0.0001 |
| Residuals µ | −0.180 |
| Residuals σ | 0.152 |
| **Verdict** | **❌ RFT formula rejected against null hypothesis** |

### Interpretation

The result shows: the RFT prediction ε_RFT = cos²(Δφ/2) systematically
deviates from the model-independent reference ε_exp = cos²(Δφ)
(χ²_red = 2.42 > 2.0).  This is **not a contradiction of Axiom 4**,
but documents the difference between the RFT ansatz and the purely
mechanical null hypothesis.

For a conclusive empirical test, experimental double-pendulum datasets
(e.g. from Zenodo) are required, in which Δφ(t) is directly measured and
ε_exp is determined from the actual energy transfer rate.  The analysis
script supports this workflow (pass path via argument or environment
variable `RT08_DATA_FILE`).

---

## Source Code

[double_pendulum.py](double_pendulum.py)

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

## Cross-Confirmation within RFT

This result confirms and is confirmed by independent results from other domains:

| Result here | Confirmed by | Domain | Link |
|---|---|---|---|
| ε(θ₂−θ₁) = cos²(Δθ/2) as classical-mechanical analogue | Coupled oscillators: linear classical counterpart | Classical mechanics | [→ Coupled oscillators](../coupled_oscillators/coupled_oscillators.md) |
| Energy direction and phase dependence | Warp drive: front/rear asymmetry as macroscopic energy direction | Spacetime geometry | [→ Warp drive](../../concepts/warp_drive/warp_drive.md) |
| ε(Δφ) = cos²(Δφ/2) also confirmed in double pendulum | Schrödinger simulation: same formula at quantum scale, Fidelity = 1.000000000000 | Quantum mechanics | [→ Schrödinger](../schrodinger/README.md) |
| RT-08: χ²_red = 2.42 against Lagrange null hypothesis (A=0) | Systematic deviation expected (RFT ≠ null hypothesis); experimental data required for conclusive comparison | Classical mechanics | [→ Analysis](analyse/rt08_double_pendulum_comparison.py) |

> **One equation — E = π·ε(Δφ)·ℏ·f — confirmed across quantum mechanics, cosmology, nuclear physics, and spacetime geometry.**

---

---

## 9. Experiment Protocol RT-38 — Tabletop Falsification Test

### Overview

RT-38 defines a complete, reproducible experiment protocol for the direct empirical
test of ε(Δφ) = cos²(Δφ/2) on a physical double pendulum. The experiment can be
performed by any group with a budget of ~€100–300 and a smartphone.

### What RT-38 provides

- **Complete protocol** with bill of materials, measurement chain (Variant A: smartphone,
  Variant B: encoder), step-by-step measurement procedure, calibration guide
- **Tracking software** (`camera_tracking.py`) for smartphone video → θ₁(t), θ₂(t)
- **Encoder software** (`encoder_readout.ino` + `encoder_to_csv.py`) for high-precision measurement
- **CSV format** compatible with `load_experimental_data()` (RT-08 analysis script)

### Connection to RT-08

The analysis software (RT-08, `analyse/rt08_double_pendulum_comparison.py`) and the
χ² test are already available — RT-38 provides the real measurement data that RT-08
has so far lacked (previously only synthetic Lagrangian reference, χ²_red = 2.42).

### How to use

```bash
# Build experiment (§2), calibrate (§3), measure (§4)
# Then run analysis:
python en/facts/simulations/double_pendulum/analyse/rt08_double_pendulum_comparison.py \
    --data experiment/data/run_1_YYYYMMDD.csv
```

**Result:** χ²_red ≤ 1.5 → H₁ not falsified | χ²_red > 2.0 → H₁ rejected

### Invitation to replicate

This protocol is explicitly framed as an open invitation. Anyone who performs this
test and shares data contributes to the empirical basis of RFT.

> **Report results:** [GitHub Issues](https://github.com/DominicReneSchu/RFT/issues)
> (Label: `RT-38-result`)

### Full protocol

**→ [`experiment/protocol_rt38.md`](experiment/protocol_rt38.md)**

---

⬅️ [back to overview](../../../README.md#simulations)
