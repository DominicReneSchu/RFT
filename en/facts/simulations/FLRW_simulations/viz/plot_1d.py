"""
Visualisation of the 1D FLRW resonance field simulation.

Four plots: resonance field ε(t), scale factor a(t),
comoving energy density ρ·a³, Hubble parameter H(t).

Note: With non-minimal coupling (α ≠ 0), ρ·a³ is not an
exactly conserved quantity — energy transfer takes place between
the scalar field and the spacetime geometry.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_1d_results(sol, V, alpha=0.5, kappa=1.0, save_path=None, show=True):
    """Plots the results of the 1D FLRW simulation.

    Parameters
    ----------
    sol : OdeSolution
        Solution from flrw_1d_sim (sol.y = [ε, dε/dt, a, da/dt])
    V : callable
        Potential function V(ε)
    alpha : float
        Non-minimal coupling
    kappa : float
        Gravitational coupling
    save_path : str or None
        If provided, the plot is saved to this path
    show : bool
        If True, plt.show() is called
    """
    eps = sol.y[0]
    epsdot = sol.y[1]
    a = sol.y[2]
    adot = sol.y[3]
    t = sol.t

    # Energy density and Hubble parameter
    rho_eps = 0.5 * epsdot**2 + V(eps)
    H = adot / a

    # Comoving energy density (not exactly conserved at α ≠ 0)
    rho_komovil = rho_eps * a**3

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    # (1) Resonance field ε(t)
    axes[0, 0].plot(t, eps, color="tab:blue", linewidth=1.5)
    axes[0, 0].set_xlabel("t")
    axes[0, 0].set_ylabel("ε")
    axes[0, 0].set_title("Resonance field ε(t)  [Axiom A1: oscillation]")
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(0, color="gray", linewidth=0.5)

    # (2) Scale factor a(t)
    axes[0, 1].plot(t, a, color="tab:orange", linewidth=1.5)
    axes[0, 1].set_xlabel("t")
    axes[0, 1].set_ylabel("a")
    axes[0, 1].set_title("Scale factor a(t)")
    axes[0, 1].grid(True, alpha=0.3)

    # (3) Hubble parameter H(t)
    axes[1, 0].plot(t, H, color="tab:green", linewidth=1.5)
    axes[1, 0].set_xlabel("t")
    axes[1, 0].set_ylabel("H = ȧ/a")
    axes[1, 0].set_title("Hubble parameter H(t)")
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(0, color="gray", linewidth=0.5)

    # (4) Comoving energy density ρ·a³
    axes[1, 1].plot(t, rho_komovil, color="tab:red", linewidth=1.5)
    axes[1, 1].set_xlabel("t")
    axes[1, 1].set_ylabel("ρ · a³")
    axes[1, 1].set_title(
        "Comoving energy density ρ·a³\n"
        "(not exactly conserved at α ≠ 0 — energy transfer field ↔ geometry)"
    )
    axes[1, 1].grid(True, alpha=0.3)

    plt.suptitle(
        f"1D FLRW resonance field  |  α = {alpha}, κ = {kappa}, "
        f"ε₀ = {eps[0]:.2f}, ȧ₀ = {adot[0]:.2f}",
        fontsize=12, fontweight="bold",
    )
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)
