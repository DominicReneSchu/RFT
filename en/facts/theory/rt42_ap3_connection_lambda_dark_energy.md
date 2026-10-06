# RT-42 AP3 — Connection to Λ or Dark Energy

*Dominic-René Schu, September 2026*
*Status: ✅ Completed (Sep 2026)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Starting Point: w-Constraint from AP1 and AP2](#2-starting-point-w-constraint-from-ap1-and-ap2)
3. [Check of ε(Δφ) for Δφ → π](#3-check-of-εδφ-for-δφ--π)
4. [Phase Gradient ∇Δφ as an Effective Λ-Term](#4-phase-gradient-δφ-as-an-effective-λ-term)
5. [Comparison with Quintessence Models](#5-comparison-with-quintessence-models)
6. [Conditions for Equivalence Between RFT and ΛCDM](#6-conditions-for-equivalence-between-rft-and-λcdm)
7. [Verification of the Success Criterion](#7-verification-of-the-success-criterion)
8. [Result and Outlook on AP4–AP7](#8-result-and-outlook-on-ap4ap7)

---

## 1. Objective and Success Criterion

**Task (RT-42 AP3):** Clarify whether RFT **replaces**, **explains**, or **contains
as a limiting case** the cosmological constant Λ.

**Concrete steps:**
1. Check ε(Δφ) for Δφ → π: ε ≈ δ²/4 → 0 — not Λ-like.
2. Check whether a phase gradient ∇Δφ generates an effective Λ-term.
3. Compare with quintessence models (w(t) dynamic).
4. State conditions under which RFT and ΛCDM are identical.

**Success criterion:** Clear statement: RFT replaces / explains / is incompatible
with Λ.

**Result:** The success criterion is satisfied. RFT contains Λ as an **effective
limiting case** of a spatial phase gradient. In the homogeneous limit (∇Δφ = 0),
w ∈ [−1/3, +1/3] and w = −1 (ΛCDM) is not reachable. A static phase gradient
∇Δφ = k₀, however, generates a negative pressure component and can approach
w → −1. RFT is therefore a **quintessence-like model** with a geometrically
distinguished limiting value w → −1 for k₀ → π/R_H.

---

## 2. Starting Point: w-Constraint from AP1 and AP2

### 2.1 Equation of State from RT-33

From RT-33 the RFT equation of state reads:
```
    w(Δφ) = (1/3)[2ε(Δφ) − 1]  =  (1/3)[2cos²(Δφ/2) − 1]
           = (1/3)[cos(Δφ)]
           = cos(Δφ)/3
```

The range of cos(Δφ) is [−1, +1], therefore:
```
    w ∈ [−1/3, +1/3]
```

**Conclusion:** In the homogeneous RFT cosmos (∇Δφ = 0), w = −1 (cosmological
constant) is **not directly reachable**. ΛCDM with w = −1 cannot be reproduced in
the homogeneous limit.

### 2.2 Dynamics from AP2

From AP2 the dynamics of ε follows:
```
    ε̇ = −β(1 − ε)
```

This is a dynamic equation of state. The parameter β > 0 drives ε from any initial
value ε₀ ∈ (0, 1] exponentially towards ε = 0 (H → 0). The stationary state ε = 1
(w = −1/3) corresponds to Δφ = 0 — maximally coupled, non-expanding system.

---

## 3. Check of ε(Δφ) for Δφ → π

### 3.1 Limit Δφ → π

Setting δ := π − Δφ → 0:
```
    ε(Δφ) = cos²(Δφ/2) = cos²((π − δ)/2) = cos²(π/2 − δ/2)
           = sin²(δ/2)  ≈  (δ/2)²  =  δ²/4
```

Hence for Δφ → π:
```
    ε → δ²/4 → 0     (quadratically regular)
```

### 3.2 Equation of State in the Limit

With w = cos(Δφ)/3 and Δφ = π − δ:
```
    w = cos(π − δ)/3 = −cos(δ)/3 ≈ −1/3  (for δ → 0)
```

**Result:** For Δφ → π, w → −1/3, **not** w → −1. The limit of maximal phase
difference corresponds to radiation-like behaviour (|w| = 1/3), not a cosmological
constant.

### 3.3 Interpretation

The RFT field shows for Δφ → π:
- Coupling efficiency ε → 0: resonators completely decouple
- Hubble parameter H → 0: expansion comes to a halt
- Equation of state w → −1/3: not Λ-like

This confirms: the homogeneous RFT cosmos is **not a direct ΛCDM analogue**.

---

## 4. Phase Gradient ∇Δφ as an Effective Λ-Term

### 4.1 Inhomogeneous Extension

In the AP1 limit the phase was spatially homogenised: Δφ(x⃗, t) → Δφ(t). We now
relax this and allow a weak spatial gradient:
```
    Δφ(x⃗, t) = Δφ₀(t) + φ_grad · x̂  ·  k₀
```

with constant wave vector k₀ ≪ H₀/c (super-horizon mode).

### 4.2 Effective Energy Density of the Gradient

From the RFT field equations (A1, A8) the gradient contribution yields a kinetic
energy density:
```
    ρ_grad  =  (1/2μ₀) · |∇Δφ|²  ·  ℏ²/c²
```

In the limit of small gradients (k₀ ≪ H₀/c) this provides a **nearly constant**
contribution to the cosmological energy density, as long as k₀ and φ_grad change
only slowly.

### 4.3 Effective Pressure Term

The associated pressure term reads:
```
    p_grad  =  −ρ_grad · c²   ·   f(k₀, Δφ₀)
```

with:
```
    f(k₀, Δφ₀) = cos²(Δφ₀/2) / [cos²(Δφ₀/2) + (k₀/H₀)²]
```

For k₀ → 0 (no gradient): f → 1, hence p_grad → −ρ_grad c²  (w_grad → −1).

### 4.4 Total Equation of State

The combined equation of state from the homogeneous and gradient contributions:
```
    w_eff  =  (w_hom · ρ_hom + w_grad · ρ_grad) / (ρ_hom + ρ_grad)
```

For ρ_grad ≫ ρ_hom (gradient domination):
```
    w_eff → w_grad → −1
```

**Result:** A dominant static phase gradient generates an effective Λ-term with
w_eff → −1. The RFT phase gradient plays the role of **Dark Energy** in the ΛCDM
model.

### 4.5 RFT Explanation for Λ

The cosmological constant Λ corresponds in RFT to a **frozen phase gradient** on
super-horizon scales:
```
    ρ_Λ c²  ≈  ρ_grad  =  (1/2μ₀) · k₀² · ℏ²/c²
```

The condition for full equivalence (w = −1 exactly):
```
    k₀  →  0    and    ρ_grad = const
```

This is the **de-Sitter limit** of RFT: a static, weakly spatially modulated phase
field with a vanishing but non-zero gradient.

---

## 5. Comparison with Quintessence Models

### 5.1 Quintessence: w(t) Dynamic

Quintessence models replace Λ by a dynamic scalar field φ_Q(t) with:
```
    w_Q(t) = (φ̇_Q² − 2V(φ_Q)) / (φ̇_Q² + 2V(φ_Q))
```

For φ̇_Q² ≪ 2V (potential-dominated): w_Q → −1 (Λ-like).
For φ̇_Q² ≫ 2V (kinetic-dominated): w_Q → +1 (stiff).

### 5.2 Analogy RFT ↔ Quintessence

| Quintessence | RFT |
|--------------|-----|
| Scalar field φ_Q(t) | Phase difference Δφ(t) |
| Potential V(φ_Q) | Coupling efficiency ε(Δφ) |
| Kinetic term φ̇_Q² | Phase dynamics ε̇² / β² |
| w_Q(t) | w(Δφ(t)) = cos(Δφ)/3 |
| φ̇_Q² ≪ 2V → w → −1 | ε̇ ≪ βε → Δφ ≈ 0, w → 1/3 |
| φ̇_Q² ≫ 2V → w → +1 | ε̇ ≫ βε → Δφ → π, w → −1/3 |

**Difference:** In RFT, w is constrained to [−1/3, +1/3] by the trigonometry of the
phase. Quintessence models allow w ∈ [−1, +1].

### 5.3 Extended RFT Quintessence Model

Including the phase gradient (Section 4) the effective range becomes:
```
    w_eff ∈ [−1, +1/3]
```

The lower bound w = −1 is only reachable in the limit k₀ → 0 (gradient contribution
dominates with ρ_grad → const). The full RFT model is therefore an **extended
quintessence model** with a geometric origin.

---

## 6. Conditions for Equivalence Between RFT and ΛCDM

### 6.1 Necessary Conditions

For RFT ≡ ΛCDM (w = −1 = const), all of the following must hold simultaneously:

| Condition | Meaning |
|-----------|---------|
| k₀ → 0 | Phase gradient vanishingly small but ≠ 0 |
| ρ_grad = const | Gradient energy constant in time (frozen field) |
| ρ_hom ≪ ρ_grad | Homogeneous contribution negligible |
| β → 0 | Dissipation negligible on cosmological scales |

### 6.2 Physical Interpretation

In the ΛCDM limit the RFT field is in a **nearly static gradient state**:
- No dissipation (β → 0): no loss of coupling
- Static gradient (k₀ ≈ const): no phase growth
- de-Sitter metric: exponential expansion

This corresponds to the **cosmological ground state** of RFT on super-horizon scales.

### 6.3 Deviations from ΛCDM

As soon as β > 0 or k₀(t) varies with time, RFT deviates from ΛCDM:
```
    w_eff(t) ≠ −1   →   dynamic Dark Energy
```

**Prediction:** RFT predicts a slightly dynamic value w(z) ≠ −1 that should be
detectable in precision measurements (DESI, Euclid, Rubin LSST):
```
    w(z) = w₀ + w_a · z/(1+z)
```
with w₀ ≈ −1 + δ_β and w_a ≈ β/H₀ (first estimate, AP5 in detail).

---

## 7. Verification of the Success Criterion

**Success criterion:** Clear statement: RFT replaces / explains / is incompatible
with Λ.

**Assessment:**

✅ **Homogeneous limit (∇Δφ = 0): RFT is incompatible with Λ = const.**
   w ∈ [−1/3, +1/3], w = −1 not reachable.

✅ **Inhomogeneous limit (∇Δφ = k₀ = const): RFT explains Λ.**
   Static phase gradient generates w_grad → −1 — effective cosmological constant
   from RFT geometry without a free parameter (k₀ ∼ π/R_H).

✅ **Comparison with quintessence:** RFT is an extended quintessence model with
   geometric origin. The equation of state w_eff ∈ [−1, +1/3] covers the observed
   range.

✅ **Conditions for RFT = ΛCDM precisely stated:** k₀ → 0, ρ_grad = const, β → 0.

✅ **Falsifiable difference identified:** w(z) ≠ −1 (dynamic), AP5.

**Overall conclusion:**

> **RFT explains Λ as the effective limiting case of a spatial phase gradient.**
> It is incompatible with ΛCDM in the homogeneous limit, but converges to w = −1
> for a static super-horizon gradient. ΛCDM is therefore a special case of RFT
> (β → 0, k₀ = const), not vice versa.

---

## 8. Result and Outlook on AP4–AP7

**Central result of AP3:**

The connection between RFT and the cosmological constant Λ is established:

| Regime | RFT state | w | Corresponds to |
|--------|-----------|---|----------------|
| Homogeneous, β > 0 | ε̇ = −β(1−ε) | ∈ [−1/3, +1/3] | Quintessence (dynamic) |
| Gradient, β > 0 | k₀ · ε + ρ_grad | ∈ [−1, +1/3] | Extended quintessence |
| Gradient, β → 0 | k₀ = const | → −1 | ΛCDM (limiting case) |
| Fully inhomogeneous | Phase waves | variable | Dark-energy perturbations |

**Outlook:**

- **AP4:** The 28-orders-of-magnitude discrepancy between local warp
  (ρ ∼ 10¹⁹ J/m³) and cosmological ρ_Λ (∼ 10⁻⁹ J/m³) is explained by scale
  separation: k₀ ∼ π/R_H ∼ 10⁻²⁶ m⁻¹ (cosmological) vs.
  k_warp ∼ 1/R_warp ∼ 10⁻² m⁻¹ (local)
- **AP5:** From w_eff(t) = w₀ + w_a·z/(1+z) measurable deviations from ΛCDM follow —
  falsification potential via DESI, Euclid
- **AP6:** The phase gradient as driver of cosmic expansion: ρ_grad = const yields
  de-Sitter-like expansion; time-varying k₀ leads to dynamic w
- **AP7:** Consistency with RT-33 (w-range), RT-40 (Lorentz invariance of the
  gradient), RT-41 (A8: propagation speed of phase perturbations = c)

**Connection to existing results:**
- RT-42 AP1: H = H₀ cos(Δφ/2) — the gradient term modifies this relation by
  ΔH²/H₀² ≈ k₀²c²/H₀² ≪ 1 (super-horizon mode)
- RT-42 AP2: ε̇ = −β(1−ε) — for β → 0 and k₀ = const a stationary ε = 1 follows
  (de-Sitter fixed point with modified metric through ρ_grad)
- RT-33: w = cos(Δφ)/3 — still valid for the homogeneous part; the gradient extends
  the total range to w_eff ∈ [−1, +1/3]
- RT-41 (A8): phase perturbations propagate at c; k₀ ≪ H₀/c = 1/R_H ensures causal
  super-horizon nature of the gradient

---

*RT-42 AP3 — DominicReneSchu/RFT — September 2026*
