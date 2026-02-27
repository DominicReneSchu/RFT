"""Startskript Stufe 6b: CMB-Vergleich mit Planck 2018."""

import numpy as np
from core.cmb_comparison import (
    download_planck_tt, load_planck_tt,
    compare_with_planck, scan_h0_chi2,
)
from viz.plot_cmb import plot_cmb_comparison, plot_chi2_scan

print("=" * 60)
print("Stufe 6b: CMB-Vergleich — Planck 2018 vs. Resonanzfeldtheorie")
print("=" * 60)

# === 1. Planck-Daten laden ===
print("\n1. Planck 2018 TT-Spektrum laden ...")
try:
    filepath = download_planck_tt(filepath="data/planck_tt_binned.txt")
    planck = load_planck_tt(filepath)
    print(f"   {len(planck['ell'])} Datenpunkte geladen")
    print(f"   ell-Bereich: {planck['ell'][0]:.0f} - {planck['ell'][-1]:.0f}")
    data_available = True
except Exception as e:
    print(f"   WARNUNG: Planck-Download fehlgeschlagen: {e}")
    print("   Verwende synthetische Daten fuer Demonstration ...")
    data_available = False

    # Synthetische Daten als Fallback
    from core.cmb_comparison import lcdm_spectrum
    ell_synth = np.arange(2, 2509, dtype=float)
    D_synth = lcdm_spectrum(ell_synth, h0=67.4)
    # Rauschen hinzufuegen
    rng = np.random.default_rng(42)
    noise = rng.normal(0, 50, size=len(ell_synth))
    D_synth_noisy = D_synth + noise
    err_synth = np.full_like(ell_synth, 50.0)
    planck = {
        "ell": ell_synth,
        "D_ell": D_synth_noisy,
        "err_low": err_synth,
        "err_high": err_synth,
    }
    print(f"   {len(ell_synth)} synthetische Punkte erzeugt")

# === 2. Vergleich bei Planck H0 ===
print("\n2. Vergleich bei H0 = 67.4 (Planck) ...")
result_planck = compare_with_planck(planck, h0=67.4, d_eta=0.1334)
print(f"   Chi^2/dof (LCDM):       {result_planck['chi2_lcdm_reduced']:.2f}")
print(f"   Chi^2/dof (Resonanz):   {result_planck['chi2_resonanz_reduced']:.2f}")
print(f"   Delta Chi^2:            {result_planck['chi2_lcdm'] - result_planck['chi2_resonanz']:.1f}")

# === 3. Vergleich bei SH0ES H0 ===
print("\n3. Vergleich bei H0 = 73.0 (SH0ES) ...")
result_shoes = compare_with_planck(planck, h0=73.0, d_eta=0.1448)
print(f"   Chi^2/dof (LCDM):       {result_shoes['chi2_lcdm_reduced']:.2f}")
print(f"   Chi^2/dof (Resonanz):   {result_shoes['chi2_resonanz_reduced']:.2f}")
print(f"   Delta Chi^2:            {result_shoes['chi2_lcdm'] - result_shoes['chi2_resonanz']:.1f}")

# === 4. Chi^2-Scan ueber H0 ===
print("\n4. Chi^2-Scan: H0 = 60 - 80 km/s/Mpc ...")

# d_eta(H0) aus Stufe 6a: linearer Fit
d_eta_func = lambda h0: 0.00204 * h0 - 0.00404

chi2_scan = scan_h0_chi2(planck, h0_values=np.linspace(60, 80, 41),
                          d_eta_func=d_eta_func)

idx_min_l = np.argmin(chi2_scan["chi2_lcdm"])
idx_min_r = np.argmin(chi2_scan["chi2_resonanz"])
print(f"   LCDM Chi^2-Minimum:     H0 = {chi2_scan['h0_values'][idx_min_l]:.1f}")
print(f"   Resonanz Chi^2-Minimum: H0 = {chi2_scan['h0_values'][idx_min_r]:.1f}")

# === 5. Plots ===
print("\n5. Erstelle Plots ...")
plot_cmb_comparison(result_planck, save_path="bilder/cmb_comparison.png")
plot_chi2_scan(chi2_scan, save_path="bilder/cmb_chi2_scan.png")

# === 6. Zusammenfassung ===
print("\n" + "=" * 60)
print("Zusammenfassung Stufe 6b")
print("=" * 60)
print(f"\n  Datenbasis: {'Planck 2018 (echt)' if data_available else 'Synthetisch'}")
print(f"  Datenpunkte: {len(planck['ell'])}")
print(f"\n  Bei H0 = 67.4 (Planck):")
print(f"    Chi^2/dof LCDM:     {result_planck['chi2_lcdm_reduced']:.2f}")
print(f"    Chi^2/dof Resonanz: {result_planck['chi2_resonanz_reduced']:.2f}")
print(f"\n  Bei H0 = 73.0 (SH0ES):")
print(f"    Chi^2/dof LCDM:     {result_shoes['chi2_lcdm_reduced']:.2f}")
print(f"    Chi^2/dof Resonanz: {result_shoes['chi2_resonanz_reduced']:.2f}")
print(f"\n  Chi^2-Minimum LCDM:     H0 = {chi2_scan['h0_values'][idx_min_l]:.1f}")
print(f"  Chi^2-Minimum Resonanz: H0 = {chi2_scan['h0_values'][idx_min_r]:.1f}")

if data_available:
    print("\n  Status: Vergleich mit echten Planck-Daten abgeschlossen.")
else:
    print("\n  Status: Demonstration mit synthetischen Daten.")
    print("  Fuer echte Ergebnisse: Planck-Datei manuell herunterladen")
    print("  von https://pla.esac.esa.int/pla/ und als")
    print("  data/planck_tt_binned.txt speichern.")

print("\nFertig.")