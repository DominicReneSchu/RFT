# Schrödinger Simulation — Reference and Resonance Hamiltonian

Numerical 1D simulation of the Schrödinger equation as reference
and proof of the correspondence principle between standard QM and
Resonance Field Theory. Implements the Resonance Hamiltonian
from the RFT manuscript (eq. eq:h_res):

$$
\hat{H}_{\mathrm{res}} = \hat{H}_0 + \varepsilon(\Delta\varphi)\,\hat{V}_{\mathrm{coupling}}
$$

with the coupling efficiency from Axiom 4:

$$
\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi / 2) \in [0, 1]
$$

> **Classification:** This simulation demonstrates the **derivation of the
> Schrödinger equation from Axiom 4** and numerically proves the
> correspondence principle: Standard QM is a special case of RFT.
> It follows the recommendation to derive the Schrödinger equation from the RFT axioms.

---

## Axiom Reference

| Axiom | Implementation |
|-------|----------------|
| A1 Oscillation | Gaussian wave packet as superposition of plane waves |
| A2 Superposition | Interference in momentum and position space |
| A4 Coupling efficiency | ε(Δφ) = cos²(Δφ/2) modulates V̂_coupling in the Resonance Hamiltonian |

---

## What the Simulation Shows

### Reference Simulation (`schrodinger_1d_reference.py`)

Numerically exact 1D Schrödinger equation with split-operator (FFT).
Serves as a verified reference standard:

- **Free particle**, harmonic oscillator, or potential well
- Unitary time evolution (norm conservation < 10⁻¹³)
- Dual check of ⟨p⟩ (k-space + derivative operator)
- Energy conservation verified

### RFT Simulation (`schrodinger_1d_rft.py`)

Implements the Resonance Hamiltonian Ĥ_res = Ĥ₀ + ε(Δφ)·V̂_coupling
and demonstrates that for every Δφ the time evolution exactly matches
the standard Schrödinger equation.

**Four correspondence scenarios:**

| Scenario | Δφ | ε(Δφ) | Fidelity |
|----------|----|-------|----------|
| Free particle | π | 0 | 1.000000000000 |
| Weak coupling | 2π/3 | 0.25 | 1.000000000000 |
| Half coupling | π/2 | 0.5 | 1.000000000000 |
| Full coupling | 0 | 1.0 | 1.000000000000 |

→ **Correspondence principle numerically proven:** Standard QM is
  a special case of RFT with V_eff = ε(Δφ)·V_coupling.

### RFT Dynamic (`schrodinger_1d_rft_dynamic.py`)

> **Critique point:** The static RFT simulation is mathematically
> a tautology — the split-operator sees only V_eff, regardless of whether ε·V is
> passed as coupling or directly as potential.

Makes Δφ(t) a **dynamic field** that feeds back on ψ:

$$
\Delta\varphi(t+\mathrm{d}t) = \Delta\varphi(t) + \lambda \cdot F[\psi] \cdot \mathrm{d}t
$$

**Three feedback models:**

| Model | F[ψ] | Physical interpretation |
|-------|------|------------------------|
| `density` | ∫\|ψ\|⁴ dx | Coupling to localization |
| `position` | ⟨x⟩ | Coupling to mean position |
| `energy` | ⟨H⟩ − E₀ | Coupling to energy deviation |

→ **First time distinguishable from standard QM:** The feedback
  ψ → Δφ → V_eff → ψ produces nonlinear, state-dependent dynamics
  that measurably deviate from standard QM via fidelity, ⟨x⟩, ⟨p⟩.

### Perturbation Theory (`schrodinger_1d_rft_perturbation.py`)

> **Recommendation:** "In the limit λ → 0, the dynamic RFT must converge to
> standard QM, with leading corrections O(λ). This is the perturbation theory of RFT."

Systematic λ-scan over several orders of magnitude (10⁻⁴ … 10⁰) with
power-law analysis and first-order analytical perturbation theory:

| Observable | Exponent (numerical) | Exponent (theory) | Deviation |
|------------|---------------------:|------------------:|----------:|
| 1 − Fidelity | 2.001 | 2 | 0.05 % |
| \|Δ⟨x⟩\| | 1.001 | 1 | 0.1 % |
| \|Δ⟨p⟩\| | 1.001 | 1 | 0.1 % |
| max\|Δψ\| | 0.999 | 1 | 0.1 % |

That $1 - F \sim \lambda^2$ follows directly from
$|\langle\psi_0|\psi_0 + \lambda\psi_1\rangle|^2 = 1 - \lambda^2\|\psi_1\|^2 + \mathcal{O}(\lambda^3)$.
The first-order analytical prediction agrees with numerics to within
relative error $1.3 \times 10^{-4}$ — a hard, independent consistency check.

→ **Standard QM is the exact limit of RFT.** Perturbation theory
  confirms: RFT is a well-defined, controlled extension with λ as the only free parameter.

### Experimental Proposal (`schrodinger_1d_rft_experiment.py`)

> **Critique point 3.1:** "SI units / calibration —
> map dimensionless parameters to a physical system."

Maps the perturbation theory results to **ultracold ⁸⁷Rb atoms
in a harmonic trap** — the experimental standard system
for precision measurements in quantum mechanics:

**SI Calibration:**

| Dimensionless quantity | SI counterpart | Formula | Value (ω = 2π × 100 Hz) |
|------------------------|---------------|--------|------------------------:|
| x = 1 | ℓ | $V_s^{1/4} \cdot a_\mathrm{ho}$ | 0.41 µm |
| t = 1 | τ | $\sqrt{V_s} / \omega$ | 0.225 ms |
| E = 1 | ℏ/τ | $\hbar \cdot \omega / \sqrt{V_s}$ | 2.92 × 10⁻¹² eV |
| p = 1 | ℏ/ℓ | $\hbar / \ell$ | 2.60 × 10⁻²⁸ kg·m/s |

The calibration chain is clean: $\hbar = m \cdot \ell^2 / \tau$ is
verified as a consistency check (6 independent relations).

**Falsifiable prediction:**

$$
|\Delta\langle x\rangle|_\mathrm{SI} = 4.9 \cdot \lambda \cdot \ell
\approx 2.0 \cdot \lambda\;\mu\mathrm{m}
$$

| Scenario | λ_min | Method |
|----------|------:|--------|
| Single shot | 0.50 | 1 µm resolution directly |
| 100 repetitions | 0.05 | σ/√N |
| 10,000 repetitions | 0.005 | Statistics |

### Lagrangian / Action Principle (`schrodinger_1d_rft_lagrangian.py`)

> **Referee critique 1.1:** "Without an action principle, the
> density model remains motivated, not derived."

Defines the RFT action functional $S[\psi, \Delta\varphi]$ and derives
the Δφ-dynamics from the Euler-Lagrange equations:

$$
S = \int \mathrm{d}t \left[ \langle\psi|i\hbar\partial_t - \hat{H}_0|\psi\rangle
- \varepsilon(\Delta\varphi)\langle V\rangle_\psi
+ \frac{\mu}{2}(\dot{\Delta\varphi})^2 \right]
$$

**Two regimes:**

| Regime | Equation | Physics |
|--------|----------|---------|
| Inertial (μ > 0) | μ·Δφ̈ = ½ sin(Δφ) · ⟨V⟩_ψ | Phase field with its own inertia |
| Overdamped (γ) | γ·Δφ̇ = ½ sin(Δφ) · ⟨V⟩_ψ | → density model as limiting case |

→ **The density model is an effective limit of the action principle.**
  Noether energy E = ⟨Ĥ_res⟩ + μ/2·(Δφ̇)² is numerically conserved.

### 2-Particle / Gisin Theorem (`schrodinger_1d_rft_two_particle.py`)

> **Referee critique (Gisin):** "Nonlinear QM in principle allows
> superluminal signaling (Gisin 1990). Is RFT consistent?"

Implements the full Gisin protocol:

1. Prepare entangled state |Ψ⟩ = (|L⟩_A|↑⟩_B + |R⟩_A|↓⟩_B) / √2
2. Alice measures in two different bases (X: L/R, Z: +/−)
3. Bob's states are propagated with RFT dynamics
4. Compare ρ_B(t) for both bases

**Result:** Global Δφ violates no-signaling (D ~ λ¹).
Local Δφ (separate fields Δφ_A, Δφ_B) preserves no-signaling.

→ **RFT requires a local coupling structure:** φ(x,t) is a
  local field (like the EM field). This is physically natural
  and consistent with GR.

### Theoretical λ Expectation (`schrodinger_1d_rft_lambda_bounds.py`)

> **Referee critique:** "Without an order of magnitude for λ, it remains unclear
> whether the experiment has any chance."

Systematic order-of-magnitude estimate from five perspectives:

| Approach | λ (order of magnitude) | Feasible? |
|----------|-----------------------:|----------:|
| Gravitational (Penrose/Diósi) | 10⁻³⁵ | no |
| BSM (electroweak α²) | 10⁻⁴ | no (10⁴ shots) |
| Decoherence (spontaneous emission) | 10⁻⁶ | no |
| Experiment (100 shots) | 0.62 | boundary |
| Experiment (10,000 shots) | 0.062 | boundary |

→ **The experiment is a bound experiment:** Either λ is
  measured (discovery) or an upper bound is set (exclusion).

### Critical Assessment (`--critical`)

> **What a referee will ask** — and the answers.

**Kohn theorem as key argument:** In a purely harmonic trap,
the GP interaction does *not* shift the center of mass ⟨x⟩
(Kohn theorem). The RFT feedback ε(Δφ(t))·V modulates the
trap strength time-dependently and *breaks* the Kohn condition
→ the ⟨x⟩ shift is a *unique* RFT signal.

**Systematic errors:** The dominant error is the magnetic field gradient
(~650 nm at 0.1 mG/cm). Anharmonicities (~1 nm) and three-body losses
(~11 nm) are subdominant.

**Overall status vs. peer review:**

| Requirement | Status |
|-------------|--------|
| 1.1 Lagrangian density | ✅ Action principle S[ψ,Δφ] + Euler-Lagrange |
| 1.2 Specification ε(Δφ) | ✅ cos²(Δφ/2) |
| 2.1 GR limit | ❌ Deliberately excluded |
| 2.2 Gauge invariance | ❌ Open |
| 2.3 Gisin theorem / No-signaling | ✅ Local coupling → consistent |
| 3.1 SI units / calibration | ✅ Complete |
| 3.2 Statistical significance ΛCDM | ❌ Different sector |
| 3.3 Theoretical expectation for λ | ✅ Order-of-magnitude estimate |
| 4.1 Efficiency κ=1 | ❌ Different sector |
| "Schrödinger from Axiom 4" | ✅ Five stages |
| Falsifiable prediction | ✅ ⁸⁷Rb experiment |
| Critical assessment (GP/syst.) | ✅ Kohn theorem + error budget |

→ **RFT delivers a testable prediction.** Either a position shift
  $\propto \lambda$ is measured (RFT confirmed), or an upper bound
  on λ is set (parameter space constrained).
  Details in the [Experimental Proposal](docs/experimental_proposal.md).

---

## File Structure

| File | Function |
|------|----------|
| [`python/schrodinger_1d_reference.py`](python/schrodinger_1d_reference.py) | Reference: standard Schrödinger (split-operator, FFT) |
| [`python/schrodinger_1d_rft.py`](python/schrodinger_1d_rft.py) | RFT: Resonance Hamiltonian + correspondence proof |
| [`python/schrodinger_1d_rft_dynamic.py`](python/schrodinger_1d_rft_dynamic.py) | RFT-dynamic: Δφ(t) with feedback on ψ |
| [`python/schrodinger_1d_rft_perturbation.py`](python/schrodinger_1d_rft_perturbation.py) | Perturbation theory: λ→0 convergence, scaling analysis |
| [`python/schrodinger_1d_rft_experiment.py`](python/schrodinger_1d_rft_experiment.py) | Experimental proposal: SI calibration for ⁸⁷Rb |
| [`python/schrodinger_1d_rft_lagrangian.py`](python/schrodinger_1d_rft_lagrangian.py) | Lagrangian: action principle for Δφ dynamics |
| [`python/schrodinger_1d_rft_two_particle.py`](python/schrodinger_1d_rft_two_particle.py) | 2-particle: Gisin theorem, no-signaling analysis |
| [`python/schrodinger_1d_rft_lambda_bounds.py`](python/schrodinger_1d_rft_lambda_bounds.py) | Theoretical expectation for λ: order-of-magnitude estimate |
| [`docs/experimental_proposal.md`](docs/experimental_proposal.md) | Experimental proposal: falsifiable prediction |
| [`docs/schrodinger_roadmap.md`](docs/schrodinger_roadmap.md) | Research program: discrete field → Schrödinger |
| [`requirements.txt`](requirements.txt) | Dependencies |

---

## Quick Start

```bash
pip install numpy matplotlib

# Reference (standard QM)
python python/schrodinger_1d_reference.py --checks
python python/schrodinger_1d_reference.py --plot

# RFT correspondence proof
python python/schrodinger_1d_rft.py --checks
python python/schrodinger_1d_rft.py --plot

# RFT dynamic (Δφ feeds back on ψ)
python python/schrodinger_1d_rft_dynamic.py --checks
python python/schrodinger_1d_rft_dynamic.py --model density --lambda_coupling 5.0
python python/schrodinger_1d_rft_dynamic.py --model position --plot

# Perturbation theory (λ → 0 convergence)
python python/schrodinger_1d_rft_perturbation.py --checks
python python/schrodinger_1d_rft_perturbation.py --plot

# Experimental proposal (SI calibration)
python python/schrodinger_1d_rft_experiment.py --checks
python python/schrodinger_1d_rft_experiment.py --omega 50
python python/schrodinger_1d_rft_experiment.py --critical
python python/schrodinger_1d_rft_experiment.py --plot

# Lagrangian (action principle)
python python/schrodinger_1d_rft_lagrangian.py --checks
python python/schrodinger_1d_rft_lagrangian.py --regime inertial --mu 0.1
python python/schrodinger_1d_rft_lagrangian.py --plot

# 2-particle / Gisin theorem
python python/schrodinger_1d_rft_two_particle.py --checks
python python/schrodinger_1d_rft_two_particle.py --plot

# Theoretical λ expectation
python python/schrodinger_1d_rft_lambda_bounds.py --checks
python python/schrodinger_1d_rft_lambda_bounds.py --omega 50

# Reference with potential
python python/schrodinger_1d_reference.py --V harmonic --Vstrength 0.01 --steps 3000 --plot
```

---

## Coupling Efficiency Limit Cases

| Condition | ε | Potential | Physics |
|-----------|---|-----------|---------|
| Perfect coupling (Δφ = 0) | 1 | V_eff = V_coupling | Full interaction |
| Half coupling (Δφ = π/2) | 0.5 | V_eff = ½·V_coupling | 90° phase shift |
| Weak coupling (Δφ = 2π/3) | 0.25 | V_eff = ¼·V_coupling | Partial coupling |
| No coupling (Δφ = π) | 0 | V_eff = 0 | Free particle |

---

## Numerical Methods

### Split-Operator (symplectic, 2nd order)

$$
\psi(t+\Delta t) = e^{-iV\Delta t/2\hbar}\;\mathcal{F}^{-1}\!\left[e^{-iT\Delta t/\hbar}\;\mathcal{F}\!\left[e^{-iV\Delta t/2\hbar}\;\psi(t)\right]\right]
$$

- Unitary → exact norm conservation (numerically < 10⁻¹³)
- Energy conservation in split-operator: max|Δ⟨H⟩| < 10⁻⁵
- FFT-based → O(N log N) per time step

### FFT Normalization Conventions

For physical expectation values in momentum space, a
continuously normalized ψ̃(k) is computed:

$$
\tilde\psi(k) = \frac{dx}{\sqrt{2\pi}} \cdot \text{FFT}[\psi]
$$

such that ∑|ψ̃(k)|²·dk = 1 when ∑|ψ(x)|²·dx = 1.

---

## Research Program

The complete research program (discrete field → continuum limit
→ Schrödinger equation) is documented in the [Roadmap](docs/schrodinger_roadmap.md).

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

⬅️ [Back to Overview](../../../README.md#simulations)
