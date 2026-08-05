"""
Gekoppelte FLRW-Resonanzfeldsimulation — zwei skalare Felder.
PUBLIKATIONSVERSION — t_eval auf 12000 Punkte, parametrierbar.

Zwei Resonanzfelder e1(t) und e2(t) mit Phasendifferenz dphi(t),
gekoppelt an den kosmologischen Skalenfaktor a(t).

Zentrale Erweiterung gegenueber Standard-Scalar-Tensor-Theorie:
    Die Kopplungseffizienz zwischen den Feldern folgt
        eta(dphi) = cos^2(dphi/2)
    Dies wird NICHT postuliert, sondern ergibt sich aus der
    Interferenz zweier kohaerenter Oszillatoren im selben Potential.

RT-32 — Nichtlinearer Saettigungsterm:
    Der lambda_eps4-Parameter fuehrt einen quartischen
    Saettigungsterm in das Potential ein:
        V(eps) = 0.5*m^2*eps^2 + 0.25*lambda_field*eps^4
                               + (1/6)*lambda_eps4*eps^6
    Dieser Term modelliert nichtlineare Selbstwechselwirkung des
    Resonanzfelds (RT-32: stoerungstheoretische Erweiterung).

Abhaengigkeiten: numpy, scipy
"""

import numpy as np
from scipy.integrate import solve_ivp


def coupled_flrw_sim(
    eps1_0=0.3, eps2_0=0.3,
    epsdot1_0=0.0, epsdot2_0=0.0,
    delta_phi_0=0.0,
    a0=1.0, adot0=0.3,
    m=1.0, lmbda=0.1, alpha=0.5, kappa=1.0, g=0.2,
    lambda_eps4=0.0,
    t_span=(0, 120), t_eval=None,
    n_eval=12000,
    rtol=1e-10, atol=1e-12,
):
    """Gekoppelte FLRW-Simulation mit zwei skalaren Resonanzfeldern.

    Parameters
    ----------
    eps1_0, eps2_0 : float
        Anfangsamplituden der Felder.
    epsdot1_0, epsdot2_0 : float
        Anfangsgeschwindigkeiten.
    delta_phi_0 : float
        Initiale Phasendifferenz.
    a0, adot0 : float
        Skalenfaktor und dessen Ableitung bei t=0.
    m, lmbda, alpha, kappa, g : float
        Modellparameter.
    lambda_eps4 : float
        RT-32: Nichtlinearer Saettigungsparameter. Fuehrt den Term
        (1/6)*lambda_eps4*eps^6 in das Potential ein. Stoerungstheoretisch
        klein (|lambda_eps4| << 1); lambda_eps4=0 entspricht dem
        Standard-lambda-phi^4-Potential.
    t_span : tuple
        Integrationsintervall.
    t_eval : array or None
        Auswertungszeitpunkte. Wenn None, wird n_eval verwendet.
    n_eval : int
        Anzahl Auswertungspunkte (Standard: 12000).
    rtol, atol : float
        Relative/absolute Toleranz des Integrators.

    Returns
    -------
    sol : OdeResult
        Loesung des ODE-Systems.
    results : dict
        Abgeleitete Groessen (eta, Phasen, Energien, ...).
    """
    omega_0 = m
    if epsdot2_0 == 0.0 and delta_phi_0 != 0.0:
        epsdot1_0 = 0.0
        epsdot2_0 = -eps2_0 * omega_0 * np.sin(delta_phi_0)
        eps2_0 = eps2_0 * np.cos(delta_phi_0)

    def V(eps):
        return 0.5 * m**2 * eps**2 + 0.25 * lmbda * eps**4 + (1.0 / 6.0) * lambda_eps4 * eps**6

    def Vp(eps):
        return m**2 * eps + lmbda * eps**3 + lambda_eps4 * eps**5

    def rhs(t, y):
        eps1, epsdot1, eps2, epsdot2, a, adot = y
        H = adot / a
        rho1 = 0.5 * epsdot1**2 + V(eps1)
        rho2 = 0.5 * epsdot2**2 + V(eps2)
        rho_kopplung = g * eps1 * eps2
        rho_total = rho1 + rho2 + rho_kopplung
        eps_sq = eps1**2 + eps2**2
        denom = 1 + alpha * eps_sq
        H2 = kappa / 3 * rho_total / denom
        p1 = 0.5 * epsdot1**2 - V(eps1)
        p2 = 0.5 * epsdot2**2 - V(eps2)
        p_total = p1 + p2 + rho_kopplung
        addot = -a * kappa / 6 * (rho_total + 3 * p_total) / denom
        R = 6 * (addot / a + H**2)
        epsddot1 = -3 * H * epsdot1 - Vp(eps1) - g * eps2 + alpha / kappa * R * eps1
        epsddot2 = -3 * H * epsdot2 - Vp(eps2) - g * eps1 + alpha / kappa * R * eps2
        return [epsdot1, epsddot1, epsdot2, epsddot2, adot, addot]

    y0 = [eps1_0, epsdot1_0, eps2_0, epsdot2_0, a0, adot0]
    if t_eval is None:
        t_eval = np.linspace(*t_span, n_eval)

    sol = solve_ivp(
        rhs, t_span, y0, t_eval=t_eval,
        rtol=rtol, atol=atol, method="DOP853",
    )

    eps1 = sol.y[0]
    epsdot1 = sol.y[1]
    eps2 = sol.y[2]
    epsdot2 = sol.y[3]
    a = sol.y[4]
    adot = sol.y[5]

    from scipy.signal import hilbert
    analytic1 = hilbert(eps1)
    analytic2 = hilbert(eps2)
    amp1 = np.abs(analytic1)
    amp2 = np.abs(analytic2)
    phase1 = np.unwrap(np.angle(analytic1))
    phase2 = np.unwrap(np.angle(analytic2))
    delta_phi = phase2 - phase1
    amp_max = max(np.max(amp1), np.max(amp2))
    amp_threshold = 0.01 * amp_max
    valid_mask = (amp1 > amp_threshold) & (amp2 > amp_threshold)
    eta_theorie = np.cos(delta_phi / 2) ** 2

    window = max(int(2 * np.pi / m / (sol.t[1] - sol.t[0])), 20)
    n = len(eps1)
    eta_gemessen = np.full(n, np.nan)
    for i in range(n):
        lo = max(0, i - window // 2)
        hi = min(n, i + window // 2)
        seg1 = eps1[lo:hi]
        seg2 = eps2[lo:hi]
        cross = np.mean(seg1 * seg2)
        auto1 = np.mean(seg1**2)
        auto2 = np.mean(seg2**2)
        d = np.sqrt(auto1 * auto2)
        if d > 1e-20:
            corr = cross / d
            eta_gemessen[i] = 0.5 * (1 + corr)

    rho1 = 0.5 * epsdot1**2 + V(eps1)
    rho2 = 0.5 * epsdot2**2 + V(eps2)
    kreuzterm = g * eps1 * eps2
    rho_total = rho1 + rho2 + kreuzterm

    results = {
        "delta_phi": delta_phi, "eta_theorie": eta_theorie,
        "eta_gemessen": eta_gemessen, "valid_mask": valid_mask,
        "amp1": amp1, "amp2": amp2,
        "rho1": rho1, "rho2": rho2,
        "rho_kopplung": kreuzterm, "rho_total": rho_total,
        "H": adot / a, "V": V,
    }
    return sol, results


def scan_phase_coupling(delta_phi_values=None, t_span=(0, 120), **kwargs):
    """Phasenscan ueber delta_phi_0.

    Parameters
    ----------
    delta_phi_values : array or None
        Phasendifferenzen. Default: 30 Werte, 0 bis pi.
    t_span : tuple
        Integrationsintervall.
    **kwargs : dict
        Weitere Parameter fuer coupled_flrw_sim.
    """
    if delta_phi_values is None:
        delta_phi_values = np.linspace(0, np.pi, 30)
    eta_mean = []
    for dphi in delta_phi_values:
        sol, results = coupled_flrw_sim(
            delta_phi_0=dphi, t_span=t_span, **kwargs,
        )
        mask = results["valid_mask"]
        eta = results["eta_gemessen"]
        combined_mask = mask & np.isfinite(eta)
        if np.any(combined_mask):
            eta_mean.append(np.mean(eta[combined_mask]))
        else:
            eta_mean.append(np.nan)
    return {
        "delta_phi_values": np.array(delta_phi_values),
        "eta_mean": np.array(eta_mean),
        "eta_cos2": np.cos(delta_phi_values / 2) ** 2,
    }


def scan_lambda_eps4(
    lambda_eps4_values=None,
    delta_phi_0=np.pi / 4,
    t_span=(0, 120),
    **kwargs,
):
    """RT-32: Stoerungstheoretischer Scan des lambda_eps4-Parameters.

    Quantifiziert den Effekt des nichtlinearen Saettigungsterms auf die
    mittlere Kopplungseffizienz eta(Δφ) = cos²(Δφ/2).

    Parameters
    ----------
    lambda_eps4_values : array or None
        Zu scannende lambda_eps4-Werte. Default: 9 Werte 0..0.4.
    delta_phi_0 : float
        Feste Phasendifferenz fuer den Scan. Default: pi/4.
    t_span : tuple
        Integrationsintervall.
    **kwargs : dict
        Weitere Parameter fuer coupled_flrw_sim.

    Returns
    -------
    dict mit Schluesseln:
        lambda_eps4_values : array
        eta_mean           : array, mittlere gemessene eta
        eta_cos2_ref       : float, cos^2-Referenzwert fuer delta_phi_0
        d_eta              : array, Abweichung eta_mean − eta_cos2_ref
    """
    if lambda_eps4_values is None:
        lambda_eps4_values = np.linspace(0.0, 0.4, 9)
    eta_mean = []
    eta_cos2_ref = np.cos(delta_phi_0 / 2) ** 2
    for lep4 in lambda_eps4_values:
        sol, results = coupled_flrw_sim(
            delta_phi_0=delta_phi_0, t_span=t_span,
            lambda_eps4=lep4, **kwargs,
        )
        mask = results["valid_mask"]
        eta = results["eta_gemessen"]
        combined_mask = mask & np.isfinite(eta)
        if np.any(combined_mask):
            eta_mean.append(np.mean(eta[combined_mask]))
        else:
            eta_mean.append(np.nan)
    eta_mean = np.array(eta_mean)
    return {
        "lambda_eps4_values": np.array(lambda_eps4_values),
        "eta_mean": eta_mean,
        "eta_cos2_ref": eta_cos2_ref,
        "d_eta": eta_mean - eta_cos2_ref,
    }