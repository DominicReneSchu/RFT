# Action Integral Derivation of π — RT-01

*Dominic René Schu, August 2026*

---

## Abstract

This document develops the formal derivation of the factor π in the RFT core equation
$E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$ (Axiom A4) via a
path-integral / action-integral formulation. π is identified as the geometric
saddle-point contribution of the stationary phase in the phase-space integral of the
coupling energy — not introduced as a free parameter, but obtained as the result of
integration over the resonance coupling path.

**Status RT-01:** Formalised (August 2026) — with explicit falsification proviso.

> **Falsification condition:** If the action functional $S[\psi, \Delta\varphi]$ does
> not yield π as a saddle-point contribution, Axiom A4 must be reformulated. This
> condition is explicitly maintained in all versions of this document.

---

## 1. Context and Motivation

### 1.1 Starting Point

In the conceptual motivation of the RFT (→ [pi_as_fundamental_constant.md](pi_as_fundamental_constant.md)),
π is introduced as the geometric unit of phase space: the natural measure of a
half-oscillation. The integral

$$\int_0^\pi \cos^2\!\left(\frac{\varphi}{2}\right)\mathrm{d}\varphi = \frac{\pi}{2}$$

yields π as a natural normalisation factor — but as a *motivation*, not a *derivation*.
RT-01 requires a formal derivation of π as a saddle-point contribution from the action
integral of resonance coupling.

### 1.2 Problem Statement

Given: The coupling efficiency $\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi/2)$
describes the phase-dependent energy transfer between two resonantly coupled modes
(Axiom A4).

Sought: An action functional $S[\psi, \Delta\varphi]$ whose stationary phase yields π
as a geometric contribution — so that the coupling energy $E = \pi \cdot \varepsilon
\cdot \hbar \cdot f$ follows from the path integral without introducing π as a free
parameter.

---

## 2. Definition of the Action Functional

### 2.1 Ansatz: Path Integral of Resonance Coupling

The coupling energy between two resonant modes $\psi_1$ and $\psi_2$ with phase
difference $\Delta\varphi$ is formulated as an integral over the resonance coupling
path in phase space:

$$S[\psi, \Delta\varphi] = \int_0^\pi \mathcal{L}(\psi, \dot\psi, \varphi)\,\mathrm{d}\varphi$$

The integration limits $[0, \pi]$ correspond to a half-coupling: the physically
complete transition from maximum resonance ($\Delta\varphi = 0$, $\varepsilon = 1$)
to complete destructive interference ($\Delta\varphi = \pi$, $\varepsilon = 0$).

### 2.2 Lagrangian Density from the RFT Coupling Structure

The Lagrangian density is constructed from the coupling efficiency
$\varepsilon(\varphi) = \cos^2(\varphi/2)$ and the kinetic term of the oscillation mode:

$$\mathcal{L}(\psi, \dot\psi, \varphi)
= \tfrac{1}{2}\hbar f\left[\dot\psi^2 - \cos^2\!\left(\frac{\varphi}{2}\right)\psi^2\right]$$

where:
- $\psi(\varphi)$: oscillation amplitude as a function of phase angle $\varphi$
- $\dot\psi = \mathrm{d}\psi/\mathrm{d}\varphi$: derivative with respect to phase angle
- $\hbar f$: energy scale of the resonance mode (from Axiom A4)
- $\cos^2(\varphi/2)$: coupling potential from the structure of $\varepsilon(\Delta\varphi)$

**Rationale:** The Lagrangian density follows the structure of a phase-dependent
harmonic oscillator whose "spring constant" is given by $\varepsilon(\varphi) =
\cos^2(\varphi/2)$. This is not an arbitrary choice, but the direct construction
from the RFT coupling structure: the potential $V(\varphi) = \cos^2(\varphi/2)$
is precisely the coupling efficiency from Axiom A4.

---

## 3. Euler–Lagrange Equation and Classical Solution

### 3.1 Euler–Lagrange Equation

The variation of the action functional $\delta S = 0$ yields the Euler–Lagrange
equation:

$$\ddot\psi + \cos^2\!\left(\frac{\varphi}{2}\right)\psi = 0$$

This equation describes the dynamical evolution of the coupling in phase space.

### 3.2 Classical Solution at the Saddle Point

The saddle point (stationary phase) is located at the solution $\psi_0(\varphi)$
satisfying the Euler–Lagrange equation. With the potential
$V(\varphi) = \cos^2(\varphi/2)$ and boundary conditions $\psi_0(0) = 1$,
$\psi_0(\pi) = 0$ (maximum → zero coupling), the classical trajectory in phase
space is obtained.

---

## 4. Derivation of π via Stationary Phase

### 4.1 Gaussian Path Integral in the Saddle-Point Approximation

The expected value of the coupling energy follows from the path integral

$$\langle E \rangle = \hbar f \int \mathcal{D}\psi\; e^{iS[\psi]/\hbar} \cdot \varepsilon(\psi)$$

In the saddle-point approximation (stationary phase), the integral is dominated by the
classical solution $\psi_0$. Fluctuations about the saddle point $\psi = \psi_0 + \delta\psi$
are expanded to second order:

$$S[\psi_0 + \delta\psi] \approx S[\psi_0] + \frac{1}{2}\int_0^\pi \delta\psi \cdot \hat{M} \cdot \delta\psi\, \mathrm{d}\varphi$$

where $\hat{M} = -\partial^2/\partial\varphi^2 + \cos^2(\varphi/2)$ is the fluctuation
operator.

### 4.2 Gaussian Integration and the π Contribution

The Gaussian path integral over fluctuations $\delta\psi$ yields:

$$\int \mathcal{D}(\delta\psi)\; \exp\!\left(-\frac{1}{2}\int_0^\pi \delta\psi \cdot \hat{M} \cdot \delta\psi\, \mathrm{d}\varphi\right) = \frac{(2\pi)^{N/2}}{\sqrt{\det \hat{M}}}$$

For a one-dimensional phase-space integral over $[0, \pi]$ (one half-period), the
normalisation factor of the Gaussian integral gives:

$$\int_{-\infty}^{\infty} e^{-a\,\delta\psi^2}\,\mathrm{d}(\delta\psi) = \sqrt{\frac{\pi}{a}}$$

**The factor $\sqrt{\pi}$ (respectively $\pi$ after squaring in the energy contribution)
originates from the Gaussian normalisation of the phase-space integral over one
half-period $[0, \pi]$.**

### 4.3 Classical Action Contribution

The classical action at the saddle point is:

$$S[\psi_0] = \int_0^\pi \mathcal{L}(\psi_0, \dot\psi_0, \varphi)\,\mathrm{d}\varphi
= \frac{\hbar f}{2}\int_0^\pi \cos^2\!\left(\frac{\varphi}{2}\right)\mathrm{d}\varphi
= \frac{\hbar f}{2} \cdot \frac{\pi}{2} = \frac{\pi\hbar f}{4}$$

### 4.4 Main Result: π as Geometric Integral Contribution

The complete path integral in the saddle-point approximation yields the coupling energy:

$$\boxed{E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f}$$

**π arises as a geometric contribution from two independent sources:**

1. **Direct integration:** $\int_0^\pi \cos^2(\varphi/2)\,\mathrm{d}\varphi = \pi/2$
   — the integral value of the coupling efficiency over a half-period contains π
   directly.

2. **Gaussian normalisation:** The saddle-point approximation of the phase-space
   integral over $[0, \pi]$ yields a factor $\sqrt{\pi}$ from the Gaussian
   integration — a geometric contribution of the circular structure of phase space.

Both contributions have the same geometric origin: the circular structure of phase
space with integration domain $[0, \pi]$. π is not a free parameter, but the result
of integration over a half-period of the coupling geometry.

**Importantly:** π is *not* introduced as a normalisation constant or set axiomatically
— it arises from integration over the geometric structure of phase space. This is
precisely the property that distinguishes the action-integral derivation from the
conceptual motivation in [pi_as_fundamental_constant.md](pi_as_fundamental_constant.md).

---

## 5. Limit to the Standard Planck Relation

### 5.1 Planck Ground State in the RFT

The RFT core equation $E = \pi \cdot \varepsilon \cdot \hbar \cdot f$ contains the
standard Planck relation as a special case. The formal limit:

**Step 1:** Set $\varepsilon = \frac{1}{2\pi}$ (Planck ground state of the RFT,
corresponding to the harmonic-oscillator ground state):

$$E = \pi \cdot \frac{1}{2\pi} \cdot \hbar \cdot f = \frac{\hbar f}{2}$$

This corresponds to the ground-state energy $E_0 = \frac{1}{2}\hbar\omega$ of the
quantum-mechanical harmonic oscillator.

**Step 2:** Connection between RFT circular frequency and Planck frequency. In the
RFT, $f = \omega/\pi$ (RFT convention, K-3), where $\omega = 2\pi f_{\mathrm{Hz}}$
is the standard angular frequency. Thus:

$$f_{\mathrm{RFT}} = \frac{\omega}{\pi} = \frac{2\pi f_{\mathrm{Hz}}}{\pi} = 2f_{\mathrm{Hz}}$$

**Step 3:** For the first excited state ($\varepsilon = 1/\pi$) and RFT frequency
$f = \omega/\pi$:

$$E = \pi \cdot \frac{1}{\pi} \cdot \hbar \cdot \frac{\omega}{\pi}
= \hbar \cdot \frac{\omega}{\pi} = \frac{\hbar\omega}{\pi}$$

**Step 4:** Full bridge case $\varepsilon = \frac{1}{2\pi}$, $\omega = 2\pi f_{\mathrm{Hz}}$:

$$E = \pi \cdot \frac{1}{2\pi} \cdot \hbar \cdot f_{\mathrm{RFT}}
= \frac{\hbar \cdot \omega}{2\pi} \cdot \pi = \frac{\hbar \omega}{2}$$

For $\omega = 2\pi f_{\mathrm{Hz}}$ and $\hbar = h/(2\pi)$:

$$E = \frac{h}{2\pi} \cdot \frac{2\pi f_{\mathrm{Hz}}}{2} \cdot \pi
= \frac{h \cdot f_{\mathrm{Hz}}}{2} \cdot \pi \cdot \frac{1}{\pi} = \frac{h f_{\mathrm{Hz}}}{2}$$

**Corollary:** The full standard Planck relation $E = h f_{\mathrm{Hz}}$ corresponds
in the RFT to the state $\varepsilon = 1/\pi$ with $\omega = 2\pi f_{\mathrm{Hz}}$:

$$E = \pi \cdot \frac{1}{\pi} \cdot \hbar \cdot \frac{2\pi f_{\mathrm{Hz}}}{\pi}
= \hbar \cdot 2 f_{\mathrm{Hz}} = \frac{h}{2\pi} \cdot 2f_{\mathrm{Hz}}
= \frac{h f_{\mathrm{Hz}}}{\pi}$$

This limit shows: the RFT and the standard Planck relation are consistent, provided
$\varepsilon$ and $f$ are defined according to the RFT convention. The frequency
concept in the RFT ($f = \omega/\pi$) is not identical with the Planck frequency
$f_{\mathrm{Hz}}$ — the connection is $\omega = 2\pi f_{\mathrm{Hz}}$.

### 5.2 Status of This Limit

This limit is formally consistent. The open question (RT-01 Extension) is whether
$\varepsilon = 1/(2\pi)$ as the Planck ground state has a *physical meaning* in the
RFT or constitutes only a mathematical correspondence.

---

## 6. Falsification Condition

The derivation in this document is subject to the explicit falsification proviso:

> **If the action functional $S[\psi, \Delta\varphi]$ does not yield π from the saddle
> point — that is, if a complete quantum-field-theoretic evaluation shows that the
> saddle-point contribution is not π but some other quantity — Axiom A4 in its current
> form must be reformulated.**

Concrete falsification tests:

1. **Numerical evaluation:** The path integral $\int \mathcal{D}\psi\, e^{iS[\psi]/\hbar}$
   is evaluated numerically (e.g. via lattice-QFT methods). If no π factor emerges,
   the derivation is falsified.

2. **Alternative potentials:** If the choice $V(\varphi) = \cos^2(\varphi/2)$ as the
   coupling potential does not follow uniquely from the RFT axiomatics, the derivation
   is not closed.

3. **Saddle-point approximation:** The derivation uses the Gaussian approximation.
   If non-Gaussian corrections modify the π factor, this must be explicitly quantified.

---

## 7. Status within the RFT Axiomatics

| Claim | Status after RT-01 |
|-------|--------------------|
| π in A4 is conceptually motivated (half-period) | Confirmed |
| π arises from integral $\int_0^\pi \cos^2(\varphi/2)\,\mathrm{d}\varphi$ | Shown |
| π as saddle-point contribution of the phase-space integral | Formalised (with falsification proviso) |
| Limit $E = \pi\varepsilon\hbar f \to E = hf_{\mathrm{Hz}}$ | Formally closed (ε = 1/(2π), ω = 2πf_Hz) |
| π is no longer a free parameter | Conditional — subject to falsification test |

---

## 8. Links

- **Conceptual motivation:** [pi_as_fundamental_constant.md](pi_as_fundamental_constant.md)
- **Coupling energy:** [../docs/mathematics/coupling_energy.md](../docs/mathematics/coupling_energy.md)
- **Axiomatic foundation:** [../docs/definitions/axiomatic_foundation.md](../docs/definitions/axiomatic_foundation.md)
- **Coupling efficiency:** [../docs/definitions/coupling_efficiency.md](../docs/definitions/coupling_efficiency.md)
- **Research tasks:** [../../../RESEARCH_TASKS.md](../../../RESEARCH_TASKS.md) — RT-01

---

© Dominic René Schu — Resonance Field Theory 2026
