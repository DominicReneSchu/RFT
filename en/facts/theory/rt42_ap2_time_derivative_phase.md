# RT-42 AP2 — Time Derivative of the Phase

*Dominic-René Schu, September 2026*
*Status: ✅ Completed (Sep 2026)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Coupling Dynamics and Starting Point](#2-coupling-dynamics-and-starting-point)
3. [Derivation of the Differential Equation for Δφ(t)](#3-derivation-of-the-differential-equation-for-δφt)
4. [Identification with the Expansion Rate H](#4-identification-with-the-expansion-rate-h)
5. [Stationary and Dynamic Solutions](#5-stationary-and-dynamic-solutions)
6. [Consistency with A8 — Phase Dynamics and the Speed of Light](#6-consistency-with-a8--phase-dynamics-and-the-speed-of-light)
7. [Verification of the Success Criterion](#7-verification-of-the-success-criterion)
8. [Result and Outlook on AP3–AP7](#8-result-and-outlook-on-ap3ap7)

---

## 1. Objective and Success Criterion

**Task (RT-42 AP2):** Determine Δφ̇(t) from the coupling dynamics and interpret it
as the expansion rate.

**Success criterion:** Closed differential equation for Δφ(t), comparable to
Friedmann solutions.

**Result:** The success criterion is satisfied. The differential equation
```
    Δφ̇ = β · tan(Δφ/2)
```
is a closed, analytically solvable ODE for Δφ(t). The solution yields a
Friedmann-comparable expansion dynamics:
```
    ε(t) = 1 − sin²(Δφ₀/2) · e^{βt}
    H(t) = H₀ · √ε(t)
```
The Hubble parameter H(t) follows directly from the phase dynamics, without a
separate Λ-term.

---

## 2. Coupling Dynamics and Starting Point

### 2.1 Homogeneous Field (RT-42 Baseline)

In the cosmological limit (AP1: spatially homogeneous phase Δφ(t)), the coupling
dynamics reads:
```
    dK/dt = α · G · cos(Δφ) − β · K
```

| Symbol | Meaning |
|--------|---------|
| K      | Coupling strength between resonators |
| α      | Coupling growth rate |
| G      | G_sync coupling constant (Axiom A5) |
| β      | Dissipation rate (β > 0) |
| Δφ(t)  | Global phase difference (AP1) |

### 2.2 Adiabatic Condition and K₀

In adiabatic equilibrium (dK/dt = 0):
```
    K_stat = (α·G/β) · cos(Δφ)
```

We parametrise the coupling strength consistently with A4:
```
    K(t) = K₀ · ε(Δφ(t))  =  K₀ · cos²(Δφ(t)/2)
```

Since in the equilibrium solution K_stat ∝ cos(Δφ) and K ∝ cos²(Δφ/2) = (1 + cos Δφ)/2
share the same qualitative behaviour, we identify:
```
    K₀ = α·G/β
```

This choice is consistent: for Δφ = 0 we have K = K₀ = αG/β = K_stat (maximum coupling).

---

## 3. Derivation of the Differential Equation for Δφ(t)

### 3.1 Differentiation of the Coupling Parametrisation

We differentiate K(t) = K₀ cos²(Δφ(t)/2) with respect to time:
```
    dK/dt = K₀ · d/dt[cos²(Δφ/2)]
           = K₀ · 2cos(Δφ/2) · (−sin(Δφ/2)) · (Δφ̇/2)
           = −(K₀/2) · sin(Δφ) · Δφ̇
```

### 3.2 Equating with the Coupling Equation

Substituting into dK/dt = αG cos(Δφ) − βK:
```
    −(K₀/2) · sin(Δφ) · Δφ̇  =  α·G · cos(Δφ) − β·K₀·cos²(Δφ/2)
```

With K₀ = αG/β:
```
    −(αG/2β) · sin(Δφ) · Δφ̇  =  αG · cos(Δφ) − αG · cos²(Δφ/2)
```

Dividing by αG:
```
    −(1/2β) · sin(Δφ) · Δφ̇  =  cos(Δφ) − cos²(Δφ/2)
```

### 3.3 Trigonometric Simplification

Using the identity cos(Δφ) = 2cos²(Δφ/2) − 1:
```
    cos(Δφ) − cos²(Δφ/2)  =  [2cos²(Δφ/2) − 1] − cos²(Δφ/2)
                            =  cos²(Δφ/2) − 1
                            =  −sin²(Δφ/2)
```

Hence:
```
    −(1/2β) · sin(Δφ) · Δφ̇  =  −sin²(Δφ/2)
```

### 3.4 Closed ODE for Δφ(t)

Rearranging using sin(Δφ) = 2sin(Δφ/2)cos(Δφ/2):
```
    (1/2β) · 2sin(Δφ/2)cos(Δφ/2) · Δφ̇  =  sin²(Δφ/2)
    (1/β) · sin(Δφ/2)cos(Δφ/2) · Δφ̇  =  sin²(Δφ/2)
```

Dividing by sin(Δφ/2) (valid for Δφ ≠ 0, 2π):
```
    (1/β) · cos(Δφ/2) · Δφ̇  =  sin(Δφ/2)
```

**Closed ODE:**
```
    Δφ̇ = β · tan(Δφ/2)
```

This is the central result of AP2: an autonomous, nonlinear first-order ODE for the
cosmological phase difference Δφ(t), derived entirely from the RFT coupling dynamics.

---

## 4. Identification with the Expansion Rate H

### 4.1 Direct Identification Δφ̇ ≠ H

From AP1: H(t) = H₀ · cos(Δφ/2)

From AP2: Δφ̇ = β · tan(Δφ/2) = β · sin(Δφ/2)/cos(Δφ/2)

The ratio:
```
    Δφ̇ / H = (β · sin(Δφ/2)/cos(Δφ/2)) / (H₀ · cos(Δφ/2))
            = (β/H₀) · sin(Δφ/2)/cos²(Δφ/2)
```

depends explicitly on Δφ and is not constant. **A direct identification Δφ̇ = H is
therefore not possible** (except in trivial special cases).

### 4.2 Indirect Relation via ε̇

The physically relevant connection passes through the coupling efficiency ε = cos²(Δφ/2):
```
    ε̇ = d/dt[cos²(Δφ/2)] = −sin(Δφ/2)cos(Δφ/2) · Δφ̇
       = −sin(Δφ/2)cos(Δφ/2) · β · tan(Δφ/2)
       = −β · sin²(Δφ/2)
       = −β · (1 − ε)
```

The equation
```
    ε̇ = −β (1 − ε)
```
is the Friedmann analogue: it describes how the coupling efficiency ε (and hence
the cosmological density Ω = ε from AP1) decreases at rate β.

### 4.3 Modified Raychaudhuri Equation

From H = H₀√ε, differentiating yields:
```
    Ḣ = H₀ · ε̇ / (2√ε)  =  H₀ · (−β(1−ε)) / (2√ε)
```

With H = H₀√ε → √ε = H/H₀:
```
    Ḣ = −(βH₀²/2) · (1−ε) / H
```

Since H² = H₀²ε and thus ε = H²/H₀²:
```
    Ḣ = −(β/2) · (H₀² − H²) / H
```

**Modified RFT Raychaudhuri equation:**
```
    Ḣ = −(β/2) · (H₀² − H²) / H
```

Comparison with the standard Raychaudhuri equation Ḣ = −4πG(ρ + p):

Identification:
```
    4πG(ρ + p)  =  (β/2)(H₀² − H²)/H
```

This shows that the dissipation parameter β controls the effective equation of state
(ρ + p) of the RFT cosmology.

---

## 5. Stationary and Dynamic Solutions

### 5.1 Stationary Solution (Δφ̇ = 0)

From Δφ̇ = β tan(Δφ/2) = 0:
```
    tan(Δφ/2) = 0  →  Δφ = 0  (mod 2π)
```

| Δφ | ε | H | Interpretation |
|----|---|---|----------------|
| 0  | 1 | H₀ | Maximum coupling — static de-Sitter-like universe |
| π  | 0 | 0  | Complete loss of coupling — unstable fixed point (not physically reachable) |

The fixed point Δφ = 0 corresponds to a static universe with maximum coupling
efficiency. Any infinitesimal perturbation Δφ > 0 drives the system into expansion
(Δφ̇ > 0 for β > 0).

### 5.2 Analytical Solution of the ODE

The ODE Δφ̇ = β tan(Δφ/2) is separable:
```
    dΔφ / tan(Δφ/2) = β · dt
    (cos(Δφ/2)/sin(Δφ/2)) · dΔφ = β · dt
```

Substitution u = sin(Δφ/2), du = (cos(Δφ/2)/2) dΔφ:
```
    2 du/u = β dt
    2 ln|u| = βt + C
    sin(Δφ(t)/2) = sin(Δφ₀/2) · e^{βt/2}
```

**General solution:**
```
    Δφ(t) = 2 · arcsin(sin(Δφ₀/2) · e^{βt/2})
```

Valid for t ∈ [0, t_max) with:
```
    t_max = (2/β) · ln(1 / sin(Δφ₀/2))
```

### 5.3 Representation via Coupling Efficiency

Since ε = cos²(Δφ/2) = 1 − sin²(Δφ/2):
```
    ε(t) = 1 − sin²(Δφ₀/2) · e^{βt}
```

**Hubble parameter as a function of time:**
```
    H(t) = H₀ · √(1 − sin²(Δφ₀/2) · e^{βt})
```

| Time range | Behaviour |
|------------|-----------|
| t = 0 | H(0) = H₀ · cos(Δφ₀/2) = H₀√ε₀ (initial condition AP1) |
| t ≪ t_max | H(t) ≈ H₀√ε₀ · (1 − sin²(Δφ₀/2)(e^{βt}−1)/(2ε₀)) (slow decrease) |
| t → t_max | H(t) → 0 (end of expansion phase) |

### 5.4 Comparison with Friedmann Solutions

| Model | H(t) | Characteristic |
|-------|------|----------------|
| Matter domination (ΛCDM) | H₀(1+z)^{3/2} | Power-law decay |
| Radiation domination | H₀(1+z)² | Power-law decay |
| de Sitter (Λ > 0) | H₀ = const | Exponential |
| **RFT AP2** | H₀√(1 − sin²(Δφ₀/2)e^{βt}) | Decrease with saturation character |

The RFT solution is structurally between power law and de Sitter: for small β·t it
behaves approximately like a power law; for large times it approaches a final state
H → 0.

---

## 6. Consistency with A8 — Phase Dynamics and the Speed of Light

### 6.1 A8 and the Cosmological Phase Dynamics

Axiom A8 (RT-41) fixes the coupling wave speed:
```
    c = 1/√(μ₀ε₀)
```

Changes of the phase difference Δφ(x⃗, t) propagate at the speed of light c. In
the homogeneous limit (AP1), Δφ(t) is a global degree of freedom — no spatial
propagation, but a collective mode.

**Consequence:** A8 does not directly constrain Δφ̇, because Δφ(t) does not
represent spatial propagation.

### 6.2 Indirect Bound: Cosmological Timescale

The characteristic timescale of the ODE Δφ̇ = β tan(Δφ/2) is β⁻¹. For the phase
dynamics to be compatible with realistic cosmological expansion:
```
    β ~ H₀  →  β⁻¹ ~ H₀⁻¹  (Hubble time ≈ 14 Gyr)
```

For β ≫ H₀ the phase dynamics would be much faster than the Hubble expansion —
inconsistent with observations. For β ≪ H₀ the expansion would not occur.

A8 consistency is therefore ensured by the **scale compatibility** β ~ H₀.

### 6.3 Phase Gradient and Hubble Radius

For inhomogeneous perturbations δΔφ(x⃗, t) around the homogeneous background Δφ(t),
the dispersion relation (from A8) reads:
```
    ω²  =  c² · k²    (wave equation for δΔφ)
```

A cosmological phase fluctuation on the Hubble radius R_H = c/H₀ has:
```
    ω_H = c · k_H = c · H₀/c = H₀
```

This shows: the cosmological phase dynamics (timescale β⁻¹ ~ H₀⁻¹) is exactly
causally consistent at the Hubble horizon — Axiom A8 is not violated.

---

## 7. Verification of the Success Criterion

**Success criterion:** Closed differential equation for Δφ(t), comparable to
Friedmann solutions.

**Assessment:**

✅ **Closed ODE derived.** The differential equation
```
    Δφ̇ = β · tan(Δφ/2)
```
is an autonomous first-order ODE that follows entirely from the RFT coupling dynamics
(A4, A5, AP1 homogenisation). It possesses an analytical solution and is therefore
comparable to Friedmann solutions.

✅ **Equivalent form via coupling efficiency:**
```
    ε̇ = −β(1 − ε)
```
with solution ε(t) = 1 − (1 − ε₀)e^{βt} — direct Friedmann analogy.

✅ **Hubble parameter explicit:**
```
    H(t) = H₀ √(1 − sin²(Δφ₀/2) · e^{βt})
```

✅ **Modified Raychaudhuri equation:**
```
    Ḣ = −(β/2)(H₀² − H²)/H
```

⚠️ **Direct identification Δφ̇ = H not possible:** Δφ̇ and H are different functions
of Δφ. The physical connection runs via ε̇ (Section 4.2).

✅ **A8 consistency:** For β ~ H₀ the phase dynamics is causally consistent with the
Hubble horizon. No violation of Axiom A8.

✅ **Success criterion satisfied** (with documented restriction on direct identification).

---

## 8. Result and Outlook on AP3–AP7

**Central result of AP2:**

The time derivative Δφ̇(t) of the cosmological phase follows from the RFT coupling
dynamics as a closed ODE:
```
    Δφ̇ = β · tan(Δφ/2)
```

The complete solution reads:
```
    sin(Δφ(t)/2) = sin(Δφ₀/2) · e^{βt/2}
    ε(t) = 1 − sin²(Δφ₀/2) · e^{βt}
    H(t) = H₀ · √(1 − sin²(Δφ₀/2) · e^{βt})
```

The phase dynamics is comparable to Friedmann solutions: it describes a universe
transitioning from maximum coupling (Δφ = 0, H = H₀) to complete loss of coupling
(Δφ → π, H → 0), driven by the dissipation parameter β ~ H₀.

**Outlook:**

- **AP3:** Check whether a phase gradient ∇Δφ generates an effective Λ-term —
  AP2 shows w ∈ [−1/3, +1/3] from RT-33; whether w = −1 is reachable remains open
- **AP4:** Cosmological classification of the 28-orders-of-magnitude discrepancy:
  β ∼ H₀ ∼ 10⁻¹⁸ Hz as the natural scale; the warp regime β ∼ f_resonator is incompatible
- **AP5:** From ε(t) = 1 − sin²(Δφ₀/2)e^{βt} one obtains H(z) — comparable to
  Planck/SH0ES, since β and Δφ₀ are free parameters of RFT cosmology
- **AP6:** ε̇ = −β(1−ε) as the equation of motion for the phase effect: cosmic
  expansion is fully described by loss of coupling
- **AP7:** Consistency check with RT-33 (w(Δφ)), RT-40 (Lorentz structure) and
  RT-41 (A8, causality)

**Connection to existing results:**
- RT-42 AP1: H = H₀ cos(Δφ/2) — AP2 provides the equation of motion for this quantity
- RT-40 AP2: ε = 1/γ² — coupling efficiency carries energy information; here: ε carries cosmological density
- RT-33: w(Δφ) = (1/3)[2ε − 1]; from ε̇ = −β(1−ε) it follows ẇ = −(2β/3)ε (dynamic equation of state)
- RT-41 (A8): β ~ H₀ ensures causal consistency at the Hubble horizon

---

*RT-42 AP2 — DominicReneSchu/RFT — September 2026*
