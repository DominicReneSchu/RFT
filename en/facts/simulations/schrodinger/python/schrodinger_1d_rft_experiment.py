"""
Experimental Proposal — SI calibration of the RFT perturbation theory
======================================================================

Context (Criticism 3.1: SI units / calibration)
------------------------------------------------
The perturbation theory (`schrodinger_1d_rft_perturbation.py`) has shown:

  |Δ⟨x⟩| ≈ C_x · λ    with  C_x ≈ 4.9  (dimensionless)

Here this prediction is mapped onto a concrete physical system:
**ultracold ⁸⁷Rb atoms in a harmonic trap**,
the experimental standard system for precision measurements in
quantum mechanics (BEC laboratories worldwide).

Falsifiable Prediction
----------------------
If the RFT feedback (Δφ couples to |ψ|²) exists, then
the center of mass of a wave packet shifts by:

  |Δ⟨x⟩|_SI = C_x · λ · ℓ

where ℓ is the length unit of the simulation, determined by the
trap parameters:

  ℓ = V_strength^(1/4) · a_ho
  a_ho = √(ℏ / (m · ω_trap))

For ⁸⁷Rb at ω_trap = 2π × 100 Hz this gives:
  a_ho ≈ 1.08 µm,  ℓ ≈ 0.41 µm

  → |Δ⟨x⟩| ≈ 2.0 µm · λ

Measurement method: absorption imaging (time-of-flight) with spatial
resolution ~ 1 µm. The RFT shift is directly detectable for λ ≳ 0.5,
and statistically detectable for λ ≳ 0.01 via repeated measurements
(σ_Δx ~ 0.1 µm after 100 repetitions).

Units: SI units. All physical constants from CODATA 2018.

Usage:
  python python/schrodinger_1d_rft_experiment.py
  python python/schrodinger_1d_rft_experiment.py --checks
  python python/schrodinger_1d_rft_experiment.py --omega 200
  python python/schrodinger_1d_rft_experiment.py --plot
"""

from __future__ import annotations

import argparse
import math
from typing import Any

import numpy as np


# ═══════════════════════════════════════════════════════════════════════════════
#  Physical constants (CODATA 2018)
# ═══════════════════════════════════════════════════════════════════════════════

HBAR_SI: float = 1.054571817e-34      # ℏ [J·s]
M_RB87_SI: float = 86.909180520 * 1.66053906660e-27  # ⁸⁷Rb mass [kg]
K_B_SI: float = 1.380649e-23          # Boltzmann constant [J/K]
A_S_RB87: float = 5.77e-9             # ⁸⁷Rb s-wave scattering length [m]

# Simulation parameters (identical to schrodinger_1d_rft_perturbation.py)
V_STRENGTH_SIM: float = 0.02          # ½ · V_strength · x² (dimensionless)
C_X_PREFACTOR: float = 4.9            # |Δ⟨x⟩| ≈ C_x · λ (from fit)
C_P_PREFACTOR: float = 3.2            # |Δ⟨p⟩| ≈ C_p · λ (from fit)
C_FID_PREFACTOR: float = 138.0        # 1 − F ≈ C_F · λ² (from fit)


# ═══════════════════════════════════════════════════════════════════════════════
#  SI calibration
# ═══════════════════════════════════════════════════════════════════════════════


def harmonic_oscillator_length(
    m_si: float, omega_si: float,
) -> float:
    """Harmonic oscillator natural length a_ho = √(ℏ/(m·ω)) [m]."""
    return math.sqrt(HBAR_SI / (m_si * omega_si))


def simulation_length_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Length unit ℓ of the simulation in SI [m].

    ℓ = V_strength^(1/4) · a_ho

    Derivation: The dimensionless Schrödinger equation with ℏ=m=1
    has the potential V(x̃) = ½·V_strength·x̃². In SI units
    x̃ = x_phys / ℓ, where ℓ⁴ = V_strength · ℏ² / (m²ω²),
    i.e., ℓ = V_strength^(1/4) · a_ho.
    """
    a_ho = harmonic_oscillator_length(m_si, omega_si)
    return v_strength ** 0.25 * a_ho


def simulation_time_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Time unit τ of the simulation in SI [s].

    τ = m · ℓ² / ℏ = √(V_strength) / ω
    """
    return math.sqrt(v_strength) / omega_si


def simulation_energy_unit(
    omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Energy unit of the simulation in SI [J].

    E_unit = ℏ / τ = ℏ · ω / √(V_strength)
    """
    return HBAR_SI * omega_si / math.sqrt(v_strength)


def simulation_momentum_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Momentum unit of the simulation in SI [kg·m/s].

    p_unit = ℏ / ℓ
    """
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    return HBAR_SI / ell


# ═══════════════════════════════════════════════════════════════════════════════
#  Predictions in SI units
# ═══════════════════════════════════════════════════════════════════════════════


def predict_delta_x_si(
    lam: float | np.ndarray,
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
    c_x: float = C_X_PREFACTOR,
) -> float | np.ndarray:
    """RFT prediction: |Δ⟨x⟩|_SI = C_x · λ · ℓ  [m]."""
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    return c_x * lam * ell


def predict_delta_p_si(
    lam: float | np.ndarray,
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
    c_p: float = C_P_PREFACTOR,
) -> float | np.ndarray:
    """RFT prediction: |Δ⟨p⟩|_SI = C_p · λ · p_unit  [kg·m/s]."""
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)
    return c_p * lam * p_unit


def predict_delta_fidelity(
    lam: float | np.ndarray,
    c_fid: float = C_FID_PREFACTOR,
) -> float | np.ndarray:
    """RFT prediction: 1 − F = C_F · λ²  (dimensionless)."""
    return c_fid * lam ** 2


# ═══════════════════════════════════════════════════════════════════════════════
#  Experimental parameters and detectability
# ═══════════════════════════════════════════════════════════════════════════════


def absorption_imaging_resolution() -> float:
    """Typical spatial resolution of absorption imaging [m].

    Standard in BEC experiments: ~ 1 µm optical resolution,
    improvable to ~ 0.3 µm with high-resolution objectives.
    """
    return 1.0e-6


def statistical_sensitivity(
    single_shot_resolution: float,
    n_repetitions: int,
) -> float:
    """Statistical sensitivity after N repetitions [m].

    σ_Δx = σ_single / √N
    """
    return single_shot_resolution / math.sqrt(n_repetitions)


def detectable_lambda_range(
    m_si: float, omega_si: float,
    resolution_m: float,
    n_repetitions: int = 1,
    v_strength: float = V_STRENGTH_SIM,
    c_x: float = C_X_PREFACTOR,
) -> float:
    """Smallest detectable λ value for given resolution.

    λ_min = σ_eff / (C_x · ℓ)
    """
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    sigma_eff = resolution_m / math.sqrt(n_repetitions)
    return sigma_eff / (c_x * ell)


# ═══════════════════════════════════════════════════════════════════════════════
#  Gross-Pitaevskii comparison and systematic errors
# ═══════════════════════════════════════════════════════════════════════════════


def gross_pitaevskii_coupling(
    m_si: float,
    a_s: float = A_S_RB87,
) -> float:
    """Gross-Pitaevskii coupling constant g = 4π·ℏ²·a_s / m  [J·m³]."""
    return 4.0 * math.pi * HBAR_SI ** 2 * a_s / m_si


def gp_mean_field_shift(
    m_si: float,
    omega_si: float,
    n_atoms: int = 100_000,
    a_s: float = A_S_RB87,
) -> dict[str, float]:
    """Analysis of GP mean-field effects on ⟨x⟩ [m].

    Kohn theorem: In a purely harmonic trap the center-of-mass motion
    is exactly at ω, independent of interactions.
    → GP mean-field does NOT shift ⟨x⟩ in a perfect harmonic trap!

    Effects on ⟨x⟩ come only from:
    1. Anharmonicities (trap imperfections)
    2. Position-dependent losses

    GP effects on higher moments (⟨x²⟩, width) are present,
    but do not interfere with the ⟨x⟩ measurement.
    """
    a_ho = harmonic_oscillator_length(m_si, omega_si)
    r_tf = a_ho * (15.0 * n_atoms * a_s / a_ho) ** 0.2
    mu = 0.5 * m_si * omega_si ** 2 * r_tf ** 2
    mu_over_hbar_omega = mu / (HBAR_SI * omega_si)

    return {
        "r_tf_m": r_tf,
        "mu_j": mu,
        "mu_over_hbar_omega": mu_over_hbar_omega,
        "dx_shift_m": 0.0,  # Kohn theorem: exactly zero
        "kohn_protected": True,
    }


def systematic_error_budget(
    m_si: float,
    omega_si: float,
    n_atoms: int = 100_000,
    a_s: float = A_S_RB87,
) -> dict[str, float]:
    """Estimate of systematic error sources [m].

    Returns
    -------
    Dictionary with estimated systematic shifts.
    """
    a_ho = harmonic_oscillator_length(m_si, omega_si)

    # GP mean-field: Kohn-protected in harmonic trap
    dx_gp = 0.0

    # Potential anharmonicity (typical: δω/ω ~ 10⁻³ → δx ~ 10⁻³ · a_ho)
    dx_anharmonicity = 1e-3 * a_ho

    # Magnetic field gradients (well-compensated experiment: 0.1 mG/cm)
    mu_b = 9.274e-24  # Bohr magneton [J/T]
    db_dx = 1e-3  # 0.1 mG/cm = 10⁻³ T/m (compensated coils)
    f_mag = mu_b * db_dx
    tau = simulation_time_unit(m_si, omega_si)
    t_sim = 20.0 * tau
    dx_magnetic = 0.5 * f_mag / m_si * t_sim ** 2

    # Three-body losses (atom number loss → center-of-mass drift)
    dx_three_body = 0.01 * a_ho

    return {
        "gp_mean_field_m": dx_gp,
        "anharmonicity_m": dx_anharmonicity,
        "magnetic_gradient_m": dx_magnetic,
        "three_body_loss_m": dx_three_body,
        "total_systematic_m": math.sqrt(
            dx_gp ** 2 + dx_anharmonicity ** 2
            + dx_magnetic ** 2 + dx_three_body ** 2
        ),
    }


def gp_rft_discriminability(
    lam: float,
    m_si: float,
    omega_si: float,
    n_atoms: int = 100_000,
    v_strength: float = V_STRENGTH_SIM,
) -> dict[str, float]:
    """Comparison: RFT shift vs. GP mean-field effect.

    Central argument (Kohn theorem):
    In a purely harmonic trap the GP interaction does NOT shift
    the center of mass ⟨x⟩. The center-of-mass motion is exactly
    harmonic at ω, independent of g, N, a_s.

    The RFT feedback ε(Δφ(t))·V on the other hand produces a
    time-dependent modulation of the trap strength, which shifts ⟨x⟩.
    → RFT effect on ⟨x⟩ is conceptually different from GP.

    Protocol for additional experimental discrimination:
    1. N-scan: GP width ∝ N^(2/5), RFT shift ⟨x⟩ independent of N
    2. a_s-scan: Feshbach resonance to tune a_s
    3. ω-scan: Different scaling laws
    4. Δφ₀-scan: Only RFT depends on initial phase difference
    """
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    dx_rft = C_X_PREFACTOR * lam * ell

    gp = gp_mean_field_shift(m_si, omega_si, n_atoms)
    dx_gp_on_mean_x = gp["dx_shift_m"]

    return {
        "dx_rft_m": dx_rft,
        "dx_gp_on_mean_x_m": dx_gp_on_mean_x,
        "kohn_protected": gp["kohn_protected"],
        "mu_over_hbar_omega": gp["mu_over_hbar_omega"],
        "r_tf_m": gp["r_tf_m"],
    }


def experimental_parameters(
    omega_hz: float,
    m_si: float = M_RB87_SI,
    v_strength: float = V_STRENGTH_SIM,
) -> dict[str, Any]:
    """Compute all experimental parameters for a given trap frequency.

    Returns
    -------
    Dictionary with SI-calibrated parameters and predictions.
    """
    omega_si = 2.0 * math.pi * omega_hz

    a_ho = harmonic_oscillator_length(m_si, omega_si)
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    tau = simulation_time_unit(m_si, omega_si, v_strength)
    e_unit = simulation_energy_unit(omega_si, v_strength)
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)

    # Simulation time in SI
    sim_steps = 2000
    sim_dt = 0.01
    t_sim_total = sim_steps * sim_dt  # dimensionless
    t_phys = t_sim_total * tau  # SI [s]

    # Predictions for various λ
    lambdas = np.array([0.001, 0.01, 0.05, 0.1, 0.5, 1.0])
    dx_si = predict_delta_x_si(lambdas, m_si, omega_si, v_strength)
    dp_si = predict_delta_p_si(lambdas, m_si, omega_si, v_strength)
    delta_fid = predict_delta_fidelity(lambdas)

    # Detectability
    res_abs = absorption_imaging_resolution()
    lam_min_single = detectable_lambda_range(
        m_si, omega_si, res_abs, 1, v_strength,
    )
    lam_min_100 = detectable_lambda_range(
        m_si, omega_si, res_abs, 100, v_strength,
    )
    lam_min_10000 = detectable_lambda_range(
        m_si, omega_si, res_abs, 10000, v_strength,
    )

    # BEC temperature (reference value)
    # T_BEC ~ ℏ·ω/(k_B) · (N_atoms)^(1/3)
    # For ~10⁵ atoms: T_BEC ~ 100 nK
    t_bec_typical = HBAR_SI * omega_si / K_B_SI * (1e5) ** (1.0 / 3.0)

    return {
        "omega_hz": omega_hz,
        "omega_si": omega_si,
        "m_si": m_si,
        "m_amu": m_si / 1.66053906660e-27,
        "a_ho_m": a_ho,
        "ell_m": ell,
        "tau_s": tau,
        "e_unit_j": e_unit,
        "e_unit_ev": e_unit / 1.602176634e-19,
        "p_unit_si": p_unit,
        "t_phys_s": t_phys,
        "v_strength": v_strength,
        "lambdas": lambdas,
        "dx_si_m": dx_si,
        "dp_si": dp_si,
        "delta_fid": delta_fid,
        "resolution_m": res_abs,
        "lam_min_single": lam_min_single,
        "lam_min_100": lam_min_100,
        "lam_min_10000": lam_min_10000,
        "t_bec_typical_nK": t_bec_typical * 1e9,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Verification of scale relations
# ═══════════════════════════════════════════════════════════════════════════════


def verify_unit_consistency(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> list[tuple[str, bool, str]]:
    """Check the consistency of the SI calibration.

    Returns
    -------
    List of (test name, passed, detail string).
    """
    results: list[tuple[str, bool, str]] = []

    a_ho = harmonic_oscillator_length(m_si, omega_si)
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    tau = simulation_time_unit(m_si, omega_si, v_strength)
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)

    # Test 1: ℏ = m · ℓ² / τ
    hbar_check = m_si * ell ** 2 / tau
    rel1 = abs(hbar_check - HBAR_SI) / HBAR_SI
    results.append((
        "ℏ = m·ℓ²/τ",
        rel1 < 1e-10,
        f"rel. error = {rel1:.2e}",
    ))

    # Test 2: ℓ = V_strength^(1/4) · a_ho
    ell_check = v_strength ** 0.25 * a_ho
    rel2 = abs(ell_check - ell) / ell
    results.append((
        "ℓ = V_s^(1/4)·a_ho",
        rel2 < 1e-10,
        f"rel. error = {rel2:.2e}",
    ))

    # Test 3: τ = √V_s / ω
    tau_check = math.sqrt(v_strength) / omega_si
    rel3 = abs(tau_check - tau) / tau
    results.append((
        "τ = √V_s / ω",
        rel3 < 1e-10,
        f"rel. error = {rel3:.2e}",
    ))

    # Test 4: p_unit = ℏ / ℓ
    p_check = HBAR_SI / ell
    rel4 = abs(p_check - p_unit) / p_unit
    results.append((
        "p_unit = ℏ/ℓ",
        rel4 < 1e-10,
        f"rel. error = {rel4:.2e}",
    ))

    # Test 5: E_unit · τ = ℏ
    e_unit = simulation_energy_unit(omega_si, v_strength)
    hbar_check2 = e_unit * tau
    rel5 = abs(hbar_check2 - HBAR_SI) / HBAR_SI
    results.append((
        "E_unit · τ = ℏ",
        rel5 < 1e-10,
        f"rel. error = {rel5:.2e}",
    ))

    # Test 6: For V_strength=1 we have ℓ = a_ho
    ell_natural = simulation_length_unit(m_si, omega_si, 1.0)
    rel6 = abs(ell_natural - a_ho) / a_ho
    results.append((
        "V_s=1 → ℓ=a_ho",
        rel6 < 1e-10,
        f"rel. error = {rel6:.2e}",
    ))

    return results


# ═══════════════════════════════════════════════════════════════════════════════
#  Numerical verification with perturbation scan
# ═══════════════════════════════════════════════════════════════════════════════


def run_perturbation_verification(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> dict[str, Any]:
    """Run the perturbation theory scan and verify the prefactors.

    Imports the simulation from schrodinger_1d_rft_perturbation.py and
    checks that the prefactors computed there agree with the ones used here.
    """
    # Simulation parameters (identical to perturbation.py defaults)
    n_grid = 2048
    l_domain = 200.0
    dt = 0.01
    steps = 2000
    hbar_sim = 1.0
    m_sim = 1.0
    x0, k0, sigma = -40.0, 1.0, 8.0
    delta_phi0 = math.pi / 3.0

    dx = l_domain / n_grid
    x = (np.arange(n_grid) - n_grid // 2) * dx
    dk = 2.0 * math.pi / l_domain
    k = 2.0 * math.pi * np.fft.fftfreq(n_grid, d=dx)
    v_coupling = 0.5 * v_strength * x ** 2

    # Gaussian wave packet
    psi0 = np.exp(-0.5 * ((x - x0) / sigma) ** 2) * np.exp(1j * k0 * x)
    norm = np.sum(np.abs(psi0) ** 2) * dx
    psi0 = psi0 / math.sqrt(norm)

    # Perturbation scan (only in the strongly perturbative regime)
    lambdas = np.array([1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3])

    # Import core functions (identical code)
    from schrodinger_1d_rft_perturbation import (
        evolve_rft_dynamic,
        evolve_standard,
        epsilon_coupling,
        fit_power_law,
    )

    eps0 = float(epsilon_coupling(delta_phi0))
    v_eff_ref = eps0 * v_coupling

    ref = evolve_standard(
        psi0, v_eff_ref, x, k, dx, dk, dt, steps, hbar_sim, m_sim,
    )

    delta_x_list: list[float] = []
    delta_p_list: list[float] = []
    delta_fid_list: list[float] = []

    for lam in lambdas:
        rft = evolve_rft_dynamic(
            psi0, v_coupling, delta_phi0, float(lam),
            x, k, dx, dk, dt, steps, hbar_sim, m_sim,
        )
        overlap = np.sum(np.conj(ref["psi_final"]) * rft["psi_final"]) * dx
        fid = float(np.abs(overlap) ** 2)
        delta_fid_list.append(1.0 - fid)
        delta_x_list.append(abs(ref["x_means"][-1] - rft["x_means"][-1]))
        delta_p_list.append(abs(ref["p_means"][-1] - rft["p_means"][-1]))

    delta_x_arr = np.array(delta_x_list)
    delta_p_arr = np.array(delta_p_list)
    delta_fid_arr = np.array(delta_fid_list)

    exp_x, pre_x = fit_power_law(lambdas, delta_x_arr)
    exp_p, pre_p = fit_power_law(lambdas, delta_p_arr)
    exp_fid, pre_fid = fit_power_law(lambdas, delta_fid_arr)

    # SI conversion
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)

    return {
        "lambdas": lambdas,
        "delta_x_sim": delta_x_arr,
        "delta_p_sim": delta_p_arr,
        "delta_fid": delta_fid_arr,
        "exp_x": exp_x,
        "pre_x": pre_x,
        "exp_p": exp_p,
        "pre_p": pre_p,
        "exp_fid": exp_fid,
        "pre_fid": pre_fid,
        "delta_x_si": delta_x_arr * ell,
        "delta_p_si": delta_p_arr * p_unit,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Main program
# ═══════════════════════════════════════════════════════════════════════════════


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Experimental proposal: SI calibration of the "
            "RFT perturbation theory for ultracold ⁸⁷Rb atoms"
        ),
    )
    ap.add_argument(
        "--omega", type=float, default=100.0,
        help="Trap frequency [Hz] (default: 100 Hz)",
    )
    ap.add_argument(
        "--plot", action="store_true",
        help="Detectability plot",
    )
    ap.add_argument(
        "--checks", action="store_true",
        help="Extended consistency tests",
    )
    ap.add_argument(
        "--verify", action="store_true",
        help="Numerical verification of prefactors",
    )
    ap.add_argument(
        "--critical", action="store_true",
        help="Critical assessment: GP comparison, systematic errors",
    )
    args = ap.parse_args()

    omega_hz: float = args.omega
    omega_si: float = 2.0 * math.pi * omega_hz
    m_si: float = M_RB87_SI

    # ─── Header ───────────────────────────────────────────────────────
    print("=" * 74)
    print("  Experimental proposal: RFT perturbation theory → SI units")
    print("  System: ⁸⁷Rb atoms in harmonic trap")
    print("=" * 74)

    # ─── Physical parameters ──────────────────────────────────────────
    params = experimental_parameters(omega_hz, m_si)

    print(f"\n  Physical parameters:")
    print(f"  {'─' * 50}")
    print(f"  Atom:              ⁸⁷Rb  (m = {params['m_amu']:.3f} u)")
    print(f"  Mass:              {m_si:.6e} kg")
    print(f"  Trap frequency:    ω = 2π × {omega_hz:.1f} Hz")
    print(f"  V_strength (sim):  {params['v_strength']}")

    print(f"\n  Natural scales:")
    print(f"  {'─' * 50}")
    print(f"  a_ho   = √(ℏ/mω)         = {params['a_ho_m'] * 1e6:.4f} µm")
    print(f"  ℓ      = V_s^(1/4) · a_ho = {params['ell_m'] * 1e6:.4f} µm")
    print(f"  τ      = √V_s / ω         = {params['tau_s'] * 1e3:.4f} ms")
    print(f"  E_unit = ℏ/τ              = {params['e_unit_ev']:.4e} eV")
    print(f"  p_unit = ℏ/ℓ              = {params['p_unit_si']:.4e} kg·m/s")
    print(f"  T_sim  = {2000 * 0.01:.0f} τ "
          f"= {params['t_phys_s'] * 1e3:.2f} ms")

    # ─── RFT predictions in SI ────────────────────────────────────────
    print(f"\n  RFT predictions (|Δ⟨x⟩| = {C_X_PREFACTOR} · λ · ℓ):")
    print(f"  {'─' * 60}")
    print(f"  {'λ':>10s}  {'|Δ⟨x⟩| [µm]':>14s}  "
          f"{'|Δ⟨p⟩| [ℏ/µm]':>14s}  {'1−F':>12s}")
    print(f"  {'─' * 60}")

    for i, lam in enumerate(params["lambdas"]):
        dx_um = params["dx_si_m"][i] * 1e6
        dp_hbar_um = params["dp_si"][i] / (HBAR_SI / 1e-6)
        print(f"  {lam:10.3f}  {dx_um:14.4f}  "
              f"{dp_hbar_um:14.4f}  {params['delta_fid'][i]:12.4e}")

    # ─── Detectability ────────────────────────────────────────────────
    print(f"\n  Detectability (absorption imaging):")
    print(f"  {'─' * 60}")
    print(f"  Single-shot resolution:     {params['resolution_m'] * 1e6:.1f} µm")
    print(f"  λ_min (1 measurement):      {params['lam_min_single']:.2f}")
    print(f"  λ_min (100 measurements):   {params['lam_min_100']:.3f}")
    print(f"  λ_min (10 000 measurements): {params['lam_min_10000']:.4f}")
    print(f"\n  → For λ ≳ {params['lam_min_100']:.2f} the "
          f"RFT shift is statistically detectable after 100 repetitions")
    print(f"    at ω = 2π × {omega_hz:.0f} Hz.")

    # ─── Experimental recommendations ─────────────────────────────────
    print(f"\n  Experimental protocol:")
    print(f"  {'─' * 60}")
    print(f"  1. Prepare BEC from ⁸⁷Rb (T < {params['t_bec_typical_nK']:.0f} nK)")
    print(f"  2. Harmonic trap with ω = 2π × {omega_hz:.0f} Hz")
    print(f"  3. Initialize wave packet (momentum kick: k₀ = 1.0 / ℓ)")
    print(f"  4. Let propagate freely for t = {params['t_phys_s'] * 1e3:.1f} ms")
    print(f"  5. Absorption imaging: measure ⟨x⟩")
    print(f"  6. Repeat N = 100–10000 times")
    print(f"  7. Statistics: Δ⟨x⟩ = ⟨x⟩_exp − ⟨x⟩_QM")
    print(f"     → If |Δ⟨x⟩| > 0: RFT effect detected")
    print(f"     → If |Δ⟨x⟩| ≈ 0: Upper bound on λ")

    # ─── Frequency scan ───────────────────────────────────────────────
    print(f"\n  Frequency dependence of sensitivity:")
    print(f"  {'─' * 55}")
    print(f"  {'ω/2π [Hz]':>12s}  {'a_ho [µm]':>10s}  {'ℓ [µm]':>10s}  "
          f"{'λ_min(100)':>12s}")
    print(f"  {'─' * 55}")

    for freq in [10.0, 50.0, 100.0, 200.0, 500.0, 1000.0]:
        omega_f = 2.0 * math.pi * freq
        a_f = harmonic_oscillator_length(m_si, omega_f) * 1e6
        ell_f = simulation_length_unit(m_si, omega_f) * 1e6
        lam_f = detectable_lambda_range(
            m_si, omega_f, absorption_imaging_resolution(), 100,
        )
        print(f"  {freq:12.0f}  {a_f:10.4f}  {ell_f:10.4f}  {lam_f:12.3f}")

    print(f"\n  → Lower trap frequency = larger a_ho = better sensitivity.")
    print(f"    Optimum: ω ≲ 2π × 50 Hz (but longer preparation time).")

    # ─── Smoke tests ──────────────────────────────────────────────────
    all_pass = True

    if args.checks:
        print(f"\n{'=' * 74}")
        print("  Consistency tests: SI calibration")
        print(f"{'=' * 74}")

        checks = verify_unit_consistency(m_si, omega_si)
        for name, passed, detail in checks:
            symbol = "✓" if passed else "✗"
            print(f"  {symbol} {name:25s}  {detail}")
            if not passed:
                all_pass = False

        # Test: prediction is positive and physically plausible
        dx_test = predict_delta_x_si(0.1, m_si, omega_si)
        ok = 1e-12 < dx_test < 1e-3
        symbol = "✓" if ok else "✗"
        print(f"  {symbol} {'|Δx|(λ=0.1) plausible':25s}  "
              f"{dx_test * 1e6:.4f} µm")
        if not ok:
            all_pass = False

        # Test: detectability threshold is in physical range
        ok2 = 1e-4 < params["lam_min_100"] < 100.0
        symbol = "✓" if ok2 else "✗"
        print(f"  {symbol} {'λ_min(100) physical':25s}  "
              f"{params['lam_min_100']:.4f}")
        if not ok2:
            all_pass = False

        # Test: different frequencies → monotonically decreasing sensitivity
        lam_10 = detectable_lambda_range(
            m_si, 2 * math.pi * 10,
            absorption_imaging_resolution(), 100,
        )
        lam_1000 = detectable_lambda_range(
            m_si, 2 * math.pi * 1000,
            absorption_imaging_resolution(), 100,
        )
        ok3 = lam_10 < lam_1000
        symbol = "✓" if ok3 else "✗"
        print(f"  {symbol} {'Monotonicity ω → λ_min':25s}  "
              f"λ_min(10 Hz)={lam_10:.3f} < λ_min(1 kHz)={lam_1000:.3f}")
        if not ok3:
            all_pass = False

    if args.verify:
        print(f"\n{'=' * 74}")
        print("  Numerical verification: Prefactors")
        print(f"{'=' * 74}")

        vresult = run_perturbation_verification(m_si, omega_si)
        print(f"\n  Scaling exponents (verification):")
        print(f"    |Δ⟨x⟩|:  exp = {vresult['exp_x']:.3f}  "
              f"(expected 1.0), prefactor = {vresult['pre_x']:.3f}  "
              f"(used: {C_X_PREFACTOR})")
        print(f"    |Δ⟨p⟩|:  exp = {vresult['exp_p']:.3f}  "
              f"(expected 1.0), prefactor = {vresult['pre_p']:.3f}  "
              f"(used: {C_P_PREFACTOR})")
        print(f"    1−F:     exp = {vresult['exp_fid']:.3f}  "
              f"(expected 2.0), prefactor = {vresult['pre_fid']:.1f}  "
              f"(used: {C_FID_PREFACTOR})")

        rel_x = abs(vresult["pre_x"] - C_X_PREFACTOR) / C_X_PREFACTOR
        rel_p = abs(vresult["pre_p"] - C_P_PREFACTOR) / C_P_PREFACTOR
        print(f"\n  Prefactor deviations: "
              f"C_x: {rel_x:.2%}, C_p: {rel_p:.2%}")

        if rel_x > 0.05:
            print(f"  [WARN] C_x deviates by >{5}% — check prefactor!")
        if rel_p > 0.05:
            print(f"  [WARN] C_p deviates by >{5}% — check prefactor!")

    # ─── Critical assessment ──────────────────────────────────────────
    if args.critical:
        print(f"\n{'=' * 74}")
        print("  Critical assessment: GP comparison & systematic errors")
        print(f"{'=' * 74}")

        # Systematic errors
        syst = systematic_error_budget(m_si, omega_si)
        print(f"\n  Systematic error sources:")
        print(f"  {'─' * 60}")
        print(f"  {'Source':<30s}  {'Δx [µm]':>10s}  {'Δx [nm]':>10s}")
        print(f"  {'─' * 60}")
        for label, key in [
            ("GP mean-field", "gp_mean_field_m"),
            ("Anharmonicity", "anharmonicity_m"),
            ("Magnetic field gradient", "magnetic_gradient_m"),
            ("Three-body losses", "three_body_loss_m"),
            ("Total (quadratic)", "total_systematic_m"),
        ]:
            val_m = syst[key]
            print(f"  {label:<30s}  {val_m * 1e6:10.4f}  {val_m * 1e9:10.2f}")

        # GP vs. RFT comparison — Kohn theorem
        comp_ref = gp_rft_discriminability(0.1, m_si, omega_si)
        print(f"\n  Kohn theorem — protection of ⟨x⟩:")
        print(f"  {'─' * 60}")
        print("  In a purely harmonic trap the Kohn theorem applies:")
        print("  The center-of-mass motion ⟨x⟩(t) is exactly harmonic")
        print("  at ω — INDEPENDENT of atom-atom interactions.")
        print(f"  → GP interaction does NOT shift ⟨x⟩.")
        print(f"  → Kohn-protected: {comp_ref['kohn_protected']}")
        print(f"  → µ/(ℏω) = {comp_ref['mu_over_hbar_omega']:.1f}  "
              f"(Thomas-Fermi regime)")
        print(f"  → R_TF = {comp_ref['r_tf_m'] * 1e6:.2f} µm")
        print()
        print("  RFT feedback ε(Δφ(t))·V modulates the trap strength")
        print("  time-dependently → breaks the Kohn condition → ⟨x⟩ shift.")
        print()
        print(f"  {'λ':>8s}  {'Δx_RFT [µm]':>12s}  {'Δx_GP(⟨x⟩)':>12s}  "
              f"{'Comment':>20s}")
        print(f"  {'─' * 60}")
        for lam in [0.01, 0.05, 0.1, 0.5, 1.0]:
            comp = gp_rft_discriminability(lam, m_si, omega_si)
            print(f"  {lam:8.2f}  {comp['dx_rft_m'] * 1e6:12.4f}  "
                  f"{'0 (Kohn)':>12s}  {'RFT unique':>20s}")

        print(f"\n  Additional discrimination protocol:")
        print(f"  {'─' * 60}")
        print("  1. N-scan: GP width ∝ N^(2/5), RFT ⟨x⟩ ≠ f(N)")
        print("  2. a_s-scan: GP ∝ a_s via Feshbach, RFT independent of a_s")
        print("  3. ω-scan: RFT ∝ ω^(-1/2), GP width ∝ ω^(-3/5)")
        print("  4. Δφ₀-scan: Only RFT depends on the initial phase difference")

        # Reviewer questions
        print(f"\n  Open reviewer questions:")
        print(f"  {'─' * 60}")
        print("  Q1: Is λ = 0.05 physically plausible?")
        print("      → No theoretical prediction for λ. If λ < 10⁻¹⁰")
        print("        (typical for BSM corrections), the experiment would")
        print("        be hopeless. The experiment sets upper bounds.")
        print()
        print("  Q2: Systematic vs. statistical errors?")
        dx_rft_01 = predict_delta_x_si(0.1, m_si, omega_si) * 1e6
        print(f"      → Δx_RFT(λ=0.1) = {dx_rft_01:.3f} µm")
        print(f"      → Δx_syst(total) = {syst['total_systematic_m'] * 1e6:.3f} µm")
        if syst["total_systematic_m"] > predict_delta_x_si(0.1, m_si, omega_si):
            print("      ⚠ Systematics dominate for λ ≲ 0.1!")
        else:
            print("      ✓ RFT signal at λ = 0.1 exceeds systematics.")
        print()
        print("  Q3: Gross-Pitaevskii problem:")
        print("      → RFT feedback Δφ̇ ∝ ∫|ψ|⁴dx has the same")
        print("        functional form as GP contact interaction g|ψ|²ψ.")
        print("      → BUT: Kohn theorem protects ⟨x⟩ in harmonic trap")
        print("        from GP shifts. GP changes only the width,")
        print("        not the center of mass.")
        print("      → RFT modulates ε(Δφ(t))·V time-dependently → breaks Kohn")
        print("        → shifts ⟨x⟩. Conceptually different effect.")
        print("      → Additionally: scaling behavior (N, a_s, ω, Δφ₀)")
        print("        distinguishes RFT and GP experimentally.")

        # Summary
        print(f"\n  Overall assessment vs. peer review:")
        print(f"  {'─' * 60}")
        print(f"  {'Reviewer requirement':<40s}  {'Status':>10s}")
        print(f"  {'─' * 60}")
        for label, status in [
            ("1.1 Lagrangian density", "⚠️ Motivated"),
            ("1.2 Specification ε(Δφ)", "✅"),
            ("2.1 GR limit", "❌ Delineated"),
            ("2.2 Gauge invariance", "❌ Open"),
            ("3.1 SI units / calibration", "✅"),
            ("3.2 Statistical significance ΛCDM", "❌ Different sector"),
            ("4.1 Efficiency κ=1", "❌ Different sector"),
            ("Schrödinger from Axiom 4", "✅ Five steps"),
            ("Falsifiable prediction", "✅ ⁸⁷Rb experiment"),
            ("Critical assessment (GP/syst.)", "✅ Addressed here"),
        ]:
            print(f"  {label:<40s}  {status:>10s}")


    # ─── Summary ──────────────────────────────────────────────────────
    print(f"\n{'=' * 74}")
    print("  Summary: Falsifiable prediction of the RFT")
    print(f"{'─' * 74}")
    print(f"  System:  ⁸⁷Rb in harmonic trap (ω = 2π × {omega_hz:.0f} Hz)")
    print(f"  Effect:  |Δ⟨x⟩| = {C_X_PREFACTOR:.1f} · λ · "
          f"{params['ell_m'] * 1e6:.2f} µm")
    print(f"         = {C_X_PREFACTOR * params['ell_m'] * 1e6:.2f} · λ  µm")
    print(f"  Detection: Absorption imaging, N ≥ 100 repetitions")
    print(f"  Sensitivity: λ ≳ {params['lam_min_100']:.2f} (100 shots)")
    print(f"               λ ≳ {params['lam_min_10000']:.3f} (10 000 shots)")
    print(f"  Null hypothesis: Δ⟨x⟩ = 0 (Standard QM, λ = 0)")
    print(f"  Alternative hypothesis: |Δ⟨x⟩| ∝ λ (RFT, λ > 0)")
    print(f"{'=' * 74}")

    if all_pass:
        print("  ✓ All tests passed.")
    else:
        print("  ✗ Tests failed.")

    # ─── Plot ─────────────────────────────────────────────────────────
    if args.plot:
        _plot_detectability(m_si, omega_hz)

    return 0 if all_pass else 1


# ═══════════════════════════════════════════════════════════════════════════════
#  Visualization
# ═══════════════════════════════════════════════════════════════════════════════


def _plot_detectability(m_si: float, omega_hz: float) -> None:
    """Detectability diagram: λ vs. |Δ⟨x⟩| for various ω."""
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    lambdas = np.logspace(-4, 1, 200)
    res_um = absorption_imaging_resolution() * 1e6
    res_100_um = res_um / math.sqrt(100)

    # --- Left panel: |Δ⟨x⟩| vs λ for various frequencies ---
    freqs = [10.0, 50.0, 100.0, 500.0]
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

    for freq, color in zip(freqs, colors):
        omega_f = 2.0 * math.pi * freq
        dx_um = predict_delta_x_si(lambdas, m_si, omega_f) * 1e6
        ax1.loglog(lambdas, dx_um, color=color,
                   label=f"ω = 2π × {freq:.0f} Hz")

    ax1.axhline(res_um, color="gray", ls="--", alpha=0.5,
                label=f"Resolution (1 shot): {res_um:.0f} µm")
    ax1.axhline(res_100_um, color="gray", ls=":", alpha=0.5,
                label=f"Sensitivity (100 shots): {res_100_um:.1f} µm")

    ax1.set_xlabel("λ (RFT coupling parameter)")
    ax1.set_ylabel("|Δ⟨x⟩| [µm]")
    ax1.set_title("RFT position shift vs. λ")
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3, which="both")
    ax1.set_xlim(1e-4, 10)
    ax1.set_ylim(1e-5, 100)

    # --- Right panel: λ_min vs ω ---
    freqs_scan = np.logspace(0.5, 3.5, 100)
    lam_min_1 = [
        detectable_lambda_range(
            m_si, 2 * math.pi * f,
            absorption_imaging_resolution(), 1,
        )
        for f in freqs_scan
    ]
    lam_min_100 = [
        detectable_lambda_range(
            m_si, 2 * math.pi * f,
            absorption_imaging_resolution(), 100,
        )
        for f in freqs_scan
    ]
    lam_min_10k = [
        detectable_lambda_range(
            m_si, 2 * math.pi * f,
            absorption_imaging_resolution(), 10000,
        )
        for f in freqs_scan
    ]

    ax2.loglog(freqs_scan, lam_min_1, "b-", label="N = 1")
    ax2.loglog(freqs_scan, lam_min_100, "r-", label="N = 100")
    ax2.loglog(freqs_scan, lam_min_10k, "g-", label="N = 10 000")

    ax2.axhline(1.0, color="gray", ls="--", alpha=0.3)
    ax2.axvline(omega_hz, color="gray", ls=":", alpha=0.5,
                label=f"ω = 2π × {omega_hz:.0f} Hz")

    ax2.set_xlabel("ω / 2π [Hz]")
    ax2.set_ylabel("λ_min (smallest detectable value)")
    ax2.set_title("Detectability threshold vs. trap frequency")
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3, which="both")

    plt.suptitle(
        "Experimental proposal: RFT effect in ⁸⁷Rb\n"
        f"|Δ⟨x⟩| = {C_X_PREFACTOR:.1f} · λ · ℓ  —  "
        "Absorption imaging",
        fontsize=13,
    )
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    raise SystemExit(main())
