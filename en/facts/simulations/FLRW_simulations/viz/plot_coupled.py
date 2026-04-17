"""Visualisation of the coupled FLRW resonance field simulation."""

import numpy as np
import matplotlib.pyplot as plt


def plot_coupled_results(sol, results, alpha=0.5, kappa=1.0, g=0.2, save_path=None, show=True):
    t = sol.t
    eps1 = sol.y[0]
    eps2 = sol.y[2]
    a = sol.y[4]
    delta_phi = results["delta_phi"]
    eta_th = results["eta_theorie"]
    eta_gem = results["eta_gemessen"]
    valid = results["valid_mask"]
    H = results["H"]
    rho1 = results["rho1"]
    rho2 = results["rho2"]
    rho_kop = results["rho_kopplung"]

    delta_phi_plot = np.where(valid, delta_phi, np.nan)
    eta_th_plot = np.where(valid, eta_th, np.nan)
    eta_gem_plot = np.where(valid, eta_gem, np.nan)

    if np.any(valid):
        valid_indices = np.where(valid)[0]
        t_valid_end = t[valid_indices[-1]]
    else:
        t_valid_end = t[0]

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    axes[0, 0].plot(t, eps1, label="e1", color="tab:blue", linewidth=1)
    axes[0, 0].plot(t, eps2, label="e2", color="tab:orange", linewidth=1)
    axes[0, 0].axvspan(t_valid_end, t[-1], alpha=0.1, color="gray", label="Amplitude < threshold")
    axes[0, 0].set_xlabel("t"); axes[0, 0].set_ylabel("e")
    axes[0, 0].set_title("Resonance fields e1(t), e2(t)  [A1]")
    axes[0, 0].legend(fontsize=8); axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(0, color="gray", linewidth=0.5)

    axes[0, 1].plot(t, delta_phi_plot, color="tab:purple", linewidth=1)
    axes[0, 1].axvspan(t_valid_end, t[-1], alpha=0.1, color="gray")
    axes[0, 1].set_xlabel("t"); axes[0, 1].set_ylabel("dphi [rad]")
    axes[0, 1].set_title("Phase difference dphi(t)  [A3]")
    axes[0, 1].grid(True, alpha=0.3); axes[0, 1].axhline(0, color="gray", linewidth=0.5)

    axes[0, 2].plot(t, eta_th_plot, label="cos^2(dphi/2)", color="tab:red", linewidth=1.5, linestyle="--")
    axes[0, 2].plot(t, eta_gem_plot, label="eta measured", color="tab:green", linewidth=1, alpha=0.8)
    axes[0, 2].axvspan(t_valid_end, t[-1], alpha=0.1, color="gray")
    axes[0, 2].set_xlabel("t"); axes[0, 2].set_ylabel("eta")
    axes[0, 2].set_title("Coupling efficiency eta(dphi)  [A4]")
    axes[0, 2].legend(fontsize=8); axes[0, 2].grid(True, alpha=0.3)
    axes[0, 2].set_ylim(-0.05, 1.15)

    axes[1, 0].plot(t, a, color="tab:orange", linewidth=1.5)
    axes[1, 0].set_xlabel("t"); axes[1, 0].set_ylabel("a")
    axes[1, 0].set_title("Scale factor a(t)  [A5: responds to eta]")
    axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].plot(t, H, color="tab:green", linewidth=1.5)
    axes[1, 1].set_xlabel("t"); axes[1, 1].set_ylabel("H")
    axes[1, 1].set_title("Hubble parameter H(t)")
    axes[1, 1].grid(True, alpha=0.3); axes[1, 1].axhline(0, color="gray", linewidth=0.5)

    axes[1, 2].plot(t, rho1, label="rho1", color="tab:blue", linewidth=1)
    axes[1, 2].plot(t, rho2, label="rho2", color="tab:orange", linewidth=1)
    axes[1, 2].plot(t, rho_kop, label="rho_coupling", color="tab:red", linewidth=1)
    axes[1, 2].set_xlabel("t"); axes[1, 2].set_ylabel("rho")
    axes[1, 2].set_title("Energy densities  [A4]")
    axes[1, 2].legend(fontsize=8); axes[1, 2].grid(True, alpha=0.3)

    plt.suptitle(f"Coupled FLRW resonance field  |  alpha={alpha}, g={g}, kappa={kappa}\nGrey region: amplitudes too small", fontsize=12, fontweight="bold")
    plt.tight_layout()
    if save_path: plt.savefig(save_path, dpi=300)
    if show: plt.show()
    plt.close(fig)


def plot_phase_scan(scan, save_path=None, show=True):
    dphi = scan["delta_phi_values"]
    eta_sim = scan["eta_mean"]
    valid = np.isfinite(eta_sim)

    fig, ax = plt.subplots(figsize=(9, 6))
    dphi_fine = np.linspace(0, np.pi, 200)
    ax.plot(dphi_fine, np.cos(dphi_fine / 2)**2, color="tab:red", linewidth=2.5, linestyle="--", label="Theory: cos^2(dphi/2)")
    ax.scatter(dphi[valid], eta_sim[valid], color="tab:blue", s=80, zorder=5, edgecolors="black", linewidths=0.5, label="Simulation (mean value)")

    if np.any(valid):
        residual = np.abs(eta_sim[valid] - scan["eta_cos2"][valid])
        ax.text(0.5, 0.05, f"Mean deviation: {np.mean(residual):.4f}", transform=ax.transAxes, fontsize=10, ha="center", style="italic", bbox=dict(boxstyle="round", facecolor="lightyellow"))

    ax.set_xlabel("Phase difference dphi_0  [rad]", fontsize=12)
    ax.set_ylabel("Coupling efficiency eta", fontsize=12)
    ax.set_title("Resonance field theory: eta(dphi) = cos^2(dphi/2)\nEmerges from coupled Klein–Gordon equation in FLRW spacetime", fontsize=12, fontweight="bold")
    ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.1, np.pi + 0.1); ax.set_ylim(-0.05, 1.15)
    plt.tight_layout()
    if save_path: plt.savefig(save_path, dpi=300)
    if show: plt.show()
    plt.close(fig)
