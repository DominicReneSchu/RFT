# -*- coding: utf-8 -*-
# Schu Resonance Field Theory – Compact numerical demonstration
# © Dominic Schu, 2025 – All rights reserved.
# Theory: https://github.com/DominicReneSchu/Resoshift and Pi-e-Theory

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

def berechne_resonanzenergie(
    A: np.ndarray,
    T: np.ndarray,
    omega_0: float = 1.0,
    gamma: float = 0.2
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Calculates the Schu resonance energy:
        E_res = A / (1 + ((ω_ext - ω_0) / γ)²)
    where:
        ω_ext = ω_0 · (1 + sin(T))

    Args:
        A (ndarray): Amplitudes (1D, positive)
        T (ndarray): Time constants (1D, positive)
        omega_0 (float): Natural frequency
        gamma (float): Damping constant

    Returns:
        (E_res, T_grid, A_grid): Clipped resonance energy and grids
    """
    if np.any(A <= 0) or np.any(T <= 0):
        raise ValueError("All values of A and T must be > 0 (physically meaningful).")
    if A.ndim != 1 or T.ndim != 1:
        raise ValueError("A and T must be 1D arrays.")

    T_grid, A_grid = np.meshgrid(T, A)
    omega_ext = omega_0 * (1 + np.sin(T_grid))
    E_res = A_grid / (1 + ((omega_ext - omega_0) / gamma) ** 2)
    return np.clip(E_res, 1e-8, None), T_grid, A_grid

def berechne_resonanzentropie(E_res: np.ndarray) -> np.ndarray:
    """
    Calculates the resonance entropy according to:
        S = –E_res · ln(E_res)

    Args:
        E_res (ndarray): Resonance energy (must be > 0)

    Returns:
        S (ndarray): Entropy
    """
    if np.any(E_res <= 0):
        raise ValueError("All values of E_res must be > 0 (numerical stability).")
    return -E_res * np.log(E_res)

def plot_resonanzfeld(
    T_grid: np.ndarray,
    A_grid: np.ndarray,
    E_res: np.ndarray,
    S: np.ndarray,
    save_path: str | None = None,
    show: bool = True
) -> None:
    """
    Creates two 3D plots: Schu resonance energy and resonance entropy.

    Args:
        T_grid, A_grid (ndarray): Grids for T and A
        E_res (ndarray): Resonance energy
        S (ndarray): Entropy
        save_path (str): Optional filename to save the plot
        show (bool): Whether to display the plot
    """
    fig = plt.figure(figsize=(14, 6))
    # Plot 1: Resonance energy
    ax1 = fig.add_subplot(121, projection='3d')
    surf1 = ax1.plot_surface(T_grid, A_grid, E_res, cmap='inferno', edgecolor='none')
    ax1.set_title("Schu resonance energy $E_{res}$")
    ax1.set_xlabel('Time constant $T$')
    ax1.set_ylabel('Amplitude $A$')
    ax1.set_zlabel('$E_{res}$')
    fig.colorbar(surf1, ax=ax1, shrink=0.6, aspect=10, pad=0.1)
    # Plot 2: Entropy
    ax2 = fig.add_subplot(122, projection='3d')
    surf2 = ax2.plot_surface(T_grid, A_grid, S, cmap='viridis', edgecolor='none')
    ax2.set_title("Resonance entropy $S$")
    ax2.set_xlabel('Time constant $T$')
    ax2.set_ylabel('Amplitude $A$')
    ax2.set_zlabel('Entropy $S$')
    fig.colorbar(surf2, ax=ax2, shrink=0.6, aspect=10, pad=0.1)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)

if __name__ == "__main__":
    # === Input parameters (normalised, physically plausible) ===
    A = np.linspace(0.1, 5, 500)
    T = np.linspace(0.1, 5, 500)
    # === Calculation ===
    E_res, T_grid, A_grid = berechne_resonanzenergie(A, T)
    S = berechne_resonanzentropie(E_res)
    # === Visualisation (optionally saveable) ===
    plot_resonanzfeld(T_grid, A_grid, E_res, S, save_path=None, show=True)
