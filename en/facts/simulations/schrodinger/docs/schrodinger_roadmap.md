# Schrödinger Roadmap (Research Program, Minimal Proof)

Goal: Formulate a clean, reproducible path showing how a resonance-/phase-based mode model yields the non-relativistic Schrödinger equation in the appropriate limit, and in parallel implement a numerical reference against which a later resonance discrete model can be checked.

No publication claim. No statements on GR/gauge theories. Focus: QM of a single particle.

---

## A. Minimal Goal (Reference Equation)

We want to reproduce as target equation:

$$
 i\hbar\,\partial_t\psi(x,t)= -\frac{\hbar^2}{2m}\,\nabla^2\psi(x,t)+V(x)\psi(x,t)
$$

with:
- $\psi$: complex wave function (amplitude + phase)
- $m$: effective mass (parameter/scale)
- $V(x)$: external potential (parameter field)
- $\hbar$: scale factor for coupling between phase and energy

---

## B. Minimal Assumptions (Resonance/Mode Model → QM)

We assume a discrete field (lattice) of degrees of freedom that oscillates locally and couples via nearest neighbors:

- Grid points $x_n = n\,a$ with grid spacing $a$
- Field variable: phase $\varphi_n(t)$ and (optionally) amplitude $A_n(t)$
- Complex field representation:
  $$
  \psi_n(t) := A_n(t)\,e^{i\varphi_n(t)}
  $$
- Local frequency / energy reference (as working definition):
  $$
  E_n = \hbar\,\omega_n \quad,\quad \omega_n:=\partial_t\varphi_n
  $$
- Coupling: a function of the phase difference $\Delta\varphi_{n,n+1}$, e.g. via a coupling term that in the continuum limit leads to a Laplace operator.

Important: The concrete form $\varepsilon(\Delta\varphi)$ remains open here. What matters is only: in the small-gradient limit the coupling term must reduce to something like $\partial_x^2 \psi$.

---

## C. Concrete Path (Discrete → Continuous → Schrödinger Form)

### Step C1: Discrete Complex Field and Linear Approximation
The starting point is not "energy balance" but a dynamical equation for $\psi_n(t)$. For small phase gradients and weak coupling a linear approximation is plausible:

$$
 i\,\partial_t \psi_n \approx -\kappa\,(\psi_{n+1}-2\psi_n+\psi_{n-1}) + U_n\,\psi_n
$$

- $\kappa$ is a coupling strength with dimension $1/\text{time}$
- $U_n$ is a local term (corresponding later to $V/\hbar$)

This form is deliberately chosen because the discrete Laplace operator is already visible.

### Step C2: Continuum Limit
Set $x = n a$, $\psi_n(t)\to \psi(x,t)$ and use:

$$
\psi_{n\pm1} = \psi(x\pm a,t) \approx \psi \pm a\partial_x\psi + \frac{a^2}{2}\partial_x^2\psi
$$

Then:

$$
\psi_{n+1}-2\psi_n+\psi_{n-1} \approx a^2 \partial_x^2\psi
$$

This gives:

$$
 i\,\partial_t\psi = -\kappa\,a^2\,\partial_x^2\psi + U(x)\psi
$$

### Step C3: Identification of $\hbar$, $m$, $V$
Compare with:

$$
 i\hbar\,\partial_t\psi = -\frac{\hbar^2}{2m}\partial_x^2\psi + V\psi
$$

and identify:

$$
 \kappa a^2 \equiv \frac{\hbar}{2m}
 \quad,\quad
 U(x) \equiv \frac{V(x)}{\hbar}
$$

This clarifies what "mass" means in the resonance model: an effective inertia scale that arises from coupling strength and discretization.

### Step C4: Where "Resonance" Enters the Equation
In the resonance picture, the physics is encoded in the choice of coupling mechanism that in the small-gradient limit generates exactly this Laplace term.

Open design question:
- Which $\varepsilon(\Delta\varphi)$ leads to linear coupling in $\psi$?
- Which nonlinear corrections arise (leading e.g. to nonlinear Schrödinger equation)?
- Which stability conditions hold (norm conservation, unitarity)?

---

## D. Numerical Reference (Important for Later Falsification/Comparison)

Before a resonance discrete model claims "Schrödinger emergent", a reference is implemented:

- 1D, free particle $V=0$ (mandatory test)
- optional: harmonic oscillator or potential well
- Initial state: Gaussian wave packet
- Checks:
  - Norm conservation $\int |\psi|^2 dx$
  - Expectation values $\langle x\rangle, \langle p\rangle$
  - Qualitative spreading (dispersion)

This reference serves as a regression test: the resonance model must (in the appropriate parameter regime) reproduce these curves.

---

## E. Open Points / TODOs (explicit)

1. **$\varepsilon(\Delta\varphi)$**: analytical specification + justification of why the Laplace term arises in the limit.
2. **Units/calibration**: Dimensionless vs. SI scales. At minimum: unambiguous documentation of which quantities are dimensionless.
3. **Derivation instead of postulate**: In the long run, an action principle (Lagrange/Hamilton) is needed from which the discrete dynamics follows.
4. **Demarcation**: No cosmological/thermodynamic claims as long as the QM minimal case is not established.

---

## E′. Critique Point: What the Referee Will Ask Next

### The Tautology Problem

The previous derivation shows:

$$
\hat{H}_{\mathrm{res}} = \hat{H}_0 + \varepsilon(\Delta\varphi)\,\hat{V}_{\mathrm{coupling}}
$$

reproduces standard QM with $V_{\mathrm{eff}} = \varepsilon \cdot V_{\mathrm{coupling}}$.

This is mathematically a **tautology**: the split operator sees only $V_{\mathrm{eff}}$, regardless of whether it is supplied as $\varepsilon(\Delta\varphi) \cdot V$ via a coupling or directly as a potential. A critical referee will notice this immediately.

### The Decisive Open Question: Where Does $\Delta\varphi$ Come From?

| Question | Why decisive |
|-------|-------------------|
| Is $\Delta\varphi$ an external parameter or a dynamical field? | If external → RFT is just a reparametrization of standard QM |
| Does $\Delta\varphi$ have its own equation of motion? | If yes → new physics possible (and testable) |
| How does $\Delta\varphi$ couple to the state $\psi$? | Feedback $\psi \to \Delta\varphi \to V_{\mathrm{eff}} \to \psi$ would be non-trivial |

### Concrete Recommendation

A `schrodinger_1d_rft_dynamic.py` in which $\Delta\varphi(t)$ is **itself dynamic** — e.g. coupled to $|\psi|^2$ or to $\langle x \rangle$ — would for the first time make RFT **distinguishable** from standard QM. Only then can one say: *"RFT is not merely a rewriting, but an extension."*

This is also the point at which critique point 2.1 (GR limit) and 2.2 (gauge invariance) first become approachable — once the dynamics of $\Delta\varphi$ is fixed, predictions can be derived that are experimentally testable.

**Status:** Implemented in [`python/schrodinger_1d_rft_dynamic.py`](../python/schrodinger_1d_rft_dynamic.py).

---

## G. Perturbation Theory of RFT — Convergence toward Standard QM

### Recommendation (addressed)

> In the limit λ → 0 (weak feedback) the dynamic RFT must converge toward
> standard QM, with leading corrections of order O(λ). This is the
> perturbation theory of RFT.

### Perturbation Expansion

Write $\psi_{\mathrm{RFT}} = \psi_0 + \lambda\,\psi_1 + O(\lambda^2)$
and $\Delta\varphi(t) = \Delta\varphi_0 + \lambda\,\varphi_1(t) + O(\lambda^2)$.

**Zeroth order** ($\lambda = 0$):

$$
i\hbar\,\partial_t\psi_0 = [\hat{H}_0 + \varepsilon(\Delta\varphi_0)\,V]\,\psi_0
$$

This is exactly the standard Schrödinger equation with $V_{\mathrm{eff}} = \varepsilon_0 \cdot V$.

**First order**:

$$
i\hbar\,\partial_t\psi_1 = [\hat{H}_0 + \varepsilon_0\,V]\,\psi_1 + \varepsilon'(\Delta\varphi_0)\,\varphi_1(t)\,V\,\psi_0
$$

where $\varphi_1(t) = \int_0^t F[\psi_0(t')]\,\mathrm{d}t'$ is the integrated
feedback functional of the unperturbed solution.

### Numerical Verification

The simulation [`python/schrodinger_1d_rft_perturbation.py`](../python/schrodinger_1d_rft_perturbation.py)
confirms the perturbation theory via a systematic λ scan:

| Observable | Scaling (numerical) | Expected (theory) |
|------------|------------------------|--------------------|
| 1 − Fidelity | ~ λ^2.00 | O(λ²) |
| \|Δ⟨x⟩\| | ~ λ^1.00 | O(λ) |
| \|Δ⟨p⟩\| | ~ λ^1.00 | O(λ) |
| max\|Δψ\| | ~ λ^1.00 | O(λ) |

In addition, the first-order analytical prediction for Δε agrees with
the numerics to relative errors < 0.02%.

### Consequences

1. **Standard QM is exact limiting case:** For λ = 0 the dynamic RFT reproduces
   the standard Schrödinger equation identically
   (Fidelity = 1.000000000000).

2. **Controlled corrections:** Deviations are O(λ) in
   expectation values and O(λ²) in state fidelity — the RFT is
   a well-defined extension with a controlled parameter space.

3. **Norm conservation:** For all λ the norm is conserved (< 10⁻¹³),
   since V_eff is always real and the split operator remains unitary.

**Status:** Implemented in [`python/schrodinger_1d_rft_perturbation.py`](../python/schrodinger_1d_rft_perturbation.py).

---

## H. Critique Points — Gisin Theorem, Axiom Derivation, Measurement Data

### H.1 Axiomatic Derivation of the Feedback Model

**Critique point:** The three models (density, position, energy) in the
dynamic simulation are ad hoc. Which one follows from the RFT axioms?

**Answer (Section G of the roadmap):**

The density model $\dot{\Delta\varphi} = \lambda \int |\psi|^4\,\mathrm{d}x$
can be motivated from the RFT formalism as follows:

1. The RFT coupling functional contains the term
   $S_{\mathrm{coupling}}[\psi, \varphi] = \int \varepsilon(\Delta\varphi) \cdot |\psi(x)|^2\,\mathrm{d}x$.

2. Variation with respect to $\Delta\varphi$ yields $\varepsilon'(\Delta\varphi)$
   as the source of the phase dynamics.

3. The localization term $\int |\psi|^4\,\mathrm{d}x$ arises as the
   lowest nonlinear correction in the effective action functional
   (analogous to the Gross-Pitaevskii derivation from the contact interaction term).

4. The position and energy models remain as **alternative
   feedback hypotheses** — they are empirically testable once
   measurement data are available (critique point H.3).

**Open point:** ~~A complete derivation from an
RFT action principle (Hamilton/Lagrange formalism) is outstanding.~~
→ **Addressed** in [`schrodinger_1d_rft_lagrangian.py`](../python/schrodinger_1d_rft_lagrangian.py):

The RFT action functional is:

$$
S[\psi, \Delta\varphi] = \int \mathrm{d}t \left[
\langle\psi|i\hbar\partial_t - \hat{H}_0|\psi\rangle
- \varepsilon(\Delta\varphi)\langle V\rangle_\psi
+ \frac{\mu}{2}(\dot{\Delta\varphi})^2
\right]
$$

The Euler-Lagrange equation for Δφ yields:
- **Inertial regime (μ > 0):** $\mu\ddot{\Delta\varphi} = \frac{1}{2}\sin(\Delta\varphi)\cdot\langle V\rangle_\psi$
- **Overdamped regime (γ):** $\gamma\dot{\Delta\varphi} = \frac{1}{2}\sin(\Delta\varphi)\cdot\langle V\rangle_\psi$

The density model is identified as the effective limit of the overdamped regime. The Noether energy $E = \langle\hat{H}_\mathrm{res}\rangle + \frac{\mu}{2}(\dot{\Delta\varphi})^2$
is numerically conserved (rel. deviation < 0.3%).

### H.2 Gisin Theorem and No-Signaling Condition

**Critique point:** Nonlinear QM in principle allows superluminal
signaling (Gisin 1990). Does the RFT dynamics violate the
no-signaling condition?

**Answer:**

1. **1-particle sector:** In the present 1D simulation there is
   no signaling problem. The dynamics is nonlinear, but local
   (no second particle to which a signal could be sent).

2. **Norm is conserved:** Since $V_{\mathrm{eff}}$ is always real, the
   split operator remains unitary at each individual step. Numerically confirmed:
   norm deviation < 10⁻¹³ for all λ.

3. **Perturbative protection:** In the limit λ → 0 the dynamics is strictly
   linear and unitary → no-signaling holds exactly. For 0 < λ ≪ 1
   deviations from linearity are O(λ) — the Gisin theorem applies
   only at finite λ in the many-body sector.

4. **2-particle analysis (addressed):**
   → Implemented in [`schrodinger_1d_rft_two_particle.py`](../python/schrodinger_1d_rft_two_particle.py)

   The complete Gisin protocol was numerically implemented:
   - Entangled state |Ψ⟩ = (|L⟩_A|↑⟩_B + |R⟩_A|↓⟩_B) / √2
   - Alice measures in two different bases (X: L/R, Z: +/−)
   - Bob's states are propagated with RFT dynamics
   - Comparison of ρ_B(t) for both bases

   **Results:**
   - λ = 0 (standard QM): No-signaling exact (D ~ 10⁻¹⁵) ✓
   - **Global Δφ:** No-signaling **violated** (D ~ 0.58 at λ = 2)
     → Different measurement bases generate different ∫|ψ|⁴dx
     → Different Δφ trajectories → different ε(t) → different ρ_B
   - **Local Δφ:** No-signaling **preserved** (by construction)
     → Δφ_B depends only on ρ_B, not on Alice's basis

   **Consequence:** RFT must use **local coupling structure**:
   φ(x,t) is a local field (like the EM field), not a global parameter.
   This is physically natural and consistent with GR locality.

### H.2b Theoretical Expectation for λ

**Critique point:** Without an order of magnitude it remains unclear whether the experiment has a chance.

→ Implemented in [`schrodinger_1d_rft_lambda_bounds.py`](../python/schrodinger_1d_rft_lambda_bounds.py)

**Result:** Five perspectives on λ:

| Approach | λ (order of magnitude) | Reachable? |
|--------|-------------------:|-------------|
| Gravitational (Penrose/Diósi) | 10⁻³⁵ | no |
| BSM (electroweak α²) | 10⁻⁴ | no (10⁴ shots) |
| Decoherence (spontaneous emission) | 10⁻⁶ | no |
| Experiment (100 shots) | 0.62 | limit |
| Experiment (10 000 shots) | 0.062 | limit |

**Recommendation:** The experiment is meaningful as a **bounds experiment**.
If no effect is seen → upper bound on λ.
If effect is seen → discovery!

### H.3 Contact with Measurement Data (addressed)

**Critique point 3.1 (SI units, calibration) is addressed.**
Critique point 2.1 (GR limit) remains open.

The perturbation theory results have been mapped to a concrete physical
system: **ultracold ⁸⁷Rb atoms in a harmonic trap**.

**Falsifiable prediction:**

$$
|\Delta\langle x\rangle|_\mathrm{SI} = 4.9 \cdot \lambda \cdot \ell
\approx 2.0 \cdot \lambda\;\mu\mathrm{m}
$$

where $\ell = V_\mathrm{strength}^{1/4} \cdot a_\mathrm{ho}$ is the
length unit of the simulation. For $\omega = 2\pi \times 100\;\mathrm{Hz}$
this gives $a_\mathrm{ho} \approx 1.08\;\mu\mathrm{m}$ and
$\ell \approx 0.41\;\mu\mathrm{m}$.

The prediction is measurable via absorption imaging (time-of-flight)
with spatial resolution ~ 1 µm. Detection limit:
$\lambda \gtrsim 0.05$ after 100 repetitions.

| Step | Description | Status |
|---------|-------------|--------|
| Calibration | Map dimensionless parameters to SI units | ✅ [`schrodinger_1d_rft_experiment.py`](../python/schrodinger_1d_rft_experiment.py) |
| Experimental proposal | Falsifiable prediction for ⁸⁷Rb | ✅ [`experimental_proposal.md`](experimental_proposal.md) |
| Critical assessment | GP problem (Kohn), systematics, referee questions | ✅ `--critical` flag + [Section 6](experimental_proposal.md#6-critical-assessment) |
| GR limit | Coupling of φ to the metric | ❌ Open (deliberately excluded) |

---

## I. Next Steps (updated)
- ~~Implement `schrodinger_1d_free_particle.py` as reference.~~ ✓ (`schrodinger_1d_reference.py`)
- ~~Add smoke test: norm deviation after N steps < tolerance.~~ ✓
- ~~Build a minimal phase coupling model and compare numerically against the reference.~~ ✓ (`schrodinger_1d_rft.py`)
- ~~Dynamic phase coupling $\Delta\varphi(t)$ with feedback to $|\psi|^2$.~~ ✓ (`schrodinger_1d_rft_dynamic.py`)
- ~~Perturbation theory: λ scan, scaling analysis, analytical prediction.~~ ✓ (`schrodinger_1d_rft_perturbation.py`)
- ~~SI calibration and experimental proposal.~~ ✓ (`schrodinger_1d_rft_experiment.py`)
- ~~Critical assessment: GP problem, systematics, peer-review balance sheet.~~ ✓ (`--critical`)
- ~~2-particle extension for Gisin theorem / no-signaling~~ ✓ (`schrodinger_1d_rft_two_particle.py`)
- ~~Action principle (Lagrangian density) for the feedback~~ ✓ (`schrodinger_1d_rft_lagrangian.py`)
- ~~Theoretical expectation for λ~~ ✓ (`schrodinger_1d_rft_lambda_bounds.py`)
- **Open:** GR limit (deliberately excluded)
- **Open:** Gauge invariance of the Δφ dynamics
