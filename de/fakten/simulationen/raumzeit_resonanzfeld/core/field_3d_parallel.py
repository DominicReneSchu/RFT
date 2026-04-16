"""
3D-Resonanzfeldsimulation — Numba-parallelisierte Variante.

Identische Physik wie field_3d.py, aber mit @njit(parallel=True)
für deutlich schnellere Berechnung auf Mehrkern-CPUs.

Voraussetzung: pip install numba

Abhängigkeiten: numpy, numba
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
from numba import njit, prange


@njit(parallel=True)
def step_field_3d_parallel(eps: np.ndarray, eps_old: np.ndarray, m: float, lmbda: float, dt: float, dx: float) -> np.ndarray:
    """Ein Zeitschritt der 3D-Wellengleichung (parallelisiert).

    Parameters
    ----------
    eps, eps_old : ndarray, shape (N, N, N)
        Aktuelle und vorherige Feldkonfiguration
    m, lmbda : float
        Masse und Selbstkopplung
    dt, dx : float
        Zeit- und Raumschritt

    Returns
    -------
    eps_new : ndarray, shape (N, N, N)
    """
    N = eps.shape[0]
    eps_new = np.zeros_like(eps)
    for i in prange(1, N - 1):
        for j in prange(1, N - 1):
            for k in prange(1, N - 1):
                lap = (
                    eps[i+1, j, k] + eps[i-1, j, k] +
                    eps[i, j+1, k] + eps[i, j-1, k] +
                    eps[i, j, k+1] + eps[i, j, k-1] -
                    6 * eps[i, j, k]
                ) / dx**2
                Vp = m**2 * eps[i, j, k] + lmbda * eps[i, j, k]**3
                eps_new[i, j, k] = (
                    2 * eps[i, j, k] - eps_old[i, j, k]
                    + dt**2 * (lap - Vp)
                )
    return eps_new


def field_3d_sim_parallel(
    N: int = 64, L: float = 10.0, dt: float = 0.004, steps: int = 300, m: float = 1.0, lmbda: float = 0.2,
    initial_bump_size: int = 5, bump_value: float = 1.0, callback: Callable[[np.ndarray, int], None] | None = None
) -> np.ndarray:
    """3D-Simulation mit Numba-Parallelisierung.

    Parameter und Rückgabe identisch zu field_3d.field_3d_sim.
    """
    dx = L / N
    eps = np.zeros((N, N, N))
    ix = iy = iz = N // 2
    half = initial_bump_size // 2
    eps[ix-half:ix+half+1, iy-half:iy+half+1, iz-half:iz+half+1] = bump_value
    eps_old = eps.copy()

    for step in range(steps):
        eps_new = step_field_3d_parallel(eps, eps_old, m, lmbda, dt, dx)
        # Dirichlet-Randbedingungen
        eps_new[0, :, :] = 0
        eps_new[-1, :, :] = 0
        eps_new[:, 0, :] = 0
        eps_new[:, -1, :] = 0
        eps_new[:, :, 0] = 0
        eps_new[:, :, -1] = 0
        eps_old, eps = eps, eps_new
        if callback is not None:
            callback(eps, step)

    return eps