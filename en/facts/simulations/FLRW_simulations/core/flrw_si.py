"""
RT-04: FLRW solver in SI units with astropy comparison.

Implements the Friedmann equations in physical SI units and validates
the RFT solver against astropy.cosmology.FlatLambdaCDM.

Physical context:
    - Standard Friedmann equation: H² = (8πG/3) · ρ_total
    - Matter: ρ_m ∝ a⁻³, radiation: ρ_r ∝ a⁻⁴, Λ: ρ_Λ = const
    - RFT extension: H_rft(t) = H_lcdm(t) · (1 + d_eta · ε(Δφ(t)))
      with ε(Δφ) = cos²(Δφ/2)

Planck-2018 default values (arXiv:1807.06209):
    H0 = 67.36 km/s/Mpc, Ω_m = 0.3153, Ω_r = 9.14e-5, Ω_Λ = 0.6847

Falsification criterion (RT-04):
    Maximum deviation |a_rft − a_astropy| / a_astropy < 1 %
    over t = 0.1..13.8 Gyr.

Dependencies: numpy, scipy, astropy
"""

import numpy as np
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------------------
# Physical constants (SI)
# ---------------------------------------------------------------------------
_G_SI = 6.674e-11           # m³ kg⁻¹ s⁻²
_MPC_TO_M = 3.085677581e22  # 1 Mpc in metres
_GYR_TO_S = 3.15576e16      # 1 Gyr in seconds
_KM_PER_MPC_TO_SI = 1e3 / _MPC_TO_M  # (km/s/Mpc) → s⁻¹

# ---------------------------------------------------------------------------
# Planck-2018 default values
# ---------------------------------------------------------------------------
H0_PLANCK = 67.36           # km/s/Mpc
OMEGA_M = 0.3153            # Matter (baryon + CDM)
OMEGA_R = 9.14e-5           # Radiation
OMEGA_LAMBDA = 0.6847       # Cosmological constant
OMEGA_B_H2 = 0.02237        # Baryon density × h²
OMEGA_C_H2 = 0.1200         # CDM density × h²
TAU = 0.0544                # Optical depth


def _h_lcdm(a, H0_si, Omega_m, Omega_r, Omega_Lambda):
    """Hubble parameter H(a) for flat ΛCDM (s⁻¹).

    H²(a) = H₀² · [Ω_m/a³ + Ω_r/a⁴ + Ω_Λ]
    Flatness is assumed: Ω_k = 0.
    """
    return H0_si * np.sqrt(Omega_m / a**3 + Omega_r / a**4 + Omega_Lambda)


def _da_dt(t, a, H0_si, Omega_m, Omega_r, Omega_Lambda):
    """Right-hand side da/dt = a · H(a) for the ODE solver."""
    a_val = a[0]
    if a_val <= 0:
        return [0.0]
    H = _h_lcdm(a_val, H0_si, Omega_m, Omega_r, Omega_Lambda)
    return [a_val * H]


def flrw_si_sim(
    H0=H0_PLANCK,
    Omega_m=OMEGA_M,
    Omega_r=OMEGA_R,
    Omega_Lambda=OMEGA_LAMBDA,
    t_span_Gyr=(0.001, 13.8),
    n_eval=1000,
    d_eta=0.0,
    delta_phi_func=None,
):
    """Solves the Friedmann equation in SI units.

    Parameters
    ----------
    H0 : float
        Hubble constant in km/s/Mpc (default: Planck-2018).
    Omega_m, Omega_r, Omega_Lambda : float
        Density parameters (dimensionless, sum ≈ 1 for flat universe).
    t_span_Gyr : tuple
        Integration interval in Gyr, e.g. (0.001, 13.8).
    n_eval : int
        Number of evaluation points.
    d_eta : float
        RFT correction parameter. d_eta = 0 → pure ΛCDM.
    delta_phi_func : callable or None
        Function Δφ(t_Gyr) for RFT correction. If None and d_eta != 0,
        Δφ = const = π/4 is used (approximation).

    Returns
    -------
    dict with:
        t_Gyr         : array, time in Gyr
        a_lcdm        : array, scale factor (ΛCDM)
        a_rft         : array, scale factor (ΛCDM + η correction)
        H_lcdm_si     : array, Hubble parameter in s⁻¹
        H_lcdm_kmsMpc : array, Hubble parameter in km/s/Mpc
        H_rft_kmsMpc  : array, RFT-corrected Hubble in km/s/Mpc
        H0_si         : float, H₀ in s⁻¹
    """
    H0_si = H0 * _KM_PER_MPC_TO_SI  # s⁻¹

    t_start_s = t_span_Gyr[0] * _GYR_TO_S
    t_end_s = t_span_Gyr[1] * _GYR_TO_S

    # Initial condition: radiation-dominated approximation
    a_start = H0_si * t_start_s * np.sqrt(Omega_r) * 0.5
    a_start = max(a_start, 1e-8)

    t_eval_s = np.linspace(t_start_s, t_end_s, n_eval)

    sol = solve_ivp(
        _da_dt,
        (t_start_s, t_end_s),
        [a_start],
        t_eval=t_eval_s,
        args=(H0_si, Omega_m, Omega_r, Omega_Lambda),
        method="DOP853",
        rtol=1e-10,
        atol=1e-12,
        dense_output=True,
    )

    a_raw = sol.y[0]
    t_Gyr = sol.t / _GYR_TO_S

    # Normalise: a(t_today) = 1 at t = 13.8 Gyr
    t_today_s = 13.8 * _GYR_TO_S
    if t_today_s <= t_end_s:
        a_today = float(sol.sol(t_today_s)[0])
    else:
        a_today = a_raw[-1]

    a_lcdm = a_raw / a_today

    # ΛCDM Hubble parameter
    H_lcdm_si = np.array([
        _h_lcdm(a, H0_si, Omega_m, Omega_r, Omega_Lambda)
        for a in np.where(a_lcdm > 0, a_lcdm, 1e-10)
    ])
    H_lcdm_kmsMpc = H_lcdm_si / _KM_PER_MPC_TO_SI

    # RFT correction: H_rft = H_lcdm · (1 + d_eta · cos²(Δφ/2))
    if delta_phi_func is not None:
        delta_phi = np.array([delta_phi_func(t) for t in t_Gyr])
    else:
        delta_phi = np.full_like(t_Gyr, np.pi / 4)

    eps_dphi = np.cos(delta_phi / 2) ** 2
    H_rft_kmsMpc = H_lcdm_kmsMpc * (1.0 + d_eta * eps_dphi)

    # RFT scale factor via cumulative integration of H_rft
    dt_s = np.diff(sol.t, prepend=sol.t[0])
    H_rft_si = H_rft_kmsMpc * _KM_PER_MPC_TO_SI
    integral_H_rft = np.cumsum(H_rft_si * dt_s)
    integral_H_lcdm = np.cumsum(H_lcdm_si * dt_s)

    a_rft = a_lcdm[0] * np.exp(integral_H_rft - integral_H_lcdm[0])
    if t_today_s <= t_end_s:
        idx_today = np.argmin(np.abs(sol.t - t_today_s))
        a_rft = a_rft / a_rft[idx_today]
    else:
        a_rft = a_rft / a_rft[-1]

    return {
        "t_Gyr": t_Gyr,
        "a_lcdm": a_lcdm,
        "a_rft": a_rft,
        "H_lcdm_si": H_lcdm_si,
        "H_lcdm_kmsMpc": H_lcdm_kmsMpc,
        "H_rft_kmsMpc": H_rft_kmsMpc,
        "H0_si": H0_si,
        "H0_kmsMpc": H0,
    }


def compare_to_astropy(
    H0=H0_PLANCK,
    Omega_m=OMEGA_M,
    Omega_Lambda=OMEGA_LAMBDA,
    t_span_Gyr=(0.1, 13.8),
    n_eval=500,
    d_eta=0.0,
):
    """Compares the RFT solver against astropy.cosmology.FlatLambdaCDM.

    Parameters
    ----------
    H0 : float
        Hubble constant in km/s/Mpc.
    Omega_m : float
        Matter density parameter.
    Omega_Lambda : float
        Λ density parameter.
    t_span_Gyr : tuple
        Comparison time range in Gyr.
    n_eval : int
        Number of comparison points.
    d_eta : float
        RFT correction parameter.

    Returns
    -------
    dict with:
        t_Gyr       : array
        a_rft       : array, RFT scale factor
        a_astropy   : array, astropy reference
        rel_err     : array, |a_rft − a_astropy| / a_astropy
        max_rel_err : float, maximum relative deviation
        passes_1pct : bool, whether criterion < 1% is met
    """
    try:
        from astropy.cosmology import FlatLambdaCDM
        import astropy.units as u
    except ImportError as exc:
        raise ImportError(
            "RT-04 requires astropy:\n"
            "  pip install astropy\n"
        ) from exc

    Omega_r = OMEGA_R
    sim = flrw_si_sim(
        H0=H0,
        Omega_m=Omega_m,
        Omega_r=Omega_r,
        Omega_Lambda=Omega_Lambda,
        t_span_Gyr=t_span_Gyr,
        n_eval=n_eval,
        d_eta=d_eta,
    )

    t_Gyr = sim["t_Gyr"]
    a_rft = sim["a_rft"]

    cosmo = FlatLambdaCDM(H0=H0, Om0=Omega_m, Ob0=OMEGA_B_H2 / (H0 / 100) ** 2)

    from scipy.interpolate import interp1d
    z_test = np.logspace(-3, 4, 5000)
    age_test = cosmo.age(z_test).to(u.Gyr).value
    mask_valid = np.diff(age_test) < 0
    age_valid = age_test[1:][mask_valid]
    z_valid = z_test[1:][mask_valid]

    if len(age_valid) > 1:
        z_of_t = interp1d(
            age_valid[::-1], z_valid[::-1],
            kind="linear", bounds_error=False, fill_value=(z_valid[-1], z_valid[0])
        )
        z_at_t = z_of_t(t_Gyr)
        a_astropy = 1.0 / (1.0 + np.where(z_at_t > 0, z_at_t, 0.0))
        a_astropy = np.clip(a_astropy, 1e-6, 1.0)
    else:
        t_0 = cosmo.age(0).to(u.Gyr).value
        a_astropy = (t_Gyr / t_0) ** (2.0 / 3.0)

    with np.errstate(invalid="ignore", divide="ignore"):
        rel_err = np.where(
            a_astropy > 0,
            np.abs(a_rft - a_astropy) / a_astropy,
            np.nan,
        )

    mask_finite = np.isfinite(rel_err)
    max_rel_err = float(np.max(rel_err[mask_finite])) if np.any(mask_finite) else np.nan

    return {
        "t_Gyr": t_Gyr,
        "a_rft": a_rft,
        "a_lcdm": sim["a_lcdm"],
        "a_astropy": a_astropy,
        "H_lcdm_kmsMpc": sim["H_lcdm_kmsMpc"],
        "H_rft_kmsMpc": sim["H_rft_kmsMpc"],
        "rel_err": rel_err,
        "max_rel_err": max_rel_err,
        "passes_1pct": max_rel_err < 0.01,
    }
