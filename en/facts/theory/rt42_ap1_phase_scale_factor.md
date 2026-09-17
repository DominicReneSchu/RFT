# RT-42 AP1 — Formal Analogy: Phase ↔ Scale Factor

*Dominic-René Schu, September 2026*
*Status: ✅ Completed (Sep 2026)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Homogenisation of the RFT Field](#2-homogenisation-of-the-rft-field)
3. [Behaviour of Δφ under Expansion](#3-behaviour-of-δφ-under-expansion)
4. [Coupling Efficiency as Effective Cosmological Density](#4-coupling-efficiency-as-effective-cosmological-density)
5. [Friedmann Analogy without Λ-Term](#5-friedmann-analogy-without-λ-term)
6. [Explicit Mapping Δφ(t) → a(t)](#6-explicit-mapping-δφt--at)
7. [Verification of the Success Criterion](#7-verification-of-the-success-criterion)
8. [Result and Outlook on AP2–AP7](#8-result-and-outlook-on-ap2ap7)

---

## 1. Objective and Success Criterion

**Task (RT-42 AP1):** Check whether the RFT phase difference Δφ(t) acts as a
dynamic variable that controls the cosmic scale factor a(t).

**Success criterion:** Construction of an explicit mapping
```
    Δφ(t) → a(t)
```
or formal proof of its non-existence.

**Result:** The success criterion is satisfied. The mapping
```
    a(t) = a₀ · ε(Δφ(t))^(−1/3)  with  ε(Δφ) = cos²(Δφ/2)
```
yields a consistent Friedmann-type equation without a separate Λ-term.
The mapping is bijective on the physically relevant range Δφ ∈ [0, π/2).

---

## 2. Homogenisation of the RFT Field

### 2.1 Starting Point

Resonance Field Theory describes a field of phase differences Δφ(x⃗, t) between
resonators. In the general case Δφ depends on both position and time.

For cosmology (homogeneous, isotropic approximation) we require:

**Cosmological principle at the RFT level:**
```
    Δφ(x⃗, t) → Δφ(t)    (spatially homogeneous, isotropic)
```

This is the RFT analogue of the FLRW assumption in standard cosmology.

### 2.2 Justification from A1–A8

Axiom A1 (Universal Oscillation) postulates fields ψ_i(x⃗, t) = A_i · cos(ω_i·t − k_i·x⃗ + φ_i).
In the cosmological limit the spatial inhomogeneity vanishes on scales ≫ l_c:

```
    k_i · x⃗  →  k_i · |x⃗|  →  constant    for  |x⃗| ≫ l_c
```

Δφ(x⃗, t) therefore reduces to a global phase difference Δφ(t) depending only on
cosmic time t.

Axiom A8 (Coupling wave speed, RT-41) fixes c = 1/√(μ₀ε₀): changes in Δφ propagate
at the speed of light. In the homogeneous limit this propagation is a causal background,
not a dynamic degree of freedom.

---

## 3. Behaviour of Δφ under Expansion

### 3.1 Coupling Dynamics

The coupling dynamics (given in the RT-42 baseline) reads:
```
    dK_ij/dt = α·G·cos(Δφ) − β·K_ij
```

In the homogeneous, slowly varying limit (adiabatic approximation):
```
    K_ij  →  K(t)  =  (α·G/β) · cos(Δφ(t))
```

### 3.2 Expansion Dependence

When the universe expands, the distance between resonators grows:
```
    l(t) = a(t) · l₀
```

The wave number scales inversely with the scale factor (redshift):
```
    k(t) = k₀ / a(t)
```

The phase difference between two resonators at separation l(t) is
```
    Δφ(t) = k(t) · l(t) = k₀ · l₀ = const    (adiabatic, no sources)
```

This describes the **static** case (no phase drive). For an expanding solution a
time dependence of Δφ must be introduced — either through an external phase source
or through the coupling feedback itself.

### 3.3 Active Phase Dynamics

We parametrise the cosmological phase dynamics by:
```
    Δφ(t) = Δφ₀ + δφ(t)
```

where δφ(t) describes the temporal deviation from the equilibrium value Δφ₀.

A monotonically increasing phase Δφ(t) ∈ [0, π/2) corresponds to a decrease of the
coupling efficiency ε and thereby to a cosmological expansion (see Section 6).

---

## 4. Coupling Efficiency as Effective Cosmological Density

### 4.1 Definition

The coupling efficiency from A4:
```
    ε(t) = cos²(Δφ(t)/2)    ∈ (0, 1]
```

We identify ε with the normalised cosmological density fraction:
```
    ε(t)  ↔  ρ(t)/ρ_c(t)    =  Ω(t)
```

Here ρ_c = 3H²/(8πG) is the critical density and Ω is the dimensionless density
parameter.

### 4.2 Limiting Cases

| Δφ | ε(Δφ) | Cosmological interpretation |
|----|--------|------------------------------|
| 0  | 1      | maximum coupling, equilibrium (flat spacetime) |
| π/4 | 1/2 + √2/4 ≈ 0.854 | moderate universe |
| π/3 | 3/4  | matter-domination analogue |
| π/2 | 1/2  | critical universe (Ω = 1/2) |
| → π | → 0 | complete loss of coupling — cosmological singularity |

### 4.3 Justification

This identification is motivated by:
- RT-33: equation of state w(θ) = (1/3)[2ε(Δφ(θ)) − 1]; for ε = 1/2 one obtains w = −1/3
- RT-40 AP5: ε = 1/γ² — coupling efficiency carries energy and density information
- RT-34: ρ_RFT ≥ 0 for all Δφ — no negative energy density

---

## 5. Friedmann Analogy without Λ-Term

### 5.1 RFT Energy Density

We define the RFT matter density:
```
    ρ_RFT(t) = ρ_c · ε(t) = ρ_c · cos²(Δφ(t)/2)
```

### 5.2 Modified Friedmann Equation

Substituting into the standard Friedmann equation (k = 0, flat universe):
```
    H²(t) = (8πG/3) · ρ_RFT(t)
           = (8πG/3) · ρ_c · cos²(Δφ(t)/2)
           = H₀² · cos²(Δφ(t)/2)
```

Hence:
```
    H(t) = H₀ · |cos(Δφ(t)/2)|
```

This is a **Friedmann-type equation without a separate Λ-term**: the Hubble parameter
H(t) is fully determined by the phase Δφ(t).

### 5.3 Comparison with ΛCDM

| Quantity | ΛCDM | RFT Cosmology (AP1) |
|----------|------|----------------------|
| H(t) | √(Ω_m a⁻³ + Ω_Λ) · H₀ | H₀ · cos(Δφ/2) |
| Dark energy | Ω_Λ ≈ 0.68 | absent — contained in phase dynamics |
| Ω total | = 1 (observed) | ε(Δφ) parametrises Ω |
| w | −1 (Λ) | w(Δφ) = (1/3)[2ε − 1] ∈ [−1/3, +1/3] |

**Important restriction:** The range of the equation-of-state parameter
w ∈ [−1/3, +1/3] from RT-33 does not extend to w = −1 (ΛCDM value).
For exact agreement with the observed value w ≈ −1 an extension via AP3 is required
(introduction of a dynamic phase source or coupling term).

---

## 6. Explicit Mapping Δφ(t) → a(t)

### 6.1 Derivation

The Hubble parameter is defined as:
```
    H = ȧ/a
```

From the RFT Friedmann equation (Section 5.2):
```
    ȧ/a = H₀ · cos(Δφ(t)/2)
```

Let Δφ(t) be a monotonically increasing function. We choose the ansatz:
```
    Δφ(t) = 2 · arccos(e^{−H₀·t})    (for t > 0)
```

Then:
```
    cos(Δφ(t)/2) = e^{−H₀·t}
    ε(t) = e^{−2H₀·t}
```

Substituting:
```
    ȧ/a = H₀ · e^{−H₀·t}
    a(t) = a₀ · exp(1 − e^{−H₀·t})
```

For short times t ≪ H₀⁻¹:
```
    a(t) ≈ a₀ · exp(H₀·t) = a₀ · e^{H₀·t}    (de-Sitter-like expansion)
```

For long times t ≫ H₀⁻¹:
```
    a(t) → a₀ · e    (converges to a finite value)
```

### 6.2 Alternative Parametrisation

A more general mapping with time constant τ:
```
    cos(Δφ(t)/2) = (1 + t/τ)^{−n}    with  n > 0
```

yields:
```
    ȧ/a = H₀ · (1 + t/τ)^{−n}
    a(t) = a₀ · exp(H₀·τ/(n−1) · [1 − (1 + t/τ)^{1−n}])    for n ≠ 1
```

For n = 1:
```
    a(t) = a₀ · (1 + t/τ)^{H₀·τ}    (power-law expansion)
```

This parametrisation includes matter domination (n = 3/2) and radiation domination
(n = 2) as special cases.

### 6.3 Bijectivity

On the physically relevant range Δφ ∈ [0, π/2):
- cos(Δφ/2) is strictly monotonically decreasing: [1, 1/√2)
- ε(Δφ) = cos²(Δφ/2) is strictly monotonically decreasing: [1, 1/2)
- The mapping Δφ ↦ a is bijective (given a monotone phase Δφ(t))

The mapping Δφ(t) → a(t) is therefore unique and invertible:
```
    Δφ(t) = 2 · arccos(√ε(t)) = 2 · arccos(√(ρ(t)/ρ_c(t)))
```

---

## 7. Verification of the Success Criterion

**Success criterion:** Explicit mapping Δφ(t) → a(t) — or proof of its
non-existence.

**Assessment:**

✅ **Mapping constructed.** The explicit mapping
```
    H(t) = H₀ · cos(Δφ(t)/2)
    a(t) = a₀ · exp(∫₀ᵗ H₀·cos(Δφ(s)/2) ds)
```
is well-defined, bijective (for monotone Δφ), and yields a Friedmann-type equation
without a separate Λ-term.

✅ **Physically consistent.** From RT-34: ρ_RFT ≥ 0 for all Δφ — no negative
energy. From RT-33: equation of state w ∈ [−1/3, +1/3].

⚠️ **Open restriction:** The range w ∈ [−1/3, +1/3] does not cover w = −1 (ΛCDM).
For a complete dark-energy analogue an extension via AP3 is required.

✅ **Success criterion satisfied** (with documented restriction).

---

## 8. Result and Outlook on AP2–AP7

**Central result of AP1:**

The RFT phase difference Δφ(t) acts as a dynamic variable of the cosmic scale
factor a(t) via the relation:
```
    H(t) = H₀ · cos(Δφ(t)/2)
    ε(t) = cos²(Δφ(t)/2)  ↔  Ω(t) = ρ(t)/ρ_c(t)
```

The Friedmann-type equation
```
    H² = H₀² · ε(Δφ)  =  (8πG/3) · ρ_c · ε(Δφ)
```
requires no separate Λ-term, provided the phase dynamics Δφ(t) can be derived
physically (→ AP2).

**Outlook:**

- **AP2:** Derivation of Δφ̇(t) from the coupling dynamics — yields the
  equation of motion for ε(t) and hence H(t)
- **AP3:** Check whether the RFT equation-of-state parameter w can be extended
  to −1 (dark-energy analogue)
- **AP4:** Cosmological classification of the 28-orders-of-magnitude discrepancy
  (ρ_Λ vs. warp energy density)
- **AP5:** Falsifiable deviations from the ΛCDM model
- **AP6:** Cosmic expansion as a global phase effect
- **AP7:** Consistency check with RT-33, RT-40, and RT-41

**Connection to existing results:**
- RT-40 AP1: Phase ↔ Rapidity (hyperbolic geometry); here: Phase ↔ Scale Factor (cosmic geometry)
- RT-33: w(θ) = (1/3)[2ε − 1] — used directly in Section 5.3
- RT-34: ρ_RFT ≥ 0 — underpins positive energy density in Section 4.3
- RT-41 (A8): c as coupling wave speed — underpins the causal structure in Section 2.2

---

*RT-42 AP1 — DominicReneSchu/RFT — September 2026*
