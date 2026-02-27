"""
Stufe 6b: Vergleich der Resonanzfeldtheorie mit Planck 2018 CMB-Daten.

Kernidee:
    Die Resonanzfeldtheorie sagt eine H0-abhaengige Verschiebung
    der Kopplungseffizienz eta voraus. Diese Verschiebung modifiziert
    die effektive Energiedichte skalarer Felder im fruehen Universum
    und hinterlaesst eine Signatur im CMB-Leistungsspektrum.

    Konkret: Die eta-Korrektur verschiebt das Verhaeltnis der
    akustischen Peaks relativ zum Standard-LCDM-Modell.

Datenquelle:
    Planck 2018 Release 3 (PR3)
    COM_PowerSpect_CMB-TT-binned_R3.01.txt
    Quelle: https://pla.esac.esa.int/pla/

Abhaengigkeiten: numpy, urllib (fuer Download)
"""

import numpy as np
import os
import urllib.request

# Planck 2018 TT-Spektrum (binned) — oeffentlich
PLANCK_URL = (
    "https://irsa.ipac.caltech.edu/data/Planck/release_3/"
    "ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-binned_R3.01.txt"
)
PLANCK_URL_FALLBACK = (
    "https://pla.esac.esa.int/pla/aio/product-action"
    "?COSMOLOGY.FILE_ID=COM_PowerSpect_CMB-TT-binned_R3.01.txt"
)


def download_planck_tt(filepath="data/planck_tt_binned.txt", force=False):
    """Laedt das Planck 2018 TT-Leistungsspektrum herunter.

    Parameters
    ----------
    filepath : str
        Lokaler Speicherpfad.
    force : bool
        Falls True, wird auch bei vorhandener Datei neu geladen.

    Returns
    -------
    str : Pfad zur heruntergeladenen Datei
    """
    if os.path.exists(filepath) and not force:
        print(f"  Planck-Daten vorhanden: {filepath}")
        return filepath

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    for url in [PLANCK_URL, PLANCK_URL_FALLBACK]:
        try:
            print(f"  Lade herunter: {url}")
            urllib.request.urlretrieve(url, filepath)
            print(f"  Gespeichert: {filepath}")
            return filepath
        except Exception as e:
            print(f"  Fehler bei {url}: {e}")

    raise RuntimeError("Planck-Daten konnten nicht heruntergeladen werden.")


def load_planck_tt(filepath="data/planck_tt_binned.txt"):
    """Liest das Planck TT-Spektrum ein.

    Erwartet Spalten: ell_min, ell_max, D_ell, err_minus, err_plus
    (D_ell = ell*(ell+1)*C_ell / (2*pi) in muK^2)

    Returns
    -------
    dict mit:
        ell      : Mittelpunkt der Bins
        D_ell    : D_ell-Werte [muK^2]
        err_low  : Unterer Fehler
        err_high : Oberer Fehler
    """
    # Ueberspringe Kommentarzeilen (beginnen mit #)
    data = np.loadtxt(filepath, comments="#")

    if data.shape[1] >= 5:
        ell_min = data[:, 0]
        ell_max = data[:, 1]
        D_ell = data[:, 2]
        err_low = data[:, 3]
        err_high = data[:, 4]
        ell = (ell_min + ell_max) / 2.0
    elif data.shape[1] >= 3:
        ell = data[:, 0]
        D_ell = data[:, 1]
        err_low = data[:, 2] if data.shape[1] > 2 else np.zeros_like(ell)
        err_high = data[:, 3] if data.shape[1] > 3 else err_low
    else:
        raise ValueError(f"Unerwartetes Datenformat: {data.shape[1]} Spalten")

    return {
        "ell": ell,
        "D_ell": D_ell,
        "err_low": err_low,
        "err_high": err_high,
    }


def lcdm_spectrum(ell, h0=67.4, omega_b=0.02237, omega_c=0.1200, tau=0.0544, A_s=2.1e-9, n_s=0.9649):
    """Vereinfachtes LCDM-Leistungsspektrum (analytische Naeherung).

    Verwendet die Sachs-Wolfe-Naeherung mit akustischen Peaks.
    Nicht fuer Praezisionskosmologie geeignet, aber ausreichend
    fuer den qualitativen Vergleich mit der eta-Korrektur.

    Parameters
    ----------
    ell : array
        Multipol-Momente
    h0 : float
        Hubble-Konstante [km/s/Mpc]
    omega_b, omega_c : float
        Baryonen- und CDM-Dichte (physikalisch)
    tau : float
        Optische Tiefe der Reionisation
    A_s : float
        Amplitude des primordialen Spektrums
    n_s : float
        Spektralindex

    Returns
    -------
    D_ell : array
        D_ell = ell*(ell+1)*C_ell/(2*pi) in muK^2
    """
    ell = np.asarray(ell, dtype=float)
    h = h0 / 100.0

    # Primordialer Beitrag (Harrison-Zeldovich mit Tilt)
    ell_pivot = 1500.0
    primordial = A_s * (ell / ell_pivot) ** (n_s - 1)

    # Akustische Peaks (vereinfachtes Modell)
    # Peakpositionen skalieren mit Schallhorizont
    theta_s = 0.0104 * (67.4 / h0)  # Schallhorizont-Winkel
    ell_peak = np.pi / theta_s

    # Envelope: Silk-Daempfung
    ell_silk = 1200.0 * (h0 / 67.4) ** 0.5
    damping = np.exp(-(ell / ell_silk) ** 1.2)

    # Akustische Oszillationen
    R_b = omega_b / omega_c  # Baryon-zu-CDM-Verhaeltnis
    phase_shift = 0.267 * R_b

    oscillation = 1.0 + 0.55 * np.cos(np.pi * ell / ell_peak + phase_shift)
    oscillation += 0.25 * np.cos(2 * np.pi * ell / ell_peak + 2 * phase_shift)
    oscillation += 0.10 * np.cos(3 * np.pi * ell / ell_peak + 3 * phase_shift)

    # Reionisations-Unterdrueckung
    reion = np.exp(-2 * tau) * np.ones_like(ell)
    reion[ell < 20] = 1.0  # Nur Hochmultipole betroffen

    # Zusammensetzen und normieren
    T_cmb = 2.7255e6  # muK
    C_ell = primordial * oscillation * damping * reion
    D_ell = ell * (ell + 1) / (2 * np.pi) * C_ell

    # Normierung auf Planck-Skala (~5700 muK^2 beim ersten Peak)
    norm = 5700.0 / np.max(D_ell[ell > 100])
    D_ell *= norm

    return D_ell


def eta_correction(ell, d_eta, ell_sensitive=(500, 1500)):
    """Berechnet die Resonanzfeld-Korrektur zum Leistungsspektrum.

    Die eta-Verschiebung modifiziert die effektive Energiedichte
    der Skalarfelder. Dies wirkt sich auf die Hoehen der akustischen
    Peaks aus, insbesondere auf das Verhaeltnis gerader zu ungerader Peaks.

    Parameters
    ----------
    ell : array
        Multipol-Momente
    d_eta : float
        Mittlere eta-Abweichung (aus H0-Scan)
    ell_sensitive : tuple
        Bereich maximaler Sensitivitaet

    Returns
    -------
    correction : array
        Multiplikativer Korrekturfaktor (1 + delta)
    """
    ell = np.asarray(ell, dtype=float)
    ell_min, ell_max = ell_sensitive

    # Sensitivitaetsfenster (Gauss-foermig)
    ell_center = (ell_min + ell_max) / 2
    ell_width = (ell_max - ell_min) / 2
    window = np.exp(-0.5 * ((ell - ell_center) / ell_width) ** 2)

    # Die eta-Verschiebung modifiziert die Peakhoehen
    # Effekt: Ungerade Peaks (1, 3, 5) werden relativ zu
    # geraden Peaks (2, 4) verschoben
    # Staerke: proportional zu d_eta
    correction = 1.0 + d_eta * window * 0.5 * np.sin(np.pi * ell / 300)

    return correction


def compare_with_planck(planck_data, h0=67.4, d_eta=0.1334):
    """Vergleicht LCDM und LCDM+Resonanzfeld mit Planck-Daten.

    Parameters
    ----------
    planck_data : dict
        Ergebnis von load_planck_tt()
    h0 : float
        Hubble-Konstante fuer das Modell
    d_eta : float
        eta-Abweichung aus dem H0-Scan

    Returns
    -------
    dict mit:
        ell          : Multipol-Momente
        D_planck     : Planck-Messwerte
        D_lcdm       : Standard-LCDM
        D_resonanz   : LCDM + Resonanzfeld-Korrektur
        residual_lcdm     : (Planck - LCDM) / err
        residual_resonanz : (Planck - Resonanz) / err
        chi2_lcdm    : Chi^2 fuer LCDM
        chi2_resonanz: Chi^2 fuer Resonanzfeld
    """
    ell = planck_data["ell"]
    D_planck = planck_data["D_ell"]
    err = (planck_data["err_low"] + planck_data["err_high"]) / 2
    err = np.where(err > 0, err, 1.0)  # Schutz gegen Division durch 0

    # Standard-LCDM
    D_lcdm = lcdm_spectrum(ell, h0=h0)

    # LCDM + Resonanzfeld-Korrektur
    corr = eta_correction(ell, d_eta)
    D_resonanz = D_lcdm * corr

    # Residuen
    residual_lcdm = (D_planck - D_lcdm) / err
    residual_resonanz = (D_planck - D_resonanz) / err

    # Chi^2
    chi2_lcdm = np.sum(residual_lcdm ** 2)
    chi2_resonanz = np.sum(residual_resonanz ** 2)
    n_dof = len(ell)

    return {
        "ell": ell,
        "D_planck": D_planck,
        "D_lcdm": D_lcdm,
        "D_resonanz": D_resonanz,
        "err": err,
        "residual_lcdm": residual_lcdm,
        "residual_resonanz": residual_resonanz,
        "chi2_lcdm": chi2_lcdm,
        "chi2_resonanz": chi2_resonanz,
        "chi2_lcdm_reduced": chi2_lcdm / n_dof,
        "chi2_resonanz_reduced": chi2_resonanz / n_dof,
        "n_dof": n_dof,
        "h0": h0,
        "d_eta": d_eta,
    }


def scan_h0_chi2(planck_data, h0_values=None, d_eta_func=None):
    """Scannt Chi^2 als Funktion von H0.

    Parameters
    ----------
    planck_data : dict
        Planck-Daten
    h0_values : array
        H0-Werte zum Scannen
    d_eta_func : callable
        Funktion d_eta(H0), z.B. aus linearem Fit

    Returns
    -------
    dict mit h0_values, chi2_lcdm, chi2_resonanz
    """
    if h0_values is None:
        h0_values = np.linspace(60, 80, 41)
    if d_eta_func is None:
        # Linearer Fit aus Stufe 6a
        d_eta_func = lambda h0: 0.00204 * h0 - 0.00404

    chi2_lcdm = []
    chi2_resonanz = []

    for h0 in h0_values:
        d_eta = d_eta_func(h0)
        result = compare_with_planck(planck_data, h0=h0, d_eta=d_eta)
        chi2_lcdm.append(result["chi2_lcdm"])
        chi2_resonanz.append(result["chi2_resonanz"])

    return {
        "h0_values": np.array(h0_values),
        "chi2_lcdm": np.array(chi2_lcdm),
        "chi2_resonanz": np.array(chi2_resonanz),
    }