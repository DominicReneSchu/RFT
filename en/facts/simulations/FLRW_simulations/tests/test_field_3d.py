"""
Unit tests for core/field_3d.py

Execution (recommended):
    cd FLRW_simulations
    pytest tests/test_field_3d.py -v

Execution (standalone, without pytest):
    cd FLRW_simulations
    python tests/test_field_3d.py
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.field_3d import field_3d_sim


def test_field_3d_shape():
    """Result has the correct shape."""
    eps = field_3d_sim(N=16, steps=5)
    assert eps.shape == (16, 16, 16)


def test_field_3d_finite():
    """All values remain finite."""
    eps = field_3d_sim(N=16, steps=10)
    assert np.all(np.isfinite(eps))


def test_field_3d_dirichlet():
    """Dirichlet boundary conditions: boundary = 0."""
    eps = field_3d_sim(N=16, steps=10)
    assert np.all(eps[0, :, :] == 0)
    assert np.all(eps[-1, :, :] == 0)
    assert np.all(eps[:, 0, :] == 0)
    assert np.all(eps[:, -1, :] == 0)
    assert np.all(eps[:, :, 0] == 0)
    assert np.all(eps[:, :, -1] == 0)


def test_field_3d_initial_bump():
    """After 0 steps the field contains the initial bump."""
    eps = field_3d_sim(N=16, steps=0, bump_value=2.0)
    # Centre must have the bump value
    assert eps[8, 8, 8] == 2.0


def test_field_3d_evolution():
    """After several steps the field has changed."""
    eps_0 = field_3d_sim(N=16, steps=0)
    eps_10 = field_3d_sim(N=16, steps=10)
    assert not np.allclose(eps_0, eps_10)


def test_field_3d_callback():
    """Callback is called and receives correct arguments."""
    steps_seen = []

    def my_callback(eps, step):
        steps_seen.append(step)
        assert eps.shape == (16, 16, 16)

    field_3d_sim(N=16, steps=5, callback=my_callback)
    assert steps_seen == [0, 1, 2, 3, 4]


def test_field_3d_symmetry():
    """Field remains symmetric (cubic initial condition)."""
    eps = field_3d_sim(N=16, steps=20, initial_bump_size=3)
    c = 8  # Centre
    # x symmetry
    np.testing.assert_allclose(
        eps[c-1, c, c], eps[c+1, c, c], rtol=1e-10
    )
    # y symmetry
    np.testing.assert_allclose(
        eps[c, c-1, c], eps[c, c+1, c], rtol=1e-10
    )
    # z symmetry
    np.testing.assert_allclose(
        eps[c, c, c-1], eps[c, c, c+1], rtol=1e-10
    )


# === Standalone runner ===

def run_all_tests():
    tests = [
        test_field_3d_shape,
        test_field_3d_finite,
        test_field_3d_dirichlet,
        test_field_3d_initial_bump,
        test_field_3d_evolution,
        test_field_3d_callback,
        test_field_3d_symmetry,
    ]

    passed = 0
    failed = 0
    errors = []

    print("Field 3D — Unit tests")
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
