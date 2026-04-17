# Resonance Impulse Drive — Directed Fission as Space Propulsion

*Dominic-René Schu, 2025/2026*

---

## 1. Summary

The resonance impulse drive uses directed fission of actinides
through resonant photon excitation at the Giant-Dipole-Resonance
(GDR) frequency. The fission fragments (~4.3% c) are collimated
through a magnetic nozzle and produce continuous, controllable
thrust.

**Key specifications:**

```
    Specific impulse:      I_sp = 1.3 × 10⁶ s
    Fragment velocity:     v_f = 1.3 × 10⁷ m/s (4.3% c)
    Fuel:                  Pu-239, Am-241, U-235 (nuclear waste)
    Control:               Phase difference Δφ → η(Δφ) = cos²(Δφ/2)
    Free parameters:       κ = 1 (none)
```

**Comparison with Starship (SpaceX):**

| Parameter | Starship (Raptor) | Resonance Shuttle |
|-----------|-------------------|-------------------|
| I_sp | 380 s (sea level) | 1,300,000 s |
| Fuel for Mars round trip | ~1,200 t (LOX/CH₄) | ~200 kg (Pu-239) |
| Orbital refueling | Yes (5–8 tanker flights) | No |
| Travel time Earth→Mars | 6–9 months | ~45 days (direct flight) |
| Reusable | Yes (with maintenance) | Yes (fuel lasts decades) |
| Multi-stage | Yes (Super Heavy + Starship) | No (SSTO possible) |

---

## 2. Physical Basis

### 2.1 Directed Fission from the RFT

The RFT fundamental formula E = π · ε(Δφ) · ℏ · f describes the
coupling between an external field (photon) and an oscillation
system (nucleus). Under GDR excitation, the nucleus is placed
into a collective dipole state — the nuclear matter oscillates
against itself.

The fission axis is determined by the polarization of the exciting
photon: Linearly polarized γ-radiation at f_GDR preferentially
produces fission along the polarization axis.

```
    Photon excitation:  γ(f_GDR, ε⃗) + ²³⁹Pu → ²³⁹Pu*(GDR)
    Fission:            ²³⁹Pu*(GDR) → Fragment₁ + Fragment₂ + 2–3 n
    Direction:          Fission axis ∥ ε⃗ (polarization vector)
```

### 2.2 Axiom Assignment

| Axiom | Application in the Impulse Drive |
|-------|----------------------------------|
| A1 (Universal Oscillation) | Nucleus as an oscillation system with GDR eigenfrequency |
| A3 (Resonance Condition) | f_γ = f_GDR → maximum nuclear coupling |
| A4 (Coupling Energy) | E = π · ε · ℏ · f determines GDR excitation energy |
| A5 (Energy Direction) | Directed energy transfer → net impulse |
| A6 (Information Flow) | Phase coherence and polarization control thrust vector |
| A7 (Invariance) | Works in any reference frame (vacuum, gravitational field) |

### 2.3 Formulas

```
    Fission energy:            E_fiss = 200 MeV = 3.2 × 10⁻¹¹ J
    Mean fragment mass:        m_f ≈ 117 u = 1.94 × 10⁻²⁵ kg
    Fragment velocity:         v_f = √(2 · E_fiss / m_f)
                                   = 1.3 × 10⁷ m/s = 4.3% c

    Specific impulse:          I_sp = v_f / g₀ = 1.3 × 10⁶ s
    Thrust:                    F = ṁ_f · v_f · η_dir
    Effective exhaust rate:    ṁ_f = N · λ_eff · m_f
    Coupling efficiency:       η(Δφ) = cos²(Δφ/2)
    Directional efficiency:    η_dir ≈ 0.85 (magnetic nozzle)
    Total efficiency:          η_total = η(Δφ) · η_dir
```

---

## 3. Rocket Equation: Why I_sp Decides Everything

### 3.1 Tsiolkovsky Equation

```
    Δv = v_e · ln(m_start / m_end)
    v_e = I_sp · g₀

    Mass ratio:
    m_start / m_end = exp(Δv / v_e)
```

### 3.2 Fuel Requirements in Comparison

For a 100-ton shuttle (structure + payload):

| Mission (Δv) | Chemical (I_sp=450) | Ion drive (I_sp=5000) | Resonance (I_sp=1,300,000) |
|--------------|--------------------|-----------------------|----------------------------|
| Earth→LEO (9.4 km/s) | 725 t | 17.4 t | 73 g |
| LEO→Mars orbit (4 km/s) | 149 t | 7.7 t | 31 g |
| Mars landing (1 km/s) | 25.5 t | 2.0 t | 8 g |
| Mars launch (3.5 km/s) | 119 t | 6.8 t | 27 g |
| Mars→Earth (4 km/s) | 149 t | 7.7 t | 31 g |
| Earth landing (0.1 km/s) | 2.3 t | 0.2 t | 0.8 g |
| **Total (22 km/s)** | **11,800 t** | **47 t** | **170 g** |

**Chemical:** 99.2% fuel. Impossible as single stage.
Starship solves this with multi-stage design and orbital refueling —
but requires 5–8 tanker flights for a Mars mission.

**Resonance:** 0.00017% fuel. The shuttle is practically all
payload. No refueling, no multi-stage rocket, arbitrarily
reusable. 170 grams of Pu-239 for Earth↔Mars↔Earth.

### 3.3 SSTO (Single Stage to Orbit)

```
    Δv Earth→LEO: 9.4 km/s (including gravity losses)

    Chemical:     m_start/m_end = exp(9400/4415) = 8.6
                  → SSTO theoretically possible, but no payload budget
                  → That's why no chemical SSTO vehicles exist

    Resonance:    m_start/m_end = exp(9400/12,750,000) = 1.00074
                  → SSTO trivial, 99.93% of weight is payload
                  → A 100 t shuttle needs 74 g of fuel
```

---

## 4. Thrust: The Remaining Challenge

### 4.1 Thrust Equation

```
    F = N_atoms · λ_eff · m_f · v_f · η_dir

    N_atoms = m_target · N_A / A          (nuclei in target)
    λ_eff = λ₀ + η(Δφ) · Φ_γ · σ_GDR    (effective fission rate)
```

### 4.2 Thrust Scaling with Photon Flux

| Target mass (Pu-239) | Φ (γ/cm²/s) | Fissions/s | Thrust (N) | Thrust/weight |
|----------------------|-------------|-----------|-----------|---------------|
| 10 kg | 10¹² | 2.9 × 10¹² | 0.75 | 7.6 × 10⁻⁶ |
| 10 kg | 10¹⁴ | 2.9 × 10¹⁴ | 75 | 7.6 × 10⁻⁴ |
| 10 kg | 10¹⁶ | 2.9 × 10¹⁶ | 7,500 | 0.076 |
| 10 kg | 10¹⁸ | 2.9 × 10¹⁸ | 750,000 | 7.6 |
| 100 kg | 10¹⁸ | 2.9 × 10¹⁹ | 7,500,000 | 7.6 |
| 1 t | 10¹⁶ | 2.9 × 10¹⁸ | 750,000 | 0.076 |
| 1 t | 10¹⁸ | 2.9 × 10²⁰ | 75,000,000 | 7.6 |

### 4.3 Requirement for Planetary Launch

```
    Thrust/weight > 1 required for launch from planetary surface

    Earth (g = 9.81 m/s²):
    100 t shuttle → F > 981 kN
    → 100 kg Pu-239 at Φ = 10¹⁸: F = 7.5 MN → F/W = 7.6 ✓

    Mars (g = 3.72 m/s²):
    100 t shuttle → F > 372 kN
    → 10 kg Pu-239 at Φ = 10¹⁸: F = 750 kN → F/W = 2.0 ✓

    Moon (g = 1.62 m/s²):
    100 t shuttle → F > 162 kN
    → 10 kg Pu-239 at Φ = 10¹⁷: F = 75 kN → F/W = 0.46 ✗
    → 100 kg Pu-239 at Φ = 10¹⁷: F = 750 kN → F/W = 4.6 ✓
```

### 4.4 Regime Selection: High Δv vs. High Thrust

```
    Orbital transfers (no gravitational field):
    → Low thrust sufficient (Φ = 10¹²–10¹⁴)
    → Continuous acceleration over days/weeks
    → Low fuel consumption

    Planetary launch/landing:
    → High thrust required (Φ = 10¹⁷–10¹⁸)
    → Short burn duration (minutes)
    → Higher fuel consumption (but still < 1 kg)

    Control: Φ and Δφ are adjusted in real-time
    → Δφ = 0: maximum thrust (resonance)
    → Δφ → π: thrust → 0 (braking by shutdown)
    → Δφ variable: thrust modulation without mechanical parts
```

---

## 5. Mission Profiles

### 5.1 Earth → Mars → Earth (Direct Flight)

```
    Shuttle:           100 t (structure + crew + payload)
    Fuel:              100 kg Pu-239
    Photon source:     Compact FEL, variable Φ = 10¹²–10¹⁸

    Phase 1 — Earth launch:
    Φ = 10¹⁸, Δφ = 0, F = 7.5 MN
    Burn duration: ~4 min → orbit (Δv = 9.4 km/s)
    Consumption: ~0.5 g Pu-239

    Phase 2 — Transfer Earth→Mars:
    Φ = 10¹⁴, Δφ = 0, F = 7.5 kN
    Continuous acceleration: a = 0.075 m/s²
    Halfway Δv: ~145 km/s after 22 days
    Total duration: ~30–45 days (depending on planetary alignment)
    Consumption: ~50 g Pu-239

    Phase 3 — Mars landing:
    Φ = 10¹⁸, Δφ = 0, F = 7.5 MN
    Burn duration: ~2 min (Mars gravity weaker)
    Consumption: ~0.2 g Pu-239

    Phase 4 — Mars stay:
    Drive off. Shuttle stands on the surface.
    No external infrastructure required.

    Phase 5 — Mars launch + return flight + Earth landing:
    Analogous to Phases 1–3, reversed.
    Additional consumption: ~50 g Pu-239

    Total consumption:  ~100 g Pu-239 (of 100 kg on board)
    Remaining:          99.9 kg → ~999 further missions possible
    Total duration:     ~90 days (outbound + 2 weeks stay + return)
```

### 5.2 Comparison: Starship vs. Resonance Shuttle (Mars Mission)

| Parameter | Starship (SpaceX) | Resonance Shuttle |
|-----------|-------------------|-------------------|
| Payload to Mars surface | ~100 t | ~100 t |
| Launch mass (LEO) | ~1,300 t (after refueling) | ~100 t |
| Fuel mass | ~1,200 t LOX/CH₄ | ~100 g Pu-239 |
| Orbital refueling | 5–8 tanker flights | Not required |
| Travel time | 6–9 months | 30–45 days |
| Launch from Mars | Yes (ISRU fuel required) | Yes (no refueling) |
| Return flight | Requires Mars fuel production | Immediately possible |
| Missions per fuel load | 1 | ~1,000 |
| Cost per kg to Mars | ~100,000 USD (SpaceX target) | ~10 USD (fuel value) |
| Technical maturity | Development (2024–2028) | Concept (2025) |

### 5.3 Outer Solar System

```
    Jupiter (Δv ≈ 30 km/s, direct flight):
    Φ = 10¹⁴, continuous: ~60 days
    Fuel: ~200 g Pu-239
    Comparison chemical: 4–6 years (gravity assists required)

    Saturn (Δv ≈ 35 km/s, direct flight):
    ~70 days, ~250 g Pu-239
    Comparison: Cassini took 7 years

    Pluto (Δv ≈ 45 km/s, direct flight):
    ~90 days, ~350 g Pu-239
    Comparison: New Horizons took 9.5 years (flyby, no landing)

    Pluto with landing and return flight (Δv ≈ 120 km/s):
    ~8 months, ~1 kg Pu-239
    Chemical: Physically impossible
```

### 5.4 Interstellar Probe

```
    Target: Proxima Centauri (4.24 light-years)

    Φ = 10¹⁸, 1 t Pu-239 target:
    F = 75 MN, shuttle mass: 10 t (uncrewed)
    a = 7,500 m/s² (765 g) — only for uncrewed probes

    More realistic: Φ = 10¹⁶, 10 t target, 100 t probe
    F = 7.5 MN, a = 75 m/s²
    Acceleration to 10% c: ~46 days
    Travel time at 10% c: ~42 years
    Deceleration at target: another ~46 days

    Total duration: ~43 years (instead of 70,000 years with Voyager)
    Fuel: ~50 kg Pu-239

    For crewed mission (a < 3 g, 1000 t ship):
    Cruise velocity: ~5% c
    Travel time: ~85 years → Generation ship becomes conceivable
```

---

## 6. System Design: Resonance Shuttle

### 6.1 Main Components

```
    ┌─────────────────────────────────────────────────┐
    │                RESONANCE SHUTTLE                │
    │                                                 │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
    │  │  Crew    │  │ Payload  │  │  Life    │       │
    │  │  module  │  │  (cargo) │  │  support │       │
    │  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
    │       │             │             │             │
    │  ┌────┴─────────────┴─────────────┴────┐        │
    │  │         Shadow shielding            │        │
    │  │    (Tungsten/Polyethylene, ~5 t)    │        │
    │  └───────────────────┬─────────────────┘        │
    │                      │                          │
    │  ┌───────────────────┴───────────────────┐      │
    │  │         Compact FEL                   │      │
    │  │  (Inverse Compton, 13 MeV, ~10 t)     │      │
    │  │  Phase control (PLL/FPGA)             │      │
    │  └───────────────────┬───────────────────┘      │
    │                      │ γ-beam                   │
    │  ┌───────────────────┴───────────────────┐      │
    │  │     Fission chamber (Target)          │      │
    │  │  Pu-239 / Am-241 (100 kg, ~0.005 m³)  │      │
    │  │  Shielded, cooled                     │      │
    │  └───────────────────┬───────────────────┘      │
    │                      │ Fission fragments        │
    │  ┌───────────────────┴───────────────────┐      │
    │  │     Magnetic nozzle                   │      │
    │  │  Superconducting coils (~5 t)         │      │
    │  │  Collimation: θ < 15°                 │      │
    │  │  Thrust vector: steerable via B-field │      │
    │  └───────────────────┬───────────────────┘      │
    │                      │                          │
    │                      ▼ Thrust                   │
    └─────────────────────────────────────────────────┘
```

### 6.2 Mass Budget (100 t Shuttle)

| Component | Mass (t) | Function |
|-----------|----------|----------|
| Crew module (6 persons) | 15 | Pressure cabin, life support |
| Payload | 40 | Cargo, equipment, rover |
| Compact FEL | 10 | Photon source (13 MeV) |
| Phase control (FPGA/DRN) | 1 | Real-time optimization of Δφ, Φ |
| Shadow shielding | 8 | Radiation protection (W + PE) |
| Magnetic nozzle | 5 | Fragment collimation |
| Fission chamber + target | 2 | 100 kg Pu-239 + housing |
| Structure + thermal control | 10 | Frame, cooling, tanks |
| Internal power supply | 5 | Reactor waste heat → electricity |
| Heat shield (atmospheric entry) | 4 | Ablative or regenerative |
| **Total** | **100 t** | |
| **Fuel (Pu-239)** | **0.0001 t** | **100 g per Mars mission** |

### 6.3 Thrust Control

```
    Thrust vector control:

    1. Thrust magnitude: Via photon flux Φ (10¹² – 10¹⁸)
                         Continuously variable, millisecond response
                         FEL power electrically adjustable

    2. Thrust direction:  Via magnetic field geometry of the nozzle
                         Fragment beam deflectable (±30°)
                         Additionally: photon polarization ε⃗

    3. Thrust efficiency: Via phase difference Δφ
                         η(Δφ) = cos²(Δφ/2)
                         Δφ = 0: full thrust
                         Δφ = π: no thrust (immediate stop)
                         → No mechanical valves or flaps

    4. Emergency shutdown: Δφ → π (destructive interference)
                         Fission stops within nanoseconds
                         Inherently safe: no thrust without photons
```

---

## 7. Technical Challenges

| Challenge | Description | Solution Approach | TRL |
|-----------|-------------|-------------------|-----|
| Compact FEL (13 MeV) | Synchrotron-level on board | Inverse Compton source (LLNL, ELI) | 3–4 |
| Φ = 10¹⁸ scaling | 10⁶× above current FEL | Superconducting cavities, energy recovery | 2–3 |
| Magnetic nozzle | Bundle fission fragments (Z = 30–60) | Superconducting solenoids (>10 T) | 3–4 |
| Fragment collimation | θ < 15° divergence | Multi-layer magnetic lens | 2–3 |
| Shadow shielding | Neutrons + γ from target | W + PE + B₄C (proven materials) | 5–6 |
| Thermal control | 200 MeV/fission → heat | Heat pipe + radiation cooling | 4–5 |
| Heat shield | Atmospheric entry on return | PICA-X (SpaceX) or UHTC | 6–7 |
| Directed fission | Polarization asymmetry of fission axis | Measured: A ≈ 0.1–0.3 for polarized γ | 3–4 |
| Inherent safety | Prevent uncontrolled fission | No thrust without photons (fail-safe) | — |

**Overall assessment:** The critical components (compact FEL,
magnetic nozzle) have been individually demonstrated in the
laboratory. Integration into a propulsion system is an engineering
project, not a physics problem.

---

## 8. Development Roadmap

### Phase 1: Fundamental Validation (2025–2030)

```
    ✅ RFT fundamental formula → GDR frequencies
    ✅ ε = η → κ = 1 (FLRW simulation, 1,530 runs)
    ✅ Simulation of transmutation rates
    ⬜ Experimental confirmation: λ_eff > λ₀ (Am-241 at synchrotron)
    ⬜ Measurement of phase dependence η = cos²(Δφ/2)
    ⬜ Measurement of fission asymmetry with polarized γ
```

### Phase 2: Component Development (2028–2035)

```
    ⬜ Compact FEL (inverse Compton, 13 MeV, laboratory scale)
    ⬜ Magnetic nozzle (prototype, fission fragment collimation)
    ⬜ Integrated thrust test (vacuum chamber, μN range)
    ⬜ Shadow shielding (material qualification)
```

### Phase 3: Engine Demonstration (2033–2040)

```
    ⬜ Integrated engine (FEL + target + nozzle)
    ⬜ Ground test: thrust in mN–N range
    ⬜ Orbital test: uncrewed demonstrator (CubeSat class)
    ⬜ Scaling test: kN range
```

### Phase 4: Spacecraft (2038–2045)

```
    ⬜ Uncrewed Mars orbiter (resonance propulsion)
    ⬜ Uncrewed Mars lander (round trip)
    ⬜ Crewed shuttle: Earth → Mars → Earth (45–90 days)
```

### Phase 5: Routine Operations (from 2045)

```
    ⬜ Regular Mars shuttle flights
    ⬜ Outer solar system: Jupiter, Saturn (60–90 days)
    ⬜ Permanent lunar base supply (Earth↔Moon: hours)
    ⬜ Interstellar probe (Proxima Centauri, ~43 years)
```

---

## 9. Comparison of All Propulsion Concepts

| Drive | I_sp (s) | Thrust/weight | Mars trip | Fuel/100t | Status |
|-------|----------|--------------|-----------|-----------|--------|
| Chemical (LOX/LH₂) | 450 | >1 | 7–9 mo. | 1,200 t | Operational |
| Chemical (LOX/CH₄, Raptor) | 380 | >1 | 6–9 mo. | 1,200 t | Development |
| Ion drive (Xe) | 5,000 | 10⁻⁵ | 2–3 years | 47 t | Operational |
| VASIMR (Plasma) | 30,000 | 10⁻⁴ | 39 days | 8 t | Development |
| Nuclear thermal (NERVA) | 900 | ~0.3 | 4–6 mo. | 400 t | Demonstrated |
| Nuclear electric | 10,000 | 10⁻⁴ | 1–2 years | 22 t | Concept |
| Orion (nuclear pulses) | 50,000 | ~1 | 30 days | 4 t | Concept |
| **Resonance impulse (RFT)** | **1,300,000** | **up to 7.6** | **30–45 days** | **100 g** | **Concept** |

---

## 10. Economic Significance

### 10.1 Cost per kg to Mars

```
    Starship (SpaceX, target):   ~100,000 USD/kg
    → 100 t payload: 10 billion USD per mission

    Resonance Shuttle:
    Fuel: 100 g Pu-239 ≈ 500 USD (material value)
    FEL power: ~10,000 USD (per launch)
    Maintenance/depreciation: ~50,000 USD/mission
    → 100 t payload: ~60,000 USD per mission
    → ~0.60 USD/kg to Mars

    Factor: ~170,000× cheaper per kg
```

### 10.2 Market Potential

```
    Short-term (2040–2050):
    — Mars missions (research, colony): 10–50 billion USD/y
    — Lunar supply (base, mining): 5–20 billion USD/y
    — Satellite maneuvering (GEO repositioning): 2–5 billion USD/y

    Long-term (2050+):
    — Interplanetary trade: 100+ billion USD/y
    — Asteroid mining: 50–200 billion USD/y
    — Interstellar exploration: Not quantifiable

    Total market (2040–2070): ~500 billion–1 trillion USD
```

### 10.3 Synergies with Resonance Reactor (Disposal)

```
    Fuel = nuclear waste:
    — Pu-239 from reprocessing → shuttle fuel
    — Am-241 from old smoke detectors → shuttle fuel
    — No separate fuel production pathway required
    — Disposal problem becomes fuel supply

    Global Pu-239 reserve: ~1,500 t
    Missions (at 100 g each): ~15,000,000 Mars round trips
    → Fuel for millennia
```

---

## 11. Summary

| Key Statement | Value |
|---------------|-------|
| Specific impulse | 1.3 × 10⁶ s (1,000× chemical) |
| Fuel for Mars round trip | 100 g Pu-239 (instead of 1,200 t LOX/CH₄) |
| Travel time Earth↔Mars | 30–45 days (instead of 6–9 months) |
| SSTO possible | Yes (mass ratio ≈ 1.0) |
| Reusable | ~1,000 missions per fuel load |
| Cost per kg to Mars | ~0.60 USD (instead of ~100,000 USD) |
| Thrust control | Via Δφ: continuously variable, nanosecond response |
| Inherently safe | No thrust without photons |
| Fuel | Nuclear waste (Pu-239, Am-241) |
| Physical basis | E = π · ε · ℏ · f, κ = 1 |
| Interstellar | Proxima Centauri in ~43 years (10% c) |

```
    The equation that revolutionizes space travel:

    Δv = 1.3 × 10⁷ m/s · ln(m_start / m_end)

    At m_start/m_end ≈ 1.0 (resonance propulsion):
    → Any Δv is achievable
    → Fuel is no longer a limiting factor
    → The solar system becomes accessible
```

---

## References

- Tsiolkovsky, K.E. (1903): Exploration of Outer Space by Means
  of Rocket Devices
- Berman, B.L., Fultz, S.C. (1975): Rev. Mod. Phys. 47, 713
- Schmidt, G.R. et al. (2002): Nuclear Pulse Propulsion — Orion
  and Beyond. AIAA 2000-3856
- Frisbee, R.H. (2003): Advanced Space Propulsion for the 21st
  Century. J. Propulsion and Power 19(6)
- SpaceX (2024): Starship Users Guide, Rev. 1.0
- Schu, D.-R. (2025/2026): Resonance Field Theory
  ([GitHub](https://github.com/DominicReneSchu/public))

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---
