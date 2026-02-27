"""Visualisierung Stufe 6b: CMB-Leistungsspektrum-Vergleich."""

import numpy as np
import matplotlib.pyplot as plt


def plot_cmb_comparison(result, save_path=None, show=True):
    """Drei-Panel-Plot: Spektrum, Residuen, Chi^2-Vergleich."""
    ell = result["ell"]
    D_planck = result["D_planck"]
    D_lcdm = result["D_lcdm"]
    D_resonanz = result["D_resonanz"]
    err = result["err"]

    fig, axes = plt.subplots(2, 1, figsize=(14, 10),
                              gridspec_kw={"height_ratios": [3, 1]},
                              sharex=True)

    # === Panel 1: Leistungsspektrum ===
    ax = axes[0]
    ax.errorbar(ell, D_planck, yerr=err, fmt=".", color="gray",
                markersize=3, elinewidth=0.5, alpha=0.6, label="Planck 2018")
    ax.plot(ell, D_lcdm, "-", color="tab:blue", linewidth=1.5,
            label=f"ΛCDM (H₀={result['h0']:.1f})")
    ax.plot(ell, D_resonanz, "--", color="tab:red", linewidth=1.5,
            label=f"ΛCDM + Resonanzfeld (d_η={result['d_eta']:.4f})")

    ax.set_ylabel("D_ℓ = ℓ(ℓ+1)C_ℓ/(2π)  [μK²]", fontsize=12)
    ax.set_title(
        "Stufe 6b: CMB-Leistungsspektrum — Planck 2018 vs. Resonanzfeldtheorie",
        fontsize=13, fontweight="bold",
    )
    ax.legend(fontsize=10, loc="upper right")
    ax.grid(True, alpha=0.2)
    ax.set_xlim(2, max(ell) + 50)

    # === Panel 2: Residuen ===
    ax2 = axes[1]
    ax2.axhline(0, color="black", linewidth=0.5)
    ax2.plot(ell, result["residual_lcdm"], ".", color="tab:blue",
             markersize=3, alpha=0.6, label="ΛCDM")
    ax2.plot(ell, result["residual_resonanz"], ".", color="tab:red",
             markersize=3, alpha=0.6, label="ΛCDM + Resonanzfeld")

    ax2.set_xlabel("Multipol ℓ", fontsize=12)
    ax2.set_ylabel("(Planck − Modell) / σ", fontsize=12)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.2)
    ax2.set_ylim(-5, 5)

    # Chi^2-Annotation
    text = (
        f"χ²/dof (ΛCDM):       {result['chi2_lcdm_reduced']:.2f}\n"
        f"χ²/dof (Resonanz):  {result['chi2_resonanz_reduced']:.2f}\n"
        f"Δχ² = {result['chi2_lcdm'] - result['chi2_resonanz']:.1f}"
    )
    ax2.text(
        0.02, 0.95, text, transform=ax2.transAxes, fontsize=10,
        verticalalignment="top", fontfamily="monospace",
        bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.9),
    )

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)


def plot_chi2_scan(chi2_result, save_path=None, show=True):
    """Chi^2(H0)-Vergleich: LCDM vs. Resonanzfeld."""
    h0 = chi2_result["h0_values"]
    chi2_l = chi2_result["chi2_lcdm"]
    chi2_r = chi2_result["chi2_resonanz"]

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(h0, chi2_l, "-o", color="tab:blue", markersize=4,
            linewidth=1.5, label="ΛCDM")
    ax.plot(h0, chi2_r, "-s", color="tab:red", markersize=4,
            linewidth=1.5, label="ΛCDM + Resonanzfeld")

    # Minima markieren
    idx_l = np.argmin(chi2_l)
    idx_r = np.argmin(chi2_r)
    ax.axvline(h0[idx_l], color="tab:blue", linewidth=0.8, alpha=0.4,
               linestyle=":")
    ax.axvline(h0[idx_r], color="tab:red", linewidth=0.8, alpha=0.4,
               linestyle=":")

    ax.plot(h0[idx_l], chi2_l[idx_l], "o", color="tab:blue",
            markersize=12, markeredgecolor="black", markeredgewidth=1.5,
            label=f"ΛCDM min: H₀={h0[idx_l]:.1f}", zorder=10)
    ax.plot(h0[idx_r], chi2_r[idx_r], "s", color="tab:red",
            markersize=12, markeredgecolor="black", markeredgewidth=1.5,
            label=f"Resonanz min: H₀={h0[idx_r]:.1f}", zorder=10)

    # Planck / SH0ES Baender
    ax.axvspan(66.9, 67.9, alpha=0.1, color="tab:purple",
               label="Planck 2018")
    ax.axvspan(72.0, 74.0, alpha=0.1, color="tab:orange",
               label="SH0ES")

    ax.set_xlabel("H₀  [km/s/Mpc]", fontsize=13)
    ax.set_ylabel("χ²", fontsize=13)
    ax.set_title(
        "χ²(H₀): Vergleich ΛCDM vs. Resonanzfeldtheorie\n"
        "Verschiebt die η-Korrektur das χ²-Minimum?",
        fontsize=13, fontweight="bold",
    )
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)