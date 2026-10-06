"""
RT-05: CAMB/CLASS CMB comparison analysis.

Runs the CAMB/CLASS-based CMB comparison and H0 tension scan.

Falsification criterion:
    Δχ²_CAMB > 0: RFT correction improves the fit vs. pure ΛCDM
    (K-5 resolved if positive).

Usage:
    python analyse/rt05_camb_vergleich.py

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
    print("RT-05: CAMB/CLASS CMB-Vergleich")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 1. Planck-Daten laden
    # ------------------------------------------------------------------
    data_path = os.path.join(_ROOT, "data", "planck_tt_binned.txt")
    print(f"\n[1] Planck-Daten laden von: {data_path}")
    try:
        planck_data = load_planck_tt(data_path)
    except FileNotFoundError:
        print("  Datei nicht gefunden, versuche Download ...")
        download_planck_tt(data_path)
        planck_data = load_planck_tt(data_path)
    print(f"  {len(planck_data['ell'])} Datenpunkte, ℓ = {planck_data['ell'][0]:.0f}..{planck_data['ell'][-1]:.0f}")

    # ------------------------------------------------------------------
    # 2. Spielzeugmodell-Vergleich (Referenz, Rückwärtskompatibilität)
    # ------------------------------------------------------------------
    print("\n[2] Spielzeugmodell-Vergleich (generate_lcdm_bestfit) ...")
    result_toy = compare_with_planck(planck_data, h0=67.36, d_eta=0.1334)
    print(f"  χ²_ΛCDM (Toy)      = {result_toy['chi2_lcdm']:.1f}")
    print(f"  χ²_RFT  (Toy)      = {result_toy['chi2_resonanz']:.1f}")
    print(f"  Δχ²     (Toy)      = {result_toy['delta_chi2']:+.1f}")
    print(f"  Pearson r (Toy)    = {result_toy['pearson_r']:.3f}")

    # ------------------------------------------------------------------
    # 3. CAMB/CLASS-Vergleich
    # ------------------------------------------------------------------
    print("\n[3] CAMB/CLASS-Vergleich ...")
    camb_available = True
    try:
        result_camb = compare_with_camb(
            planck_data, H0=67.36, d_eta=0.1334,
        )
        backend = result_camb["backend"]
        print(f"  Backend: {backend}")
        print(f"  χ²_ΛCDM ({backend})  = {result_camb['chi2_lcdm']:.1f}")
        print(f"  χ²_RFT  ({backend})  = {result_camb['chi2_resonanz']:.1f}")
        print(f"  Δχ²     ({backend})  = {result_camb['delta_chi2']:+.1f}")
        print(f"  Pearson r ({backend}) = {result_camb['pearson_r']:.3f}")

        if result_camb["delta_chi2"] > 0:
            print("  → K-5 BEHOBEN: Δχ²_CAMB > 0 — RFT verbessert Fit gegenüber echtem ΛCDM")
        else:
            print("  → K-5b: Δχ²_CAMB ≤ 0 — bisheriger Δχ² war Artefakt des Spielzeugmodells")
            print("     Neue RT für Parameteranpassung erforderlich!")
    except ImportError as e:
        print(f"  CAMB/CLASS nicht verfügbar: {e}")
        print("  → Fallback auf Spielzeugmodell")
        result_camb = result_toy
        backend = "toy_model"
        camb_available = False

    # ------------------------------------------------------------------
    # 4. H0-Spannungstest
    # ------------------------------------------------------------------
    print("\n[4] H0-Spannungstest (40 Schritte, H₀ ∈ [60, 80]) ...")
    tension_result = scan_h0_tension(
        planck_data,
        h0_range=(60.0, 80.0),
        n_steps=40,
        use_camb=camb_available,
    )
    print(f"  Backend: {tension_result['backend']}")
    print(f"  H₀_min(ΛCDM) = {tension_result['h0_min_lcdm']:.1f} km/s/Mpc")
    print(f"  H₀_min(RFT)  = {tension_result['h0_min_rft']:.1f} km/s/Mpc")
    tension_status = "✓ ZWISCHEN Planck und SH0ES" if tension_result["tension_test"] else "✗ AUSSERHALB [67, 73]"
    print(f"  Spannungstest: {tension_status}")

    # ------------------------------------------------------------------
    # 5. Vergleichstabelle
    # ------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("Vergleichstabelle RT-05:")
    print(f"{'Messgröße':<30} {'Spielzeugmodell':>15} {backend:>15}")
    print("-" * 62)
    print(f"{'χ²_ΛCDM':<30} {result_toy['chi2_lcdm']:>15.1f} {result_camb['chi2_lcdm']:>15.1f}")
    print(f"{'χ²_RFT':<30} {result_toy['chi2_resonanz']:>15.1f} {result_camb['chi2_resonanz']:>15.1f}")
    print(f"{'Δχ²':<30} {result_toy['delta_chi2']:>+15.1f} {result_camb['delta_chi2']:>+15.1f}")
    print(f"{'Pearson r':<30} {result_toy['pearson_r']:>15.3f} {result_camb['pearson_r']:>15.3f}")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 6. Plots
    # ------------------------------------------------------------------
    print("\n[6] Erstelle Plots ...")
    _plot_spectrum(planck_data, result_toy, result_camb, backend, _HERE)
    _plot_residuals(planck_data, result_toy, result_camb, backend, _HERE)
    _plot_h0_scan(tension_result, _HERE)

    print("\nRT-05 abgeschlossen.")
    return 0


def _plot_spectrum(planck_data, result_toy, result_camb, backend, outdir):
    """Spektrum-Vergleich: Planck, ΛCDM (Toy), ΛCDM (CAMB), RFT."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ell = planck_data["ell"]
    ax.errorbar(ell, planck_data["D_ell"], yerr=planck_data["err"],
                fmt="k.", ms=3, alpha=0.5, label="Planck 2018 TT", zorder=1)
    ax.plot(ell, result_toy["D_lcdm"], "b-", lw=1.5, alpha=0.6, label="ΛCDM (Spielzeugmodell)")
    ax.plot(ell, result_camb["D_lcdm"], "g-", lw=2, label=f"ΛCDM ({backend})")
    ax.plot(ell, result_camb["D_resonanz"], "r--", lw=2, label=f"ΛCDM+η ({backend})")
    ax.set_xlabel("Multipolmoment ℓ")
    ax.set_ylabel("D_ℓ [μK²]")
    ax.set_title(f"RT-05: CMB TT-Spektrum — Spielzeugmodell vs. {backend}")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(ell[0], ell[-1])
    plt.tight_layout()
    outpath = os.path.join(outdir, "rt05_spektrum_vergleich.png")
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot gespeichert: {outpath}")


def _plot_residuals(planck_data, result_toy, result_camb, backend, outdir):
    """Residuen-Vergleich."""
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    ell = planck_data["ell"]

    axes[0].plot(ell, result_toy["residual_lcdm"], "b-", lw=1.5, alpha=0.6,
                 label="ΛCDM (Toy) Residuen")
    axes[0].plot(ell, result_toy["residual_resonanz"], "r-", lw=1.5, alpha=0.6,
                 label="RFT (Toy) Residuen")
    axes[0].axhline(0, color="black", ls="--", alpha=0.5)
    axes[0].set_ylabel("(D_Planck − D_Modell) / σ")
    axes[0].set_title(f"Spielzeugmodell: Δχ² = {result_toy['delta_chi2']:+.1f}")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(ell, result_camb["residual_lcdm"], "g-", lw=1.5, alpha=0.6,
                 label=f"ΛCDM ({backend}) Residuen")
    axes[1].plot(ell, result_camb["residual_resonanz"], "m-", lw=1.5, alpha=0.6,
                 label=f"RFT ({backend}) Residuen")
    axes[1].axhline(0, color="black", ls="--", alpha=0.5)
    axes[1].set_xlabel("Multipolmoment ℓ")
    axes[1].set_ylabel("(D_Planck − D_Modell) / σ")
    axes[1].set_title(f"{backend}: Δχ² = {result_camb['delta_chi2']:+.1f}")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(outdir, "rt05_residuen_vergleich.png")
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot gespeichert: {outpath}")


def _plot_h0_scan(tension_result, outdir):
    """H₀-χ²-Scan mit Planck und SH0ES Markierungen."""
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
    axes[1].axvline(tension_result["h0_planck"], color="blue", ls=":", alpha=0.7,
                    label=f"H₀_Planck")
    axes[1].axvline(tension_result["h0_shoes"], color="orange", ls=":", alpha=0.7,
                    label=f"H₀_SH0ES")
    axes[1].set_xlabel("H₀ [km/s/Mpc]")
    axes[1].set_ylabel("Δχ² = χ²_ΛCDM − χ²_RFT")
    tension_label = "✓ Minimum zwischen Planck/SH0ES" if tension_result["tension_test"] else "✗ Außerhalb"
    axes[1].set_title(f"Δχ²(H₀): {tension_label}")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(outdir, "rt05_h0_scan.png")
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot gespeichert: {outpath}")


if __name__ == "__main__":
    sys.exit(main())
