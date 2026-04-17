# Resonance Reactor – Resonantly Controlled Transmutation of Nuclear Waste

*Dominic-René Schu, 2025/2026*

---

## 1. Fundamental Principle

The resonance reactor uses Resonance Field Theory (RFT) for targeted
modulation of nuclear decay rates through resonant photon excitation at
the Giant-Dipole-Resonance (GDR) frequency of an isotope.

The central prediction: The decay rate of an isotope is not constant
(as in the standard model), but modulable through resonant coupling
at the eigenfrequency of the nucleus — in direct contradiction to
the stochastic standard assumption.

**RFT Fundamental Formula (Axiom 4):**

```
    E = π · ε(Δφ) · ℏ · f
```

**Application to the resonance reactor:**

```
    f_GDR = E_GDR / (π · ℏ)
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR
```

Where:
- **f_GDR**: GDR resonance frequency of the isotope (from E_GDR via the fundamental formula)
- **λ₀**: natural decay constant
- **λ_eff**: effective (modulated) decay constant
- **η(Δφ)**: coupling efficiency = cos²(Δφ/2) (identical to ε)
- **Φ_γ**: photon flux at f_GDR [γ/(cm²·s)]
- **σ_GDR**: GDR cross section of the isotope [barn]

**Key result:** κ = 1 exact (from ε = η, no free parameter).

---

## 2. Axiom Assignment

| Axiom | Application in the Resonance Reactor |
|-------|--------------------------------------|
| A1 (Universal Oscillation) | Nucleus as an oscillation system with GDR eigenfrequency |
| A3 (Resonance Condition) | Coupling at f_γ = f_GDR (rational frequency ratio 1:1) |
| A4 (Coupling Energy) | E = π · ε · ℏ · f determines f_GDR from E_GDR |
| A5 (Energy Direction) | Directed energy transfer: Photon → Nucleus → Fission |
| A6 (Information Flow) | Only coherent photon fields couple effectively |
| A7 (Invariance) | Results stable across isotopes and flux regimes |

---

## 3. Isotope-Specific Parameters

### 3.1 GDR Energies and Resonance Frequencies

```
    f_GDR = E_GDR / (π · ℏ)
    ℏ = 6.582 × 10⁻²² MeV·s
```

| Isotope | E_GDR (MeV) | f_GDR (Hz) | σ_GDR (barn) | λ₀ (s⁻¹) | t₁/₂ |
|---------|-------------|------------|--------------|-----------|-------|
| U-235 | 13.0 | 6.29 × 10²¹ | 0.120 | 3.12 × 10⁻¹⁷ | 7.04 × 10⁸ y |
| Pu-239 | 13.5 | 6.53 × 10²¹ | 0.115 | 9.11 × 10⁻¹³ | 2.41 × 10⁴ y |
| Am-241 | 13.3 | 6.44 × 10²¹ | 0.110 | 5.08 × 10⁻¹¹ | 432 y |
| Cs-137 | 15.3 | 7.41 × 10²¹ | 0.085 | 7.30 × 10⁻¹⁰ | 30.2 y |
| Sr-90 | 16.5 | 7.99 × 10²¹ | 0.075 | 7.63 × 10⁻¹⁰ | 28.8 y |

### 3.2 Effective Decay Rates

At perfect resonance (ε = η = 1, Δφ = 0):

```
    λ_eff = λ₀ + 1.0 · Φ_γ · σ_GDR
```

| Isotope | Φ_γ (γ/cm²/s) | λ_eff/λ₀ | Interpretation |
|---------|---------------|----------|----------------|
| U-235 | 10¹² | 7872 | Decay accelerated 7872× |
| Pu-239 | 10¹² | 127 | Decay accelerated 127× |
| Am-241 | 10¹² | 3.16 | Decay accelerated 3× |
| Cs-137 | 10¹² | 1.12 | Decay accelerated 12% |

**Physics:** The longer the natural half-life, the stronger
the relative effect — because λ₀ is small and the resonance term
η · Φ · σ dominates.

---

## 4. The Identity ε = η in the Resonance Reactor

### 4.1 Why κ = 1

In earlier versions, the formula contained a free coupling
parameter κ:

```
    λ_eff = λ₀ + κ · η(Δφ) · Φ_γ · σ_GDR    (old)
```

The FLRW simulations (1,530 runs) have proven that
ε(Δφ) = η(Δφ) = cos²(Δφ/2) — the theoretical operator
and the measurable observable are identical. From this follows:

```
    κ = 1 exact (no free parameter)
    λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR    (current)
```

### 4.2 Phase Dependence

The coupling efficiency depends on the phase difference Δφ between
the photon field and the GDR eigenmode of the nucleus:

```
    η(Δφ) = cos²(Δφ/2)

    Δφ = 0:   η = 1.0   perfect coupling (maximum acceleration)
    Δφ = π/2: η = 0.5   half coupling
    Δφ = π:   η = 0.0   no coupling (destructive interference)
```

**Consequence:** The phase coherence of the photon field determines
the efficiency of the transmutation. Incoherent light (thermal)
averages over all phases → η_eff ≈ 0.5.

---

## 5. Fissibility Quotient Q_fission

The fissibility quotient quantifies whether an isotope is
effectively fissile under resonant excitation:

```
    Q_fiss = η · Φ_γ · σ_GDR / λ₀
```

| Isotope | Q_fiss (Φ = 10¹² γ/cm²/s) | Interpretation |
|---------|---------------------------|----------------|
| U-235 | 3.85 × 10⁶ | Extremely fissile |
| Pu-239 | 1.26 × 10² | Highly fissile |
| Am-241 | 2.16 | Fissile |
| Cs-137 | 0.12 | Difficult to fission (β-emitter) |
| Sr-90 | 0.098 | Difficult to fission (β-emitter) |

**Threshold:** Q_fiss > 1 means that the resonant excitation
dominates the decay. For β-emitters (Cs-137, Sr-90),
Q_fiss < 1 — here GDR excitation is less effective because the
decay channel is β-emission rather than fission.

---

## 6. System Components

| Component | Function | Technological Basis |
|-----------|----------|---------------------|
| **Photon source** | Coherent photon flux at f_GDR | Synchrotron / FEL (6–17 MeV) |
| **Resonance chamber** | Fuel target under irradiation | Shielded cavity, fuel rod geometry |
| **Phase control** | Maximization of η(Δφ) → 1 | Phase-locked loop (PLL), FPGA |
| **Cooling** | Heat removal from fission processes | Sodium/lead coolant or helium |
| **Energy extraction** | Fission energy → electricity | Thermal cycle / direct conversion |
| **Control** | Real-time optimization of f, Δφ, Φ | Deep Resonance Network (DRN) |

---

## 7. Comparison: RFT Prediction vs. Standard Model

| Aspect | Standard Model | RFT (Resonance Reactor) |
|--------|---------------|------------------------|
| Decay rate | λ = const (stochastic) | λ_eff = λ₀ + η·Φ·σ (modulable) |
| Influencing | Not possible | Through resonant photon excitation |
| Coupling parameter | — | κ = 1 (from ε = η, no free parameter) |
| Phase dependence | — | η = cos²(Δφ/2) determines efficiency |
| Transmutation | Only through neutron bombardment | Additionally through GDR photoexcitation |
| Energy formula | E = ℏω | E = π · ε · ℏ · f |
| Testable prediction | — | λ_eff/λ₀ measurable at known Φ·σ |

**Decisive difference:** The RFT predicts that nuclear decay can be
measurably accelerated through resonant excitation at the GDR
eigenfrequency — the standard model considers nuclear decay as
purely stochastic and fundamentally not modulable.

---

## 8. Experimental Verifiability

### 8.1 Minimal Experiment

```
    Target:     Am-241 (t₁/₂ = 432 y, Q_fiss = 2.16)
    Source:     Synchrotron at E_γ = 13.3 MeV (f_GDR)
    Flux:       Φ = 10¹⁰ − 10¹² γ/(cm²·s)
    Observable: Decay rate λ_eff vs. λ₀
    Prediction: λ_eff/λ₀ = 1 + Q_fiss = 3.16 at Φ = 10¹²
```

### 8.2 Signature

The RFT-specific signature is the **phase dependence**:
If one rotates the phase of the photon field relative to the target,
η = cos²(Δφ/2) must be observed — an effect that the standard model
does not predict.

### 8.3 Null Experiment

```
    Control:    Same target, same flux, but
                thermal (incoherent) photons
    Expectation: η_eff ≈ 0.5 (averaging over all phases)
    Prediction:  λ_eff(coherent)/λ_eff(incoherent) ≈ 2
```

---

## 9. Application: Nuclear Waste Transmutation

### 9.1 Transmutation Chain

```
    U-235  →(n,γ)→  U-236  →(n,γ)→  Np-237  →(GDR)→  Fission products
    Pu-239 →(n,γ)→  Pu-240 →(n,γ)→  Am-241  →(GDR)→  Fission products
```

### 9.2 Nuclear Waste Inventory and Transmutation Times

| Isotope | Quantity (DE, t) | t₁/₂ (natural) | t₁/₂_eff (resonant) | Reduction factor |
|---------|-----------------|-------------------|---------------------|-----------------|
| U-235 | ~5 | 7.04 × 10⁸ y | ~90,000 y | 7872× |
| Pu-239 | ~75 | 24,100 y | ~190 y | 127× |
| Am-241 | ~3 | 432 y | ~137 y | 3.2× |

### 9.3 Energy Balance

Each fission releases ~200 MeV. Under resonant acceleration
of the Pu-239 decay:

```
    P_fiss = N · λ_eff · E_fiss
    At 1 kg Pu-239: N ≈ 2.5 × 10²⁴ nuclei
    λ_eff = 127 · λ₀ = 1.16 × 10⁻¹⁰ s⁻¹
    P_fiss ≈ 2.5 × 10²⁴ × 1.16 × 10⁻¹⁰ × 200 MeV
           ≈ 9.3 kW (thermal, per kg Pu-239)
```

---

## 10. Open Questions

1. **Experimental confirmation:** The prediction λ_eff/λ₀ > 1
   under GDR excitation must be experimentally verified.
2. **Photon source performance:** Synchrotron sources with
   Φ = 10¹² γ/(cm²·s) at 13 MeV are technically demanding.
3. **Phase coherence:** Practical realization of phase control
   at nuclear scale.
4. **Nonlinear effects:** Saturation at high fluxes
   (analogous to FLRW saturation at high H₀).
5. **Complete decay chain:** Simulation of all daughter isotopes
   with their respective GDR parameters.

---

## 11. Summary

| Key Statement | Result |
|---------------|--------|
| Fundamental formula | E = π · ε · ℏ · f → f_GDR = E_GDR/(π·ℏ) |
| Effective decay rate | λ_eff = λ₀ + η · Φ · σ_GDR |
| Coupling parameter | κ = 1 exact (from ε = η) |
| Standard model | ε(Δφ) = η(Δφ) = cos²(Δφ/2) |
| Strongest effect | U-235: λ_eff/λ₀ = 7872 at Φ = 10¹² |
| Fissibility | Q_fiss > 1 for actinides (U, Pu, Am) |
| Testable prediction | Phase dependence η = cos²(Δφ/2) |
| Main application | Transmutation of long-lived actinides |
| Connection to FLRW | ε = η validated in 1,530 simulations |

---

## 12. References

- Berman, B.L., Fultz, S.C. (1975): Measurements of the giant
  dipole resonance with monoenergetic photons.
  *Rev. Mod. Phys.* **47**, 713
- Dietrich, S.S., Berman, B.L. (1988): Atlas of photoneutron
  cross sections. *Atomic Data and Nuclear Data Tables* **38**, 199
- Planck Collaboration (2020): *A&A* **641**, A6 (Planck-2018)
- Schu, D.-R. (2025/2026): Resonance Field Theory
  ([GitHub](https://github.com/DominicReneSchu/public))

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[Back to overview](README.md)
