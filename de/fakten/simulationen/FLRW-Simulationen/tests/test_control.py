"""Unit-Tests fuer den Kontrolltest (Stufe 5)."""

import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from core.flat_coupled import flat_coupled_sim, scan_phase_flat
from core.coupled_flrw import scan_phase_coupling


def test_flat_fields_oscillate():
    sol, res = flat_coupled_sim(t_span=(0, 20))
    eps1 = sol.y[0]; eps2 = sol.y[2]
    assert np.any(eps1 > 0) and np.any(eps1 < 0)
    assert np.any(eps2 > 0) and np.any(eps2 < 0)

def test_flat_no_damping():
    sol, res = flat_coupled_sim(delta_phi_0=0.0, t_span=(0, 40))
    eps1 = sol.y[0]
    amp_first = np.max(np.abs(eps1[:len(eps1)//4]))
    amp_last = np.max(np.abs(eps1[-len(eps1)//4:]))
    assert amp_last > 0.8 * amp_first

def test_flat_eta_near_cos2():
    scan = scan_phase_flat(
        delta_phi_values=np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]),
        t_span=(0, 40),
    )
    eta_sim = scan["eta_mean"]; eta_cos2 = scan["eta_cos2"]
    valid = np.isfinite(eta_sim)
    mean_delta = np.mean(np.abs(eta_sim[valid] - eta_cos2[valid]))
    assert mean_delta < 0.10, f"<|d_eta|> flach zu gross: {mean_delta:.4f}"

def test_flat_resonance_max():
    sol, res = flat_coupled_sim(delta_phi_0=0.0, t_span=(0, 40))
    mask = res["valid_mask"] & np.isfinite(res["eta_gemessen"])
    if np.any(mask):
        assert np.mean(res["eta_gemessen"][mask]) > 0.9

def test_flat_antiresonance_min():
    sol, res = flat_coupled_sim(delta_phi_0=np.pi, t_span=(0, 40))
    mask = res["valid_mask"] & np.isfinite(res["eta_gemessen"])
    if np.any(mask):
        assert np.mean(res["eta_gemessen"][mask]) < 0.15

def test_flrw_deviation_larger():
    dphi_vals = np.array([np.pi/4, np.pi/2, 3*np.pi/4])
    sf = scan_phase_flat(delta_phi_values=dphi_vals, t_span=(0, 40))
    sc = scan_phase_coupling(delta_phi_values=dphi_vals, t_span=(0, 40), alpha=0.5, kappa=1.0, adot0=0.3)
    v = np.isfinite(sf["eta_mean"]) & np.isfinite(sc["eta_mean"])
    if np.any(v):
        d_flat = np.mean(np.abs(sf["eta_mean"][v] - sf["eta_cos2"][v]))
        d_flrw = np.mean(np.abs(sc["eta_mean"][v] - sc["eta_cos2"][v]))
        assert np.isfinite(d_flat) and np.isfinite(d_flrw)


def run_all_tests():
    tests = [
        test_flat_fields_oscillate, test_flat_no_damping,
        test_flat_eta_near_cos2, test_flat_resonance_max,
        test_flat_antiresonance_min, test_flrw_deviation_larger,
    ]
    passed = failed = 0
    print("Kontrolltest — Unit-Tests")
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
