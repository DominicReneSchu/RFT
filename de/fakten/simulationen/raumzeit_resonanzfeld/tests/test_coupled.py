"""Unit-Tests fuer core/coupled_flrw.py"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.coupled_flrw import coupled_flrw_sim, scan_phase_coupling


def test_coupled_dimensions():
    sol, res = coupled_flrw_sim(t_span=(0, 5), t_eval=np.linspace(0, 5, 50))
    assert sol.y.shape[0] == 6
    assert sol.y.shape[1] == 50

def test_coupled_all_finite():
    sol, res = coupled_flrw_sim(t_span=(0, 20))
    assert np.all(np.isfinite(sol.y))

def test_coupled_scale_factor_positive():
    sol, res = coupled_flrw_sim(t_span=(0, 20))
    assert np.all(sol.y[4] > 0)

def test_coupled_fields_oscillate():
    sol, res = coupled_flrw_sim(t_span=(0, 20))
    eps1 = sol.y[0]; eps2 = sol.y[2]
    assert np.any(eps1 > 0) and np.any(eps1 < 0)
    assert np.any(eps2 > 0) and np.any(eps2 < 0)

def test_coupled_resonance_max():
    sol, res = coupled_flrw_sim(delta_phi_0=0.0, t_span=(0, 20))
    eta = res["eta_theorie"]
    assert np.mean(eta) > 0.8

def test_coupled_antiresonance_min():
    sol, res = coupled_flrw_sim(delta_phi_0=np.pi, t_span=(0, 20))
    eta = res["eta_theorie"]
    n = len(eta)
    assert np.mean(eta[n//2:]) < 0.5

def test_coupled_cos2_monotone():
    scan = scan_phase_coupling(
        delta_phi_values=np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]),
        t_span=(0, 20),
    )
    eta_sim = scan["eta_mean"]
    for i in range(len(eta_sim) - 1):
        assert eta_sim[i] >= eta_sim[i + 1] - 0.15

def test_coupled_custom_params():
    sol, res = coupled_flrw_sim(
        eps1_0=0.5, eps2_0=0.2, delta_phi_0=np.pi/3,
        m=0.5, lmbda=0.05, alpha=0.3, kappa=2.0, g=0.1,
        t_span=(0, 10), t_eval=np.linspace(0, 10, 100),
    )
    assert sol.y.shape == (6, 100)
    assert np.all(np.isfinite(sol.y))


def run_all_tests():
    tests = [
        test_coupled_dimensions, test_coupled_all_finite,
        test_coupled_scale_factor_positive, test_coupled_fields_oscillate,
        test_coupled_resonance_max, test_coupled_antiresonance_min,
        test_coupled_cos2_monotone, test_coupled_custom_params,
    ]
    passed = failed = 0
    print("Gekoppeltes FLRW — Unit-Tests")
    print("=" * 50)
    for t in tests:
        try:
            t(); print(f"  ok {t.__name__}"); passed += 1
        except Exception as e:
            print(f"  FAIL {t.__name__}: {e}"); failed += 1
    print("=" * 50)
    print(f"{passed} bestanden, {failed} fehlgeschlagen von {len(tests)}")
    return failed == 0

if __name__ == "__main__":
    sys.exit(0 if run_all_tests() else 1)
