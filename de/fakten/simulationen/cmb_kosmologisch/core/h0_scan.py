"""
Stufe 6a: H0-abhaengiger Scan der Resonanzfeldkopplung.

Kernfrage: Wie veraendert sich die Abweichung d_eta als Funktion
der Hubble-Konstante H0?

Physikalischer Hintergrund:
    In der Simulation steuert adot0 = H0 * a0 die anfaengliche
    Expansionsrate. Da a0 = 1 (normiert), gilt adot0 = H0.
    Die Hubble-Reibung (-3H * epsdot) daempft die Feldoszillationen
    und verschiebt eta systematisch unter cos^2(dphi/2).

    Vorhersage der Resonanzfeldtheorie:
        d_eta(H0) waechst monoton mit H0.
        Die Steigung dd_eta/dH0 ist die messbare Signatur.

Einheiten:
    H0 wird in natuerlichen Einheiten uebergeben.
    Fuer den Vergleich mit Beobachtungen (km/s/Mpc) wird
    ein Umrechnungsfaktor bereitgestellt.

Abhaengigkeiten: numpy, core.coupled_flrw, core.flat_coupled
"""

import numpy as np
from core.coupled_flrw import scan_phase_coupling
from core.flat_coupled import scan_phase_flat


# Umrechnung: H0 [km/s/Mpc] -> H0 [1/s] -> natuerliche Einheiten
# 1 Mpc = 3.0857e22 m, c = 2.998e8 m/s
# H0_phys = H0_kmsMpc * 1e3 / 3.0857e22  [1/s]
# In Planck-Einheiten: t_P = 5.391e-44 s -> H0_planck = H0_phys * t_P
# Fuer die Simulation: Wir skalieren H0_kmsMpc linear auf adot0.
# Referenzpunkt: H0 = 67.4 km/s/Mpc -> adot0 = 0.3 (unser Standardwert)
H0_REF = 67.4       # Planck 2018 [km/s/Mpc]
ADOT0_REF = 0.3      # Simulationseinheit bei H0_REF


def h0_to_adot0(h0_kmsMpc):
    """Konvertiert H0 [km/s/Mpc] in Simulationseinheit adot0.

    Lineare Skalierung relativ zum Referenzpunkt:
        adot0 = ADOT0_REF * (H0 / H0_REF)
    """
    return ADOT0_REF * (h0_kmsMpc / H0_REF)


def scan_h0(
    h0_values=None,
    delta_phi_values=None,
    t_span=(0, 60),
    m=1.0, lmbda=0.1, alpha=0.5, kappa=1.0, g=0.2,
):
    """Fuehrt einen systematischen H0-Scan durch.

    Fuer jeden H0-Wert wird ein vollstaendiger Phasenscan ausgefuehrt.
    Die mittlere Abweichung d_eta = <|eta_sim - cos^2(dphi/2)|>
    wird als Funktion von H0 berechnet.

    Parameters
    ----------
    h0_values : array-like or None
        H0-Werte in [km/s/Mpc]. Default: 60 bis 80 in 21 Schritten.
    delta_phi_values : array-like or None
        Phasendifferenzen fuer den Scan. Default: 15 Werte, 0 bis pi.
    t_span : tuple
        Simulationszeitintervall.
    m, lmbda, alpha, kappa, g : float
        Modellparameter (Defaults aus config).

    Returns
    -------
    dict mit:
        h0_values        : H0-Werte [km/s/Mpc]
        adot0_values     : Zugehoerige adot0-Werte
        d_eta_mean       : Mittlere Abweichung pro H0
        d_eta_std        : Standardabweichung pro H0
        d_eta_flat       : Referenzwert fuer flache Raumzeit (H=0)
        eta_scans        : Liste der vollstaendigen Phasenscan-Ergebnisse
    """
    if h0_values is None:
        h0_values = np.linspace(60, 80, 21)
    h0_values = np.asarray(h0_values, dtype=float)

    if delta_phi_values is None:
        delta_phi_values = np.linspace(0, np.pi, 15)
    delta_phi_values = np.asarray(delta_phi_values, dtype=float)

    common = dict(m=m, lmbda=lmbda, g=g)

    # Referenz: Flache Raumzeit
    scan_flat = scan_phase_flat(
        delta_phi_values=delta_phi_values, t_span=t_span, **common,
    )
    v_flat = np.isfinite(scan_flat["eta_mean"])
    if np.any(v_flat):
        d_eta_flat = np.nanmean(
            np.abs(scan_flat["eta_mean"][v_flat] - scan_flat["eta_cos2"][v_flat])
        )
    else:
        d_eta_flat = np.nan

    # H0-Scan
    d_eta_mean = []
    d_eta_std = []
    eta_scans = []

    for h0 in h0_values:
        adot0 = h0_to_adot0(h0)
        scan = scan_phase_coupling(
            delta_phi_values=delta_phi_values,
            t_span=t_span,
            alpha=alpha, kappa=kappa, adot0=adot0,
            **common,
        )
        eta_scans.append(scan)

        v = np.isfinite(scan["eta_mean"])
        if np.any(v):
            residuals = np.abs(scan["eta_mean"][v] - scan["eta_cos2"][v])
            d_eta_mean.append(np.mean(residuals))
            d_eta_std.append(np.std(residuals))
        else:
            d_eta_mean.append(np.nan)
            d_eta_std.append(np.nan)

    result = {
        "h0_values": h0_values,
        "adot0_values": np.array([h0_to_adot0(h) for h in h0_values]),
        "d_eta_mean": np.array(d_eta_mean),
        "d_eta_std": np.array(d_eta_std),
        "d_eta_flat": d_eta_flat,
        "eta_scans": eta_scans,
        "delta_phi_values": delta_phi_values,
    }

    # Linearer Fit: d_eta = slope * H0 + intercept
    valid = np.isfinite(result["d_eta_mean"])
    if np.sum(valid) >= 2:
        coeffs = np.polyfit(h0_values[valid], result["d_eta_mean"][valid], 1)
        result["fit_slope"] = coeffs[0]
        result["fit_intercept"] = coeffs[1]
        result["fit_poly"] = coeffs
    else:
        result["fit_slope"] = np.nan
        result["fit_intercept"] = np.nan
        result["fit_poly"] = None

    return result


def predict_d_eta(h0, fit_result):
    """Vorhersage von d_eta fuer einen gegebenen H0-Wert.

    Parameters
    ----------
    h0 : float
        H0 in [km/s/Mpc]
    fit_result : dict
        Ergebnis von scan_h0()

    Returns
    -------
    float : vorhergesagtes d_eta
    """
    if fit_result["fit_poly"] is not None:
        return np.polyval(fit_result["fit_poly"], h0)
    return np.nan


def hubble_tension_signature(fit_result, h0_planck=67.4, h0_shoes=73.0):
    """Berechnet die Resonanzfeld-Signatur der Hubble-Spannung.

    Parameters
    ----------
    fit_result : dict
        Ergebnis von scan_h0()
    h0_planck : float
        Planck 2018 Messung [km/s/Mpc]
    h0_shoes : float
        SH0ES Messung [km/s/Mpc]

    Returns
    -------
    dict mit:
        d_eta_planck     : d_eta bei H0 = 67.4
        d_eta_shoes      : d_eta bei H0 = 73.0
        delta_d_eta      : Differenz (SH0ES - Planck)
        relative_shift   : Relative Verschiebung in Prozent
        slope            : dd_eta / dH0
    """
    d_planck = predict_d_eta(h0_planck, fit_result)
    d_shoes = predict_d_eta(h0_shoes, fit_result)
    delta = d_shoes - d_planck
    rel = (delta / d_planck * 100) if d_planck != 0 else np.nan

    return {
        "h0_planck": h0_planck,
        "h0_shoes": h0_shoes,
        "d_eta_planck": d_planck,
        "d_eta_shoes": d_shoes,
        "delta_d_eta": delta,
        "relative_shift": rel,
        "slope": fit_result["fit_slope"],
    }


def export_results(fit_result, filepath="h0_scan_results.csv"):
    """Exportiert die Scan-Ergebnisse als CSV.

    Parameters
    ----------
    fit_result : dict
        Ergebnis von scan_h0()
    filepath : str
        Ausgabepfad
    """
    h0 = fit_result["h0_values"]
    adot0 = fit_result["adot0_values"]
    d_eta = fit_result["d_eta_mean"]
    d_std = fit_result["d_eta_std"]

    header = "H0_kmsMpc,adot0,d_eta_mean,d_eta_std"
    data = np.column_stack([h0, adot0, d_eta, d_std])
    np.savetxt(filepath, data, delimiter=",", header=header, comments="",
               fmt=["%.2f", "%.6f", "%.6f", "%.6f"])