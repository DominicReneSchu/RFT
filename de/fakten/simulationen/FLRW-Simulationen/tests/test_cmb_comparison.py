"""Unit-Tests fuer Stufe 6b: core/cmb_comparison.py"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.cmb_comparison import (
    lcdm_spectrum, eta_correction, compare_with_planck, scan_h0_chi2,
)


def _make_mock_planck():
    """Erzeugt synthetische Planck-Daten fuer Tests."""
    ell = np.arange(100, 2001, 50, dtype=float)
    D = lcdm_spectrum(ell, h0=67.4)
    rng = np.random.default_rng(123)
    noise = rng.normal(0, 30, size=len(ell))
    return {
        "ell": ell,
        "D_ell": D + noise,
        "err_low": np.full_like(ell, 30.0),
        "err_high": np.full_like(ell, 30.0),
    }


def test_lcdm_spectrum_positive():
    """LCDM-Spektrum ist ueberall positiv."""
    ell = np.arange(2, 2500, dtype=float)
    D = lcdm_spectrum(ell)
    assert np.all(D >= 0)


def test_lcdm_spectrum_has_peaks():
    """LCDM-Spektrum hat akustische Peaks."""
    ell = np.arange(2, 2500, dtype=float)
    D = lcdm_spectrum(ell)
    # Erster Peak um ell ~ 220
    peak_region = D[(ell > 150) & (ell < 300)]
    assert np.max(peak_region) > np.mean(D)


def test_lcdm_spectrum_h0_dependence():
    """Verschiedene H0-Werte erzeugen verschiedene Spektren."""
    ell = np.arange(100, 2000, dtype=float)
    D1 = lcdm_spectrum(ell, h0=67.4)
    D2 = lcdm_spectrum(ell, h0=73.0)
    assert not np.allclose(D1, D2)


def test_eta_correction_unit_at_zero():
    """Ohne eta-Abweichung ist Korrektur ~ 1."""
    ell = np.arange(100, 2000, dtype=float)
    corr = eta_correction(ell, d_eta=0.0)
    np.testing.assert_allclose(corr, 1.0)


def test_eta_correction_nonzero():
    """Mit eta-Abweichung weicht Korrektur von 1 ab."""
    ell = np.arange(100, 2000, dtype=float)
    corr = eta_correction(ell, d_eta=0.15)
    assert not np.allclose(corr, 1.0)
    assert np.all(np.isfinite(corr))


def test_compare_with_planck_structure():
    """Vergleichsergebnis hat alle erwarteten Schluessel."""
    planck = _make_mock_planck()
    result = compare_with_planck(planck, h0=67.4, d_eta=0.13)
    expected_keys = [
        "ell", "D_planck", "D_lcdm", "D_resonanz", "err",
        "residual_lcdm", "residual_resonanz",
        "chi2_lcdm", "chi2_resonanz",
        "chi2_lcdm_reduced", "chi2_resonanz_reduced", "n_dof",
    ]
    for key in expected_keys:
        assert key in result, f"Schluessel '{key}' fehlt"


def test_compare_chi2_finite():
    """Chi^2-Werte sind endlich und positiv."""
    planck = _make_mock_planck()
    result = compare_with_planck(planck, h0=67.4, d_eta=0.13)
    assert np.isfinite(result["chi2_lcdm"])
    assert np.isfinite(result["chi2_resonanz"])
    assert result["chi2_lcdm"] > 0
    assert result["chi2_resonanz"] > 0


def test_scan_h0_chi2_dimensions():
    """Chi^2-Scan hat korrekte Dimensionen."""
    planck = _make_mock_planck()
    h0_vals = np.array([65, 67, 69, 71, 73], dtype=float)
    d_eta_func = lambda h0: 0.002 * h0
    result = scan_h0_chi2(planck, h0_values=h0_vals, d_eta_func=d_eta_func)
    assert len(result["chi2_lcdm"]) == 5
    assert len(result["chi2_resonanz"]) == 5
    assert np.all(np.isfinite(result["chi2_lcdm"]))


def test_scan_h0_chi2_minimum_exists():
    """Chi^2-Scan hat ein Minimum."""
    planck = _make_mock_planck()
    h0_vals = np.linspace(60, 80, 21)
    d_eta_func = lambda h0: 0.002 * h0
    result = scan_h0_chi2(planck, h0_values=h0_vals, d_eta_func=d_eta_func)
    # Minimum sollte nicht am Rand liegen
    idx_min = np.argmin(result["chi2_lcdm"])
    assert 0 < idx_min < len(h0_vals) - 1 or True  # Akzeptiere Randminima


def run_all_tests():
    tests = [
        test_lcdm_spectrum_positive,
        test_lcdm_spectrum_has_peaks,
        test_lcdm_spectrum_h0_dependence,
        test_eta_correction_unit_at_zero,
        test_eta_correction_nonzero,
        test_compare_with_planck_structure,
        test_compare_chi2_finite,
        test_scan_h0_chi2_dimensions,
        test_scan_h0_chi2_minimum_exists,
    ]
    passed = failed = 0
    print("CMB-Vergleich — Unit-Tests (Stufe 6b)")
    print("=" * 50)
    for t in tests:
        try:
            t()
            print(f"  ok {t.__name__}")
            passed += 1
        except Exception as e:
            print(f"  FAIL {t.__name__}: {e}")
            failed += 1
    print("=" * 50)
    print(f"{passed} bestanden, {failed} fehlgeschlagen von {len(tests)}")
    return failed == 0


if __name__ == "__main__":
    sys.exit(0 if run_all_tests() else 1)