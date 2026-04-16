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
    print(f"   D_ell-Bereich: {np.min(planck['D_ell']):.0f} - {np.max(planck['D_ell']):.0f} muK^2")
    data_available = True
except Exception as e:
    print(f"   WARNUNG: Planck-Download fehlgeschlagen: {e}")
    print("   Verwende synthetische Daten ...")
    data_available = False

    from core.cmb_comparison import generate_lcdm_bestfit
    ell_synth = np.arange(30, 2500, 30, dtype=float)
    D_synth = generate_lcdm_bestfit(ell_synth)
    rng = np.random.default_rng(42)
    D_synth += rng.normal(0, 40, size=len(ell_synth))
    err_synth = np.full_like(ell_synth, 40.0)
    planck = {
        "ell": ell_synth, "D_ell": D_synth,
        "err_low": err_synth, "err_high": err_synth,
        "err": err_synth,
    }

# === 2. Vergleich bei Planck H0 ===
print("\n2. Vergleich bei H0 = 67.4 (Planck) ...")
result_planck = compare_with_planck(planck, h0=67.4, d_eta=0.1334)
print(f"   Chi^2/dof (LCDM):       {result_planck['chi2_lcdm_reduced']:.2f}")
print(f"   Chi^2/dof (Resonanz):   {result_planck['chi2_resonanz_reduced']:.2f}")
print(f"   Delta Chi^2:            {result_planck['delta_chi2']:.1f}")
print(f"   Pearson r (Korrektur vs Residuen): {result_planck['pearson_r']:.3f}")

# === 3. Vergleich bei SH0ES H0 ===
print("\n3. Vergleich bei H0 = 73.0 (SH0ES) ...")
result_shoes = compare_with_planck(planck, h0=73.0, d_eta=0.1448)
print(f"   Chi^2/dof (LCDM):       {result_shoes['chi2_lcdm_reduced']:.2f}")
print(f"   Chi^2/dof (Resonanz):   {result_shoes['chi2_resonanz_reduced']:.2f}")
print(f"   Delta Chi^2:            {result_shoes['delta_chi2']:.1f}")
print(f"   Pearson r:              {result_shoes['pearson_r']:.3f}")

# === 4. Chi^2-Scan ===
print("\n4. Chi^2-Scan: H0 = 60 - 80 km/s/Mpc ...")
d_eta_func = lambda h0: 0.00204 * h0 - 0.00404
chi2_scan = scan_h0_chi2(planck, h0_values=np.linspace(60, 80, 41),
                          d_eta_func=d_eta_func)

idx_min_l = np.argmin(chi2_scan["chi2_lcdm"])
idx_min_r = np.argmin(chi2_scan["chi2_resonanz"])
print(f"   LCDM Chi^2-Minimum:     H0 = {chi2_scan['h0_values'][idx_min_l]:.1f}")
print(f"   Resonanz Chi^2-Minimum: H0 = {chi2_scan['h0_values'][idx_min_r]:.1f}")

# Wo ist Delta Chi^2 maximal positiv?
idx_best = np.argmax(chi2_scan["delta_chi2"])
print(f"   Max Delta Chi^2:        {chi2_scan['delta_chi2'][idx_best]:.1f} bei H0 = {chi2_scan['h0_values'][idx_best]:.1f}")

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
print(f"    Pearson r:          {result_planck['pearson_r']:.3f}")
print(f"\n  Bei H0 = 73.0 (SH0ES):")
print(f"    Chi^2/dof LCDM:     {result_shoes['chi2_lcdm_reduced']:.2f}")
print(f"    Chi^2/dof Resonanz: {result_shoes['chi2_resonanz_reduced']:.2f}")
print(f"    Pearson r:          {result_shoes['pearson_r']:.3f}")

print(f"\n  Interpretation:")
if result_planck['delta_chi2'] > 0:
    print(f"    Die eta-Korrektur VERBESSERT den Fit um Delta Chi^2 = {result_planck['delta_chi2']:.1f}")
else:
    print(f"    Die eta-Korrektur verschlechtert den Fit um Delta Chi^2 = {result_planck['delta_chi2']:.1f}")
    print(f"    Das ist ehrlich: Das parametrische best-fit-Modell muss verfeinert werden.")
    print(f"    Die Korrelationsanalyse (Pearson r) zeigt, ob die RICHTUNG stimmt.")

if abs(result_planck['pearson_r']) > 0.3:
    print(f"    Pearson r = {result_planck['pearson_r']:.3f} zeigt signifikante Korrelation!")
elif abs(result_planck['pearson_r']) > 0.1:
    print(f"    Pearson r = {result_planck['pearson_r']:.3f} zeigt schwache Korrelation.")
else:
    print(f"    Pearson r = {result_planck['pearson_r']:.3f} — keine klare Korrelation.")

print("\nFertig.")