"""
Resonance Field Theory — Numerical Analysis

Calculates resonance energy (Lorentz profile), coupling efficiency
and resonance entropy over the (A, τ) parameter space.

Axiom references:
  A3: Resonance condition — peak at ω_ext ≈ ω₀
  A4: Coupling efficiency — ε(τ) derivable from Lorentz profile
  A5: Stable resonance field — entropy plateau at resonance

Dependencies: numpy, matplotlib
Usage: python numerical_demonstration.py
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


def berechne_resonanzenergie(
    A: np.ndarray,
    tau: np.ndarray,
    omega_0: float = 1.0,
    gamma: float = 0.2
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Resonance energy as a Lorentz profile.

    E_res = A / (1 + ((ω_ext − ω₀) / γ)²)

    with ω_ext = ω₀ · (1 + sin(τ)), where τ is the
    detuning parameter.

    At τ = 0, π, 2π, ... we have ω_ext = ω₀ (exact resonance)
    and E_res = A (maximum).

    Args:
        A: Amplitudes (1D, positive)
        tau: Detuning parameter (1D, positive)
        omega_0: Natural frequency
        gamma: Damping constant (half-width)

    Returns:
        (E_res, tau_grid, A_grid)
    """
    if np.any(A <= 0) or np.any(tau <= 0):
        raise ValueError("A and τ must be > 0.")
    if A.ndim != 1 or tau.ndim != 1:
        raise ValueError("A and τ must be 1D arrays.")

    tau_grid, A_grid = np.meshgrid(tau, A)
    omega_ext = omega_0 * (1 + np.sin(tau_grid))
    E_res = A_grid / (1 + ((omega_ext - omega_0) / gamma) ** 2)
    return np.clip(E_res, 1e-8, None), tau_grid, A_grid


def berechne_kopplungseffizienz(
    E_res: np.ndarray,
    A_grid: np.ndarray
) -> np.ndarray:
    """Coupling efficiency from the resonance profile.

    ε = E_res / A ∈ (0, 1]

    At exact resonance (ω_ext = ω₀): ε = 1
    At strong detuning: ε → 0

    This corresponds to the Lorentz profile as the
    frequency-dependent realisation of Axiom 4.
    """
    return np.clip(E_res / A_grid, 1e-8, 1.0)


def berechne_resonanzentropie(eps: np.ndarray) -> np.ndarray:
    """Resonance entropy as an information measure.

    S = −ε · ln(ε)

    Defined via the coupling efficiency ε ∈ (0, 1],
    guaranteeing S ≥ 0.

    Maximum at ε = 1/e ≈ 0.368 (natural damping).
    S = 0 at ε = 1 (perfect resonance) and ε → 0.
    """
    eps_safe = np.clip(eps, 1e-8, 1.0)
    return -eps_safe * np.log(eps_safe)


def plot_numerische_demonstration(
    tau_grid: np.ndarray,
    A_grid: np.ndarray,
    E_res: np.ndarray,
    eps: np.ndarray,
    S: np.ndarray,
    save_path: str | None = None,
    show: bool = True
) -> None:
    """Three 3D plots: resonance energy, coupling efficiency, entropy."""

    fig = plt.figure(figsize=(18, 5.5))
    fig.canvas.manager.set_window_title(
        'Resonance Field Theory — Numerical Analysis (A3, A4, A5)')

    # --- Plot 1: Resonance energy ---
    ax1 = fig.add_subplot(131, projection='3d')
    surf1 = ax1.plot_surface(tau_grid, A_grid, E_res,
                             cmap='inferno', edgecolor='none')
    ax1.set_title(r"Resonance energy $E_{\mathrm{res}}$"
                  "\n(Lorentz profile, Axiom A3)")
    ax1.set_xlabel(r'Detuning $\tau$')
    ax1.set_ylabel(r'Amplitude $A$')
    ax1.set_zlabel(r'$E_{\mathrm{res}}$')
    fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10, pad=0.12)

    # --- Plot 2: Coupling efficiency ---
    ax2 = fig.add_subplot(132, projection='3d')
    surf2 = ax2.plot_surface(tau_grid, A_grid, eps,
                             cmap='plasma', edgecolor='none')
    ax2.set_title(r"Coupling efficiency $\varepsilon = E_{\mathrm{res}}/A$"
                  "\n(Axiom A4)")
    ax2.set_xlabel(r'Detuning $\tau$')
    ax2.set_ylabel(r'Amplitude $A$')
    ax2.set_zlabel(r'$\varepsilon$')
    ax2.set_zlim(0, 1.05)
    fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10, pad=0.12)

    # --- Plot 3: Resonance entropy ---
    ax3 = fig.add_subplot(133, projection='3d')
    surf3 = ax3.plot_surface(tau_grid, A_grid, S,
                             cmap='viridis', edgecolor='none')
    ax3.set_title(r"Resonance entropy $S = -\varepsilon \ln \varepsilon$"
                  "\n(Axiom A5)")
    ax3.set_xlabel(r'Detuning $\tau$')
    ax3.set_ylabel(r'Amplitude $A$')
    ax3.set_zlabel(r'Entropy $S$')
    fig.colorbar(surf3, ax=ax3, shrink=0.5, aspect=10, pad=0.12)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    if show:
        plt.show()
    plt.close(fig)


if __name__ == "__main__":
    # Input parameters
    A = np.linspace(0.1, 5, 500)
    tau = np.linspace(0.1, 5, 500)

    # Calculation
    E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    S = berechne_resonanzentropie(eps)

    # Console output
    print("Resonance Field Theory — Numerical Analysis")
    print("=" * 50)
    print(f"A ∈ [{A[0]:.1f}, {A[-1]:.1f}], "
          f"τ ∈ [{tau[0]:.1f}, {tau[-1]:.1f}]")
    print(f"E_res ∈ [{E_res.min():.4f}, {E_res.max():.4f}]")
    print(f"ε ∈ [{eps.min():.4f}, {eps.max():.4f}]")
    print(f"S ∈ [{S.min():.4f}, {S.max():.4f}]")
    print(f"S_max at ε = 1/e ≈ {1/np.e:.4f}: "
          f"S = {1/np.e:.4f}")
    print("=" * 50)

    # Visualisation
    plot_numerische_demonstration(tau_grid, A_grid, E_res, eps, S,
                      save_path="plot.png", show=True)
