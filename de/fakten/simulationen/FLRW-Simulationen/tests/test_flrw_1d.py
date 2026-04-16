"""
Unit-Tests für core/flrw_1d.py

Ausführung (empfohlen):
    cd relativitaet_verbindung
    pytest tests/test_flrw_1d.py -v

Ausführung (standalone, ohne pytest):
    cd relativitaet_verbindung
    python tests/test_flrw_1d.py
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.flrw_1d import flrw_1d_sim


def test_flrw_1d_dimensions():
    """Lösung hat die korrekte Dimension."""
    sol, V = flrw_1d_sim(t_span=(0, 1), t_eval=np.linspace(0, 1, 10))
    assert sol.y.shape == (4, 10)


def test_flrw_1d_scale_factor_positive():
    """Skalenfaktor bleibt positiv."""
    sol, V = flrw_1d_sim(
        eps0=0.3, adot0=0.3,
        t_span=(0, 10), t_eval=np.linspace(0, 10, 200),
    )
    assert np.all(sol.y[2] > 0)


def test_flrw_1d_energy_finite():
    """Gesamtenergie bleibt endlich."""
    sol, V = flrw_1d_sim(
        eps0=0.3, adot0=0.3,
        t_span=(0, 10), t_eval=np.linspace(0, 10, 200),
    )
    eps, epsdot, a = sol.y[0], sol.y[1], sol.y[2]
    rho_eff = (0.5 * epsdot**2 + V(eps)) / (1 + 0.5 * eps**2)
    energie = rho_eff * a**3
    assert np.all(np.isfinite(energie))


def test_flrw_1d_energy_conservation():
    """Relative Energieänderung bleibt unter 20%."""
    sol, V = flrw_1d_sim(
        eps0=0.3, adot0=0.3,
        t_span=(0, 10),
        t_eval=np.linspace(0, 10, 1000),
        rtol=1e-12, atol=1e-14,
    )
    eps, epsdot, a = sol.y[0], sol.y[1], sol.y[2]
    rho_eff = (0.5 * epsdot**2 + V(eps)) / (1 + 0.5 * eps**2)
    energie = rho_eff * a**3
    delta = np.abs(energie - energie[0]) / energie[0]
    assert np.max(delta) < 0.2, f"Max ΔE/E₀ = {np.max(delta):.4f}"


def test_flrw_1d_field_oscillates():
    """Das Resonanzfeld ε(t) wechselt das Vorzeichen (Oszillation)."""
    sol, V = flrw_1d_sim(eps0=0.3, adot0=0.3, t_span=(0, 20))
    eps = sol.y[0]
    assert np.any(eps > 0) and np.any(eps < 0), "Feld oszilliert nicht"


def test_flrw_1d_custom_parameters():
    """Simulation läuft mit veränderten Parametern."""
    sol, V = flrw_1d_sim(
        eps0=0.5, epsdot0=0.1, a0=2.0, adot0=0.5,
        m=0.5, lmbda=0.05, alpha=0.3, kappa=2.0,
        t_span=(0, 5), t_eval=np.linspace(0, 5, 100),
    )
    assert sol.y.shape == (4, 100)
    assert np.all(np.isfinite(sol.y))


# === Standalone-Runner ===

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

    print("FLRW 1D — Unit-Tests")
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
    print(f"Ergebnis: {passed} bestanden, {failed} fehlgeschlagen "
          f"von {len(tests)} Tests")

    if errors:
        print("\nFehlgeschlagene Tests:")
        for name, err in errors:
            print(f"  {name}: {err}")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)