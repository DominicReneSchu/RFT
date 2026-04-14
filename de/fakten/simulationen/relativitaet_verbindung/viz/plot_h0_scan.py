"""Visualisierung Stufe 6a: d_eta(H0) — Vorhersagekurve."""

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt


def plot_h0_scan(fit_result: dict[str, Any], save_path: str | None = None, show: bool = True) -> None:
    """Plottet d_eta als Funktion von H0 mit linearem Fit.

    Zwei Panels:
        Links:  d_eta(H0) mit Fit und Planck/SH0ES-Markierungen
        Rechts: Einzelne eta-Phasenscans fuer ausgewaehlte H0-Werte
    """
    h0 = fit_result["h0_values"]
    d_eta = fit_result["d_eta_mean"]
    d_std = fit_result["d_eta_std"]
    d_flat = fit_result["d_eta_flat"]
    valid = np.isfinite(d_eta)

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # === Panel 1: d_eta(H0) ===
    ax = axes[0]

    # Datenpunkte mit Fehlerbalken
    ax.errorbar(
        h0[valid], d_eta[valid], yerr=d_std[valid],
        fmt="o", color="tab:blue", markersize=7,
        ecolor="tab:blue", elinewidth=1, capsize=3,
        label="Simulation", zorder=5,
    )

    # Linearer Fit
    if fit_result["fit_poly"] is not None:
        h0_fine = np.linspace(h0[0] - 2, h0[-1] + 2, 200)
        d_fit = np.polyval(fit_result["fit_poly"], h0_fine)
        slope = fit_result["fit_slope"]
        ax.plot(
            h0_fine, d_fit, "--", color="tab:red", linewidth=2,
            label=f"Fit: dd_eta/dH0 = {slope:.5f} / (km/s/Mpc)",
        )

    # Referenz: Flache Raumzeit
    ax.axhline(
        d_flat, color="tab:green", linewidth=1.5, linestyle=":",
        label=f"Flach (H=0): d_eta = {d_flat:.4f}",
    )

    # Planck und SH0ES Markierungen
    h0_planck, h0_shoes = 67.4, 73.0
    for h0_val, name, color, marker in [
        (h0_planck, "Planck 2018", "tab:purple", "s"),
        (h0_shoes, "SH0ES", "tab:orange", "D"),
    ]:
        if fit_result["fit_poly"] is not None:
            d_pred = np.polyval(fit_result["fit_poly"], h0_val)
            ax.plot(
                h0_val, d_pred, marker, color=color, markersize=12,
                markeredgecolor="black", markeredgewidth=1,
                label=f"{name}: H0={h0_val}, d_eta={d_pred:.4f}",
                zorder=10,
            )
            ax.axvline(h0_val, color=color, linewidth=0.8, alpha=0.4)

    ax.set_xlabel("H0  [km/s/Mpc]", fontsize=12)
    ax.set_ylabel("<|d_eta|>  (mittlere Abweichung von cos^2)", fontsize=12)
    ax.set_title(
        "Resonanzfeldtheorie: d_eta(H0)\n"
        "Vorhersage: Hubble-Reibung verschiebt eta monoton",
        fontsize=12, fontweight="bold",
    )
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(True, alpha=0.3)

    # === Panel 2: Ausgewaehlte Phasenscans ===
    ax2 = axes[1]
    dphi_fine = np.linspace(0, np.pi, 200)
    ax2.plot(
        dphi_fine, np.cos(dphi_fine / 2)**2,
        "--", color="black", linewidth=2, label="cos^2(dphi/2)", zorder=10,
    )

    # 5 gleichmaessig verteilte H0-Werte auswaehlen
    n_show = min(5, len(h0))
    indices = np.linspace(0, len(h0) - 1, n_show, dtype=int)
    colors = plt.cm.coolwarm(np.linspace(0, 1, n_show))

    for idx, clr in zip(indices, colors):
        scan = fit_result["eta_scans"][idx]
        dphi = scan["delta_phi_values"]
        eta = scan["eta_mean"]
        v = np.isfinite(eta)
        if np.any(v):
            ax2.scatter(
                dphi[v], eta[v], color=clr, s=50, zorder=5,
                edgecolors="black", linewidths=0.5,
                label=f"H0 = {h0[idx]:.1f}",
            )

    ax2.set_xlabel("Phasendifferenz dphi_0  [rad]", fontsize=12)
    ax2.set_ylabel("Kopplungseffizienz eta", fontsize=12)
    ax2.set_title(
        "Phasenscans bei verschiedenen H0\n"
        "Staerkere Expansion -> staerkere Abweichung",
        fontsize=12, fontweight="bold",
    )
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(-0.1, np.pi + 0.1)
    ax2.set_ylim(-0.05, 1.15)

    plt.suptitle(
        "Stufe 6a: Kosmologische Skalierung der Resonanzfeldkopplung",
        fontsize=14, fontweight="bold",
    )
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)


def plot_hubble_tension(tension: dict[str, Any], fit_result: dict[str, Any], save_path: str | None = None, show: bool = True) -> None:
    """Detailplot: Hubble-Spannungs-Signatur."""
    fig, ax = plt.subplots(figsize=(10, 7))

    h0 = fit_result["h0_values"]
    d_eta = fit_result["d_eta_mean"]
    valid = np.isfinite(d_eta)

    ax.plot(h0[valid], d_eta[valid], "o-", color="tab:blue",
            markersize=6, linewidth=1, label="Simulation")

    # Planck-Band
    ax.axvspan(67.4 - 0.5, 67.4 + 0.5, alpha=0.15, color="tab:purple",
               label="Planck 2018: 67.4 +/- 0.5")
    # SH0ES-Band
    ax.axvspan(73.0 - 1.0, 73.0 + 1.0, alpha=0.15, color="tab:orange",
               label="SH0ES: 73.0 +/- 1.0")

    # Vorhergesagte Werte
    ax.plot(tension["h0_planck"], tension["d_eta_planck"], "s",
            color="tab:purple", markersize=14, markeredgecolor="black",
            markeredgewidth=1.5, zorder=10)
    ax.plot(tension["h0_shoes"], tension["d_eta_shoes"], "D",
            color="tab:orange", markersize=14, markeredgecolor="black",
            markeredgewidth=1.5, zorder=10)

    # Verbindungslinie
    ax.annotate(
        "", xy=(tension["h0_shoes"], tension["d_eta_shoes"]),
        xytext=(tension["h0_planck"], tension["d_eta_planck"]),
        arrowprops=dict(arrowstyle="<->", color="red", linewidth=2),
    )
    mid_h0 = (tension["h0_planck"] + tension["h0_shoes"]) / 2
    mid_d = (tension["d_eta_planck"] + tension["d_eta_shoes"]) / 2
    ax.text(
        mid_h0, mid_d + 0.005,
        f"Delta d_eta = {tension['delta_d_eta']:.4f}\n"
        f"({tension['relative_shift']:.1f}% Verschiebung)",
        ha="center", fontsize=11, color="red", fontweight="bold",
        bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.9),
    )

    ax.set_xlabel("H0  [km/s/Mpc]", fontsize=13)
    ax.set_ylabel("<|d_eta|>", fontsize=13)
    ax.set_title(
        "Resonanzfeld-Signatur der Hubble-Spannung\n"
        f"dd_eta/dH0 = {tension['slope']:.5f} / (km/s/Mpc)",
        fontsize=13, fontweight="bold",
    )
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    plt.close(fig)