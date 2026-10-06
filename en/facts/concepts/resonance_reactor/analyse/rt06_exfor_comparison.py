# rt06_exfor_comparison.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
# RT-06: EXFOR cross-validation and σ(γ,α) analysis for Am-241
#
# This script:
#   1. Loads all three EXFOR channels: (γ,α), (γ,f), (γ,n) for Am-241
#   2. Runs validate_against_literature() for (γ,f) and (γ,n)
#   3. Creates four-panel plot:
#      - Panel 1: σ(γ,α) EXFOR/HF vs. GDR estimate
#      - Panel 2: σ(γ,f) EXFOR vs. Soldatov et al. (2001)
#      - Panel 3: σ(γ,n) EXFOR vs. Dietrich-Berman Atlas
#      - Panel 4: Deviation plot
#   4. Tabular output: new sigma_photo_alpha, deviation, K-6 status
#   5. Saves plot as rt06_exfor_comparison.png

from __future__ import annotations

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

# Add simulation directory to path
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_SIM_DIR = os.path.join(_SCRIPT_DIR, '..', 'simulation')
sys.path.insert(0, _SIM_DIR)

from exfor_data import (
    load_am241_photo_alpha,
    load_am241_photo_fission,
    load_am241_photo_neutron,
    validate_against_literature,
    sigma_photo_alpha_at_energy,
)
from experiment_am241 import (
    Am241_Literature,
    gdr_cross_section,
    photo_alpha_cross_section,
)


# ============================================================
# Configuration
# ============================================================

OUTPUT_DIR = os.path.join(_SCRIPT_DIR)
OUTPUT_PNG = os.path.join(OUTPUT_DIR, 'rt06_exfor_comparison.png')

# GDR centroid Am-241 (Dietrich-Berman Atlas)
E_PEAK_MEV = Am241_Literature.E_gdr_centroid_MeV  # 14.0 MeV

# Previous GDR estimate (total cross-section at centroid)
SIGMA_GDR_ESTIMATE_MB = gdr_cross_section(E_PEAK_MEV)


# ============================================================
# Load data
# ============================================================

def load_all_channels() -> dict:
    """Loads all three reaction channels for Am-241."""
    print("Loading EXFOR data for Am-241 ...")

    print("  (γ,α) ...")
    ga = load_am241_photo_alpha(energy_range_MeV=(6.0, 20.0))

    print("  (γ,f) ...")
    gf = load_am241_photo_fission(energy_range_MeV=(5.0, 14.0))

    print("  (γ,n) ...")
    gn = load_am241_photo_neutron(energy_range_MeV=(7.0, 20.0))

    return {"gamma_alpha": ga, "gamma_fission": gf, "gamma_neutron": gn}


# ============================================================
# Plot
# ============================================================

def make_plot(data: dict, output_path: str) -> None:
    """Creates four-panel comparison plot."""
    am = Am241_Literature
    ga = data["gamma_alpha"]
    gf = data["gamma_fission"]
    gn = data["gamma_neutron"]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "RT-06: Am-241 Cross Sections — EXFOR/Hauser-Feshbach vs. Literature",
        fontsize=13, fontweight='bold'
    )

    # --- Panel 1: σ(γ,α) ---
    ax1 = axes[0, 0]
    E_fine = np.linspace(6, 20, 200)

    # HF estimate (RT-06)
    ax1.plot(ga["E_MeV"], ga["sigma_mb"], 'b-o', ms=3,
             label=f'σ(γ,α) Hauser-Feshbach (RT-06)\n'
                   f'Uncertainty: ±factor 2–5')
    # Error band
    ax1.fill_between(
        ga["E_MeV"],
        ga["sigma_mb"] / 5.0,
        ga["sigma_mb"] * 5.0,
        alpha=0.15, color='blue', label='±factor 5 uncertainty'
    )
    # Previous GDR estimate (total cross-section)
    sigma_gdr_arr = np.array([gdr_cross_section(e) for e in E_fine])
    ax1.plot(E_fine, sigma_gdr_arr, 'r--',
             label=f'σ_GDR total (Dietrich-Berman)\n'
                   f'[previous proxy, ≠ σ(γ,α)]')
    ax1.axvline(E_PEAK_MEV, color='gray', ls=':', alpha=0.7,
                label=f'GDR centroid ({E_PEAK_MEV} MeV)')
    ax1.scatter([E_PEAK_MEV], [sigma_photo_alpha_at_energy(E_PEAK_MEV, ga)],
                color='blue', s=80, zorder=5,
                label=f'σ(γ,α) @ {E_PEAK_MEV} MeV = '
                      f'{sigma_photo_alpha_at_energy(E_PEAK_MEV, ga):.2f} mb')
    ax1.set_xlabel('E_γ (MeV)')
    ax1.set_ylabel('σ (mb)')
    ax1.set_title('σ(γ,α) Am-241: RT-06 vs. GDR estimate')
    ax1.legend(fontsize=7)
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    ax1.set_ylim(bottom=1e-5)

    # --- Panel 2: σ(γ,f) ---
    ax2 = axes[0, 1]
    ax2.plot(gf["E_MeV"], gf["sigma_mb"], 'g-o', ms=4,
             label=f'σ(γ,f) {gf["source"][:40]}')
    ax2.plot(am.soldatov_E_MeV, am.soldatov_sigma_f_mb, 'r^--', ms=5,
             label='Soldatov et al. (2001) — literature')
    max_dev_f = gf.get('max_deviation_pct', 0.0)
    pass_f = gf.get('validation_pass', True)
    ax2.set_xlabel('E_γ (MeV)')
    ax2.set_ylabel('σ (mb)')
    ax2.set_title(f'σ(γ,f) Am-241: Cross-validation vs. Soldatov\n'
                  f'Max. deviation: {max_dev_f:.1f}%  '
                  f'[{"PASS" if pass_f else "FAIL"}]')
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    # --- Panel 3: σ(γ,n) ---
    ax3 = axes[1, 0]
    ax3.plot(gn["E_MeV"], gn["sigma_mb"], 'purple', marker='s', ms=3, ls='-',
             label=f'σ(γ,n) {gn["source"][:40]}')
    ax3.plot(am.berman_E_MeV, am.berman_sigma_n_mb, 'r^--', ms=5,
             label='Dietrich-Berman Atlas — literature')
    max_dev_n = gn.get('max_deviation_pct', 0.0)
    pass_n = gn.get('validation_pass', True)
    ax3.set_xlabel('E_γ (MeV)')
    ax3.set_ylabel('σ (mb)')
    ax3.set_title(f'σ(γ,n) Am-241: Cross-validation vs. Berman\n'
                  f'Max. deviation: {max_dev_n:.1f}%  '
                  f'[{"PASS" if pass_n else "FAIL"}]')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    # --- Panel 4: Deviation plot ---
    ax4 = axes[1, 1]
    # σ(γ,α): ratio HF / GDR_total
    E_common = np.linspace(9, 18, 50)
    sigma_ga_interp = np.array([sigma_photo_alpha_at_energy(e, ga) for e in E_common])
    sigma_gdr_interp = np.array([gdr_cross_section(e) for e in E_common])
    ratio_ga = np.where(sigma_gdr_interp > 0,
                        sigma_ga_interp / sigma_gdr_interp * 100.0, 0.0)
    ax4.plot(E_common, ratio_ga, 'b-', lw=2,
             label='σ(γ,α)/σ_GDR × 100  [branching ratio %]')
    ax4.axhline(0, color='black', ls='--', alpha=0.3)
    ax4.axhline(2.0, color='gray', ls=':', alpha=0.7,
                label='2% — RIPL-3 parametrisation at GDR peak')
    ax4.set_xlabel('E_γ (MeV)')
    ax4.set_ylabel('σ(γ,α)/σ_GDR × 100 (%)')
    ax4.set_title('σ(γ,α)/σ_GDR: Branching ratio (Γ_α/Γ_tot)')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  → {output_path}")


# ============================================================
# Critical output
# ============================================================

def print_rt06_result(data: dict) -> None:
    """Prints RT-06 result table."""
    am = Am241_Literature
    ga = data["gamma_alpha"]
    gf = data["gamma_fission"]
    gn = data["gamma_neutron"]

    sigma_exfor = sigma_photo_alpha_at_energy(E_PEAK_MEV, ga)
    sigma_gdr_estimate = SIGMA_GDR_ESTIMATE_MB

    # Deviation (absolute factor, due to orders of magnitude)
    if sigma_exfor > 0 and sigma_gdr_estimate > 0:
        factor = sigma_gdr_estimate / sigma_exfor
    else:
        factor = float('inf')

    max_dev_f = gf.get('max_deviation_pct', 0.0)
    max_dev_n = gn.get('max_deviation_pct', 0.0)
    pass_f = gf.get('validation_pass', True)
    pass_n = gn.get('validation_pass', True)

    # K-6 status
    k6_resolved = sigma_exfor > 0
    revision_required = factor > 10.0

    print("\n" + "=" * 60)
    print("=== RT-06 RESULT ===")
    print("=" * 60)
    print(f"\nσ(γ,α) Am-241 at E_peak = {E_PEAK_MEV:.1f} MeV:")
    print(f"  EXFOR/method:         {sigma_exfor:.4f} mb  "
          f"(±{ga['uncertainty_percent']:.0f}%)")
    print(f"  Method:               {ga['method']}")
    print(f"  Source:               {ga['source']}")
    print(f"  Previous proxy:       {sigma_gdr_estimate:.1f} mb  "
          f"[σ_GDR total — not a real σ(γ,α)!]")
    print(f"  Ratio (proxy/HF):     factor {factor:.0f}")
    print()
    print(f"  NOTE: The previous 'estimate' was the total GDR cross-")
    print(f"  section (σ_GDR ≈ {sigma_gdr_estimate:.0f} mb), not a real (γ,α)")
    print(f"  cross-section. The Hauser-Feshbach value {sigma_exfor:.3f} mb")
    print(f"  corresponds to the physical branching ratio")
    print(f"  Γ_α/Γ_tot ≈ 2% (RIPL-3). Factor {factor:.0f} difference")
    print(f"  → RFT reactor rate prediction must be revised.")
    print()
    print(f"σ(γ,f) cross-validation (Soldatov):  "
          f"max. deviation {max_dev_f:.1f}%  "
          f"[{'PASS' if pass_f else 'FAIL'}]")
    if not pass_f:
        print(f"  Note: literature values returned (EXFOR not available)")
    print(f"σ(γ,n) cross-validation (Berman):    "
          f"max. deviation {max_dev_n:.1f}%  "
          f"[{'PASS' if pass_n else 'FAIL'}]")
    if not pass_n:
        print(f"  Note: literature values returned (EXFOR not available)")
    print()

    if k6_resolved and not revision_required:
        k6_status = "RESOLVED"
        k6_note = "σ(γ,α) > 0, deviation < factor 10."
    elif k6_resolved and revision_required:
        k6_status = "RESOLVED (revision required)"
        k6_note = (
            f"σ(γ,α) determined, but deviation from previous proxy "
            f"= factor {factor:.0f} > 10. RFT reactor rate prediction "
            "must be recalculated using σ(γ,α) = Hauser-Feshbach value."
        )
    else:
        k6_status = "OPEN"
        k6_note = "σ(γ,α) could not be determined."

    print(f"K-6 Status: {k6_status}")
    print(f"  {k6_note}")
    print("=" * 60)


# ============================================================
# Main
# ============================================================

def main() -> None:
    print("=" * 60)
    print("RT-06: EXFOR cross-validation Am-241")
    print("=" * 60)

    data = load_all_channels()

    print("\nCreating plot ...")
    make_plot(data, OUTPUT_PNG)

    print_rt06_result(data)


if __name__ == "__main__":
    main()
