# The Resonance Field Equation

*Dominic-René Schu, 2025/2026*

---

## 1. Introduction

The Resonance Field Equation connects resonance frequency, coupling efficiency,
and energy flow. It is the central energy equation of
Resonance Field Theory, derived from Axiom 4
(see [axiomatic foundation](../definitions/axiomatic_foundation.md)).

The identity ε(Δφ) = η(Δφ) = cos²(Δφ/2) ensures that
the equation contains no free parameter — the theoretical
operator and the measurable observable are identical.

---

## 2. Basic Form

```
    E = π · ε(Δφ) · ℏ · f
```

- **ε(Δφ)**: Coupling efficiency, ε ∈ [0, 1]
  (see [Unified Definition](../definitions/coupling_efficiency.md))
- **π**: Geometric factor from the cyclic coupling geometry
- **ℏ**: Reduced Planck action quantum (ℏ = h/2π)
- **f**: Resonance frequency

**Standard model:** ε(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)

**Identity:** ε(Δφ) = η(Δφ) — validated in 1,530 FLRW simulations
(d_η = 0.043 ± 0.008 in the flat case). Consequence: κ = 1 in the
resonance reactor (no free parameter).

---

## 3. Special Cases

| Coupling state | ε | Energy | Physics |
|----------------|---|--------|---------|
| Perfect resonance (Δφ = 0) | 1 | π·ℏ·f | Maximum coupling |
| Natural damping | 1/e ≈ 0.368 | (π/e)·ℏ·f | After relaxation time (special case) |
| Planck (1st excitation) | 1/π ≈ 0.318 | ℏ·f | E = ℏω (special case) |
| Planck (ground state) | 1/(2π) ≈ 0.159 | ½·ℏ·f | E = ½ℏf (special case) |
| Half coupling (Δφ = π/2) | 0.5 | π·ℏ·f/2 | 90° phase shift |
| Decoupled (Δφ = π) | 0 | 0 | Destructive interference |

Complete derivation: [Coupling Energy: Special Cases](coupling_energy.md)

---

## 4. Phase-Modulated Form

Including the complex time structure:

```
    E = π · ε · ℏ · f · e^{iα}
```

- **α**: Phase angle between observer time and field time
- **e^{iα} = cos(α) + i·sin(α)**: Euler representation

The real part describes the measurable energy transfer, the
imaginary part the latent phase coupling.

**Derivation:** From Axiom 6 (information flow through coherent
phase and frequency relations) it follows that the full
coupling energy contains phase information. The projection
onto the real time axis (α = 0) yields the basic form.

---

## 5. Frequency Dependence

- For f → 0: energy negligible (Axiom 1)
- Linear increase with f at constant coupling
- At harmonic ratio f₁/f₂ = n/m: maximum
  resonance weighting G (Axiom 3)

**Resonance reactor application:** The GDR frequencies f_GDR = E_GDR/(π·ℏ)
follow directly from the basic form. For U-235: f = 6.3 × 10²¹ Hz
at E_GDR = 13.0 MeV.

---

## 6. Usable Energy and Dissipation

In real systems dissipation occurs. The usable energy
after deducting losses:

```
    E_usable(f) = π · ε · ℏ · f · (1 − γ(f))
```

where γ(f) is the frequency-dependent dissipation factor.

For a system with exponential damping:

```
    γ(f) = 1 − e^(−f/f_c)
```

where f_c is the critical frequency above which dissipation
becomes negligible. At high frequencies (f ≫ f_c), γ → 0
and E_usable → π·ε·ℏ·f.

In FLRW simulations, Hubble friction acts as a cosmological
dissipation source: d_η grows with H₀ (slope
0.00113 ± 0.00017 per km/s/Mpc).

---

## 7. Power over a Frequency Interval

```
    P(f₁, f₂) = ∫_{f₁}^{f₂} π · ε(f) · ℏ · f · (1 − γ(f)) df
```

For constant ε and negligible dissipation:

```
    P = (π · ε · ℏ / 2) · (f₂² − f₁²)
```

---

## 8. Comparison with Classical Energy Description

| Property | Classical | RFT |
|----------|-----------|-----|
| Energy formula | E = ℏω | E = π·ε·ℏ·f |
| Coupling efficiency | Not modeled | ε(Δφ) ∈ [0, 1] |
| Geometry | Not included | π from coupling geometry |
| Phase structure | Not included | e^{iα} |
| Dissipation | Modeled separately | Integrated via γ(f) |
| Decay | λ = const | λ_eff = λ₀ + η·Φ·σ |
| Free parameters | — | None (ε = η, κ = 1) |
| Ground state | E = ½ℏf | ε = 1/(2π) → E = ½ℏf |

---

## 9. Applications

| Domain | Application of the equation | Result |
|--------|----------------------------|--------|
| Particle physics | Resonance condition at M₀ | 5 resonances, emp. p = 0 |
| Cosmology | Klein-Gordon in FLRW | η ≈ cos², Δχ² = +16 |
| Resonance reactor | f_GDR = E_GDR/(π·ℏ) | κ = 1, Q_fiss ≈ 1.0 |
| Double pendulum | Dynamic coupling efficiency ε(θ₂−θ₁) | ε = cos²(Δθ/2) confirmed |
| Energy storage | Phase control → loss minimization | Axiom 6 |
| Measurement technology | Phase modulation → energy flow monitoring | Axioms 5, 6 |

---

## 10. Conclusion

The Resonance Field Equation E = π·ε·ℏ·f generalizes the
classical Planck relation through:

1. The coupling efficiency ε(Δφ) ∈ [0, 1] as the central quantity
2. The identity ε = η (operator = observable, no free parameter)
3. The geometric factor π from the coupling geometry
4. The phase-modulated extension e^{iα} for complex time structure
5. The Planck ground state as a special case ε = 1/(2π)

Empirically validated in four domains: particle physics, cosmology,
nuclear technology, and classical mechanics.

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[⬅️ back](../../../README.md)
