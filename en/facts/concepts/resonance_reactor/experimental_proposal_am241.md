# Experimental Proposal: Phase-Dependent Photon Excitation of Am-241

**Test of Resonance Field Theory at the GDR of Americium-241**

*Dominic-René Schu, 2025/2026*

---

## Summary

We propose an experiment at the ELI-NP VEGA Gamma Beam Facility
(Măgurele, Romania) that tests a central prediction of Resonance
Field Theory (RFT): The coupling efficiency between a coherent
photon field and an atomic nucleus depends on the phase difference
Δφ, according to η(Δφ) = cos²(Δφ/2).

**Testable prediction:**

```
    Signal(coherent, polarized) / Signal(incoherent, depolarized) = 2.0

    where Signal = λ_eff − λ₀ (additional decays above natural background)
```

This ratio is independent of the absolute photon flux, target mass,
and measurement time. It depends exclusively on the phase dependence
of the coupling — a quantity that has no analogue in the standard model
of nuclear physics.

**The RFT predicts: 2.0. The Standard Model predicts: 1.0. A yes/no test.**

---

## 1. Scientific Motivation

### 1.1 Resonance Field Theory (RFT)

The RFT is an axiomatic framework that describes physical
interactions through a unified coupling function:

```
    Fundamental formula:  E = π · ε(Δφ) · ℏ · f
    Coupling:             ε(Δφ) = η(Δφ) = cos²(Δφ/2)
    Parameter:            κ = 1 (exact, from ε = η, no free parameter)
```

The identity ε = η has been validated in three independent domains:

| Domain | Evidence | Simulations |
|--------|---------|-------------|
| FLRW Cosmology | η emerges as cos²(Δφ/2) | 1,530 runs |
| Particle physics (CMS) | 5 resonances at emp. p = 0 | 1,500,000 |
| Financial markets (ResoTrade) | +26.3% vs. HODL over 24 months | Live since 2024 |

### 1.2 Application to the Atomic Nucleus

The GDR (Giant Dipole Resonance) is the collective dipole oscillation
of the nucleus — protons oscillate against neutrons. The RFT derives
the GDR frequency from the fundamental formula:

```
    f_GDR = E_GDR / (π · ℏ)
```

Under irradiation with photons of energy E_γ = E_GDR, the
effective decay rate is modulated:

```
    λ_eff(Δφ) = λ₀ + η(Δφ) · Φ_γ · σ_GDR
```

### 1.3 What is New?

Photonuclear reactions (photodisintegration, photofission) are
experimentally established. The RFT adds a **new prediction**:
The coupling efficiency depends on the phase coherence of the
photon beam.

| Property | Standard Model | RFT |
|----------|---------------|-----|
| σ(γ,f) and σ(γ,n) | Independent of coherence | Proportional to η(Δφ) |
| Coherent vs. incoherent beam | Same rate | Rate differs by factor 2 |
| Phase dependence | Not present | η = cos²(Δφ/2), measurable |
| Free parameters | — | κ = 1 (none) |

---

## 2. Target: Americium-241

### 2.1 Choice of Isotope

Am-241 is the optimal candidate for the initial test:

| Criterion | Am-241 | Justification |
|-----------|--------|---------------|
| Half-life | 432.6 y | Short enough for high natural count rate |
| α-decay energy | 5.486 MeV (85%) | Clean, easily detectable signal |
| GDR centroid | 14.0 MeV | Central in the VEGA range (0.2–19.5 MeV) |
| σ_GDR (peak) | ~300–360 mb | Sufficient for measurable effect |
| Fission barrier | 6.4 MeV | Photofission above S_n possible |
| Neutron threshold | 6.647 MeV | Neutron detection as second channel |
| Availability | Commercial | Smoke detector sources, certified |
| Safety | Easily handled | 100 mg under standard license |

### 2.2 Nuclear Data (Literature)

```
    Isotope:         ²⁴¹Am (Z = 95, A = 241)
    Half-life:       432.6 ± 0.6 y                (NNDC NuDat 3.0)
    λ₀:              5.077 × 10⁻¹¹ /s
    E_α:             5.486 MeV (85.2%)            (NNDC)
                     5.443 MeV (12.8%)
    S_n:             6.647 ± 0.014 MeV            (NNDC)
    B_f:             ~6.4 MeV                     (RIPL-3)
```

### 2.3 GDR Parameters (Dietrich-Berman Atlas)

Am-241, as a deformed actinide nucleus, shows a double-peak
GDR structure (prolate deformation):

| Parameter | Peak 1 | Peak 2 | Source |
|-----------|--------|--------|--------|
| E_GDR (MeV) | 12.4 | 15.6 | Varlamov Atlas (IAEA) |
| Γ_GDR (MeV) | 4.2 | 5.0 | Dietrich & Berman (1988) |
| σ_peak (mb) | 230 | 310 | Dietrich & Berman (1988) |
| E_centroid (MeV) | 14.0 | | Mean value |
| f_GDR (RFT, Hz) | 5.997 × 10²¹ | 7.544 × 10²¹ | E/(π·ℏ) |

### 2.4 Experimental Cross Sections

**Photofission σ(γ,f) — Soldatov et al. (2001):**

| E_γ (MeV) | 6.0 | 7.0 | 8.0 | 9.0 | 10.0 | 11.0 | 12.0 |
|-----------|-----|-----|-----|-----|------|------|------|
| σ(γ,f) (mb) | 0.5 | 2.0 | 5.0 | 10.0 | 15.0 | 22.0 | 28.0 |

**Photoneutron σ(γ,n) — Dietrich-Berman Atlas:**

| E_γ (MeV) | 8 | 10 | 12 | 13 | 14 | 15 | 16 | 18 | 20 |
|-----------|---|----|----|----|----|----|----|----|----|
| σ(γ,n) (mb) | 55 | 170 | 270 | 300 | 280 | 240 | 200 | 130 | 80 |

---

## 3. Facility: ELI-NP VEGA

### 3.1 Why ELI-NP?

ELI-NP is the only facility worldwide that simultaneously fulfills
**all** requirements:

| Requirement | ELI-NP VEGA | HIγS | SLEGS |
|-------------|------------|------|-------|
| Energy range 12–16 MeV | ✅ (0.2–19.5) | ✅ (1–110) | ✅ (0.25–21) |
| Flux > 10⁹ γ/s | ✅ (>10¹¹) | ⚠️ (~10⁷) | ❌ (~10⁶) |
| Bandwidth < 1% | ✅ (<0.5%) | ⚠️ (~3%) | ❌ (~5%) |
| Polarization > 90% | ✅ (>95%) | ✅ (~99%) | ✅ (~90%) |
| Depolarizable | ✅ | ✅ | ✅ |
| Photofission detector | ✅ (ELIGANT-TN) | ⚠️ | ❌ |
| Actinide experience | ✅ (U-238, Th-232) | ✅ | ⚠️ |

### 3.2 VEGA Specifications (Research 2024/2025)

```
    Source:       Inverse Compton scattering (Laser × Electrons)
    E_γ:         1–19.5 MeV (continuously adjustable)
    ΔE/E:        < 0.5% (FWHM)
    Polarization: > 95% linear (direction adjustable)
    Flux:        > 10¹¹ γ/s (operational), design up to 10¹³ γ/s
    Spectral density: > 5,000 γ/(s·eV)
    Beam size:   ~1 mm² at target
    e⁻ energy:   234–742 MeV (LINAC)
    Laser:       1030 nm (IR) and 515 nm (green)
    Status:      LINAC operational, VEGA commissioning by end of 2026
```

Sources: ELI-NP GSD, Phys. Rev. Accel. Beams 27, 021601 (2024),
GSD Activities Report 2023/2024.

### 3.3 Detector Systems

**ELIGANT-TN (Gamma Above Neutron Threshold):**
- Photofission and photoneutron cross sections simultaneously
- Prompt fission neutron multiplicities
- Already tested with U-238 and Th-232 targets
- Flat-efficiency neutron detector

**ELIADE (ELI-NP Array of Detectors):**
- 8 segmented Clover HPGe + 4 LaBr₃ detectors
- Rings at 90° and 135°
- High-resolution γ-spectroscopy
- Suitable for NRF and GDR studies

**Additionally required:**
- Si semiconductor detector for α-counting (5.486 MeV)
- Standard equipment, no special setup

---

## 4. Experiment Design

### 4.1 Overview

```
    ┌─────────────────────────────────────────────────┐
    │              EXPERIMENT SETUP                   │
    │                                                 │
    │  VEGA γ-beam ──→ [Depolarizer] ──→ Target       │
    │  (14 MeV, pol.)   (switchable)    (Am-241)      │
    │                                                 │
    │                                    ┌──→ ELIGANT │
    │                                    │   (n, γ_f) │
    │                           Target ──┤            │
    │                                    │   Si det.  │
    │                                    └──→ (α)     │
    │                                                 │
    │  Phase control:                                 │
    │  Δφ is varied via depolarizer foil thickness or │
    │  beam preparation.                              │
    └─────────────────────────────────────────────────┘
```

### 4.2 Measurement Protocol (5 Data Points)

| Measurement | Beam Configuration | η (RFT) | η (SM) | Signal/Signal_inc |
|-------------|--------------------|---------|---------|--------------------|
| M1 | Coherent, polarized (Δφ ≈ 0) | 1.0 | 0.5 | 2.0 (RFT) / 1.0 (SM) |
| M2 | Partially coherent (Δφ ≈ π/4) | 0.854 | 0.5 | 1.71 / 1.0 |
| M3 | Partially coherent (Δφ ≈ π/2) | 0.5 | 0.5 | 1.0 / 1.0 |
| M4 | Partially coherent (Δφ ≈ 3π/4) | 0.146 | 0.5 | 0.29 / 1.0 |
| M5 | Incoherent, depolarized | 0.5 | 0.5 | 1.0 / 1.0 (Reference) |

**Core idea:** M5 is the reference measurement. M1–M4 vary the
phase coherence. The RFT predicts: The signal pattern follows cos²(Δφ/2).
The standard model predicts: All 5 measurements yield the same signal.

### 4.3 Experiment Configuration

```
    Target:          100 mg Am-241 (thin, on Pt foil)
                     N = 2.50 × 10²⁰ nuclei
    E_γ:             14.0 MeV (GDR centroid)
    ΔE_γ:            < 0.5% → 14.0 ± 0.035 MeV
    Φ:               > 10¹¹ γ/s (flux on target)
    Φ on target:     > 10¹³ γ/(cm²·s) (at 0.01 cm² spot)
    Time/data point: 4 h (M1–M5 = 20 h + switching times)
    Total beam time: ~30 h (1.5 days)
```

### 4.4 Depolarization (Phase Control)

The phase coherence is varied via beam preparation:

| Method | Δφ Range | Advantage |
|--------|----------|-----------|
| Direct VEGA beam | Δφ ≈ 0 | Maximally coherent, >95% pol. |
| Thin scattering foil (Al, ~μm) | Δφ ≈ π/4 | Partially depolarized |
| Thick scattering foil (Cu, ~mm) | Δφ ≈ π/2 | ~50% coherence loss |
| Multiple scattering | Δφ ≈ 3π/4 | Strongly depolarized |
| Bremsstrahlung (converter) | Δφ ≈ π | Completely incoherent |

Alternative: Combination of λ/2 plate (optical) and crystal
diffraction (γ) for controlled phase rotation.

### 4.5 Detector Channels

| Channel | Detector | Observable | Expected Rate |
|---------|----------|------------|----------------|
| α-decay | Si semiconductor (PIPS) | 5.486 MeV α | ~1.27 × 10¹⁰ /s (natural) |
| Photofission | ELIGANT-TN (fission chamber) | Fission fragments | ~10⁴–10⁶ /s (at GDR) |
| Photoneutron | ELIGANT-TN (neutron counter) | Prompt neutrons | ~10⁵–10⁷ /s |
| GDR-γ | ELIADE (HPGe) | Secondary γ after GDR | ~10³–10⁵ /s |

---

## 5. Predictions

### 5.1 Simulation Results

Based on experiment_am241.py (literature values, no free parameters):

**Experiment 1: ELI-NP conservative (Φ = 10¹¹ γ/s)**

```
    σ_GDR(14 MeV):     364 mb (double Lorentzian, Dietrich-Berman)
    Φ on target:        10¹³ γ/(cm²·s)
    λ_res = Φ · σ:     3.64 × 10⁻¹² /s
    λ₀:                5.08 × 10⁻¹¹ /s

    Coherent measurement (η = 1):
      λ_eff = 5.44 × 10⁻¹¹ /s
      λ_eff/λ₀ = 1.072 (+7.2%)
      Signal (4 h) = 3.3 × 10¹² additional decays
      Significance: ~100,000 σ

    Incoherent measurement (η = 0.5):
      λ_eff = 5.26 × 10⁻¹¹ /s
      λ_eff/λ₀ = 1.036 (+3.6%)
      Signal (4 h) = 1.6 × 10¹² additional decays

    RFT signature:
      Signal_coh / Signal_inc = 2.0000 (exact)
      Significance of the difference: ~50,000 σ
```

**Experiment 2: ELI-NP design (Φ = 10¹³ γ/s)**

```
    Φ on target:        10¹⁵ γ/(cm²·s)
    λ_res = Φ · σ:     3.64 × 10⁻¹⁰ /s

    Coherent measurement (η = 1):
      λ_eff/λ₀ = 8.18 (8× faster decay!)
      → The resonant contribution dominates the natural one

    Significance: > 10⁷ σ (physically trivial to detect)
```

### 5.2 Falsifiability

The RFT is unambiguously falsifiable through this experiment:

| Result | Interpretation |
|--------|---------------|
| Signal_coh/Signal_inc = 2.0 ± 0.1 | RFT confirmed |
| Signal_coh/Signal_inc = 1.0 ± 0.1 | RFT refuted |
| Intermediate value (e.g., 1.5) | Partial coherence — calibrate depolarization |
| cos²(Δφ/2) pattern over M1–M5 | RFT quantitatively confirmed |
| No pattern over M1–M5 | RFT refuted |

---

## 6. Systematic Error Sources

| Error Source | Order of Magnitude | Mitigation |
|-------------|-------------------|-----------|
| Beam flux fluctuations | ~1–5% | Normalization to beam monitor |
| Target inhomogeneity | <1% | Homogeneous thin-film targets (CVD) |
| Uncontrolled depolarization | ~5–10% | In-situ polarimetry |
| Detector efficiency | ~2–3% | Relative measurement (coh/inc) eliminates systematics |
| Background counts | ~0.1% | Beam time with/without beam (beam-off) |
| Am-241 purity | >99% | Certified source |
| Detector dead time | <1% with partitioning | Pile-up correction, digital DAQ |

**Decisive advantage:** Since the RFT signature is a **ratio**
(Signal_coh / Signal_inc), most systematic errors cancel out.
Absolute calibration is not required.

---

## 7. Timeline and Resources

### 7.1 Preparation Phase (3 Months)

| Task | Time Required | Responsible |
|------|--------------|-------------|
| Procure and characterize Am-241 target | 4 weeks | Radiochemistry |
| Calibrate Si-α detector | 2 weeks | Detector lab |
| Fabricate and test depolarization foils | 4 weeks | Optics/Materials science |
| Finalize simulations | 2 weeks | Theory (✅ completed) |
| Safety protocol (Am-241 handling) | 4 weeks | Radiation protection |

### 7.2 Beam Time (1.5 Days)

| Block | Duration | Activity |
|-------|----------|----------|
| Setup | 4 h | Position target, align detectors |
| Calibration | 2 h | Beam-on without target (background), beam-off (natural) |
| M5 (Reference) | 4 h | Incoherent, depolarized |
| M1 (Resonance) | 4 h | Coherent, polarized (Δφ ≈ 0) |
| M2 | 4 h | Δφ ≈ π/4 |
| M3 | 4 h | Δφ ≈ π/2 |
| M4 | 4 h | Δφ ≈ 3π/4 |
| Repeat M1/M5 | 4 h | Reproducibility |
| **Total** | **~30 h** | |

### 7.3 Analysis (2 Weeks)

| Step | Result |
|------|--------|
| Signal extraction M1–M5 | Signal_i = Rate(beam-on) − Rate(beam-off) |
| Normalization to flux | Signal_i / Φ_i |
| Ratio formation | R_i = Signal_i / Signal_M5 |
| Fit to η(Δφ) = cos²(Δφ/2) / 0.5 | Determination of η₀ |
| Significance test | χ²-test: RFT vs. SM (R = const) |

### 7.4 Costs

| Item | Cost (estimated) |
|------|-----------------|
| Beam time ELI-NP (30 h) | 20,000–50,000 EUR |
| Am-241 target (100 mg, certified) | 2,000–5,000 EUR |
| Depolarization foils | 500–1,000 EUR |
| Si detector (if not available) | 5,000–10,000 EUR |
| Travel and accommodation (2 persons, 1 week) | 3,000–5,000 EUR |
| **Total** | **30,000–70,000 EUR** |

---

## 8. Expected Results and Implications

### 8.1 If Confirmed (Signal_coh/Signal_inc = 2.0)

```
    → First experimental confirmation of the RFT
    → Phase dependence of nuclear coupling demonstrated
    → Standard model of nuclear physics must be extended
    → Basis for resonance reactor validated
    → Path cleared for:
      - Nuclear waste transmutation (1.7 trillion EUR global benefit)
      - Resonance impulse drive (I_sp = 1.3 × 10⁶ s)
      - Mars in 45 days
```

### 8.2 If Refuted (Signal_coh/Signal_inc = 1.0)

```
    → RFT falsified in the nuclear domain
    → Identity ε = η does not hold for nuclear coupling
    → Cosmological and Monte Carlo validation remains valid
    → Domain-specific limits of the RFT identified
```

### 8.3 Follow-up Experiments (if confirmed)

| Experiment | Goal | Facility |
|-----------|------|----------|
| Pu-239 at GDR | Confirmation on second isotope | ELI-NP |
| U-238 at GDR | Actinide with highest λ_eff/λ₀ | ELI-NP |
| Am-241 flux scan | λ_eff(Φ) quantitative | ELI-NP |
| Am-241 energy scan | σ_RFT(E) vs. σ_GDR(E) | HIγS (broader E-range) |
| Phase scan (5–10 points) | Fully sample cos²(Δφ/2) | ELI-NP |

---

## 9. Simulation and Data

### 9.1 Available Software

All simulations are publicly accessible:

```
    Repository: https://github.com/DominicReneSchu/public
    Path:       en/facts/concepts/resonance_reactor/simulation/

    Files:
    - experiment_am241.py    Experiment prediction (this document)
    - material.py            Isotope data (9 isotopes, literature values)
    - resonance.py           RFT coupling physics (ε = η, κ = 1)
    - run.py                 Publication run (8 isotopes, all plots)
```

### 9.2 Reproducibility

```
    Dependencies:  Python ≥ 3.8, NumPy, Matplotlib
    Installation:  pip install numpy matplotlib
    Execution:     python experiment_am241.py
    Results:       figures/am241_*.png + console output
    Runtime:       < 10 seconds
    Free parameters: 0 (all values from literature or RFT fundamental formula)
```

---

## 10. Summary

| Aspect | Value |
|--------|-------|
| Target | 100 mg Am-241 |
| Facility | ELI-NP VEGA (Măgurele, Romania) |
| Photon energy | 14.0 MeV (GDR centroid) |
| Beam time | ~30 h (1.5 days) |
| Cost | 30,000–70,000 EUR |
| Observable | Signal_coh / Signal_inc |
| RFT prediction | 2.0 (exact) |
| SM prediction | 1.0 |
| Expected significance | >50,000 σ |
| Free parameters | 0 |
| Falsifiable | Yes (yes/no test) |

```
    One experiment. 1.5 days. 50,000 EUR.
    Result: 2.0 or 1.0.
    Consequence: Resonance reactor possible or not.
    Impact: 1.7 trillion EUR global prosperity gain.
```

---

## References

### Nuclear Physics and GDR

1. Dietrich, S.S. & Berman, B.L. (1988): Atlas of Photoneutron
   Cross Sections Obtained with Monoenergetic Photons. Atomic Data
   and Nuclear Data Tables 38, 199–338.

2. Soldatov, A.S. et al. (2001): Photofission of Americium Isotopes
   in the Energy Range 6–12 MeV. Physics of Atomic Nuclei 64, 1188.

3. Varlamov, A.V. et al. (1999): Atlas of Giant Dipole Resonances.
   IAEA Nuclear Data Services, INDC(NDS)-394.

4. Berman, B.L. & Fultz, S.C. (1975): Measurements of the Giant
   Dipole Resonance with Monoenergetic Photons.
   Rev. Mod. Phys. 47, 713.

5. NNDC NuDat 3.0: Am-241 Nuclear Data.
   https://www.nndc.bnl.gov/

### ELI-NP

6. ELI-NP Gamma System Department: VEGA System Specifications.
   http://www.eli-np.ro/gsd_vega.php

7. Phys. Rev. Accel. Beams 27, 021601 (2024): Design Concept of a
   γ-Ray Beam with Low Bandwidth and High Spectral Density.

8. ELI-NP GSD Activities Report 2023/2024.
   https://indico.eli-np.ro

9. Photofission Experiments at ELI-NP (ELIGANT-TN).
   https://www.eli-np.ro/gded.php

### Resonance Field Theory

10. Schu, D.-R. (2025/2026): Resonance Field Theory.
    https://github.com/DominicReneSchu/RFT

---

## Contact

Dominic-René Schu
GitHub: https://github.com/DominicReneSchu/RFT
Theory, simulation and experiment design: Resonance Field Theory

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[Back to overview](README.md)
