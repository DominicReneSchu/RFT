"""Vergleichsplot: Flache Raumzeit vs. FLRW-Expansion."""

import numpy as np
import matplotlib.pyplot as plt


def plot_control_comparison(scan_flat, scan_flrw, scan_fast=None, save_path=None, show=True):
    dphi = scan_flat["delta_phi_values"]
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    ax = axes[0]
    dphi_fine = np.linspace(0, np.pi, 200)
    ax.plot(dphi_fine, np.cos(dphi_fine / 2)**2, color="black", linewidth=2, linestyle="--", label="Theorie: cos^2(dphi/2)", zorder=10)

    valid_flat = np.isfinite(scan_flat["eta_mean"])
    ax.scatter(dphi[valid_flat], scan_flat["eta_mean"][valid_flat], color="tab:blue", s=70, zorder=5, edgecolors="black", linewidths=0.5, marker="o", label="Flach (H = 0)")

    valid_flrw = np.isfinite(scan_flrw["eta_mean"])
    ax.scatter(dphi[valid_flrw], scan_flrw["eta_mean"][valid_flrw], color="tab:red", s=70, zorder=5, edgecolors="black", linewidths=0.5, marker="s", label="FLRW (adot0 = 0.3)")

    if scan_fast is not None:
        valid_fast = np.isfinite(scan_fast["eta_mean"])
        ax.scatter(dphi[valid_fast], scan_fast["eta_mean"][valid_fast], color="tab:orange", s=70, zorder=5, edgecolors="black", linewidths=0.5, marker="D", label="FLRW (adot0 = 1.0)")

    ax.set_xlabel("Phasendifferenz dphi_0  [rad]", fontsize=12)
    ax.set_ylabel("Kopplungseffizienz eta", fontsize=12)
    ax.set_title("Kontrolltest: eta(dphi) in verschiedenen Raumzeiten", fontsize=12)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.1, np.pi + 0.1); ax.set_ylim(-0.05, 1.15)

    ax2 = axes[1]
    cos2 = np.cos(dphi / 2)**2

    if np.any(valid_flat):
        d_flat = scan_flat["eta_mean"][valid_flat] - cos2[valid_flat]
        ax2.scatter(dphi[valid_flat], d_flat, color="tab:blue", s=70, edgecolors="black", linewidths=0.5, marker="o", label=f"Flach: <|d_eta|> = {np.mean(np.abs(d_flat)):.4f}")

    if np.any(valid_flrw):
        d_flrw = scan_flrw["eta_mean"][valid_flrw] - cos2[valid_flrw]
        ax2.scatter(dphi[valid_flrw], d_flrw, color="tab:red", s=70, edgecolors="black", linewidths=0.5, marker="s", label=f"FLRW: <|d_eta|> = {np.mean(np.abs(d_flrw)):.4f}")

    if scan_fast is not None and np.any(valid_fast):
        d_fast = scan_fast["eta_mean"][valid_fast] - cos2[valid_fast]
        ax2.scatter(dphi[valid_fast], d_fast, color="tab:orange", s=70, edgecolors="black", linewidths=0.5, marker="D", label=f"Schnell: <|d_eta|> = {np.mean(np.abs(d_fast)):.4f}")

    ax2.axhline(0, color="black", linewidth=1, linestyle="--")
    ax2.set_xlabel("Phasendifferenz dphi_0  [rad]", fontsize=12)
    ax2.set_ylabel("d_eta = eta_sim - cos^2(dphi/2)", fontsize=12)
    ax2.set_title("Raumzeit-Signatur: Abweichung d_eta\nVorhersage: d_eta(H=0) ~ 0, d_eta(H>0) > 0", fontsize=12)
    ax2.legend(fontsize=10); ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-0.1, np.pi + 0.1)

    plt.suptitle("Falsifizierbare Vorhersage der Resonanzfeldtheorie:\nHubble-Reibung verschiebt eta systematisch ueber cos^2(dphi/2)", fontsize=13, fontweight="bold")
    plt.tight_layout()
    if save_path: plt.savefig(save_path, dpi=300)
    if show: plt.show()
    plt.close(fig)
