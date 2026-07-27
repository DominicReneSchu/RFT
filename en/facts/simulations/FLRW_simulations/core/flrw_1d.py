"""
1D FLRW resonance field simulation

Time evolution of a scalar resonance field ε(t) coupled to
the cosmological scale factor a(t) via modified
Friedmann equations.

Physical context:
    - Klein–Gordon equation with Ricci coupling (established physics)
    - Non-minimal coupling α·R·ε² (scalar–tensor theory)
    - Potential V(ε) = ½m²ε² + ¼λε⁴

Axiom reference:
    - A1: The field ε(t) oscillates (oscillation in the potential)
    - A4: The coupling α modulates the energy transfer
          between field and spacetime

Dependencies: numpy, scipy
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
    """Solves the coupled field equation + Friedmann equation.

    Parameters
    ----------
    eps0 : float
        Initial value of the resonance field ε(0)
    epsdot0 : float
        Initial velocity dε/dt(0)
    a0 : float
        Initial value of the scale factor a(0)
    adot0 : float
        Initial expansion rate da/dt(0)
    m : float
        Mass of the scalar field
    lmbda : float
        Self-coupling constant (λε⁴ term)
    alpha : float
        Non-minimal coupling to spacetime
    kappa : float
        Gravitational coupling constant (κ = 8πG)

    Returns
    -------
    sol : OdeSolution
        Solution with sol.y = [ε, dε/dt, a, da/dt]
    V : callable
        Potential function V(ε)
    """

    def V(eps):
        """Potential: V(ε) = ½m²ε² + ¼λε⁴"""
        return 0.5 * m**2 * eps**2 + 0.25 * lmbda * eps**4

    def Vp(eps):
        """dV/dε = m²ε + λε³"""
        return m**2 * eps + lmbda * eps**3

    def rhs(t, y):
        eps, epsdot, a, adot = y
        H = adot / a  # Hubble parameter
        rho_eps = 0.5 * epsdot**2 + V(eps)

        # Modified Friedmann equation: H² = κ/3 · ρ / (1 + αε²)
        H2 = kappa / 3 * rho_eps / (1 + alpha * eps**2)

        # Second Friedmann equation (acceleration)
        p_eps = 0.5 * epsdot**2 - V(eps)  # Pressure
        addot = -a * kappa / 6 * (rho_eps + 3 * p_eps) / (1 + alpha * eps**2)

        # Ricci scalar
        R = 6 * (addot / a + H**2)

        # Klein–Gordon with Hubble friction and Ricci coupling
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
