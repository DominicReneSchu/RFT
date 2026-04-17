# Experimental Proposal — Falsifiable RFT Prediction

> **Critique point 3.1 (SI units / calibration):** Map dimensionless
> simulation parameters (λ, V_strength) to SI units and formulate
> a concrete, falsifiable prediction.

---

## 1. Starting Point: Perturbation Theory Result

The perturbation analysis (`schrodinger_1d_rft_perturbation.py`) has
numerically and analytically verified the following scaling laws for
the dynamic RFT with the density feedback model
$\dot{\Delta\varphi} = \lambda \int |\psi|^4\,\mathrm{d}x$:

| Observable | Exponent (numerical) | Exponent (theory) | Deviation |
|------------|---------------------:|-------------------:|-----------:|
| $1 - F$ (Fidelity) | 2.001 | 2 | 0.05 % |
| $|\Delta\langle x\rangle|$ | 1.001 | 1 | 0.1 % |
| $|\Delta\langle p\rangle|$ | 1.001 | 1 | 0.1 % |
| $\max|\Delta\psi|$ | 0.999 | 1 | 0.1 % |

The first-order analytical prediction agrees with the numerics to within
a relative error of $1.3 \times 10^{-4}$.

**Key numerical results (prefactors):**

$$
|\Delta\langle x\rangle| \approx 4.9 \cdot \lambda, \quad
|\Delta\langle p\rangle| \approx 3.2 \cdot \lambda, \quad
1 - F \approx 138 \cdot \lambda^2
$$

That $1 - F \sim \lambda^2$ follows directly from the fact that the Fidelity

$$
|\langle\psi_0|\psi_0 + \lambda\psi_1\rangle|^2
= 1 - \lambda^2\,\|\psi_1\|^2 + \mathcal{O}(\lambda^3)
$$

The numerics confirm the perturbation theory to 4 decimal places.

---

## 2. SI Calibration

### 2.1 Physical System

**Ultracold ⁸⁷Rb atoms in a harmonic trap** — the
experimental workhorse for precision QM worldwide:

| Parameter | Symbol | Value |
|-----------|--------|-----:|
| Atomic mass | $m$ | 86.909 u = $1.443 \times 10^{-25}$ kg |
| Trap frequency | $\omega$ | $2\pi \times 100\;\mathrm{Hz}$ (tunable) |
| Planck constant | $\hbar$ | $1.055 \times 10^{-34}\;\mathrm{J\cdot s}$ |

### 2.2 Scale Mapping

The dimensionless simulation ($\hbar = m = 1$) is mapped to SI via three
conversion quantities:

| Quantity | Formula | Value ($\omega = 2\pi \times 100\;\mathrm{Hz}$) |
|-------|--------|-------:|
| Oscillator length | $a_\mathrm{ho} = \sqrt{\hbar/(m\omega)}$ | $1.08\;\mu\mathrm{m}$ |
| Length unit | $\ell = V_\mathrm{strength}^{1/4} \cdot a_\mathrm{ho}$ | $0.41\;\mu\mathrm{m}$ |
| Time unit | $\tau = \sqrt{V_\mathrm{strength}} / \omega$ | $0.225\;\mathrm{ms}$ |
| Energy unit | $E = \hbar / \tau$ | $2.92 \times 10^{-12}\;\mathrm{eV}$ |
| Momentum unit | $p = \hbar / \ell$ | $2.60 \times 10^{-28}\;\mathrm{kg\cdot m/s}$ |
| Simulation time | $T = 20\,\tau$ | $4.5\;\mathrm{ms}$ |

Consistency is verified through 6 independent relations
(e.g. $\hbar = m\,\ell^2/\tau$, $E\cdot\tau = \hbar$).

### 2.3 Derivation

The dimensionless Schrödinger equation with $\hbar = m = 1$:

$$
i\,\partial_{\tilde{t}}\,\psi = -\tfrac{1}{2}\,\partial_{\tilde{x}}^2\,\psi
+ V(\tilde{x})\,\psi
$$

is mapped to SI via $x = \ell\,\tilde{x}$, $t = \tau\,\tilde{t}$.
The harmonic coupling potential
$V(\tilde{x}) = \tfrac{1}{2}\,V_\mathrm{strength}\,\tilde{x}^2$
is identified with $V_\mathrm{phys}(x) = \tfrac{1}{2}\,m\,\omega^2\,x^2$:

$$
V_\mathrm{strength} = \frac{m^2\,\omega^2\,\ell^4}{\hbar^2}
\quad\Longrightarrow\quad
\ell = V_\mathrm{strength}^{1/4} \cdot \sqrt{\frac{\hbar}{m\,\omega}}
$$

---

## 3. Falsifiable Prediction

### 3.1 Position Shift

$$
\boxed{|\Delta\langle x\rangle|_\mathrm{SI}
= C_x \cdot \lambda \cdot \ell
\approx 2.0 \cdot \lambda\;\mu\mathrm{m}}
$$

where $C_x \approx 4.9$ is the numerically determined prefactor
and $\ell \approx 0.41\;\mu\mathrm{m}$ for $\omega = 2\pi \times 100\;\mathrm{Hz}$.

### 3.2 Prediction Table

| $\lambda$ | $|\Delta\langle x\rangle|$ [µm] | $1 - F$ | Detectable? |
|----------:|------:|-------:|:---:|
| 0.001 | 0.002 | $1.4 \times 10^{-4}$ | No (single shot) |
| 0.01 | 0.020 | 0.014 | Yes (10 000 shots) |
| 0.05 | 0.099 | 0.345 | Yes (100 shots) |
| 0.1 | 0.199 | 1.38 | Yes (100 shots) |
| 0.5 | 0.994 | 34.5 | Yes (single shot) |
| 1.0 | 1.987 | 138 | Yes (single shot) |

### 3.3 Frequency Dependence

Lower trap frequency = larger $a_\mathrm{ho}$ = better sensitivity:

| $\omega / 2\pi$ [Hz] | $a_\mathrm{ho}$ [µm] | $\ell$ [µm] | $\lambda_\mathrm{min}$ (100 shots) |
|------:|------:|------:|------:|
| 10 | 3.41 | 1.28 | 0.016 |
| 50 | 1.53 | 0.57 | 0.036 |
| 100 | 1.08 | 0.41 | 0.050 |
| 500 | 0.48 | 0.18 | 0.113 |
| 1000 | 0.34 | 0.13 | 0.159 |

**Optimal range:** $\omega \lesssim 2\pi \times 50\;\mathrm{Hz}$
(but longer preparation time).

---

## 4. Experimental Protocol

### 4.1 Preparation

1. **BEC preparation:** ⁸⁷Rb condensate in magnetic or optical trap,
   $T < 200\;\mathrm{nK}$, $N \sim 10^5$ atoms.

2. **Harmonic trap:** Tunable to $\omega = 2\pi \times (10{-}500)\;\mathrm{Hz}$.
   Axial frequency determines $a_\mathrm{ho}$ and thus sensitivity.

3. **Wave packet initialization:** Momentum kick via Bragg pulse
   or Raman transition: $\hbar k_0 = \hbar / \ell$.

### 4.2 Measurement

4. **Propagation:** Allow wave packet to propagate in the trap
   for $t \approx 4.5\;\mathrm{ms}$ (at $\omega = 2\pi \times 100\;\mathrm{Hz}$).

5. **Absorption imaging:** Switch off trap, time-of-flight,
   record absorption image. Spatial resolution: $\sim 1\;\mu\mathrm{m}$.

6. **Repetition:** $N = 100{-}10\,000$ identical runs.

### 4.3 Analysis

7. **Statistics:** Mean position $\langle x\rangle_\mathrm{exp}$
   from $N$ measurements. Standard error:
   $\sigma_{\Delta x} = \sigma_\mathrm{single} / \sqrt{N}$.

8. **Comparison with theory:**
   - **Null hypothesis** $H_0$: $\Delta\langle x\rangle = 0$ (standard QM, $\lambda = 0$)
   - **Alternative hypothesis** $H_1$: $|\Delta\langle x\rangle| = C_x \cdot \lambda \cdot \ell > 0$ (RFT)

9. **Result:**
   - $|\Delta\langle x\rangle| > 2\sigma$: RFT effect detected → $\lambda$ determined
   - $|\Delta\langle x\rangle| \leq 2\sigma$: upper bound $\lambda_\mathrm{max}$

---

## 5. Measurement Method: Absorption Imaging

### Principle

A resonant laser beam is passed through the atomic cloud.
The absorption is proportional to the column density
$n_\mathrm{col}(x, y) = \int |\psi(x, y, z)|^2\,\mathrm{d}z$.

$\langle x\rangle$ is determined from the absorption profile.

### Resolution

| Method | Spatial resolution |
|---------|-------------------:|
| Standard absorption | ~ 1 µm |
| High-resolution objective | ~ 0.3 µm |
| Fluorescence detection | ~ 0.5 µm |
| Quantum gas microscope | ~ 0.5 µm (single atom) |

For $N = 100$ repetitions: $\sigma_\mathrm{eff} = 1\;\mu\mathrm{m} / \sqrt{100} = 0.1\;\mu\mathrm{m}$.

---

## 6. Critical Assessment

### 6.1 Strengths

- **Concrete system:** ⁸⁷Rb BEC in harmonic trap — the
  experimental workhorse of dozens of labs worldwide (MIT, MPQ, JILA, …)
- **Realistic protocol:** Momentum kick + free propagation +
  absorption imaging — standard experimental physics
- **Frequency scan:** The sensitivity analysis shows that lower
  $\omega$ gives better sensitivity ($a_\mathrm{ho} \propto \omega^{-1/2}$)
- **Null and alternative hypothesis** cleanly formulated — the language
  an experimental referee expects
- **SI calibration chain** consistent: $\hbar = m \cdot \ell^2 / \tau$
  verified as consistency check (6 independent relations)

### 6.2 Questions a Referee Will Still Ask

#### Question 1: Is $\lambda = 0.05$ physically plausible?

The simulation shows that one *could* measure $\lambda$, but not
*why* $\lambda$ should have a particular value. A referee will
ask: Is there a theoretical expectation for the order of magnitude of $\lambda$?

If $\lambda < 10^{-10}$ (typical for BSM corrections), the
experiment would have no chance. **The experiment yields upper bounds**, not
a guaranteed detection.

#### Question 2: Systematic errors

The analysis assumes only statistical errors ($\sigma / \sqrt{N}$).
In real BEC experiments, systematic effects dominate:

| Error source | Estimated shift | Scaling |
|-------------|------------------------:|------------|
| GP mean-field on $\langle x\rangle$ | **0 (Kohn theorem)** | not applicable |
| Potential anharmonicities | ~ 1 nm | $\delta\omega/\omega$ |
| Magnetic field gradients (0.1 mG/cm) | ~ 650 nm | $\mu_B \cdot \nabla B$ |
| Three-body losses | ~ 11 nm | $\Delta N / N$ |
| **Total (quadrature)** | **~ 650 nm** | |

→ For $\lambda \lesssim 0.3$ magnetic field gradients dominate.
Better magnetic field compensation (< 0.01 mG/cm) would reduce the systematics
by one order of magnitude.

#### Question 3: The Gross-Pitaevskii Problem

The RFT feedback $\dot{\Delta\varphi} \propto \int |\psi|^4\,\mathrm{d}x$
has exactly the same functional form as the contact interaction term
in the Gross-Pitaevskii equation ($g|\psi|^2\psi$).

**Key answer: The Kohn Theorem**

In a *purely harmonic* trap, the Kohn theorem (also:
generalized Kohn theorem) holds: the center-of-mass motion $\langle x\rangle(t)$
is exactly harmonic at $\omega$, **independent of atom-atom interactions**.

$$
\text{GP: } \Delta\langle x\rangle = 0 \quad\text{(Kohn-protected)}
$$

The RFT feedback, however, modulates the trap strength time-dependently
via $\varepsilon(\Delta\varphi(t)) \cdot V$. This time-dependent
modulation breaks the Kohn condition and generates a
$\langle x\rangle$-shift:

$$
\text{RFT: } |\Delta\langle x\rangle| = C_x \cdot \lambda \cdot \ell \neq 0
$$

→ **The RFT effect on $\langle x\rangle$ is conceptually distinct
from the GP mean-field.** The GP term changes the *width* of the condensate,
not the *center of mass*.

Additional experimental distinguishing features:

| Protocol | GP dependence | RFT dependence |
|-----------|----------------|-------------------|
| N scan | Width $\propto N^{2/5}$ | $\langle x\rangle$-shift $\neq f(N)$ |
| $a_s$ scan (Feshbach) | $\propto a_s$ | independent of $a_s$ |
| $\omega$ scan | Width $\propto \omega^{-3/5}$ | Shift $\propto \omega^{-1/2}$ |
| $\Delta\varphi_0$ scan | independent | $\propto \varepsilon'(\Delta\varphi_0)$ |

---

## 7. Peer-Review Balance Sheet

| Requirement | Status |
|---------------------|--------|
| 1.1 Lagrangian density / action principle | ⚠️ Motivated, not derived |
| 1.2 Specification $\varepsilon(\Delta\varphi)$ | ✅ $\cos^2(\Delta\varphi/2)$, analytical, invertible |
| 2.1 GR limit | ❌ Open (deliberately excluded) |
| 2.2 Gauge invariance / U(1) | ❌ Open |
| 3.1 SI units / calibration | ✅ Complete (6 consistency relations) |
| 3.2 Statistical significance ΛCDM | ❌ Different sector |
| 4.1 Efficiency κ=1 | ❌ Different sector |
| Schrödinger from Axiom 4 | ✅ Five steps, numerically verified |
| Correspondence principle | ✅ Static + dynamic ($\lambda \to 0$) |
| Perturbation theory | ✅ Scaling exact, analytically verified |
| Falsifiable prediction | ✅ ⁸⁷Rb experiment |
| Critical assessment | ✅ GP problem (Kohn theorem), systematics |
| Gisin theorem / No-Signaling | ⚠️ 1-particle addressed, many-body open |

The work is in a state within the 1-particle QM sector that justifies
submission as a *"research program with concrete experimental
proposal"* — precisely the repositioning recommended by the reviewer.

---

## 8. Recommended Next Step

The simulation package is **complete and falsifiable** with this experimental
proposal for the 1-particle sector. The logical next items would be:

1. **Contact with experimental group:** The prediction
   $|\Delta\langle x\rangle| = 2.0 \cdot \lambda\;\mu\mathrm{m}$
   is testable with existing BEC technology. Groups such as Bloch (MPQ),
   Ketterle (MIT), or Cornell's BEC group have the necessary infrastructure.

2. **2-particle extension:** For the Gisin theorem and No-Signaling
   the simulation must be extended to entangled 2-particle states
   (next theoretical hurdle).

3. **Magnetic field compensation:** For sensitivity $\lambda < 0.1$ the
   dominant systematic error (magnetic field gradient) must be reduced through
   better compensation (< 0.01 mG/cm) or differential measurements.

---

*© Dominic-René Schu, 2025/2026 — Resonance Field Theory*

---

⬅️ [back to Schrödinger overview](../README.md)
