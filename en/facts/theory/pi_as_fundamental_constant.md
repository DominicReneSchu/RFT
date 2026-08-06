# π and e as Fundamental Constants of Space — The Founding Idea of RFT (RT-01a)

*Dominic René Schu, August 2026*
*Status: ✅ Complete (Aug 2026)*

---

## Abstract

This document records the philosophical-mathematical founding idea from which the
Resonance Field Theory (RFT) emerged: the observation that π and e are not
"irrational numbers" in any sense that reflects a property of nature, but rather
artefacts of an arbitrary decimal representation — and that treating them as
geometric fundamental constants of phase space provides the conceptual foundation
for Axiom A4 and the vectorial nature of energy (A5).

RT-01a provides the **philosophical-mathematical prerequisite** for RT-01: it
formalises the decimal-artefact argument, establishes the justification for treating
π as a geometric unit, and explains why the vectoriality inconsistency of standard
physics is the physical motivation for A5 as an irreducible postulate — without
deriving A5.

The formal derivation of the factor π in the action integral (the *necessity*, not
merely the *justification*) is the subject of RT-01.

---

## 1. The Decimal Artefact Argument

### 1.1 π in the Decimal System

The number π has a non-terminating, non-repeating decimal representation:
3.14159265… The standard characterisation is that π is "irrational" — it cannot
be expressed as the ratio of two integers.

This statement is mathematically correct. What is frequently overlooked, however,
is that it is a statement about the **representation** of π in a particular number
system — not about π itself as a physical quantity.

**The circumference of a circle with radius 1 is a physically exact, finite and
measurable quantity.** A circle of radius 1 has a circumference that can be
measured to any desired physical precision. The measurement always yields the same
value. The infinity of the decimal expansion 3.14159… is not a property of the
circumference — it is a property of mapping that quantity into the decimal system.

### 1.2 The Decimal System as an Arbitrary Encoding

The decimal system uses base 10 — a number with no distinguished role in nature
(it reflects the count of human fingers). In a number system that uses π itself as
a base, π = 10 (in that system) would be a finite, rational representation.

**The irrationality of π is not a natural phenomenon; it is an artefact of the
arbitrary base-10 encoding.**

This is not a new observation — it is well-known within the theory of numeral
systems. The RFT draws a physical consequence from it: if π is not intrinsically
"irrational" but merely appears so due to our representational convention, then
treating π as a fundamental unit — a primordial constant of space — is both
meaningful and physically motivated.

### 1.3 Formal Theorem: Representational Relativity of π

The decimal-artefact argument can be stated precisely as a structural claim:

> **Theorem (Representational Relativity of π):** Let $b > 0$ be real and $b \neq 1$.
> In a positional system with base $b$, $\pi$ admits a finite or periodic expansion
> if and only if $b$ and $\pi$ are rationally commensurate. In particular: in the
> positional system with base $b = \pi$, we have $\pi = 1 \cdot b^1 = (10)_\pi$ —
> a finite, single-digit representation.

The three-step structure of the argument:

1. **π is an exact and finite physical quantity:** The circumference of a circle
   with $r = 1$ is a well-defined, measurable value, independent of any
   representational convention.
2. **The decimal representation is an encoding, not a property of the quantity:**
   The expansion 3.14159… results from projecting the physical quantity into a
   base-10 number system. It does not describe the quantity completely; it encodes
   it within a particular representational frame.
3. **Therefore, π is rationally usable in a natural unit system for circular
   geometry:** The apparent irrationality is a representational artefact — it
   vanishes as soon as the number system is adapted to the geometric structure.

**Scope limitation:** The argument ends here. It establishes the *justification* for
treating π as a geometric unit — not the physical *necessity*. The physical
necessity — why π *must* appear in A4 — is provided by RT-01.

### 1.4 Parallel with Other Natural Constants

Physics routinely employs natural unit systems in which fundamental constants take
the value 1:

- Planck units: $c = \hbar = G = k_B = 1$
- Geometric units: $c = G = 1$

Why not also: π = 1 as the natural unit of circular geometry?

In such a system, π would no longer be an irrational number but rather the
definition of the unit for cyclic completeness — analogous to how 1 metre defines
a unit of length. Circular geometry carries its own natural unit, and that unit
is π.

---

## 2. π as a Geometric Fundamental Constant of Phase Space

### 2.1 π as the Measure of a Half-Oscillation

A complete oscillation period runs from $0$ to $2\pi$ in radian measure. A half
period — a physically significant unit representing, for example, the reversal of
a motion or the reaching of maximum amplitude — runs from $0$ to $\pi$.

**π is the natural measure of a half-oscillation** — not as an arbitrarily chosen
unit, but as a geometric property of circular structure itself.

In the RFT, the phase interval $[0, \pi]$ corresponds precisely to a half-coupling:
the transition from full resonance ($\Delta\varphi = 0$, $\varepsilon = 1$) to
complete destructive interference ($\Delta\varphi = \pi$, $\varepsilon = 0$). The
energy of a fully coherent resonance state therefore normalises naturally to π.

### 2.2 Consequence for A4

Axiom A4 states:

$$E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$$

The factor π in this equation is not an arbitrarily chosen numerical constant.
It is the **natural normalisation** of the coupling energy to the geometry of the
circle: a fully coherent resonance coupling ($\varepsilon = 1$) spans exactly one
half-period, and π is the measure of that half-period.

The integral

$$\int_0^\pi \cos^2\!\left(\frac{\varphi}{2}\right)\mathrm{d}\varphi = \frac{\pi}{2}$$

produces π as the natural normalisation factor when the coupling efficiency
$\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi/2)$ is integrated over a complete
half-period. This integral serves as *motivation*, not *derivation* — the formal
derivation is provided by RT-01.

→ **Formal derivation:** [action_integral_pi_derivation.md](action_integral_pi_derivation.md)
(RT-01, August 2026)

### 2.3 Status of This Claim

The π argument is formulated here as a **conceptual motivation**, not a formal proof.
The claim is:

> If π is understood as a phase-space constant (the geometric unit of the circle),
> the factor π in A4 loses its status as a free numerical postulate and acquires
> the status of a geometric necessity.

The formal derivation — the proof that π under this treatment emerges from physics
itself as the saddle-point contribution of the action integral — is the subject of
RT-01.

---

## 3. Two-Level Argument: RT-01a and RT-01 as a Consistent Unit

The relationship between RT-01a (conceptual-mathematical) and RT-01 (physical-formal)
is as follows: the two levels are not mutually exclusive but interlocking.

| Level | Document | Question | Result |
|-------|----------|----------|--------|
| **Level 1 (RT-01a)** | `pi_as_fundamental_constant.md` | *Why may π be treated as a unit?* | Decimal artefact: π is representation-relative — irrationality is not a natural phenomenon |
| **Level 2 (RT-01)** | `action_integral_pi_derivation.md` | *Why must π appear in A4?* | π is the saddle-point contribution of the action integral $S[\psi,\Delta\varphi]$ over the half-period $[0,\pi]$ |

**Level 1 (RT-01a)** establishes the *justification* for treating π as a geometric
unit: the apparent problem of irrationality dissolves once it is recognised as a
representational artefact. This opens the conceptual space for treating π as a
natural normalisation unit.

**Level 2 (RT-01)** shows that π under this treatment follows from physics itself:
the stationary phase of the action integral of resonance coupling has π as its
geometric contribution — independently of any postulated normalisation choice.

**The two-level structure** ensures that π in A4 is doubly secured: conceptually
(representational relativity) and formally (action-integral saddle point). Neither
level alone is complete: RT-01a without RT-01 remains mere motivation; RT-01
without RT-01a would appear as an unmotivated formal trick.

---

## 4. Connection to G_sync and the Minimality Principle (RT-02)

### 4.1 The k=1 Representation of U(1)

RT-02 (group structure of G_sync) shows: the coupling efficiency
$\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi/2)$ follows uniquely from the
**k=1 representation** of U(1) ⊂ G_sync. The k=1 representation is the
*fundamental* (minimal) irreducible representation — all other representations
(k=2, 3, …) yield higher-harmonic couplings not observed in experiment.

### 4.2 Structural Equivalence of Minimality Principles

The minimality principle in RT-02 and the founding idea of RT-01a are structurally
equivalent:

> **The k=1 representation of U(1) is the minimal representation** — analogously,
> π is the minimal geometric unit of the circle: the measure of the half-oscillation,
> below which no complete geometric structure exists.

Formally:

- RT-01a: π = minimal geometric unit of the circle (half-period $[0,\pi]$)
- RT-02 (k=1): $\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi/2)$ =
  minimal irreducible representation of phase rotation in U(1)

Both minimality requirements meet in the integral

$$\int_0^\pi \cos^2\!\left(\frac{\varphi}{2}\right)\mathrm{d}\varphi = \frac{\pi}{2}$$

which contains both the normalisation measure (π, from RT-01a) and the coupling
form ($\cos^2(\Delta\varphi/2)$, from the k=1 representation, RT-02).

The convergence of both principles is not coincidental: it reflects the geometric
self-consistency of the RFT axiomatics. Both paths — the conceptual-mathematical
(RT-01a) and the group-theoretic (RT-02) — enforce the same structure.

→ **Group-theoretic proof:** [gsync_group_structure.md](gsync_group_structure.md) (RT-02)

---

## 5. Internal Inconsistency in Standard Physics: The Vectorial Nature of Energy

### 5.1 The Core Problem

Standard physics treats energy as a scalar — a quantity with no directional
property. This convention is, however, not entirely internally consistent, as
three separate structures demonstrate:

**Mechanics:** Work is defined as

$$E = \vec{F} \cdot \vec{s}$$

the scalar product of two vectors. By definition this yields a scalar — but only
because the directional information is fully collapsed by the projection. The
deeper question is: why does the directional information collapse completely? Is
this a fact of nature or a modelling choice?

**Torque:** Torque is defined as

$$\vec{M} = \vec{r} \times \vec{F}$$

with unit N·m = J (joule) — identical to the unit of energy. Yet torque is a
**vector**, not a scalar. Standard physics assigns torque and energy the same unit
while treating them as different types of quantity: one vectorial, the other
scalar. This asymmetry is not derived from a deeper structure — it is a convention.

**Quantum mechanics / Spin:** Spin is an intrinsic vectorial property of quantum
particles without classical analogue. It carries energy (Zeeman effect,
hyperfine structure) and is inseparably linked to spatial orientation. Spin obeys
an algebra (SU(2)) that corresponds to the geometric structure of rotations.

**Special relativity:** In the Lorentz four-vector

$$(E/c,\, \vec{p})$$

energy already appears as the temporal component of a vectorial quantity. Energy is not
independent of direction (momentum) in the relativistic formalism — it is part
of a covariant four-vector.

### 5.2 The Internal Inconsistency

Standard physics treats energy as a scalar, yet its own structures contradict this
in three independent contexts:

| Context | Structure | Vectorial character of energy |
|---------|-----------|-------------------------------|
| Torque | M⃗ = r⃗ × F⃗, unit J | Implicitly present |
| Spin | SU(2) algebra, energy contributions (Zeeman) | Intrinsically vectorial |
| Lorentz four-vector | (E/c, p⃗) | Energy as vector component |

This inconsistency is not a proof of the RFT — it is an **open question** in the
foundations of physics that the RFT takes as its starting point in developing an
alternative model.

### 5.3 Clarification: No Refutation of Standard Physics

The inconsistency described here is not to be understood as a refutation of
standard physics. The established formalisms (classical mechanics, QM, GR) are
internally consistent in the sense that they yield non-contradictory predictions.
The inconsistency lies at a deeper conceptual level: what is energy ontologically —
a scalar quantity or a quantity with geometric structure?

The RFT makes an explicit modelling decision: energy has direction in the resonance
field (A5). This decision is an axiom, not a derivation.

---

## 6. A5 Placement: Vectoriality Inconsistency as Motivation, not Derivation

### 6.1 A5 and its Current Status

Axiom A5 states:

$$\vec{E} = E_{\text{eff}} \cdot \hat{e}(\Delta\varphi, \nabla\Phi)$$

A5 is not derived from A1–A4. It is an independent, irreducible postulate
establishing the vectorial character of energy in the resonance field.

**Complete (RT-36, Aug 2026):** RT-36 has shown that A5 is an irreducible postulate
(possibility B). The D-generator of G_sync yields $\delta_D \Phi \propto \partial_t \Phi$
(not $\nabla\Phi$); in general $\delta_D(\nabla\Phi/|\nabla\Phi|) \neq 0$.
G_sync operates on the internal phase space (frequencies, phases, time) — not on
spatial directions. The directional unit $\hat{e}(\Delta\varphi, \nabla\Phi)$ is
therefore group-theoretically irreducible and cannot be derived from G_sync.

### 6.2 The Conceptual Motivation

The vectoriality inconsistency of standard physics (§5) is the **physical motivation**
for A5 as an irreducible postulate — it is not a derivation of A5.

- The structures torque, spin, and Lorentz four-vector show that standard physics
  is not fully internally consistent in its scalar treatment of energy.
- The RFT takes this inconsistency as its starting point and postulates A5: energy
  has a directional structure in the resonance field.

**Precise formulation:** The vectoriality inconsistency *motivates* A5 — it does
not *compel* it. A5 is a modelling decision of the RFT that is justified by the
empirical picture of standard physics but is not logically derivable from it alone.

### 6.3 A5 Status: Complete

A5 is formally complete (RT-36, Aug 2026) as an irreducible postulate. The
conceptual justification basis is the vectoriality inconsistency in torque, spin,
and Lorentz four-vector (this document, §5).

Open question: A consistency proof with the energy-momentum tensor of General
Relativity remains outside the current formal framework.

→ Full analysis: [a5_vectoriality_derivation.md](a5_vectoriality_derivation.md) (RT-36)

---

## 7. e as the Fundamental Constant of Dynamic Coupling

### 7.1 Euler's Number in the Decimal System

Euler's number $e = 2.71828\ldots$ shares with π the property of being irrational
and transcendental in the decimal system. The same decimal-artefact argument
applies: the infinity of the decimal expansion is not a natural phenomenon but a
consequence of the base-10 encoding. In a number system with base $e$, we have
$e = (10)_e$ — finite and rationally representable.

### 7.2 e as the Fundamental Constant of Dynamic Equilibrium

Formally: all processes of the form

$$\dot{x}(t) = \lambda \, x(t), \quad \lambda \in \mathbb{C}$$

have as their **unique analytic solution**

$$x(t) = x_0 \cdot e^{\lambda t}.$$

This is not coincidental and not merely definitional. The requirement that the rate
of change $\dot{x}$ be encoded in the solution $x$ itself — i.e. that the solution
carries its own rate as a structural property — uniquely forces the base $e$.
Formally: let $f(t)$ be differentiable and $f'(t) = \lambda f(t)$. Then separation
of variables and integration give:

$$\int_{x_0}^{x} \frac{\mathrm{d}u}{u} = \lambda t \implies \ln\!\left(\frac{x}{x_0}\right) = \lambda t \implies x(t) = x_0 \cdot e^{\lambda t}.$$

The base $e$ is the unique base satisfying this self-similarity property.

**Analogy with π:** π is the measure of static circular geometry — the unit of
spatial structure. $e$ is the measure of self-similar dynamics — the unit of
temporal structure. Together they capture the fundamental structures of phase space:
space (π) and dynamics ($e$).

**In the RFT:** Resonance coupling is a self-similar process — the rate at which
energy is exchanged between two resonantly coupled systems is proportional to the
existing coupling. $e$ is therefore not "an irrational number" but rather the
**fundamental constant of dynamic equilibrium** — the natural base for all
self-similar coupling processes.

### 7.3 Relation to the Natural Unit System

Analogously to π (§1.4), $e$ can be understood as a base quantity of a natural
unit system: in a system that uses $e$ as the unit of dynamics, all equations of
the form $\dot{x} = \lambda x$ take their simplest possible form. A complete
formalisation of a natural unit system $\{\pi, e, \hbar\}$ (analogous to Planck
units) is declared as an open step in §9.

### 7.4 Status

The formal property — $e$ as the unique base of self-similarity dynamics — is
complete (§7.2). What is formally **not yet** shown:

- $e$ has not yet been integrated into the axiomatics (A1–A7).
- The connection between $e$ as a coupling constant and the specific dynamics of
  resonance coupling in the RFT is conceptually motivated but not yet formulated
  as an axiom or corollary.

This is declared as an open step — not as a gap that invalidates existing results,
but as the next formalisation task.

---

## 8. Consequence for the Interpretation of A4

Taken together, the founding idea yields the following interpretation of the
core equation:

$$E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$$

| Factor | Standard interpretation | Interpretation from the founding idea |
|--------|------------------------|---------------------------------------|
| $\pi$ | Numerical constant (irrational) | Geometric unit of phase space (measure of the half-oscillation, §2; formally derived in RT-01) |
| $\varepsilon(\Delta\varphi)$ | Phenomenological coupling parameter | k=1 representation of U(1) ⊂ G_sync — uniquely determined by representation theory (RT-02) |
| $\hbar$ | Action quantum (Planck constant / 2π) | Action quantum — links energy and frequency |
| $f$ | Resonance frequency of the system | Resonance frequency — to be determined independently (open: RT-01, RT-03) |

The equation thus describes: **Energy arises from complete phase coupling,
normalised to the geometry of the circle (π), modulated by the effective coupling
strength (ε), scaled by the universal action quantum (ℏ) and the system frequency
(f).**

In this reading, π is not an arbitrary number in the prefactor — it is the
normalisation unit of the space in which coupling occurs.

---

## 9. Optional Outlook: Natural Unit System {π, e, ℏ}

As a conceptual outlook: analogously to Planck units ($c = \hbar = G = k_B = 1$),
a natural unit system can be described that uses the RFT fundamental constants as
base quantities:

$$\pi = 1, \quad e = 1, \quad \hbar = 1$$

In this system, Axiom A4 takes the particularly simple form:

$$E = \varepsilon(\Delta\varphi) \cdot f$$

and the coupling efficiency $\varepsilon = \cos^2(\Delta\varphi/2)$ is the only
remaining dimensionless structure. The Lorentz factor of the half-period integral
would equal 1/2.

**Status:** This description is conceptually consistent but not yet formally
elaborated. In particular, the relationship between $e$ (dynamics base) and π
(geometry base) within the joint unit system has not yet been established as a
formal corollary of the axiomatics. This is declared as an open formalisation step.

---

## 10. Open Formalisation Steps

| Step | Content | Status | Reference |
|------|---------|--------|-----------|
| Action-integral derivation | π as saddle-point contribution of the stationary phase in the path integral | **✅ Complete (Aug 2026)** | [action_integral_pi_derivation.md](action_integral_pi_derivation.md) (RT-01) |
| Decimal artefact (formal) | π and e as rational base quantities in a natural unit system — three-step argument formalised | **✅ Complete (Aug 2026)** | This document, §1; (RT-01a) |
| π as phase-space constant | Connection between decimal artefact and action-integral result | **✅ Formally closed (Aug 2026)** | Two-level argument §3; RT-01a + RT-01 |
| Derivation of A5 | Directional unit $\hat{e}$ from phase-space geometry — result: irreducible postulate (possibility B) | **✅ Complete (Aug 2026)** — A5 is irreducible postulate; group-theoretically not derivable from G_sync (RT-36) | [a5_vectoriality_derivation.md](a5_vectoriality_derivation.md) (RT-36) |
| e as fundamental constant | Self-similarity property formally shown; analogy with π as structural unit elaborated | **✅ Conceptually complete, formally as far as possible (Aug 2026)** | §7 of this document |
| Frequency definition | Independent determination of $f$ without reference to A4 | Open | RT-01, RT-03 |
| e in the axiomatics | Integration of Euler's number as a coupling constant in A1–A7 | Open | — |
| Natural {π, e, ℏ} unit system | Formal elaboration as a corollary of the axiomatics | Open | §9 of this document |

---

*Related:* [Coupling Energy](../docs/mathematics/coupling_energy.md) |
[Axiomatic Foundation](../docs/definitions/axiomatic_foundation.md) |
[Coupling Efficiency](../docs/definitions/coupling_efficiency.md) |
[Action-Integral Derivation](action_integral_pi_derivation.md) (RT-01) |
[G_sync Group Structure](gsync_group_structure.md) (RT-02) |
[A5 Vectoriality](a5_vectoriality_derivation.md) (RT-36) |
[RESEARCH_TASKS.md](../../../RESEARCH_TASKS.md) |
[PEER_REVIEW_READINESS.md](../../../PEER_REVIEW_READINESS.md)
