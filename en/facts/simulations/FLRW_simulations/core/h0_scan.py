"""
Level 6a: H0-dependent scan of resonance field coupling.
PUBLICATION VERSION — extended with Jackknife error and bootstrap.

Core question: How does the deviation d_eta change as a function
of the Hubble constant H0?

Extensions:
  - Jackknife error on d_eta (leave-one-phase-out)
  - Bootstrap confidence intervals for slope
  - Extended H0 range (0-100 km/s/Mpc)
  - 30 phase points (instead of 15)
  - Weighted linear fit with 1-sigma band

Dependencies: numpy, core.coupled_flrw, core.flat_coupled
"""

import numpy as np
from core.coupled_flrw import scan_phase_coupling
from core.flat_coupled import scan_phase_flat


# Conversion: H0 [km/s/Mpc] -> adot0
# Reference point: H0 = 67.4 km/s/Mpc -> adot0 = 0.3
H0_REF = 67.4
ADOT0_REF = 0.3


def h0_to_adot0(h0_kmsMpc):
    """Converts H0 [km/s/Mpc] to simulation unit adot0.

    Linear scaling relative to the reference point:
        adot0 = ADOT0_REF * (H0 / H0_REF)

    Special case: H0 = 0 -> adot0 = 0 (flat spacetime).
    """
    return ADOT0_REF * (h0_kmsMpc / H0_REF)


def _jackknife_d_eta(eta_mean, eta_cos2):
    """Jackknife error on d_eta over phase groups.

    For N phase points: N jackknife samples, each leaving out one point.
    The jackknife error is:
        sigma_JK = sqrt((N-1)/N * sum((d_eta_i - d_eta_mean)^2))

    Returns
    -------
    d_eta : float
        Mean deviation (all points)
    d_eta_jk_err : float
        Jackknife error
    d_eta_jk_samples : array
        Individual jackknife values
    """
    valid = np.isfinite(eta_mean) & np.isfinite(eta_cos2)
    if np.sum(valid) < 3:
        return np.nan, np.nan, np.array([])

    residuals = np.abs(eta_mean[valid] - eta_cos2[valid])
    d_eta_full = np.mean(residuals)
    n = len(residuals)

    jk_samples = np.zeros(n)
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        jk_samples[i] = np.mean(residuals[mask])

    jk_err = np.sqrt((n - 1) / n * np.sum((jk_samples - d_eta_full) ** 2))

    return d_eta_full, jk_err, jk_samples


def scan_h0(
    h0_values=None,
    delta_phi_values=None,
    t_span=(0, 120),
    m=1.0, lmbda=0.1, alpha=0.5, kappa=1.0, g=0.2,
):
    """Performs a systematic H0 scan.
    PUBLICATION VERSION with Jackknife error.

    For each H0 value a full phase scan is executed.
    d_eta = <|eta_sim - cos^2(dphi/2)|> with Jackknife error.

    Parameters
    ----------
    h0_values : array-like or None
        H0 values in [km/s/Mpc]. Default: 0 to 100 in 51 steps.
    delta_phi_values : array-like or None
        Phase differences. Default: 30 values, 0 to pi.
    t_span : tuple
        Simulation time interval. Default: (0, 120).
    m, lmbda, alpha, kappa, g : float
        Model parameters (defaults from config).

    Returns
    -------
    dict with:
        h0_values        : H0 values [km/s/Mpc]
        adot0_values     : Corresponding adot0 values
        d_eta_mean       : Mean deviation per H0
        d_eta_std        : Standard deviation per H0 (over phases)
        d_eta_jk_err     : Jackknife error per H0
        d_eta_flat       : Reference value for flat spacetime (H=0)
        d_eta_flat_jk    : Jackknife error of the reference value
        eta_scans        : List of complete phase scan results
        n_simulations    : Total number of individual simulations
    """
    if h0_values is None:
        h0_values = np.linspace(0, 100, 51)
    h0_values = np.asarray(h0_values, dtype=float)

    if delta_phi_values is None:
        delta_phi_values = np.linspace(0, np.pi, 30)
    delta_phi_values = np.asarray(delta_phi_values, dtype=float)

    common = dict(m=m, lmbda=lmbda, g=g)
    n_sims = 0

    # Reference: flat spacetime
    scan_flat = scan_phase_flat(
        delta_phi_values=delta_phi_values, t_span=t_span, **common,
    )
    n_sims += len(delta_phi_values)

    d_eta_flat, d_eta_flat_jk, _ = _jackknife_d_eta(
        scan_flat["eta_mean"], scan_flat["eta_cos2"]
    )

    # H0 scan
    d_eta_mean = []
    d_eta_std = []
    d_eta_jk_err = []
    eta_scans = []

    for h0 in h0_values:
        adot0 = h0_to_adot0(h0)

        # At H0 = 0 use flat simulation
        if h0 == 0.0:
            scan = scan_flat
        else:
            scan = scan_phase_coupling(
                delta_phi_values=delta_phi_values,
                t_span=t_span,
                alpha=alpha, kappa=kappa, adot0=adot0,
                **common,
            )
            n_sims += len(delta_phi_values)

        eta_scans.append(scan)

        d_eta, jk_err, _ = _jackknife_d_eta(
            scan["eta_mean"], scan["eta_cos2"]
        )
        d_eta_mean.append(d_eta)
        d_eta_jk_err.append(jk_err)

        v = np.isfinite(scan["eta_mean"])
        if np.any(v):
            residuals = np.abs(scan["eta_mean"][v] - scan["eta_cos2"][v])
            d_eta_std.append(np.std(residuals))
        else:
            d_eta_std.append(np.nan)

    d_eta_mean = np.array(d_eta_mean)
    d_eta_std = np.array(d_eta_std)
    d_eta_jk_err = np.array(d_eta_jk_err)

    result = {
        "h0_values": h0_values,
        "adot0_values": np.array([h0_to_adot0(h) for h in h0_values]),
        "d_eta_mean": d_eta_mean,
        "d_eta_std": d_eta_std,
        "d_eta_jk_err": d_eta_jk_err,
        "d_eta_flat": d_eta_flat,
        "d_eta_flat_jk": d_eta_flat_jk,
        "eta_scans": eta_scans,
        "delta_phi_values": delta_phi_values,
        "n_simulations": n_sims,
    }

    # Weighted linear fit with Jackknife errors
    valid = np.isfinite(d_eta_mean) & (d_eta_jk_err > 0)
    if np.sum(valid) >= 2:
        weights = 1.0 / d_eta_jk_err[valid] ** 2
        coeffs = np.polyfit(
            h0_values[valid], d_eta_mean[valid], 1, w=np.sqrt(weights)
        )
        result["fit_slope"] = coeffs[0]
        result["fit_intercept"] = coeffs[1]
        result["fit_poly"] = coeffs

        # Error on slope via bootstrap
        n_boot = 1000
        slopes = np.zeros(n_boot)
        h0_v = h0_values[valid]
        d_v = d_eta_mean[valid]
        w_v = np.sqrt(weights)
        for b in range(n_boot):
            idx = np.random.choice(len(h0_v), size=len(h0_v), replace=True)
            c = np.polyfit(h0_v[idx], d_v[idx], 1, w=w_v[idx])
            slopes[b] = c[0]
        result["fit_slope_err"] = np.std(slopes)
        result["fit_slope_16"] = np.percentile(slopes, 16)
        result["fit_slope_84"] = np.percentile(slopes, 84)
    else:
        result["fit_slope"] = np.nan
        result["fit_intercept"] = np.nan
        result["fit_poly"] = None
        result["fit_slope_err"] = np.nan
        result["fit_slope_16"] = np.nan
        result["fit_slope_84"] = np.nan

    return result


def predict_d_eta(h0, fit_result):
    """Predicts d_eta for a given H0 value."""
    if fit_result["fit_poly"] is not None:
        return np.polyval(fit_result["fit_poly"], h0)
    return np.nan


def hubble_tension_signature(fit_result, h0_planck=67.4, h0_shoes=73.0):
    """Computes the resonance field signature of the Hubble tension.
    PUBLICATION VERSION with error propagation.

    Returns
    -------
    dict with:
        d_eta_planck / d_eta_shoes  : Predicted values
        delta_d_eta                 : Difference
        delta_d_eta_err             : Error (via slope error)
        relative_shift              : Relative shift [%]
        slope / slope_err           : Slope + error
    """
    d_planck = predict_d_eta(h0_planck, fit_result)
    d_shoes = predict_d_eta(h0_shoes, fit_result)
    delta = d_shoes - d_planck
    rel = (delta / d_planck * 100) if d_planck != 0 else np.nan

    # Error on Delta d_eta = slope * (H0_shoes - H0_planck)
    delta_h0 = h0_shoes - h0_planck
    slope_err = fit_result.get("fit_slope_err", np.nan)
    delta_err = slope_err * delta_h0 if np.isfinite(slope_err) else np.nan

    return {
        "h0_planck": h0_planck,
        "h0_shoes": h0_shoes,
        "d_eta_planck": d_planck,
        "d_eta_shoes": d_shoes,
        "delta_d_eta": delta,
        "delta_d_eta_err": delta_err,
        "relative_shift": rel,
        "slope": fit_result["fit_slope"],
        "slope_err": slope_err,
    }


def export_results(fit_result, filepath="h0_scan_results.csv"):
    """Exports the scan results as CSV.
    PUBLICATION VERSION with Jackknife errors.
    """
    h0 = fit_result["h0_values"]
    adot0 = fit_result["adot0_values"]
    d_eta = fit_result["d_eta_mean"]
    d_std = fit_result["d_eta_std"]
    d_jk = fit_result["d_eta_jk_err"]

    header = "H0_kmsMpc,adot0,d_eta_mean,d_eta_std,d_eta_jk_err"
    data = np.column_stack([h0, adot0, d_eta, d_std, d_jk])
    np.savetxt(filepath, data, delimiter=",", header=header, comments="",
               fmt=["%.2f", "%.6f", "%.6f", "%.6f", "%.6f"])
