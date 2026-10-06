"""
RT-08 — Doppelpendel: Experimentaldaten vs. RFT-Vorhersage

Dieses Skript vergleicht die RFT-Kopplungseffizienz
    ε_RFT(Δφ) = cos²(Δφ/2)   (Axiom 4)
gegen eine experimentelle bzw. synthetische Referenz per χ²-Fit.

Datenstrategie:
    Primär: Übergabe eines CSV-Pfads via Kommandozeile oder Umgebungsvariable
            RT08_DATA_FILE.
    Fallback: Synthetische Referenzdaten aus reiner Lagrange-Mechanik
              (A = 0, kein RFT-Term) — valide Nullhypothese, wenn keine
              öffentlichen Experimentaldaten verfügbar sind.

Synthetische Daten:
    Quelle:  Lagrange-Doppelpendel-Simulation (doppelpendel.py), A = 0
    Lizenz:  MIT (dieses Repository), kein externer Datensatz
    DOI:     — (synthetisch)

Experimentelle CSV-Daten (optional):
    Empfohlene Quelle: Zenodo – „double pendulum experimental data"
    Beispiel-DOI: https://doi.org/10.5281/zenodo.XXXXXXX (Platzhalter)
    Lizenz: CC-BY 4.0 (je nach Datensatz prüfen)
    Erwartetes Format: CSV mit Kopfzeile, Spalten: t, theta1, theta2
                       oder t, x1, y1, x2, y2

Falsifizierungskriterium (scharf):
    χ²_red ≤ 1.5               → RFT-Formel nicht falsifiziert (bestätigt)
    1.5 < χ²_red ≤ 2.0         → Grenzbereich, Interpretation offen
    χ²_red > 2.0                → RFT-Formel durch Daten abgelehnt (5 %-Niveau)

Ausgabe:
    - Tabelle auf stdout
    - 4 Plots als PNG: rt08_scatter.png, rt08_timeseries.png,
                       rt08_residuals.png, rt08_chi2dist.png

Verwendung:
    cd de/fakten/simulationen/doppelpendel/analyse
    python rt08_doppelpendel_vergleich.py [pfad/zu/daten.csv]

© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie
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

# Simulationsverzeichnis in Suchpfad aufnehmen
_sim_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, _sim_dir)

from doppelpendel import (
    load_experimental_data,
    compute_epsilon_from_data,
    rft_epsilon_prediction,
    chi2_fit,
)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Synthetische Referenzdaten (Lagrange, A = 0)
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
    """Synthetisches Doppelpendel ohne RFT-Term (A = 0) als Nullhypothese.

    Die Integration erfolgt mit dem Runge-Kutta-Verfahren RK45 (scipy).
    Startbedingungen sind bewusst leicht asymmetrisch gewählt, um ein
    repräsentatives chaotisches Regime zu erfassen.
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
# Hauptanalyse
# ---------------------------------------------------------------------------

def run_analysis(data_filepath: str | None = None) -> None:
    """Lädt Daten, führt χ²-Fit durch und erstellt vier Plots."""

    # --- Daten laden oder synthetisch erzeugen ---
    if data_filepath is not None:
        print(f"Lade experimentelle Daten: {data_filepath}")
        data = load_experimental_data(data_filepath)
        data_label = "Experimentell"
        data_source = f"Datei: {os.path.basename(data_filepath)}"
    else:
        print("Kein Datenpfad übergeben — erzeuge synthetische Referenzdaten (A=0, Lagrange).")
        data = generate_synthetic_reference()
        data_label = "Synthetisch (Lagrange, A=0)"
        data_source = "Doppelpendel-Simulation (doppelpendel.py), A=0, kein RFT-Term"

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

    # --- Konsolenausgabe ---
    print()
    print("RT-08 — Doppelpendel: ε_RFT vs. ε_exp")
    print("=" * 65)
    print(f"Datenbasis:          {data_source}")
    print(f"N Datenpunkte:       {len(delta_phi)}")
    print(f"Freiheitsgrade:      {dof}")
    print("-" * 65)
    print(f"χ²:                  {chi2_val:.4f}")
    print(f"χ²_red:              {chi2_red:.4f}")
    print(f"p-Wert:              {p_value:.4f}")
    print(f"Residuen µ:          {np.mean(residuals):.4f}")
    print(f"Residuen σ:          {np.std(residuals):.4f}")
    print("-" * 65)

    # Falsifizierungskriterium
    if verdict == "confirmed":
        symbol = "✅"
        msg = "RFT-Formel nicht falsifiziert (χ²_red ≤ 1.5)"
    elif verdict == "borderline":
        symbol = "⚠️ "
        msg = "Grenzbereich: 1.5 < χ²_red ≤ 2.0 — Interpretation offen"
    else:
        symbol = "❌"
        msg = "RFT-Formel durch Daten abgelehnt (χ²_red > 2.0, 5%-Niveau)"

    print(f"{symbol} ERGEBNIS: {msg}")
    print("=" * 65)
    print()

    # --- Plots ---
    _plot_scatter(delta_phi, epsilon_rft, epsilon_exp, data_label, chi2_red, verdict)
    _plot_timeseries(t, delta_phi, epsilon_rft, epsilon_exp, data_label)
    _plot_residuals(residuals, data_label)
    _plot_chi2_distribution(chi2_val, dof, data_label)

    print(f"Plots gespeichert in: {OUTPUT_DIR}")
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
    """Plot 1: ε_RFT(Δθ) vs. ε_exp(Δθ) — Scatterplot mit Residuen."""
    fig, (ax_main, ax_res) = plt.subplots(
        2, 1, figsize=(8, 7), gridspec_kw={"height_ratios": [3, 1]}, sharex=False
    )

    # Sortiert nach Δφ für Linienplot
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
    ax_res.set_ylabel("Residuen", fontsize=11)
    ax_res.grid(True, alpha=0.3)

    # Farbige Rahmenlinie je nach Urteil
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
    """Plot 2: Zeitreihe Δθ(t), ε_RFT(t), ε_exp(t)."""
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(t, delta_phi, color="tab:purple", lw=0.8)
    axes[0].set_ylabel("Δθ (rad)", fontsize=11)
    axes[0].set_title(
        f"RT-08 — Zeitreihe  |  {data_label}", fontsize=12
    )
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(t, epsilon_rft, "r-", lw=1.2,
                 label=r"ε_RFT = cos²(Δφ/2)")
    axes[1].set_ylabel("ε_RFT", fontsize=11)
    axes[1].set_ylim(-0.05, 1.15)
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(t, epsilon_exp, color="tab:blue", lw=1.2,
                 label="ε_exp (normiert)")
    axes[2].set_ylabel("ε_exp", fontsize=11)
    axes[2].set_ylim(-0.05, 1.15)
    axes[2].set_xlabel("t (s)", fontsize=11)
    axes[2].legend(fontsize=9)
    axes[2].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rt08_timeseries.png"), dpi=150)
    plt.close(fig)


def _plot_residuals(residuals: np.ndarray, data_label: str) -> None:
    """Plot 3: Residuen-Histogramm mit Gauß-Test."""
    fig, ax = plt.subplots(figsize=(7, 5))

    n_bins = max(20, len(residuals) // 50)
    counts, bin_edges, _ = ax.hist(
        residuals, bins=n_bins, density=True,
        color="tab:blue", alpha=0.7, label="Residuen"
    )

    mu = float(np.mean(residuals))
    sigma = float(np.std(residuals))
    x_gauss = np.linspace(bin_edges[0], bin_edges[-1], 300)
    ax.plot(x_gauss, norm_dist.pdf(x_gauss, mu, sigma), "r-", lw=2,
            label=fr"Gauß µ={mu:.3f}, σ={sigma:.3f}")

    ax.set_xlabel("Residuum (ε_exp − ε_RFT)", fontsize=12)
    ax.set_ylabel("Dichte", fontsize=12)
    ax.set_title(f"RT-08 — Residuen-Histogramm  |  {data_label}", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rt08_residuals.png"), dpi=150)
    plt.close(fig)


def _plot_chi2_distribution(chi2_val: float, dof: int, data_label: str) -> None:
    """Plot 4: χ²-Verteilung mit eingezeichnetem Messwert."""
    fig, ax = plt.subplots(figsize=(7, 5))

    x = np.linspace(0, max(chi2_val * 1.5, chi2_dist.ppf(0.9999, df=dof)), 500)
    y = chi2_dist.pdf(x, df=dof)
    ax.plot(x, y, "k-", lw=2, label=f"χ²({dof})")

    # Schraffierte Fläche rechts vom Messwert (p-Wert)
    x_fill = x[x >= chi2_val]
    y_fill = chi2_dist.pdf(x_fill, df=dof)
    if len(x_fill) > 1:
        ax.fill_between(x_fill, y_fill, alpha=0.35, color="red",
                        label=f"p-Wert-Fläche")

    ax.axvline(chi2_val, color="red", lw=2, linestyle="--",
               label=f"χ²_mess = {chi2_val:.2f}")

    # Falsifizierungsgrenzen (χ²_red × dof)
    limit_15 = 1.5 * dof
    limit_20 = 2.0 * dof
    ax.axvline(limit_15, color="orange", lw=1.5, linestyle=":",
               label=f"χ²_red=1.5 (χ²={limit_15:.1f})")
    ax.axvline(limit_20, color="darkred", lw=1.5, linestyle=":",
               label=f"χ²_red=2.0 (χ²={limit_20:.1f})")

    ax.set_xlabel("χ²", fontsize=12)
    ax.set_ylabel("Dichte", fontsize=12)
    ax.set_title(f"RT-08 — χ²-Verteilung (dof={dof})  |  {data_label}", fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR, "rt08_chi2dist.png"), dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Einstiegspunkt
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    filepath = None
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    elif "RT08_DATA_FILE" in os.environ:
        filepath = os.environ["RT08_DATA_FILE"]

    run_analysis(filepath)
