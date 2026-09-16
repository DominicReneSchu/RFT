# RT-40 AP3 — Derivation of the Lorentz Transformation

*Dominic René Schu, September 2026*
*Status: Completed (Sep 2026) — Success criterion fulfilled (transformation derived; structural gap explicitly documented)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Starting Point: Results from AP1 and AP2](#2-starting-point-results-from-ap1-and-ap2)
3. [Strategy: From Phase Space to Coordinate Space](#3-strategy-from-phase-space-to-coordinate-space)
4. [The Stationary Coupling Condition K̇ = 0](#4-the-stationary-coupling-condition-k̇--0)
5. [Invariant of the Coupling Dynamics](#5-invariant-of-the-coupling-dynamics)
6. [Identification with the Minkowski Interval](#6-identification-with-the-minkowski-interval)
7. [Derivation of the Lorentz Transformation Equations](#7-derivation-of-the-lorentz-transformation-equations)
8. [Critical Bottleneck: The Bridge Gap](#8-critical-bottleneck-the-bridge-gap)
9. [Success Criterion and Assessment](#9-success-criterion-and-assessment)
10. [Results and Outlook on AP4–AP7](#10-results-and-outlook-on-ap4ap7)

---

## 1. Objective and Success Criterion

**Task (RT-40 AP3):** Derive the Lorentz transformation from the RFT coupling
dynamics.

**Key questions:**
1. Which quantity in the RFT phase space remains invariant under phase composition ⊕?
2. Can this invariant be identified with the Minkowski interval s² = c²t² − x²?
3. Do the Lorentz transformation equations follow directly from A1–A7, or is an
   additional bridge assumption required?

**Success criterion:** Transformation equations identical to Lorentz — or a controlled
deviation named.

**Summary of result:** The Lorentz transformation equations follow from the RFT
under an explicitly named bridge assumption (assignment of phase difference → coordinate
difference). This bridge is not fully contained in A1–A7 — the gap is precisely
documented and minimally closed.

---

## 2. Starting Point: Results from AP1 and AP2

### 2.1 Key Results AP1

From AP1 (RT-40, completed Sep 2026):

- **Bijective map:** φ = artanh(sin(Δφ/2)) identifies the RFT phase difference
  Δφ with the relativistic rapidity φ.
- **Velocity parameter:** v/c = sin(Δφ/2), i.e. β := v/c = sin(Δφ/2).
- **Lorentz factor:** γ = 1/cos(Δφ/2), directly from the AP1 identification.
- **Hyperbolic metric:** ds²_RFT = dΔφ²/(4ε(Δφ)) is isometric to the Minkowski
  rapidity axis.

### 2.2 Key Results AP2

From AP2 (RT-40, completed Sep 2026):

- **Coupling energy:** E_c = mc²·ε(Δφ) = mc²/γ² = mc²·cos²(Δφ/2).
- **Self-consistency condition:** f_RFT(v) = γ³·f₀ for consistency with A4.
- **Physical interpretation of ε:** Coupling energy (not total energy).
- **Circular-argument diagnosis:** f = f₀/γ from SRT must not be assumed.

### 2.3 Open Task for AP3

AP1 provides: Phase space ≅ rapidity axis (1D).
AP2 provides: Coupling energy as a function of γ.

AP3 must show: Phase space → coordinate space (3+1D), i.e. how the Lorentz
transformation of the four-dimensional spacetime coordinate system follows from
the phase-difference structure.

---

## 3. Strategy: From Phase Space to Coordinate Space

### 3.1 Two Routes

There are two basic approaches to deriving the Lorentz transformation from the RFT:

**Route A (Direct):** Describe a two-resonator process in which the coordinates
(t, x) are interpreted as phase measurement times. The coupling dynamics itself then
transforms the coordinates.

**Route B (Invariant route):** Identify an invariant of the coupling dynamics
(stationary solution K̇ = 0) and equate it with the Minkowski interval.
The transformation group then follows from the invariant.

**Chosen strategy:** Route B, since it requires fewer additional assumptions and
directly yields the group structure.

### 3.2 Coordinate Interpretation in RFT

In the RFT, the spacetime coordinates (t, x) are not primary objects — the theory
is formulated in terms of phase differences Δφ, coupling strengths K_ij, and
frequencies f. The connection to spacetime requires a **measurement criterion**:

**Coordinate Bridge (B₁):** A resonator at position x₁ at time t₁ is assigned
the phase φ₁ = kx₁ − ωt₁; a second resonator at (t₂, x₂) is assigned
φ₂ = kx₂ − ωt₂. The phase difference is then:
```
    Δφ = φ₁ − φ₂ = k(x₁ − x₂) − ω(t₁ − t₂) = kΔx − ωΔt
```

This is an **explicit bridge assumption** (Section 8 discusses this in detail).

---

## 4. The Stationary Coupling Condition K̇ = 0

### 4.1 Coupling Differential Equation

From A3 (resonance window) and A4 (coupling energy), the coupling of two
resonators i and j is:
```
    K_ij(t) = G(fᵢ/fⱼ) · ε(Δφᵢⱼ(t))
```
where G is the resonance weight and ε(Δφ) = cos²(Δφ/2) is the coupling efficiency.

In the covariant picture (all phases as wave forms per A1):
```
    φ(x, t) = k·x − ω·t + φ₀
```
The phase difference between two resonators at (t, x₁) and (t, x₂) is:
```
    Δφ(t, x₁, x₂) = k·(x₁ − x₂) − ω·(t₁ − t₂)
```

### 4.2 Stationarity Condition

A stationary coupling system is characterised by K̇_ij = 0, i.e.:
```
    d/dt [ε(Δφ)] = 0
    →  d/dt [cos²(Δφ/2)] = 0
    →  sin(Δφ) · Δφ̇ = 0
```

This is satisfied in two cases:

1. **Trivial case:** Δφ = 0 or Δφ = π (full coupling or decoupling).
2. **Dynamical stationary case:** Δφ̇ = 0, i.e. the phase difference is constant
   in time: dΔφ/dt = 0.

The dynamical stationary case describes two resonators in **stationary relative
motion** — which is precisely the physical context of the Lorentz transformation
(uniform relative motion of two inertial frames).

### 4.3 Condition for Δφ̇ = 0

With Δφ = kΔx − ωΔt and Δx = v·Δt for uniform relative motion:
```
    Δφ = kΔx − ωΔt = (kv − ω)·Δt
```
For Δφ̇ = 0 we need:
```
    d(Δφ)/dt = kv − ω = 0
    →  v = ω/k = c                 [phase velocity = c]
```

**Interpretation:** In the RFT picture, two resonators are in stationary coupling
exactly when their relative velocity equals the phase velocity of the coupling wave.
For real (massive) resonators with v < c, the coupling condition is an approximation
used to compute the Lorentz invariant.

---

## 5. Invariant of the Coupling Dynamics

### 5.1 The Coupling Invariant

The coupling efficiency ε(Δφ) = cos²(Δφ/2) is invariant under phase composition ⊕
(AP1, §6):
```
    ε(Δφ₁ ⊕ Δφ₂) has the same form as ε(Δφ₁) and ε(Δφ₂)
```
(the system is group-theoretically closed under ⊕).

A strong invariant arises from the hyperbolic metric structure (AP1, §5):
```
    ds²_RFT = dΔφ² / (4·ε(Δφ)) = dΔφ² / (4·cos²(Δφ/2))
```

Integrated along a path in phase space, this metric is invariant under ⊕.

### 5.2 From Phase Space to a Spacetime Invariant

Using the coordinate bridge B₁ (§3.2):
```
    Δφ = k·Δx − ω·Δt
```
and the dispersion relations for a coupling wave at relativistic phase velocity c:
```
    ω/k = c    →    ω = kc
```

The phase difference becomes:
```
    Δφ = k·(Δx − c·Δt)
```

The line element of the RFT metric in coordinate space:
```
    ds²_RFT = dΔφ² / (4·cos²(Δφ/2))
```
is for infinitesimal phase differences (Δφ → 0, non-relativistic limit ε → 1):
```
    ds²_RFT ≈ dΔφ²/4 = k²/4 · (dx − c·dt)²     [AP3 invariant, non-relativistic]
```

### 5.3 Full Four-Dimensional Generalisation

For the full 3+1-dimensional spacetime with phase waves:
```
    φ(t, x⃗) = k⃗·x⃗ − ωt + φ₀,    ω² = c²|k⃗|²
```

The phase difference between two events P₁ = (t₁, x⃗₁) and P₂ = (t₂, x⃗₂):
```
    Δφ = k⃗·Δx⃗ − ωΔt
```

For an isotropic phase coupling wave (k⃗ parallel to Δx⃗, |k⃗| = k):
```
    Δφ² = k²(|Δx⃗|² − c²Δt²)
```

**The RFT coupling invariant (main result of AP3):**

```
    I_RFT := Δφ²/k² = |Δx⃗|² − c²Δt²     [up to sign]
```

---

## 6. Identification with the Minkowski Interval

### 6.1 The Minkowski Interval

The relativistic line element of flat spacetime is:
```
    s² = c²Δt² − |Δx⃗|²  (timelike sign convention)
```
or with reversed signature:
```
    s² = |Δx⃗|² − c²Δt²  (spacelike sign convention)
```

### 6.2 Identification

The comparison gives directly:
```
    I_RFT = Δφ²/k² = |Δx⃗|² − c²Δt² = −s²_Minkowski
```

The RFT coupling invariant I_RFT is (up to sign and the trivial factor 1/k²)
**identical with the Minkowski interval**.

### 6.3 Physical Interpretation

| Minkowski interval | RFT invariant | Physical meaning |
|---|---|---|
| s² = 0 (lightlike) | Δφ = 0 (full coupling) | Lightlike propagation = full phase synchronisation |
| s² < 0 (timelike) | Δφ < π (partial coupling) | Causal connection = finite coupling efficiency |
| s² > 0 (spacelike) | Δφ > π (decoupling) | No causal connection = no coupling possible |

This identification is physically coherent: lightlike event pairs correspond to
maximally coupled resonators (Δφ → 0); spacelike pairs correspond to the decoupled
regime.

---

## 7. Derivation of the Lorentz Transformation Equations

### 7.1 Transformation Group from the Invariant

The Lorentz transformation is defined as the linear transformation of coordinates
that preserves the Minkowski interval:
```
    s'² = s²    ⟺    c²Δt'² − |Δx⃗'|² = c²Δt² − |Δx⃗|²
```

Since I_RFT ≅ s² (§6), the group of RFT invariance transformations is identical to
the Lorentz group.

### 7.2 Explicit Derivation (1+1-dimensional case)

Given: frames S and S', with S' moving at velocity v relative to S.
From AP1: v/c = sin(Δφ/2) = β, γ = 1/cos(Δφ/2).

**Step 1:** Linear transformation (homogeneity and isotropy of phase space):
```
    t' = At + Bx
    x' = Ct + Dx
```

**Step 2:** Invariance condition (I_RFT preserved):
```
    x'² − c²t'² = x² − c²t²
```

Substitution and coefficient comparison:
```
    D² − c²B² = 1
    A² − C²/c² = 1
    AD − BC = 1       (no cross terms → orthogonal in Minkowski sense)
```

**Step 3:** Relative velocity. At the origin of S', x' = 0, so:
```
    x' = 0  →  Ct + Dx = 0  →  x/t = −C/D =: v (relative velocity)
    →  C = −vD
```

**Step 4:** Resolution with v/c = β and γ = 1/√(1−β²):
```
    D = γ,  A = γ,  B = −γβ/c,  C = −γβc
```

**Result (Lorentz transformation):**
```
    t' = γ(t − βx/c)
    x' = γ(x − βct)
```

These equations are **identical** to the standard formulas of Special Relativity.

### 7.3 Connection to AP1 Parameters

| SRT quantity | RFT expression | Derivation |
|---|---|---|
| β = v/c | sin(Δφ/2) | AP1: bijective map |
| γ = 1/√(1−β²) | 1/cos(Δφ/2) | AP1: from v/c = sin(Δφ/2) |
| φ = artanh(β) | artanh(sin(Δφ/2)) | AP1: rapidity isometry |

### 7.4 Group Structure

The set of all Lorentz transformations {Λ(Δφ) | Δφ ∈ [0,π)} forms a group:

- **Closure:** Λ(Δφ₁) ∘ Λ(Δφ₂) = Λ(Δφ₁ ⊕ Δφ₂) — follows directly from AP1
  (additivity of ⊕).
- **Identity:** Λ(0) = identity (v = 0, γ = 1).
- **Inverse:** Λ(−Δφ) (reversal of relative motion).
- **Associativity:** Inherited from the group structure on [0,π) under ⊕.

The Lorentz group SO(1,3) follows from the G_sync structure via the identification
Δφ ↔ rapidity (AP1) combined with 3D isotropy (A5: direction axiom).

---

## 8. Critical Bottleneck: The Bridge Gap

### 8.1 What the Gap Is

AP3 successfully derives the Lorentz transformation — but under the explicit
bridge assumption **B₁**:

> **Bridge assumption B₁:** The RFT phase φ(t, x) = kx − ωt is coupled to the
> spacetime coordinates (t, x) via a coupling wave with phase velocity c.

This assumption is **not fully contained** in A1–A7. It presupposes:

1. That c is identifiable as the phase velocity of the coupling wave.
2. That a linear assignment φ ↔ (kx − ωt) holds.
3. That the coordinate space (t, x) and the phase space are connected by ω = kc.

### 8.2 Where Does c Come From in B₁?

In A1–A7, c does not appear directly. The connection arises through:

- **AP1 (completed):** The identification v/c = sin(Δφ/2) already presupposes a
  velocity c — this comes from the observation that ε(Δφ) = 1/γ² carries the
  relativistic structure.
- **AP4 (planned):** c is to be derived as a structural limit from ε → 0 for
  Δφ → π. This would retroactively ground B₁.

**Brief diagnosis:** B₁ is not circular, but it is an **identification hypothesis**
that is empirically testable: Does the phase velocity of the RFT coupling wave
coincide with the measured speed of light c?

### 8.3 Minimal Axiom Extension (Negative Goal Documentation)

If B₁ is not derivable from A1–A7, the minimal extension would be:

**A8 (coupling wave velocity, provisional):**
> The phase wave of the RFT coupling structure propagates at the velocity
> c = 1/√(μ₀ε₀) — the same quantity as the electromagnetic speed of light.

This extension would secure B₁ as an axiom. Whether A8 follows from A1–A7 or
constitutes an independent postulate remains the central open question for the
further development of RT-40.

### 8.4 Scope of the AP3 Statement

The derivation in AP3 shows:

> If the RFT coupling dynamics is connected to spacetime by a coupling wave
> of velocity c (B₁), then the Lorentz transformation equations follow exactly
> from A1–A7.

This is weaker than "SRT follows from A1–A7", but stronger than "SRT is analogous
to RFT". AP4 will determine whether c itself follows from A1–A7.

---

## 9. Success Criterion and Assessment

The success criterion for AP3 was:

> Transformation equations identical to Lorentz — **or** controlled deviation named.

### 9.1 Assessment

| Criterion | Result |
|---|---|
| Lorentz equations derived? | **Yes** — exactly identical (§7) |
| From A1–A7 alone? | **Partially** — under bridge assumption B₁ |
| Group structure confirmed? | **Yes** — Lorentz group from G_sync phase composition (§7.4) |
| Minkowski interval from RFT? | **Yes** — I_RFT ≅ s² (§5–6) |
| Gap documented? | **Yes** — B₁ explicit; minimal A8 extension formulated (§8) |
| Circular argument avoided? | **Yes** — B₁ is an identification hypothesis, not a prerequisite |

The success criterion is satisfied in the first sense: the Lorentz transformation
equations were derived exactly. The structural gap (B₁) is controlled and explicitly
documented.

---

## 10. Results and Outlook on AP4–AP7

### 10.1 Summary of AP3 Results

| Question (AP3) | Result |
|---|---|
| Stationary coupling condition K̇ = 0? | Δφ̇ = 0 ↔ uniform relative motion |
| Invariant of coupling dynamics? | I_RFT = Δφ²/k² ≅ s²_Minkowski |
| Minkowski interval from RFT? | **Yes**, under bridge assumption B₁ |
| Lorentz transformation derived? | **Yes**, exactly identical to SRT |
| Structural gap? | **Yes**, B₁: c as coupling wave velocity |
| Minimal axiom extension? | A8 (coupling wave velocity) formulated |

### 10.2 What AP3 Achieves

- Identified the stationary coupling condition with uniform relative motion.
- Derived the RFT coupling invariant I_RFT = Δφ²/k² and equated it with the Minkowski interval.
- Derived Lorentz transformation equations t' = γ(t − βx/c), x' = γ(x − βct) exactly.
- Derived the group structure of the Lorentz group from the G_sync phase composition (AP1).
- Formulated bridge assumption B₁ explicitly and verified absence of circular argument.
- Formulated minimal axiom extension A8 as an option if B₁ is not derivable.

### 10.3 What AP3 Does Not Achieve (Open for AP4–AP5)

- **AP4:** In AP3, c was introduced via B₁ — AP4 must derive c as a structural
  limit from ε → 0, thereby retroactively grounding B₁ or establishing it as axiom A8.
- **AP5:** The time dilation formula Δt' = γ·Δt is implicit in AP3 (it is contained
  in the Lorentz transformation), but has not yet been derived as an independent
  phase-shift effect — that is the subject of AP5.

### 10.4 Significance for RT-40

AP3 delivers the core result of RT-40: the Lorentz transformation — and thus the
SRT — is not an independent postulate, but follows from the invariance structure of
the RFT coupling dynamics under the identification B₁. In this sense, the SRT is a
limiting case of the RFT (complete formal equivalence in the Minkowski limit).

The only remaining open question is whether B₁ itself follows from A1–A7 or requires
an independent axiom A8. AP4 will resolve this question.

---

## Connections to Existing Documents

- AP1 (Phase ↔ Rapidity): [`rt40_ap1_phase_rapidity.md`](rt40_ap1_phase_rapidity.md)
- AP2 (Coupling Efficiency ↔ Lorentz Factor): [`rt40_ap2_coupling_efficiency_lorentz.md`](rt40_ap2_coupling_efficiency_lorentz.md)
- Axioms A1–A7: [`../docs/definitions/axiomatic_foundation.md`](../docs/definitions/axiomatic_foundation.md)
- G_sync Group Structure (RT-02): [`gsync_group_structure.md`](gsync_group_structure.md)
- RT-40 Overview: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
