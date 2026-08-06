# Response-to-Reviewers Template

**Manuscript:** "Resonance Field Theory: Axiomatics, Fundamental Formula, and Empirical Validation"
**Author:** Dominic-René Schu (ORCID: 0009-0004-9769-9061)
**Journal:** Journal of Physics Communications, IOP Publishing
**Version:** RT-39, August 2026

---

*This document is an anticipatory template for the most likely standard reviewer objections. Each response is derived from the actual manuscript content and RT-series results. Responses are complete and require only minor adaptation to the specific reviewer wording received.*

---

## General Response Preamble

We thank the reviewers for their time and careful reading of the manuscript. We address each raised point in detail below. All changes to the manuscript are indicated with section references. The revised manuscript has the same structure as the original; changes are summarized at the start of each response.

---

## Critique 1 — "The factor π in A4 is arbitrary"

**Anticipated reviewer formulation:**
> *"The factor π in Eq. (3) appears to be an arbitrary normalization choice. Why not 2π or any other constant?"*

**Response:**

We appreciate this question, as it targets the most critical claim of the manuscript. The factor π is not a normalization choice. We address this at three levels.

**Level 1 — The action-integral derivation (RT-01, §3.2).**
The derivation proceeds as follows. The action functional for a single resonance half-cycle is defined as S[φ] = ∫₀^π ε(φ) dφ, where φ ∈ [0, π] parametrizes the phase range of one half-oscillation. Applying the stationary-phase approximation to this integral yields a saddle-point contribution at φ = π/2, which evaluates to exactly π · ε(π/2). No free parameter is introduced at any step. The choice of the integration domain [0, π] — a half-period — is not arbitrary: it is the minimal complete resonance cycle (the interval over which the coupling efficiency completes exactly one full excursion from ε = 1 to ε = 0). The full derivation is given in §3.2 of the manuscript.

**Level 2 — Numerical confirmation (RT-01b, §3.2).**
The derivation generates residual coefficients c₃ and c₄ for higher-order saddle-point corrections. Numerical evaluation yields |c₃ + c₄| ≈ 5.5 × 10⁻¹¹. This confirms that the saddle-point is the dominant contribution and that no other constant (2π, π/2, etc.) would satisfy the stationarity condition to this precision. A factor of 2π would require |c₃ + c₄| to equal a value of order 1, which contradicts the numerical result.

**Level 3 — The decimal-artifact argument (RT-01a).**
π is the natural unit of cyclic completeness in phase space — the measure of one half-oscillation. In a number system with π as base, π = 10 (rational and finite). The irrationality of 3.14159... is not a property of the circle but of the base-10 representation. This is structurally analogous to Planck units (c = ℏ = 1): setting π = 1 would absorb the geometric factor but would not eliminate it from the physics. The explicit appearance of π in E = π · ε · ℏ · f makes the geometric origin transparent.

**Falsification condition (§6):** If a future precision measurement of the phase-integrated coupling energy in a BEC (Experiment II) finds a systematic deviation from π · ε · ℏ · f that cannot be explained by higher-order saddle-point corrections, the derivation in §3.2 would be falsified.

**Manuscript change:** None required for this point; the derivation is fully present in §3.2. If the reviewer requests additional detail, we can expand the saddle-point calculation in an appendix.

---

## Critique 2 — "ε = cos²(Δφ/2) is a phenomenological choice"

**Anticipated reviewer formulation:**
> *"The choice of ε(Δφ) = cos²(Δφ/2) seems phenomenological. Many other functions satisfy the boundary conditions."*

**Response:**

This objection would be correct if ε were chosen by boundary conditions alone. It is not. The selection is representation-theoretically constrained, and the proof is given in §3.3 of the manuscript. We summarize it here.

**The uniqueness theorem (RT-02, §3.3).**
The symmetry group of RFT is G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ). The coupling efficiency ε must transform as a scalar under G_sync and must be expressible in terms of the U(1) component alone (since it depends only on the relative phase Δφ). The irreducible representations of U(1) are labeled by k ∈ ℤ, with basis functions e^{ikΔφ}. The k=1 representation provides the unique real-valued, non-negative, normalized function on [0, 2π] that satisfies:
1. ε(0) = 1 (perfect coupling at zero phase difference),
2. ε(π) = 0 (no coupling at maximum phase difference),
3. Parity: ε(Δφ) = ε(−Δφ),
4. No mixing of higher representations (k ≥ 2).

The function satisfying all four conditions simultaneously is ½(1 + cos Δφ) = cos²(Δφ/2). Any other smooth function satisfying conditions 1–3 — such as cos⁴(Δφ/2), (1 − |Δφ|/π)², or a Gaussian — violates condition 4 because it requires a Fourier expansion with k ≥ 2 components.

**Cross-domain confirmation.**
The function ε(Δφ) = cos²(Δφ/2) is not merely theoretically derived but independently confirmed in three physical domains at unrelated energy scales: (a) the FLRW cosmological simulation (1,530 runs) shows η(Δφ) = cos²(Δφ/2) as an emergent property of the coupled scalar field dynamics (§4.2); (b) the Schrödinger simulation (§4.4) confirms fidelity = 1.0 for all four Δφ scenarios; (c) the double pendulum simulation (§4.3) yields ε(θ₂ − θ₁) = cos²(Δθ/2) in classical mechanics. The same function appearing in domains separated by 19 orders of magnitude in energy is not consistent with a phenomenological choice.

**Manuscript change:** None required; the uniqueness proof is in §3.3. On reviewer request, we can add a brief enumeration of disqualified alternatives (e.g., cos⁴, Gaussian, polynomial) in a supplementary note.

---

## Critique 3 — "Domain transfer to financial markets is not physical"

**Anticipated reviewer formulation:**
> *"Applying a physical theory to financial markets seems like an overreach. What justifies this domain transfer?"*

**Response:**

We appreciate this concern. The manuscript explicitly addresses it in two places, and we confirm the status here.

**The A7 domain transfer is declared as a motivated postulate — not a formal derivation.**
Axiom A7 (invariance under G_sync) establishes the symmetry structure for physical resonance fields. The application of this axiom to financial price dynamics (ResoTrade) is presented as an analogical transfer — a testable hypothesis that the same resonance conditions that hold in physical systems also appear in competitive market dynamics. This is explicitly stated in §4.5: "ResoTrade is classified as an application concept demonstrating the scope of RFT axioms in a non-physical domain; it is not presented as a derivation of market dynamics from first principles."

**ResoTrade is not a primary validation domain.**
The abstract states this explicitly: "primary axiom evidence comes from RFT-internal simulations." The four primary validation domains are particle physics, cosmology, nuclear physics, and quantum mechanics — none of which involve financial data. ResoTrade appears as a fifth, exploratory section precisely because its domain transfer has a different epistemic status.

**The backtest result is falsifiable and limited.**
The walk-forward backtest (RT-10) uses synthetic price data (Binance Public API with seed=42) and yields 3/5 folds positive against the falsification criterion (vs_hodl > 0). This is a weak positive result, not a proof. The manuscript does not claim financial market validation as evidence for the physical axioms.

**Manuscript change:** If the reviewer judges the ResoTrade section as distracting from the physical content, we are prepared to move it to supplementary material without loss of the primary argument.

---

## Critique 4 — "The FLRW simulation is not a genuine cosmological test"

**Anticipated reviewer formulation:**
> *"The FLRW simulation uses a toy model ΛCDM and κ = 1, not the physical value 8πG/c⁴. This makes the comparison with Planck data questionable."*

**Response:**

This is a well-founded concern. We address it on three points.

**κ_RFT = 1 is explicitly declared as a normalization convention (RT-11, §3.4).**
The manuscript states in §3.4: "The coupling constant κ_RFT = 1 is adopted as a normalization convention; its relationship to the Einstein gravitational coupling 8πG/c⁴ is not derived within the current framework." This is not an oversight but a deliberate, documented simplification. The physical implication is that the FLRW model represents a dimensionless resonance analogue of the Friedmann equations, not a full GR simulation.

**Δχ² = +16 is a relative improvement, not an absolute calibration.**
The improvement Δχ² = +16 compared to the uncoupled Planck-2018 CMB template (83 data points) measures the improvement attributable to the η-correction term in the coupled FLRW simulation relative to the same parametric model without the correction. It is not a comparison with the full CAMB/CLASS numerical pipeline. This limitation is explicitly stated in the manuscript: "The parametric ΛCDM model does not reach the level of CAMB/CLASS."

**Falsifiable prediction remains valid.**
The sensitivity scaling d(d_η)/d(H₀) = (0.00113 ± 0.00017) (km/s/Mpc)⁻¹ and the 6σ separation of the η-correction signal from the null hypothesis are derived quantities that do not depend on the absolute calibration of κ. They test whether the resonance coupling term improves the fit to the CMB angular power spectrum relative to a common baseline — a question that is answerable even with a simplified parametric model.

**RT-05 pathway for full CAMB comparison.**
The manuscript acknowledges that a full CAMB/CLASS comparison (RT-05) has been identified as future work. This would allow an absolute χ² comparison with the Planck pipeline. The current result is a proof-of-concept with a properly disclosed limitation.

**Manuscript change:** None required; the κ limitation is in §3.4 and the FLRW limitation is at the end of §4.2. We can add a one-sentence cross-reference if the reviewer requests it.

---

## Critique 5 — "All validation is based on simulations; no experimental confirmation"

**Anticipated reviewer formulation:**
> *"All validation is based on simulations. Without experimental confirmation, the theory cannot be considered validated."*

**Response:**

We accept the premise that experimental confirmation would strengthen the claims. We note, however, three points:

**The CMS data analysis is a statistical analysis of real experimental measurements.**
The Monte Carlo component of §4.1 uses 1,500,000 simulated RFT resonance curves, but the data against which they are tested — the CMS Open Data dielectron dataset (CMS-2021) — are real experimental measurements from the LHC. The result (empirical p = 0, stable across 3 KDE bandwidths and 10 seeds) demonstrates that the RFT resonance predictions are consistent with real particle physics data at a significance level that has no simulation analogue. This is not a pure simulation result.

**Two concrete, independently reproducible experimental proposals are provided in §6.**
Experiment I (Am-241 at ELI-NP, §6.1): Phase-dependent nuclear photo-excitation at the γ-ray beam facility ELI-NP (Măgurele, Romania). The prediction is SNR ≥ 3σ at 100 h beam time (realistic scenario: SNR_median ≈ 10σ). The experiment requires 0 free parameters on the prediction side. This is a direct test of ε(Δφ) in nuclear physics.

Experiment II (⁸⁷Rb BEC, §6.2): Center-of-mass shift |Δ⟨x⟩| ≈ 2.0·λ μm in a ⁸⁷Rb Bose-Einstein condensate in a harmonic trap at Δφ = π. The experiment uses existing BEC apparatus (T < 200 nK, ω = 2π × 100 Hz). One free parameter (λ, the perturbation strength) is measured from the BEC and then the shift is predicted. This is a direct test of ε(Δφ) in quantum mechanics.

**The RT-38 double pendulum protocol enables immediate experimental testing.**
The publicly available RT-38 protocol (https://github.com/DominicReneSchu/RFT) provides a complete tabletop falsification test with a budget of approximately 200 EUR and a smartphone camera. The prediction is explicit: the coupling efficiency ε(θ₂ − θ₁) = cos²(Δθ/2) should be recoverable from tracking the phase difference of a double pendulum. Any group can perform this experiment and report results via the labeled GitHub issue tracker.

**Manuscript change:** We propose adding one sentence to §6 referencing the RT-38 protocol URL for the double pendulum experiment, as this strengthens the claim of experimental accessibility.

---

## Critique 6 — "RFT reformulates well-known oscillator physics"

**Anticipated reviewer formulation:**
> *"The framework appears to reformulate well-known oscillator physics. What is the novel theoretical contribution beyond unifying notation?"*

**Response:**

This is an important question that goes to the core of the manuscript's contribution. We identify three specific results that are not present in prior oscillator frameworks and that carry concrete, falsifiable consequences.

**Contribution 1: π as a derived geometric constant, not a numerical postulate.**
Standard quantum mechanics writes E = ℏω = 2πℏf. The factor 2π is absorbed into ω by definition. In RFT, the factor π appears explicitly as the result of a phase-space integration (§3.2). The consequence is a prediction that the coupling energy integrated over a half-cycle is exactly π · ε · ℏ · f, not 2π · ε · ℏ · f / 2 or any rescaled equivalent. This is a dimensionless prediction about the geometry of phase space that can be tested directly in Experiment II.

**Contribution 2: ε = cos²(Δφ/2) is the unique representation-theoretically forced coupling function.**
No prior oscillator theory (Kuramoto model, coupled harmonic oscillators, QFT resonance formulas) derives the specific functional form of the coupling efficiency from group-theoretic uniqueness. The Kuramoto model uses sin(θⱼ − θᵢ) by construction; coupled harmonic oscillator theory uses arbitrary coupling constants; QFT uses Breit-Wigner resonance profiles that are fitted to data. RFT uniquely derives cos²(Δφ/2) from the representation theory of G_sync without fitting any parameter to the data being described (§3.3).

**Contribution 3: A3 as a corollary reduces the axiom count.**
Prior oscillator frameworks — including the RFT formulation in early repository versions — treated the resonance condition |f₁/f₂ − m/n| < δ as an independent postulate. RT-02 and RT-35 show it is derivable from Axiom A7 (invariance under G_sync). This is a genuine structural result: the framework now has one fewer independent postulate than its precedents.

**The experimentally distinguishing prediction.**
The ⁸⁷Rb center-of-mass shift |Δ⟨x⟩| ≈ 2.0·λ μm as a function of Δφ is a quantitative prediction that follows directly from the RFT coupling function but not from standard BEC theory. A measurement confirming or refuting this scaling would directly test whether RFT's derivation of ε(Δφ) provides additional predictive content beyond existing frameworks.

**Manuscript change:** None required; these three contributions are detailed in §3 and §5. We can add a concise comparison table in §5 if the reviewer requests explicit side-by-side notation.

---

## Critique 7 — "A5 (vectoriality of energy) contradicts established physics"

**Anticipated reviewer formulation:**
> *"Axiom A5 claims that energy is vectorial. This directly contradicts standard physics where energy is a Lorentz scalar."*

**Response:**

We appreciate the precision of this concern. The manuscript addresses it in §2.5, but we provide a complete clarification here.

**A5 is explicitly declared as an irreducible postulate (RT-36, §2.5).**
RT-36 investigated whether A5 could be derived from G_sync or from any other axiom in the RFT system. The conclusion is negative: A5 is not derivable from the other axioms. It is correctly classified as an independent postulate, and the manuscript states this explicitly: "A5 is an irreducible postulate; its derivability from G_sync has been systematically excluded (RT-36)."

**A5 does not replace the Lorentz scalar — it extends the energy concept in a specific context.**
The Lorentz scalar E is the timelike component of the 4-momentum pᵘ = (E/c, p⃗) and is invariant under Lorentz transformations. RFT does not dispute this. A5 defines an energy direction in the resonance field — the vector E⃗ = E · ê(Δφ, ∇Φ) — where ê is a unit vector in the phase gradient of the field configuration. This direction is defined in a non-inertial, field-internal context; it is not a claim that the Lorentz-covariant energy changes its transformation properties.

**The motivation for A5 is structural, not empirical (§2.5).**
The formal motivation cited in the manuscript is the observation that several energy-related quantities in standard physics have directional properties: torque M⃗ = r⃗ × F⃗ (unit: J), spin (SU(2) algebra, Zeeman splitting), and the Lorentz 4-vector (E/c, p⃗) itself. This is not a proof of A5 but a consistency argument: if energy-like quantities exhibit directional structure in multiple established contexts, defining energy direction explicitly in RFT is a well-motivated extension rather than a contradiction.

**The warp drive simulation (§4.6) provides a domain where A5 has observable consequences.**
In the warp drive simulation, A5 enables the sign change of the effective equation-of-state parameter w via phase control ε(Δφ). The prediction ρ ∝ cos⁴(Δφ/2) with E⁻ = 0 (no exotic energy) is a direct consequence of A5 combined with A4. This constitutes a falsifiable domain of application for A5 that is not accessible to standard scalar-energy frameworks.

**Manuscript change:** We propose adding a one-sentence clarification to §2.5: "A5 introduces energy direction within the resonance field geometry and does not affect the Lorentz-covariant transformation properties of the 4-momentum in special relativity."

---

*Template version: RT-39, August 2026 — Dominic-René Schu*
