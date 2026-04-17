"""
Resonanzfeldtheorie — Numerische Demonstration

Demonstriert die Konsistenz von Resonanzenergie (Lorentz-Profil),
Kopplungseffizienz und Resonanzentropie über dem (A, τ)-Parameterraum.

Diese Simulation ist kein Beweis der Resonanzfeldtheorie, sondern
eine numerische Demonstration der internen Konsistenz der Axiome
A3–A5. Die empirische Validierung erfolgt separat über die
Monte-Carlo-Analyse mit unabhängigen Daten.

Axiom-Bezug:
  A3: Resonanzbedingung — Peak bei ω_ext ≈ ω₀
  A4: Kopplungseffizienz — ε(τ) aus Lorentz-Profil ableitbar
  A5: Stabiles Resonanzfeld — Entropie-Plateau bei Resonanz

Abhängigkeiten: numpy, matplotlib
Ausführung: python numerische_demonstration.py

© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie
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
    """Resonanzenergie als Lorentz-Profil.

    E_res = A / (1 + ((ω_ext − ω₀) / γ)²)

    mit ω_ext = ω₀ · (1 + sin(τ)), wobei τ den
    Verstimmungsparameter darstellt.

    Bei τ = 0, π, 2π, ... ist ω_ext = ω₀ (exakte Resonanz)
    und E_res = A (Maximum).

    Args:
        A: Amplituden (1D, positiv)
        tau: Verstimmungsparameter (1D, positiv)
        omega_0: Eigenfrequenz
        gamma: Dämpfungskonstante (Halbwertsbreite)

    Returns:
        (E_res, tau_grid, A_grid)
    """
    if np.any(A <= 0) or np.any(tau <= 0):
        raise ValueError(
            "A und τ müssen > 0 sein.")
    if A.ndim != 1 or tau.ndim != 1:
        raise ValueError(
            "A und τ müssen 1D-Arrays sein.")

    tau_grid, A_grid = np.meshgrid(tau, A)
    omega_ext = omega_0 * (1 + np.sin(tau_grid))
    E_res = A_grid / (1 + ((omega_ext - omega_0) / gamma) ** 2)
    return np.clip(E_res, 1e-8, None), tau_grid, A_grid


def berechne_kopplungseffizienz(
    E_res: np.ndarray,
    A_grid: np.ndarray
) -> np.ndarray:
    """Kopplungseffizienz aus Resonanzprofil (Axiom A4).

    ε = E_res / A ∈ (0, 1]

    Bei exakter Resonanz (ω_ext = ω₀): ε = 1
    Bei starker Verstimmung: ε → 0

    Dies ist die frequenzabhängige Realisierung der
    Kopplungseffizienz.
    """
    return np.clip(E_res / A_grid, 1e-8, 1.0)


def berechne_resonanzentropie(eps: np.ndarray) -> np.ndarray:
    """Resonanzentropie als Informationsmaß (Axiom A5).

    S = −ε · ln(ε)

    Definiert über die Kopplungseffizienz ε ∈ (0, 1],
    damit S ≥ 0 garantiert ist.

    Maximum bei ε = 1/e ≈ 0.368 (natürliche Dämpfung).
    S = 0 bei ε = 1 (perfekte Resonanz) und ε → 0.
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
    """Drei 3D-Plots: Resonanzenergie, Kopplungseffizienz, Entropie."""

    fig = plt.figure(figsize=(18, 5.5))
    fig.canvas.manager.set_window_title(
        'Resonanzfeldtheorie — Numerische Demonstration (A3, A4, A5)')

    # --- Plot 1: Resonanzenergie ---
    ax1 = fig.add_subplot(131, projection='3d')
    surf1 = ax1.plot_surface(
        tau_grid, A_grid, E_res,
        cmap='inferno', edgecolor='none')
    ax1.set_title(
        r"Resonanzenergie $E_{\mathrm{res}}$"
        "\n(Lorentz-Profil, Axiom A3)")
    ax1.set_xlabel(r'Verstimmung $\tau$')
    ax1.set_ylabel(r'Amplitude $A$')
    ax1.set_zlabel(r'$E_{\mathrm{res}}$')
    fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10, pad=0.12)

    # --- Plot 2: Kopplungseffizienz ---
    ax2 = fig.add_subplot(132, projection='3d')
    surf2 = ax2.plot_surface(
        tau_grid, A_grid, eps,
        cmap='plasma', edgecolor='none')
    ax2.set_title(
        r"Kopplungseffizienz "
        r"$\varepsilon = E_{\mathrm{res}}/A$"
        "\n(Axiom A4)")
    ax2.set_xlabel(r'Verstimmung $\tau$')
    ax2.set_ylabel(r'Amplitude $A$')
    ax2.set_zlabel(r'$\varepsilon$')
    ax2.set_zlim(0, 1.05)
    fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10, pad=0.12)

    # --- Plot 3: Resonanzentropie ---
    ax3 = fig.add_subplot(133, projection='3d')
    surf3 = ax3.plot_surface(
        tau_grid, A_grid, S,
        cmap='viridis', edgecolor='none')
    ax3.set_title(
        r"Resonanzentropie "
        r"$S = -\varepsilon \ln \varepsilon$"
        "\n(Axiom A5)")
    ax3.set_xlabel(r'Verstimmung $\tau$')
    ax3.set_ylabel(r'Amplitude $A$')
    ax3.set_zlabel(r'Entropie $S$')
    fig.colorbar(surf3, ax=ax3, shrink=0.5, aspect=10, pad=0.12)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    if show:
        plt.show()
    plt.close(fig)


if __name__ == "__main__":
    # Eingabeparameter
    A = np.linspace(0.1, 5, 500)
    tau = np.linspace(0.1, 5, 500)

    # Berechnung
    E_res, tau_grid, A_grid = berechne_resonanzenergie(A, tau)
    eps = berechne_kopplungseffizienz(E_res, A_grid)
    S = berechne_resonanzentropie(eps)

    # Konsolen-Output
    print("Resonanzfeldtheorie — Numerische Demonstration")
    print("=" * 50)
    print(f"A ∈ [{A[0]:.1f}, {A[-1]:.1f}], "
          f"τ ∈ [{tau[0]:.1f}, {tau[-1]:.1f}]")
    print(f"E_res ∈ [{E_res.min():.4f}, {E_res.max():.4f}]")
    print(f"ε ∈ [{eps.min():.4f}, {eps.max():.4f}]")
    print(f"S ∈ [{S.min():.4f}, {S.max():.4f}]")
    print(f"S_max bei ε = 1/e ≈ {1/np.e:.4f}: "
          f"S = {1/np.e:.4f}")
    print()
    print("Hinweis: Dies ist eine numerische Demonstration")
    print("der Axiom-Konsistenz, kein empirischer Beweis.")
    print("Für empirische Validierung siehe Monte-Carlo-Analyse.")
    print("=" * 50)

    # Visualisierung
    plot_numerische_demonstration(tau_grid, A_grid, E_res, eps, S,
                      save_path="plot.png", show=True)