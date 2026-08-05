"""
RT-05: CAMB/CLASS CMB comparison analysis.

Runs the CAMB/CLASS-based CMB comparison and H0 tension scan.

Falsification criterion:
    Δχ²_CAMB > 0: RFT correction improves the fit vs. pure ΛCDM
    (K-5 resolved if positive).

Usage:
    python analyse/rt05_camb_comparison.py

Output:
    - Console: Δχ²_CAMB, Δχ²_toy_model comparison table
    - Plots: analyse/rt05_*.png

Dependencies: numpy, matplotlib, camb or classy
"""

import sys
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from core.cmb_comparison import (
    load_planck_tt,
    download_planck_tt,
    compare_with_planck,
    compare_with_camb,
    scan_h0_tension,
)


def main():
    print("=" * 60)
    print("RT-05: CAMB/CLASS CMB Comparison")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 1. Load Planck data
    # ------------------------------------------------------------------
    data_path = os.path.join(_ROOT, "data", "planck_tt_binned.txt")
    print(f"\n[1] Loading Planck data from: {data_path}")
    try:
        planck_data = load_planck_tt(data_path)
    except FileNotFoundError:
        print("  File not found, attempting download ...")
        download_planck_tt(data_path)
        planck_data = load_planck_tt(data_path)
    print(f"  {len(planck_data['ell'])} data points, ℓ = {planck_data['ell'][0]:.0f}..{planck_data['ell'][-1]:.0f}")

    # ------------------------------------------------------------------
    # 2. Toy model comparison (reference, backward compatibility)
    # ------------------------------------------------------------------
    print("\n[2] Toy model comparison (generate_lcdm_bestfit) ...")
    result_toy = compare_with_planck(planck_data, h0=67.36, d_eta=0.1334)
    print(f"  χ²_ΛCDM (toy)    = {result_toy['chi2_lcdm']:.1f}")
    print(f"  χ²_RFT  (toy)    = {result_toy['chi2_resonanz']:.1f}")
    print(f"  Δχ²     (toy)    = {result_toy['delta_chi2']:+.1f}")
    print(f"  Pearson r (toy)  = {result_toy['pearson_r']:.3f}")

    # ------------------------------------------------------------------
    # 3. CAMB/CLASS comparison
    # ------------------------------------------------------------------
    print("\n[3] CAMB/CLASS comparison ...")
    camb_available = True
    try:
        result_camb = compare_with_camb(
            planck_data, H0=67.36, d_eta=0.1334,
        )
        backend = result_camb["backend"]
        print(f"  Backend: {backend}")
        print(f"  χ²_ΛCDM ({backend}) = {result_camb['chi2_lcdm']:.1f}")
        print(f"  χ²_RFT  ({backend}) = {result_camb['chi2_resonanz']:.1f}")
        print(f"  Δχ²     ({backend}) = {result_camb['delta_chi2']:+.1f}")
        print(f"  Pearson r ({backend}) = {result_camb['pearson_r']:.3f}")
        if result_camb["delta_chi2"] > 0:
            print("  → K-5 RESOLVED: Δχ²_CAMB > 0 — RFT improves fit vs. true ΛCDM")
        else:
            print("  → K-5b: Δχ²_CAMB ≤ 0 — previous Δχ² was artefact of toy model")
            print("     New RT for parameter optimisation required!")
    except ImportError as e:
        print(f"  CAMB/CLASS not available: {e}")
        print("  → Falling back to toy model")
        result_camb = result_toy
        backend = "toy_model"
        camb_available = False

    # ------------------------------------------------------------------
    # 4. H0 tension test
    # ------------------------------------------------------------------
    print("\n[4] H0 tension test (40 steps, H₀ ∈ [60, 80]) ...")
    tension_result = scan_h0_tension(
        planck_data,
        h0_range=(60.0, 80.0),
        n_steps=40,
        use_camb=camb_available,
    )
    print(f"  Backend: {tension_result['backend']}")
    print(f"  H₀_min(ΛCDM) = {tension_result['h0_min_lcdm']:.1f} km/s/Mpc")
    print(f"  H₀_min(RFT)  = {tension_result['h0_min_rft']:.1f} km/s/Mpc")
    tension_status = "✓ BETWEEN Planck and SH0ES" if tension_result["tension_test"] else "✗ OUTSIDE [67, 73]"
    print(f"  Tension test: {tension_status}")

    # ------------------------------------------------------------------
    # 5. Comparison table
    # ------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("Comparison table RT-05:")
    print(f"{'Metric':<30} {'Toy model':>15} {backend:>15}")
    print("-" * 62)
    print(f"{'χ²_ΛCDM':<30} {result_toy['chi2_lcdm']:>15.1f} {result_camb['chi2_lcdm']:>15.1f}")
    print(f"{'χ²_RFT':<30} {result_toy['chi2_resonanz']:>15.1f} {result_camb['chi2_resonanz']:>15.1f}")
    print(f"{'Δχ²':<30} {result_toy['delta_chi2']:>+15.1f} {result_camb['delta_chi2']:>+15.1f}")
    print(f"{'Pearson r':<30} {result_toy['pearson_r']:>15.3f} {result_camb['pearson_r']:>15.3f}")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 6. Plots
    # ------------------------------------------------------------------
    print("\n[5] Creating plots ...")
    _plot_spectrum(planck_data, result_toy, result_camb, backend, _HERE)
    _plot_residuals(planck_data, result_toy, result_camb, backend, _HERE)
    _plot_h0_scan(tension_result, _HERE)

    print("\nRT-05 completed.")
    return 0


def _plot_spectrum(planck_data, result_toy, result_camb, backend, outdir):
    fig, ax = plt.subplots(figsize=(10, 6))
    ell = planck_data["ell"]
    ax.errorbar(ell, planck_data["D_ell"], yerr=planck_data["err"],
                fmt="k.", ms=3, alpha=0.5, label="Planck 2018 TT", zorder=1)
    ax.plot(ell, result_toy["D_lcdm"], "b-", lw=1.5, alpha=0.6, label="ΛCDM (toy model)")
    ax.plot(ell, result_camb["D_lcdm"], "g-", lw=2, label=f"ΛCDM ({backend})")
    ax.plot(ell, result_camb["D_resonanz"], "r--", lw=2, label=f"ΛCDM+η ({backend})")
    ax.set_xlabel("Multipole moment ℓ")
    ax.set_ylabel("D_ℓ [μK²]")
    ax.set_title(f"RT-05: CMB TT spectrum — toy model vs. {backend}")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(ell[0], ell[-1])
    plt.tight_layout()
    outpath = os.path.join(outdir, "rt05_spectrum_comparison.png")
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot saved: {outpath}")


def _plot_residuals(planck_data, result_toy, result_camb, backend, outdir):
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    ell = planck_data["ell"]
    axes[0].plot(ell, result_toy["residual_lcdm"], "b-", lw=1.5, alpha=0.6,
                 label="ΛCDM (toy) residuals")
    axes[0].plot(ell, result_toy["residual_resonanz"], "r-", lw=1.5, alpha=0.6,
                 label="RFT (toy) residuals")
    axes[0].axhline(0, color="black", ls="--", alpha=0.5)
    axes[0].set_ylabel("(D_Planck − D_model) / σ")
    axes[0].set_title(f"Toy model: Δχ² = {result_toy['delta_chi2']:+.1f}")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[1].plot(ell, result_camb["residual_lcdm"], "g-", lw=1.5, alpha=0.6,
                 label=f"ΛCDM ({backend}) residuals")
    axes[1].plot(ell, result_camb["residual_resonanz"], "m-", lw=1.5, alpha=0.6,
                 label=f"RFT ({backend}) residuals")
    axes[1].axhline(0, color="black", ls="--", alpha=0.5)
    axes[1].set_xlabel("Multipole moment ℓ")
    axes[1].set_ylabel("(D_Planck − D_model) / σ")
    axes[1].set_title(f"{backend}: Δχ² = {result_camb['delta_chi2']:+.1f}")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    plt.tight_layout()
    outpath = os.path.join(outdir, "rt05_residuals_comparison.png")
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot saved: {outpath}")


def _plot_h0_scan(tension_result, outdir):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    h0 = tension_result["h0_values"]
    backend = tension_result["backend"]
    axes[0].plot(h0, tension_result["chi2_lcdm"], "b-", lw=2, label="χ²_ΛCDM")
    axes[0].plot(h0, tension_result["chi2_resonanz"], "r-", lw=2, label="χ²_RFT")
    axes[0].axvline(tension_result["h0_planck"], color="blue", ls=":", alpha=0.7,
                    label=f"H₀_Planck = {tension_result['h0_planck']}")
    axes[0].axvline(tension_result["h0_shoes"], color="orange", ls=":", alpha=0.7,
                    label=f"H₀_SH0ES = {tension_result['h0_shoes']}")
    axes[0].axvline(tension_result["h0_min_rft"], color="red", ls="--", alpha=0.7,
                    label=f"H₀_min(RFT) = {tension_result['h0_min_rft']:.1f}")
    axes[0].set_xlabel("H₀ [km/s/Mpc]")
    axes[0].set_ylabel("χ²")
    axes[0].set_title(f"χ²(H₀) — {backend}")
    axes[0].legend(fontsize=8)
    axes[0].grid(True, alpha=0.3)
    axes[1].plot(h0, tension_result["delta_chi2"], "purple", lw=2)
    axes[1].axhline(0, color="black", ls="--", alpha=0.5, label="Δχ² = 0")
    axes[1].axvline(tension_result["h0_planck"], color="blue", ls=":", alpha=0.7)
    axes[1].axvline(tension_result["h0_shoes"], color="orange", ls=":", alpha=0.7)
    axes[1].set_xlabel("H₀ [km/s/Mpc]")
    axes[1].set_ylabel("Δχ² = χ²_ΛCDM − χ²_RFT")
    tension_label = "✓ Minimum between Planck/SH0ES" if tension_result["tension_test"] else "✗ Outside"
    axes[1].set_title(f"Δχ²(H₀): {tension_label}")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)
    plt.tight_layout()
    outpath = os.path.join(outdir, "rt05_h0_scan.png")
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot saved: {outpath}")


if __name__ == "__main__":
    sys.exit(main())
