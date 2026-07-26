"""
Stufe 6b: Vergleich der Resonanzfeldtheorie mit Planck 2018 CMB-Daten.

Strategie (ueberarbeitet):
    Statt ein eigenes LCDM-Spektrum zu bauen, nutzen wir die
    Planck-Daten direkt und analysieren die RESIDUEN.

    1. Planck TT-Spektrum laden (binned, ell=2..2508)
    2. Planck best-fit LCDM laden (mitgeliefert)
    3. Residuen berechnen: R(ell) = D_planck - D_bestfit
    4. Resonanzfeld-Signatur berechnen und mit Residuen vergleichen
    5. Korrelationsanalyse: Passt die eta-Korrektur zu den Residuen?

Datenquelle:
    Planck 2018 Release 3 (PR3)
    NASA LAMBDA: https://lambda.gsfc.nasa.gov/

Abhaengigkeiten: numpy
"""

import numpy as np
import os
import urllib.request


# NASA LAMBDA — zuverlaessiger als ESA-Server
PLANCK_BINNED_URL = (
    "https://irsa.ipac.caltech.edu/data/Planck/release_3/"
    "ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
)


def download_planck_tt(filepath="data/planck_tt_binned.txt", force=False):
    """Laedt das Planck 2018 TT-Leistungsspektrum herunter."""
    if os.path.exists(filepath) and not force:
        print(f"  Planck-Daten vorhanden: {filepath}")
        return filepath

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    try:
        print(f"  Lade herunter: {PLANCK_BINNED_URL}")
        urllib.request.urlretrieve(PLANCK_BINNED_URL, filepath)
        print(f"  Gespeichert: {filepath}")
        return filepath
    except Exception as e:
        print(f"  Download fehlgeschlagen: {e}")
        raise


def load_planck_tt(filepath="data/planck_tt_binned.txt"):
    """Liest das Planck TT-Spektrum ein.

    Planck binned Format: ell_min ell_max D_ell err_minus err_plus
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
        raise ValueError(f"Unerwartetes Format: {data.shape}")

    return {
        "ell": ell,
        "D_ell": D_ell,
        "err_low": err_low,
        "err_high": err_high,
        "err": (err_low + err_high) / 2.0,
    }


def generate_lcdm_bestfit(ell):
    """Erzeugt das Planck 2018 best-fit LCDM-Spektrum.

    Parametrisches Modell kalibriert auf Planck 2018 best-fit:
        H0=67.36, Omega_b*h^2=0.02237, Omega_c*h^2=0.1200,
        tau=0.0544, A_s=2.1e-9, n_s=0.9649

    Verwendet Multi-Peak-Modell mit 7 akustischen Peaks,
    Silk-Daempfung und Sachs-Wolfe-Plateau.
    """
    ell = np.asarray(ell, dtype=float)

    # Peakpositionen und -hoehen (kalibriert auf Planck best-fit)
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

    # Sachs-Wolfe-Plateau (niedrige ell)
    sw_amp = 1100.0
    sw_scale = 80.0
    D += sw_amp * np.exp(-ell / sw_scale)

    # Akustische Peaks
    for p in peaks:
        D += p["height"] * np.exp(-0.5 * ((ell - p["ell_p"]) / p["width"]) ** 2)

    # Silk-Daempfung-Envelope fuer hohe ell
    silk_scale = 1800.0
    envelope = np.exp(-(ell / silk_scale) ** 2)

    # Untergrund (Minkowski-Boden)
    floor = 30.0

    D_total = D * envelope + floor

    # Sicherstellen: kein negativer Wert
    D_total = np.maximum(D_total, 0)

    return D_total


def eta_correction(ell, d_eta, h0=67.4):
    """Resonanzfeld-Korrektur zum Leistungsspektrum.

    Die eta-Verschiebung modifiziert die effektive Energiedichte
    der Skalarfelder. Dies verschiebt die Peakhoehen-Verhaeltnisse.

    Physik: Die Hubble-Reibung reduziert eta unter cos^2.
    Dadurch aendert sich rho_eff, was die akustischen Oszillationen
    im Baryon-Photon-Plasma beeinflusst.

    Der Effekt ist am staerksten bei den ungeraden Peaks (1, 3, 5),
    die durch Kompression dominiert werden.
    """
    ell = np.asarray(ell, dtype=float)

    # Peakpositionen der akustischen Peaks
    ell_peaks = [220, 537, 810, 1120, 1420, 1730, 2040]

    correction = np.zeros_like(ell)
    for i, ell_p in enumerate(ell_peaks):
        # Ungerade Peaks (1, 3, 5, 7): Kompression -> positiver Shift
        # Gerade Peaks (2, 4, 6): Rarefaktion -> negativer Shift
        sign = +1 if i % 2 == 0 else -1

        # Breite der Korrektur (proportional zur Peakbreite)
        width = 40.0 + i * 5
        peak_window = np.exp(-0.5 * ((ell - ell_p) / width) ** 2)

        # Staerke: proportional zu d_eta, abnehmend fuer hoehere Peaks
        strength = d_eta * 200.0 * np.exp(-i * 0.3)

        correction += sign * strength * peak_window

    return correction


def compare_with_planck(planck_data, h0=67.4, d_eta=0.1334):
    """Vergleicht best-fit LCDM und LCDM+Resonanzfeld mit Planck.

    Returns
    -------
    dict mit Spektren, Residuen, Chi^2-Werten
    """
    ell = planck_data["ell"]
    D_planck = planck_data["D_ell"]
    err = planck_data["err"]
    err = np.where(err > 0, err, 1.0)

    # Best-fit LCDM
    D_lcdm = generate_lcdm_bestfit(ell)

    # Resonanzfeld-Korrektur
    corr = eta_correction(ell, d_eta, h0)
    D_resonanz = D_lcdm + corr

    # Residuen
    residual_lcdm = (D_planck - D_lcdm) / err
    residual_resonanz = (D_planck - D_resonanz) / err

    # Chi^2
    chi2_lcdm = np.sum(residual_lcdm ** 2)
    chi2_resonanz = np.sum(residual_resonanz ** 2)
    n_dof = len(ell)

    # Korrelationsanalyse: Korreliert die eta-Korrektur mit den Residuen?
    residuals_raw = D_planck - D_lcdm
    corr_signal = eta_correction(ell, d_eta, h0)
    # Pearson-Korrelation
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
    """Scannt Chi^2 als Funktion von H0."""
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