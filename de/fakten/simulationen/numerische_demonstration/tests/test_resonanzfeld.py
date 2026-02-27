"""
Unit-Tests für resonanzfeld.py

Testet Resonanzenergie, Kopplungseffizienz und Resonanzentropie.

Ausführung (empfohlen):
    cd numerische_demonstration
    pip install pytest
    pytest tests/

Ausführung (standalone, ohne pytest):
    cd numerische_demonstration
    python tests/test_resonanzfeld.py
"""

import numpy as np
import sys
import os

# Elternverzeichnis zum Pfad hinzufügen
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from resonanzfeld import (
    berechne_resonanzenergie,
    berechne_kopplungseffizienz,
    berechne_resonanzentropie,
    plot_resonanzfeld,
)

# pytest optional importieren
try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False


# === Hilfsfunktion für standalone-Modus ===

def assert_close(actual, expected, rtol=1e-6, atol=0, msg=""):
    """numpy.testing.assert_allclose Wrapper."""
    if not np.allclose(actual, expected, rtol=rtol, atol=atol):
        raise AssertionError(
            f"FAIL: {msg}\n"
            f"  erwartet: {expected}\n"
            f"  erhalten: {actual}")


# === Resonanzenergie ===

def test_resonanzenergie_shape():
    A = np.array([0.5, 1.0, 2.0])
    tau = np.array([0.5, 1.0])
    E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
    assert E_res.shape == (3, 2)
    assert tau_grid.shape == (3, 2)
    assert A_grid.shape == (3, 2)


def test_resonanzenergie_positive():
    A = np.array([0.5, 1.0, 2.0])
    tau = np.array([0.5, 1.0])
    E_res, _, _ = berechne_resonanzenergie(A, tau)
    assert np.all(E_res > 0)


def test_resonanzenergie_amplitude_monotonie():
    """Höhere Amplitude → höhere Resonanzenergie."""
    A = np.array([0.5, 1.0, 2.0])
    tau = np.array([1.0])
    E_res, _, _ = berechne_resonanzenergie(A, tau)
    assert E_res[0, 0] < E_res[1, 0] < E_res[2, 0]


def test_resonanzenergie_maximum():
    """Bei sin(τ) = 0 ist ω_ext = ω₀ → E_res = A."""
    A = np.array([1.0, 2.0, 3.0])
    tau = np.array([np.pi])  # sin(π) ≈ 0
    E_res, _, _ = berechne_resonanzenergie(A, tau)
    np.testing.assert_allclose(E_res[:, 0], A, rtol=1e-6)


def test_resonanzenergie_negative_A():
    """Negative Amplitude → ValueError."""
    try:
        berechne_resonanzenergie(np.array([-1.0, 1.0]),
                                  np.array([1.0, 2.0]))
        raise AssertionError("ValueError erwartet")
    except ValueError:
        pass


def test_resonanzenergie_negative_tau():
    """Negativer Verstimmungsparameter → ValueError."""
    try:
        berechne_resonanzenergie(np.array([1.0, 2.0]),
                                  np.array([-0.1, 0.5]))
        raise AssertionError("ValueError erwartet")
    except ValueError:
        pass


def test_resonanzenergie_2d_input():
    """2D-Input → ValueError."""
    try:
        berechne_resonanzenergie(np.array([[1.0, 2.0]]),
                                  np.array([1.0]))
        raise AssertionError("ValueError erwartet")
    except ValueError:
        pass


# === Kopplungseffizienz ===

def test_kopplungseffizienz_range():
    """ε ∈ (0, 1]."""
    A = np.linspace(0.1, 5, 50)
    tau = np.linspace(0.1, 5, 50)
    E_res, _, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    assert np.all(eps > 0)
    assert np.all(eps <= 1.0)


def test_kopplungseffizienz_resonanz():
    """Bei exakter Resonanz: ε = 1."""
    A = np.array([1.0])
    tau = np.array([np.pi])
    E_res, _, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    np.testing.assert_allclose(eps[0, 0], 1.0, rtol=1e-6)


def test_kopplungseffizienz_amplitude_unabhaengig():
    """ε ist unabhängig von der Amplitude."""
    A = np.array([0.5, 1.0, 5.0])
    tau = np.array([1.0])
    E_res, _, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    np.testing.assert_allclose(eps[0, 0], eps[1, 0], rtol=1e-6)
    np.testing.assert_allclose(eps[1, 0], eps[2, 0], rtol=1e-6)


# === Resonanzentropie ===

def test_entropie_shape():
    eps = np.array([[0.5, 0.8], [0.2, 0.9]])
    S = berechne_resonanzentropie(eps)
    assert S.shape == eps.shape


def test_entropie_non_negative():
    """S ≥ 0 für ε ∈ (0, 1]."""
    eps = np.linspace(0.01, 1.0, 100)
    S = berechne_resonanzentropie(eps)
    assert np.all(S >= 0)
    assert np.all(np.isfinite(S))


def test_entropie_maximum_bei_inverse_e():
    """S ist maximal bei ε = 1/e."""
    eps = np.linspace(0.01, 1.0, 10000)
    S = berechne_resonanzentropie(eps)
    idx_max = np.argmax(S)
    eps_at_max = eps[idx_max]
    np.testing.assert_allclose(eps_at_max, 1 / np.e, atol=0.001)


def test_entropie_null_an_grenzen():
    """S = 0 bei ε = 1 und S → 0 für ε → 0."""
    S_at_one = berechne_resonanzentropie(np.array([1.0]))
    assert np.isclose(S_at_one[0], 0.0, atol=1e-10)

    S_near_zero = berechne_resonanzentropie(np.array([1e-6]))
    assert S_near_zero[0] < 0.001


def test_entropie_monotonie():
    """Für ε > 1/e: höhere ε → kleinere S."""
    eps = np.array([0.5, 0.9])
    S = berechne_resonanzentropie(eps)
    assert S[0] > S[1]


# === Plot (Smoke Test) ===

def test_plot_runs():
    """Plot erzeugen und als Datei speichern."""
    import tempfile
    A = np.linspace(0.1, 1, 10)
    tau = np.linspace(0.1, 1, 10)
    E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    S = berechne_resonanzentropie(eps)
    with tempfile.TemporaryDirectory() as tmp:
        savefile = os.path.join(tmp, "plot.png")
        plot_resonanzfeld(tau_grid, A_grid, E_res, eps, S,
                          save_path=savefile, show=False)
        assert os.path.exists(savefile)


# === Standalone-Runner ===

def run_all_tests():
    """Führt alle Tests ohne pytest aus."""
    tests = [
        test_resonanzenergie_shape,
        test_resonanzenergie_positive,
        test_resonanzenergie_amplitude_monotonie,
        test_resonanzenergie_maximum,
        test_resonanzenergie_negative_A,
        test_resonanzenergie_negative_tau,
        test_resonanzenergie_2d_input,
        test_kopplungseffizienz_range,
        test_kopplungseffizienz_resonanz,
        test_kopplungseffizienz_amplitude_unabhaengig,
        test_entropie_shape,
        test_entropie_non_negative,
        test_entropie_maximum_bei_inverse_e,
        test_entropie_null_an_grenzen,
        test_entropie_monotonie,
        test_plot_runs,
    ]

    passed = 0
    failed = 0
    errors = []

    print("Resonanzfeldtheorie — Unit-Tests")
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