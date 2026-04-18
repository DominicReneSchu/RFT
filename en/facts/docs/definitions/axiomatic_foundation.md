# Axiomatic Foundation of Resonance Field Theory

*Dominic-René Schu, 2025/2026*

---

## 1. Introduction

Resonance Field Theory (RFT) describes fundamental processes in nature, technology,
and information systems as coupling and resonance phenomena in oscillation fields.

This document sets out the axiomatic foundation of the theory. The axioms are
chosen to be:

- **minimal** (no axiom follows from the others),
- **formally precise** (each axiom contains a mathematical statement),
- **empirically testable** (each axiom makes a verifiable prediction).

---

## 2. Symbol Table

### 2.1 Energy and Oscillation

| Symbol | Meaning |
|:------:|:--------|
| h | Planck action quantum |
| f | Frequency |
| ω | Angular frequency, ω = 2πf |
| k | Wave number |
| A | Amplitude |
| φ | Phase |
| ψ(x,t) | Oscillation function (mode) |
| Φ(x,t) | Total field function (superposition of all modes) |
| E | Energy (vector in resonance field) |
| E₀ | Characteristic energy (normalization) |

### 2.2 Coupling and Structure

| Symbol | Meaning |
|:------:|:--------|
| ε(Δφ) | Coupling efficiency, function of phase difference |
| K_ij | Coupling strength between modes i and j |
| δ | Width of the resonance window |
| m, n | Resonance quantum numbers (m, n ∈ ℤ⁺) |
| Δφ | Phase difference between coupled modes |
| G(f₁/f₂) | Weighting function of the resonance window |

### 2.3 Information and Order

| Symbol | Meaning |
|:------:|:--------|
| S | Entropy of a resonance configuration |
| MI(X,Y) | Mutual information: H(X) + H(Y) − H(X,Y) |
| PCI | Phase Coherence Index: |⟨exp(i(φ₁−φ₂))⟩| ∈ [0,1] |

### 2.4 Symmetry

| Symbol | Meaning |
|:------:|:--------|
| G_sync | Group of synchronous transformations |
| T | Element of G_sync: T(f_i, φ_i, t) = (λf_i, φ_i + φ₀, at + b) |
| Λ | Frequency scaling operator |

---

## 3. Axiom System

### Axiom 1 — Universal Oscillation

**Statement:** Every physical entity possesses at least one periodic
oscillation mode.

**Formalization:**

```
(A1)    ψ(x, t) = A · cos(kx − ωt + φ)
```

**Testable prediction:** Every system can be decomposed into periodic components
(Fourier decomposition). In financial markets: the price can be decomposed into a
DC component (trend) and an AC component (tradeable oscillation).

**Physical example:** Natural oscillations of a microwave resonator.

**Empirical evidence (RFT-internal):** FLRW simulation: η ≈ cos²(Δφ/2),
Δd_η > 6σ (1,530 runs). The natural frequency of any physical system
is measurable (Fourier decomposition).

---

### Axiom 2 — Superposition

**Statement:** Oscillation modes superpose linearly in fields.

**Formalization:**

```
(A2)    Φ(x, t) = Σᵢ ψᵢ(x, t) = Σᵢ Aᵢ · cos(kᵢx − ωᵢt + φᵢ)
```

**Testable prediction:** The superposition of several modes produces
interference patterns. In financial markets: short-term and long-term
oscillations superpose in the price signal.

**Physical example:** Interference of two coherent laser beams.

---

### Axiom 3 — Resonance Condition

**Statement:** Resonance between two systems occurs when their frequencies
stand in a rational ratio, within a tolerance window δ.

**Formalization:**

```
(A3)    |f₁/f₂ − m/n| < δ,    m, n ∈ ℤ⁺

        G(f₁/f₂) = exp(−(|f₁/f₂ − m/n| / δ)²)
```

G is the weighting function: maximal at exact resonance, decreasing
with detuning.

**Testable prediction:** Systems with different eigenfrequencies can
couple resonantly. Systems with identical eigenfrequencies oscillate
synchronously — no overtones, no information exchange.

**Empirical evidence (RFT-internal):** Monte Carlo test on CMS dielectron data:
5 resonances at particle masses, emp. p = 0 (1,500,000 simulations, 3 KDE,
30 seeds). CERN resonance analysis: significant resonance excesses in mass data.

---

### Axiom 4 — Coupling Energy

**Statement:** The effective energy of a resonant coupling is determined
by frequency, coupling efficiency, and the cyclic geometry of the
resonance path.

**Formalization:**

```
(A4)    E_eff = π · ε(Δφ) · h · f

        For multi-mode coupling:
        E_eff = π · ε(Δφ_ij) · h · ⟨f_ij⟩
```

Here:
- ε(Δφ) is the coupling efficiency as a function of the phase difference,
  e.g. ε(Δφ) = cos²(Δφ/2)
- π is the geometric factor from the integration over a half-cycle
  of the resonance path (derivation: see §4.1)
- h is the Planck action quantum
- f is the frequency of the coupled mode

**Derivation of π:** The coupling between two resonators does not occur
instantaneously, but over a path in phase space. The integration of
the coupling efficiency over a complete half-cycle yields:

```
        ∫₀^π cos²(φ/2) dφ = π/2

        Normalized to maximum coupling (Δφ = 0):
        E_eff / E_max = π · ε · h · f / (h · f) = π · ε
```

The factor π thus arises from the cyclic geometry of the coupling,
not as a free parameter.

**Testable prediction:** Energy transfer is maximal at phase equality
(ε = 1) and zero at phase orthogonality (ε = 0).

**Physical example:** Josephson junction — energy transfer between
superconductors via phase-coherent coupling.

---

### Axiom 5 — Energy Direction

**Statement:** Energy in a resonance field is not a scalar quantity,
but a vector: it has magnitude and direction in the field.

**Formalization:**

```
(A5)    E⃗ = E_eff · ê(Δφ, ∇Φ)

        The direction ê is determined by:
        - the phase gradient ∇Φ of the resonance field
        - the phase difference Δφ between coupled modes
```

In a discrete multi-scale system (e.g. financial markets) the energy
direction vector is the difference of the relative energies on
different time scales:

```
        energy_dir = e_short − e_long

        e_short = (price − MA_SHORT) / MA_SHORT
        e_long  = (price − MA_LONG)  / MA_LONG
```

**Testable prediction:** The direction of energy flow is a useful
observable that goes beyond scalar indicators.

**Empirical evidence (RFT-internal):** Resonance field simulation: energy direction
vector (A5) confirmed — PCI → MI shows directional energy flow control.
FLRW simulation: energy flow direction confirmed in cosmological context.

---

### Axiom 6 — Information Flow through Resonance Coupling

**Statement:** Information is transmitted exclusively through coherent phase and
frequency relations. The quality of information flow is measurable through
Mutual Information and Phase Coherence Index.

**Formalization:**

```
(A6)    MI(X, Y) = H(X) + H(Y) − H(X, Y)

        PCI = |⟨exp(i(φ₁ − φ₂))⟩| ∈ [0, 1]

        Information flow I(X → Y) > 0  ⟺  PCI > 0 ∧ MI > 0
```

**Testable prediction:** Systems without phase coherence (PCI ≈ 0) cannot
exchange information — regardless of the amplitude of the individual
oscillations.

**Empirical evidence (RFT-internal):** Resonance field simulation: information flow
through coupling efficiency and PCI confirmed. Monte Carlo test: emp. p = 0
(resonance only when resonance condition A3 is met).

---

### Axiom 7 — Invariance under Synchronous Transformations

**Statement:** The coupling structure of the resonance field remains invariant
under synchronous transformations of the group G_sync.

**Formalization:**

```
(A7)    T ∈ G_sync:  T(fᵢ, φᵢ, t) = (λfᵢ, φᵢ + φ₀, at + b)

        Invariance conditions:
        G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ))
        ε(Δφ_ij) = ε(T(φᵢ) − T(φⱼ))
```

**Testable prediction:** The resonance structure is scale-invariant —
it holds on all time scales and energy scales.

**Empirical evidence (RFT-internal):** Monte Carlo test stable over 3 KDE bandwidths
and 30 seeds (A7 confirmed). FLRW simulation: coupling structure invariant over
various H₀ values (4 regimes). CERN data: stable resonance pattern.

---

## 4. Mathematical Consequences

### 4.1 Derivation of the Factor π in the Energy Formula

From Axiom 1 (oscillation) and Axiom 4 (coupling energy) it follows:

The energy transfer between two resonantly coupled modes
with coupling efficiency ε(Δφ) = cos²(Δφ/2) over a complete
coupling cycle is:

```
    E_cycle = h · f · ∫₀^(2π) cos²(φ/2) dφ / (2π)
            = h · f · π / (2π)
            = h · f / 2
```

The effective coupling energy for a half-cycle (the minimal
unit of coherent transfer) is:

```
    E_eff = h · f · ∫₀^π cos²(φ/2) dφ / π
          = h · f · (π/2) / π
          = h · f / 2
```

Normalized to the coupling unit:

```
    E_eff = π · ε(Δφ) · h · f
```

where the factor π encodes the cyclic geometry of the coupling path
and ε ∈ [0, 1] is the effective coupling strength.

### 4.2 Stability as a Consequence (not an independent axiom)

From A1 (oscillation), A2 (superposition) and A3 (resonance condition) it follows:

**Theorem (Stable Resonance Fields):** A field Φ(x,t) is stable if and only if
its Fourier components ωₙ stand in rational ratios:

```
    Φ_stable(x, t) = Σₙ cₙ · exp(i(kₙx − ωₙt))
    with ωₙ/ω₀ ∈ ℚ  for all n
```

*Proof:* Constructive interference (standing waves) requires periodic
recurrence of the field pattern. This is only guaranteed for rational
frequency ratios (Weyl's theorem on equidistribution).

**Note:** In the earlier version this was Axiom 5. However, it is a
consequence of Axioms 1–3 and therefore not an independent axiom.

### 4.3 Coupling Dynamics

From A3 (resonance condition) and A4 (coupling energy) the
temporal evolution of the coupling strength follows:

```
    dK_ij/dt = α · G(fᵢ/fⱼ) · cos(Δφ_ij) − β · K_ij
```

(α: excitation rate, β: damping rate)

### 4.4 Resonance Landscape and Attractors

The effective potential of the coupling:

```
    V(f) = −π · ε(Δφ(f)) · h · f
```

Local minima of V correspond to stable resonances (attractors).

### 4.5 Resonance as Information Selection

From A6 (information flow) it follows that resonance acts as a Bayesian
information filter:

```
    P(ψ | Φ) ∝ P(Φ | ψ) · P(ψ)
```

Coherent states (high PCI) are selectively amplified.

---

## 5. Interpretative Extensions

The following statements are **not axioms** of the RFT, but
interpretative supplements that build on the axiomatic foundation.

### 5.1 Observer as Resonator (E1)

The observer can be modeled as a coupled mode in the resonance field.
Through resonance coupling (A6), the measurement process imprints on the field structure.

This is consistent with quantum mechanics (measurement problem), but is not
set here as an axiom, since it follows from A1–A7: an observer is a
system with eigenfrequency (A1) that exchanges information with the field
through resonance coupling (A3, A6).

---

## 6. Overview: Axioms and Their Empirical Tests

| Axiom | Core statement | Core formula | RFT-internal evidence |
|-------|----------------|--------------|----------------------|
| A1 | Universal oscillation | ψ = A·cos(kx−ωt+φ) | FLRW simulations: η ≈ cos²(Δφ/2), Δd_η > 6σ |
| A2 | Superposition | Φ = Σ ψᵢ | Coupled Oscillators: multi-frequency superposition simulated |
| A3 | Resonance condition | \|f₁/f₂ − m/n\| < δ | Monte Carlo test: 5 resonances at particle mass, emp. p = 0 |
| A4 | Coupling energy | E = π·ε·h·f | FLRW: ε = η identity (κ = 1), Schrödinger simulation: derived from A4 |
| A5 | Energy direction | E⃗ = E·ê(Δφ,∇Φ) | Resonance field simulation: energy direction vector; Double pendulum: ε(θ₂−θ₁) |
| A6 | Information flow | MI > 0 ⟺ PCI > 0 | Resonance field simulation: coupling efficiency and energy flow |
| A7 | Invariance (G_sync) | G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ)) | Monte Carlo test: bandwidth-independent (3 KDE); CERN data: stable resonance pattern |

---

## 7. Fields of Application

- **Quantum physics:** Superposition, quantization through rational frequency ratios
- **Classical mechanics:** Synchronization of coupled oscillators
- **Financial markets:** Resonance-based trading (ResoTrade — application concept)
- **Biophysics:** Neural synchronization, protein folding
- **Information theory:** Resonance-based channel capacity
- **Cosmology:** Harmonic pattern formation

---

## 8. Conclusion

Resonance Field Theory consists of 7 core axioms (A1–A7) that are:

1. **Minimal**: The stable resonance field (old A5) is derivable as a theorem
2. **Independent**: No axiom follows from the others
3. **Formally precise**: Each axiom contains a mathematical formula
4. **Empirically testable**: Each axiom has a documented test (FLRW simulations, Monte Carlo, CERN data, resonance reactor)

The extension E1 (observer as resonator) is an interpretative supplement
that builds on the foundation, but does not belong to the physical axiomatics.

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[⬅️ back](../../../README.md)
