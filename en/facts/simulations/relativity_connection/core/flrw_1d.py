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
    t_span=(0,30),
    t_eval=None,
    rtol=1e-8,
    atol=1e-10,
):
    def V(eps):  # Potential
        return 0.5 * m**2 * eps**2 + 0.25 * lmbda * eps**4

    def Vp(eps): # Ableitung
        return m**2 * eps + lmbda * eps**3

    def ricci_scalar(a, adot, addot):
        return 6 * (addot/a + (adot/a)**2)

    def rhs(t, y):
        eps, epsdot, a, adot = y
        rho_eps = 0.5*epsdot**2 + V(eps)
        H2 = kappa/3 * rho_eps / (1 + alpha*eps**2)
        H = np.sqrt(np.abs(H2)) * np.sign(adot)
        addot = a * H2
        R = ricci_scalar(a, adot, addot)
        epsddot = -3 * adot/a * epsdot - Vp(eps) + alpha/kappa * R * eps
        return [epsdot, epsddot, adot, addot]

    y0 = [eps0, epsdot0, a0, adot0]
    if t_eval is None:
        t_eval = np.linspace(*t_span, 2000)
    sol = solve_ivp(rhs, t_span, y0, t_eval=t_eval, rtol=rtol, atol=atol, method="DOP853")
    return sol, V