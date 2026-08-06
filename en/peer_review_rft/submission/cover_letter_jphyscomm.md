# Cover Letter — Journal of Physics Communications

*Dominic-René Schu — August 2026*

---

**To:**
The Editor
Journal of Physics Communications
IOP Publishing
Temple Circus, Temple Way
Bristol BS1 6HG
United Kingdom

---

Dear Editor,

## 1. Submission Statement

I hereby submit the manuscript

> **"Resonance Field Theory: Axiomatics, Fundamental Formula, and Empirical Validation"**

by Dominic-René Schu (ORCID: 0009-0004-9769-9061) for consideration as an **Original Research Article** in the *Journal of Physics Communications*.

---

## 2. Core Statement

Resonance Field Theory (RFT) is an axiomatic framework that derives a phase-dependent extension of the Planck relation, E = π · ε(Δφ) · ℏ · f, from seven hierarchically structured axioms. The central result is that the factor π in this formula is not a free normalization parameter but emerges geometrically from the stationary-phase contribution of the action integral over a half-cycle of phase space (RT-01, RT-01b); and that the coupling efficiency ε(Δφ) = cos²(Δφ/2) is the unique function satisfying all boundary conditions within the k=1 irreducible representation of U(1) ⊂ G_sync, the theory's symmetry group (RT-02). The theory is empirically validated across four independent physical domains — particle physics, cosmology, nuclear physics, and quantum mechanics — and two concrete falsifiable experimental proposals are presented with numerically specified decision criteria.

*Journal of Physics Communications* is the appropriate venue because the manuscript communicates a significant original result that simultaneously (a) introduces a formally structured axiomatic framework, (b) presents cross-domain empirical validation with quantified significance, and (c) provides experimentally testable predictions accessible to existing laboratory infrastructure.

---

## 3. Distinction from Prior Work

RFT is not a reformulation of existing oscillator physics. Three features distinguish it from prior frameworks:

**3.1 π as a derived geometric constant (RT-01, RT-01b)**
In the standard Planck relation E = ℏω, the factor of 2π is built into the definition of ω. In RFT, π appears explicitly in the coupling-energy formula E = π · ε · ℏ · f as a result of integrating the saddle-point contribution of the action integral S[φ] = ∫₀^π ε(φ) dφ over one half-period of the resonance cycle. The numerical confirmation (|c₃ + c₄| ≈ 5.5 × 10⁻¹¹, RT-01b) shows this is not an arbitrary normalization choice. The falsification condition is explicit: any measurement demonstrating that the phase-integrated coupling energy deviates from π · ε · ℏ · f by more than the numerical precision of the saddle-point calculation would refute the derivation.

**3.2 ε = cos²(Δφ/2) as representation-theoretically forced (RT-02)**
The coupling efficiency function is not chosen phenomenologically. Within the symmetry group G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ), the k=1 irreducible representation of U(1) admits exactly one function F: [0, 2π] → [0,1] satisfying ε(0) = 1, ε(π) = 0, parity ε(Δφ) = ε(−Δφ), and non-mixing of higher representations (k ≥ 2). That function is cos²(Δφ/2). All other smooth functions satisfying the boundary conditions mix higher-dimensional representations. The uniqueness theorem is stated and proved in §3.3 of the manuscript.

**3.3 A3 as a corollary, not an independent axiom (RT-02, RT-35)**
The resonance condition |f₁/f₂ − m/n| < δ (Axiom A3 in prior versions of RFT) is derived as a corollary of Axiom A7 (invariance under G_sync) and is no longer counted as an independent postulate. This reduces the axiom count from seven to six effective independent postulates.

**3.4 Falsifiable predictions with quantified criteria**
Two experimental proposals include specific falsification thresholds: (I) SNR ≥ 3σ for Am-241 photo-excitation at ELI-NP with 100 h beam time at a realistic parameter scenario (SNR_median ≈ 10σ at 100 h; conservative scenario requires ≈516 h for 5σ); (II) center-of-mass shift |Δ⟨x⟩| ≈ 2.0 · λ μm for ⁸⁷Rb BEC in a harmonic trap at Δφ = π, testable with existing BEC apparatus. Neither prediction follows directly from other established frameworks.

---

## 4. Empirical Reach

The manuscript presents validation across four independent domains:

| Domain | Method | Key Result |
|--------|--------|------------|
| Particle physics | 1,500,000 Monte Carlo simulations on CMS Open Data dielectron events | 5 known resonances detected (φ(1020), J/ψ, Υ(1S), Υ(2S), Z), empirical p = 0, stable across 3 KDE bandwidths and 10 seeds |
| Cosmology | 1,530 coupled FLRW simulations | η(Δφ) ≈ cos²(Δφ/2) emergent, Δd_η > 6σ, Δχ² = +16 vs Planck-2018 CMB data |
| Nuclear physics | Resonance reactor simulation with κ = 1 (no free parameter) | Fission break-even Q ≈ 1.0, λ_eff/λ₀ = 7,872 for U-235 |
| Quantum mechanics | Schrödinger simulation (5 derivation steps) | Fidelity = 1.0 (all 4 Δφ scenarios), perturbation theory 1 − F ∼ λ² confirmed |

The combined statistical evidence across 1,500,000 Monte Carlo runs on real CMS data constitutes a direct empirical test, not a purely theoretical simulation.

---

## 5. Open Science Statement

All derivations, source code, simulation scripts, and raw data underlying this manuscript are openly and permanently available at:

**https://github.com/DominicReneSchu/RFT**

This includes all RT-series analyses (RT-01 through RT-38), the double pendulum experiment protocol (RT-38, reproducible with ≈200 EUR and a smartphone), and the full backtest infrastructure for ResoTrade (RT-10). The repository is public and version-controlled. No code or data have been withheld.

---

## 6. Suggested Reviewers

The manuscript spans particle physics, mathematical physics, cosmology, and quantum mechanics. The following researchers have relevant expertise and active publication records in the respective subfields.

**Particle Physics / Resonance Physics (CMS/ATLAS environment)**

1. **Dr. Günter Dissertori**
   ETH Zürich, Institute for Particle Physics and Astrophysics
   *Expertise:* CMS collaboration, resonance searches in dielectron/dimuon channels, high-luminosity LHC phenomenology
   Contact: dissertori@phys.ethz.ch

2. **Dr. Markus Klute**
   MIT, Laboratory for Nuclear Science / CMS Collaboration
   *Expertise:* Higgs boson physics, resonance structure in CMS data, precision SM measurements
   Contact: mklute@mit.edu

**Mathematical Physics (Group Theory / Representation Theory)**

3. **Prof. Gerd Rudolph**
   Universität Leipzig, Institute for Theoretical Physics
   *Expertise:* Gauge field theory, group-theoretic structures in physics, differential geometry of field theories
   Contact: rudolph@itp.uni-leipzig.de

**Cosmology (FLRW / CMB)**

4. **Dr. Licia Verde**
   ICC, Universitat de Barcelona / ICREA
   *Expertise:* CMB power spectrum analysis, Hubble tension, Bayesian parameter estimation in ΛCDM
   Contact: liciaverde@icc.ub.edu

**Quantum Mechanics / Atomic Physics (BEC / Interferometry)**

5. **Prof. Markus Oberthaler**
   Universität Heidelberg, Kirchhoff-Institut für Physik
   *Expertise:* BEC physics, matter-wave interferometry, precision measurements with ultracold ⁸⁷Rb atoms
   Contact: markus.oberthaler@kip.uni-heidelberg.de

---

## 7. Excluded Reviewers

No reviewers are formally excluded. The submitted work does not involve any personal, commercial, or intellectual conflict that would warrant exclusion.

---

## 8. Author Information

**Dominic-René Schu**
Independent Researcher
Email: dominic.rene.schu@gmail.com
ORCID: 0009-0004-9769-9061
GitHub: https://github.com/DominicReneSchu/RFT

**Co-authors:** None. This is a single-author submission.

**Conflicts of interest:** None.

**Funding:** No external funding was received for this work.

**Data availability:** All code, data, and simulation scripts are publicly available at https://github.com/DominicReneSchu/RFT under RFT-License 1.4.

---

I confirm that this manuscript is original, has not been published elsewhere, and is not currently under consideration at any other journal.

Yours sincerely,

Dominic-René Schu
August 2026
