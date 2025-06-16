import numpy as np
from numba import njit, prange

@njit(parallel=True)
def step_field_3d_parallel(eps, eps_old, m, lmbda, dt, dx):
    N = eps.shape[0]
    eps_new = np.zeros_like(eps)
    for i in prange(1, N-1):
        for j in prange(1, N-1):
            for k in prange(1, N-1):
                lap = (
                    eps[i+1,j,k] + eps[i-1,j,k] +
                    eps[i,j+1,k] + eps[i,j-1,k] +
                    eps[i,j,k+1] + eps[i,j,k-1] -
                    6 * eps[i,j,k]
                ) / dx**2
                Vp = m**2 * eps[i,j,k] + lmbda * eps[i,j,k]**3
                eps_new[i,j,k] = 2*eps[i,j,k] - eps_old[i,j,k] + dt**2 * (lap - Vp)
    return eps_new

def field_3d_sim_parallel(
    N=64, L=10.0, dt=0.004, steps=300, m=1.0, lmbda=0.2, 
    initial_bump_size=5, bump_value=1.0, callback=None
):
    dx = L/N
    eps = np.zeros((N,N,N))
    ix = iy = iz = N//2
    half = initial_bump_size // 2
    eps[ix-half:ix+half+1, iy-half:iy+half+1, iz-half:iz+half+1] = bump_value
    eps_old = eps.copy()

    for step in range(steps):
        eps_new = step_field_3d_parallel(eps, eps_old, m, lmbda, dt, dx)
        # Dirichlet-Randbedingung
        eps_new[0,:,:] = eps_new[-1,:,:] = eps_new[:,0,:] = eps_new[:,-1,:] = eps_new[:,:,0] = eps_new[:,:,-1] = 0
        eps_old, eps = eps, eps_new
        if callback is not None:
            callback(eps, step)
    return eps