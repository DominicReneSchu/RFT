# Resonance Field Theory (Version 4.0)

[![License: RFT-License 1.4](https://img.shields.io/badge/License-RFT--License%201.4-blue.svg)](license/RFT-license_v1.4.md)

Welcome to the official repository of the **Resonance Field Theory (RFT)**.
This project unifies mathematics, physics, and engineering into
an axiomatic model of resonance. The theory describes
fundamental processes as coupling and resonance phenomena in
oscillation fields — formally grounded in 8 axioms (A1–A8).

**Empirically validated in six domains:** Particle physics
(1,500,000 Monte Carlo simulations, 5 resonances, emp. p = 0),
Cosmology (1,530 FLRW simulations, Δd_η > 6σ),
Nuclear technology (resonance reactor, κ = 1, λ_eff/λ₀ = 7,872 for U-235),
Classical mechanics (double pendulum, ε(θ₂−θ₁) = cos²(Δθ/2)),
Quantum mechanics (Schrödinger simulation, Fidelity = 1.0, 1−F ~ λ²) and
Spacetime physics (warp drive — first positive-energy warp bubble).

---

## ☰ Table of Contents

- [Core Formula and Central Quantities](#core-formula-and-central-quantities)
- [Axiom System (Summary)](#axiom-system-summary)
- [Empirical Validation](#empirical-validation)
- [PDF Summary](#pdf-summary)
- [Peer Review](#peer-review)
- [Resonance Field Theory (RFT) – The Universe as a Resonance Bubble](#resonance-field-theory-rft--the-universe-as-a-resonance-bubble)
- [How Results Confirm Each Other](#how-results-confirm-each-other)
- [Contents](#contents)
    - [Axiomatics and Definitions](#axiomatics-and-definitions)
    - [Mathematics and Physics](#mathematics-and-physics)
    - [Concepts](#concepts)
    - [Simulations](#simulations)
    - [Empirical Evidence](#empirical-evidence)
    - [Explanations](#explanations)
    - [Analysis Tools](#analysis-tools)
    - [Theoretical Foundations](#theoretical-foundations)
    - [RT-40 Applications: Relativity and Lorentz](#rt-40-applications-relativity-and-lorentz)
    - [RT-42 Cosmology: Friedmann Analogy from Phase Dynamics](#rt-42-cosmology-friedmann-analogy-from-phase-dynamics)
- [License](#license)
- [Research Tasks](#research-tasks)

---

## Core Formula and Central Quantities

The central equation of Resonance Field Theory (Axiom 4):

$$
E = \pi \cdot \varepsilon(\Delta\phi) \cdot \hbar \cdot f
$$

| Symbol | Name | Meaning |
|:------:|:-----|:--------|
| **π** | Pi | Geometric factor from the cyclic coupling geometry |
| **ε(Δφ)** | Coupling efficiency | Fraction of transferred resonance energy, ε ∈ [0, 1] |
| **ℏ** | Red. Planck constant | Action quantum (ℏ = h/2π) |
| **f** | Frequency | Oscillation frequency of the coupled mode |

### Coupling Efficiency ε

The coupling efficiency describes what fraction of the maximum
possible resonance energy is actually transferred between two coupled
modes.

**Standard model:** ε(Δφ) = cos²(Δφ/2) = ½(1 + cos Δφ)

| Coupling state | ε | Energy |
|----------------|---|--------|
| Perfect coupling (Δφ = 0) | 1 | π·ℏ·f |
| Planck special case (ground state) | 1/(2π) ≈ 0.159 | ½·ℏ·f |
| Natural damping | 1/e ≈ 0.368 | (π/e)·ℏ·f |
| Half coupling (Δφ = π/2) | 0.5 | π·ℏ·f/2 |
| No coupling (Δφ = π) | 0 | 0 |

The factor π arises from the integration of the coupling efficiency
over a half-cycle of phase space — not as a free parameter.
The Planck ground-state energy E = ½ℏf is the special case
ε = 1/(2π).

### Identity ε = η

The FLRW simulations show: the theoretical operator ε and
the measurable observable η (cross-term of two coupled
scalar fields) are identical:

$$
\varepsilon(\Delta\phi) = \eta(\Delta\phi) = \cos^2(\Delta\phi / 2)
$$

This identity eliminates the last free parameter:
In the resonance reactor κ = 1 follows exactly.

Complete definition: [Coupling efficiency](facts/docs/definitions/coupling_efficiency.md)

---

## Why This Theory? — The Founding Idea

RFT arose from a simple but far-reaching observation:

> **π is not an irrational number of nature — it is an artifact of our base-10 representation.**

A circle with radius 1 has a perfectly finite, measurable circumference. The infinity of 3.14159… is not a property of the circle — it is a property of the arbitrary decimal encoding. In a number system with π as its base, π = 10: rational and finite.

Drawing the same conclusion as with Planck units (c = ℏ = 1): **π is the natural unit of cyclic completeness** — the measure of one half-oscillation in phase space. The factor π in

$$E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$$

thus loses its status as a free numerical postulate and becomes a geometric necessity.

At the same time, standard physics treats energy as a scalar — yet torque (M⃗ = r⃗ × F⃗, unit J), spin (SU(2) algebra, Zeeman effect), and the Lorentz 4-vector (E/c, p⃗) all point structurally toward vectoriality. RFT makes this explicit: **energy has direction in the resonance field** (Axiom A5).

These two observations — π as a phase-space constant and energy as a vector — are the conceptual origin of the entire theory.

→ [Full exposition: π and e as Fundamental Constants of Space](facts/theory/pi_as_fundamental_constant.md)

---

![Visualization of Resonance Field Theory](images/visualization_RFT.png)

*Fig. 1: Symbolic representation of the interaction of π, ℏ, ε and f in resonance space*

---

## Axiom System (Summary)

The RFT consists of 8 core axioms:

| Axiom | Core statement | Formula | Status (Aug 2026) |
|-------|----------------|---------|-------------------|
| A1 | Universal oscillation | ψ = A·cos(kx − ωt + φ) | Postulate |
| A2 | Superposition | Φ = Σ ψᵢ | Postulate |
| A3 | Resonance condition | \|f₁/f₂ − m/n\| < δ | **Corollary from A7** (RT-02, RT-35) |
| A4 | Coupling energy | E = π·ε·ℏ·f | π: **geometrically derived** (RT-01, RT-01b); ε=cos²(Δφ/2): **representation-theoretically unique** (RT-02) |
| A5 | Energy direction | E⃗ = E·ê(Δφ, ∇Φ) | **Irreducible postulate** (RT-36) |
| A6 | Information flow | MI > 0 ⟺ PCI > 0 | Postulate |
| A7 | Invariance (G_sync) | G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) | **Algebraically proved** (RT-02) |
| A8 | Coupling wave velocity | c = 1/√(μ₀ε₀) | **Irreducible postulate** (RT-41) |

Additionally there is an interpretative extension:
- **E1 (Observer as resonator):** Follows from A1, A3, A6

Complete formalization: [Axiomatic Foundation](facts/docs/definitions/axiomatic_foundation.md)

---

## Empirical Validation

The RFT is empirically validated across six independent domains:

| Domain | Method | Result | Axioms |
|--------|--------|--------|--------|
| Particle physics | 1,500,000 MC sim. on CMS data | 5 resonances, emp. p = 0 | A3, A7 |
| Cosmology | 1,530 FLRW simulations | Δd_η > 6σ, Δχ² = +16 vs CMB | A1, A3–A5, A7 |
| Nuclear technology | Resonance reactor (GDR-based) | κ = 1, λ_eff/λ₀ = 7,872 (U-235) | A1, A3, A4 |
| Classical mechanics | Double pendulum + coupled oscillators | ε(θ₂−θ₁) = cos²(Δθ/2) | A1, A2, A4 |
| Quantum mechanics | Schrödinger simulation | Derivation of Schrödinger eq. from A4; Fidelity = 1.0 (4 scenarios); 1−F ~ λ² confirmed | A4 |
| Spacetime physics | Warp drive simulation | First positive-energy warp bubble; w sign change via ε(Δφ) phase control | A4, A5 |

**Falsification tests:**
- Monte Carlo test: 1,500,000 simulations, 5 resonances, emp. p = 0 (A3 confirmed)
- CERN resonance analysis: significant resonance excesses in mass data (A1, A3, A7)
- Resonance reactor prediction: σ_coh > σ_incoh (experimentally testable)
- Schrödinger simulation: falsifiable prediction |Δ⟨x⟩| ≈ 2.0·λ µm for ⁸⁷Rb atoms

---

## PDF Summary

The detailed summary of Resonance Field Theory as a PDF:
[**rft_summary.pdf**](./rft_summary.pdf)

---

## Peer Review

A peer review process is actively being pursued:
[**rft_manuscript_en_iop.pdf**](peer_review_rft/manuscript_en/rft_manuscript_en_iop.pdf)

**Submission preparation (RT-39, August 2026):** All submission materials for the Journal of Physics Communications (IOP Publishing) have been prepared and are available in [`peer_review_rft/submission/`](peer_review_rft/submission/):
- [Cover Letter](peer_review_rft/submission/cover_letter_jphyscomm.md)
- [Submission Checklist](peer_review_rft/submission/submission_checklist.md)
- [Response-to-Reviewers Template](peer_review_rft/submission/response_to_reviewers_template.md)
- [Journal Selection Rationale](peer_review_rft/submission/journal_selection.md)
- [Manuscript Review Report](peer_review_rft/submission/manuscript_review_report.md)
- [Figures Overview](peer_review_rft/manuscript_en/figures/README.md)

---

## Resonance Field Theory (RFT) – The Universe as a Resonance Bubble

> ⚠️ **Note:** The following sections develop the physical structure of the universe as a coherent resonance field. They extend beyond the axiomatic core and are to be understood as interpretive extensions within the physically derivable framework.
> 
[Resonance Field Theory (RFT) – The Universe as a Resonance Bubble](facts/docs/explanations/the_universe_as_a_resonance_bubble.md)

---

## How Results Confirm Each Other

Resonance Field Theory states that resonance is the **connecting element of physics**.
This connection becomes visible because the same formula is confirmed in completely
independent domains — from different directions, at different scales.

### ε(Δφ) = cos²(Δφ/2) — one formula, three scales

| Domain | Simulation/Evidence | Result | Link |
|--------|---------------------|--------|------|
| Quantum mechanics | Schrödinger simulation | Fidelity = 1.000000000000 for all 4 Δφ scenarios | [→](facts/simulations/schrodinger/README.md) |
| Cosmology | FLRW simulation (1,530 runs) | η = cos²(Δφ/2) exact, Δd_η > 6σ | [→](facts/simulations/FLRW_simulations/README.md) |
| Nuclear physics | Resonance reactor (U-235) | κ = 1 exact, λ_eff/λ₀ = 7.872 | [→](facts/concepts/resonance_reactor/resonance_reactor.md) |
| Classical mechanics | Double pendulum, coupled oscillators | ε(θ₂−θ₁) = cos²(Δθ/2) | [→](facts/simulations/double_pendulum/accompanying_chapter_double_pendulum.md) |
| Spacetime geometry | Warp drive simulation | ρ ∝ cos⁴(Δφ/2), E⁻ = 0 | [→](facts/concepts/warp_drive/warp_drive.md) |

### Resonance condition (A3) — confirmed from three independent directions

| Evidence | Method | Result | Link |
|---------|--------|--------|------|
| CERN resonance analysis | CMS Open Data | Significant resonance excesses, A7 confirmed | [→](facts/empirical/cern/documentation.md) |
| Monte Carlo test | 1,500,000 simulations | 5 resonances, emp. p = 0 | [→](facts/empirical/monte_carlo/monte_carlo_test/monte_carlo.md) |
| Resonance reactor | GDR-based | f_γ = f_GDR condition, σ_coh > σ_incoh | [→](facts/concepts/resonance_reactor/resonance_reactor.md) |

### Cross-connections in detail

```
Schrödinger ──ε(Δφ)──→ FLRW ──Klein-Gordon──→ Warp drive
     │                    │                          │
  Fidelity=1          η = cos²              ρ ∝ cos⁴, E⁻=0
     │                    │                          │
     └──Perturbation──→ Numerical Demo    Cascade Stage 3
                          │                          │
                     Consistency A3–A5   Resonance reactor (Stage 1)
                                                     │
                     CERN ←─ A3 ─→ Monte Carlo ──────┘
```

> **One equation — E = π·ε(Δφ)·ℏ·f — confirmed across quantum mechanics, cosmology, nuclear physics, and spacetime geometry.**

---

# Contents

## Axiomatics and Definitions

| # | Document | Axioms | Description |
|---|----------|--------|-------------|
| 1 | [Axiomatic Foundation](facts/docs/definitions/axiomatic_foundation.md) | A1–A8 | Formal axioms A1–A8 with proofs and empirical tests |
| 2 | [Coupling Efficiency ε](facts/docs/definitions/coupling_efficiency.md) | A1–A7 | Unified definition, ε = η identity |
| 3 | [Energy as Fundamental Quantity](facts/docs/definitions/energy_as_fundamental_constant.md) | A1–A5, A7 | Interpretative hypothesis: all quantities from E |
| 4 | [Resonance Lexicon](facts/docs/definitions/resonance_lexicon.md) | A1–A7 | Glossary of RFT terms |
| 5 | [Resonance-Logical ODEs](facts/docs/definitions/resonance_logical_differential_equations.md) | A1–A4, A6, A7 | Classical ODEs as projections of the rODE |

## Mathematics and Physics

| # | Document | Axioms | Description |
|---|----------|--------|-------------|
| 1 | [Resonance Integrals](facts/docs/mathematics/resonance_integrals.md) | A1–A4, A7 | Analytical methods — Dirichlet integral as resonance energy |
| 2 | [Resonance Field Equation](facts/docs/mathematics/resonance_field_equation.md) | A1, A3, A5, A6 | Central energy equation E = π·ε·ℏ·f |
| 3 | [Coupling Energy: Special Cases](facts/docs/mathematics/coupling_energy.md) | A4 | Limit cases ε = 1, 1/(2π), 1/e, 0 |
| 4 | [Resonance Time Coefficient τ*](facts/docs/mathematics/tau_resonance_coefficient.md) | A4 | Time scale of coupling: τ*(Δφ) = π/ε(Δφ) |
| 5 | [Energy Direction](facts/docs/mathematics/energy_direction.md) | A2, A4, A5, A6 | Energy as a vector with sense of rotation |
| 6 | [Energy Sphere](facts/docs/mathematics/energy_sphere.md) | A1, A2, A4, A5, A7 | Geometric model — phase structure and dark energy |
| 7 | [Resonance Energy Vector](facts/docs/mathematics/resonance_energy_vector.md) | A4, A5 | Energy as a directional quantity in resonance space |
| 8 | [Energy Transfer](facts/docs/mathematics/energy_transfer.md) | A1, A3, A4, A6 | Principles and equations of transfer |
| 9 | [Resonance Coordinates](facts/docs/mathematics/resonance_coordinates.md) | A1, A4 | Half-angle tangent parametrization |
| 10 | [Double Pendulum](facts/docs/mathematics/double_pendulum.md) | A1, A2, A4 | Classical mechanics and RFT perspective |

---

## Concepts

| # | Concept | Axioms | Description |
|---|---------|--------|-------------|
| 1 | [ResoCalc](facts/concepts/ResoCalc/resocalc.md) | A1, A3, A4 | Torque calculation in resonance field |
| 2 | [Resonance Reactor](facts/concepts/resonance_reactor/README.md) | A1, A3–A7 | Reactor concept — overview and introduction |
| 2a | [Resonance Reactor — Main Document](facts/concepts/resonance_reactor/resonance_reactor.md) | A1, A3–A7 | Complete description of the resonance reactor concept |
| 2b | [Experimental Proposal Am-241](facts/concepts/resonance_reactor/experimental_proposal_am241.md) | A1, A3, A4 | Falsifiable experimental proposal: phase-dependent photoexcitation of Am-241 at the GDR |
| 2c | [Simulation Results — Resonance Reactor](facts/concepts/resonance_reactor/simulation_results.md) | A1, A3, A4 | Quantitative simulation results of the resonance reactor |
| 2d | [Cost-Benefit Analysis — Resonance Reactor](facts/concepts/resonance_reactor/cost_benefit_analysis.md) | A1, A3, A4 | Quantitative assessment based on RFT simulation results |
| 2e | [Resonance Impulse Drive](facts/concepts/resonance_reactor/impulse_drive.md) | A1, A4, A5 | Directed fission as a space propulsion system |
| 3 | [Warp Drive — Overview](facts/concepts/warp_drive/README.md) | A1, A4, A5 | Introduction and overview of the warp drive concept |
| 3a | [Warp Drive — Main Document](facts/concepts/warp_drive/warp_drive.md) | A1, A4, A5 | Propulsion concept — **first positive-energy warp bubble simulation** (E⁻ = 0); w sign change; RT-33: scaling law ρ∝R⁻², R*>>1 AU ([analysis](facts/concepts/warp_drive/analyse/rt33_energy_gap.py)) |

---

## Simulations

| # | Simulation | Axioms | Description |
|---|------------|--------|-------------|
| 1 | [Resonance Field](facts/simulations/resonance_field/simulation_resonance_field_theory.md) | A1–A5 | Two oscillators, coupling efficiency, energy direction |
| 2 | [Double Pendulum](facts/simulations/double_pendulum/accompanying_chapter_double_pendulum.md) | A1, A2, A4 | Classical double pendulum with dynamic coupling efficiency ε(θ₂−θ₁) — RT-08: χ² fit 🔬 ([Analysis](facts/simulations/double_pendulum/analyse/rt08_double_pendulum_comparison.py)) — RT-38: [Experiment protocol](facts/simulations/double_pendulum/experiment/protocol_rt38.md) 🧪 |
| 3 | [Coupled Oscillators](facts/simulations/coupled_oscillators/coupled_oscillators.md) | A1–A4 | Energy exchange, resonance detection, live animation |
| 4 | [Numerical Demonstration](facts/simulations/numerical_demonstration/README.md) | A3, A4, A5 | Consistency demonstration: resonance energy, coupling efficiency, and entropy over (A, τ) |
| 4a | [Numerical Demonstration — Accompanying Chapter](facts/simulations/numerical_demonstration/accompanying_chapter_numerical_demonstration.md) | A3, A4, A5 | Extended accompanying chapter for the numerical demonstration |
| 4b | [Numerical Demonstration — Documentation](facts/simulations/numerical_demonstration/docs/index.md) | A3, A4, A5 | Technical documentation and index |
| 5 | [FLRW Simulations](facts/simulations/FLRW_simulations/README.md) | A1–A7 | 1,530 runs, η ≈ cos², Δd_η > 6σ |
| 6 | [Schrödinger Simulation](facts/simulations/schrodinger/README.md) | A4 | Derivation of Schrödinger eq. from Axiom 4; Fidelity = 1.0 (all 4 scenarios); perturbation theory 1−F ~ λ² confirmed; falsifiable prediction for ⁸⁷Rb |
| 6a | [Schrödinger — Experimental Proposal](facts/simulations/schrodinger/docs/experimental_proposal.md) | A4 | Falsifiable experimental proposal for ⁸⁷Rb-BEC in a harmonic trap |
| 6b | [Schrödinger — Research Programme (Roadmap)](facts/simulations/schrodinger/docs/schrodinger_roadmap.md) | A4 | Schrödinger starting track: research programme and minimal proof |
| 7 | [Hamilton Simulations](facts/simulations/hamilton/README.md) | A1, A3, A4 | RT-31: Resonance Hamiltonian operator — phonon coupling and spin-orbit coupling |

---

## Empirical Evidence

| # | Evidence | Axioms | Description |
|---|---------|--------|-------------|
| 1 | [Resonance Analysis in Mass Data](facts/empirical/cern/documentation.md) | A1, A3, A7 | CERN data: significant resonance excesses |
| 2 | [Monte Carlo Test](facts/empirical/monte_carlo/monte_carlo_test/monte_carlo.md) | A1, A3, A7 | 1,500,000 simulations, 5 resonances, emp. p = 0 |
| 2a | [Monte Carlo — Publication Report](facts/empirical/monte_carlo/monte_carlo_test/publication_results/main_report/resonance_report.md) | A1, A3, A7 | Full publication report of the Monte Carlo analysis |
| 2b | [Monte Carlo — Analysis Report](facts/empirical/monte_carlo/monte_carlo_test/report_out/resonance_report.md) | A1, A3, A7 | Auto-generated analysis report from the Monte Carlo simulation |


---

## Explanations

| # | Explanation | Axioms | Description |
|---|-------------|--------|-------------|
| 1 | [Swarm Resonance](facts/docs/explanations/swarm_resonance.md) | A1–A7 | Why flocks of birds don't collide — and why RFT opens new doors |
| 2 | [Resonance Across Physics](facts/docs/explanations/resonance_across_physics.md) | A1–A7 | How one pattern connects mechanics, thermodynamics, electrodynamics, QM, and relativity |
| 3 | [RFT — Consistency Review: Universe as a Resonance Bubble](facts/docs/explanations/rft_consistency_review_resonance_bubble.md) | A1–A7 | Formal companion study: consistency check of the core claims from "The Universe as a Resonance Bubble" |

---

## Analysis Tools

| # | Document | Axioms | Description |
|---|----------|--------|-------------|
| 1 | [Social Analysis](facts/docs/analysis_tools/social_analysis.md) | A1–A7 | RFT analysis instrument for social dynamics – AI context prompt for pattern recognition in news reports; Version 2.10: usage guide extended with projection and retrodiction; §1.11a retrodiction as formal method; time-modes section added to preamble |

---

## Theoretical Foundations

| # | Document | Axioms | Description |
|---|----------|--------|-------------|
| 1 | [π and e as Fundamental Constants of Space](facts/theory/pi_as_fundamental_constant.md) | A4, A5 | Founding idea of RFT: π as geometric phase-space constant, vectorial nature of energy — **✅ RT-01a complete (Aug 2026)** |
| 2 | [Action Integral Derivation of π](facts/theory/action_integral_pi_derivation.md) | A4 | Formal derivation of π as the saddle-point contribution of the stationary phase in the path integral (RT-01, Aug 2026) |
| 3 | [G_sync — Group Structure and Invariance Proofs](facts/theory/gsync_group_structure.md) | A7 | Group-theoretic proof: G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ); uniqueness of cos²(Δφ/2); RT-02, Aug 2026 |
| 4 | [A5 Derivation: ê(Δφ, ∇Φ) from G_sync](facts/theory/a5_vektorialitaet_herleitung.md) | A5 | RT-36: ê is an irreducible postulate — D-generator forces ∂_t Φ, not ∇Φ; formal justification for RT-01a; Aug 2026 |
| 5 | [RT-41 — Axiom A8: Coupling Wave Speed](facts/theory/rt41_axiom_a8_coupling_wave.md) | A1–A7 | Derivation or irreducible postulate of the coupling wave speed (Sep 2026) |
| 6 | [RT-01b — Numerical Path Integral: π Derivation](facts/theory/simulations/rt01b/README.md) | A4 | Numerical verification of the π derivation via path integral simulation |
| 7 | [Peer Review Readiness](../PEER_REVIEW_READINESS.md) | — | Status of all open formalisation steps and theoretical foundations against peer-review criteria |

---

## RT-40 Applications: Relativity and Lorentz

Formal applications of RFT to relativistic physics (RT-40, Sep 2026):

| # | Document | Axioms | Description |
|---|----------|--------|-------------|
| 1 | [AP1 — Phase ↔ Rapidity](facts/theory/rt40_ap1_phase_rapidity.md) | A1, A4, A5 | Formal identification: resonance-field-theoretic phase and relativistic rapidity |
| 2 | [AP2 — Coupling Efficiency in the Lorentz Frame](facts/theory/rt40_ap2_coupling_efficiency_lorentz.md) | A1, A4 | Behaviour of ε(Δφ) under Lorentz transformation |
| 3 | [AP3 — Lorentz Transformation from RFT](facts/theory/rt40_ap3_lorentz_transformation.md) | A1, A4, A7 | Derivation of the Lorentz transformation from the RFT formalism |
| 4 | [AP4 — Speed of Light as a Limiting Case](facts/theory/rt40_ap4_speed_of_light_limit.md) | A1, A4 | c as an emergent limiting case of Resonance Field Theory |
| 5 | [AP5 — Time Dilation and Length Contraction](facts/theory/rt40_ap5_time_dilation_length_contraction.md) | A1, A4, A5 | Time dilation and length contraction in the RFT framework |
| 6 | [AP6 — Falsifiability and SRT Distinction](facts/theory/rt40_ap6_falsifiability_srt_distinction.md) | A1–A7 | Falsifiable predictions and distinction from Special Relativity |
| 7 | [AP7 — Warp Drive: Consistency Check](facts/theory/rt40_ap7_warp_consistency_check.md) | A1, A4, A5 | Formal consistency check of the warp drive concept in the Lorentz framework |

---

## RT-42 Cosmology: Friedmann Analogy from Phase Dynamics

Formal applications of RFT to cosmology (RT-42, Sep 2026):

| # | Document | Axioms | Description |
|---|----------|--------|-------------|
| 1 | [AP1 — Phase ↔ Scale Factor](facts/theory/rt42_ap1_phase_scale_factor.md) | A1, A4, A8 | Formal analogy: RFT phase difference as dynamic variable of the cosmic scale factor — **✅ RT-42 AP1 completed (Sep 2026)** |
| 2 | [AP2 — Time Derivative of the Phase](facts/theory/rt42_ap2_time_derivative_phase.md) | A4, A5, A8 | Closed ODE Δφ̇ = β·tan(Δφ/2) from coupling dynamics; Hubble parameter H(t) = H₀√ε(t) derived analytically — **✅ RT-42 AP2 completed (Sep 2026)** |
| 3 | [AP3 — Connection to Λ or Dark Energy](facts/theory/rt42_ap3_connection_lambda_dark_energy.md) | A1, A4, A5, A8 | RFT explains Λ as the effective limiting case of a static super-horizon gradient; w_eff ∈ [−1, +1/3]; ΛCDM as special case (β → 0, k₀ = const) — **✅ RT-42 AP3 completed (Sep 2026)** |
| 4 | [AP4 — Scaling Problem: Cosmological Classification](facts/theory/rt42_ap4_scaling_problem_cosmology.md) | A1, A4, A5, A8 | 28-orders discrepancy (ρ_warp ~ 10¹⁹ J/m³ vs. ρ_Λ ~ 10⁻⁹ J/m³) identified as an apparent problem: k_warp ~ 10⁻² m⁻¹ (local) ≠ k₀ ~ 10⁻²⁶ m⁻¹ (cosmological); different regimes, different energy formulas — **✅ RT-42 AP4 completed (Sep 2026)** |
| 5 | [AP5 — Falsifiable Deviations from ΛCDM](facts/theory/rt42_ap5_falsifiable_deviations_lcdm.md) | A1, A4, A5, A8 | Four measurable deviations from ΛCDM identified: dynamic w(z) = w₀ + w_a·z/(1+z) with w_a ≈ β/H₀; modified H(z) (≤ 3 %); suppressed structure growth Δ(fσ₈) ≤ 1 %; reduced ISW signal at ℓ < 20. Primary falsification criterion: w_a = 0 (5σ) forces β = 0 (ΛCDM limit). DESI DR5 and Euclid decisive — **✅ RT-42 AP5 completed (Sep 2026)** |
| 6 | [AP6 — Cosmic Expansion as a Phase Effect](facts/theory/rt42_ap6_cosmic_expansion_phase_effect.md) | A1, A4, A5, A8 | Hypothesis confirmed: ȧ/a = H₀·cos(Δφ/2) fully derived from A1–A8. Scenario A (Δφ = const): de Sitter fixed point and generalised de Sitter. Scenario B (β > 0): slow-roll inflation; n_s ∈ [0.97, 0.99] Planck-consistent. Scenario C (β < 0): accelerated expansion; explains DESI DR1 signal (w_a < 0). Time-varying k₀(t): dynamic Λ_eff(t). Three new falsification criteria (F6–F8) — **✅ RT-42 AP6 completed (Sep 2026)** |

---

## License

This project is licensed under the **RFT-License 1.4**
→ [View license text](license/RFT-license_v1.4.md)
→ [Changelog](license/CHANGELOG.md)

---

## Research Tasks

→ [Research tasks and open items](../RESEARCH_TASKS.md)

---

© Dominic-René Schu — Resonance Field Theory 2025/2026
