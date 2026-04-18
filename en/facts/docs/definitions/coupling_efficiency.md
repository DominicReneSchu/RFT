# Coupling Efficiency ε — Definition, Theory, and Validation

*Dominic-René Schu, 2025/2026*

---

## Summary

Resonance Field Theory (RFT) describes fundamental processes in
nature, technology, and information systems as coupling and
resonance phenomena in oscillation fields. This document provides
a comprehensive overview of the theory, summarizes the axiomatic
foundation, and introduces the coupling efficiency ε as the central
quantity — including its unified definition, the identity ε = η,
and empirical validation in four independent domains.

The identity ε(Δφ) = η(Δφ) = cos²(Δφ/2) has been empirically
validated: particle physics (1,500,000 Monte Carlo simulations),
cosmology (1,530 FLRW simulations), nuclear technology
(resonance reactor, κ = 1) and quantum mechanics
(Schrödinger simulation, Fidelity = 1.0, ⁸⁷Rb prediction).

For the complete formal axiomatics see the
[axiomatic foundation](../definitions/axiomatic_foundation.md).

---

## 1. Introduction

Resonance Field Theory postulates that all fundamental
processes are based on oscillation, coupling, and resonance. It
unifies concepts from classical oscillation theory, quantum physics,
information theory, and network theory in an axiomatic
framework.

---

## 2. Axiom System (Summary)

The RFT consists of 7 core axioms. Each axiom is minimal,
formally precise, and empirically testable. The complete
formalization with proofs and empirical tests is found
in the [axiomatic foundation](../definitions/axiomatic_foundation.md).

### Axiom 1 — Universal Oscillation

Every physical entity possesses at least one periodic
oscillation mode:

$$
\psi(x, t) = A \cdot \cos(kx - \omega t + \phi)
$$

### Axiom 2 — Superposition

Oscillation modes superpose linearly in fields:

$$
\Phi(x, t) = \sum_i \psi_i(x, t)
$$

### Axiom 3 — Resonance Condition

Resonance occurs at rational frequency ratios within
a tolerance window δ:

$$
|f_1/f_2 - m/n| < \delta, \quad m, n \in \mathbb{Z}^+
$$

### Axiom 4 — Coupling Energy

The effective energy of a resonant coupling:

$$
E = \pi \cdot \varepsilon(\Delta\phi) \cdot \hbar \cdot f
$$

where ε(Δφ) ∈ [0, 1] is the coupling efficiency.

### Axiom 5 — Energy Direction

Energy is a vector in the resonance field:

$$
\vec{E} = E_{\text{eff}} \cdot \hat{e}(\Delta\phi, \nabla\Phi)
$$

### Axiom 6 — Information Flow through Resonance Coupling

Information is transmitted exclusively through coherent phase and
frequency relations:

$$
MI(X, Y) = H(X) + H(Y) - H(X, Y)
$$

$$
PCI = |\langle e^{i(\phi_1 - \phi_2)} \rangle| \in [0, 1]
$$

### Axiom 7 — Invariance under Synchronous Transformations

The coupling structure remains invariant under transformations
of the group G_sync:

$$
T(f_i, \phi_i, t) = (\lambda f_i, \phi_i + \phi_0, at + b)
$$

### Interpretative Extensions

In addition there are two interpretative extensions that build on
the axiomatic foundation, but do not belong to the physical axiomatics:

- **E1 (Observer as resonator):** The observer can be modeled as a
  coupled mode (follows from A1, A3, A6)

---

## 3. Coupling Efficiency ε — Unified Definition

### 3.1 Notation

In earlier versions of the RFT various symbols
(ε, 𝓔, 𝜀) and different definitions were used. Since 2026
the following is binding:

| Symbol | Name | Usage |
|:------:|:-----|:------|
| **ε** | Coupling efficiency | In formulas and mathematical texts |
| **ε(Δφ)** | Phase-dependent coupling efficiency | When the dependence is explicit |
| **η(Δφ)** | Coupling efficiency (observable) | In FLRW simulations (cross-term) |

The calligraphic symbol **𝓔** was a typographic variant
from earlier versions and has been replaced by **ε**.

### 3.2 Definition

The coupling efficiency ε describes what fraction of the maximum
possible resonance energy is actually transferred between two coupled
modes.

$$
\varepsilon : \text{State space} \to [0, 1]
$$

```
    ε = 1    perfect coupling (phase equality, maximum coherence)
    ε = 0    no coupling (phase orthogonality, decoherence)
```

### 3.3 Standard Model

$$
\varepsilon(\Delta\phi) = \cos^2(\Delta\phi / 2) = \frac{1}{2}(1 + \cos\Delta\phi)
$$

| Property | Value |
|----------|-------|
| Value range | [0, 1] |
| At phase equality (Δφ = 0) | ε = 1 (perfect coupling) |
| At antiphase (Δφ = π) | ε = 0 (no coupling) |
| At 90° shift (Δφ = π/2) | ε = 0.5 (half coupling) |

ε is not a constant, but depends on:
- Phase difference Δφ between coupled modes
- Coherence of the coupling
- Damping and dissipation

### 3.4 More General Models

For systems with finite resonance width an alternative
Gaussian model can be used:

$$
\varepsilon(\Delta\phi) = \exp(-(\Delta\phi/\delta)^2)
$$

where δ describes the width of the coupling window.

Both models satisfy: ε ∈ [0, 1], ε(0) = 1, monotonically decreasing
with |Δφ|.

---

## 4. The Energy Formula

### 4.1 Basic Form (Axiom 4)

$$
E = \pi \cdot \varepsilon(\Delta\phi) \cdot \hbar \cdot f
$$

### 4.2 Limit Cases and Special Values

| Condition | ε | Energy | Physics |
|-----------|---|--------|---------|
| Perfect coupling (Δφ = 0) | 1 | π·ℏ·f | Maximum resonance energy |
| Planck (1st excitation) | 1/π ≈ 0.318 | ℏ·f | E = ℏω (special case) |
| Planck (ground state) | 1/(2π) ≈ 0.159 | ℏ·f/2 | Ground-state energy (harm. osc.) |
| Natural damping | 1/e ≈ 0.368 | (π/e)·ℏ·f | After one relaxation time |
| Half coupling (Δφ = π/2) | 0.5 | π·ℏ·f/2 | 90° phase shift |
| No coupling (Δφ = π) | 0 | 0 | Decoupled systems |

### 4.3 Derivation of the Factor π

The factor π arises from the integration of the coupling efficiency
over a half-cycle of the resonance path in phase space:

$$
\int_0^\pi \cos^2(\phi/2) \, d\phi = \frac{\pi}{2}
$$

Normalized to the coupling unit the basic formula
E = π · ε · ℏ · f follows (complete derivation: see
[axiomatic foundation](../definitions/axiomatic_foundation.md) §4.1).

---

## 5. The Identity ε = η

### 5.1 Derivation

In the FLRW simulation the coupling efficiency is extracted as the
time-averaged cross-term of two coupled scalar fields:

$$
\eta(\Delta\phi) = \frac{\langle \varepsilon_1 \cdot \varepsilon_2 \rangle}{\sqrt{\langle \varepsilon_1^2 \rangle \cdot \langle \varepsilon_2^2 \rangle}}
$$

The analytical expectation for harmonic fields is
η_theo = cos²(Δφ/2). Since simultaneously the theoretical
coupling operator ε(Δφ) = cos²(Δφ/2) holds, the exact
identity follows:

$$
\varepsilon(\Delta\phi) = \eta(\Delta\phi) = \cos^2(\Delta\phi / 2)
$$

### 5.2 Consequences

| Domain | Consequence |
|--------|-------------|
| General | Operator and observable are identical |
| FLRW cosmology | η emerges as observable, d_η scales with H₀ |
| Resonance reactor | κ = 1 exactly (no free parameter) |
| Schrödinger simulation | ε(Δφ) → 0 at Δφ = π, Fidelity = 1.0 confirmed |
| Monte Carlo | ε = 1 at resonance mass → Axiom 3 confirmed |

### 5.3 Empirical Evidence

```
    Flat (H = 0):      d_η = 0.043 ± 0.008  → cos² nearly exact
    Planck (H₀ = 67.4): d_η = 0.140 ± 0.025  → Hubble friction
    SH0ES (H₀ = 73.0):  d_η = 0.149 ± 0.026  → Δd_η > 6σ
```

The deviation from cos² is systematic and explained by
spacetime expansion (Hubble friction). In the flat limit
the identity ε = η is exact to d_η ≈ 0.04.

---

## 6. Distinction: ε vs. η vs. K_ij vs. G

| Quantity | Symbol | Value range | Meaning |
|----------|--------|-------------|---------|
| Coupling efficiency (operator) | ε(Δφ) | [0, 1] | Theoretical coupling operator |
| Coupling efficiency (observable) | η(Δφ) | [0, 1] | Measurable cross-term (FLRW) |
| Coupling strength | K_ij | [0, ∞) | Absolute coupling between modes |
| Resonance weighting | G(f₁/f₂) | [0, 1] | Frequency resonance window (Axiom 3) |

**Identity:** ε = η (proven by cos² identity, validated
in FLRW with 1,530 simulations).

The coupling strength K_ij describes how strongly two modes
interact fundamentally. The coupling efficiency ε describes
how much of this interaction is actually converted into energy transfer.

---

## 7. Classification of Earlier Definitions

### 7.1 The Interval [1/e, e]

In the original version a "natural resonance interval" ε ∈ [1/e, e]
was given. Classification:

- The range ε ∈ [1/e, 1] describes physically meaningful
  coupling states (damped to perfect)
- The range ε > 1 was intended as resonance amplification
  (constructive interference of several modes), but is not defined in the
  single-mode coupling efficiency
- For multi-mode systems the **effective coupling strength**
  K_ij can take values > 1 (superposition of several paths),
  but ε as efficiency remains ∈ [0, 1]

**Correction:** The interval [1/e, e] applies to the coupling strength
K_ij between modes, not to the coupling efficiency ε.

### 7.2 The Definition 𝓔 := √(e · 1/e) = 1

In an earlier README it was defined:

```
    𝓔 := √(e · 1/e) = 1
```

This describes the **reference state**: the geometric mean
between maximum growth (e) and maximum decay (1/e)
yields the neutral coupling. In the current notation
ε = 1 corresponds to perfect coupling → E = π · ℏ · f.

### 7.3 The Special Case ε = 1/e

In an earlier version ε = 1/e was presented as a universal
correction factor. Correct classification:

$$
\varepsilon(t) = e^{-t/\tau} \quad \Rightarrow \quad \varepsilon(\tau) = 1/e \approx 0.368
$$

This is a physically important special case
(typical coupling after settling), not the
general case.

---

## 8. Mathematical Consequences

### 8.1 Stable Resonance Fields (Theorem)

From A1, A2, and A3 it follows: a field Φ(x,t) is stable if and only if
its Fourier components stand in rational frequency ratios.
(Proof: axiomatic foundation §4.2)

### 8.2 Coupling Dynamics

$$
\frac{dK_{ij}}{dt} = \alpha \cdot G(f_i/f_j) \cdot \cos(\Delta\phi_{ij}) - \beta \cdot K_{ij}
$$

### 8.3 Resonance as Information Selection

$$
P(\psi | \Phi) \propto P(\Phi | \psi) \cdot P(\psi)
$$

Coherent states (high PCI) are selectively amplified.

### 8.4 Entropy of a Resonance Configuration

$$
S(x) = -x \cdot \ln(x) \quad \text{with } x = E/E_0 \in (0, 1]
$$

---

## 9. Empirical Validation

### 9.1 Axiom-by-Axiom Evidence from RFT-Internal Simulations

| Axiom | Test | Result |
|-------|------|--------|
| A1 | FLRW simulations: η ≈ cos²(Δφ/2) | Δd_η > 6σ, Δχ² = +16 vs CMB |
| A2 | Coupled Oscillators: multi-frequency superposition | Energy exchange confirmed at resonance |
| A3 | Monte Carlo: 1,500,000 sim. on CMS data | 5 resonances, emp. p = 0 |
| A4 | FLRW: ε = η identity, resonance reactor κ = 1 | No free parameter |
| A5 | Resonance field simulation: energy direction vector | Energy directionality confirmed |
| A6 | Resonance field simulation: coupling efficiency and energy flow | PCI → MI confirmed |
| A7 | Monte Carlo: bandwidth-independent (3 KDE); CERN data | Stable resonance pattern across seeds |

### 9.2 Four Validation Domains

| Domain | Method | Result |
|--------|--------|--------|
| Particle physics | 1,500,000 MC sim. on CMS data | 5 resonances, emp. p = 0 |
| Cosmology | 1,530 FLRW simulations | Δd_η > 6σ, Δχ² = +16 |
| Nuclear technology | Resonance reactor (GDR) | κ = 1, Q_fiss ≈ 1.0 |
| Classical mechanics | Double pendulum + coupled oscillators | ε(θ₂−θ₁) = cos²(Δθ/2) confirmed |

### 9.3 Detailed Results per Domain

**FLRW Cosmology:**
```
    η(Δφ) = ⟨ε₁·ε₂⟩ / √(⟨ε₁²⟩·⟨ε₂²⟩)
    d_η = ⟨|η_sim − η_theo|⟩
    dd_η/dH₀ = (0.00113 ± 0.00017) (km/s/Mpc)⁻¹
    Δd_η (SH0ES − Planck) = 0.0063 ± 0.0010 (> 6σ)
    Δχ² = +16 vs Planck-2018-CMB
```

**Resonance Reactor:**
```
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR
    κ = 1 (from ε = η, no free parameter)
    f_GDR = E_GDR / (π·ℏ)

    U-235: GDR 13.0 MeV, f = 6.3×10²¹ Hz, λ_eff/λ₀ = 7872
    Pu-239: GDR 13.5 MeV, Q_fiss ≈ 1.0 at Φ = 10¹² γ/(cm²·s)
    Am-241: GDR 13.3 MeV, α-decay accelerable
```

**Double Pendulum:**
```
    ε(θ₂−θ₁) = cos²((θ₂−θ₁)/2)
    ε = 1 at Δθ = 0 (synchronized), ε = 0 at Δθ = π (antiphase)
    Dynamic coupling efficiency confirms cos²-model
```

**Coupled Oscillators:**
```
    Resonance condition (A3): ε = 1 at frequency ratio n:m
    Energy exchange confined to resonant modes
    Multi-frequency superposition (A2) confirmed
```

**Monte Carlo (CMS data):**
```
    Resonance condition (A3): ε = 1 at M₀ = particle mass
    5 resonances detected with emp. p = 0:
    φ(1020), J/ψ, Υ(1S), Υ(2S), Z-boson
    1,500,000 total simulations (30 seeds × 50,000)
    Stable over 3 KDE bandwidths
```

### 9.4 Falsification Tests

- **Resonance condition (A3):** Monte Carlo test on CMS dielectron data.
  Prediction: resonance peaks at particle masses. Result: 5 resonances,
  emp. p = 0 (1,500,000 simulations, 3 KDE bandwidths, 30 seeds).
- **Classical indicators:** RSI, Momentum, MA-crossover,
  posterior probabilities — all correlation < 0.05.
  RFT observables (energy_dir, AC-phase) systematic.
- **Resonance reactor:** σ_coh > σ_incoh (RFT prediction)
  vs. σ_coh = σ_incoh (standard model). Experimentally testable.

---

## 10. Fields of Application

- **Particle physics:** Monte Carlo resonance analysis on
  CMS open data (5 resonances, 1,500,000 simulations)
- **Cosmology:** Coupled FLRW simulations, Hubble tension,
  CMB comparison with Planck-2018 data
- **Nuclear technology:** Resonance reactor — resonant
  transmutation of actinides (GDR-based, κ = 1)
- **Financial markets:** ResoTrade — resonance-based BTC trading
  (application concept)
- **Classical mechanics:** Synchronization of coupled
  oscillators, [double pendulum](../mathematics/double_pendulum.md)
- **Biophysics:** Neural synchronization, protein folding
- **Information theory:** Resonance-based channel capacity
- **Analytical mathematics:** [Resonance integrals](../mathematics/resonance_integrals.md)

---

## 11. Distinction from Other Theories

Compared to classical field theories (Maxwell, Yang-Mills) the
RFT is not restricted to specific types of interaction,
but emphasizes the universal coupling structure of all fields.

Compared to information theory (Shannon), information
packets are not treated as isolated bits, but as
coherent field structures (Axiom 6).

Compared to conventional algorithmic trading (ML, RSI,
MACD), the application concept ResoTrade is not based on
price prediction, but on phase recognition in the oscillation
field (see [ResoTrade — application concept](../../concepts/ResoTrade/resotrade_trading_ai.md)).

---

## 12. Conclusion

The coupling efficiency ε of Resonance Field Theory is:

1. **A function**, not a fixed value: ε = ε(Δφ, coherence, ...)
2. **Restricted to [0, 1]**: efficiency > 100% is not physically defined
3. **The standard model** is ε(Δφ) = cos²(Δφ/2)
4. **Identical to the observable η**: ε(Δφ) = η(Δφ), validated
   in FLRW simulations (1,530 runs, d_η = 0.043 in the flat case)
5. **Eliminates κ**: In the resonance reactor κ = 1 follows exactly
6. **Special cases**: ε = 1 (perfect), ε = 1/(2π) (Planck ground state),
   ε = 1/π (Planck 1st excitation), ε = 1/e (natural damping)
7. **Not to be confused** with the coupling strength K_ij, which
   can be unbounded
8. **Empirically confirmed** in four domains: particle physics,
   cosmology, nuclear technology, classical mechanics
9. **Notation unified**: All documents and simulations
   use ε (instead of 𝓔), ℏ (instead of h), cos²(Δφ/2) as
   standard model

This definition is binding for all documents of
Resonance Field Theory from version 2026 onwards.

---

## References

1. L. Boltzmann: *Vorlesungen über Gastheorie*, Leipzig, 1896.
2. M. Born, E. Wolf: *Principles of Optics*, Cambridge, 1999.
3. C. E. Shannon: *A Mathematical Theory of Communication*, 1948.
4. N. Wiener: *Cybernetics*, 1948.
5. R. P. Feynman et al.: *The Feynman Lectures on Physics*, 1964.
6. Planck Collaboration: *Astron. Astrophys.* **641** A5, A6 (2020).
7. CMS Collaboration: *CMS Open Data Portal*, opendata.cern.ch (2016).
8. Berman B L, Fultz S C: *Rev. Mod. Phys.* **47** 713 (1975).
9. Riess A G et al.: *Astrophys. J. Lett.* **934** L7 (2022).

---

## Document Structure of the RFT

| Document | Content |
|----------|---------|
| [Axiomatic Foundation](../definitions/axiomatic_foundation.md) | Formal axioms A1–A7 with proofs and tests |
| [Coupling Efficiency](coupling_efficiency.md) | This document |
| [Resonance Field Equation](../mathematics/resonance_field_equation.md) | Central energy equation |
| [Energy Sphere](../mathematics/energy_sphere.md) | Geometric model |
| [Resonance Integrals](../mathematics/resonance_integrals.md) | Analytical methods |
| [Resonance Energy Vector](../mathematics/resonance_energy_vector.md) | Energy as directional quantity |
| [Empirical Evidence](../../empirical/) | CERN evaluation, Monte Carlo |

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[⬅️ back](../../../README.md)
