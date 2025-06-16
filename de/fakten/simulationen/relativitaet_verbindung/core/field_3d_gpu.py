try:
    import cupy as cp
except ImportError:
    cp = None

def field_3d_sim_gpu(
    N=64, L=10.0, dt=0.004, steps=300, m=1.0, lmbda=0.2, 
    initial_bump_size=5, bump_value=1.0, callback=None
):
    if cp is None:
        raise ImportError("CuPy is not installed. Please install cupy for GPU support.")
    dx = L/N
    eps = cp.zeros((N,N,N), dtype=cp.float32)
    ix = iy = iz = N//2
    half = initial_bump_size // 2
    eps[ix-half:ix+half+1, iy-half:iy+half+1, iz-half:iz+half+1] = bump_value
    eps_old = eps.copy()
    for step in range(steps):
        lap = (
            cp.roll(eps, 1, axis=0) + cp.roll(eps, -1, axis=0) +
            cp.roll(eps, 1, axis=1) + cp.roll(eps, -1, axis=1) +
            cp.roll(eps, 1, axis=2) + cp.roll(eps, -1, axis=2) -
            6 * eps
        ) / dx**2
        Vp = m**2 * eps + lmbda * eps**3
        eps_new = 2*eps - eps_old + dt**2 * (lap - Vp)
        eps_new[0,:,:] = eps_new[-1,:,:] = eps_new[:,0,:] = eps_new[:,-1,:] = eps_new[:,:,0] = eps_new[:,:,-1] = 0
        eps_old, eps = eps, eps_new
        if callback is not None:
            callback(cp.asnumpy(eps), step)
    return cp.asnumpy(eps)