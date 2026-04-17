"""Start script Level 6b: CMB comparison with Planck 2018."""

import numpy as np
from core.cmb_comparison import (
    download_planck_tt, load_planck_tt,
    compare_with_planck, scan_h0_chi2,
)
from viz.plot_cmb import plot_cmb_comparison, plot_chi2_scan

print("=" * 60)
print("Level 6b: CMB Comparison — Planck 2018 vs. Resonance Field Theory")
print("=" * 60)

# === 1. Load Planck data ===
print("\n1. Loading Planck 2018 TT spectrum ...")
try:
    filepath = download_planck_tt(filepath="data/planck_tt_binned.txt")
    planck = load_planck_tt(filepath)
    print(f"   {len(planck['ell'])} data points loaded")
    print(f"   ell range: {planck['ell'][0]:.0f} - {planck['ell'][-1]:.0f}")
    print(f"   D_ell range: {np.min(planck['D_ell']):.0f} - {np.max(planck['D_ell']):.0f} muK^2")
    data_available = True
except Exception as e:
    print(f"   WARNING: Planck download failed: {e}")
    print("   Using synthetic data ...")
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

# === 2. Comparison at Planck H0 ===
print("\n2. Comparison at H0 = 67.4 (Planck) ...")
result_planck = compare_with_planck(planck, h0=67.4, d_eta=0.1334)
print(f"   Chi^2/dof (LCDM):              {result_planck['chi2_lcdm_reduced']:.2f}")
print(f"   Chi^2/dof (resonance field):   {result_planck['chi2_resonanz_reduced']:.2f}")
print(f"   Delta Chi^2:                   {result_planck['delta_chi2']:.1f}")
print(f"   Pearson r (correction vs residuals): {result_planck['pearson_r']:.3f}")

# === 3. Comparison at SH0ES H0 ===
print("\n3. Comparison at H0 = 73.0 (SH0ES) ...")
result_shoes = compare_with_planck(planck, h0=73.0, d_eta=0.1448)
print(f"   Chi^2/dof (LCDM):              {result_shoes['chi2_lcdm_reduced']:.2f}")
print(f"   Chi^2/dof (resonance field):   {result_shoes['chi2_resonanz_reduced']:.2f}")
print(f"   Delta Chi^2:                   {result_shoes['delta_chi2']:.1f}")
print(f"   Pearson r:                     {result_shoes['pearson_r']:.3f}")

# === 4. Chi^2 scan ===
print("\n4. Chi^2 scan: H0 = 60 - 80 km/s/Mpc ...")
d_eta_func = lambda h0: 0.00204 * h0 - 0.00404
chi2_scan = scan_h0_chi2(planck, h0_values=np.linspace(60, 80, 41),
                          d_eta_func=d_eta_func)

idx_min_l = np.argmin(chi2_scan["chi2_lcdm"])
idx_min_r = np.argmin(chi2_scan["chi2_resonanz"])
print(f"   LCDM Chi^2 minimum:            H0 = {chi2_scan['h0_values'][idx_min_l]:.1f}")
print(f"   Resonance field Chi^2 minimum: H0 = {chi2_scan['h0_values'][idx_min_r]:.1f}")

# Where is Delta Chi^2 maximally positive?
idx_best = np.argmax(chi2_scan["delta_chi2"])
print(f"   Max Delta Chi^2:               {chi2_scan['delta_chi2'][idx_best]:.1f} at H0 = {chi2_scan['h0_values'][idx_best]:.1f}")

# === 5. Plots ===
print("\n5. Creating plots ...")
plot_cmb_comparison(result_planck, save_path="images/cmb_comparison.png")
plot_chi2_scan(chi2_scan, save_path="images/cmb_chi2_scan.png")

# === 6. Summary ===
print("\n" + "=" * 60)
print("Summary Level 6b")
print("=" * 60)
print(f"\n  Data basis: {'Planck 2018 (real)' if data_available else 'Synthetic'}")
print(f"  Data points: {len(planck['ell'])}")
print(f"\n  At H0 = 67.4 (Planck):")
print(f"    Chi^2/dof LCDM:              {result_planck['chi2_lcdm_reduced']:.2f}")
print(f"    Chi^2/dof resonance field:   {result_planck['chi2_resonanz_reduced']:.2f}")
print(f"    Pearson r:                   {result_planck['pearson_r']:.3f}")
print(f"\n  At H0 = 73.0 (SH0ES):")
print(f"    Chi^2/dof LCDM:              {result_shoes['chi2_lcdm_reduced']:.2f}")
print(f"    Chi^2/dof resonance field:   {result_shoes['chi2_resonanz_reduced']:.2f}")
print(f"    Pearson r:                   {result_shoes['pearson_r']:.3f}")

print(f"\n  Interpretation:")
if result_planck['delta_chi2'] > 0:
    print(f"    The eta correction IMPROVES the fit by Delta Chi^2 = {result_planck['delta_chi2']:.1f}")
else:
    print(f"    The eta correction worsens the fit by Delta Chi^2 = {result_planck['delta_chi2']:.1f}")
    print(f"    This is honest: the parametric best-fit model needs to be refined.")
    print(f"    The correlation analysis (Pearson r) shows whether the DIRECTION is correct.")

if abs(result_planck['pearson_r']) > 0.3:
    print(f"    Pearson r = {result_planck['pearson_r']:.3f} shows significant correlation!")
elif abs(result_planck['pearson_r']) > 0.1:
    print(f"    Pearson r = {result_planck['pearson_r']:.3f} shows weak correlation.")
else:
    print(f"    Pearson r = {result_planck['pearson_r']:.3f} — no clear correlation.")

print("\nDone.")
