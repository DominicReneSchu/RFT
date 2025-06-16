import numpy as np
from core.flrw_1d import flrw_1d_sim

def test_flrw_1d_basic():
    sol, V = flrw_1d_sim(t_span=(0, 1), t_eval=np.linspace(0,1,10))
    # Test: Lösung hat die richtige Dimension
    assert sol.y.shape[1] == 10
    # Test: Skalenfaktor wächst oder bleibt positiv
    assert np.all(sol.y[2] > 0)
    # Test: Energie bleibt endlich
    eps, epsdot, a = sol.y[0], sol.y[1], sol.y[2]
    rho_eps = 0.5*epsdot**2 + V(eps)
    energie_gesamt = rho_eps * a**3
    assert np.all(np.isfinite(energie_gesamt))
