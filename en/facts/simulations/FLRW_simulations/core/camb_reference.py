"""
RT-05: CAMB/CLASS reference spectrum for CMB comparison.

Replaces generate_lcdm_bestfit() (toy model) with a real Boltzmann
code (CAMB or CLASS) as the ΛCDM reference.

Fallback hierarchy:
    1. CAMB  (pip install camb)   — preferred
    2. CLASS (pip install classy) — alternative
    3. ImportError with clear instructions

Planck-2018 default values (arXiv:1807.06209):
    H0=67.36, ombh2=0.02237, omch2=0.1200, tau=0.0544,
    As=2.1e-9, ns=0.9649

Dependencies: numpy, camb or classy
"""

import numpy as np

# ---------------------------------------------------------------------------
# Planck-2018 default values (arXiv:1807.06209)
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
    """Computes the ΛCDM CMB TT power spectrum via CAMB or CLASS.

    Parameters
    ----------
    H0 : float
        Hubble constant in km/s/Mpc.
    ombh2 : float
        Baryon density × h² (default: Planck-2018).
    omch2 : float
        CDM density × h² (default: Planck-2018).
    tau : float
        Optical depth (default: Planck-2018).
    As : float
        Primordial power spectrum amplitude A_s.
    ns : float
        Spectral index n_s.
    lmax : int
        Maximum multipole moment.

    Returns
    -------
    dict with:
        ell      : array, multipole moments ℓ = 2..lmax
        D_ell    : array, D_ℓ = ℓ(ℓ+1)/2π · C_ℓ [μK²]
        backend  : str, 'camb' or 'classy'

    Raises
    ------
    ImportError
        If neither CAMB nor CLASS is installed.
    """
    # Attempt 1: CAMB
    try:
        return _generate_with_camb(H0, ombh2, omch2, tau, As, ns, lmax)
    except ImportError:
        pass

    # Attempt 2: CLASS
    try:
        return _generate_with_classy(H0, ombh2, omch2, tau, As, ns, lmax)
    except ImportError:
        pass

    raise ImportError(
        "RT-05 requires CAMB or CLASS:\n"
        "  pip install camb   (recommended)\n"
        "  pip install classy (alternative)\n"
        "\n"
        "The current generate_lcdm_bestfit() fallback is insufficient for RT-05\n"
        "(toy model, not a physical Boltzmann solver)."
    )


def _generate_with_camb(H0, ombh2, omch2, tau, As, ns, lmax):
    """Internal CAMB implementation."""
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
    tt = powers["total"][:, 0]  # TT spectrum, D_ℓ [μK²]

    ell_arr = np.arange(len(tt))
    mask = ell_arr >= 2
    return {
        "ell": ell_arr[mask].astype(float),
        "D_ell": tt[mask],
        "backend": "camb",
    }


def _generate_with_classy(H0, ombh2, omch2, tau, As, ns, lmax):
    """Internal CLASS implementation."""
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
    # CLASS returns C_ℓ; D_ℓ = ℓ(ℓ+1)/(2π) · C_ℓ · T_cmb² · 1e12
    T_cmb_uK = 2.7255e6  # μK
    D_ell = ell_arr * (ell_arr + 1) / (2.0 * np.pi) * cls["tt"] * T_cmb_uK**2

    mask = ell_arr >= 2
    cosmo.struct_cleanup()
    return {
        "ell": ell_arr[mask],
        "D_ell": D_ell[mask],
        "backend": "classy",
    }
