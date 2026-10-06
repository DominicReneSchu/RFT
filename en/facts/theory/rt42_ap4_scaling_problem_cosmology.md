# RT-42 AP4 — Scaling Problem: Cosmological Classification

*Dominic-René Schu, September 2026*
*Status: ✅ Completed (Sep 2026)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Starting Point: Warp Energy Density and Cosmological Constant](#2-starting-point-warp-energy-density-and-cosmological-constant)
3. [Calculation of ρ_Λ](#3-calculation-of-ρ_λ)
4. [Physical Classification: Warp ≠ Cosmological Background Metric](#4-physical-classification-warp--cosmological-background-metric)
5. [Scaling Analysis: ρ_warp/ρ_Λ ∝ (R_H/R)^n](#5-scaling-analysis-ρ_warpρ_λ--r_hrn)
6. [Classification as an Apparent Problem](#6-classification-as-an-apparent-problem)
7. [Verification of the Success Criterion](#7-verification-of-the-success-criterion)
8. [Result and Outlook on AP5–AP7](#8-result-and-outlook-on-ap5ap7)

---

## 1. Objective and Success Criterion

**Task (RT-42 AP4):** Resolve the 28-orders-of-magnitude discrepancy between the
warp energy density (10¹⁹ J/m³) and ρ_Λ (10⁻⁹ J/m³), or expose it as an
apparent problem.

**Concrete steps:**
1. Compute ρ_Λ c² ≈ 10⁻⁹ J/m³.
2. Interpret: warp = local metric perturbation ≠ cosmological background metric.
3. Check scaling factor ρ_warp/ρ_Λ ∝ (R_H/R)^n — what is n?

**Success criterion:** Discrepancy resolved (scaling factor) or identified as an
apparent problem (different regimes).

**Result:** The success criterion is satisfied. The 28-orders-of-magnitude
discrepancy is an **apparent problem**: it does not reflect a fundamental
inconsistency of RFT, but rather the physically distinct regimes of the local metric
perturbation (warp, k_warp ~ 10⁻² m⁻¹) and the global cosmological background
energy (Λ, k₀ ~ 10⁻²⁶ m⁻¹). The formal k-scaling factor (k_warp/k₀)² ~ 10⁴⁸
exceeds the observed 28 orders by a further 20 — demonstrating that both energy
densities belong not only to quantitatively but to qualitatively different regimes
and are not directly comparable.

---

## 2. Starting Point: Warp Energy Density and Cosmological Constant

### 2.1 Warp Energy Density from RT-33/RT-34

From RT-33 (warp scaling) and RT-34 (3D warp bubble), for a warp bubble with
radius R_warp = 50 m:
```
    ρ_warp  ≈  10¹⁹ J/m³
```

This value follows from the RFT-modified Alcubierre metric:
```
    h_μν^RFT  =  h_μν^Alcubierre · ε(Δφ)
```

with ε(Δφ) = cos²(Δφ/2) from A4/A5. The energy density is positive (ρ_RFT ≥ 0)
since ε ≥ 0 everywhere — no exotic matter required (RT-33 result).

For smaller warp bubbles the energy density increases as the bubble size decreases:
```
    ρ_warp(R)  ∝  R⁻²    (formal scaling from curvature term)
```

This is the characteristic R⁻² scaling of local metric perturbations in general
relativity (curvature ∝ 1/R² at fixed warp parameter).

### 2.2 Cosmological Energy Density ρ_Λ

The energy density of the cosmological constant Λ is determined from Planck 2018
data:
```
    Λ  ≈  1.11 × 10⁻⁵² m⁻²   (Planck 2018)
```

The associated energy density reads:
```
    ρ_Λ  =  Λ c² / (8πG)
```

**Known tension:**
```
    ρ_warp / ρ_Λ  ≈  10¹⁹ / 10⁻⁹  =  10²⁸
```

These 28 orders of magnitude constitute the scaling problem to be investigated.

---

## 3. Calculation of ρ_Λ

### 3.1 Numerical Evaluation

Using the fundamental constants:
```
    c  =  2.998 × 10⁸  m/s
    G  =  6.674 × 10⁻¹¹  m³ kg⁻¹ s⁻²
    Λ  =  1.11 × 10⁻⁵²  m⁻²
```

one obtains:
```
    ρ_Λ  =  Λ c² / (8πG)
           =  (1.11 × 10⁻⁵²) × (8.99 × 10¹⁶) / (1.676 × 10⁻⁹)
           =  (9.98 × 10⁻³⁶) / (1.676 × 10⁻⁹)
           ≈  5.96 × 10⁻²⁷  kg/m³
```

As an energy density:
```
    ρ_Λ c²  =  5.96 × 10⁻²⁷  kg/m³  ×  (2.998 × 10⁸ m/s)²
            ≈  5.36 × 10⁻¹⁰  J/m³
            ≈  10⁻⁹  J/m³
```

**Result:** ρ_Λ c² ≈ 5.4 × 10⁻¹⁰ J/m³ ≈ 10⁻⁹ J/m³ ✓

### 3.2 RFT Interpretation from AP3

From RT-42 AP3, the cosmological gradient contribution satisfies:
```
    ρ_Λ c²  ≈  ρ_grad  =  (1/2μ₀) · k₀² · ℏ²/c²
```

The associated super-horizon wave vector:
```
    k₀  ~  π/R_H  ~  π / (1.36 × 10²⁶  m)  ≈  2.3 × 10⁻²⁶  m⁻¹
```

with Hubble radius R_H = c/H₀ ≈ 1.36 × 10²⁶ m (H₀ = 67.4 km/s/Mpc).

This wave vector is the characteristic **cosmological scale** of RFT.

---

## 4. Physical Classification: Warp ≠ Cosmological Background Metric

### 4.1 Two Fundamentally Different Regimes

The warp energy density and the cosmological energy density ρ_Λ belong to
physically distinct regimes of RFT:

| Quantity | Warp Bubble (RT-33/34) | Cosmological Constant (AP3) |
|----------|----------------------|------------------------------|
| Char. scale R | 50 m (local) | R_H ≈ 1.4 × 10²⁶ m (global) |
| Char. k | k_warp ~ 1/R ~ 0.02 m⁻¹ | k₀ ~ π/R_H ~ 2 × 10⁻²⁶ m⁻¹ |
| Physical origin | Local curvature perturbation | Super-horizon phase gradient |
| RFT mechanism | h_μν^RFT · ε(Δφ), ε → 0 for v→c | ρ_grad = (1/2μ₀)k₀²ℏ²/c², k₀ = const |
| Energy formula | Curvature energy (GR) | Gradient energy (RFT) |
| Comparable? | **No** | **No** |

### 4.2 Analogy: Laser vs. Background Radiation

The situation is analogous to the following question in classical physics:

> *Why is the energy density of a laser beam (∼ 10¹² J/m³) many orders of
> magnitude greater than the cosmic microwave background (∼ 4 × 10⁻¹⁴ J/m³)?*

The answer: they are physically different objects — a local, focused phenomenon
versus a global, diffuse background. A direct comparison is meaningless.

Likewise: **warp energy density** (local metric perturbation with
k_warp ~ 10⁻² m⁻¹) and **ρ_Λ** (global phase gradient with
k₀ ~ 10⁻²⁶ m⁻¹) are physically different objects.

### 4.3 Scale Separation in RFT

RFT contains an explicit **scale separation** between local and cosmological
regimes:

```
    k_warp  ~  1/R_warp  ~  0.02  m⁻¹     (local)
    k₀      ~  π/R_H     ~  2 × 10⁻²⁶ m⁻¹   (cosmological)
```

Both scales are physically well-founded:
- k_warp is the wave number of the local metric perturbation (warp bubble radius)
- k₀ is the wave number of the cosmological background gradient (Hubble radius)

The methodological guideline of RT-42 (Section 6) states explicitly:
> **Scale separation:** Warp (local) ≠ Friedmann (cosmological) — do not confuse.

---

## 5. Scaling Analysis: ρ_warp/ρ_Λ ∝ (R_H/R)^n

### 5.1 Formal Scaling for n = 2

In RFT the gradient energy scales as ρ ∝ k²:
```
    ρ_grad  ∝  k²
```

This corresponds to n = 2 in the scaling relation ρ ∝ (R_H/R)^n:
```
    ρ_warp / ρ_Λ  ~  (k_warp / k₀)²
```

Numerical evaluation:
```
    k_warp / k₀  ≈  0.02 / (2 × 10⁻²⁶)  ≈  10²⁴
    
    (k_warp / k₀)²  ≈  10⁴⁸
```

### 5.2 Comparison with the Observed Discrepancy

| Quantity | Value |
|----------|-------|
| Observed discrepancy | ρ_warp/ρ_Λ ≈ 10²⁸ |
| Formal k²-scaling | (k_warp/k₀)² ≈ 10⁴⁸ |
| Excess of formal scaling | ≈ 10²⁰ |

**Key result:** The formal k²-scaling predicts a ratio of 10⁴⁸ — 20 orders of
magnitude **larger** than the observed 10²⁸.

This shows: ρ_warp and ρ_Λ do **not** follow the same physical formula. The warp
energy density arises from the local curvature term (Alcubierre metric with
ε-modulation), not from a k-gradient energy. The cosmological ρ_Λ arises from the
super-horizon phase gradient.

### 5.3 Determination of the Effective Scaling Exponent

From the observed discrepancy one obtains an empirical exponent:
```
    ρ_warp/ρ_Λ  =  (R_H/R_warp)^n
    
    10²⁸  =  (2.7 × 10²⁴)^n
    
    28  =  n × log₁₀(2.7 × 10²⁴)  =  n × 24.4
    
    n  ≈  1.15
```

The empirical exponent n ≈ 1.15 lies **between** n = 1 (linear scaling) and
n = 2 (gradient-energy scaling). It is non-integer and not a universal law — a
further indication that the comparison has no physical foundation.

### 5.4 Range of 28–50 Orders of Magnitude

For smaller warp bubbles (R_warp → R_Planck ∼ 10⁻³⁵ m) the discrepancy would
grow to 50+ orders of magnitude (since ρ_warp ∝ R⁻²). This is not a sharpening
of the problem, but confirms the scale separation:

| R_warp | ρ_warp (approx.) | log₁₀(ρ_warp/ρ_Λ) |
|--------|-----------------|-------------------|
| 50 m (RT-33) | ∼ 10¹⁹ J/m³ | ≈ 28 |
| 1 m | ∼ 10²¹ J/m³ | ≈ 30 |
| 10⁻¹⁰ m (atomic scale) | ∼ 10³⁹ J/m³ | ≈ 48 |

The ratio grows as the bubble size decreases — the scaling problem is not a fixed
value but a property of the chosen local scale R_warp.

---

## 6. Classification as an Apparent Problem

### 6.1 The Argument

The "scaling problem" rests on the implicit comparison:
```
    ρ_warp(R_warp = 50 m)  vs.  ρ_Λ
```

This comparison is **physically unjustified**, because:

1. **Different energy formulas:** ρ_warp comes from the curvature term of the
   modified Alcubierre metric; ρ_Λ comes from the super-horizon phase gradient.

2. **Different physical regimes:**
   - Warp: perturbative regime, local metric perturbation, high k
   - Cosmology: global background, static gradient, tiny k

3. **Different RFT mechanisms:**
   - Warp: ε(Δφ)-modulation of the Alcubierre metric
   - Λ: spatial phase gradient ∇Δφ = k₀ on super-horizon scales

4. **The k-scaling overshoots:** (k_warp/k₀)² ~ 10⁴⁸ ≫ 10²⁸ — pure scaling
   gives more discrepancy than observed. This shows that warp energy is not
   described by gradient energy alone.

### 6.2 Consistency Check: Cosmological Vacuum Contribution

The cosmological energy density ρ_Λ corresponds to a vanishingly small gradient:
```
    k₀  ~  2 × 10⁻²⁶  m⁻¹
```

A warp bubble with a comparable wave number would require a radius of:
```
    R  ~  1/k₀  ~  5 × 10²⁵  m  ~  R_H/π
```

— that is, of the order of the Hubble horizon. Such a "cosmological warp bubble"
would indeed have an energy density comparable to ρ_Λ.

This confirms: the 10²⁸ discrepancy is not an inconsistency, but the
**consequence of the chosen scale** R_warp = 50 m versus R ~ R_H.

### 6.3 The Vacuum Energy Analogue in QFT

The best-known scaling problem in physics is the **cosmological constant problem
of quantum field theory**: comparing the QFT vacuum energy (∼ ρ_Planck ≈ 10¹¹³ J/m³)
with ρ_Λ (∼ 10⁻⁹ J/m³) yields a discrepancy of ∼ 122 orders of magnitude. There
too, the "problem" is a consequence of comparing physically different quantities
(local QFT vacuum fluctuations vs. global spacetime curvature).

The RT-42 scaling problem (28–50 orders of magnitude) is an **analogous situation
within the RFT framework** — and its resolution as an apparent problem follows the
same logic.

---

## 7. Verification of the Success Criterion

**Success criterion:** Discrepancy resolved (scaling factor) or identified as an
apparent problem (different regimes).

**Assessment:**

✅ **Step 1: ρ_Λ c² ≈ 10⁻⁹ J/m³ computed.**
   ρ_Λ c² = Λ c⁴/(8πG) ≈ 5.36 × 10⁻¹⁰ J/m³. ✓

✅ **Step 2: Warp ≠ cosmological background metric.**
   Warp energy density: local curvature perturbation, k_warp ~ 0.02 m⁻¹.
   Cosmological ρ_Λ: global phase gradient, k₀ ~ 2 × 10⁻²⁶ m⁻¹.
   Different formulas, different regimes.

✅ **Step 3: Scaling factor analysed.**
   Formal k²-scaling: (k_warp/k₀)² ~ 10⁴⁸ > 10²⁸ (excess of 10²⁰).
   Empirical exponent n ≈ 1.15 — not universal.

✅ **Success criterion satisfied: discrepancy identified as an apparent problem.**

**Overall conclusion:**

> **The 28-orders-of-magnitude discrepancy between ρ_warp and ρ_Λ is an apparent
> problem.** It arises from the physically unjustified comparison of a local metric
> perturbation term (warp bubble, R = 50 m) with a global background term
> (cosmological phase gradient, R ~ R_H). Within RFT, both energy densities reside
> in different regimes: the warp regime uses the ε(Δφ)-modulation of the Alcubierre
> metric; the cosmological regime uses the static super-horizon gradient ∇Δφ = k₀.
> A consistent RFT contains **both regimes** — without contradiction.

---

## 8. Result and Outlook on AP5–AP7

**Central result of AP4:**

The scaling situation of RFT is fully classified:

| Regime | Char. scale | Char. k | Energy density | RFT mechanism |
|--------|-------------|---------|----------------|---------------|
| Warp bubble (local) | R_warp ~ 50 m | k_warp ~ 10⁻² m⁻¹ | ρ_warp ~ 10¹⁹ J/m³ | h_μν · ε(Δφ) |
| Cosmological | R_H ~ 10²⁶ m | k₀ ~ 10⁻²⁶ m⁻¹ | ρ_Λ ~ 10⁻⁹ J/m³ | ρ_grad = (1/2μ₀)k₀²ℏ²/c² |
| **Ratio** | **(R_H/R_warp) ~ 10²⁴** | **(k_warp/k₀) ~ 10²⁴** | **10²⁸** | **Apparent problem** |

**Outlook:**

- **AP5:** Falsifiable deviations from ΛCDM: w(z) = w₀ + w_a·z/(1+z) with
  w_a ≈ β/H₀ — detectable by DESI, Euclid, Rubin LSST
- **AP6:** Cosmic expansion as a phase effect: ρ_grad = const yields de-Sitter-like
  expansion; time-varying k₀(t) leads to dynamic w(z)
- **AP7:** Consistency with RT-33 (no negative energy), RT-40 (Lorentz invariance),
  RT-41 (A8: phase perturbations propagate at c)

**Connection to existing results:**
- RT-42 AP1: H = H₀ cos(Δφ/2) — holds on cosmological scales (k₀-regime);
  for warp: Δφ determined by local bubble dynamics (k_warp-regime)
- RT-42 AP2: ε̇ = −β(1−ε) — dynamics of the homogeneous cosmological field;
  warp-ε(Δφ) is stationary (no β-decay during warp travel)
- RT-42 AP3: ρ_grad = (1/2μ₀)k₀²ℏ²/c² explains ρ_Λ;
  ρ_warp follows the other regime (curvature term) — no contradiction
- RT-33: ρ_RFT ≥ 0 everywhere (ε ≥ 0) — holds in **both** regimes (local and
  cosmological); no exotic matter required in either regime

---

*RT-42 AP4 — DominicReneSchu/RFT — September 2026*
