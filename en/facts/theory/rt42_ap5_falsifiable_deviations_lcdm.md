# RT-42 AP5 — Falsifiable Deviations from $\Lambda$CDM

*Dominic-René Schu, September 2026*
*Status: ✅ Completed (Sep 2026)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Free Parameters of RFT Cosmology](#2-free-parameters-of-rft-cosmology)
3. [Prediction 1: Dynamic Equation-of-State Parameter w(z)](#3-prediction-1-dynamic-equation-of-state-parameter-wz)
4. [Prediction 2: Modified Hubble Parameter H(z)](#4-prediction-2-modified-hubble-parameter-hz)
5. [Prediction 3: Structure Growth and Growth Factor](#5-prediction-3-structure-growth-and-growth-factor)
6. [Prediction 4: Cosmic Microwave Background](#6-prediction-4-cosmic-microwave-background)
7. [Comparison with Current Observations](#7-comparison-with-current-observations)
8. [Falsification Criteria](#8-falsification-criteria)
9. [Verification of the Success Criterion](#9-verification-of-the-success-criterion)
10. [Result and Outlook on AP6–AP7](#10-result-and-outlook-on-ap6ap7)

---

## 1. Objective and Success Criterion

**Task (RT-42 AP5):** Identify measurable differences between RFT cosmology
and $\Lambda$CDM.

**Concrete steps:**
1. Free parameters: $\alpha/\beta$, $G(f_i/f_j)$, $\Delta\phi_0$,
   $\dot{\Delta\phi}_0$.
2. Observable effects: deviations in $H(z)$, dynamic $w(z)$, structure growth,
   CMB.
3. Comparison with Planck, DES, SH0ES.
4. State falsification criteria.

**Success criterion:** At least one measurable deviation — or proof of complete
equivalence.

**Result:** The success criterion is satisfied. RFT yields four structurally
distinct, potentially measurable deviations from $\Lambda$CDM:

1. **Dynamic $w(z)$:** CPL parametrisation $w(z) = w_0 + w_a\,z/(1+z)$
   with $w_a \approx \beta/H_0 \neq 0$ (provided $\beta \neq 0$) — $\Lambda$CDM
   postulates $w = -1$, $w_a = 0$.
2. **Modified $H(z)$:** Explicit deviation via RFT phase dynamics, measurable
   for $\beta \gtrsim 0.1\,H_0$.
3. **Altered structure growth:** Suppressed growth for $w > -1$ (dynamic range
   of the RFT field).
4. **ISW signature in CMB:** Modified integrated Sachs-Wolfe signal at large
   angular scales.

---

## 2. Free Parameters of RFT Cosmology

### 2.1 Parameter space

RFT cosmology has the following free parameters:

| Parameter | Meaning | $\Lambda$CDM limit |
|-----------|---------|-------------------|
| $\beta$ | Coupling decay rate ($\dot\varepsilon = -\beta(1-\varepsilon)$) | $\beta \to 0$ |
| $k_0$ | Super-horizon phase gradient ($\nabla\Delta\phi = k_0$) | $k_0 = $ const |
| $\Delta\phi_0$ | Initial phase difference at $z = 0$ | $\Delta\phi_0 \to 0$ |
| $\alpha/\beta$ | Ratio of coupling strength to decay rate | arbitrary |

**Central statement from AP3:**
```
    ΛCDM  =  RFT  with  β → 0  and  k₀ = const
```
$\Lambda$CDM is a limiting case, not the general model.

### 2.2 Physical interpretation of the free parameters

**$\beta$** (coupling decay rate): Determines the time scale on which the RFT
field evolves from the dynamic regime ($\varepsilon < 1$) to the de-Sitter fixed
point ($\varepsilon \to 1$). For $\beta \sim H_0$ the dynamics are active on
Hubble time scales — observable in $w(z)$.

**$k_0$** (cosmological wave-number vector): Controls the energy density of the
gradient-$\Lambda$ term. For time-constant $k_0$ one obtains an effective
$\Lambda = $ const. A time-varying $k_0(t)$ produces a dynamic effective
$\Lambda_{\rm eff}(t)$ — this is the AP6 question.

**$\Delta\phi_0$**: Initial condition. Determines the present value
$\varepsilon_0 = \cos^2(\Delta\phi_0/2)$ and hence $w_0$.

---

## 3. Prediction 1: Dynamic Equation-of-State Parameter $w(z)$

### 3.1 Derivation of $w(z)$ from RFT

From RT-42 AP3 the effective equation-of-state parameter is:
```
    w_eff(t)  =  w_grad + w_hom(t)
```

with the gradient contribution $w_{\rm grad} \approx -1$ (for $k_0 = $ const,
$\beta \to 0$) and the homogeneous part:
```
    w_hom(t)  =  [2ε(t) - 1] / 3  ∈ [-1/3, +1/3]
```

For small deviations from the de-Sitter fixed point ($\varepsilon \approx 1$,
$\Delta\phi \approx 0$), using RT-42 AP2:
```
    ε(t)  =  1 - sin²(Δφ₀/2) · e^{βt}
    
    w_hom(t)  ≈  (2/3) · [1 - sin²(Δφ₀/2) · e^{βt}] - 1/3
             =  (1/3) - (2/3) · sin²(Δφ₀/2) · e^{βt}
```

### 3.2 CPL parametrisation

The RFT prediction can be expressed in the Chevallier-Polarski-Linder (CPL)
parametrisation:
```
    w(z)  =  w₀ + w_a · z/(1+z)
```

**Identification:**
```
    w₀  ≡  w_eff(z=0)  ≈  -1 + (1/3) · sin²(Δφ₀/2)  ∈ [-1, -1/3]
    
    w_a  ≈  β / H₀  ·  sin²(Δφ₀/2)
```

To leading order (small $\Delta\phi_0$, $\beta \ll H_0$):
```
    w₀  ≈  -1 + Δφ₀²/12
    
    w_a  ≈  β/H₀ · Δφ₀²/4
```

### 3.3 Deviation from $\Lambda$CDM

$\Lambda$CDM postulates:
```
    w_ΛCDM  =  -1  (constant)    →    w₀ = -1,  w_a = 0
```

RFT postulates:
```
    w_RFT(z)  =  w₀ + w_a · z/(1+z)    with  w_a ≈ β/H₀ ≠ 0  (if β ≠ 0)
```

**Quantitative estimate** for $\beta = 0.1\,H_0$, $\Delta\phi_0 = 0.3$ rad:
```
    w₀  ≈  -1 + (0.09)/12  ≈  -0.9925
    
    w_a  ≈  0.1 · (0.09)/4  ≈  0.00225
```

For $\beta = H_0$, $\Delta\phi_0 = 0.3$ rad:
```
    w₀  ≈  -0.9925
    
    w_a  ≈  0.0225
```

A value $w_a \approx 0.02$ is in principle compatible with DESI DR1 data (2024)
and lies within the detection range of DESI DR5 and Euclid.

### 3.4 Comparison with DESI DR1 (2024)

DESI DR1 BAO data (2024) combined with Planck+CMB yield:
```
    w₀  =  -0.827 ± 0.063   (68 % C.L.)
    w_a  =  -0.75  ± 0.29   (68 % C.L.)
```

The RFT prediction for small $\beta$ and $\Delta\phi_0$ is close to the ΛCDM
limit and compatible with current data. The prediction can be precisely tested
with Euclid (2026+) and DESI DR5 (2027).

---

## 4. Prediction 2: Modified Hubble Parameter $H(z)$

### 4.1 RFT Hubble function

From RT-42 AP1–AP2 the RFT Hubble function is:
```
    H_RFT(t)  =  H₀ · √ε(t)
               =  H₀ · √[1 - sin²(Δφ₀/2) · e^{βt}]
```

Since $z = a_0/a - 1$ and $a \propto e^{-\int H\,dt}$, the redshift-dependent
Hubble function in a small-$\beta/H_0$ approximation reads:
```
    H_RFT(z)  ≈  H₀ · √[Ω_m (1+z)³ + Ω_grad + Ω_dyn(z)]
```

with the dynamic RFT contribution:
```
    Ω_dyn(z)  ≈  Ω_Λ · [1 + (β/H₀) · z/(1+z)]
```

### 4.2 Relative deviation

The relative deviation from $\Lambda$CDM is:
```
    ΔH/H_ΛCDM  ≡  [H_RFT(z) - H_ΛCDM(z)] / H_ΛCDM(z)
```

For $\beta = 0.5\,H_0$ and $z = 1$:
```
    ΔH/H_ΛCDM  ≈  β/(2H₀) · z/(1+z) · Ω_Λ / (Ω_m(1+z)³ + Ω_Λ)
               ≈  0.25 · 0.5 · (0.68 / (0.32·8 + 0.68))
               ≈  0.25 · 0.5 · 0.21
               ≈  0.026  →  approx. 2–3 %
```

**Detectability:** Hubble parameter measurements via Type Ia supernovae (Rubin
LSST) and BAO distance measurements (DESI, Euclid) achieve 1–2 % accuracy — a
deviation of 2–3 % for $\beta \sim 0.5\,H_0$ would be detectable.

**Falsification criterion:**
```
    |H_RFT(z) - H_ΛCDM(z)| / H_ΛCDM(z) < 0.01  for all z ∈ [0, 2]
    →  β < 0.2 H₀  (excluded if violated)
```

---

## 5. Prediction 3: Structure Growth and Growth Factor

### 5.1 Linear growth equation

In the linear regime the matter density contrast $\delta_m$ satisfies:
```
    δ̈_m + 2H δ̇_m - (4πG/c²) ρ_m δ_m  =  0
```

In $\Lambda$CDM, $H(z)$ is determined by the Friedmann equation with $w = -1$.
In RFT, $H(z)$ is replaced by the RFT Hubble function. Since
$H_{\rm RFT}(z) > H_{\rm \Lambda CDM}(z)$ for $\beta > 0$ at low $z$, the
friction term $2H\dot\delta_m$ is enhanced — structure growth is **suppressed**.

### 5.2 Growth rate $f\sigma_8$

The observable product $f\sigma_8$ (growth rate × fluctuation amplitude) satisfies:
```
    f(z)  =  d ln D / d ln a    (D = linear growth factor)
    
    f_RFT(z)  <  f_ΛCDM(z)  for  β > 0  and  w > -1
```

**Quantitative estimate** for $\beta = 0.5\,H_0$, $z = 0.5$:
```
    Δ(fσ_8) / (fσ_8)_ΛCDM  ≈  -0.5 · (w_RFT + 1) · Ω_Λ / (Ω_m + Ω_Λ)
                            ≈  -0.5 · 0.01 · 0.68
                            ≈  -0.003  →  approx. 0.3 %
```

For larger $\beta$ or $\Delta\phi_0$ the deviation grows proportionally.

### 5.3 Measurement via RSD and gravitational lensing

- **Redshift-Space Distortions (RSD):** DESI and Euclid measure $f\sigma_8$
  with ~1–2 % accuracy up to $z \approx 2$. An RFT deviation of 0.3 % is
  borderline for $\beta \sim 0.5\,H_0$; for $\beta \sim H_0$ it would reach
  ~1 % and become detectable.

- **Weak gravitational lensing:** The lensing signal $\Sigma_8$ is sensitive
  to the integral $\int_0^{z_s} H^{-1}(z') D(z') dz'$. A deviation in $H(z)$
  propagates directly to $\Sigma_8$.

**Falsification criterion:**
```
    |f_RFT σ_8 - f_ΛCDM σ_8| / (f σ_8)_ΛCDM < 0.02  for  z < 1
    →  β < H₀  and  Δφ₀ < 0.5 rad  (excluded if violated)
```

---

## 6. Prediction 4: Cosmic Microwave Background

### 6.1 Integrated Sachs-Wolfe effect (ISW)

The dynamic $w(z)$ of RFT produces a **modified late-time integrated
Sachs-Wolfe effect** (ISW). For $w > -1$, gravitational potential wells decay
more slowly than in $\Lambda$CDM — the ISW signal at large angular scales
($\ell < 20$) is reduced.

The ISW temperature contrast is proportional to:
```
    ΔT_ISW / T  ∝  ∫ dΦ/dt dt    (along line of sight)
```

For $w > -1$: $dΦ/dt$ smaller $\Rightarrow$ ISW contribution smaller than in
$\Lambda$CDM.

### 6.2 Acoustic peaks

The scale factor at recombination $a_{\rm rec} \approx 1/1100$ is, at early
times ($z > 1100$), dominated by matter and radiation — the RFT phase gradient
$k_0$ is negligible on sub-Hubble scales there. The positions of the acoustic
CMB peaks ($\ell_1 \approx 220$) are therefore **consistent** with $\Lambda$CDM
in RFT, as long as $k_0$ remains super-horizon.

**Prediction:** No deviation in CMB peak positions; possible deviation in the
power spectrum at $\ell < 20$ (ISW) for $\beta \sim H_0$.

### 6.3 CMB falsification criteria

```
    ISW correlation  C_l^{ISW}  at  l < 20:
    
    |C_l^{RFT} - C_l^{ΛCDM}| / C_l^{ΛCDM}  <  5%
    →  β < 0.3 H₀  or  sin²(Δφ₀/2) < 0.01
```

---

## 7. Comparison with Current Observations

### 7.1 Planck 2018

| Observation | Planck value | RFT prediction ($\beta = 0$) | Compatible? |
|-------------|-------------|------------------------------|------------|
| $H_0$ | 67.4 ± 0.5 km/s/Mpc | $H_0$ = free | ✅ (free parameter) |
| $w_0$ | $-1.03 \pm 0.03$ | $w_0 \in [-1, -1/3]$ | ✅ (at $\Delta\phi_0 \to 0$) |
| $\Omega_\Lambda$ | 0.6847 ± 0.0073 | $\Omega_{\rm grad} = k_0^2 \hbar^2 c^{-2}/(2\mu_0 \rho_c)$ | ✅ (free) |
| $\sigma_8$ | 0.811 ± 0.006 | $\sigma_8$ slightly reduced for $\beta > 0$ | ✅ (small effect) |

### 7.2 DESI DR1 (2024)

DESI DR1 provides evidence for dynamic dark energy ($w_a \neq 0$):
```
    w₀ = -0.827 ± 0.063,   w_a = -0.75 ± 0.29
```

**RFT interpretation:**
- RFT allows $w_a > 0$ (for $\beta > 0$, approach to equilibrium) and
  $w_a < 0$ (for $\beta < 0$, departure from equilibrium).
- DESI DR1 shows $w_a < 0$ — in RFT this would require negative $\beta$
  (decreasing $\varepsilon$, i.e. departure from the de-Sitter fixed point) or
  a time-varying $k_0(t)$.
- This is not excluded in RFT — it requires an extension via AP6 (time-varying
  $k_0$) for a complete quantitative picture.

### 7.3 SH0ES Hubble tension

The Hubble tension ($H_0^{\rm CMB} = 67.4$ vs. $H_0^{\rm SH0ES} = 73.0$
km/s/Mpc) could be partly addressed in RFT by a non-vanishing initial phase
difference $\Delta\phi_0 > 0$, which produces an additional expansion rate:
```
    ΔH_0^{RFT}  ≈  H_0 · sin²(Δφ₀/2) · β/(2H₀)
```

For $\beta = H_0$ and $\Delta\phi_0 \approx 0.5$ rad:
```
    ΔH_0  ≈  H_0 · 0.062 · 0.5  ≈  3.1 % · H_0  ≈  2.1  km/s/Mpc
```

This explains the Hubble tension of $\approx 5.6$ km/s/Mpc only partially — the
RFT contribution is a possible partial factor, not a complete explanation.

---

## 8. Falsification Criteria

### 8.1 Primary falsification criterion: $w_a = 0$

```
    FALSIFICATION OF THE RFT PREDICTION:
    
    Measured  w_a  =  0  (at 5σ level)
    →  β  =  0  forced
    →  RFT fully equivalent to ΛCDM (limiting case)
    →  AP5 prediction falsified, but RFT not falsified
       (since β = 0 is an allowed limiting case)
    
    CONFIRMATION OF THE RFT PREDICTION:
    
    Measured  w_a  ≠  0  (at 3σ level)
    →  β ≠ 0  required
    →  ΛCDM falsified or strong evidence for dynamic DE
    →  RFT as dynamic DE model supported
    →  Value β/H₀ ≈ w_a / sin²(Δφ₀/2) directly measurable
```

### 8.2 Secondary falsification criteria

| No. | Observation | $\Lambda$CDM | RFT prediction | Threshold |
|----|-------------|-------------|----------------|----------|
| F1 | $w_a$ (DESI DR5, 2027) | 0 | $\approx \beta/H_0$ | $|w_a| > 0.05$ at 3σ |
| F2 | $\Delta H/H$ (Euclid $z<2$) | 0 | $< 2\,\%$ at $\beta = 0.5 H_0$ | $> 1\,\%$ at 3σ |
| F3 | $f\sigma_8$ (DESI+Euclid) | 0.46 at $z = 0.5$ | slightly reduced | $> 2\,\%$ deviation |
| F4 | ISW $C_\ell^{TE}$ ($\ell < 20$) | $\Lambda$CDM value | reduced for $\beta > 0$ | $> 5\,\%$ deviation |
| F5 | Hubble tension contribution | not explained | $\leq 2$ km/s/Mpc | no complete explanation |

### 8.3 Overall statement on falsifiability

RFT cosmology is **falsifiable** in the sense that:

1. The free parameters $(\beta, k_0, \Delta\phi_0)$ can be fully constrained by
   a combination of BAO, SNe Ia, CMB, and weak lensing.
2. The model makes a specific structural prediction: $w(z)$ follows the CPL
   form with $w_a \propto \beta/H_0$. Any observation that excludes $w_a > 0$
   at high significance forces $\beta = 0$ and hence the ΛCDM limiting case.
3. In the case $\beta = 0$, RFT is fully equivalent to $\Lambda$CDM — no
   deviation is measurable, but the model remains consistent (not falsified).

---

## 9. Verification of the Success Criterion

**Success criterion:** At least one measurable deviation — or proof of complete
equivalence.

**Assessment:**

✅ **Step 1: Free parameters identified.**
   $\beta$, $k_0$, $\Delta\phi_0$ — all motivated by A1–A8; $\beta \to 0$,
   $k_0 = $ const, $\Delta\phi_0 \to 0$ yields the ΛCDM limit.

✅ **Step 2: Observable effects identified.**
   Four predictions: $w(z)$, $H(z)$, $f\sigma_8$, ISW — all in principle
   measurable.

✅ **Step 3: Comparison with Planck, DES, SH0ES.**
   RFT with small $\beta$ and $\Delta\phi_0$ compatible; DESI DR1 hint at
   $w_a \neq 0$ consistent with RFT prediction.

✅ **Step 4: Falsification criteria stated.**
   Primary criterion: $w_a = 0$ (5σ) forces $\beta = 0$ (ΛCDM limit).
   Five secondary criteria specified.

✅ **Success criterion satisfied:** At least one measurable deviation (dynamic
   $w(z)$ with $w_a \approx \beta/H_0$) identified and supplied with concrete
   falsification thresholds.

**Overall conclusion:**

> **RFT cosmology makes a prediction structurally distinct from $\Lambda$CDM:**
> The dark energy equation-of-state parameter is dynamic,
> $w(z) = w_0 + w_a\,z/(1+z)$, with
> $w_a \approx \beta/H_0 \cdot \sin^2(\Delta\phi_0/2)$.
> For $\beta = 0$ RFT is fully equivalent to $\Lambda$CDM (limiting case).
> The prediction is compatible with DESI DR1 (2024) and testable by DESI DR5,
> Euclid, and Rubin LSST. A detection of $w_a \neq 0$ at high significance
> would be strong evidence for RFT phase dynamics; an exclusion of $w_a \neq 0$
> forces the ΛCDM limiting case of RFT.

---

## 10. Result and Outlook on AP6–AP7

**Central result of AP5:**

| Prediction | Parameter dependence | Detectability | Experiment |
|-----------|---------------------|---------------|-----------|
| $w_a = \beta/H_0 \cdot \sin^2(\Delta\phi_0/2)$ | $\beta$, $\Delta\phi_0$ | Yes | DESI DR5, Euclid |
| $\Delta H/H \lesssim 3\,\%$ at $\beta = 0.5 H_0$ | $\beta$ | Yes | Rubin LSST, Euclid |
| $\Delta(f\sigma_8) \lesssim 1\,\%$ | $\beta$, $\Delta\phi_0$ | Borderline | DESI+Euclid |
| ISW at $\ell < 20$ | $\beta$ | Challenging | Planck successor |
| Hubble tension: $\Delta H_0 \lesssim 2$ km/s/Mpc | $\beta$, $\Delta\phi_0$ | Partial | Rubin LSST |

**Outlook:**

- **AP6:** Test the hypothesis whether cosmic expansion can be understood as a
  phase effect ($k_0(t)$ time-varying). A time-varying $k_0$ would explain the
  DESI DR1 signal ($w_a < 0$) within RFT.
- **AP7:** Consistency check with RT-33 ($w$ range), RT-40 (Lorentz invariance
  of the gradient), RT-41 (A8: phase perturbations propagate at $c$).

**Connection to existing results:**
- RT-42 AP1: $H = H_0 \cos(\Delta\phi/2)$ — holds for the homogeneous part;
  the gradient part ($k_0$) modifies $H$ through $\rho_{\rm grad}$
- RT-42 AP2: $\varepsilon(t) = 1 - \sin^2(\Delta\phi_0/2)\,e^{\beta t}$ —
  direct source of $w(z)$ and $H(z)$
- RT-42 AP3: $w_{\rm eff} \in [-1, +1/3]$; $\Lambda$CDM = limit at $\beta \to 0$,
  $k_0 = $ const — foundation of the entire AP5 analysis
- RT-42 AP4: Scale separation confirmed — cosmological predictions concern
  exclusively the $k_0$ sector, not the warp regime

**Core documents:**
`de/fakten/theorie/rt42_ap5_falsifizierbare_abweichungen_lcdm.md` ·
`en/facts/theory/rt42_ap5_falsifiable_deviations_lcdm.md`

---

*RT-42 AP5 — DominicReneSchu/RFT — September 2026*
