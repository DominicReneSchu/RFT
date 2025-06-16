import matplotlib.pyplot as plt
import numpy as np
from core.field_3d import field_3d_sim
from viz.plot_3d import live_slice_and_mean

N = 64
means = []
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
im = ax1.imshow(np.zeros((N,N)), origin='lower', cmap='RdBu', vmin=-1, vmax=1)
ax1.set_title(f"Schnitt z={N//2}")
line2, = ax2.plot([], [])
ax2.set_ylim(-0.1,1.1)
ax2.set_title("Mittelwert ε")
fig_ax = (ax1, ax2, im, line2)

eps = field_3d_sim(N=N, steps=300, callback=lambda eps, step: live_slice_and_mean(eps, step, slice_idx=N//2, means=means, fig_ax=fig_ax))
plt.show()