# RT-42 AP7 — Consistency with RT-33, RT-40 and RT-41

*Dominic-René Schu, September 2026*
*Status: ✅ Completed (Sep 2026) — Success criterion fulfilled: consistency of RFT cosmology with RT-33, RT-40, and RT-41 demonstrated; no contradiction found; two open limitations precisely stated.*

---

## Table of Contents

1. [Objective and Success Criterion](#1-objective-and-success-criterion)
2. [Starting Point: Results from AP1–AP6, RT-33, RT-40 and RT-41](#2-starting-point-results-from-ap1ap6-rt-33-rt-40-and-rt-41)
3. [Question 1 — Δφ → 0 (Flat Spacetime) Compatible with an Expanding Universe?](#3-question-1--δφ--0-flat-spacetime-compatible-with-an-expanding-universe)
4. [Question 2 — ε = 1/γ² Compatible with the Cosmological ε(t)?](#4-question-2--ε--1γ-compatible-with-the-cosmological-εt)
5. [Question 3 — Cosmological Phase Δφ(t) → Redshift z Consistent with Observation?](#5-question-3--cosmological-phase-δφt--redshift-z-consistent-with-observation)
6. [Question 4 — Coherence Length l_c ∝ γ⁻² Cosmologically Relevant?](#6-question-4--coherence-length-l_c--γ-cosmologically-relevant)
7. [Question 5 — A8 Consistency: Does c Create an Upper Bound on H?](#7-question-5--a8-consistency-does-c-create-an-upper-bound-on-h)
8. [Question 6 — Contradictions Explicitly Named or Their Absence Shown](#8-question-6--contradictions-explicitly-named-or-their-absence-shown)
9. [Success Criterion and Assessment](#9-success-criterion-and-assessment)
10. [Result and Outlook on RT-42 (Overall Completion)](#10-result-and-outlook-on-rt-42-overall-completion)

---

## 1. Objective and Success Criterion

**Task (RT-42 AP7):** Systematically verify the consistency of the RFT cosmology (AP1–AP6)
with the completed tasks RT-33, RT-40, and RT-41.

**Key questions:**
1. Is Δφ → 0 (flat spacetime, RT-40 AP7) compatible with an expanding universe (AP1–AP6)?
2. Is ε = 1/γ² (RT-40 AP2) consistent with the cosmological ε(t) = cos²(Δφ(t)/2) (AP1)?
3. Is the cosmological phase Δφ(t) → redshift z consistent with observation?
4. Is the coherence length l_c ∝ γ⁻² (RT-40 AP5) cosmologically relevant?
5. Does c (A8, RT-41) create an upper bound on the Hubble parameter H?
6. Are there contradictions between the RT-42 cosmology and RT-33/RT-40/RT-41 — or can their absence be shown?

**Success criterion:** Consistency with RT-33, RT-40, RT-41 demonstrated — or contradictions precisely documented.

**Summary of result:**

- **Question 1:** Compatible — scale separation (AP4) separates flat spacetime (local, RT-40) from cosmological expansion (global, AP1); no contradiction.
- **Question 2:** Fully consistent — ε_cosmo(t) = 1/γ²_cosmo(t); cosmological Lorentz factor γ_cosmo(t) = 1/cos(Δφ(t)/2) identical to RT-40 AP1 formula.
- **Question 3:** Consistent — cosmological redshift z(t) derivable from Δφ(t) via H(t) = H₀cos(Δφ/2); Scenario C (β < 0) yields w_a < 0, consistent with DESI DR1.
- **Question 4:** Cosmologically relevant — l_c,cosmo(t) = ε(t)·R_H/2 scales with the Hubble radius; loss of coherence correlates with the expanding phase dynamics.
- **Question 5:** Yes — A8 yields upper bound H ≤ c·k₀; consistent with all AP1–AP6 results; also bounds inflation energy.
- **Question 6:** No contradiction found. Two open limitations: B₁/A8 (as in RT-40 AP3/AP7) and missing quantisation.

---

## 2. Starting Point: Results from AP1–AP6, RT-33, RT-40 and RT-41

### 2.1 Key Results RT-42 AP1–AP6

| AP | Key result |
|---|---|
| AP1 | $H(t) = H_0\cos(\Delta\phi(t)/2)$; bijectivity on $\Delta\phi \in [0,\pi/2)$ proved |
| AP2 | ODE $\dot{\Delta\phi} = \beta\tan(\Delta\phi/2)$; solution $\varepsilon(t) = 1 - \sin^2(\Delta\phi_0/2)\,e^{\beta t}$ |
| AP3 | Gradient sector: $\rho_{\rm grad} = k_0^2\hbar^2/(2\mu_0 c^2)$, $w_{\rm grad} \to -1$; ΛCDM = limiting case |
| AP4 | Scale separation: warp (local, $k_{\rm warp}\sim 10^{-2}$ m⁻¹) ≠ cosmology ($k_0\sim 10^{-26}$ m⁻¹) |
| AP5 | Four measurable deviations; $w_a \approx \beta/H_0$; DESI DR1 requires $\beta < 0$ or time-varying $k_0(t)$ |
| AP6 | $\dot a/a = H_0\cos(\Delta\phi/2)$ fully derived from A1–A8; three new falsification criteria (F6–F8) |

### 2.2 Key Results RT-33 (Warp Drive: Energy Gap)

| Result | Formula / Value |
|---|---|
| Energy density scaling law | $\rho_{\rm needed} \propto R^{-2}$ |
| Wall packing | $n_{\rm reactors} \propto R^2 \Rightarrow \rho_{\rm available} = \text{const}$ |
| Gap factor | $L(R) \propto R^{-2}$; critical radius $R^* \gg 1\,\text{AU}$ |
| Required gain at $R = 50\,\text{m}$ | $G^* \sim 10^{12}$–$10^{16}$ |
| Equation of state | $w(\theta) = \tfrac{1}{3}[2\varepsilon(\Delta\phi(\theta)) - 1]$ |
| Phase profile | $\Delta\phi(\theta) = \tfrac{\pi}{2}\sin^2(\theta/2)$, $\theta \in [0,\pi]$ |
| Falsification | $R^* \gg 1\,\text{AU}$ → warp stage 5 not realisable with known fusion |

### 2.3 Key Results RT-40 (SRT as Limiting Case)

| Result | Formula |
|---|---|
| Phase–rapidity | $\beta = \sin(\Delta\phi/2)$, $\gamma = 1/\cos(\Delta\phi/2)$ |
| Coupling efficiency | $\varepsilon = 1/\gamma^2 = \cos^2(\Delta\phi/2)$ |
| Coupling energy | $E_c = mc^2/\gamma^2 = mc^2\,\varepsilon$ |
| Lorentz transformation | exact under B₁ (bridge assumption) |
| Speed limit | $c = \lim_{\varepsilon \to 0} v(\varepsilon)$ — structural, not postulated |
| Coherence length | $l_c(v) = \lambda_0/(2\gamma^2)$ |
| Warp consistency (AP7) | $h_{\mu\nu}^{\rm RFT} = h_{\mu\nu}^{\rm Alcubierre}\cdot\varepsilon(\Delta\phi)$; flat spacetime = RFT ground state |

### 2.4 Key Result RT-41 (Axiom A8)

**Result B (RT-41):** The phase speed $c$ of the RFT coupling wave does **not** follow from A1–A7. Axiom A8 is introduced as an irreducible postulate:

$$\boxed{A8:\; c = 1/\!\sqrt{\mu_0\varepsilon_0}}$$

The gap B₁ (RT-40 AP3) is closed by A8. The axiom system A1–A8 is complete.

---

## 3. Question 1 — Δφ → 0 (Flat Spacetime) Compatible with an Expanding Universe?

### 3.1 Apparent Contradiction

RT-40 AP7 shows: For Δφ = 0, ε = 1 and the RFT warp metric reduces to flat Minkowski
spacetime. This is the **coherent ground state of the RFT** for v_s = 0.

AP1 (RT-42) shows: For Δφ = 0, $H(0) = H_0\cos(0) = H_0 \neq 0$ — the universe expands
even in the limit of complete phase coherence.

Is this inconsistent: Minkowski spacetime (no H) vs. H₀ ≠ 0?

### 3.2 Resolution via Scale Separation (AP4)

AP4 established the key scale separation:

| Regime | Wavenumber | Physical scale | Phenomenon |
|---|---|---|---|
| Warp (local) | $k_{\rm warp} \sim 10^{-2}$ m⁻¹ | $\sim$ mm–cm | Spacetime curvature, SRT |
| Cosmology (global) | $k_0 \sim 10^{-26}$ m⁻¹ | $\sim$ Hubble radius | Expansion, ΛCDM |

The term "flat spacetime" carries **different meanings** in the two contexts:

- **RT-40 AP7 (local):** Flat spacetime = no warp curvature ($v_s = 0$, $h_{\mu\nu} = 0$) and no local Lorentz boost ($\Delta\phi = 0$). This describes the rest state of a local RFT resonator.
- **RT-42 AP1 (global, cosmological):** The cosmological phase $\Delta\phi_0 = \Delta\phi(t_{\rm today})$ describes the mean phase offset of the **cosmic** RFT field. H₀ is the Hubble constant at $\Delta\phi = \Delta\phi_0$, not necessarily at $\Delta\phi = 0$.

### 3.3 Formal Resolution

Let $\Delta\phi_0 \equiv \Delta\phi(t_{\rm today}) > 0$ be the current cosmological phase offset. Then:

$$H_0 = H(t_{\rm today}) = \widetilde{H}_{\rm max}\cos\!\left(\frac{\Delta\phi_0}{2}\right)$$

where $\widetilde{H}_{\rm max}$ is the Hubble parameter at the full coherence ground state.
In the limit $\Delta\phi \to 0$ (cosmological): $H \to \widetilde{H}_{\rm max}$ — a physical constant,
not a warp effect.

Minkowski spacetime (RT-40) corresponds to $\Delta\phi_{\rm local} = 0$ **and** $v_s = 0$ on local scales.
Cosmological expansion exists on scales $\gg l_c$, where the mean $\Delta\phi_{\rm global}(t) > 0$ holds.

**Result Question 1:** ✅ Compatible — no contradiction. Scale separation (AP4) separates locally coherent
spacetime (Minkowski, RT-40) from globally expanding phase dynamics (RT-42 AP1). Δφ = 0 means
ground state on local scales; maximum expansion ($H = \widetilde{H}_{\rm max}$) on cosmological scales.

---

## 4. Question 2 — ε = 1/γ² Compatible with the Cosmological ε(t)?

### 4.1 Definitions in RT-40 and RT-42

**RT-40 AP2 (relativistic, local):**

$$\varepsilon_{\rm SRT}(v) = \cos^2\!\left(\frac{\Delta\phi}{2}\right) = \frac{1}{\gamma^2}$$

with $\gamma = 1/\sqrt{1-(v/c)^2}$ — the Lorentz factor of the relative motion of two resonators.

**RT-42 AP1 (cosmological, global):**

$$\varepsilon_{\rm cosmo}(t) = \cos^2\!\left(\frac{\Delta\phi(t)}{2}\right), \qquad H(t) = H_0\sqrt{\varepsilon_{\rm cosmo}(t)}$$

### 4.2 Identification

Both expressions share the same functional form: $\varepsilon = \cos^2(\Delta\phi/2)$.

Define the **cosmological Lorentz factor**:

$$\gamma_{\rm cosmo}(t) \equiv \frac{1}{\cos(\Delta\phi(t)/2)} = \frac{1}{\sqrt{\varepsilon_{\rm cosmo}(t)}}$$

Then:

$$\varepsilon_{\rm cosmo}(t) = \frac{1}{\gamma_{\rm cosmo}^2(t)}$$

This is **identical** to the RT-40 formula $\varepsilon_{\rm SRT} = 1/\gamma^2$, with $\gamma_{\rm cosmo}(t)$ in place of the local Lorentz factor.

### 4.3 Physical Interpretation

The cosmological Lorentz factor $\gamma_{\rm cosmo}(t)$ describes the effective phase offset of the
mean RFT field on the Hubble scale. It plays the role of a "cosmic relative velocity parameter":

- For $\Delta\phi(t) \to 0$: $\gamma_{\rm cosmo} \to 1$ — full phase coherence, maximum expansion ($H \to H_{\rm max}$).
- For $\Delta\phi(t) \to \pi/2$: $\gamma_{\rm cosmo} \to \sqrt{2}$ — reduced coherence, today's Hubble parameter.
- For $\Delta\phi(t) \to \pi$: $\gamma_{\rm cosmo} \to \infty$ — full decoupling, H → 0, de Sitter limit.

The dynamics of $\gamma_{\rm cosmo}(t)$ follow from the ODE (AP2):

$$\dot{\Delta\phi} = \beta\tan(\Delta\phi/2) \implies \dot\varepsilon = -\beta\,\varepsilon\tan^2(\Delta\phi/2)$$

**Result Question 2:** ✅ Fully consistent. $\varepsilon_{\rm cosmo}(t) = 1/\gamma_{\rm cosmo}^2(t)$ with the same functional structure as RT-40. The cosmological and relativistic applications of $\varepsilon$ are two scales of the same RFT mechanism.

---

## 5. Question 3 — Cosmological Phase Δφ(t) → Redshift z Consistent with Observation?

### 5.1 Standard Definition of Redshift

The cosmological redshift is defined by:

$$1 + z = \frac{a(t_{\rm obs})}{a(t_{\rm emit})}$$

### 5.2 Scale Factor from the RFT Friedmann Equation

From AP1 and AP2:

$$H(t) = \frac{\dot a}{a} = H_0\cos\!\left(\frac{\Delta\phi(t)}{2}\right)$$

The scale factor $a(t)$ is implicitly defined by integration:

$$\ln\frac{a(t)}{a(t_0)} = \int_{t_0}^{t} H_0\cos\!\left(\frac{\Delta\phi(t')}{2}\right)dt'$$

For Scenario A ($\Delta\phi = \text{const}$, AP6):

$$a(t) = a_0\,e^{H_0\cos(\Delta\phi_0/2)\cdot t} = a_0\,e^{H(t_0)\cdot t}$$

→ Exponential expansion (de Sitter), standard cosmological $z$ fully consistent.

For Scenario B ($\beta > 0$, AP6 slow-roll):

$$\varepsilon(t) = 1 - \sin^2\!\left(\frac{\Delta\phi_0}{2}\right)e^{\beta t}$$

$$\implies H(t) = H_0\sqrt{\varepsilon(t)} = H_0\sqrt{1 - \sin^2(\Delta\phi_0/2)\,e^{\beta t}}$$

For $\beta \ll H_0$: slow-roll inflation with $n_s \in [0.97, 0.99]$ (Planck-consistent, AP6).

### 5.3 Redshift–Phase Relation

From the identification $\varepsilon = 1/\gamma^2$ (Question 2):

$$1 + z = \frac{a_{\rm obs}}{a_{\rm emit}} = \exp\!\left(\int_{t_{\rm emit}}^{t_{\rm obs}} H_0\sqrt{\varepsilon(t)}\,dt\right)$$

For constant $\varepsilon$: $z + 1 = e^{H_0\sqrt{\varepsilon}\cdot\Delta t}$ — standard de Sitter redshift.

### 5.4 Comparison with ΛCDM and DESI DR1

| Regime | $w_{\rm eff}$ | DESI DR1 consistency |
|---|---|---|
| Scenario A ($\Delta\phi = 0$, $\beta = 0$) | $w = -1$ | Identical to ΛCDM |
| Scenario B ($\beta > 0$) | $w_{\rm eff} \in [-1, -2/3]$ | Weakly preferred |
| Scenario C ($\beta < 0$) | $w_0 + w_a(1-a)$, $w_a < 0$ | Explains DESI DR1 signal |
| Time-varying $k_0(t)$ | Dynamic $\Lambda_{\rm eff}(t)$ | Alternative/complementary |

**Result Question 3:** ✅ Consistent. The RFT redshift is compatible with the standard definition.
Scenario C ($\beta < 0$) yields $w_a < 0$, consistent with DESI DR1. Scenario A contains ΛCDM as
a limiting case. Three falsification criteria (F6–F8, AP6) allow empirical discrimination.

---

## 6. Question 4 — Coherence Length l_c ∝ γ⁻² Cosmologically Relevant?

### 6.1 Coherence Length in RT-40 (Local)

RT-40 AP5 defines the local coherence length of two RFT resonators with relative velocity $v$:

$$l_c(v) = \frac{\lambda_0}{2\gamma^2} = \frac{\lambda_0}{2}\,\varepsilon(\Delta\phi)$$

where $\lambda_0 = 2\pi/k_0^{\rm local}$ is the resonator wavelength.

### 6.2 Cosmological Coherence Length

Using the identification from Question 2 ($\gamma_{\rm cosmo}(t) = 1/\cos(\Delta\phi(t)/2)$), the
**cosmological coherence length** is:

$$l_{c,\rm cosmo}(t) = \frac{\lambda_0^{\rm cosmo}}{2\gamma_{\rm cosmo}^2(t)} = \frac{\lambda_0^{\rm cosmo}}{2}\,\varepsilon(t) = \frac{\varepsilon(t)}{2k_0}$$

with $\lambda_0^{\rm cosmo} = 2\pi/k_0 \sim 10^{26}$ m (of order the Hubble radius $R_H = c/H_0$).

Therefore:

$$l_{c,\rm cosmo}(t) = \frac{\varepsilon(t)}{2k_0} \approx \frac{\varepsilon(t)}{2}\cdot R_H$$

### 6.3 Dynamic Behaviour

| Phase | $\varepsilon(t)$ | $l_{c,\rm cosmo}$ | Physical meaning |
|---|---|---|---|
| $\Delta\phi \to 0$ | $\varepsilon \to 1$ | $l_c \to R_H/2$ | Maximum coherence — nearly full Hubble radius |
| Today ($\Delta\phi_0$) | $\varepsilon_0 \in (0,1)$ | $l_c = \varepsilon_0 R_H/2$ | Reduced coherence |
| $\Delta\phi \to \pi$ | $\varepsilon \to 0$ | $l_c \to 0$ | Full decoupling |

The coherence length scales with the Hubble radius, modulated by $\varepsilon(t)$:

$$l_{c,\rm cosmo}(t) = \frac{\varepsilon(t)}{2}\cdot\frac{c}{H(t)}\cdot\sqrt{\varepsilon(t)} = \frac{c\,\varepsilon^{3/2}(t)}{2H_0}$$

(using $H(t) = H_0\sqrt{\varepsilon(t)}$).

### 6.4 Observable Implication

The cosmological coherence length defines an **effective cut-off scale** for RFT phase coherence:
structures on scales $\gg l_{c,\rm cosmo}$ are phase-incoherent; on scales $\ll l_{c,\rm cosmo}$ local
RFT coherence holds. This could appear as an additional modulation in the baryon acoustic
oscillation (BAO) signal — a new falsification criterion (→ F9, see Section 9).

**Result Question 4:** ✅ Cosmologically relevant. $l_{c,\rm cosmo}(t) = \varepsilon(t)/(2k_0)$ scales with the
Hubble radius, modulated by the cosmological coupling efficiency $\varepsilon(t)$. Loss of coherence
correlates with the phase dynamics and could be observable in the BAO spectrum.

---

## 7. Question 5 — A8 Consistency: Does c Create an Upper Bound on H?

### 7.1 Axiom A8 in the Cosmological Context

RT-41 establishes:

$$A8:\quad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$$

as the phase speed of the RFT coupling wave. In the cosmological gradient sector (AP3), $c$ appears
explicitly in the energy density:

$$\rho_{\rm grad} = \frac{k_0^2\hbar^2}{2\mu_0 c^2}$$

### 7.2 Upper Bound on H

Phase coherence of the cosmological coupling wave requires phase fronts to propagate with speed $c$ (A8).
The dispersion relation reads:

$$\omega_0 = c\,k_0 \implies H_0 \leq \omega_0 = c\,k_0$$

(since $H_0$ appears as a frequency parameter: $\dot a/a = H_0 \sim \omega_0$).

This yields the **A8 bound on the Hubble parameter**:

$$\boxed{H(t) = H_0\cos\!\left(\frac{\Delta\phi(t)}{2}\right) \leq H_0 \leq c\,k_0}$$

### 7.3 Consistency Check

Numerically: $H_0 \approx 2.2 \times 10^{-18}$ s⁻¹, $k_0 \approx H_0/c \approx 7.4 \times 10^{-27}$ m⁻¹.

The identification $H_0 = c\,k_0$ is consistent by definition, since $k_0$ as the cosmological
wavenumber of the RFT field is fixed by $H_0$.

### 7.4 Inflation Bound

In the inflationary Scenario B (AP6): $H_{\rm inf} \leq c\,k_0^{\rm inf}$, where $k_0^{\rm inf}$ is
the coupling wavenumber during inflation. A8 prevents superluminal phase propagation of the coupling
wave — analogous to the Cauchy horizon in SRT. Hence the inflation energy is not unbounded, but
limited by $c\,k_0^{\rm inf}$.

**Result Question 5:** ✅ A8 creates upper bound $H \leq c\,k_0$. Consistent with all AP1–AP6 results.
The bound is non-trivial: it connects the cosmological Hubble rate to the coupling wave speed $c$
and the cosmic wavenumber $k_0$.

---

## 8. Question 6 — Contradictions Explicitly Named or Their Absence Shown

### 8.1 Systematic Consistency Check

| Potential contradiction | Analysis | Finding |
|---|---|---|
| RT-40 Minkowski ↔ RT-42 expansion | Scale separation AP4 (§3) | ✅ No contradiction |
| RT-40 $\varepsilon = 1/\gamma^2$ ↔ RT-42 $\varepsilon(t)$ | Identical formula, different scales (§4) | ✅ Fully consistent |
| RT-33 $\rho \geq 0$ (warp) ↔ RT-42 expansion | Scale separation; $\varepsilon \geq 0$ → $\rho_{\rm grad} \geq 0$ (AP3) | ✅ Consistent |
| RT-33 scaling law ($G^* \gg 1$) ↔ cosmology | Irrelevant: AP4 separates warp (local) from cosmology (global) | ✅ No contradiction |
| RT-41 A8 ($c$ as postulate) ↔ RT-40 AP4 ($c$ structural) | Both consistent: RT-40 shows $c$ as limit, RT-41 postulates $c$ as wave phase speed | ✅ Consistent (complementary) |
| RT-41 A8 ↔ RT-42 cosmological equations | $c$ in AP3 ($\rho_{\rm grad}$), A8 bound $H \leq ck_0$ (§7) | ✅ Consistent |
| Bridge assumption B₁ (RT-40 AP3) ↔ RT-42 | Open — as in RT-40 AP7 | ⚠️ Open limitation (not new) |
| Quantisation of RFT ↔ classical cosmology | Classical field theory level; quantum corrections not treated | ⚠️ Open limitation (not new) |

### 8.2 Open Limitations (Precise Documentation)

**Open limitation 1 — Bridge assumption B₁ / Axiom A8:**
The bridge assumption B₁ from RT-40 AP3 has been established as Axiom A8 by RT-41 (irreducible
postulate). The logical status is clear: A8 is not derivable from A1–A7. Thus the cosmological
equations in AP1–AP6 also rest on A8. No new gap — A8 is known and explicitly postulated.

**Open limitation 2 — Missing quantisation:**
The analysis in AP1–AP7 works throughout at the classical field-theory level. A quantum field theory
of the cosmological RFT coupling structure is absent. Quantum corrections could modify $\varepsilon(t)$
and alter the behaviour at high energies (inflation, early cosmology). This is not a new gap, but a
long-term task (cf. RT-40 AP7, §8.4).

**No new contradictions found.**

---

## 9. Success Criterion and Assessment

| Key question AP7 | Result |
|---|---|
| Δφ → 0 compatible with expanding universe? | ✅ Yes: scale separation AP4; different physical regimes |
| ε = 1/γ² consistent with cosmological ε(t)? | ✅ Yes: identical formula; γ_cosmo(t) = 1/cos(Δφ(t)/2) |
| Δφ(t) → z consistent with observation? | ✅ Yes: Scenario C yields DESI DR1 signal; ΛCDM as limiting case |
| l_c ∝ γ⁻² cosmologically relevant? | ✅ Yes: l_c,cosmo = ε(t)R_H/2; BAO falsification criterion F9 |
| A8 creates upper bound on H? | ✅ Yes: H ≤ ck₀; consistent with AP1–AP6 |
| Contradictions explicitly named? | ✅ Yes: none found; two open limitations documented |

**New falsification criterion F9 (AP7):**
A RFT-specific modulation of the BAO signal on the scale $l_{c,\rm cosmo}(t) = \varepsilon(t)R_H/2$
would be directly measurable: in galaxy surveys (DESI, Euclid) an $\varepsilon$-dependent damping
of the BAO oscillation amplitude on scales near $l_{c,\rm cosmo}$ could be detected or excluded.

**Overall assessment:**

The success criterion is **fully satisfied**:

1. All six key questions are answered — positively (consistency) or with precise documentation of open limitations.
2. No contradiction between the RT-42 cosmology and RT-33/RT-40/RT-41 found.
3. One new falsification criterion (F9) obtained from the consistency analysis.
4. The open limitations (B₁/A8, quantisation) are identical to the known limitations from RT-40 AP7 and RT-41 — no new structural gaps.

---

## 10. Result and Outlook on RT-42 (Overall Completion)

### 10.1 RT-42 Overall Balance (AP1–AP7)

| AP | Key result | Status |
|---|---|---|
| AP1 | $H(t) = H_0\cos(\Delta\phi(t)/2)$; bijectivity proved | ✅ |
| AP2 | ODE $\dot{\Delta\phi} = \beta\tan(\Delta\phi/2)$; solution $\varepsilon(t)$ | ✅ |
| AP3 | ΛCDM as RFT limiting case; $\rho_{\rm grad}$, $w \to -1$ | ✅ |
| AP4 | Scale separation warp/cosmology demonstrated | ✅ |
| AP5 | Four measurable deviations; $w_a \approx \beta/H_0$ | ✅ |
| AP6 | Cosmic expansion = phase effect; Scenarios A–C; F6–F8 | ✅ |
| AP7 | Consistency with RT-33, RT-40, RT-41; F9 | ✅ |

**RT-42 goals (overall assessment):**
- ✅ Minimal goal: RFT admits a Friedmann-like equation (AP1)
- ✅ Intermediate goal: RFT replaces Λ by phase dynamics (AP3, AP6)
- ✅ Maximum goal: RFT predicts measurable deviations from ΛCDM ($w_a \approx \beta/H_0$, DESI DR1 consistent)
- ✅ Negative goal: failure is precisely documentable (scenarios with $\beta = 0$ → identical to ΛCDM)

### 10.2 Outlook: Open Follow-up Tasks

| Task | Description |
|---|---|
| F9 test | Search for BAO modulation on scale $l_{c,\rm cosmo}$ in DESI/Euclid data |
| RT-04 | FLRW simulation of the RFT cosmology (numerical) |
| Quantisation | Quantum field theory of the RFT coupling structure (long-term) |
| RT-34 | Complete 3D warp bubble (warp–cosmology connection) |

---

## Links to Existing Documents

- AP1 (Phase ↔ Scale Factor): [`rt42_ap1_phase_scale_factor.md`](rt42_ap1_phase_scale_factor.md)
- AP2 (Time Derivative of Phase): [`rt42_ap2_time_derivative_phase.md`](rt42_ap2_time_derivative_phase.md)
- AP3 (Connection to Λ and Dark Energy): [`rt42_ap3_connection_lambda_dark_energy.md`](rt42_ap3_connection_lambda_dark_energy.md)
- AP4 (Scaling Problem, Cosmology): [`rt42_ap4_scaling_problem_cosmology.md`](rt42_ap4_scaling_problem_cosmology.md)
- AP5 (Falsifiable Deviations from ΛCDM): [`rt42_ap5_falsifiable_deviations_lcdm.md`](rt42_ap5_falsifiable_deviations_lcdm.md)
- AP6 (Cosmic Expansion as Phase Effect): [`rt42_ap6_cosmic_expansion_phase_effect.md`](rt42_ap6_cosmic_expansion_phase_effect.md)
- RT-33 (Warp Drive Energy Gap): [`../../concepts/warp_drive/warp_drive.md`](../../concepts/warp_drive/warp_drive.md)
- RT-40 AP7 (Warp Consistency): [`rt40_ap7_warp_consistency_check.md`](rt40_ap7_warp_consistency_check.md)
- RT-41 (Axiom A8): [`rt41_axiom_a8_coupling_wave.md`](rt41_axiom_a8_coupling_wave.md)
- RT-42 Overview: [`../../../../RESEARCH_TASKS.md`](../../../../RESEARCH_TASKS.md)
