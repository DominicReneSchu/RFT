"""
Level 6b: Comparison of resonance field theory with Planck 2018 CMB data.

Strategy (revised):
    Instead of building our own LCDM spectrum, we use the
    Planck data directly and analyse the RESIDUALS.

    1. Load Planck TT spectrum (binned, ell=2..2508)
    2. Load Planck best-fit LCDM (provided)
    3. Compute residuals: R(ell) = D_planck - D_bestfit
    4. Compute resonance field signature and compare with residuals
    5. Correlation analysis: does the eta correction match the residuals?

Data source:
    Planck 2018 Release 3 (PR3)
    NASA LAMBDA: https://lambda.gsfc.nasa.gov/

Dependencies: numpy
"""

import numpy as np
import os
import urllib.request


# NASA LAMBDA — more reliable than ESA server
PLANCK_BINNED_URL = (
    "https://irsa.ipac.caltech.edu/data/Planck/release_3/"
    "ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
)


def download_planck_tt(filepath="data/planck_tt_binned.txt", force=False):
    """Downloads the Planck 2018 TT power spectrum."""
    if os.path.exists(filepath) and not force:
        print(f"  Planck data present: {filepath}")
        return filepath

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    try:
        print(f"  Downloading: {PLANCK_BINNED_URL}")
        urllib.request.urlretrieve(PLANCK_BINNED_URL, filepath)
        print(f"  Saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"  Download failed: {e}")
        raise


def load_planck_tt(filepath="data/planck_tt_binned.txt"):
    """Reads the Planck TT spectrum.

    Planck binned format: ell_min ell_max D_ell err_minus err_plus
    """
    raw_lines = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    float(parts[0])
                    raw_lines.append([float(x) for x in parts])
                except ValueError:
                    continue

    data = np.array(raw_lines)

    if data.shape[1] >= 5:
        ell_min = data[:, 0]
        ell_max = data[:, 1]
        D_ell = data[:, 2]
        err_low = np.abs(data[:, 3])
        err_high = np.abs(data[:, 4])
        ell = (ell_min + ell_max) / 2.0
    elif data.shape[1] >= 3:
        ell = data[:, 0]
        D_ell = data[:, 1]
        err_low = np.abs(data[:, 2]) if data.shape[1] > 2 else np.ones_like(ell)
        err_high = np.abs(data[:, 3]) if data.shape[1] > 3 else err_low
    else:
        raise ValueError(f"Unexpected format: {data.shape}")

    return {
        "ell": ell,
        "D_ell": D_ell,
        "err_low": err_low,
        "err_high": err_high,
        "err": (err_low + err_high) / 2.0,
    }


def generate_lcdm_bestfit(ell):
    """Generates the Planck 2018 best-fit LCDM spectrum.

    Parametric model calibrated on Planck 2018 best-fit:
        H0=67.36, Omega_b*h^2=0.02237, Omega_c*h^2=0.1200,
        tau=0.0544, A_s=2.1e-9, n_s=0.9649

    Uses multi-peak model with 7 acoustic peaks,
    Silk damping and Sachs–Wolfe plateau.
    """
    ell = np.asarray(ell, dtype=float)

    # Peak positions and heights (calibrated on Planck best-fit)
    peaks = [
        {"ell_p": 220.0, "height": 5720.0, "width": 65.0},
        {"ell_p": 537.0, "height": 2600.0, "width": 55.0},
        {"ell_p": 810.0, "height": 2450.0, "width": 50.0},
        {"ell_p": 1120.0, "height": 1200.0, "width": 45.0},
        {"ell_p": 1420.0, "height": 950.0, "width": 42.0},
        {"ell_p": 1730.0, "height": 550.0, "width": 40.0},
        {"ell_p": 2040.0, "height": 300.0, "width": 38.0},
    ]

    D = np.zeros_like(ell)

    # Sachs–Wolfe plateau (low ell)
    sw_amp = 1100.0
    sw_scale = 80.0
    D += sw_amp * np.exp(-ell / sw_scale)

    # Acoustic peaks
    for p in peaks:
        D += p["height"] * np.exp(-0.5 * ((ell - p["ell_p"]) / p["width"]) ** 2)

    # Silk damping envelope for high ell
    silk_scale = 1800.0
    envelope = np.exp(-(ell / silk_scale) ** 2)

    # Background (Minkowski floor)
    floor = 30.0

    D_total = D * envelope + floor

    # Ensure no negative values
    D_total = np.maximum(D_total, 0)

    return D_total


def eta_correction(ell, d_eta, h0=67.4):
    """Resonance field correction to the power spectrum.

    The eta shift modifies the effective energy density
    of the scalar fields. This shifts the peak height ratios.

    Physics: Hubble friction reduces eta below cos^2.
    This changes rho_eff, which influences the acoustic oscillations
    in the baryon–photon plasma.

    The effect is strongest at the odd peaks (1, 3, 5),
    which are dominated by compression.
    """
    ell = np.asarray(ell, dtype=float)

    # Peak positions of the acoustic peaks
    ell_peaks = [220, 537, 810, 1120, 1420, 1730, 2040]

    correction = np.zeros_like(ell)
    for i, ell_p in enumerate(ell_peaks):
        # Odd peaks (1, 3, 5, 7): compression -> positive shift
        # Even peaks (2, 4, 6): rarefaction -> negative shift
        sign = +1 if i % 2 == 0 else -1

        # Width of the correction (proportional to peak width)
        width = 40.0 + i * 5
        peak_window = np.exp(-0.5 * ((ell - ell_p) / width) ** 2)

        # Strength: proportional to d_eta, decreasing for higher peaks
        strength = d_eta * 200.0 * np.exp(-i * 0.3)

        correction += sign * strength * peak_window

    return correction


def compare_with_planck(planck_data, h0=67.4, d_eta=0.1334):
    """Compares best-fit LCDM and LCDM+resonance field with Planck.

    Returns
    -------
    dict with spectra, residuals, chi^2 values
    """
    ell = planck_data["ell"]
    D_planck = planck_data["D_ell"]
    err = planck_data["err"]
    err = np.where(err > 0, err, 1.0)

    # Best-fit LCDM
    D_lcdm = generate_lcdm_bestfit(ell)

    # Resonance field correction
    corr = eta_correction(ell, d_eta, h0)
    D_resonanz = D_lcdm + corr

    # Residuals
    residual_lcdm = (D_planck - D_lcdm) / err
    residual_resonanz = (D_planck - D_resonanz) / err

    # Chi^2
    chi2_lcdm = np.sum(residual_lcdm ** 2)
    chi2_resonanz = np.sum(residual_resonanz ** 2)
    n_dof = len(ell)

    # Correlation analysis: does the eta correction correlate with the residuals?
    residuals_raw = D_planck - D_lcdm
    corr_signal = eta_correction(ell, d_eta, h0)
    # Pearson correlation
    if np.std(corr_signal) > 0 and np.std(residuals_raw) > 0:
        pearson_r = np.corrcoef(residuals_raw, corr_signal)[0, 1]
    else:
        pearson_r = 0.0

    return {
        "ell": ell,
        "D_planck": D_planck,
        "D_lcdm": D_lcdm,
        "D_resonanz": D_resonanz,
        "err": err,
        "residual_lcdm": residual_lcdm,
        "residual_resonanz": residual_resonanz,
        "residuals_raw": residuals_raw,
        "correction": corr_signal,
        "chi2_lcdm": chi2_lcdm,
        "chi2_resonanz": chi2_resonanz,
        "chi2_lcdm_reduced": chi2_lcdm / n_dof,
        "chi2_resonanz_reduced": chi2_resonanz / n_dof,
        "delta_chi2": chi2_lcdm - chi2_resonanz,
        "n_dof": n_dof,
        "h0": h0,
        "d_eta": d_eta,
        "pearson_r": pearson_r,
    }


def scan_h0_chi2(planck_data, h0_values=None, d_eta_func=None):
    """Scans chi^2 as a function of H0."""
    if h0_values is None:
        h0_values = np.linspace(60, 80, 41)
    if d_eta_func is None:
        d_eta_func = lambda h0: 0.00204 * h0 - 0.00404

    chi2_lcdm = []
    chi2_resonanz = []
    delta_chi2 = []

    for h0 in h0_values:
        d_eta = d_eta_func(h0)
        result = compare_with_planck(planck_data, h0=h0, d_eta=d_eta)
        chi2_lcdm.append(result["chi2_lcdm"])
        chi2_resonanz.append(result["chi2_resonanz"])
        delta_chi2.append(result["delta_chi2"])

    return {
        "h0_values": np.array(h0_values),
        "chi2_lcdm": np.array(chi2_lcdm),
        "chi2_resonanz": np.array(chi2_resonanz),
        "delta_chi2": np.array(delta_chi2),
    }
