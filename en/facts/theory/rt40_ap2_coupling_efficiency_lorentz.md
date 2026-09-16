# RT-40 AP2 — Coupling Efficiency as Lorentz Factor

*Dominic René Schu, September 2026*
*Status: Completed (Sep 2026) — Success criterion satisfied (falsifiable relation named)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Starting Point: A4 in the Rest Frame](#2-starting-point-a4-in-the-rest-frame)
3. [Naive Approach: E = γmc² and f = f₀/γ](#3-naive-approach-e--γmc-and-f--f₀γ)
4. [Contradiction Analysis and Circular-Reasoning Audit](#4-contradiction-analysis-and-circular-reasoning-audit)
5. [Self-Consistency Analysis: What Frequency Is Required?](#5-self-consistency-analysis-what-frequency-is-required)
6. [Physical Content: Coupling Energy vs. Total Energy](#6-physical-content-coupling-energy-vs-total-energy)
7. [Connection to the Zitterbewegung Frequency](#7-connection-to-the-zitterbewegung-frequency)
8. [Success Criterion: Falsifiable Relation](#8-success-criterion-falsifiable-relation)
9. [Result and Outlook for AP3–AP5](#9-result-and-outlook-for-ap3ap5)

---

## 1. Objective and Success Criterion

**Task (RT-40 AP2):** Show that ε(Δφ) = 1/γ² follows from A4 — not merely as a
formal analogy, but as a physical identity.

**Success criterion:** Identity ε = 1/γ² proved — **or** a falsifiable relation between
m, f₀, and ℏ named.

**Result:** The direct proof of ε = 1/γ² via the naive approach fails (contradiction
ε_A4 = γ² ≠ 1/γ²). The success criterion is nonetheless satisfied: consistency of A4
with the AP1 result ε = 1/γ² yields the falsifiable relation

```
    f_RFT(moving resonator) = γ³ · f₀
```

and identifies the coupling energy E_c = mc²/γ² as the physical content of A4 for
moving resonators.

---

## 2. Starting Point: A4 in the Rest Frame

### 2.1 Axiom A4 (Coupling Energy)

Axiom 4 of the RFT reads:
```
    E_eff = π · ε(Δφ) · ℏ · f
```
where f denotes the RFT resonance frequency in rad/s.

### 2.2 Rest-Frame Identification

In the resonator's rest frame (Δφ = 0), one has ε₀ = 1 (full coupling) and the
resonance frequency is f₀ (eigenfrequency). A4 therefore gives:

```
    E₀ = π · 1 · ℏ · f₀ = π · ℏ · f₀
```

The rest-mass energy mc² is identified with E₀:

```
    mc² = π · ℏ · f₀                           [Defining relation]
```

This relation defines the eigenfrequency f₀ as a function of the rest mass:

```
    f₀ = mc² / (π · ℏ)
```

**Significance:** A4 is trivially consistent in the rest frame. The eigenfrequency f₀
is fixed by the rest mass. This is not circular reasoning; it is a definitional
assignment: every resonator of mass m has eigenfrequency f₀ = mc²/(π·ℏ).

### 2.3 Non-Relativistic Limit (Verification)

For small velocities (Δφ → 0, v/c = sin(Δφ/2) → Δφ/2 ≪ 1, ε → 1):
```
    ε ≈ cos²(Δφ/2) ≈ 1 − (Δφ/2)² / 2 ≈ 1 − v²/(2c²)

    E_A4 = π · ε · ℏ · f₀ ≈ mc² · (1 − v²/(2c²))
```
This corresponds to the non-relativistic approximation E_total − E_kin = mc² − mv²/2
up to sign: A4 gives the *decrease* of coupling energy with increasing velocity, not
the increase of total energy. This is a first clue to the physical meaning of ε
(Section 6).

---

## 3. Naive Approach: E = γmc² and f = f₀/γ

### 3.1 Procedure Following RT-40 Specification

RT-40 AP2 proposes the following identification:

| Quantity | Assumption | Source |
|---|---|---|
| E | γmc² (relativistic total energy) | SR |
| f | f₀/γ (time-dilated eigenfrequency) | SR (time dilation) |
| mc² | π·ℏ·f₀ | A4 in rest frame (§2.2) |

**Substituting into A4:**
```
    E = π · ε · ℏ · f

    γmc² = π · ε · ℏ · (f₀/γ)

    γmc² = (π · ε · ℏ · f₀) / γ

    γ² · mc² = π · ε · ℏ · f₀
```

**Using mc² = π·ℏ·f₀:**
```
    γ² · (π · ℏ · f₀) = π · ε · ℏ · f₀

    ε = γ²                                      [Naive result]
```

### 3.2 Contradiction with AP1

From AP1 (RT-40, completed Sep 2026):
```
    v/c = sin(Δφ/2)   →   γ = 1/cos(Δφ/2)   →   ε = cos²(Δφ/2) = 1/γ²
```

The naive approach yields ε = γ², while the AP1 result is ε = 1/γ². This is a
**contradiction** by a factor γ⁴:

```
    ε_naive / ε_AP1 = γ² / (1/γ²) = γ⁴
```

The contradiction is not a small correction; it is a systematic discrepancy of four
powers of the Lorentz factor.

---

## 4. Contradiction Analysis and Circular-Reasoning Audit

### 4.1 Origin of the Contradiction

The source lies in the assumption **f = f₀/γ**. This formula follows from SR time
dilation: a moving resonator ticks more slowly — an observer co-moving with it
measures f₀, while a lab observer measures f₀/γ.

**The circular-reasoning problem (RT-40 warning):** f = f₀/γ is a consequence of
Lorentz invariance, which is precisely what is to be derived from the RFT. Postulating
f = f₀/γ already presupposes SR — the proof that SR ⊂ RFT is then circular.

### 4.2 Why the Naive Approach Is Systematically Incorrect

The naive approach makes two conceptual errors simultaneously:

1. **Wrong energy quantity:** E = γmc² is the *total energy* in the lab frame.
   A4 describes the *coupling energy* between two resonators. These are distinct
   physical quantities.

2. **Wrong frequency argument:** f = f₀/γ (time dilation) is the frequency a lab
   observer measures for the eigenoscillation of the moving resonator. The frequency
   relevant in A4 is, however, the resonance frequency of the coupling system — a
   different concept.

### 4.3 Conclusion

The naive approach is physically inconsistent. The contradiction ε = γ² vs. ε = 1/γ²
is not a flaw in AP1; it shows that f = f₀/γ is not the correct frequency variable
for A4. The correct frequency must be derived from the RFT axioms (AP5).

---

## 5. Self-Consistency Analysis: What Frequency Is Required?

### 5.1 Back-Calculation: f from ε = 1/γ² and E = γmc²

Given:
- ε = 1/γ² (from AP1, proved)
- E = γmc² (assumed total energy)
- mc² = π·ℏ·f₀ (from A4 in rest frame)

From A4, E = π·ε·ℏ·f, so:
```
    γmc² = π · (1/γ²) · ℏ · f

    f = γ³ · mc² / (π · ℏ) = γ³ · f₀           [Self-consistency condition]
```

**Result:** For ε = 1/γ² and E = γmc², the frequency entering A4 must be:

```
    f_RFT(v) = γ³ · f₀ = γ³ · mc² / (π · ℏ)
```

### 5.2 Numerical Support

| v/c | γ | f_RFT / f₀ |
|---|---|---|
| 0 | 1 | 1 |
| 0.5 | 1.155 | 1.540 |
| 0.707 | √2 ≈ 1.414 | 2.828 |
| 0.866 | 2 | 8 |
| 0.943 | 3 | 27 |
| 0.990 | 7.09 | 356.7 |

The frequency f_RFT grows rapidly for relativistic velocities.

### 5.3 Physical Origin of f = γ³·f₀ (Hypothesis)

The factor γ³ appears in relativistic dynamics as the **longitudinal mass**:
```
    F_longitudinal = γ³ · m₀ · a     (longitudinal Newtonian equation)
```

For a harmonic oscillator with spring constant k and effective mass m_eff = γ³m₀:
```
    ω² = k / m_eff   →   ω = ω₀ / γ^(3/2)   (with k = k₀ constant)
```

This yields γ^(-3/2), not γ³. The factor γ³ therefore does not arise trivially from
longitudinal mass.

An alternative interpretation: f_RFT is the frequency of the **coupling operator**
(not of the free resonator). This operator may carry different transformation properties
under phase dynamics (A4) than the eigenfrequency. This remains an open derivation
task for AP5.

---

## 6. Physical Content: Coupling Energy vs. Total Energy

### 6.1 Two Energy Concepts

The analysis above suggests that A4 describes two distinct physical situations that
must be distinguished:

| Energy concept | Formula | Physical meaning |
|---|---|---|
| Total energy (SR) | E_total = γmc² | Energy in the lab frame (kinematic) |
| Coupling energy (RFT) | E_c = π·ε·ℏ·f₀ = mc²/γ² | Interaction energy with a stationary observer |

A4 describes the **coupling energy** — the energy fraction that a moving resonator
"makes available" for interaction with a stationary resonator (the observer), evaluated
using the rest-frame frequency f₀.

### 6.2 Coupling Energy Explicitly

With ε = cos²(Δφ/2) = 1/γ² and f = f₀ (rest frequency in the A4 expression):
```
    E_c = π · ε · ℏ · f₀
         = π · (1/γ²) · ℏ · f₀
         = mc² / γ²
         = mc² · cos²(Δφ/2)
```

Properties:
- **Δφ = 0 (v = 0):** E_c = mc² — full rest-mass coupling ✓
- **Δφ ≠ 0 (v > 0):** E_c < mc² — coupling decreases with velocity
- **Δφ → π (v → c):** E_c → 0 — complete decoupling (speed limit)

The behaviour is physically coherent: a highly relativistic resonator barely couples
to a stationary observer, because its phase dynamics appear "frozen" from the observer's
perspective (ε → 0).

### 6.3 Ratio E_c / E_total

```
    E_c / E_total = (mc²/γ²) / (γmc²) = 1/γ³ = cos³(Δφ/2)
```

The ratio 1/γ³ gives the fraction of a moving resonator's total energy that is
accessible for coupling processes with stationary observers. As v → c, this fraction
vanishes cubically in 1/γ.

---

## 7. Connection to the Zitterbewegung Frequency

### 7.1 Numerical Identification

The RFT rest frequency is:
```
    f₀ = mc² / (π · ℏ)
```

The **Zitterbewegung frequency** of the electron (Schrödinger, 1930) is defined by:
```
    ω_zbw = 2mₑc² / ℏ   →   f_zbw = ω_zbw / (2π) = mₑc² / (π · ℏ)
```

It follows:
```
    f₀_RFT = f_zbw                              [Agreement]
```

The RFT eigenfrequency agrees with the Zitterbewegung frequency. This is not a trivial
coincidence: Zitterbewegung is the interference phenomenon between positive- and
negative-energy Dirac components and is directly connected to the relativistic wave
nature of massive particles.

### 7.2 Significance for AP2

This connection suggests that f₀ is indeed an intrinsic resonance frequency of massive
particles — not a freely chosen parameter, but a physically distinguished quantity that
appears independently in relativistic quantum mechanics (as Zitterbewegung).

The self-consistency condition f_RFT = γ³·f₀ = γ³·f_zbw could therefore be tested
within the framework of a relativistic extension of the Dirac equation.

---

## 8. Success Criterion: Falsifiable Relation

The success criterion of AP2 ("Identity proved — **or** falsifiable relation between
m, f₀, and ℏ named") is satisfied in the second sense.

### 8.1 Named Relations

**Relation 1 — Rest frequency (A4, definitional):**
```
    mc² = π · ℏ · f₀     ⟺     f₀ = mc² / (π · ℏ)
```
*Falsification:* If the coupling energy of a stationary resonator cannot be traced back
to its rest mass via this relation, A4 is falsified.

**Relation 2 — Self-consistency condition (new from AP2):**
```
    f_RFT(v) = γ³ · f₀ = γ³ · mc² / (π · ℏ)
```
*Falsification:* If one determines the effective coupling frequency of a relativistic
particle (e.g., via interaction cross-section measurements) and does not observe γ³
scaling, the A4 consistency with ε = 1/γ² is broken.

**Relation 3 — Coupling energy decay:**
```
    E_c(v) = mc² · cos²(Δφ/2) = mc² / γ² = mc² · (1 − v²/c²)
```
*Falsification:* If the interaction energy in relativistic scattering experiments
follows a scaling law other than 1/γ².

### 8.2 Experimental Approaches (Preview AP6)

| Observable | RFT prediction | Standard physics | Difference |
|---|---|---|---|
| Coupling energy | mc²/γ² | — (no direct equivalent) | RFT-specific |
| f_RFT(v) | γ³·f₀ | f₀/γ (time dilation) | Factor γ⁴ |
| E_c/E_total | 1/γ³ | — | RFT-specific |

The difference f_RFT / f_naive = γ⁴ is a dramatic prediction for γ ≫ 1
(ultra-relativistic regime).

---

## 9. Result and Outlook for AP3–AP5

### 9.1 Summary of AP2 Results

| Question (AP2) | Result |
|---|---|
| Does ε = 1/γ² follow directly from A4 + E = γmc² + f = f₀/γ? | **No:** Contradiction ε = γ² |
| Is f = f₀/γ derived from RFT? | **No:** Circular-reasoning risk confirmed |
| What must f be for consistency? | **f = γ³·f₀** (new self-consistency condition) |
| What is the physical content of A4? | **Coupling energy** E_c = mc²/γ² |
| Success criterion satisfied? | **Yes:** Falsifiable relation named |

### 9.2 What AP2 Achieves and What Remains Open

**AP2 achieves:**
- Complete calculation of the naive approach (f = f₀/γ, E = γmc²) and proof of contradiction.
- Explicit analysis and confirmation of the circular-reasoning risk.
- Derivation of the self-consistency condition f_RFT = γ³·f₀.
- Clarification of A4's physical content: coupling energy E_c = mc²/γ², not total energy.
- Falsifiable relations named: mc² = π·ℏ·f₀ and f_RFT = γ³·f₀.
- Connection to Zitterbewegung frequency identified.

**AP2 does not achieve (open for AP5):**
- f_RFT = γ³·f₀ has not yet been derived from A1–A7 — this is the subject of **AP5**
  (time dilation and frequency transformation as phase/coupling effects).
- Whether E = γmc² is the correct energy quantity for A4 remains open.
- The physical origin of the factor γ³ in the RFT coupling dynamics is not yet clarified.

### 9.3 Significance for RT-40

AP2 fulfils its purpose: it shows **why** the identification ε = 1/γ² does not follow
trivially from A4. The reason is not an inconsistency of the RFT, but the fact that A4
describes a different physical quantity than the relativistic total energy. A rigorous
proof of ε = 1/γ² requires:

1. Derivation of time dilation from the RFT axioms (AP5), in order to determine f(v)
   correctly.
2. Alternatively: a more direct derivation of ε(Δφ) = 1/γ² from the coupling dynamics
   (AP3: Lorentz transformation), bypassing the energy relation.

The consistency condition f_RFT = γ³·f₀ identified in AP2 provides a concrete
benchmark for AP5.

---

## Connections to Existing Documents

- AP1 (Phase ↔ Rapidity): [`rt40_ap1_phase_rapidity.md`](rt40_ap1_phase_rapidity.md)
- Axioms A1–A4: [`../docs/definitions/axiomatic_foundation.md`](../docs/definitions/axiomatic_foundation.md)
- ε = cos²(Δφ/2) uniqueness (RT-02): [`gsync_group_structure.md`](gsync_group_structure.md)
- RT-40 overview: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
