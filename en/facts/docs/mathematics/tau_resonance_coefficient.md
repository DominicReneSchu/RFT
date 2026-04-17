# The Resonance Time Coefficient τ*

*Dominic-René Schu, 2025/2026*

---

## 1. Introduction

In classical physics, energy is a scalar quantity. In
Resonance Field Theory, energy is functionally linked to coupling efficiency
and thus to the phase structure between systems.

The dimensionless **resonance time coefficient**:

```
    τ*(Δφ) = π / ε(Δφ)
```

describes the time scale of resonance coupling: how many
coupling cycles are needed to achieve a complete energy transfer?

τ* is a **function** of the phase difference, not a constant.
With ε(Δφ) = cos²(Δφ/2) (standard model):

```
    τ*(Δφ) = π / cos²(Δφ/2)
```

Since ε = η (identity from FLRW simulations), τ* is directly
linked to the measurable coupling efficiency.

---

## 2. Definition and Value Range

```
    τ*(Δφ) = π / ε(Δφ)        with ε ∈ (0, 1]
```

| Coupling state | ε | τ* | Meaning |
|----------------|---|-----|---------|
| Perfect coupling | 1 | π ≈ 3.14 | Minimum transfer time |
| Half coupling | 0.5 | 2π ≈ 6.28 | Double transfer time |
| Natural damping | 1/e ≈ 0.368 | π·e ≈ 8.54 | After relaxation (special case) |
| Planck (1st excitation) | 1/π ≈ 0.318 | π² ≈ 9.87 | E = ℏ·f (special case) |
| Planck (ground state) | 1/(2π) ≈ 0.159 | 2π² ≈ 19.74 | E = ½ℏ·f (special case) |
| Weak coupling | 0.1 | 10π ≈ 31.4 | Slow transfer |
| No coupling | 0 | → ∞ | No transfer possible |

**Physical interpretation:** τ* is inversely proportional to
coupling efficiency. The weaker the coupling, the more cycles
are needed to transfer energy.

**Noteworthy:** At the Planck ground state (ε = 1/(2π)) the
transfer time is τ* = 2π² — a product of the two fundamental
geometric constants of the RFT.

---

## 3. Complex Time Structure

The classical unit of energy normalization:

```
    E / (ℏ·f) = π · ε
```

is interpreted in the RFT geometrically as the hypotenuse of a time-time triangle:

```
    1 = √(cos²(α) + sin²(α))
```

with:
- Real time component: t_r = cos(α) · t
- Imaginary time component: t_i = sin(α) · t

The angle α describes the phase relationship between coupled systems.
The complex energy projection:

```
    E = π · ε · ℏ · f · (cos(α) + i · sin(α))
```

The Planck ground-state energy E = ½ℏf uses only the real part
at ε = 1/(2π) and loses the phase structure.

---

## 4. Sender-Receiver Asymmetry

The coupling efficiency can differ for sender and receiver
when the phase difference acts asymmetrically:

- **Sending efficiency:** ε_S = ε(Δφ_S) — how efficiently a system
  couples energy into the field
- **Receiving efficiency:** ε_R = ε(Δφ_R) — how efficiently a system
  decouples energy from the field

The total efficiency of the transfer:

```
    η_total = ε_S · ε_R
```

For the symmetric case (ε_S = ε_R = ε):

```
    η_total = ε²
```

**Example:** At ε = 1/e (natural damping, special case):

```
    η_total = (1/e)² = 1/e² ≈ 0.135 (13.5%)
```

At ε = 0.85 (slight detuning, Δφ ≈ π/4):

```
    ε(π/4) = cos²(π/8) ≈ 0.85
    η_total = 0.85² ≈ 0.73 (73%)
```

---

## 5. Dynamics of the Resonance Time Coefficient

For a system with time-dependent coupling efficiency ε(t):

```
    τ*(t) = π / ε(t)
```

The temporal change:

```
    dτ*/dt = −π / ε² · dε/dt
```

For exponential coupling decay (damped system):

```
    ε(t) = ε₀ · e^(−λt)    →    dε/dt = −λ · ε
```

it follows:

```
    dτ*/dt = λ · τ*
```

This describes an exponential growth of τ*: the
transfer time grows exponentially when coupling decays exponentially —
consistent with physical intuition.

For growing coupling (settling process):

```
    ε(t) = 1 − e^(−λt)    →    τ*(t) = π / (1 − e^(−λt))
```

τ* falls from ∞ (no coupling) to π (perfect coupling).

---

## 6. Empirical Anchoring

| Domain | τ* reference | Observation |
|--------|-------------|-------------|
| FLRW | τ*(0) = π | η = 1.0 at Δφ = 0, minimum transfer time |
| FLRW | τ*(π) → ∞ | η = 0.0 at Δφ = π, no transfer |
| FLRW | τ* grows with H₀ | Hubble friction increases d_η → effectively higher τ* |
| Resonance reactor | τ* = π (at resonance) | κ = 1, ε = η = 1 at Δφ = 0 |
| ResoTrade | τ* → ∞ in crash | ε → 0, pause gate, no trade |
| ResoTrade | τ* ≈ π in phase | ε ≈ 1, fast energy transfer, trade active |
| ResoTrade | Settling | Convergence after 3 cycles (Δ < 1%), consistent with τ*(t) = π/(1−e^(−λt)) |

Hubble friction in FLRW simulations can be interpreted as an
effective increase in τ*: stronger expansion shifts η systematically
below cos²(Δφ/2), which corresponds to a slower energy transfer
between the resonance fields.

---

## 7. Conclusion

The resonance time coefficient τ*(Δφ) = π/ε(Δφ) connects
coupling efficiency with the time scale of energy transfer:

1. τ* is a **function** of the phase difference, not a constant
2. Perfect coupling (ε = 1) yields the minimum transfer time τ* = π
3. Planck ground state (ε = 1/(2π)) yields τ* = 2π²
4. Sender-receiver asymmetry yields η_total = ε_S · ε_R
5. The dynamics dτ*/dt = λ·τ* describe coupling decay
6. Hubble friction effectively increases τ* (FLRW simulations)

**Correction relative to earlier version:** In an earlier
version τ* = π/𝓔 was defined as a constant (with 𝓔 = 1).
That is not correct. τ* is a function: τ*(Δφ) = π/ε(Δφ).
The case τ* = π (at ε = 1) is the special case of perfect
coupling, not the general state.

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[⬅️ back](../../../README.md)
