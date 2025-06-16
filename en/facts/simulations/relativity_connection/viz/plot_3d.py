import matplotlib.pyplot as plt
import numpy as np

def live_slice_and_mean(eps, step, slice_idx=None, means=None, fig_ax=None):
    if slice_idx is None:
        slice_idx = eps.shape[2]//2
    if means is not None:
        means.append(np.mean(eps))
    if fig_ax is not None and step % 10 == 0:
        ax1, ax2, im, line2 = fig_ax
        im.set_data(eps[:,:,slice_idx])
        line2.set_data(np.arange(len(means)), means)
        ax2.set_xlim(0, step//10 + 1)
        plt.pause(0.01)