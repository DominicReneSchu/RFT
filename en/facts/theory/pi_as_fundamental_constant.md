# π and e as Fundamental Constants of Space — The Founding Idea of RFT

*Dominic René Schu, July 2026*

---

## Abstract

This document records the philosophical-mathematical founding idea from which the
Resonance Field Theory (RFT) emerged: the observation that π and e are not
"irrational numbers" in any sense that reflects a property of nature, but rather
artefacts of an arbitrary decimal representation — and that treating them as
geometric fundamental constants of phase space provides the conceptual foundation
for Axiom A4 and the vectorial nature of energy (A5).

This line of reasoning is not yet formally complete. What is presented here is a
conceptual motivation that precedes and guides the formal derivation via the
action integral (RT-01).

---

## 1. The Decimal Artefact Argument

### 1.1 π in the Decimal System

The number π has a non-terminating, non-repeating decimal representation:
3.14159265… The standard characterisation is that π is "irrational" — it cannot
be expressed as the ratio of two integers.

This statement is mathematically correct. What is frequently overlooked, however,
is that it is a statement about the *representation* of π in a particular number
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

### 1.3 Parallel with Other Natural Constants

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

Formally, the integral
$$\int_0^\pi \cos^2\!\left(\frac{\varphi}{2}\right)\mathrm{d}\varphi = \frac{\pi}{2}$$
produces π as the natural normalisation factor when the coupling efficiency
$\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi/2)$ is integrated over a complete
half-period. This integral is described in the manuscript as a *motivation*, not a
*derivation* — the formal derivation via the action integral remains open (RT-01).

### 2.3 Status of This Claim

It is explicitly noted that the π argument is formulated here as a **conceptual
motivation**, not a formal proof. The claim is:

> If π is understood as a phase-space constant (the geometric unit of the circle),
> the factor π in A4 loses its status as a free numerical postulate and acquires
> the status of a geometric necessity.

Whether and how this can be formally derived is the subject of RT-01
(action-integral derivation of π).

---

## 3. Internal Inconsistency in Standard Physics: The Vectorial Nature of Energy

### 3.1 The Core Problem

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

**Special relativity:** In the Lorentz four-vector $(E/c,\, \vec{p})$, energy
already appears as the temporal component of a vectorial quantity. Energy is not
independent of direction (momentum) in the relativistic formalism — it is part
of a covariant four-vector.

### 3.2 The Internal Inconsistency

Standard physics treats energy as a scalar, yet its own structures contradict this
in three independent contexts:

| Context | Structure | Vectorial character of energy |
|---------|-----------|-------------------------------|
| Torque | $\vec{M} = \vec{r} \times \vec{F}$, unit J | Implicitly present |
| Spin | SU(2) algebra, energy contributions (Zeeman) | Intrinsically vectorial |
| Lorentz four-vector | $(E/c, \vec{p})$ | Energy as vector component |

This inconsistency is not a proof of the RFT — it is an **open question** in the
foundations of physics that the RFT takes as its starting point in developing an
alternative model.

### 3.3 Clarification: No Refutation of Standard Physics

It is explicitly noted that the inconsistency described here is not to be
understood as a refutation of standard physics. The established formalisms
(classical mechanics, QM, GR) are internally consistent in the sense that they
yield non-contradictory predictions. The inconsistency lies at a deeper conceptual
level: what is energy ontologically — a scalar quantity or a quantity with
geometric structure?

The RFT makes an explicit modelling decision: energy has direction in the resonance
field (A5). This decision is an axiom, not a derivation — but it is motivated by
the conceptual inconsistency described above.

---

## 4. Spin and Vectoriality as Motivation for A5

### 4.1 A5 and its Current Justification

Axiom A5 states:
$$\vec{E} = E_{\text{eff}} \cdot \hat{e}(\Delta\varphi, \nabla\Phi)$$

In the current presentation, A5 is not derived from A1–A4. It is an independent
axiom postulating the vectorial character of energy.

### 4.2 The Conceptual Motivation

If π encodes the geometry of phase space (Section 2) and energy is understood as
a vectorial quantity in that space, A5 follows conceptually as the directional
component of the coupling energy:

- The scalar coupling energy $E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$
  (A4) gives the magnitude.
- The direction $\hat{e}(\Delta\varphi, \nabla\Phi)$ follows from the geometry of
  phase space: it points in the direction in which the phase coupling propagates.

This is analogous to the relationship between work and force vector:
$W = \vec{F} \cdot \vec{s}$ gives only the magnitude — the force vector $\vec{F}$
itself has direction. A5 claims that energy in the resonance field likewise
possesses a directional property, just as force does in mechanics.

**Spin** as an empirical phenomenon points independently in the same direction:
quantum systems naturally exhibit a vectorial energy structure (Zeeman splitting,
magnetic moment) that cannot be reduced to a purely scalar energy concept.

### 4.3 What Remains Formally Open

The claim that A5 "follows" from the π-as-primordial-constant argument is
conceptually plausible but not yet formally complete. Open questions include:

- A group-theoretic framework deriving the directional unit
  $\hat{e}(\Delta\varphi, \nabla\Phi)$ from the geometry of phase space
  (connection to RT-02)
- A consistency proof with the energy-momentum tensor of General Relativity

---

## 5. e as the Fundamental Constant of Dynamic Coupling

### 5.1 Euler's Number in the Decimal System

Euler's number $e = 2.71828\ldots$ shares with π the property of being irrational
and transcendental in the decimal system. The same decimal-artefact argument
applies: the infinity of the decimal expansion is not a natural phenomenon but a
consequence of the base-10 encoding.

### 5.2 e as the Fundamental Constant of Dynamic Equilibrium

$e$ appears in all growth and decay processes that are proportional to their own
state — that is, in all processes of the form $\dot{x} = \lambda x$. The solution
is always $x(t) = x_0 \cdot e^{\lambda t}$.

**In the RFT:** Resonance coupling is such a process — the rate at which energy is
exchanged between two resonantly coupled systems is proportional to the existing
coupling. $e$ is therefore not "an irrational number" but rather the **fundamental
constant of dynamic equilibrium** — the natural base for all self-similar coupling
processes.

### 5.3 Status

The argument for $e$ as a fundamental constant is analogous to the π argument —
conceptually motivated, but not yet formally integrated into the axiomatics of the
RFT. This remains an open formalisation step.

---

## 6. Consequence for the Interpretation of A4

Taken together, the founding idea yields the following interpretation of the
core equation:

$$E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$$

| Factor | Standard interpretation | Interpretation from the founding idea |
|--------|------------------------|---------------------------------------|
| $\pi$ | Numerical constant (irrational) | Geometric unit of phase space (measure of the half-oscillation) |
| $\varepsilon(\Delta\varphi)$ | Phenomenological coupling parameter | Projection of vectorial coupling energy onto the coupling axis |
| $\hbar$ | Action quantum (Planck constant / 2π) | Action quantum — links energy and frequency |
| $f$ | Resonance frequency of the system | Resonance frequency — to be determined independently (open: RT-01, RT-03) |

The equation thus describes: **Energy arises from complete phase coupling,
normalised to the geometry of the circle (π), modulated by the effective coupling
strength (ε), scaled by the universal action quantum (ℏ) and the system frequency
(f).**

In this reading, π is not an arbitrary number in the prefactor — it is the
normalisation unit of the space in which coupling occurs.

---

## 7. Open Formalisation Steps

| Step | Content | Status | Reference |
|------|---------|--------|-----------|
| Action-integral derivation | π as saddle-point contribution of the stationary phase in the path integral | Open | RT-01 |
| Decimal artefact (formal) | π and e as rational base quantities in a natural unit system | Conceptual | RT-01a |
| Derivation of A5 | Directional unit $\hat{e}$ from phase-space geometry | Open | RT-02 |
| Frequency definition | Independent determination of $f$ without reference to A4 | Open | RT-01, RT-03 |
| e in the axiomatics | Integration of Euler's number as a coupling constant | Open | — |

---

*Related:* [Coupling Energy](../docs/mathematics/coupling_energy.md) |
[Axiomatic Foundation](../docs/definitions/axiomatic_foundation.md) |
[RESEARCH_TASKS.md](../../../RESEARCH_TASKS.md) |
[PEER_REVIEW_READINESS.md](../../../PEER_REVIEW_READINESS.md)
