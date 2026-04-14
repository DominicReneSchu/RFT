"""
Live-Visualisierung der 3D-Resonanzfeldsimulation.

Zeigt einen z-Schnitt des Felds und den zeitlichen Verlauf
der mittleren Feldamplitude.
"""

from __future__ import annotations

from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def live_slice_and_mean(
    eps: np.ndarray, step: int, slice_idx: int | None = None, means: list[float] | None = None, fig_ax: tuple[Any, Any, Any, Any] | None = None,
    update_interval: int = 10
) -> None:
    """Aktualisiert die Live-Plots während der 3D-Simulation.

    Parameters
    ----------
    eps : ndarray, shape (N, N, N)
        Aktuelle Feldkonfiguration
    step : int
        Aktueller Simulationsschritt
    slice_idx : int or None
        z-Index des Schnitts (Default: Mitte)
    means : list
        Wird mit ⟨|ε|⟩ pro Schritt befüllt
    fig_ax : tuple
        (ax1, ax2, im, line2) — Matplotlib-Objekte
    update_interval : int
        Nur alle N Schritte wird der Plot aktualisiert
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

        # Dynamische y-Achse: immer ab 0, Obergrenze = Maximum * 1.3
        current_max = max(means) if means else 0.01
        ax2.set_ylim(0, max(current_max * 1.3, 1e-4))

        plt.pause(0.01)