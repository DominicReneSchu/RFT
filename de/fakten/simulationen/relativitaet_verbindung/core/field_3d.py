"""
3D-Resonanzfeldsimulation auf einem kubischen Gitter.

Löst die nichtlineare Wellengleichung:
    ∂²ε/∂t² = ∇²ε - dV/dε
mit V(ε) = ½m²ε² + ¼λε⁴ über explizite Zeitentwicklung
(Leapfrog/Verlet) und Dirichlet-Randbedingungen (ε = 0 am Rand).

Physikalischer Kontext:
    - Klein-Gordon-Gleichung mit nichtlinearem Potential
    - Diskretisierung über finite Differenzen (7-Punkt-Laplace)
    - Anfangsbedingung: lokalisierter Bump im Zentrum

Axiom-Bezug:
    - A1: Das Feld schwingt im Potential
    - A2: Superposition der Gittermoden
    - A4: Die Selbstkopplung λ bestimmt die nichtlineare Dynamik

Abhängigkeiten: numpy
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np


def field_3d_sim(
    N: int = 64, L: float = 10.0, dt: float = 0.004, steps: int = 300, m: float = 1.0, lmbda: float = 0.2,
    initial_bump_size: int = 5, bump_value: float = 1.0, callback: Callable[[np.ndarray, int], None] | None = None
) -> np.ndarray:
    """Führt die 3D-Resonanzfeldsimulation durch.

    Parameters
    ----------
    N : int
        Gitterpunkte pro Dimension
    L : float
        Physikalische Länge des Gitters
    dt : float
        Zeitschritt
    steps : int
        Anzahl der Zeitschritte
    m : float
        Feldmasse
    lmbda : float
        Selbstkopplungskonstante
    initial_bump_size : int
        Breite der Anfangsanregung (Voxel)
    bump_value : float
        Amplitude der Anfangsanregung
    callback : callable or None
        callback(eps, step) wird nach jedem Schritt aufgerufen

    Returns
    -------
    eps : ndarray, shape (N, N, N)
        Feldkonfiguration nach dem letzten Zeitschritt
    """
    dx = L / N
    eps = np.zeros((N, N, N))

    # Anfangsbedingung: lokalisierter Bump im Zentrum
    ix = iy = iz = N // 2
    half = initial_bump_size // 2
    eps[ix-half:ix+half+1, iy-half:iy+half+1, iz-half:iz+half+1] = bump_value
    eps_old = eps.copy()

    def Vp(eps: np.ndarray) -> np.ndarray:
        """Potentialableitung: dV/dε = m²ε + λε³"""
        return m**2 * eps + lmbda * eps**3

    for step in range(steps):
        # 7-Punkt-Laplace (finite Differenzen)
        lap = (
            np.roll(eps, 1, axis=0) + np.roll(eps, -1, axis=0) +
            np.roll(eps, 1, axis=1) + np.roll(eps, -1, axis=1) +
            np.roll(eps, 1, axis=2) + np.roll(eps, -1, axis=2) -
            6 * eps
        ) / dx**2

        # Leapfrog/Verlet-Zeitentwicklung
        eps_new = 2 * eps - eps_old + dt**2 * (lap - Vp(eps))

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