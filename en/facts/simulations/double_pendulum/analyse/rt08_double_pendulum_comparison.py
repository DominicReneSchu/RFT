"""
RT-08 — Double Pendulum: Experimental Data vs. RFT Prediction

This script compares the RFT coupling efficiency
    ε_RFT(Δφ) = cos²(Δφ/2)   (Axiom 4)
against an experimental or synthetic reference via χ² fit.

Data strategy:
    Primary:  Pass a CSV path via command line or environment variable
              RT08_DATA_FILE.
    Fallback: Synthetic reference data from pure Lagrange mechanics
              (A = 0, no RFT term) — a valid null hypothesis when no
              public experimental data are available.

Synthetic data:
    Source:   Lagrange double pendulum simulation (double_pendulum.py), A = 0
    Licence:  MIT (this repository), no external dataset
    DOI:      — (synthetic)

Experimental CSV data (optional):
    Recommended source: Zenodo – "double pendulum experimental data"
    Example DOI: https://doi.org/10.5281/zenodo.XXXXXXX (placeholder)
    Licence: CC-BY 4.0 (verify per dataset)
    Expected format: CSV with header, columns: t, theta1, theta2
                     or t, x1, y1, x2, y2

Falsification criterion (sharp):
    χ²_red ≤ 1.5               → RFT formula not falsified (confirmed)
    1.5 < χ²_red ≤ 2.0         → Borderline, interpretation open
    χ²_red > 2.0                → RFT formula rejected by data (5% level)

Output:
    - Table on stdout
    - 4 plots as PNG: rt08_scatter.png, rt08_timeseries.png,
                      rt08_residuals.png, rt08_chi2dist.png

Usage:
    cd en/facts/simulations/double_pendulum/analyse
    python rt08_double_pendulum_comparison.py [path/to/data.csv]

© Dominic-René Schu, 2025/2026 — Resonance Field Theory
"""

from __future__ import annotations

import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.stats import chi2 as chi2_dist, norm as norm_dist

# Add simulation directory to search path
_sim_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, _sim_dir)

from double_pendulum import (
    load_experimental_data,
    compute_epsilon_from_data,
    rft_epsilon_prediction,
    chi2_fit,
)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Synthetic reference data (Lagrange, A = 0)
# ---------------------------------------------------------------------------

def generate_synthetic_reference(
    t_end: float = 30.0,
    dt: float = 0.02,
    theta1_0: float = np.pi / 3,
    theta2_0: float = np.pi / 2 + 0.3,
    m1: float = 1.0,
    m2: float = 1.0,
    L1: float = 1.0,
    L2: float = 1.0,
) -> dict:
    """Synthetic double pendulum without RFT term (A = 0) as null hypothesis.

    Integration uses Runge-Kutta RK45 (scipy).  Initial conditions are
    deliberately slightly asymmetric to capture a representative chaotic regime.
    """
    g = 9.81

    def derivatives(t, state):
        theta1, omega1, theta2, omega2 = state
        delta = theta2 - theta1
        denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) ** 2
        denom2 = (L2 / L1) * denom1

        dtheta1_dt = omega1
        domega1_dt = (
            m2 * L1 * omega1 ** 2 * np.sin(delta) * np.cos(delta)
            + m2 * g * np.sin(theta2) * np.cos(delta)
            + m2 * L2 * omega2 ** 2 * np.sin(delta)
            - (m1 + m2) * g * np.sin(theta1)
        ) / denom1

        dtheta2_dt = omega2
        domega2_dt = (
            -m2 * L2 * omega2 ** 2 * np.sin(delta) * np.cos(delta)
            + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
            - (m1 + m2) * L1 * omega1 ** 2 * np.sin(delta)
            - (m1 + m2) * g * np.sin(theta2)
        ) / denom2

        return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

    t_eval = np.arange(0, t_end, dt)
    sol = solve_ivp(
        derivatives,
        (0, t_end),
        [theta1_0, 0.0, theta2_0, 0.0],
        t_eval=t_eval,
        method="RK45",
        rtol=1e-9,
        atol=1e-12,
    )

    theta1 = sol.y[0]
    theta2 = sol.y[2]
    delta_phi = theta2 - theta1

    return {
        "t": sol.t,
        "theta1": theta1,
        "theta2": theta2,
        "delta_phi": delta_phi,
    }


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def run_analysis(data_filepath: str | None = None) -> None:
    """Load data, perform χ² fit, and create four plots."""

    # --- Load or generate data ---
    if data_filepath is not None:
        print(f"Loading experimental data: {data_filepath}")
        data = load_experimental_data(data_filepath)
        data_label = "Experimental"
        data_source = f"File: {os.path.basename(data_filepath)}"
    else:
        print("No data path provided — generating synthetic reference data (A=0, Lagrange).")
        data = generate_synthetic_reference()
        data_label = "Synthetic (Lagrange, A=0)"
        data_source = "Double pendulum simulation (double_pendulum.py), A=0, no RFT term"

    t = data["t"]
    delta_phi = data["delta_phi"]

    epsilon_exp = compute_epsilon_from_data(delta_phi)
    epsilon_rft = rft_epsilon_prediction(delta_phi)

    result = chi2_fit(delta_phi, epsilon_exp)

    chi2_val = result["chi2"]
    chi2_red = result["chi2_reduced"]
    dof = result["dof"]
    p_value = result["p_value"]
    residuals = result["residuals"]
    verdict = result["verdict"]

    # --- Console output ---
    print()
    print("RT-08 — Double Pendulum: ε_RFT vs. ε_exp")
    print("=" * 65)
    print(f"Data source:         {data_source}")
    print(f"N data points:       {len(delta_phi)}")
    print(f"Degrees of freedom:  {dof}")
    print("-" * 65)
    print(f"χ²:                  {chi2_val:.4f}")
    print(f"χ²_red:              {chi2_red:.4f}")
    print(f"p-value:             {p_value:.4f}")
    print(f"Residuals µ:         {np.mean(residuals):.4f}")
    print(f"Residuals σ:         {np.std(residuals):.4f}")
    print("-" * 65)

    # Falsification criterion
    if verdict == "confirmed":
        symbol = "✅"
        msg = "RFT formula not falsified (χ²_red ≤ 1.5)"
    elif verdict == "borderline":
        symbol = "⚠️ "
        msg = "Borderline: 1.5 < χ²_red ≤ 2.0 — interpretation open"
    else:
        symbol = "❌"
        msg = "RFT formula rejected by data (χ²_red > 2.0, 5% level)"

    print(f"{symbol} RESULT: {msg}")
    print("=" * 65)
    print()

    # --- Plots ---
    _plot_scatter(delta_phi, epsilon_rft, epsilon_exp, data_label, chi2_red, verdict)
    _plot_timeseries(t, delta_phi, epsilon_rft, epsilon_exp, data_label)
    _plot_residuals(residuals, data_label)
    _plot_chi2_distribution(chi2_val, dof, data_label)

    print(f"Plots saved to: {OUTPUT_DIR}")
    print("  rt08_scatter.png")
    print("  rt08_timeseries.png")
    print("  rt08_residuals.png")
    print("  rt08_chi2dist.png")


# ---------------------------------------------------------------------------
# Plots
# ---------------------------------------------------------------------------

def _plot_scatter(
    delta_phi: np.ndarray,
    epsilon_rft: np.ndarray,
    epsilon_exp: np.ndarray,
    data_label: str,
    chi2_red: float,
    verdict: str,
) -> None:
    """Plot 1: ε_RFT(Δθ) vs. ε_exp(Δθ) — scatter plot with residuals."""
    fig, (ax_main, ax_res) = plt.subplots(
        2, 1, figsize=(8, 7), gridspec_kw={"height_ratios": [3, 1]}, sharex=False
    )

    idx = np.argsort(delta_phi)
    dp_sorted = delta_phi[idx]
    rft_sorted = epsilon_rft[idx]
    exp_sorted = epsilon_exp[idx]

    ax_main.scatter(dp_sorted, exp_sorted, s=4, alpha=0.4,
                    color="tab:blue", label=f"ε_exp ({data_label})")
    ax_main.plot(dp_sorted, rft_sorted, "r-", lw=2,
                 label=r"ε_RFT = cos²(Δφ/2) [Axiom 4]")
    ax_main.set_ylabel("ε", fontsize=12)
    ax_main.set_title(
        f"RT-08 — ε_RFT vs. ε_exp  |  χ²_red = {chi2_red:.3f}", fontsize=12
    )
    ax_main.legend(fontsize=10)
    ax_main.set_ylim(-0.05, 1.15)
    ax_main.grid(True, alpha=0.3)

    residuals_sorted = exp_sorted - rft_sorted
    ax_res.scatter(dp_sorted, residuals_sorted, s=4, alpha=0.4, color="tab:gray")
    ax_res.axhline(0, color="red", lw=1)
    ax_res.set_xlabel("Δφ (rad)", fontsize=12)
    ax_res.set_ylabel("Residuals", fontsize=11)
    ax_res.grid(True, alpha=0.3)

    color_map = {"confirmed": "green", "borderline": "orange", "rejected": "red"}
    for spine in ax_main.spines.values():
        spine.set_edgecolor(color_map.get(verdict, "black"))
        spine.set_linewidth(2)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rt08_scatter.png"), dpi=150)
    plt.close(fig)


def _plot_timeseries(
    t: np.ndarray,
    delta_phi: np.ndarray,
    epsilon_rft: np.ndarray,
    epsilon_exp: np.ndarray,
    data_label: str,
) -> None:
    """Plot 2: Time series Δθ(t), ε_RFT(t), ε_exp(t)."""
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(t, delta_phi, color="tab:purple", lw=0.8)
    axes[0].set_ylabel("Δθ (rad)", fontsize=11)
    axes[0].set_title(
        f"RT-08 — Time series  |  {data_label}", fontsize=12
    )
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(t, epsilon_rft, "r-", lw=1.2,
                 label=r"ε_RFT = cos²(Δφ/2)")
    axes[1].set_ylabel("ε_RFT", fontsize=11)
    axes[1].set_ylim(-0.05, 1.15)
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(t, epsilon_exp, color="tab:blue", lw=1.2,
                 label="ε_exp (normalised)")
    axes[2].set_ylabel("ε_exp", fontsize=11)
    axes[2].set_ylim(-0.05, 1.15)
    axes[2].set_xlabel("t (s)", fontsize=11)
    axes[2].legend(fontsize=9)
    axes[2].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rt08_timeseries.png"), dpi=150)
    plt.close(fig)


def _plot_residuals(residuals: np.ndarray, data_label: str) -> None:
    """Plot 3: Residuals histogram with Gaussian test."""
    fig, ax = plt.subplots(figsize=(7, 5))

    n_bins = max(20, len(residuals) // 50)
    counts, bin_edges, _ = ax.hist(
        residuals, bins=n_bins, density=True,
        color="tab:blue", alpha=0.7, label="Residuals"
    )

    mu = float(np.mean(residuals))
    sigma = float(np.std(residuals))
    x_gauss = np.linspace(bin_edges[0], bin_edges[-1], 300)
    ax.plot(x_gauss, norm_dist.pdf(x_gauss, mu, sigma), "r-", lw=2,
            label=fr"Gaussian µ={mu:.3f}, σ={sigma:.3f}")

    ax.set_xlabel("Residual (ε_exp − ε_RFT)", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    ax.set_title(f"RT-08 — Residuals histogram  |  {data_label}", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rt08_residuals.png"), dpi=150)
    plt.close(fig)


def _plot_chi2_distribution(chi2_val: float, dof: int, data_label: str) -> None:
    """Plot 4: χ² distribution with measured value marked."""
    fig, ax = plt.subplots(figsize=(7, 5))

    x = np.linspace(0, max(chi2_val * 1.5, chi2_dist.ppf(0.9999, df=dof)), 500)
    y = chi2_dist.pdf(x, df=dof)
    ax.plot(x, y, "k-", lw=2, label=f"χ²({dof})")

    x_fill = x[x >= chi2_val]
    y_fill = chi2_dist.pdf(x_fill, df=dof)
    if len(x_fill) > 1:
        ax.fill_between(x_fill, y_fill, alpha=0.35, color="red",
                        label="p-value area")

    ax.axvline(chi2_val, color="red", lw=2, linestyle="--",
               label=f"χ²_meas = {chi2_val:.2f}")

    limit_15 = 1.5 * dof
    limit_20 = 2.0 * dof
    ax.axvline(limit_15, color="orange", lw=1.5, linestyle=":",
               label=f"χ²_red=1.5 (χ²={limit_15:.1f})")
    ax.axvline(limit_20, color="darkred", lw=1.5, linestyle=":",
               label=f"χ²_red=2.0 (χ²={limit_20:.1f})")

    ax.set_xlabel("χ²", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    ax.set_title(f"RT-08 — χ² distribution (dof={dof})  |  {data_label}", fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rt08_chi2dist.png"), dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    filepath = None
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    elif "RT08_DATA_FILE" in os.environ:
        filepath = os.environ["RT08_DATA_FILE"]

    run_analysis(filepath)
