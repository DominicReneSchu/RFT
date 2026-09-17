# RT-41 — Axiom A8: Coupling Wave Velocity — Derivation or Irreducible Postulate

*Dominic-René Schu, September 2026*

*Status: ✅ Completed (Sep 2026) — A8 established as an irreducible postulate;
entered in `axiomatic_foundation.md`; axiom system A1–A8 complete.*

---

## Table of Contents

1. [Context and Starting Point](#1-context-and-starting-point)
2. [Central Question](#2-central-question)
3. [AP1 — Dispersion Relation in A1–A7](#3-ap1--dispersion-relation-in-a1a7)
4. [AP2 — Connection to AP4 (c from ε → 0)](#4-ap2--connection-to-ap4-c-from--0)
5. [AP3 — Group-Theoretic Analysis: c in G_sync](#5-ap3--group-theoretic-analysis-c-in-g_sync)
6. [Synthesis: Result A or B?](#6-synthesis-result-a-or-b)
7. [Methodological Guidelines](#7-methodological-guidelines)
8. [Summary and Status](#8-summary-and-status)

---

## 1. Context and Starting Point

In RT-40 AP3 (`de/fakten/theorie/rt40_ap3_lorentz_transformation.md`, §8), the Lorentz transformation was derived under an explicitly stated **bridge assumption B₁**:

> **B₁:** The RFT phase φ(t, x) = kx − ωt is coupled to the spacetime coordinates (t, x) through a coupling wave with phase velocity c = ω/k.

This assumption is **not fully contained** in axioms A1–A7. RT-40 AP3 therefore formulates a minimal axiom extension:

> **A8 (preliminary):** The phase wave of the RFT coupling structure propagates with the velocity c = 1/√(μ₀ε₀).

RT-41 has the task of clarifying the status of this statement:

**Does B₁ (and thus c as a phase velocity) follow from A1–A7 — or is A8 an irreducible postulate?**

The result determines whether the RFT contains the SRT fully from seven axioms, or whether an eighth axiom is required.

---

## 2. Central Question

Does the phase velocity c of the RFT coupling wave follow from A1–A7 — or is it an irreducible postulate (→ A8)?

**Two possible outcomes:**

**Result A (derivation succeeds):** c follows from A1–A7 as a structural consequence. B₁ is not an additional postulate. The RFT contains the SRT fully from seven axioms.

**Result B (derivation fails):** c is not derivable from A1–A7. A8 is formulated as an irreducible postulate: *The phase wave of the RFT coupling structure propagates with velocity c.* The RFT then contains the SRT under eight axioms — analogous to the SRT itself, which posits c as a postulate.

---

## 3. AP1 — Dispersion Relation in A1–A7

### 3.1 Question

What phase velocities does A1 (ψ = A·cos(kx − ωt + φ)) permit? Is ω/k fixed or freely choosable in A1–A7?

### 3.2 Analysis

**A1** postulates the existence of oscillation fields of the form

ψ(t, x) = A · cos(kx − ωt + φ)

with amplitude A, wave number k, angular frequency ω, and phase φ. The phase velocity is v_φ = ω/k.

**Observation:** A1 alone specifies **no** particular dispersion relation ω(k). The phase velocity v_φ = ω/k is a free parameter in A1 — ω and k can take arbitrary positive values independently.

**A3** (quantization) restricts possible frequencies to discrete values, but does not establish a dispersion relation.

**A4** (coupling energy E = π ε(Δφ) ħ f) connects energy with frequency — but does not fix a phase velocity.

**A7** (G_sync-invariance) requires that the coupling structure is invariant under the symmetry group G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ). This group contains scalings (ℝ⁺_×), phase rotations (U(1)), and affine transformations (Aff⁺(ℝ)). Whether it forces a distinguished velocity is investigated in AP3.

**Intermediate result AP1:** The dispersion relation ω/k = c is not explicitly contained in A1–A7. A1 permits arbitrary phase velocities. Fixing the value to c requires additional structure — either through AP2 (connection to the limiting velocity) or AP3 (group structure).

---

## 4. AP2 — Connection to AP4 (c from ε → 0)

### 4.1 Question

RT-40 AP4 derived c as a structural limiting velocity from ε(Δφ) → 0 for Δφ → π. Is this c the same as the phase velocity in B₁?

### 4.2 Analysis of the Limiting Velocity (RT-40 AP4)

In RT-40 AP4 (`de/fakten/theorie/rt40_ap4_lichtgeschwindigkeit_grenzfall.md`) it was shown:

- For Δφ → π, ε(Δφ) = cos²(Δφ/2) → 0.
- This corresponds to complete decoupling of two resonators.
- The limiting velocity c_lim is that relative velocity at which a massive resonator completely decouples.
- c_lim arises as a **structural consequence** of the coupling geometry — not as an empirical parameter.

### 4.3 Comparison with B₁

**B₁** assumes: φ(t, x) = kx − ωt with v_φ = ω/k = c.

Here c is used as the **phase velocity** of a coupling wave — i.e., as the propagation speed of the phase fronts.

**c_lim from AP4** is, by contrast, a **limiting velocity** — the maximum velocity at which coupling is still possible.

### 4.4 Are c_lim and c_φ Identical?

**Argument for identity:**
- In the SRT: the speed of light is both the propagation velocity of electromagnetic waves (phase velocity) and the maximum signal velocity (limiting velocity). Both are structurally the same.
- If the RFT is consistent with the SRT (RT-40 overall result), then c_lim = c_φ should hold.

**Argument against automatic identity:**
- c_lim is a **kinematic** bound (maximum relative motion under preserved coupling).
- c_φ is a **dynamic** property (propagation speed of the phase fronts of the coupling wave).
- Without an additional assumption about the wave equation of the coupling structure, c_lim = c_φ does not follow automatically.

**Finding AP2:** The connection c_lim = c_φ is plausible and consistent with the RT-40 results, but it does **not follow necessarily** from A1–A7. It would retroactively justify B₁ — but only if it is additionally shown that the phase fronts of the coupling wave propagate at exactly c_lim. This requires a statement about the dynamics of the coupling wave that is not contained in A1–A7.

**Intermediate result AP2:** c_lim and c_φ are conceptually distinct. Their equality is consistency-compatible but not provable from A1–A7 alone. B₁ is partially motivated by AP4, but not fully derived.

---

## 5. AP3 — Group-Theoretic Analysis: c in G_sync

### 5.1 Question

Does G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) contain a distinguished velocity? Does the affine component Aff⁺(ℝ) force an invariant phase velocity c?

### 5.2 Structure of G_sync

According to RT-02 (`de/fakten/theorie/gsync_gruppenstruktur.md`), G_sync is the minimal symmetry group of the RFT coupling structure:

G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ)

with:
- **ℝ⁺_×**: Amplitude scalings (A → λA, λ > 0)
- **U(1)**: Global phase rotations (φ → φ + α)
- **Aff⁺(ℝ)**: Orientation-preserving affine transformations of the time axis (t → at + b, a > 0)

### 5.3 Analysis: Does G_sync Force a Phase Velocity?

**Scaling component ℝ⁺_×:** Amplitude scalings do not change k or ω — they do not fix a dispersion relation.

**Phase component U(1):** Global phase rotations shift φ → φ + α — they do not affect the ratio ω/k.

**Affine component Aff⁺(ℝ):** The transformation t → at + b acts on the frequency through ω → ω/a. A simultaneous transformation x → ax + b' (if Aff⁺(ℝ) also acts on position) gives k → k/a — and ω/k = (ω/a)/(k/a) remains invariant. This means: v_φ = ω/k is invariant under simultaneous scaling of space and time, but **no specific value** of v_φ is singled out.

**Key observation:** G_sync is an **internal symmetry group** of the coupling structure — it acts on the phases and amplitudes of resonators, but **not on the spacetime coordinates** (t, x) as independent geometric objects. The connection between phase dynamics and spacetime geometry is precisely what B₁ establishes — and what G_sync alone cannot provide.

**Formal argument:** G_sync contains no subgroup isomorphic to a Lorentz-boost group. The boost group SO(1,1) (hyperbolic rotations) is not contained in G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ). A distinguished invariant velocity (the analog of c in the Lorentz group) is therefore not derivable from G_sync alone.

**Intermediate result AP3:** G_sync does not force a distinguished phase velocity c. The affine component Aff⁺(ℝ) preserves the ratio ω/k but does not fix its value. B₁ does not follow from A7 (G_sync-invariance).

---

## 6. Synthesis: Result A or B?

### 6.1 Summary of the Three Work Packages

| Work Package | Question | Result |
|:-------------|:---------|:-------|
| AP1 | Is ω/k fixed in A1–A7? | No — free parameter |
| AP2 | Does c_φ follow from c_lim (RT-40 AP4)? | Consistent, not provable from A1–A7 |
| AP3 | Does G_sync force a distinguished velocity? | No — G_sync contains no SO(1,1) subgroup |

### 6.2 Conclusion

**Result B obtains:** The phase velocity c of the RFT coupling wave does **not** follow from A1–A7.

The bridge assumption B₁ is an **identification hypothesis** that:
- is not derivable from the dispersion structure of A1 (AP1),
- does not necessarily follow from the limiting velocity of RT-40 AP4 (AP2),
- cannot be derived from the group structure G_sync (AP3).

**A8 is an irreducible postulate** that closes the gap between RFT phase dynamics and spacetime geometry.

### 6.3 Formulation of A8

> **A8 (Coupling Wave Velocity):** The phase wave of the RFT coupling structure propagates with the velocity c = 1/√(μ₀ε₀) in vacuum.

**Properties of A8:**
- **Irreducible:** Does not follow from A1–A7 (RT-41 AP1–AP3).
- **Independent:** No logical redundancy with A1–A7 demonstrable.
- **Consistent:** Compatible with RT-40 AP4 (c_lim = c as structural limiting velocity).
- **Empirically testable:** c = 1/√(μ₀ε₀) is metrologically accessible (Michelson–Morley, modern precision experiments).
- **Analogous to SRT:** The SRT also postulates c as a natural constant — A8 is structurally coherent with the SRT tradition.

### 6.4 Classification

Result B is **not a failure** of the RFT. It is a structurally coherent result:

- The SRT requires two postulates: (1) principle of relativity, (2) constancy of c.
- The RFT under A1–A8: seven internal axioms + A8 (phase velocity c).
- The difference from the SRT: A1–A7 provide a **richer internal structure** (coupling dynamics, ε, G_sync), from which the SRT follows as a limiting case — as soon as A8 establishes the connection to spacetime.

---

## 7. Methodological Guidelines

1. **No circular reasoning:** In AP1–AP3, c was not silently presupposed. The analysis started from A1–A7 and examined whether c as a phase velocity follows.

2. **Distinction between c-concepts:**
   - **(a) c as limiting velocity** (RT-40 AP4, from ε → 0): Structural consequence of the coupling geometry — contained in A1–A7.
   - **(b) c as phase velocity** (B₁): Propagation speed of the phase fronts — **not** contained in A1–A7, requires A8.
   - **(c) c as natural constant** (empirical): c = 299 792 458 m/s — a measurable quantity that anchors A8.

3. **Result B as coherent result:** The SRT also postulates c. An A8 at the RFT level is not a weakness, but a precise localization of the assumption that establishes the connection to spacetime.

4. **Falsification:** If c_RFT (from ε → 0, RT-40 AP4) ≠ c_phys (measured), the entire RT-40/RT-41 structure is empirically refuted.

---

## 8. Summary and Status

| Aspect | Result |
|:-------|:-------|
| Status of B₁ in A1–A7 | Not derivable — free parameter (AP1) |
| c_lim = c_φ? | Consistent, not provable from A1–A7 (AP2) |
| G_sync forces c? | No — no SO(1,1) subgroup (AP3) |
| Result | **B: A8 is an irreducible postulate** |
| A8 formulated? | Yes — § 6.3 |
| Next steps | A8 entered in `axiomatic_foundation.md` (Sep 2026) — completed |

**Deliverables of this document:**
- ✅ AP1–AP3 fully analyzed
- ✅ Result B documented
- ✅ A8 formally formulated
- ✅ A8 entered in `axiomatic_foundation.md` (AP4, completed Sep 2026)
- ✅ DE source document: `de/fakten/theorie/rt41_axiom_a8_kopplungswelle.md` (present)

**Connection to existing documents:**
- RT-40 AP3: `de/fakten/theorie/rt40_ap3_lorentz_transformation.md` §8 (starting point)
- RT-40 AP4: `de/fakten/theorie/rt40_ap4_lichtgeschwindigkeit_grenzfall.md` (c as limiting velocity)
- RT-02: `de/fakten/theorie/gsync_gruppenstruktur.md` (G_sync structure)
- RT-36: `de/fakten/theorie/a5_vektorialitaet_herleitung.md` (model: irreducible postulate)
- Axiomatic Foundation: `de/fakten/docs/definitionen/axiomatische_grundlegung.md` / `en/facts/docs/definitions/axiomatic_foundation.md`
