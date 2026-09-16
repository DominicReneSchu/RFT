# RT-40 AP1 — Formal Identification: Phase ↔ Rapidity

*Dominic René Schu, September 2026*
*Status: Completed (Sep 2026)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Domain of Δφ from A1–A4](#2-domain-of-δφ-from-a1a4)
3. [The Bridge Formula as Starting Point](#3-the-bridge-formula-as-starting-point)
4. [The Bijective Map f: [0,π) → [0,∞)](#4-the-bijective-map-f-0π--0)
5. [Hyperbolic Metric on Phase Space](#5-hyperbolic-metric-on-phase-space)
6. [Phase Composition Law and Relativistic Velocity Addition](#6-phase-composition-law-and-relativistic-velocity-addition)
7. [Success Criterion: Proof of Bijectivity and Additivity](#7-success-criterion-proof-of-bijectivity-and-additivity)
8. [Result and Outlook for AP2–AP4](#8-result-and-outlook-for-ap2ap4)

---

## 1. Objective and Success Criterion

**Task (RT-40 AP1):** Determine whether the RFT phase difference Δφ and the
relativistic rapidity φ share the same mathematical structure.

**Success criterion:** Construction of a bijective map
```
    f: [0, π) → [0, ∞)
```
with the additivity property
```
    f(Δφ₁ ⊕ Δφ₂) = f(Δφ₁) + f(Δφ₂)
```
where `⊕` denotes a well-defined composition rule on [0, π) corresponding to
relativistic velocity addition.

**Result:** The success criterion is satisfied. The map
```
    f(Δφ) = arcsech(cos(Δφ/2)) = arctanh(sin(Δφ/2))
           = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
```
is the sought bijective, additive identification.

---

## 2. Domain of Δφ from A1–A4

### 2.1 Phases from A1

Axiom 1 (Universal Oscillation) postulates:
```
    ψ(x, t) = A · cos(kx − ωt + φ),    φ ∈ [0, 2π)
```
For two oscillators i, j the phase difference is
```
    Δφ = φᵢ − φⱼ   (mod 2π)
```

### 2.2 Canonical domain via A4 and G_sync invariance

From Axiom 4 (Coupling Energy) and the RT-02 invariance analysis:

- **Parity (RT-02, §3):** ε(Δφ) = ε(−Δφ) → Δφ and −Δφ are physically equivalent.
- **Monotonicity (A4):** ε(Δφ) = cos²(Δφ/2) is strictly monotonically decreasing on [0, π].
- **Boundary conditions (A4):**
  - Δφ = 0: ε = 1 (full coupling)
  - Δφ = π: ε = 0 (full decoupling)

The physically relevant canonical domain is therefore:
```
    Δφ ∈ [0, π]
```
with open upper boundary [0, π) for the bijective map (Δφ = π corresponds to
the speed limit c, which is never reached — see AP4).

### 2.3 Topological structure of phase space

The space of coupling states P = {ε(Δφ) | Δφ ∈ [0, π]} = [0, 1] is compact,
but the associated physical distance structure (Section 5) renders it open
towards ∞: P is isomorphic to [0, ∞) under the rapidity metric.

---

## 3. The Bridge Formula as Starting Point

RT-40 identifies the following known but unproven bridge:
```
    Δφ = 2 arccos(sech φ)   ⟺   ε(Δφ) = 1/γ²
```
with φ = relativistic rapidity, γ = Lorentz factor.

**Derivation:** From ε(Δφ) = cos²(Δφ/2) and ε = 1/γ² = sech²(φ):
```
    cos²(Δφ/2) = sech²(φ)
    cos(Δφ/2)  = sech(φ)           [both sides ≥ 0 on the canonical domain]
    Δφ/2       = arccos(sech(φ))
    Δφ         = 2 arccos(sech(φ))  ✓
```
The bridge formula is thus a direct consequence of the definition
ε(Δφ) = cos²(Δφ/2) (A4) together with the identification ε = 1/γ². The
identification ε = 1/γ² itself is the subject of AP2.

---

## 4. The Bijective Map f: [0,π) → [0,∞)

### 4.1 Definition

Let φ denote the relativistic rapidity, defined by v = c·tanh(φ) with φ ∈ [0, ∞).
From cos(Δφ/2) = sech(φ) the inverse function follows directly:
```
    f(Δφ) := arcsech(cos(Δφ/2))
```

### 4.2 Closed-form expression (three equivalent representations)

**Representation 1 (arcsech):**
```
    f(Δφ) = arcsech(cos(Δφ/2))
           = ln((1 + √(1 − cos²(Δφ/2))) / cos(Δφ/2))
           = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
```

**Representation 2 (arctanh):**

*Claim:* arcsech(cos(Δφ/2)) = arctanh(sin(Δφ/2))

*Proof:*
```
    arctanh(sin(Δφ/2))
    = (1/2) ln((1 + sin(Δφ/2)) / (1 − sin(Δφ/2)))
    = (1/2) ln((1 + sin(Δφ/2))² / (1 − sin²(Δφ/2)))
    = (1/2) ln((1 + sin(Δφ/2))² / cos²(Δφ/2))
    = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
    = arcsech(cos(Δφ/2))    ✓
```

**Representation 3 (explicit logarithmic):**
```
    f(Δφ) = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
```

### 4.3 Bijectivity

| Property | Verification |
|---|---|
| Well-definedness | cos(Δφ/2) > 0 for Δφ ∈ [0, π) |
| f(0) = 0 | arcsech(cos 0) = arcsech(1) = 0 ✓ |
| f(π) = ∞ | arcsech(cos(π/2)) = arcsech(0) = ∞ ✓ |
| Strict monotonicity | df/dΔφ = 1/(2cos(Δφ/2)) > 0 for Δφ ∈ [0, π) ✓ |
| Surjectivity onto [0,∞) | Follows from continuity + limit behaviour ✓ |

The map f: [0, π) → [0, ∞) is bijective. □

### 4.4 Numerical reference values

| Δφ | f(Δφ) (rapidity) | v/c = tanh(f) | γ = 1/cos(Δφ/2) |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| π/6 | 0.2554 | 0.2527 | 1.0353 |
| π/3 | 0.5493 | 0.5000 | 1.1547 |
| π/2 | 0.8814 | 0.7071 | 1.4142 |
| 2π/3 | 1.3170 | 0.8660 | 2.0000 |
| 5π/6 | 2.0634 | 0.9659 | 3.8637 |
| π⁻ | ∞ | 1 | ∞ |

---

## 5. Hyperbolic Metric on Phase Space

### 5.1 Induced metric

The map f: ([0,π), ds²_RFT) → ([0,∞), dφ²) is an isometry when the
pullback metric on the phase difference space is defined as:
```
    ds²_RFT := dφ² = (df/dΔφ)² · dΔφ²
```

Computation of the derivative:
```
    f(Δφ) = arcsech(cos(Δφ/2))

    df/dΔφ = d/du[arcsech(u)] · d/dΔφ[cos(Δφ/2)]     with u = cos(Δφ/2)

           = (−1 / (u √(1−u²))) · (−sin(Δφ/2)/2)

           = sin(Δφ/2) / (2 · cos(Δφ/2) · sin(Δφ/2))

           = 1 / (2 · cos(Δφ/2))
```

It follows that:
```
    ds²_RFT = dΔφ² / (4 · cos²(Δφ/2)) = dΔφ² / (4 · ε(Δφ))
```

### 5.2 Physical interpretation

The metric `ds²_RFT = dΔφ² / (4ε(Δφ))` has the following properties:

- **For small phase differences (Δφ → 0, ε → 1):** ds²_RFT ≈ dΔφ²/4 — flat,
  Euclidean metric (non-relativistic limit).
- **Approaching π (ε → 0):** ds²_RFT → ∞ — the metric diverges. Infinitesimal
  phase steps near decoupling correspond to finite rapidity intervals.
  This is the direct analogue of the impossibility of reaching c.
- **Curvature:** The curvature of the metric is determined by the coupling
  function ε(Δφ) — it is an intrinsic property of the RFT coupling dynamics.

### 5.3 Isometry to the hyperbolic unit space

The phase difference space ([0,π), ds²_RFT) is isometric to the real rapidity
axis ([0,∞), dφ²), which carries the geometry of 1+1-dimensional Minkowski space.

The isometry is given explicitly by f(Δφ) = arcsech(cos(Δφ/2)).

---

## 6. Phase Composition Law and Relativistic Velocity Addition

### 6.1 Definition of the phase composition ⊕

Analogously to rapidity addition (φ₁₂ = φ₁ + φ₂ for collinear boosts), define
the RFT phase composition as the unique operation ⊕ on [0, π) satisfying:
```
    f(Δφ₁ ⊕ Δφ₂) = f(Δφ₁) + f(Δφ₂)
```
Since f is bijective, ⊕ exists and is unique:
```
    Δφ₁ ⊕ Δφ₂ := f⁻¹(f(Δφ₁) + f(Δφ₂))
```

### 6.2 Explicit formula for ⊕

With f⁻¹(φ) = 2·arccos(sech(φ)) and the identity
sech(φ₁+φ₂) = sech(φ₁)sech(φ₂) / (1 + tanh(φ₁)tanh(φ₂)):

Let p = cos(Δφ₁/2), q = cos(Δφ₂/2), so sech(φᵢ) = p resp. q, and:
```
    cosh(φ₁ + φ₂) = cosh(φ₁)cosh(φ₂) + sinh(φ₁)sinh(φ₂)
                  = (1/p)(1/q) + (√(1−p²)/p)(√(1−q²)/q)
                  = (1 + sin(Δφ₁/2)·sin(Δφ₂/2)) / (cos(Δφ₁/2)·cos(Δφ₂/2))
```
Therefore:
```
    cos((Δφ₁ ⊕ Δφ₂)/2) = sech(φ₁ + φ₂)
                        = cos(Δφ₁/2) · cos(Δφ₂/2)
                          / (1 + sin(Δφ₁/2) · sin(Δφ₂/2))
```
and hence:
```
    Δφ₁ ⊕ Δφ₂ = 2 arccos(cos(Δφ₁/2) · cos(Δφ₂/2)
                          / (1 + sin(Δφ₁/2) · sin(Δφ₂/2)))
```

### 6.3 Comparison with relativistic velocity addition

The relativistic velocity addition formula reads (via rapidities):
```
    v₁₂/c = tanh(φ₁ + φ₂) = (tanh(φ₁) + tanh(φ₂)) / (1 + tanh(φ₁)tanh(φ₂))
           = (v₁/c + v₂/c) / (1 + v₁v₂/c²)
```

Via the identification v = c·tanh(f(Δφ)) = c·tanh(arctanh(sin(Δφ/2))) = c·sin(Δφ/2):
```
    v/c = sin(Δφ/2)    [RFT velocity parameter]
```

The RFT phase composition law thereby becomes the relativistic velocity addition:
```
    sin((Δφ₁ ⊕ Δφ₂)/2)
    = (sin(Δφ₁/2) + sin(Δφ₂/2)) / (1 + sin(Δφ₁/2)·sin(Δφ₂/2))
```
*Derivation:* With p = cos(Δφ₁/2), q = cos(Δφ₂/2):
Using tanh(φ₁+φ₂) = (tanh φ₁ + tanh φ₂)/(1+tanh φ₁ tanh φ₂) with tanh(φᵢ) = sin(Δφᵢ/2)
confirms this identity.

**Conclusion:** The RFT phase composition ⊕ is structurally identical to
relativistic velocity addition under the identification v/c = sin(Δφ/2).

### 6.4 Limiting cases

| Situation | Δφ₁ | Δφ₂ | Δφ₁ ⊕ Δφ₂ | Physical interpretation |
|---|---|---|---|---|
| No motion | 0 | Δφ | Δφ | Identity element (v₁ = 0) |
| Low velocity | ε₁ | ε₂ | ε₁ + ε₂ + O(ε²) | Galilean limit |
| v₁ → c | π⁻ | Δφ | π⁻ | c + v = c (constancy of c) |

---

## 7. Success Criterion: Proof of Bijectivity and Additivity

**Theorem (AP1 main result):**

The map
```
    f: [0, π) → [0, ∞),    f(Δφ) = arcsech(cos(Δφ/2)) = arctanh(sin(Δφ/2))
```
satisfies all conditions of the success criterion:

1. **Bijectivity:** f is strictly monotonically increasing (df/dΔφ = 1/(2cos(Δφ/2)) > 0),
   f(0) = 0, lim_{Δφ→π} f(Δφ) = ∞. Hence f: [0,π) → [0,∞) is bijective.

2. **Additivity:** With the composition rule
   ```
       Δφ₁ ⊕ Δφ₂ = 2 arccos(cos(Δφ₁/2)·cos(Δφ₂/2) / (1 + sin(Δφ₁/2)·sin(Δφ₂/2)))
   ```
   one has: f(Δφ₁ ⊕ Δφ₂) = f(Δφ₁) + f(Δφ₂).

   *Proof of additivity:*
   ```
       f(Δφ₁ ⊕ Δφ₂)
       = arctanh(sin((Δφ₁ ⊕ Δφ₂)/2))
       = arctanh((sin(Δφ₁/2) + sin(Δφ₂/2)) / (1 + sin(Δφ₁/2)·sin(Δφ₂/2)))
   ```
   The arctanh addition theorem states:
   ```
       arctanh(x) + arctanh(y) = arctanh((x+y)/(1+xy))    for |xy| < 1
   ```
   Therefore:
   ```
       f(Δφ₁ ⊕ Δφ₂) = arctanh(sin(Δφ₁/2)) + arctanh(sin(Δφ₂/2))
                     = f(Δφ₁) + f(Δφ₂)    ✓
   ```
   (The condition |xy| < 1 holds for Δφ₁, Δφ₂ ∈ [0,π) since sin < 1.)

**The success criterion of AP1 is fully proven.** □

---

## 8. Result and Outlook for AP2–AP4

### 8.1 Summary of AP1 results

| Question (AP1) | Result |
|---|---|
| Domain of Δφ from A1–A4? | Δφ ∈ [0, π), canonical via A4 monotonicity |
| Hyperbolic metric on phase space? | **Yes:** ds²_RFT = dΔφ²/(4ε(Δφ)) |
| Phase addition consistent with relativity? | **Yes:** ⊕ is structurally identical to relativistic velocity addition |
| Bijective map f with additivity? | **Yes:** f(Δφ) = arctanh(sin(Δφ/2)), proven |

**Core result:** Δφ and the relativistic rapidity φ share the same mathematical
structure. The identification
```
    φ = arctanh(sin(Δφ/2))    ⟺    Δφ = 2 arcsin(tanh φ)
```
(equivalent to the bridge formula Δφ = 2 arccos(sech φ)) is an exact mathematical
isometry, not an approximation or analogy.

### 8.2 What AP1 achieves and what it does not

**AP1 achieves:**
- Mathematical isometry between the RFT phase space and the rapidity axis proven.
- Explicit bijective map constructed and proven.
- Hyperbolic metric structure on phase space identified.
- RFT composition law shown to be equivalent to relativistic velocity addition.

**AP1 does not (open for AP2–AP4):**
- The identification ε = 1/γ² has not yet been derived from A4 — it is assumed
  here as a premise, and is the subject of **AP2**.
- The bridge formula is shown as a consequence of ε = cos²(Δφ/2), but the
  physical meaning of c as a structural limit requires **AP4**.
- The Lorentz transformation itself (coordinate space) is the subject of **AP3**.

### 8.3 Significance for RT-40

AP1 provides the formal framework on which AP2–AP6 build. The isometry is not
heuristic but exactly proven. The bridge formula
```
    Δφ = 2 arccos(sech φ)   ⟺   ε(Δφ) = 1/γ²
```
is not a coincidence but the explicit form of the bijective map between the
RFT phase space and Minkowski rapidity space.

**Next step (AP2):** Show that ε(Δφ) = 1/γ² follows directly from interpreting
A4 as the relativistic resonator energy E = γmc².

---

## Links to Existing Documents

- Axioms A1–A4: [`../../docs/definitionen/axiomatische_grundlegung.md`](../../docs/definitionen/axiomatische_grundlegung.md) *(DE)*
- ε = cos²(Δφ/2) uniqueness (RT-02): [`gsync_group_structure.md`](gsync_group_structure.md)
- π as geometric factor (RT-01): [`action_integral_pi_derivation.md`](action_integral_pi_derivation.md)
- RT-40 overview: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
- German version: [`../../de/fakten/theorie/rt40_ap1_phase_rapiditaet.md`](../../de/fakten/theorie/rt40_ap1_phase_rapiditaet.md)
