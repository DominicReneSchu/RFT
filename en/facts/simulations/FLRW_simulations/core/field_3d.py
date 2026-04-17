"""
3D resonance field simulation on a cubic lattice.

Solves the nonlinear wave equation:
    ∂²ε/∂t² = ∇²ε - dV/dε
with V(ε) = ½m²ε² + ¼λε⁴ via explicit time evolution
(Leapfrog/Verlet) and Dirichlet boundary conditions (ε = 0 at boundary).

Physical context:
    - Klein–Gordon equation with nonlinear potential
    - Discretisation via finite differences (7-point Laplacian)
    - Initial condition: localised bump at the centre

Axiom reference:
    - A1: The field oscillates in the potential
    - A2: Superposition of lattice modes
    - A4: The self-coupling λ governs the nonlinear dynamics

Dependencies: numpy
"""

import numpy as np


def field_3d_sim(
    N=64, L=10.0, dt=0.004, steps=300, m=1.0, lmbda=0.2,
    initial_bump_size=5, bump_value=1.0, callback=None
):
    """Runs the 3D resonance field simulation.

    Parameters
    ----------
    N : int
        Grid points per dimension
    L : float
        Physical length of the grid
    dt : float
        Time step
    steps : int
        Number of time steps
    m : float
        Field mass
    lmbda : float
        Self-coupling constant
    initial_bump_size : int
        Width of the initial excitation (voxels)
    bump_value : float
        Amplitude of the initial excitation
    callback : callable or None
        callback(eps, step) is called after each step

    Returns
    -------
    eps : ndarray, shape (N, N, N)
        Field configuration after the last time step
    """
    dx = L / N
    eps = np.zeros((N, N, N))

    # Initial condition: localised bump at the centre
    ix = iy = iz = N // 2
    half = initial_bump_size // 2
    eps[ix-half:ix+half+1, iy-half:iy+half+1, iz-half:iz+half+1] = bump_value
    eps_old = eps.copy()

    def Vp(eps):
        """Potential derivative: dV/dε = m²ε + λε³"""
        return m**2 * eps + lmbda * eps**3

    for step in range(steps):
        # 7-point Laplacian (finite differences)
        lap = (
            np.roll(eps, 1, axis=0) + np.roll(eps, -1, axis=0) +
            np.roll(eps, 1, axis=1) + np.roll(eps, -1, axis=1) +
            np.roll(eps, 1, axis=2) + np.roll(eps, -1, axis=2) -
            6 * eps
        ) / dx**2

        # Leapfrog/Verlet time evolution
        eps_new = 2 * eps - eps_old + dt**2 * (lap - Vp(eps))

        # Dirichlet boundary conditions
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
