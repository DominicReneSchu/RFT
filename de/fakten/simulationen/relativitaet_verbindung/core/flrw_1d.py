"""
1D FLRW-Resonanzfeldsimulation

Zeitentwicklung eines skalaren Resonanzfelds ε(t) gekoppelt an
den kosmologischen Skalenfaktor a(t) über modifizierte
Friedmann-Gleichungen.

Physikalischer Kontext:
    - Klein-Gordon-Gleichung mit Ricci-Kopplung (etablierte Physik)
    - Nichtminimale Kopplung α·R·ε² (Scalar-Tensor-Theorie)
    - Potential V(ε) = ½m²ε² + ¼λε⁴

Axiom-Bezug:
    - A1: Das Feld ε(t) schwingt (Oszillation im Potential)
    - A4: Die Kopplung α moduliert den Energietransfer
          zwischen Feld und Raumzeit

Abhängigkeiten: numpy, scipy
"""

import numpy as np
from scipy.integrate import solve_ivp


def flrw_1d_sim(
    eps0=0.5,
    epsdot0=0.0,
    a0=1.0,
    adot0=0.1,
    m=1.0,
    lmbda=0.1,
    alpha=0.5,
    kappa=1.0,
    t_span=(0, 30),
    t_eval=None,
    rtol=1e-8,
    atol=1e-10,
):
    """Löst die gekoppelte Feldgleichung + Friedmann-Gleichung.

    Parameters
    ----------
    eps0 : float
        Anfangswert des Resonanzfelds ε(0)
    epsdot0 : float
        Anfangsgeschwindigkeit dε/dt(0)
    a0 : float
        Anfangswert des Skalenfaktors a(0)
    adot0 : float
        Anfangsexpansionsrate da/dt(0)
    m : float
        Masse des skalaren Felds
    lmbda : float
        Selbstkopplungskonstante (λε⁴-Term)
    alpha : float
        Nichtminimale Kopplung an die Raumzeit
    kappa : float
        Gravitationskopplungskonstante (κ = 8πG)

    Returns
    -------
    sol : OdeSolution
        Lösung mit sol.y = [ε, dε/dt, a, da/dt]
    V : callable
        Potentialfunktion V(ε)
    """

    def V(eps):
        """Potential: V(ε) = ½m²ε² + ¼λε⁴"""
        return 0.5 * m**2 * eps**2 + 0.25 * lmbda * eps**4

    def Vp(eps):
        """dV/dε = m²ε + λε³"""
        return m**2 * eps + lmbda * eps**3

    def rhs(t, y):
        eps, epsdot, a, adot = y
        H = adot / a  # Hubble-Parameter
        rho_eps = 0.5 * epsdot**2 + V(eps)

        # Modifizierte Friedmann-Gleichung: H² = κ/3 · ρ / (1 + αε²)
        H2 = kappa / 3 * rho_eps / (1 + alpha * eps**2)

        # Zweite Friedmann-Gleichung (Beschleunigung)
        p_eps = 0.5 * epsdot**2 - V(eps)  # Druck
        addot = -a * kappa / 6 * (rho_eps + 3 * p_eps) / (1 + alpha * eps**2)

        # Ricci-Skalar
        R = 6 * (addot / a + H**2)

        # Klein-Gordon mit Hubble-Reibung und Ricci-Kopplung
        epsddot = -3 * H * epsdot - Vp(eps) + alpha / kappa * R * eps

        return [epsdot, epsddot, adot, addot]

    y0 = [eps0, epsdot0, a0, adot0]
    if t_eval is None:
        t_eval = np.linspace(*t_span, 2000)

    sol = solve_ivp(
        rhs, t_span, y0,
        t_eval=t_eval, rtol=rtol, atol=atol,
        method="DOP853"
    )
    return sol, V