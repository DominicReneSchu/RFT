# 🧪 Simulation Results: Resonance Reactor

*Dominic-René Schu, 2025/2026*

This file documents the quantitative results of the resonance
reactor simulation. All calculations are based on the RFT
fundamental formula E = π · ε · ℏ · f and the empirically validated
identity ε = η = cos²(Δφ/2) with κ = 1 (no free parameter).

➡️ [Go to Python simulation](simulation/run.py)

---

## 1. Physical Foundations of the Simulation

### 1.1 Formulas

```
    GDR frequency:          f_GDR = E_GDR / (π · ℏ)
    Effective decay rate:   λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR
    Coupling efficiency:    η(Δφ) = cos²(Δφ/2)    [= ε(Δφ)]
    Coupling parameter:     κ = 1                   [from ε = η]
    Fissibility quotient:   Q_fiss = η · Φ · σ_GDR / λ₀
    Remaining fraction:     N(t) = N₀ · exp(−λ_eff · t)
    Energy release:         P(t) = N(t) · λ_eff · E_fiss
```

### 1.2 Constants

```
    ℏ = 6.582 × 10⁻²² MeV·s
    E_fiss ≈ 200 MeV (fission energy per nucleus)
    η = 1 (perfect phase coherence, Δφ = 0)
    Φ_γ = 10¹² γ/(cm²·s) (reference photon flux)
```

---

## 2. Isotope Database

| Isotope | E_GDR (MeV) | f_GDR (Hz) | σ_GDR (barn) | λ₀ (s⁻¹) | t₁/₂ (natural) |
|---------|-------------|------------|--------------|-----------|-----------------|
| U-235 | 13.0 | 6.29 × 10²¹ | 0.120 | 3.12 × 10⁻¹⁷ | 7.04 × 10⁸ y |
| U-238 | 13.2 | 6.39 × 10²¹ | 0.125 | 4.92 × 10⁻¹⁸ | 4.47 × 10⁹ y |
| Pu-239 | 13.5 | 6.53 × 10²¹ | 0.115 | 9.11 × 10⁻¹³ | 2.41 × 10⁴ y |
| Pu-240 | 13.4 | 6.49 × 10²¹ | 0.118 | 3.35 × 10⁻¹² | 6.56 × 10³ y |
| Am-241 | 13.3 | 6.44 × 10²¹ | 0.110 | 5.08 × 10⁻¹¹ | 432 y |
| Np-237 | 13.1 | 6.34 × 10²¹ | 0.112 | 1.03 × 10⁻¹⁴ | 2.14 × 10⁶ y |
| Cs-137 | 15.3 | 7.41 × 10²¹ | 0.085 | 7.30 × 10⁻¹⁰ | 30.2 y |
| Sr-90 | 16.5 | 7.99 × 10²¹ | 0.075 | 7.63 × 10⁻¹⁰ | 28.8 y |

---

## 3. Results: Effective Decay Rates

### 3.1 At Reference Photon Flux (Φ = 10¹² γ/cm²/s, η = 1)

| Isotope | λ₀ (s⁻¹) | λ_eff (s⁻¹) | λ_eff/λ₀ | t₁/₂_eff | Q_fiss |
|---------|-----------|-------------|----------|----------|--------|
| U-235 | 3.12 × 10⁻¹⁷ | 1.20 × 10⁻¹³ | 7872 | ~90,000 y | 3.85 × 10⁶ |
| U-238 | 4.92 × 10⁻¹⁸ | 1.25 × 10⁻¹³ | 25,400 | ~176,000 y | 2.54 × 10⁷ |
| Pu-239 | 9.11 × 10⁻¹³ | 1.16 × 10⁻¹⁰ | 127 | ~190 y | 126 |
| Pu-240 | 3.35 × 10⁻¹² | 1.21 × 10⁻¹⁰ | 36 | ~182 y | 35 |
| Am-241 | 5.08 × 10⁻¹¹ | 1.61 × 10⁻¹⁰ | 3.16 | ~137 y | 2.16 |
| Np-237 | 1.03 × 10⁻¹⁴ | 1.12 × 10⁻¹³ | 10.9 | ~196,000 y | 9.9 |
| Cs-137 | 7.30 × 10⁻¹⁰ | 8.15 × 10⁻¹⁰ | 1.12 | ~27 y | 0.12 |
| Sr-90 | 7.63 × 10⁻¹⁰ | 8.38 × 10⁻¹⁰ | 1.10 | ~26 y | 0.098 |

### 3.2 Interpretation

**Actinides (Q_fiss > 1):** Resonant GDR excitation dominates
over natural decay. U-235 is degraded almost 8,000× faster,
Pu-239 127×, Am-241 3×. These are actinides with α-decay or
spontaneous fission — the GDR channel opens an additional
fission pathway.

**Fission products (Q_fiss < 1):** Cs-137 and Sr-90 decay
via β-emission. GDR excitation accelerates the decay only
marginally (~10–12%), since the decay channel is β rather than
fission and σ_GDR is smaller.

**Physics:** The longer the natural half-life, the stronger
the relative effect — because λ₀ is small and the resonance
term η · Φ · σ_GDR dominates.

---

## 4. Results: Phase Dependence

### 4.1 η(Δφ) = cos²(Δφ/2) for Pu-239

| Δφ (rad) | Δφ (degrees) | η = cos²(Δφ/2) | λ_eff/λ₀ |
|----------|-------------|----------------|----------|
| 0 | 0° | 1.000 | 127 |
| π/6 | 30° | 0.933 | 119 |
| π/4 | 45° | 0.854 | 109 |
| π/3 | 60° | 0.750 | 96 |
| π/2 | 90° | 0.500 | 64 |
| 2π/3 | 120° | 0.250 | 33 |
| 3π/4 | 135° | 0.146 | 20 |
| 5π/6 | 150° | 0.067 | 9.5 |
| π | 180° | 0.000 | 1.0 |

### 4.2 Interpretation

At Δφ = π (antiphase), the resonant coupling vanishes
completely — λ_eff = λ₀ (natural decay). This is the
experimentally testable RFT signature: If one rotates the phase
of the photon field, the decay rate must follow the cos² profile.

**Comparison with incoherent light:**
Thermal photons average over all phases → η_eff = 0.5 →
λ_eff/λ₀ ≈ 64 (instead of 127 with coherent excitation). The
ratio coherent/incoherent ≈ 2 is a direct, experimentally
verifiable prediction.

---

## 5. Results: Transmutation Chains

### 5.1 Decay Chain U-235

```
    U-235   (t₁/₂ = 704 My,  λ_eff/λ₀ = 7872)
      → GDR fission → Fission products (Cs-137, Sr-90, etc.)
      → or: U-235 →(n,γ)→ U-236 →(n,γ)→ Np-237 →(GDR)→ Fission products
```

### 5.2 Decay Chain Pu-239

```
    Pu-239  (t₁/₂ = 24,100 y, λ_eff/λ₀ = 127)
      → GDR fission → Fission products
      → or: Pu-239 →(n,γ)→ Pu-240 →(n,γ)→ Am-241 →(GDR)→ Fission products

    Pu-240  (t₁/₂ = 6,560 y,  λ_eff/λ₀ = 36)
      → GDR fission → Fission products

    Am-241  (t₁/₂ = 432 y,    λ_eff/λ₀ = 3.16)
      → GDR fission → Fission products
```

### 5.3 Temporal Evolution (Pu-239, 1 kg, Φ = 10¹² γ/cm²/s)

| Year | N/N₀ (natural) | N/N₀ (resonant) | P_fiss (kW) |
|------|----------------|-----------------|-------------|
| 0 | 1.000 | 1.000 | 9.3 |
| 50 | 0.9986 | 0.835 | 7.8 |
| 100 | 0.9971 | 0.697 | 6.5 |
| 190 | 0.9946 | 0.500 | 4.7 |
| 500 | 0.9862 | 0.074 | 0.69 |
| 1000 | 0.9724 | 0.005 | 0.05 |

**Comparison:** Natural decay degrades only 2.8% of Pu-239 in
1,000 years. The resonance reactor degrades 99.5% — reduction of
the effective half-life from 24,100 to ~190 years.

---

## 6. Results: Energy Production

### 6.1 Power Profile per kg Pu-239

```
    N₀ = 2.52 × 10²⁴ nuclei/kg
    λ_eff = 1.16 × 10⁻¹⁰ s⁻¹
    E_fiss = 200 MeV = 3.2 × 10⁻¹¹ J

    P(t=0) = N₀ · λ_eff · E_fiss
           = 2.52 × 10²⁴ × 1.16 × 10⁻¹⁰ × 3.2 × 10⁻¹¹
           ≈ 9.3 kW (thermal)
```

### 6.2 Integrated Energy Release

```
    E_total = N₀ · E_fiss = 2.52 × 10²⁴ × 200 MeV
            ≈ 8.1 × 10¹³ J ≈ 22.4 GWh per kg Pu-239
```

### 6.3 Energy Balance

| Item | Power |
|------|-------|
| Fission power (per kg Pu-239) | 9.3 kW (thermal) |
| Photon source (synchrotron/FEL) | ~1 MW (electrical) |
| Critical mass for net energy | ~110 kg Pu-239 |
| German Pu-239 inventory | ~75,000 kg |
| Potential at full inventory | ~700 MW thermal |

**Consequence:** At full Pu-239 inventory (75 t) and
Φ = 10¹² γ/(cm²·s), the thermal power is ~700 MW —
comparable to a conventional nuclear power plant, but
operated with existing nuclear waste.

---

## 7. Comparison with FLRW Results

The identity ε = η, which justifies κ = 1 in the resonance
reactor, was independently validated in the FLRW simulations:

| Metric | FLRW Simulation | Resonance Reactor |
|--------|----------------|-------------------|
| Coupling efficiency | η = cos²(Δφ/2) (emergent) | η = cos²(Δφ/2) (ansatz) |
| Deviation from cos² | d_η = 0.043 (flat) | d_η ≈ 0 (no Hubble) |
| Identity ε = η | Yes (1,530 runs) | Yes → κ = 1 |
| Phase dependence | Validated over 30 phase values | Prediction (testable) |

**Consistency:** In the resonance reactor (no spacetime expansion),
the identity ε = η should hold more precisely than in FLRW cosmology,
since the Hubble friction (d_η ≈ 0.04) is absent.

---

## 8. Summary of Simulation Results

| Result | Value |
|--------|-------|
| Isotopes simulated | 8 (U-235, U-238, Pu-239, Pu-240, Am-241, Np-237, Cs-137, Sr-90) |
| Strongest effect | U-235: λ_eff/λ₀ = 7872 |
| Weakest effect | Sr-90: λ_eff/λ₀ = 1.10 |
| Fissibility threshold | Q_fiss > 1 for all actinides |
| Phase dependence | η = cos²(Δφ/2) over 9 phase values (Pu-239) |
| Energy production | 9.3 kW/kg Pu-239 (thermal) |
| Net energy threshold | ~110 kg Pu-239 |
| κ | 1 exact (no free parameter) |
| Connection to FLRW | ε = η validated in 1,530 simulations |

---

## 9. Open Simulation Tasks

1. ⬜ **Complete decay chains:** All daughter isotopes with
   their own GDR parameters, multi-step transmutation
2. ⬜ **Flux scan:** λ_eff/λ₀ as a function of Φ (10⁸ − 10¹⁵)
   → Saturation effects at high flux
3. ⬜ **Phase scan:** η(Δφ) over 30+ values (analogous to FLRW) →
   Quantify deviations from cos²
4. ⬜ **Thermal feedback:** Temperature influence on σ_GDR
   and resonance width
5. ⬜ **Multi-mode analysis:** Coupling to higher GDR modes
   (E2, E3) and their contribution to λ_eff
6. ⬜ **Monte Carlo validation:** Stochastic simulation of
   decay statistics under resonance conditions

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[Back to overview](README.md)
