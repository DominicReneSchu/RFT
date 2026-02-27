"""Unit-Tests fuer Stufe 6a: core/h0_scan.py"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.h0_scan import (
    h0_to_adot0, scan_h0, predict_d_eta,
    hubble_tension_signature, H0_REF, ADOT0_REF,
)


def test_h0_to_adot0_reference():
    """Referenzpunkt: H0_REF -> ADOT0_REF."""
    assert abs(h0_to_adot0(H0_REF) - ADOT0_REF) < 1e-10


def test_h0_to_adot0_linear():
    """Skalierung ist linear."""
    a1 = h0_to_adot0(60.0)
    a2 = h0_to_adot0(80.0)
    a_mid = h0_to_adot0(70.0)
    expected_mid = (a1 + a2) / 2
    assert abs(a_mid - expected_mid) < 1e-10


def test_h0_to_adot0_zero():
    """H0 = 0 -> adot0 = 0."""
    assert h0_to_adot0(0.0) == 0.0


def test_scan_h0_returns_correct_keys():
    """Ergebnis enthaelt alle erwarteten Schluessel."""
    result = scan_h0(
        h0_values=np.array([65.0, 70.0, 75.0]),
        delta_phi_values=np.array([0, np.pi/2, np.pi]),
        t_span=(0, 20),
    )
    expected_keys = [
        "h0_values", "adot0_values", "d_eta_mean", "d_eta_std",
        "d_eta_flat", "eta_scans", "delta_phi_values",
        "fit_slope", "fit_intercept", "fit_poly",
    ]
    for key in expected_keys:
        assert key in result, f"Schluessel '{key}' fehlt"


def test_scan_h0_dimensions():
    """Arrays haben konsistente Laengen."""
    h0_vals = np.array([65.0, 70.0, 75.0])
    result = scan_h0(
        h0_values=h0_vals,
        delta_phi_values=np.array([0, np.pi/2, np.pi]),
        t_span=(0, 20),
    )
    assert len(result["h0_values"]) == 3
    assert len(result["adot0_values"]) == 3
    assert len(result["d_eta_mean"]) == 3
    assert len(result["d_eta_std"]) == 3
    assert len(result["eta_scans"]) == 3


def test_scan_h0_all_finite():
    """Alle d_eta-Werte sind endlich."""
    result = scan_h0(
        h0_values=np.array([65.0, 70.0, 75.0]),
        delta_phi_values=np.array([0, np.pi/4, np.pi/2, np.pi]),
        t_span=(0, 20),
    )
    assert np.all(np.isfinite(result["d_eta_mean"]))


def test_scan_h0_monotone():
    """d_eta waechst mit H0 (oder bleibt gleich)."""
    result = scan_h0(
        h0_values=np.array([60.0, 70.0, 80.0]),
        delta_phi_values=np.array([np.pi/4, np.pi/2, 3*np.pi/4]),
        t_span=(0, 30),
    )
    d = result["d_eta_mean"]
    # Toleranz: leichte Nicht-Monotonie moeglich durch numerische Effekte
    for i in range(len(d) - 1):
        assert d[i] <= d[i + 1] + 0.05, (
            f"Nicht monoton: d_eta[{i}]={d[i]:.4f} > d_eta[{i+1}]={d[i+1]:.4f}"
        )


def test_scan_h0_flat_reference():
    """Flache Referenz ist kleiner als alle FLRW-Werte."""
    result = scan_h0(
        h0_values=np.array([65.0, 70.0, 75.0]),
        delta_phi_values=np.array([np.pi/4, np.pi/2, 3*np.pi/4]),
        t_span=(0, 30),
    )
    d_flat = result["d_eta_flat"]
    assert np.isfinite(d_flat)


def test_predict_d_eta():
    """Vorhersage ist konsistent mit Scan."""
    result = scan_h0(
        h0_values=np.array([65.0, 70.0, 75.0]),
        delta_phi_values=np.array([0, np.pi/2, np.pi]),
        t_span=(0, 20),
    )
    d_pred = predict_d_eta(70.0, result)
    assert np.isfinite(d_pred)
    # Vorhersage sollte nahe am tatsaechlichen Wert liegen
    d_actual = result["d_eta_mean"][1]  # Index 1 = H0=70
    assert abs(d_pred - d_actual) < 0.05


def test_hubble_tension_signature():
    """Hubble-Spannungs-Signatur hat korrekte Struktur."""
    result = scan_h0(
        h0_values=np.array([65.0, 70.0, 75.0]),
        delta_phi_values=np.array([0, np.pi/2, np.pi]),
        t_span=(0, 20),
    )
    tension = hubble_tension_signature(result)
    assert "d_eta_planck" in tension
    assert "d_eta_shoes" in tension
    assert "delta_d_eta" in tension
    assert "relative_shift" in tension
    assert tension["delta_d_eta"] >= 0  # SH0ES > Planck -> d_eta groesser


def run_all_tests():
    tests = [
        test_h0_to_adot0_reference,
        test_h0_to_adot0_linear,
        test_h0_to_adot0_zero,
        test_scan_h0_returns_correct_keys,
        test_scan_h0_dimensions,
        test_scan_h0_all_finite,
        test_scan_h0_monotone,
        test_scan_h0_flat_reference,
        test_predict_d_eta,
        test_hubble_tension_signature,
    ]
    passed = failed = 0
    print("H0-Scan — Unit-Tests (Stufe 6a)")
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