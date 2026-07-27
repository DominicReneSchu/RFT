"""Start script: 3D resonance field simulation with live visualisation."""

import matplotlib.pyplot as plt
import numpy as np
from config import MODEL_PARAMS, NUMERIC_PARAMS, VIS_PARAMS
from core.field_3d import field_3d_sim
from viz.plot_3d import live_slice_and_mean

N = NUMERIC_PARAMS["grid_3d"]
steps = NUMERIC_PARAMS["steps_3d"]
dt = NUMERIC_PARAMS["dt_3d"]

means = []
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

im = ax1.imshow(
    np.zeros((N, N)), origin='lower',
    cmap=VIS_PARAMS["colormap"],
    vmin=VIS_PARAMS["vmin"],
    vmax=VIS_PARAMS["vmax"],
)
ax1.set_title(f"Slice z = {N // 2}")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

line2, = ax2.plot([], [])
ax2.set_xlabel("Simulation step")
ax2.set_ylabel("⟨|ε|⟩")
ax2.set_title("Mean field amplitude |ε|")

fig_ax = (ax1, ax2, im, line2)

eps = field_3d_sim(
    N=N,
    L=NUMERIC_PARAMS["L_3d"],
    dt=dt,
    steps=steps,
    m=MODEL_PARAMS["m"],
    lmbda=MODEL_PARAMS["lmbda"],
    callback=lambda eps, step: live_slice_and_mean(
        eps, step,
        slice_idx=N // 2,
        means=means,
        fig_ax=fig_ax,
        update_interval=VIS_PARAMS["update_interval"],
    ),
)

plt.tight_layout()
plt.show()
