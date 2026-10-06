# RT-40 AP6 — Falsifiability and Distinction from SRT

*Dominic René Schu, September 2026*
*Status: Completed (Sep 2026) — Success criterion fulfilled (measurable deviation identified; equivalence structure complete)*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Starting Point: Results from AP1–AP5](#2-starting-point-results-from-ap1ap5)
3. [Free Parameters of the RFT: Inventory and Measurability](#3-free-parameters-of-the-rft-inventory-and-measurability)
4. [Equivalence Structure: Kinematics RFT ≡ SRT](#4-equivalence-structure-kinematics-rft--srt)
5. [Excess Predictions of the RFT](#5-excess-predictions-of-the-rft)
6. [Concrete Falsification Experiments](#6-concrete-falsification-experiments)
7. [Falsification Criterion: What Would Refute the RFT?](#7-falsification-criterion-what-would-refute-the-rft)
8. [Success Criterion and Assessment](#8-success-criterion-and-assessment)
9. [Results and Outlook on AP7](#9-results-and-outlook-on-ap7)

---

## 1. Objective and Success Criterion

**Task (RT-40 AP6):** Systematically identify empirically distinguishable predictions of the
RFT relative to the SRT and formulate concrete experiments.

**Key questions:**
1. Which free parameters of the RFT (λ, G(fᵢ/fⱼ), κ, …) are accessible to measurement?
2. In which domain are RFT and SRT mathematically equivalent — and where do they deviate?
3. Which concrete experiments (GSI/FAIR phase noise, muon g-2, gravitational wave dispersion,
   coherence length) can distinguish between RFT and SRT?
4. What measurement result would falsify the RFT?

**Success criterion:** At least one measurable deviation of the RFT from the SRT identified —
**or** complete equivalence demonstrated and the RFT thereby classified as a reformulation
of the SRT (then: value through coupling structure, not through new predictions).

**Summary of result:**
- **Kinematics:** The RFT is exactly equivalent to SRT kinematics — time dilation,
  length contraction, and the Lorentz transformation follow identically (AP1–AP5).
- **Coupling dynamics:** The RFT makes four additional, empirically distinguishable predictions:
  1. Coherence length l_c(v) = λ₀/(2γ²) — scales with γ² instead of γ (AP5).
  2. Phase noise of moving resonators: S_φ(ω,v) ∝ ε(Δφ)·S_φ(ω,0) = S_φ(ω,0)/γ².
  3. Internal coupling frequency f_int(v) = γ³·f₀ (AP2) — measurable via quantum
     interference on relativistic atoms.
  4. Frequency-dependent group velocity near ε → 0: v_g(f) < c for f < f₀.
- **Falsification criterion:** A coherence-length experiment yielding l_c ∝ γ⁻¹ (SRT
  scaling) instead of γ⁻² would refute the RFT prediction from AP5.

---

## 2. Starting Point: Results from AP1–AP5

### 2.1 Key Results AP1 (Phase ↔ Rapidity)

- Bijective map: φ = artanh(sin(Δφ/2)), v/c = β = sin(Δφ/2).
- Lorentz factor: γ = 1/cos(Δφ/2).
- Phase composition ⊕ structurally identical to relativistic velocity addition.

### 2.2 Key Results AP2 (Coupling Efficiency ↔ Lorentz Factor)

- Coupling energy: E_c = mc²·ε(Δφ) = mc²/γ².
- Internal consistency frequency: f_int(v) = γ³·f₀ (measurable prediction).
- Zitterbewegung frequency: f_zbw = mc²/(πℏ).

### 2.3 Key Results AP3 (Lorentz Transformation)

- Lorentz equations derived exactly under bridge assumption B₁.
- Coupling invariant: I_RFT ≅ s²_Minkowski.
- Open gap B₁: full derivation of the Minkowski metric from RFT axioms still outstanding.

### 2.4 Key Results AP4 (c as Structural Limit)

- c_struct = lim_{ε→0} v(ε) = c_phys — speed limit as structural property of ε(Δφ),
  not an independent postulate.
- Massive resonators (ε > 0) cannot reach c.

### 2.5 Key Results AP5 (Time Dilation, Length Contraction, New Prediction)

- Time dilation: Δt = γ·Δt₀ — exact (hyperbolic phase-projection geometry).
- Length contraction: L' = L₀/γ — exact (effective wave number k_eff = γk₀).
- **New prediction:** Coherence length l_c(v) = λ₀/(2γ²) — γ²-scaling instead of γ.
- ε = 1/γ² algebraically closed.

---

## 3. Free Parameters of the RFT: Inventory and Measurability

### 3.1 Complete Parameter List

| Parameter | Physical meaning | Status in axioms | Measurability |
|-----------|-----------------|------------------|---------------|
| λ | Spatial coupling scale; ∣Δ⟨x⟩∣ = 4.9·λ·ℓ | Free parameter (RT-03) | Medium — ⁸⁷Rb interferometry (RT-12) |
| κ | Geometric prefactor in A4 | Convention (RT-11) | Not measurable in isolation |
| G(fᵢ/fⱼ) | Coupling function between frequencies | Shape not axiomatically fixed | Indirect — spectral form of phase noise |
| ε₀ | Rest coupling (= 1 by A3) | Fixed by A3 | No freedom |
| f₀ | Resonator eigenfrequency | Physically measurable | Direct (spectroscopy) |
| c | Speed limit | Structural property of ε (AP4) | Measured, not a free parameter |

### 3.2 Relevance for Falsifiability

The essential freedom of the RFT lies in the **form of the coupling function G(fᵢ/fⱼ)**:
the axioms fix ε = cos²(Δφ/2) as a function of phase, but do not a priori determine how
different frequency components couple. This freedom generates the predictions in §5 — and
thereby the falsification criteria in §7.

---

## 4. Equivalence Structure: Kinematics RFT ≡ SRT

### 4.1 Comparison Table

| SRT quantity | SRT expression | RFT derivation | Equivalence |
|-------------|---------------|----------------|-------------|
| Lorentz factor γ | γ = 1/√(1 − β²) | γ = 1/cos(Δφ/2) with β = sin(Δφ/2) | Exact |
| Time dilation | Δt' = γΔt | Hyperbolic phase-projection geometry (AP5 §3) | Exact |
| Length contraction | L' = L/γ | k_eff = γk₀ (AP3 + AP5 §4) | Exact |
| Velocity addition | β₁₂ = (β₁+β₂)/(1+β₁β₂) | Phase composition ⊕ (AP1) | Exact |
| Invariant interval | s² = c²Δt² − Δx² | I_RFT ≅ s²_Minkowski (AP3) | Exact (under B₁) |
| c as speed limit | Postulate | ε(Δφ→π) → 0 (AP4) | Structurally derived |

**Conclusion:** SRT kinematics is completely a limiting case of the RFT coupling dynamics.
There is no kinematic observable in which RFT and SRT deviate.

### 4.2 Where the Equivalence Ends

The equivalence is **kinematically complete** but **dynamically incomplete**:
- The SRT describes spacetime geometry (Lorentz invariance as a postulate).
- The RFT derives this geometry from coupling physics and additionally contains an internal
  frequency structure (f_int = γ³f₀, AP2) and a coherence length (l_c = λ₀/(2γ²), AP5)
  that have no counterpart in the SRT.

---

## 5. Excess Predictions of the RFT

The following predictions go beyond the SRT and are in principle falsifiable:

### 5.1 Coherence Length l_c(v) = λ₀/(2γ²)

**Origin:** AP5 §6. The coherence length of a moving resonator scales with γ²:
```
    l_c(v) = λ₀ · ε(Δφ) / 2 = λ₀ / (2γ²)
```

**SRT counterpart:** The SRT contains no distinguished coherence length — any length
contracts simply with γ⁻¹.

**Physical meaning:** The RFT predicts that the internal coherence of a resonator
(wavepacket coherence) is reduced more strongly than its spatial extent. The ratio
l_c / L' = (λ₀/2γ²) / (L₀/γ) = λ₀/(2γL₀) → 0 for γ → ∞ means: ultrarelativistic
resonators lose coherence faster than they spatially contract — a purely RFT effect.

**Order of magnitude:** For an optical cavity with λ₀ = 1 µm at γ = 10 (v ≈ 0.995c):
```
    l_c = 1 µm / (2 · 100) = 5 nm
    L'  = L₀ / 10           (classical SRT contraction)
```
The difference is a factor of 2γ = 20 — metrologically relevant.

### 5.2 Phase Noise of Moving Resonators S_φ(ω, v)

**Origin:** From the coupling function G(fᵢ/fⱼ) and ε(Δφ).

For a resonator at rest, the phase-noise power spectral density is S_φ(ω, 0). The
RFT coupling structure predicts that for a resonator moving at v:
```
    S_φ(ω, v) = ε(Δφ) · S_φ(ω, 0) = S_φ(ω, 0) / γ²
```

**SRT counterpart:** The SRT makes no specific prediction about the velocity dependence
of phase noise — phase noise is not an SRT concept.

**Experimental access:** Relativistic heavy ions at GSI/FAIR (γ ≈ 2–10). The coherent
synchrotron radiation of ion bunches has a phase-noise spectrum that fundamentally depends
on γ. The RFT prediction l_c ∝ γ⁻² means that the phase-coherent emission window of
the ions shrinks faster than SRT length contraction alone would describe.

**Estimate of the effect:**
```
    Δ(S_φ)_RFT/SRT ∝ γ⁻² / γ⁻¹ = γ⁻¹
```
At γ = 5: RFT predicts 5× more phase-noise suppression than a simple
Doppler/time-dilation correction. Measurable with beam-position-monitor phase detectors.

### 5.3 Internal Consistency Frequency f_int(v) = γ³ · f₀

**Origin:** AP2, self-consistency condition.

The internal coupling frequency of a moving resonator is:
```
    f_int(v) = γ³ · f₀
```
The **observed** frequency (Doppler + time dilation) is f_obs = f₀/γ (correct SRT
prediction, confirmed by AP5). The internal frequency f_int is the resonator frequency
within its own coupling structure — not directly measurable as emission, but accessible
as a quantum-state frequency.

**Experimental access:** Ramsey spectroscopy on relativistic atoms (muons, antiprotons
at CERN/AD). If the atom oscillates internally at f_int = γ³f₀ during flight, the
interference phase after distance L is:
```
    φ_int = 2π · f_int · t_proper = 2π · γ³f₀ · (L/(γc)) = 2πγ²f₀L/c
```
The SRT calculation gives:
```
    φ_SRT = 2π · f₀ · t_proper = 2πf₀L/(γc)
```
The ratio φ_int/φ_SRT = γ³ is in principle measurable.

**Caveat:** f_int is conceptually defined as the internal coupling frequency. Whether it
directly translates to the quantum phase of an external measurement requires a complete
quantisation of the RFT coupling structure (open problem).

### 5.4 Frequency-Dependent Group Velocity near ε → 0

**Origin:** For resonators with very small eigenfrequency f₀ ≪ f_zbw = mc²/(πℏ) the
RFT predicts an anomalous group velocity.

In the limit ε → 0 (v → c):
```
    v_g(f) = c · √(1 − (f₀_eff/f)²)
```
where f₀_eff = f₀/ε^(1/2) is an effective cut-off frequency. This dispersion relation
has the form of a massive field theory (as for photons in a plasma).

**SRT counterpart:** Massless propagating fields (photons, gravitons) have v_g = c
exactly for all frequencies in the SRT.

**Experimental access:** Gravitational wave dispersion with LIGO/LISA. If gravitons
possess an RFT coupling structure, their group velocity would be frequency-dependent.
LIGO observations already set tight limits: v_g/c − 1 < 10⁻¹⁵ for f ~ 10–1000 Hz.
This constrains f₀_eff ≪ 10 Hz for the graviton coupling structure (see §6.4).

---

## 6. Concrete Falsification Experiments

### 6.1 Experiment E1: Coherence-Length Scaling with γ

**Goal:** l_c ∝ γ⁻² (RFT) vs. l_c ∝ γ⁻¹ (SRT expectation from length contraction).

**Method:**
1. Precision interferometry with relativistic atoms or ions at variable γ.
2. Measure the coherence length l_c from the visibility decay of interference as a
   function of path difference.
3. Compare the γ-dependence with the predictions:
   ```
       l_c^RFT(v) = λ₀ / (2γ²)      (RFT)
       l_c^SRT(v) = λ₀ / γ           (simple length contraction)
   ```

**Expected signal at γ = 10:**
```
    l_c^RFT = λ₀ / 200
    l_c^SRT = λ₀ / 10
```
Factor 20 difference — well above the precision of modern interferometry.

**Feasibility:** Atom interferometry with ultracold Rb atoms or muon interferometry
(PSI, J-PARC). Difficulty: γ > 5 for classical atoms requires a storage ring.

**Falsification result:** Measuring l_c ∝ γ⁻¹ refutes the AP5 prediction.
Measuring l_c ∝ γ⁻² violates the SRT expectation and favours the RFT.

---

### 6.2 Experiment E2: Phase Noise of Relativistic Ions (GSI/FAIR)

**Goal:** S_φ(ω,v) ∝ γ⁻² (RFT) vs. no γ²-dependence (SRT).

**Method:**
1. Relativistic heavy ions (e.g. ²³⁸U, γ ≈ 2–10) in the heavy-ion storage ring SIS18/
   SIS100 (GSI/FAIR, Darmstadt).
2. Measurement of the phase-noise spectrum of coherent synchrotron radiation with
   beam-position monitors and phase detection.
3. Comparison of the measured phase-noise amplitude as a function of γ.

**RFT prediction:** Phase noise S_φ ∝ γ⁻² — stronger suppression than pure time
dilation (γ⁻¹) over the same path length.

**Limitation:** The observed phase noise contains many contributions (wakefields, space
charge, vacuum fluctuations). Clean extraction of the ε-contribution requires a differential
measurement over γ. A feasibility study with GSI/FAIR collaboration is needed.

---

### 6.3 Experiment E3: Muon Anomaly (g-2) and RFT Coupling

**Goal:** Check whether the RFT coupling structure provides an additional contribution to
the anomalous magnetic moment deviation a_µ = (g-2)/2.

**Background:** The muon g-2 experiment (Fermilab) measures a_µ with ~0.2 ppm precision.
The current discrepancy between SM prediction and measurement:
```
    Δa_µ = a_µ^exp − a_µ^SM ≈ (2.51 ± 0.59) × 10⁻⁹
```

**RFT approach:** A muon is a resonator with eigenfrequency f₀_µ = m_µc²/(πℏ) and
coupling efficiency ε in external fields. The RFT energy structure E_c = mc²/γ²
modifies the effective muon mass in a strong magnetic field (γ_eff ≠ 1 through field
coupling):
```
    δa_µ^RFT ~ ε · (α_em / π) · (m_µ / m_ref)²
```
where m_ref is a reference scale of the RFT coupling structure.

**Limitation:** The exact value of δa_µ^RFT depends on the form G(fᵢ/fⱼ) (free RFT
parameter, §3). Without a complete quantisation of the RFT, only an order-of-magnitude
estimate is possible. The prediction is therefore:
- If the RFT coupling is relevant in the electromagnetic sector:
  δa_µ^RFT ≈ α_em/(2π) · (m_µ/m_W)² ~ 10⁻⁹ — **within the observed discrepancy**.
- If the RFT coupling acts only gravitationally/weakly:
  δa_µ^RFT ≪ 10⁻¹⁰ — not measurable.

**Falsification result:** Only relevant once G(fᵢ/fⱼ) is determined — therefore
qualitative, not usable as a hard falsification test.

---

### 6.4 Experiment E4: Gravitational Wave Dispersion (LIGO/LISA)

**Goal:** v_g(f) = c for all frequencies (SRT/GR) vs. v_g(f) < c for f < f₀_eff (RFT).

**Method:** Compare arrival times of GW signal frequency components. For GW150914:
frequency range 35–250 Hz, distance ~ 410 Mpc.

**LIGO bound from observation:**
```
    |v_g − c| / c < 10⁻¹⁵    (95% CL, for m_graviton < 1.2 × 10⁻²² eV/c²)
```

**RFT prediction:** If gravitons possess an RFT coupling structure:
```
    v_g(f) ≈ c · (1 − f₀_eff² / (2f²))
```
The LIGO bound sets:
```
    f₀_eff < c · √(2 · 10⁻¹⁵ · f²) ≈ 3 × 10⁻⁷ f
```
For f ~ 100 Hz: f₀_eff < 30 µHz. This means: if gravitons have an RFT coupling, their
eigenfrequency must be f₀_grav < 30 µHz — an extremely small value, essentially
consistent with massless gravitons.

**Conclusion:** LIGO data rules out significant RFT dispersion for gravitons. The RFT
is consistent with GW data but provides no new prediction for gravitational waves, as
long as f₀_grav ≫ 30 µHz remains excluded.

---

## 7. Falsification Criterion: What Would Refute the RFT?

### 7.1 Strict Falsification Criteria (direct refutation)

| Measurement | RFT prediction | Falsifying result |
|-------------|----------------|-------------------|
| Coherence length l_c(v) | l_c ∝ γ⁻² | Measurement l_c ∝ γ⁻¹ (SRT scaling) |
| Phase noise S_φ(ω,v) | S_φ ∝ γ⁻² | Measurement S_φ ∝ γ⁻¹ or γ-independent |
| Internal frequency (quantum interferometry) | φ_int ∝ γ²L | No γ² term in interference phase |
| GW dispersion | consistent with v_g = c | No falsification potential (§6.4) |

### 7.2 Structural Falsification Criteria (internal inconsistency)

The RFT would be internally refuted if:

1. **ε(Δφ) = cos²(Δφ/2) and γ = 1/cos(Δφ/2) gave ε ≠ 1/γ²** — but this is an
   algebraic identity (AP5 §7), hence excluded.

2. **The phase composition ⊕ is not associative** — this would contradict A7 (group
   structure of G_sync). A counterexample would falsify A7.

3. **c is not a structural limit** — i.e. there exists a resonator with ε > 0 reaching
   v > c. This would directly contradict the limit in AP4.

4. **Time dilation does not follow Δt = γΔt₀** — contradicting AP5 §3 and the entire
   AP1–AP5 framework. This would simultaneously refute the SRT.

### 7.3 Classification: Reformulation or New Theory?

If coherence-length experiment E1 finds no γ⁻² signal:

- **Scenario A (l_c ∝ γ⁻¹ measured):** AP5 prediction refuted. The RFT is incorrect
  or the coherence-length derivation contains an error. To investigate: whether the
  derivation l_c = λ₀ε/2 actually follows from A4 or is only an analogy claim.

- **Scenario B (no γ-dependent signal measurable):** Complete equivalence.
  The RFT is then a **reformulation** of the SRT (with richer structure), not a
  standalone theory with new predictions. This is a valid and important result:
  Lorentz invariance follows from coupling dynamics — the SRT is axiomatically derivable.

- **Scenario C (l_c ∝ γ⁻² measured):** RFT prediction confirmed. The coherence length
  is a genuinely new observable indicating an extension of the SRT.

---

## 8. Success Criterion and Assessment

**Success criterion (recap):** At least one measurable deviation identified — or complete
equivalence demonstrated.

### 8.1 Assessment: Measurable Deviation

The success criterion is fulfilled by:

**Prediction 1 (strong):** Coherence length l_c(v) = λ₀/(2γ²) — γ²-scaling,
experimentally distinguishable from γ⁻¹ (factor 2γ at γ ≫ 1). This is a concrete,
derivable consequence of the RFT coupling structure from AP5.

**Prediction 2 (medium):** Phase noise S_φ(ω,v) ∝ γ⁻² at GSI/FAIR — in principle
measurable, but extraction from background requires a feasibility study.

**Prediction 3 (weak/conditional):** Muon g-2 contribution δa_µ^RFT — only quantifiable
after complete quantisation of the RFT coupling structure (open task).

**Prediction 4 (consistent, no signal):** GW dispersion — LIGO bounds exclude significant
RFT effects for gravitons; no falsification, but no new signal either.

### 8.2 Overall Assessment

The RFT is:
- **Kinematically:** Exactly equivalent to the SRT — no deviation in time dilation,
  length contraction, Lorentz transformation, or speed limit.
- **Dynamically:** Provides an empirically distinguishable prediction (l_c ∝ γ⁻²) from
  the internal coupling structure.
- **Structurally:** Derivation of SRT axioms from A1–A7 complete (kinematically); bridge
  B₁ (Lorentz boosts ↔ phase composition) not yet fully proved (AP3).

The success criterion is fulfilled: at least one measurable deviation (l_c-scaling) has
been identified, and a concrete falsification protocol (E1) formulated.

---

## 9. Results and Outlook on AP7

### 9.1 Summary of AP6 Results

| Question (AP6) | Result |
|----------------|--------|
| Free parameters accessible? | λ (RT-12), G(fᵢ/fⱼ) (phase noise) — partially measurable |
| Kinematic equivalence with SRT? | Complete — no kinematic deviation |
| Measurable dynamic deviation? | Yes: l_c(v) = λ₀/(2γ²) — γ²-scaling (AP5) |
| Concrete experiment? | E1: coherence-length interferometry (Rb/muons) |
| Falsification criterion? | l_c ∝ γ⁻¹ measured → AP5 prediction refuted |
| GW dispersion? | Consistent, no new signal at LIGO precision |
| Muon g-2? | Qualitatively plausible, not quantifiable without quantisation |

### 9.2 What AP6 Achieves

- Complete equivalence analysis: RFT kinematics ≡ SRT (no kinematic difference).
- Identification of four excess predictions of the RFT.
- Concrete falsification protocol (E1: coherence-length test).
- Classification of scenarios: reformulation or extension of the SRT.
- Assessment of LIGO/g-2: consistent, no new effect without quantisation.

### 9.3 What AP6 Does Not Achieve (open for AP7)

- **AP7:** Warp-drive consistency check — reconstruct warp metric from A4/A5; verify
  flat spacetime as limiting case (Δφ → 0, ε → 1); document compatibility with the
  SRT bridge derived in AP3–AP6.

### 9.4 Significance for RT-40

AP6 closes the falsifiability gap of the RT-40 programme:

| RT-40 Goal | Status |
|-----------|--------|
| Minimal goal: ε = 1/γ² follows from A4 | ✅ AP2 + AP5 |
| Medium goal: Lorentz transformation fully derived | ✅ AP3 (under B₁) |
| Maximal goal: RFT contains SRT + measurable deviation | ✅ AP6 (l_c ∝ γ⁻²) |
| Negative goal: gap documentation | Bridge B₁ still open (AP3) |

---

## Connections to Existing Documents

- AP1 (Phase ↔ Rapidity): [`rt40_ap1_phase_rapidity.md`](rt40_ap1_phase_rapidity.md)
- AP2 (Coupling Efficiency ↔ Lorentz Factor): [`rt40_ap2_coupling_efficiency_lorentz.md`](rt40_ap2_coupling_efficiency_lorentz.md)
- AP3 (Lorentz Transformation): [`rt40_ap3_lorentz_transformation.md`](rt40_ap3_lorentz_transformation.md)
- AP4 (c as Structural Limit): [`rt40_ap4_speed_of_light_limit.md`](rt40_ap4_speed_of_light_limit.md)
- AP5 (Time Dilation, Length Contraction, Coherence Length): [`rt40_ap5_time_dilation_length_contraction.md`](rt40_ap5_time_dilation_length_contraction.md)
- Axioms A1–A7: [`../docs/definitions/axiomatic_foundation.md`](../docs/definitions/axiomatic_foundation.md)
- G_sync Group Structure (RT-02): [`gsync_group_structure.md`](gsync_group_structure.md)
- κ parameter (RT-11): → formally declared as convention
- λ determination (RT-03/RT-12): → external (collaboration required)
- RT-40 Overview: [`../../../../RESEARCH_TASKS.md`](../../../../RESEARCH_TASKS.md)
