import numpy as np

def field_3d_sim(
    N=64, L=10.0, dt=0.004, steps=300, m=1.0, lmbda=0.2, 
    initial_bump_size=5, bump_value=1.0, callback=None
):
    dx = L/N
    eps = np.zeros((N,N,N))
    ix = iy = iz = N//2
    half = initial_bump_size // 2
    eps[ix-half:ix+half+1, iy-half:iy+half+1, iz-half:iz+half+1] = bump_value
    eps_old = eps.copy()

    def Vp(eps):
        return m**2 * eps + lmbda * eps**3

    for step in range(steps):
        lap = (
            np.roll(eps, 1, axis=0) + np.roll(eps, -1, axis=0) +
            np.roll(eps, 1, axis=1) + np.roll(eps, -1, axis=1) +
            np.roll(eps, 1, axis=2) + np.roll(eps, -1, axis=2) -
            6 * eps
        ) / dx**2
        eps_new = 2*eps - eps_old + dt**2 * (lap - Vp(eps))
        # Randbedingungen (Dirichlet)
        eps_new[0,:,:] = eps_new[-1,:,:] = eps_new[:,0,:] = eps_new[:,-1,:] = eps_new[:,:,0] = eps_new[:,:,-1] = 0
        eps_old, eps = eps, eps_new
        if callback is not None:
            callback(eps, step)
    return eps