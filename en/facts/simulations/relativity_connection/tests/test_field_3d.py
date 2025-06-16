import numpy as np
from core.field_3d import field_3d_sim

def test_field_3d_shape_and_stability():
    eps = field_3d_sim(N=16, steps=10)  # Kleines Gitter für schnellen Test
    # Test: Shape stimmt
    assert eps.shape == (16,16,16)
    # Test: Werte bleiben endlich
    assert np.all(np.isfinite(eps))
    # Test: Randwerte sind null (Dirichlet)
    assert np.all(eps[0,:,:] == 0)
    assert np.all(eps[-1,:,:] == 0)
    assert np.all(eps[:,0,:] == 0)
    assert np.all(eps[:,-1,:] == 0)
    assert np.all(eps[:,:,0] == 0)
    assert np.all(eps[:,:,-1] == 0)
