"""
RT-05: CAMB/CLASS-Referenzspektrum für CMB-Vergleich.

Ersetzt generate_lcdm_bestfit() (Spielzeugmodell) durch einen echten
Boltzmann-Code (CAMB oder CLASS) als ΛCDM-Referenz.

Fallback-Hierarchie:
    1. CAMB  (pip install camb)   — bevorzugt
    2. CLASS (pip install classy) — Alternative
    3. ImportError mit klarem Hinweis

Planck-2018-Standardwerte (arXiv:1807.06209):
    H0=67.36, ombh2=0.02237, omch2=0.1200, tau=0.0544,
    As=2.1e-9, ns=0.9649

Abhängigkeiten: numpy, camb oder classy
"""

import numpy as np

# ---------------------------------------------------------------------------
# Planck-2018-Standardwerte (arXiv:1807.06209)
# ---------------------------------------------------------------------------
_PLANCK_H0 = 67.36
_PLANCK_OMBH2 = 0.02237
_PLANCK_OMCH2 = 0.1200
_PLANCK_TAU = 0.0544
_PLANCK_AS = 2.1e-9
_PLANCK_NS = 0.9649


def generate_camb_spectrum(
    H0=_PLANCK_H0,
    ombh2=_PLANCK_OMBH2,
    omch2=_PLANCK_OMCH2,
    tau=_PLANCK_TAU,
    As=_PLANCK_AS,
    ns=_PLANCK_NS,
    lmax=2500,
):
    """Berechnet das ΛCDM-CMB-TT-Leistungsspektrum mit CAMB oder CLASS.

    Parameters
    ----------
    H0 : float
        Hubble-Konstante in km/s/Mpc.
    ombh2 : float
        Baryonische Dichte × h² (Standard: Planck-2018).
    omch2 : float
        CDM-Dichte × h² (Standard: Planck-2018).
    tau : float
        Optische Tiefe (Standard: Planck-2018).
    As : float
        Primordiale Leistungsskalierung A_s.
    ns : float
        Spektralindex n_s.
    lmax : int
        Maximaler Multipolmoment.

    Returns
    -------
    dict mit:
        ell      : array, Multipolmomente ℓ = 2..lmax
        D_ell    : array, D_ℓ = ℓ(ℓ+1)/2π · C_ℓ [μK²]
        backend  : str, 'camb' oder 'classy'

    Raises
    ------
    ImportError
        Falls weder CAMB noch CLASS installiert ist.
    """
    # Versuch 1: CAMB
    try:
        return _generate_with_camb(H0, ombh2, omch2, tau, As, ns, lmax)
    except ImportError:
        pass

    # Versuch 2: CLASS
    try:
        return _generate_with_classy(H0, ombh2, omch2, tau, As, ns, lmax)
    except ImportError:
        pass

    raise ImportError(
        "RT-05 benötigt CAMB oder CLASS:\n"
        "  pip install camb   (empfohlen)\n"
        "  pip install classy (Alternative)\n"
        "\n"
        "Der aktuelle generate_lcdm_bestfit()-Fallback ist für RT-05 nicht\n"
        "ausreichend (Spielzeugmodell, kein physikalischer Boltzmann-Solver)."
    )


def _generate_with_camb(H0, ombh2, omch2, tau, As, ns, lmax):
    """Interne CAMB-Implementierung."""
    import camb  # noqa: PLC0415

    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=H0,
        ombh2=ombh2,
        omch2=omch2,
        tau=tau,
    )
    pars.InitPower.set_params(As=As, ns=ns)
    pars.set_for_lmax(lmax, lens_potential_accuracy=0)

    results = camb.get_results(pars)
    powers = results.get_cmb_power_spectra(pars, CMB_unit="muK")
    tt = powers["total"][:, 0]  # TT-Spektrum, D_ℓ [μK²]

    ell_arr = np.arange(len(tt))
    mask = ell_arr >= 2
    return {
        "ell": ell_arr[mask].astype(float),
        "D_ell": tt[mask],
        "backend": "camb",
    }


def _generate_with_classy(H0, ombh2, omch2, tau, As, ns, lmax):
    """Interne CLASS-Implementierung."""
    from classy import Class  # noqa: PLC0415

    cosmo = Class()
    cosmo.set({
        "H0": H0,
        "omega_b": ombh2,
        "omega_cdm": omch2,
        "tau_reio": tau,
        "A_s": As,
        "n_s": ns,
        "output": "tCl",
        "l_max_scalars": lmax,
        "lensing": "no",
    })
    cosmo.compute()
    cls = cosmo.raw_cl(lmax)
    ell_arr = cls["ell"].astype(float)
    # CLASS gibt C_ℓ in K² zurück; D_ℓ = ℓ(ℓ+1)/(2π) · C_ℓ · (T_CMB in μK)²
    # T_CMB = 2.7255 K = 2.7255e6 μK → Faktor = (2.7255e6)²
    T_cmb_K = 2.7255          # K
    T_cmb_factor = (T_cmb_K * 1e6) ** 2  # μK²/K²
    D_ell = ell_arr * (ell_arr + 1) / (2.0 * np.pi) * cls["tt"] * T_cmb_factor

    mask = ell_arr >= 2
    cosmo.struct_cleanup()
    return {
        "ell": ell_arr[mask],
        "D_ell": D_ell[mask],
        "backend": "classy",
    }
