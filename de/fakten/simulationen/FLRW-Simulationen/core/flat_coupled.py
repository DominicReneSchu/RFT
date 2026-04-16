"""
Gekoppelte Zwei-Feld-Simulation in FLACHER Raumzeit.
Kontrollexperiment: a = const = 1, H = 0, R = 0.
"""

import numpy as np
from scipy.integrate import solve_ivp


def flat_coupled_sim(
    eps1_0=0.3, eps2_0=0.3,
    epsdot1_0=0.0, epsdot2_0=0.0,
    delta_phi_0=0.0,
    m=1.0, lmbda=0.1, g=0.2,
    t_span=(0, 40), t_eval=None,
    rtol=1e-10, atol=1e-12,
):
    omega_0 = m
    if epsdot2_0 == 0.0 and delta_phi_0 != 0.0:
        epsdot1_0 = 0.0
        epsdot2_0 = -eps2_0 * omega_0 * np.sin(delta_phi_0)
        eps2_0 = eps2_0 * np.cos(delta_phi_0)

    def V(eps):
        return 0.5 * m**2 * eps**2 + 0.25 * lmbda * eps**4

    def Vp(eps):
        return m**2 * eps + lmbda * eps**3

    def rhs(t, y):
        eps1, epsdot1, eps2, epsdot2 = y
        epsddot1 = -Vp(eps1) - g * eps2
        epsddot2 = -Vp(eps2) - g * eps1
        return [epsdot1, epsddot1, epsdot2, epsddot2]

    y0 = [eps1_0, epsdot1_0, eps2_0, epsdot2_0]
    if t_eval is None:
        t_eval = np.linspace(*t_span, 4000)

    sol = solve_ivp(rhs, t_span, y0, t_eval=t_eval, rtol=rtol, atol=atol, method="DOP853")

    eps1 = sol.y[0]
    epsdot1 = sol.y[1]
    eps2 = sol.y[2]
    epsdot2 = sol.y[3]

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
    eta_theorie = np.cos(delta_phi / 2)**2

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

    results = {
        "delta_phi": delta_phi, "eta_theorie": eta_theorie,
        "eta_gemessen": eta_gemessen, "valid_mask": valid_mask,
        "amp1": amp1, "amp2": amp2,
        "rho1": rho1, "rho2": rho2, "V": V,
    }
    return sol, results


def scan_phase_flat(delta_phi_values=None, t_span=(0, 40), **kwargs):
    if delta_phi_values is None:
        delta_phi_values = np.linspace(0, np.pi, 20)
    eta_mean = []
    for dphi in delta_phi_values:
        sol, results = flat_coupled_sim(delta_phi_0=dphi, t_span=t_span, **kwargs)
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
        "eta_cos2": np.cos(delta_phi_values / 2)**2,
    }
