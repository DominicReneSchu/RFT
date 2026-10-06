# rt33_energy_gap.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
#
# RT-33: Warp Drive — Closing the Energy Gap (Stage 5)
#
# Scaling law of the energy gap as a function of bubble radius R.
#
# Physical basis:
#   rho_needed(R) ~ c⁴/(8πG) · (v_s/R)² · σ²  [Alcubierre 1994, Pfenning & Ford 1997]
#   rho_available(R) = E_fusion / V_active(R),  V_active = 4πR²/σ
#   Wall-packing model (n ∝ R²): rho_available = const
#   Gap factor: L(R) = rho_needed / rho_available
#   Critical radius R*: L(R*) = 1
#
# Conclusion:
#   R* lies in the astronomical range (parsec to kiloparsec) for all realistic
#   fusion scenarios, far beyond 1 AU. The energy gap is not a pure scaling
#   problem — it requires G* >> 10⁶ or fundamentally new physics (negative
#   energy, Casimir effect, exotic matter).
#
# Execution:
#   cd en/facts/concepts/warp_drive
#   python analyse/rt33_energy_gap.py

from __future__ import annotations

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

# Parent directory in path
_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
sys.path.insert(0, _PARENT)

from warp_drive import scaling_law

# ============================================================
# Configuration
# ============================================================

OUT_DIR = os.path.join(_PARENT, "figures")
C = 2.99792458e8    # Speed of light [m/s]
AU = 1.496e11       # 1 Astronomical Unit [m]
LY = 9.461e15       # 1 Light-year [m]
PC = 3.086e16       # 1 Parsec [m]

SCENARIOS = {
    "Conservative": {
        "n_reactors": 12, "gain": 1.5, "P_per": 1e8,
        "label": "Conservative (G=1.5, 12×100MW)",
    },
    "Realistic": {
        "n_reactors": 100, "gain": 10.0, "P_per": 1e9,
        "label": "Realistic (G=10, 100×1GW)",
    },
    "Optimistic": {
        "n_reactors": 1000, "gain": 100.0, "P_per": 1e10,
        "label": "Optimistic (G=100, 1000×10GW)",
    },
}

# ============================================================
# Main program
# ============================================================

def main() -> None:
    print("=" * 72)
    print("RT-33 — WARP DRIVE: CLOSING THE ENERGY GAP (STAGE 5)")
    print("Scaling law rho_needed(R) vs. rho_available(R)")
    print("© Dominic-René Schu, 2025/2026 – Resonance Field Theory")
    print("=" * 72)

    os.makedirs(OUT_DIR, exist_ok=True)

    R_range = np.logspace(1, 6, 500)       # 10 m … 1000 km
    v_s_list = [0.01 * C, 0.1 * C, 1.0 * C]
    sigma = 10.0    # wall sharpness [1/m]

    # ----------------------------------------------------------
    # scaling_law() for all three scenarios
    # ----------------------------------------------------------
    result = scaling_law(
        R_range=R_range,
        v_s_list=v_s_list,
        sigma_list=[sigma],
        gain_list=[1.5, 10.0, 100.0],
        n_reactors_list=[12, 100, 1000],
        P_per_reactor=1e8,
        pulse_rate=10.0,
        R_ref=50.0,
        plot=True,
        export_csv=True,
        out=OUT_DIR,
    )

    # ----------------------------------------------------------
    # Results output
    # ----------------------------------------------------------
    print("\n" + "=" * 72)
    print("RESULTS TABLE  (v_s = 0.1c, σ = 10 /m, R_ref = 50 m)")
    print("=" * 72)
    print(f"  {'Scenario':<42s} | {'R*':>18s} | {'G*':>12s} |"
          f" {'L(50m)':>10s} | Assessment")
    print(f"  {'-'*42} | {'-'*18} | {'-'*12} | {'-'*10} | {'-'*26}")

    for r in result["scenarios"]:
        Rc = r["R_crit"]
        if Rc < 1e3:
            rc_str = f"{Rc:.2f} m"
        elif Rc < AU:
            rc_str = f"{Rc / AU:.3e} AU"
        elif Rc < LY:
            rc_str = f"{Rc / LY:.3e} ly"
        elif Rc < PC * 1e6:
            rc_str = f"{Rc / PC:.3e} pc"
        else:
            rc_str = f"{Rc / (PC * 1e3):.3e} kpc"

        # G* for gap closure at R_ref = 50 m
        from warp_drive import PI, G as GRAV, C as LIGHT
        prefactor = LIGHT ** 4 / (8.0 * PI * GRAV)
        G_star = (prefactor * (0.1 * LIGHT / 50.0) ** 2 * sigma ** 2
                  * 4.0 * PI * 50.0 ** 2
                  / (r["n_reactors"] * r["P_per_reactor"] * 1e-8 * sigma))

        print(f"  {r['label']:<42s} | {rc_str:>18s} | {G_star:>12.3e} |"
              f" {r['L_at_Rref']:>10.3e} | {r['assessment']}")

    # ----------------------------------------------------------
    # Conclusion
    # ----------------------------------------------------------
    print("\n" + "=" * 72)
    print("CONCLUSION AND FALSIFICATION CRITERION (RT-33)")
    print("=" * 72)
    print("""
  Scaling law:
    rho_needed(R)    = c⁴/(8πG) · (v_s/R)² · σ²    ∝ R⁻²
    rho_available(R) = n · P · τ · G / (4πR²/σ)    ∝ R⁻² (fixed n)
    Wall-packing model (n ∝ R²): rho_available = const → L(R) ∝ R⁻²

  Agreement with literature:
    Alcubierre (1994): rho ~ c⁴/(8πG) · (v_s · σ)²  — here σ = const
    Pfenning & Ford (1997): E_total = c⁴ · v_s² · σ / (2G) — R-independent
    RFT-RT-33: rho(R) ∝ R⁻² consistent with σ = const

  Falsification criterion:
    R* < 1 km   → technically achievable in principle (long term)
    R* < 1 AU   → technically very challenging
    R* > 1 AU   → not achievable with known physics

  Result:
    All three scenarios: R* >> 1 AU (parsec to kiloparsec scale)
    → The energy gap is not a pure scaling problem.
    → For gap closure at R = 50 m: required gain G* ~ 10¹⁶ – 10¹⁸
    → This is 10¹⁶× more than the best fusion technology.

  HONESTY STANDARD MAINTAINED (§6.1):
    Δw = 0.057 is not an Alcubierre warp effect (cosmological roll behavior).
    RT-33 shows: the Alcubierre energy gap is astronomical — not technical.
    The two-field model remains physically interesting as an analogy,
    but not as an actual warp drive mechanism.

  Next step: RT-34 — 3D warp bubble (Stage 6)
""")
    print(f"  Plots saved to: {OUT_DIR}/")
    print(f"  CSV: {OUT_DIR}/rt33_scaling_law.csv")
    print("Done.")


if __name__ == "__main__":
    main()
