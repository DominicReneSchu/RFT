"""
Live visualisation of the 3D resonance field simulation.

Shows a z-slice of the field and the time evolution
of the mean field amplitude.
"""

import matplotlib.pyplot as plt
import numpy as np


def live_slice_and_mean(
    eps, step, slice_idx=None, means=None, fig_ax=None,
    update_interval=10
):
    """Updates the live plots during the 3D simulation.

    Parameters
    ----------
    eps : ndarray, shape (N, N, N)
        Current field configuration
    step : int
        Current simulation step
    slice_idx : int or None
        z-index of the slice (default: centre)
    means : list
        Filled with ⟨|ε|⟩ per step
    fig_ax : tuple
        (ax1, ax2, im, line2) — Matplotlib objects
    update_interval : int
        Plot is updated only every N steps
    """
    if slice_idx is None:
        slice_idx = eps.shape[2] // 2

    if means is not None:
        means.append(np.mean(np.abs(eps)))

    if fig_ax is not None and step % update_interval == 0:
        ax1, ax2, im, line2 = fig_ax
        im.set_data(eps[:, :, slice_idx])
        line2.set_data(np.arange(len(means)), means)
        ax2.set_xlim(0, len(means) + 1)

        # Dynamic y-axis: always from 0, upper limit = maximum * 1.3
        current_max = max(means) if means else 0.01
        ax2.set_ylim(0, max(current_max * 1.3, 1e-4))

        plt.pause(0.01)
