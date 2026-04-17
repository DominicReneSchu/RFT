"""
Unit tests for core/flrw_1d.py

Execution (recommended):
    cd FLRW_simulations
    pytest tests/test_flrw_1d.py -v

Execution (standalone, without pytest):
    cd FLRW_simulations
    python tests/test_flrw_1d.py
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.flrw_1d import flrw_1d_sim


def test_flrw_1d_dimensions():
    """Solution has the correct dimension."""
    sol, V = flrw_1d_sim(t_span=(0, 1), t_eval=np.linspace(0, 1, 10))
    assert sol.y.shape == (4, 10)


def test_flrw_1d_scale_factor_positive():
    """Scale factor remains positive."""
    sol, V = flrw_1d_sim(
        eps0=0.3, adot0=0.3,
        t_span=(0, 10), t_eval=np.linspace(0, 10, 200),
    )
    assert np.all(sol.y[2] > 0)


def test_flrw_1d_energy_finite():
    """Total energy remains finite."""
    sol, V = flrw_1d_sim(
        eps0=0.3, adot0=0.3,
        t_span=(0, 10), t_eval=np.linspace(0, 10, 200),
    )
    eps, epsdot, a = sol.y[0], sol.y[1], sol.y[2]
    rho_eff = (0.5 * epsdot**2 + V(eps)) / (1 + 0.5 * eps**2)
    energy = rho_eff * a**3
    assert np.all(np.isfinite(energy))


def test_flrw_1d_energy_conservation():
    """Relative energy change remains below 20%."""
    sol, V = flrw_1d_sim(
        eps0=0.3, adot0=0.3,
        t_span=(0, 10),
        t_eval=np.linspace(0, 10, 1000),
        rtol=1e-12, atol=1e-14,
    )
    eps, epsdot, a = sol.y[0], sol.y[1], sol.y[2]
    rho_eff = (0.5 * epsdot**2 + V(eps)) / (1 + 0.5 * eps**2)
    energy = rho_eff * a**3
    delta = np.abs(energy - energy[0]) / energy[0]
    assert np.max(delta) < 0.2, f"Max ΔE/E₀ = {np.max(delta):.4f}"


def test_flrw_1d_field_oscillates():
    """The resonance field ε(t) changes sign (oscillation)."""
    sol, V = flrw_1d_sim(eps0=0.3, adot0=0.3, t_span=(0, 20))
    eps = sol.y[0]
    assert np.any(eps > 0) and np.any(eps < 0), "Field does not oscillate"


def test_flrw_1d_custom_parameters():
    """Simulation runs with modified parameters."""
    sol, V = flrw_1d_sim(
        eps0=0.5, epsdot0=0.1, a0=2.0, adot0=0.5,
        m=0.5, lmbda=0.05, alpha=0.3, kappa=2.0,
        t_span=(0, 5), t_eval=np.linspace(0, 5, 100),
    )
    assert sol.y.shape == (4, 100)
    assert np.all(np.isfinite(sol.y))


# === Standalone runner ===

def run_all_tests():
    tests = [
        test_flrw_1d_dimensions,
        test_flrw_1d_scale_factor_positive,
        test_flrw_1d_energy_finite,
        test_flrw_1d_energy_conservation,
        test_flrw_1d_field_oscillates,
        test_flrw_1d_custom_parameters,
    ]

    passed = 0
    failed = 0
    errors = []

    print("FLRW 1D — Unit tests")
    print("=" * 50)

    for test in tests:
        name = test.__name__
        try:
            test()
            print(f"  ✓ {name}")
            passed += 1
        except Exception as e:
            print(f"  ✗ {name}: {e}")
            failed += 1
            errors.append((name, str(e)))

    print("=" * 50)
    print(f"Result: {passed} passed, {failed} failed "
          f"out of {len(tests)} tests")

    if errors:
        print("\nFailed tests:")
        for name, err in errors:
            print(f"  {name}: {err}")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
