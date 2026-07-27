"""
Unit tests for numerical_demonstration.py

Tests resonance energy, coupling efficiency and resonance entropy.

Recommended usage:
    cd numerical_demonstration
    pip install pytest
    pytest tests/

Standalone usage (without pytest):
    cd numerical_demonstration
    python tests/test_numerical_demonstration.py
"""

from __future__ import annotations

import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from numerical_demonstration import (
    berechne_resonanzenergie,
    berechne_kopplungseffizienz,
    berechne_resonanzentropie,
    plot_numerische_demonstration,
)

# Import pytest optionally
try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False


# === Helper for standalone mode ===

def assert_close(actual: float | np.ndarray, expected: float | np.ndarray, rtol: float = 1e-6, atol: float = 0, msg: str = "") -> None:
    """numpy.testing.assert_allclose wrapper."""
    if not np.allclose(actual, expected, rtol=rtol, atol=atol):
        raise AssertionError(
            f"FAIL: {msg}\n"
            f"  expected: {expected}\n"
            f"  received: {actual}")


# === Resonance energy ===

def test_resonanzenergie_shape() -> None:
    A = np.array([0.5, 1.0, 2.0])
    tau = np.array([0.5, 1.0])
    E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
    assert E_res.shape == (3, 2)
    assert tau_grid.shape == (3, 2)
    assert A_grid.shape == (3, 2)


def test_resonanzenergie_positive() -> None:
    A = np.array([0.5, 1.0, 2.0])
    tau = np.array([0.5, 1.0])
    E_res, _, _ = berechne_resonanzenergie(A, tau)
    assert np.all(E_res > 0)


def test_resonanzenergie_amplitude_monotonie() -> None:
    """Higher amplitude → higher resonance energy."""
    A = np.array([0.5, 1.0, 2.0])
    tau = np.array([1.0])
    E_res, _, _ = berechne_resonanzenergie(A, tau)
    assert E_res[0, 0] < E_res[1, 0] < E_res[2, 0]


def test_resonanzenergie_maximum() -> None:
    """At sin(τ) = 0, ω_ext = ω₀ → E_res = A."""
    A = np.array([1.0, 2.0, 3.0])
    tau = np.array([np.pi])  # sin(π) ≈ 0
    E_res, _, _ = berechne_resonanzenergie(A, tau)
    np.testing.assert_allclose(E_res[:, 0], A, rtol=1e-6)


def test_resonanzenergie_negative_A() -> None:
    """Negative amplitude → ValueError."""
    try:
        berechne_resonanzenergie(np.array([-1.0, 1.0]),
                                  np.array([1.0, 2.0]))
        raise AssertionError("ValueError expected")
    except ValueError:
        pass


def test_resonanzenergie_negative_tau() -> None:
    """Negative detuning parameter → ValueError."""
    try:
        berechne_resonanzenergie(np.array([1.0, 2.0]),
                                  np.array([-0.1, 0.5]))
        raise AssertionError("ValueError expected")
    except ValueError:
        pass


def test_resonanzenergie_2d_input() -> None:
    """2D input → ValueError."""
    try:
        berechne_resonanzenergie(np.array([[1.0, 2.0]]),
                                  np.array([1.0]))
        raise AssertionError("ValueError expected")
    except ValueError:
        pass


# === Coupling efficiency ===

def test_kopplungseffizienz_range() -> None:
    """ε ∈ (0, 1]."""
    A = np.linspace(0.1, 5, 50)
    tau = np.linspace(0.1, 5, 50)
    E_res, _, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    assert np.all(eps > 0)
    assert np.all(eps <= 1.0)


def test_kopplungseffizienz_resonanz() -> None:
    """At exact resonance: ε = 1."""
    A = np.array([1.0])
    tau = np.array([np.pi])
    E_res, _, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    np.testing.assert_allclose(eps[0, 0], 1.0, rtol=1e-6)


def test_kopplungseffizienz_amplitude_unabhaengig() -> None:
    """ε is independent of amplitude."""
    A = np.array([0.5, 1.0, 5.0])
    tau = np.array([1.0])
    E_res, _, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    np.testing.assert_allclose(eps[0, 0], eps[1, 0], rtol=1e-6)
    np.testing.assert_allclose(eps[1, 0], eps[2, 0], rtol=1e-6)


# === Resonance entropy ===

def test_entropie_shape() -> None:
    eps = np.array([[0.5, 0.8], [0.2, 0.9]])
    S = berechne_resonanzentropie(eps)
    assert S.shape == eps.shape


def test_entropie_non_negative() -> None:
    """S ≥ 0 for ε ∈ (0, 1]."""
    eps = np.linspace(0.01, 1.0, 100)
    S = berechne_resonanzentropie(eps)
    assert np.all(S >= 0)
    assert np.all(np.isfinite(S))


def test_entropie_maximum_bei_inverse_e() -> None:
    """S is maximal at ε = 1/e."""
    eps = np.linspace(0.01, 1.0, 10000)
    S = berechne_resonanzentropie(eps)
    idx_max = np.argmax(S)
    eps_at_max = eps[idx_max]
    np.testing.assert_allclose(eps_at_max, 1 / np.e, atol=0.001)


def test_entropie_null_an_grenzen() -> None:
    """S = 0 at ε = 1 and S → 0 as ε → 0."""
    S_at_one = berechne_resonanzentropie(np.array([1.0]))
    assert np.isclose(S_at_one[0], 0.0, atol=1e-10)

    S_near_zero = berechne_resonanzentropie(np.array([1e-6]))
    assert S_near_zero[0] < 0.001


def test_entropie_monotonie() -> None:
    """For ε > 1/e: higher ε → lower S."""
    eps = np.array([0.5, 0.9])
    S = berechne_resonanzentropie(eps)
    assert S[0] > S[1]


# === Plot (smoke test) ===

def test_plot_runs() -> None:
    """Generate plot and save to file."""
    import tempfile
    A = np.linspace(0.1, 1, 10)
    tau = np.linspace(0.1, 1, 10)
    E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    S = berechne_resonanzentropie(eps)
    with tempfile.TemporaryDirectory() as tmp:
        savefile = os.path.join(tmp, "plot.png")
        plot_numerische_demonstration(tau_grid, A_grid, E_res, eps, S,
                          save_path=savefile, show=False)
        assert os.path.exists(savefile)


# === Standalone runner ===

def run_all_tests() -> bool:
    """Runs all tests without pytest."""
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

    print("Resonance Field Theory — Unit Tests")
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
