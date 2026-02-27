# -*- coding: utf-8 -*-
# Schu-Resonanzfeldtheorie – Kompakter numerischer Beweis
# © Dominic Schu, 2025 – Alle Rechte vorbehalten.
# Theorie siehe auch: https://github.com/DominicReneSchu/Resoshift und Pi-e-Theorie

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
    Berechnet die Schu-Resonanzenergie:
        E_res = A / (1 + ((ω_ext - ω_0) / γ)²)
    wobei:
        ω_ext = ω_0 · (1 + sin(T))

    Args:
        A (ndarray): Amplituden (1D, positiv)
        T (ndarray): Temperaturen (1D, positiv)
        omega_0 (float): Eigenfrequenz
        gamma (float): Dämpfungskonstante

    Returns:
        (E_res, T_grid, A_grid): Clipped Resonanzenergie und Gitter
    """
    if np.any(A <= 0) or np.any(T <= 0):
        raise ValueError("Alle Werte von A und T müssen > 0 sein (physikalisch sinnvoll).")
    if A.ndim != 1 or T.ndim != 1:
        raise ValueError("A und T müssen 1D-Arrays sein.")

    T_grid, A_grid = np.meshgrid(T, A)
    omega_ext = omega_0 * (1 + np.sin(T_grid))
    E_res = A_grid / (1 + ((omega_ext - omega_0) / gamma) ** 2)
    return np.clip(E_res, 1e-8, None), T_grid, A_grid

def berechne_resonanzentropie(E_res: np.ndarray) -> np.ndarray:
    """
    Berechnet die Resonanzentropie gemäß:
        S = –E_res · ln(E_res)

    Args:
        E_res (ndarray): Resonanzenergie (muss > 0)

    Returns:
        S (ndarray): Entropie
    """
    if np.any(E_res <= 0):
        raise ValueError("Alle Werte von E_res müssen > 0 sein (numerische Stabilität).")
    return -E_res * np.log(E_res)

def plot_resonanzfeld(
    T_grid: np.ndarray,
    A_grid: np.ndarray,
    E_res: np.ndarray,
    S: np.ndarray,
    save_path: str = None,
    show: bool = True
):
    """
    Erstellt zwei 3D-Plots: Schu-Resonanzenergie und Resonanzentropie.

    Args:
        T_grid, A_grid (ndarray): Gitter für T und A
        E_res (ndarray): Resonanzenergie
        S (ndarray): Entropie
        save_path (str): Optionaler Dateiname zum Speichern des Plots
        show (bool): Ob Plot angezeigt werden soll
    """
    fig = plt.figure(figsize=(14, 6))
    # Plot 1: Resonanzenergie
    ax1 = fig.add_subplot(121, projection='3d')
    surf1 = ax1.plot_surface(T_grid, A_grid, E_res, cmap='inferno', edgecolor='none')
    ax1.set_title("Schu-Resonanzenergie $E_{res}$")
    ax1.set_xlabel('Temperatur $T$')
    ax1.set_ylabel('Amplitude $A$')
    ax1.set_zlabel('$E_{res}$')
    fig.colorbar(surf1, ax=ax1, shrink=0.6, aspect=10, pad=0.1)
    # Plot 2: Entropie
    ax2 = fig.add_subplot(122, projection='3d')
    surf2 = ax2.plot_surface(T_grid, A_grid, S, cmap='viridis', edgecolor='none')
    ax2.set_title("Resonanzentropie $S$")
    ax2.set_xlabel('Temperatur $T$')
    ax2.set_ylabel('Amplitude $A$')
    ax2.set_zlabel('Entropie $S$')
    fig.colorbar(surf2, ax=ax2, shrink=0.6, aspect=10, pad=0.1)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)

if __name__ == "__main__":
    # === Eingabeparameter (normiert, physikalisch plausibel) ===
    A = np.linspace(0.1, 5, 500)
    T = np.linspace(0.1, 5, 500)
    # === Berechnung ===
    E_res, T_grid, A_grid = berechne_resonanzenergie(A, T)
    S = berechne_resonanzentropie(E_res)
    # === Visualisierung (optional abspeicherbar) ===
    plot_resonanzfeld(T_grid, A_grid, E_res, S, save_path=None, show=True)