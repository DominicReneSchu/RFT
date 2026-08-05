"""
RT-04: FLRW-Solver in SI-Einheiten mit astropy-Vergleich.

Implementiert die Friedmann-Gleichungen in physikalischen SI-Einheiten
und validiert den RFT-Solver gegen astropy.cosmology.FlatLambdaCDM.

Physikalischer Kontext:
    - Standard-Friedmann-Gleichung: H² = (8πG/3) · ρ_total
    - Materie: ρ_m ∝ a⁻³, Strahlung: ρ_r ∝ a⁻⁴, Λ: ρ_Λ = const
    - RFT-Erweiterung: H_rft(t) = H_lcdm(t) · (1 + d_eta · ε(Δφ(t)))
      mit ε(Δφ) = cos²(Δφ/2)

Planck-2018-Standardwerte (arXiv:1807.06209):
    H0 = 67.36 km/s/Mpc, Ω_m = 0.3153, Ω_r = 9.14e-5, Ω_Λ = 0.6847

Falsifizierungskriterium (RT-04):
    Maximale Abweichung |a_rft − a_astropy| / a_astropy < 1 %
    über t = 0.1..13.8 Gyr.

Abhängigkeiten: numpy, scipy, astropy
"""

import numpy as np
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------------------
# Physikalische Konstanten (SI)
# ---------------------------------------------------------------------------
_G_SI = 6.674e-11          # m³ kg⁻¹ s⁻²
_MPC_TO_M = 3.085677581e22  # 1 Mpc in Metern
_GYR_TO_S = 3.15576e16      # 1 Gyr in Sekunden
_KM_PER_MPC_TO_SI = 1e3 / _MPC_TO_M  # (km/s/Mpc) → s⁻¹

# ---------------------------------------------------------------------------
# Planck-2018-Standardwerte
# ---------------------------------------------------------------------------
H0_PLANCK = 67.36           # km/s/Mpc
OMEGA_M = 0.3153            # Materie (baryon + CDM)
OMEGA_R = 9.14e-5           # Strahlung
OMEGA_LAMBDA = 0.6847       # Kosmologische Konstante
OMEGA_B_H2 = 0.02237        # Baryonische Dichte × h²
OMEGA_C_H2 = 0.1200         # CDM-Dichte × h²
TAU = 0.0544                # Optische Tiefe


def _h_lcdm(a, H0_si, Omega_m, Omega_r, Omega_Lambda):
    """Hubble-Parameter H(a) für flaches ΛCDM (s⁻¹).

    H²(a) = H₀² · [Ω_m/a³ + Ω_r/a⁴ + Ω_Λ]
    Flachheit wird vorausgesetzt: Ω_k = 0.
    """
    return H0_si * np.sqrt(Omega_m / a**3 + Omega_r / a**4 + Omega_Lambda)


def _da_dt(t, a, H0_si, Omega_m, Omega_r, Omega_Lambda):
    """Rechte Seite da/dt = a · H(a) für den ODE-Solver."""
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
    """Löst die Friedmann-Gleichung in SI-Einheiten.

    Parameters
    ----------
    H0 : float
        Hubble-Konstante in km/s/Mpc (Standard: Planck-2018).
    Omega_m, Omega_r, Omega_Lambda : float
        Dichteparameter (dimensionslos, Summe ≈ 1 für flaches Universum).
    t_span_Gyr : tuple
        Integrationsintervall in Gyr, z.B. (0.001, 13.8).
    n_eval : int
        Anzahl Auswertungspunkte.
    d_eta : float
        RFT-Korrekturparameter. d_eta = 0 → reines ΛCDM.
    delta_phi_func : callable or None
        Funktion Δφ(t_Gyr) für RFT-Korrektur. Falls None und d_eta != 0,
        wird Δφ = const = π/4 verwendet (Näherung).

    Returns
    -------
    dict mit:
        t_Gyr      : array, Zeit in Gyr
        a_lcdm     : array, Skalenfaktor (ΛCDM)
        a_rft      : array, Skalenfaktor (ΛCDM + η-Korrektur)
        H_lcdm_si  : array, Hubble-Parameter in s⁻¹
        H_lcdm_kmsMpc : array, Hubble-Parameter in km/s/Mpc
        H_rft_kmsMpc  : array, RFT-korrigierter Hubble in km/s/Mpc
        H0_si      : float, H₀ in s⁻¹
    """
    H0_si = H0 * _KM_PER_MPC_TO_SI  # s⁻¹

    # Anfangsbedingung: a(t_start) = H0 * t_start (Strahlungsdomäne-Näherung)
    t_start_s = t_span_Gyr[0] * _GYR_TO_S
    t_end_s = t_span_Gyr[1] * _GYR_TO_S

    # Bessere Anfangsbedingung: iterativ konsistentes a_0
    a_start = H0_si * t_start_s * np.sqrt(Omega_r) * 0.5

    # Sicherstellen, dass a_start > 0
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

    # Normierung: a(t_heute) = 1 bei t = 13.8 Gyr
    # t_heute = 13.8 Gyr ist innerhalb des Integrationszeitraums
    t_today_s = 13.8 * _GYR_TO_S
    if t_today_s <= t_end_s:
        a_today = float(sol.sol(t_today_s)[0])
    else:
        a_today = a_raw[-1]

    a_lcdm = a_raw / a_today

    # ΛCDM Hubble-Parameter
    H_lcdm_si = np.array([
        _h_lcdm(a, H0_si, Omega_m, Omega_r, Omega_Lambda)
        for a in np.where(a_lcdm > 0, a_lcdm, 1e-10)
    ])
    H_lcdm_kmsMpc = H_lcdm_si / _KM_PER_MPC_TO_SI

    # RFT-Korrektur: H_rft = H_lcdm · (1 + d_eta · cos²(Δφ/2))
    if delta_phi_func is not None:
        delta_phi = np.array([delta_phi_func(t) for t in t_Gyr])
    else:
        # Standardnäherung: Δφ aus H0-Skalierung
        # d_eta(H0) = 0.00204 * H0 - 0.00404 (aus H0-Scan)
        delta_phi = np.full_like(t_Gyr, np.pi / 4)

    eps_dphi = np.cos(delta_phi / 2) ** 2  # ε(Δφ) = cos²(Δφ/2)
    H_rft_kmsMpc = H_lcdm_kmsMpc * (1.0 + d_eta * eps_dphi)

    # RFT-Skalenfaktor: integriere H_rft numerisch
    # a_rft(t) = a_lcdm(t_0) * exp(∫ H_rft dt) — hier Näherung über kumulative Summe
    dt_s = np.diff(sol.t, prepend=sol.t[0])
    H_rft_si = H_rft_kmsMpc * _KM_PER_MPC_TO_SI
    # Kumulatives Integral ∫ H_rft dt ab t_start
    integral_H_rft = np.cumsum(H_rft_si * dt_s)
    integral_H_lcdm = np.cumsum(H_lcdm_si * dt_s)

    # Normierung auf a_lcdm am Startpunkt
    a_rft = a_lcdm[0] * np.exp(integral_H_rft - integral_H_lcdm[0])
    # Auf a(t_heute) = 1 normieren
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
    """Vergleicht den RFT-Solver mit astropy.cosmology.FlatLambdaCDM.

    Parameters
    ----------
    H0 : float
        Hubble-Konstante in km/s/Mpc.
    Omega_m : float
        Materiedichteparameter.
    Omega_Lambda : float
        Λ-Dichteparameter.
    t_span_Gyr : tuple
        Vergleichszeitraum in Gyr.
    n_eval : int
        Anzahl Vergleichspunkte.
    d_eta : float
        RFT-Korrekturparameter.

    Returns
    -------
    dict mit:
        t_Gyr       : array
        a_rft       : array, RFT-Skalenfaktor
        a_astropy   : array, astropy-Referenz
        rel_err     : array, |a_rft − a_astropy| / a_astropy
        max_rel_err : float, maximale relative Abweichung
        passes_1pct : bool, ob Kriterium < 1% erfüllt
    """
    try:
        from astropy.cosmology import FlatLambdaCDM
        import astropy.units as u
    except ImportError as exc:
        raise ImportError(
            "RT-04 benötigt astropy:\n"
            "  pip install astropy\n"
        ) from exc

    Omega_r = OMEGA_R  # Strahlung mitberücksichtigen
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

    # astropy-Referenz
    cosmo = FlatLambdaCDM(H0=H0, Om0=Omega_m, Ob0=OMEGA_B_H2 / (H0 / 100) ** 2)
    a_astropy = np.array([
        float(cosmo.scale_factor(cosmo.lookbacktime(np.inf) - t * u.Gyr + cosmo.lookbacktime(0)))
        if t > 0 else 0.0
        for t in t_Gyr
    ])

    # Sicherere Methode: z → a über age(z) = t
    # Benutze lookbacktime-Umkehrung
    from scipy.interpolate import interp1d
    z_test = np.logspace(-3, 4, 5000)
    age_test = cosmo.age(z_test).to(u.Gyr).value
    # age ist monoton fallend in z; umkehren
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
        # Clip auf sinnvollen Bereich
        a_astropy = np.clip(a_astropy, 1e-6, 1.0)
    else:
        # Fallback: Materie-dominierte Näherung
        t_0 = cosmo.age(0).to(u.Gyr).value
        a_astropy = (t_Gyr / t_0) ** (2.0 / 3.0)

    # Relative Abweichung
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
