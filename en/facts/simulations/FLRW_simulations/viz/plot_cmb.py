"""Visualisation Level 6b: CMB power spectrum comparison."""

import numpy as np
import matplotlib.pyplot as plt


def plot_cmb_comparison(result, save_path=None, show=True):
    """Three-panel plot: spectrum, residuals, correction signal."""
    ell = result["ell"]
    D_planck = result["D_planck"]
    D_lcdm = result["D_lcdm"]
    D_resonanz = result["D_resonanz"]
    err = result["err"]

    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 1, height_ratios=[3, 1, 1], hspace=0.08)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    ax3 = fig.add_subplot(gs[2], sharex=ax1)

    # === Panel 1: Power spectrum ===
    ax1.errorbar(ell, D_planck, yerr=err, fmt=".", color="gray",
                 markersize=3, elinewidth=0.5, alpha=0.6, label="Planck 2018", zorder=1)
    ax1.plot(ell, D_lcdm, "-", color="tab:blue", linewidth=1.8,
             label="ΛCDM best-fit", zorder=3)
    ax1.plot(ell, D_resonanz, "--", color="tab:red", linewidth=1.8,
             label=f"ΛCDM + resonance field (d_η={result['d_eta']:.4f})", zorder=2)

    ax1.set_ylabel("D_ℓ  [μK²]", fontsize=12)
    ax1.set_title(
        "Level 6b: CMB TT power spectrum — Planck 2018 vs. resonance field theory",
        fontsize=13, fontweight="bold",
    )
    ax1.legend(fontsize=10, loc="upper right")
    ax1.grid(True, alpha=0.2)
    ax1.set_ylim(bottom=-200)
    plt.setp(ax1.get_xticklabels(), visible=False)

    # === Panel 2: Residuals (Planck - model) / sigma ===
    ax2.axhline(0, color="black", linewidth=0.5)
    ax2.plot(ell, result["residual_lcdm"], ".", color="tab:blue",
             markersize=3, alpha=0.7, label="ΛCDM")
    ax2.plot(ell, result["residual_resonanz"], ".", color="tab:red",
             markersize=3, alpha=0.7, label="Resonance field")

    ax2.set_ylabel("(Planck−model)/σ", fontsize=11)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.2)
    ax2.set_ylim(-6, 6)
    plt.setp(ax2.get_xticklabels(), visible=False)

    # Chi^2 box
    text = (
        f"χ²/dof ΛCDM:           {result['chi2_lcdm_reduced']:.1f}\n"
        f"χ²/dof resonance field: {result['chi2_resonanz_reduced']:.1f}\n"
        f"Δχ² = {result['delta_chi2']:.1f}\n"
        f"Pearson r = {result['pearson_r']:.3f}"
    )
    ax2.text(
        0.02, 0.95, text, transform=ax2.transAxes, fontsize=9,
        verticalalignment="top", fontfamily="monospace",
        bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.9),
    )

    # === Panel 3: Correction signal vs. residuals ===
    ax3.axhline(0, color="black", linewidth=0.5)
    residuals_raw = result["residuals_raw"]
    correction = result["correction"]

    # Normalisation for comparison
    if np.max(np.abs(correction)) > 0:
        scale = np.std(residuals_raw) / np.max(np.abs(correction))
    else:
        scale = 1.0

    ax3.plot(ell, residuals_raw, ".", color="gray", markersize=2,
             alpha=0.5, label="Residuals (Planck − ΛCDM)")
    ax3.plot(ell, correction * scale, "-", color="tab:red", linewidth=1.5,
             label="η correction (scaled)", alpha=0.8)

    ax3.set_xlabel("Multipole ℓ", fontsize=12)
    ax3.set_ylabel("D_ℓ  [μK²]", fontsize=11)
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.2)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)


def plot_chi2_scan(chi2_result, save_path=None, show=True):
    """Delta-Chi^2(H0) comparison."""
    h0 = chi2_result["h0_values"]
    delta = chi2_result["delta_chi2"]

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # Panel 1: Both chi^2 curves
    ax = axes[0]
    ax.plot(h0, chi2_result["chi2_lcdm"], "-o", color="tab:blue",
            markersize=3, linewidth=1.5, label="ΛCDM")
    ax.plot(h0, chi2_result["chi2_resonanz"], "-s", color="tab:red",
            markersize=3, linewidth=1.5, label="ΛCDM + resonance field")

    ax.axvspan(66.9, 67.9, alpha=0.12, color="tab:purple", label="Planck 2018")
    ax.axvspan(72.0, 74.0, alpha=0.12, color="tab:orange", label="SH0ES")

    ax.set_xlabel("H₀  [km/s/Mpc]", fontsize=12)
    ax.set_ylabel("χ²", fontsize=12)
    ax.set_title("χ²(H₀)", fontsize=12, fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 2: Delta chi^2
    ax2 = axes[1]
    ax2.axhline(0, color="black", linewidth=0.5)
    ax2.plot(h0, delta, "-o", color="tab:green", markersize=4, linewidth=1.5)
    ax2.fill_between(h0, 0, delta, where=(delta > 0), alpha=0.2, color="tab:green",
                     label="Resonance field better (Δχ² > 0)")
    ax2.fill_between(h0, 0, delta, where=(delta < 0), alpha=0.2, color="tab:red",
                     label="ΛCDM better (Δχ² < 0)")

    ax2.axvspan(66.9, 67.9, alpha=0.12, color="tab:purple")
    ax2.axvspan(72.0, 74.0, alpha=0.12, color="tab:orange")

    ax2.set_xlabel("H₀  [km/s/Mpc]", fontsize=12)
    ax2.set_ylabel("Δχ² = χ²(ΛCDM) − χ²(resonance field)", fontsize=12)
    ax2.set_title("Δχ²(H₀): Improvement through η correction", fontsize=12, fontweight="bold")
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.suptitle(
        "Level 6b: χ² analysis — resonance field theory vs. ΛCDM",
        fontsize=14, fontweight="bold",
    )
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)
