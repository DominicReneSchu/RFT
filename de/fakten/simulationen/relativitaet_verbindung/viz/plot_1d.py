"""
Visualisierung der 1D-FLRW-Resonanzfeldsimulation.

Vier Plots: Resonanzfeld ε(t), Skalenfaktor a(t),
komovile Energiedichte ρ·a³, Hubble-Parameter H(t).

Hinweis: Bei nichtminimaler Kopplung (α ≠ 0) ist ρ·a³ keine
exakt erhaltene Größe — es findet Energietransfer zwischen
dem skalaren Feld und der Raumzeitgeometrie statt.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt


def plot_1d_results(sol: Any, V: Any, alpha: float = 0.5, kappa: float = 1.0, save_path: str | None = None, show: bool = True) -> None:
    """Plottet die Ergebnisse der 1D-FLRW-Simulation.

    Parameters
    ----------
    sol : OdeSolution
        Lösung aus flrw_1d_sim (sol.y = [ε, dε/dt, a, da/dt])
    V : callable
        Potentialfunktion V(ε)
    alpha : float
        Nichtminimale Kopplung
    kappa : float
        Gravitationskopplung
    save_path : str or None
        Falls angegeben, wird der Plot gespeichert
    show : bool
        Falls True, wird plt.show() aufgerufen
    """
    eps = sol.y[0]
    epsdot = sol.y[1]
    a = sol.y[2]
    adot = sol.y[3]
    t = sol.t

    # Energiedichte und Hubble-Parameter
    rho_eps = 0.5 * epsdot**2 + V(eps)
    H = adot / a

    # Komovilenergiedichte (nicht exakt erhalten bei α ≠ 0)
    rho_komovil = rho_eps * a**3

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    # (1) Resonanzfeld ε(t)
    axes[0, 0].plot(t, eps, color="tab:blue", linewidth=1.5)
    axes[0, 0].set_xlabel("t")
    axes[0, 0].set_ylabel("ε")
    axes[0, 0].set_title("Resonanzfeld ε(t)  [Axiom A1: Schwingung]")
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axhline(0, color="gray", linewidth=0.5)

    # (2) Skalenfaktor a(t)
    axes[0, 1].plot(t, a, color="tab:orange", linewidth=1.5)
    axes[0, 1].set_xlabel("t")
    axes[0, 1].set_ylabel("a")
    axes[0, 1].set_title("Skalenfaktor a(t)")
    axes[0, 1].grid(True, alpha=0.3)

    # (3) Hubble-Parameter H(t)
    axes[1, 0].plot(t, H, color="tab:green", linewidth=1.5)
    axes[1, 0].set_xlabel("t")
    axes[1, 0].set_ylabel("H = ȧ/a")
    axes[1, 0].set_title("Hubble-Parameter H(t)")
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(0, color="gray", linewidth=0.5)

    # (4) Komovilenergiedichte ρ·a³
    axes[1, 1].plot(t, rho_komovil, color="tab:red", linewidth=1.5)
    axes[1, 1].set_xlabel("t")
    axes[1, 1].set_ylabel("ρ · a³")
    axes[1, 1].set_title(
        "Komovilenergiedichte ρ·a³\n"
        "(nicht exakt erhalten bei α ≠ 0 — Energietransfer Feld ↔ Geometrie)"
    )
    axes[1, 1].grid(True, alpha=0.3)

    plt.suptitle(
        f"1D FLRW-Resonanzfeld  |  α = {alpha}, κ = {kappa}, "
        f"ε₀ = {eps[0]:.2f}, ȧ₀ = {adot[0]:.2f}",
        fontsize=12, fontweight="bold",
    )
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)