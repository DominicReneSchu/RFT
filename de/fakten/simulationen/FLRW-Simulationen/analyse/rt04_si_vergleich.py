"""
RT-04: SI-Einheitenvergleich — FLRW-Solver gegen astropy.

Läuft den neuen FLRW-Solver in physikalischen SI-Einheiten und
vergleicht ihn gegen astropy.cosmology.FlatLambdaCDM.

Falsifizierungskriterium:
    Maximale Abweichung |a_rft − a_astropy| / a_astropy < 1 %
    über den gesamten kosmischen Zeitraum t = 0.1..13.8 Gyr.

Verwendung:
    python analyse/rt04_si_vergleich.py

Ausgabe:
    - Konsolenausgabe: maximale Abweichung, Bestehen des 1%-Kriteriums
    - Plot: analyse/rt04_si_vergleich.png

Abhängigkeiten: numpy, matplotlib, astropy, scipy
"""

import sys
import os

# Sicherstellen, dass das übergeordnete Verzeichnis im Pfad ist
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from core.flrw_si import (
    flrw_si_sim,
    compare_to_astropy,
    H0_PLANCK, OMEGA_M, OMEGA_R, OMEGA_LAMBDA,
)


def main():
    print("=" * 60)
    print("RT-04: FLRW SI-Einheitenvergleich")
    print("=" * 60)

    # ------------------------------------------------------------------
    # 1. Basis-Simulation mit Planck-2018-Werten
    # ------------------------------------------------------------------
    print("\n[1] Simulation mit Planck-2018-Defaults ...")
    d_eta = 0.00204 * H0_PLANCK - 0.00404  # aus H0-Scan Stufe 6a

    sim = flrw_si_sim(
        H0=H0_PLANCK,
        Omega_m=OMEGA_M,
        Omega_r=OMEGA_R,
        Omega_Lambda=OMEGA_LAMBDA,
        t_span_Gyr=(0.001, 13.8),
        n_eval=1000,
        d_eta=d_eta,
    )

    t_0_idx = np.argmin(np.abs(sim["t_Gyr"] - 13.8))
    H_today = sim["H_rft_kmsMpc"][t_0_idx]
    print(f"  H_rft(t₀ = 13.8 Gyr) = {H_today:.2f} km/s/Mpc")
    print(f"  H₀_Planck             = {H0_PLANCK:.2f} km/s/Mpc")
    passes_h0 = abs(H_today - H0_PLANCK) <= 0.54
    print(f"  H₀_rft ∈ [67.36 ± 0.54]: {'✓ BESTANDEN' if passes_h0 else '✗ NICHT BESTANDEN'}")

    # ------------------------------------------------------------------
    # 2. Vergleich mit astropy
    # ------------------------------------------------------------------
    print("\n[2] Vergleich gegen astropy.cosmology.FlatLambdaCDM ...")
    try:
        cmp = compare_to_astropy(
            H0=H0_PLANCK,
            Omega_m=OMEGA_M,
            Omega_Lambda=OMEGA_LAMBDA,
            t_span_Gyr=(0.1, 13.8),
            n_eval=500,
            d_eta=d_eta,
        )
        max_err = cmp["max_rel_err"]
        passes = cmp["passes_1pct"]
        print(f"  Maximale relative Abweichung: {max_err * 100:.3f} %")
        print(f"  Falsifizierungskriterium < 1%: {'✓ BESTANDEN' if passes else '✗ NICHT BESTANDEN'}")
        astropy_available = True
    except ImportError as e:
        print(f"  astropy nicht verfügbar: {e}")
        print("  → Vergleichsplot ohne astropy-Referenz")
        astropy_available = False
        cmp = sim
        cmp["a_astropy"] = None
        cmp["rel_err"] = None

    # ------------------------------------------------------------------
    # 3. Plot
    # ------------------------------------------------------------------
    print("\n[3] Erstelle Plot ...")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(
        "RT-04: FLRW SI-Solver — Planck-2018-Vergleich",
        fontsize=14, fontweight="bold"
    )

    ax1, ax2, ax3, ax4 = axes.flat

    # Panel 1: Skalenfaktor a(t)
    ax1.plot(sim["t_Gyr"], sim["a_lcdm"], "b-", lw=2, label="ΛCDM (RFT-Solver)")
    ax1.plot(sim["t_Gyr"], sim["a_rft"], "r--", lw=2, label=f"ΛCDM+η (d_η={d_eta:.4f})")
    if astropy_available and cmp.get("a_astropy") is not None:
        ax1.plot(cmp["t_Gyr"], cmp["a_astropy"], "g:", lw=2, label="astropy Referenz")
    ax1.axvline(13.8, color="gray", ls=":", alpha=0.7, label="t₀ = 13.8 Gyr")
    ax1.set_xlabel("t [Gyr]")
    ax1.set_ylabel("Skalenfaktor a(t)")
    ax1.set_title("Skalenfaktor")
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)

    # Panel 2: Hubble-Parameter H(t)
    ax2.plot(sim["t_Gyr"], sim["H_lcdm_kmsMpc"], "b-", lw=2, label="H_ΛCDM")
    ax2.plot(sim["t_Gyr"], sim["H_rft_kmsMpc"], "r--", lw=2, label="H_RFT")
    ax2.axhline(H0_PLANCK, color="green", ls=":", alpha=0.7, label=f"H₀_Planck = {H0_PLANCK}")
    ax2.axhline(73.04, color="orange", ls=":", alpha=0.7, label="H₀_SH0ES = 73.04")
    ax2.set_xlabel("t [Gyr]")
    ax2.set_ylabel("H(t) [km/s/Mpc]")
    ax2.set_title("Hubble-Parameter")
    ax2.set_ylim(0, 200)
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    # Panel 3: Relative Abweichung vom astropy-Referenz
    if astropy_available and cmp.get("rel_err") is not None:
        ax3.semilogy(cmp["t_Gyr"], cmp["rel_err"] * 100, "purple", lw=2)
        ax3.axhline(1.0, color="red", ls="--", label="1%-Kriterium")
        ax3.set_xlabel("t [Gyr]")
        ax3.set_ylabel("|a_rft − a_astropy| / a_astropy [%]")
        ax3.set_title(f"Abweichung von astropy (max: {cmp['max_rel_err']*100:.3f} %)")
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        # Farbe je nach Ergebnis
        color = "green" if cmp["passes_1pct"] else "red"
        ax3.set_facecolor(f"#{('e8f5e9' if cmp['passes_1pct'] else 'ffebee')}")
    else:
        ax3.text(0.5, 0.5, "astropy nicht verfügbar\npip install astropy",
                 ha="center", va="center", transform=ax3.transAxes)
        ax3.set_title("Abweichung von astropy")

    # Panel 4: Zusammenfassung
    ax4.axis("off")
    summary_lines = [
        "RT-04 Ergebnisse",
        "═" * 30,
        f"H₀_Planck = {H0_PLANCK:.2f} km/s/Mpc",
        f"Ω_m = {OMEGA_M:.4f}",
        f"Ω_r = {OMEGA_R:.2e}",
        f"Ω_Λ = {OMEGA_LAMBDA:.4f}",
        f"d_η = {d_eta:.4f}",
        "",
        f"H_rft(t₀) = {H_today:.2f} km/s/Mpc",
        f"H₀_rft ∈ [67.36 ± 0.54]: {'✓' if passes_h0 else '✗'}",
    ]
    if astropy_available and cmp.get("max_rel_err") is not None:
        summary_lines += [
            "",
            f"Max. Abw. von astropy:",
            f"  {cmp['max_rel_err']*100:.3f} %",
            f"Kriterium < 1%: {'✓ BESTANDEN' if cmp['passes_1pct'] else '✗ NICHT BESTANDEN'}",
        ]
    text = "\n".join(summary_lines)
    ax4.text(0.05, 0.95, text, transform=ax4.transAxes,
             fontsize=10, verticalalignment="top", fontfamily="monospace",
             bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))

    plt.tight_layout()
    outpath = os.path.join(_HERE, "rt04_si_vergleich.png")
    plt.savefig(outpath, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot gespeichert: {outpath}")

    # ------------------------------------------------------------------
    # 4. Abschlussbericht
    # ------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("RT-04 Abschlussbericht:")
    print(f"  H_rft(t₀ = 13.8 Gyr) = {H_today:.2f} km/s/Mpc")
    if astropy_available and cmp.get("max_rel_err") is not None:
        status = "✓ BESTANDEN" if (passes_h0 and cmp["passes_1pct"]) else "✗ NICHT BESTANDEN"
        print(f"  Max. Abweichung von astropy: {cmp['max_rel_err']*100:.3f} %")
        print(f"  Gesamtstatus: {status}")
    else:
        print(f"  Gesamtstatus: {'✓ H₀-Kriterium' if passes_h0 else '✗ H₀-Kriterium'} (astropy nicht installiert)")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
