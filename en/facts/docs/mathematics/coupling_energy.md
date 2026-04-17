# Coupling Energy: Axiomatic Derivation and Special Cases

*Dominic-René Schu, 2025/2026*

---

## 1. Classification

Resonance Field Theory describes energy transfer as the result of
coherent resonance coupling between fields. The axiomatic foundation
is provided by Axiom 4 (coupling energy), formalized in the
[axiomatic foundation](../definitions/axiomatic_foundation.md).

The central identity ε(Δφ) = η(Δφ) = cos²(Δφ/2) has been empirically
validated in four domains (FLRW, Monte Carlo, resonance reactor,
ResoTrade). See
[Unified Definition](../definitions/coupling_efficiency.md).

---

## 2. General Energy Formula (Axiom 4)

The energy of a resonant coupling is:

```
    E = π · ε(Δφ) · ℏ · f
```

Here:
- ε(Δφ) is the coupling efficiency, ε ∈ [0, 1]
  (see [Unified Definition](../definitions/coupling_efficiency.md))
- π is the geometric factor from the cyclic coupling geometry
- ℏ is the reduced Planck action quantum (ℏ = h/2π)
- f is the frequency of the coupled mode

The standard model of the coupling efficiency is:

```
    ε(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)
```

**Identity:** The theoretical operator ε and the measurable
observable η (cross-term in FLRW simulations) are identical:
ε(Δφ) = η(Δφ). Consequence: κ = 1 in the resonance reactor (no
free parameter).

---

## 3. Limit Cases and Special Cases

### 3.1 Perfect Coupling (ε = 1)

At complete phase synchronization (Δφ = 0) the maximum
resonance energy is transferred:

```
    E_max = π · ℏ · f
```

**Empirically:** In FLRW simulations η ≈ 1.0 emerges at Δφ = 0
(table in [FLRW documentation](../../simulations/FLRW-simulations/README.md)).

### 3.2 Planck Special Case (ε = 1/(2π))

The ground-state energy of the harmonic oscillator E = ½ℏf
follows as a special case:

```
    ε = 1/(2π) ≈ 0.159
    E = π · 1/(2π) · ℏ · f = ½ · ℏ · f
```

The Planck relation E = ℏω = ℏ·2πf = h·f for the first
excited state corresponds to ε = 1/π:

```
    ε = 1/π ≈ 0.318
    E = π · (1/π) · ℏ · f = ℏ · f = ℏω/(2π) · 2π = ℏω
```

Classical quantum mechanics thus describes
coupling states ε = 1/(2π) (ground state) and ε = 1/π
(first excited state) — special cases of the general
resonance field energy formula.

### 3.3 Natural Damping (ε = 1/e) — Special Case

For a damped system with exponential relaxation, after one time constant τ:

```
    ε(t) = e^(−t/τ)    →    ε(τ) = 1/e ≈ 0.368
```

The corresponding energy:

```
    E = π · (1/e) · ℏ · f = (π/e) · ℏ · f ≈ 1.155 · ℏ · f
```

**Classification:** The factor π/e ≈ 1.155 is a consequence of the
coupling state after one relaxation time — **not a universal
correction factor** and **not a fundamental constant**. It
describes a physically important but special state.

**Physical significance:** This special case occurs in:
- Damped oscillators after the settling process
- Cavities with finite quality factor Q
- Systems with natural dissipation
- ResoTrade: convergence of the experience memory shows
  damped settling behavior (Δ < 1% after 3 cycles)

**Correction relative to earlier version:** In an earlier
version of this document ε = 1/e was presented as a universal
correction factor. That is not correct. ε = 1/e is
a special case for systems after one relaxation time, not
the general coupling state. The general quantity is
ε(Δφ) = cos²(Δφ/2).

### 3.4 Half Coupling (ε = 1/2)

At 90° phase shift (Δφ = π/2):

```
    ε(π/2) = cos²(π/4) = 1/2
    E = π · ℏ · f / 2
```

**Empirically:** In FLRW simulations η ≈ 0.57 emerges at
Δφ = π/2 (slightly above the theoretical value due to nonlinear
effects in expanding spacetime).

### 3.5 No Coupling (ε = 0)

At antiphase (Δφ = π):

```
    ε(π) = cos²(π/2) = 0
    E = 0
```

Destructive interference — no energy transfer.

**Empirically:**
- FLRW: η = 0.0 at Δφ = π (exact)
- ResoTrade: ε → 0 in crash → pause gate → +44.9% vs HODL

---

## 4. Overview of Special Cases

| Coupling state | ε | Energy | Condition |
|----------------|---|--------|-----------|
| Perfect resonance | 1 | π·ℏ·f | Δφ = 0 |
| Natural damping | 1/e ≈ 0.368 | (π/e)·ℏ·f | After relaxation time τ (special case) |
| Planck (1st excitation) | 1/π ≈ 0.318 | ℏ·f | E = ℏω (special case) |
| Planck (ground state) | 1/(2π) ≈ 0.159 | ½·ℏ·f | E = ½ℏf (special case) |
| Half coupling | 1/2 | π·ℏ·f/2 | Δφ = π/2 |
| Decoupled | 0 | 0 | Δφ = π |

**Order:** All named special cases are projections of the
general formula E = π·ε·ℏ·f onto specific physical
conditions. None is more fundamental than the others.

---

## 5. Complex Time Structure

The energy formula can be written in complex notation:

```
    E = π · ε · ℏ · f · e^{iα}
```

where α is the phase angle between observer time and field time.
The classical formula E = ℏf captures only the real part:

```
    Re(E) = π · ε · ℏ · f · cos(α)
```

The full resonance energy also contains the imaginary part, which describes
the phase coupling between systems. The temporal splitting into real and imaginary parts:

```
    t_r = cos(α) · t    (real time component)
    t_i = sin(α) · t    (imaginary time component)
```

shows that classical physics (α = 0, purely real time)
represents the special case in which the coupling efficiency is reduced to
ε · cos(α).

---

## 6. Empirical Anchoring

Each special case is empirically referenced:

| ε | Domain | Evidence |
|---|--------|---------|
| 1 | FLRW | η = 1.0 at Δφ = 0 (1,530 simulations) |
| 1 | Monte Carlo | 5 resonances at particle mass (emp. p = 0) |
| 1 | Resonance reactor | κ = 1 from ε = η identity |
| 0 | FLRW | η = 0.0 at Δφ = π (exact) |
| 0 | ResoTrade | Pause gate at ε → 0 (+44.9% vs HODL) |
| cos²(Δφ/2) | FLRW | d_η = 0.043 in the flat case |
| cos²(Δφ/2) | ResoTrade | AC phase identifies cycle position |

---

## 7. Conclusion

The resonance field energy formula E = π·ε·ℏ·f contains the
Planck relation as a special case (ε = 1/(2π) for the ground state,
ε = 1/π for the first excited state). The RFT
generalizes the energy concept through:

1. The coupling efficiency ε(Δφ) ∈ [0, 1] as the central quantity
2. The identity ε = η (operator = observable, no free parameter)
3. The geometric factor π from the cyclic coupling geometry
4. The complex time structure (phase angle α)

The frequently cited factor π/e ≈ 1.155 describes the natural
coupling state after one relaxation time — a physically
important **special case**, not the general case and not
a universal correction factor.

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[⬅️ back](../../../README.md)
