#!/usr/bin/env python3
"""
RT-58b: Kreuzkorrelations-Spektrum aus LOSC v2 HDF5-Dateien

Verwendung:
  python rt58_ccspektrum.py \
    --h1 H-H1_LOSC_4_V2-1126257414-4096.hdf5 \
    --l1 L-L1_LOSC_4_V2-1126257414-4096.hdf5 \
    --outdir rt58_sgwb_output

Format: LOSC v2  →  keys: meta/, quality/, strain/Strain
"""

import argparse, os, sys
import numpy as np

def load_losc_v2(filepath):
    import h5py
    with h5py.File(filepath, 'r') as f:
        strain = f['strain/Strain'][:]
        # Metadaten
        try:
            dt = float(f['strain/Strain'].attrs['Xspacing'])
            t0 = float(f['strain/Strain'].attrs['Xstart'])
        except KeyError:
            try:
                dt = 1.0 / float(f['meta/Fsample'][()])
                t0 = float(f['meta/GPSstart'][()])
            except:
                dt = 1.0/4096
                t0 = 0.0
    return strain, dt, t0

def compute_cc_spectrum(strain_h1, strain_l1, dt, nperseg=4096*4):
    """
    Berechnet normiertes Kreuzkorrelations-Spektrum.
    nperseg=16384 → Frequenzauflösung 0.25 Hz bei 4096 Hz sampling
    """
    from scipy.signal import csd, welch
    fs = 1.0 / dt
    
    f, Sxy = csd(strain_h1, strain_l1, fs=fs, nperseg=nperseg,
                 window='hann', average='median')
    _, Sxx = welch(strain_h1, fs=fs, nperseg=nperseg,
                   window='hann', average='median')
    _, Syy = welch(strain_l1, fs=fs, nperseg=nperseg,
                   window='hann', average='median')
    
    # C(f) = Re[Sxy] / sqrt(Sxx * Syy)  (normierte Korrelation)
    denom = np.sqrt(Sxx * Syy)
    C = np.real(Sxy) / np.where(denom > 0, denom, np.nan)
    sigma = 1.0 / np.sqrt(np.maximum(Sxx * Syy, 1e-100))
    sigma = sigma / np.nanmax(sigma)  # normiert
    
    return f, C, sigma

def rft_gamma(f, d_HL_m=3002e3):
    c = 299792458.0
    f0 = c / (2 * d_HL_m)
    return np.cos(np.pi * f / (2 * f0))**2, f0

def save_cc_dat(f, C, sigma, outdir):
    """Speichert C_lokal.dat im gleichen Format wie C_O3_HL.dat"""
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, 'C_lokal_HL.dat')
    with open(outfile, 'w') as fp:
        fp.write("# freq[Hz]  C(f)  sigma(f)\n")
        for fi, ci, si in zip(f, C, sigma):
            if np.isfinite(ci) and np.isfinite(si):
                fp.write(f"{fi:.6f}  {ci:.6e}  {si:.6e}\n")
    print(f"CC-Spektrum: {outfile}  ({os.path.getsize(outfile)//1024} KB)")
    return outfile

def plot_results(f, C, gamma_rft, f0, outdir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    os.makedirs(outdir, exist_ok=True)
    fig, axes = plt.subplots(2, 1, figsize=(11, 9))
    mask = (f >= 10) & (f <= 500)
    
    # Normiert für Vergleich
    C_norm = np.abs(C)
    max_C = np.nanpercentile(C_norm[mask], 99)
    C_plot = C_norm / max_C
    
    ax1 = axes[0]
    ax1.plot(f[mask], C_plot[mask], 'b-', alpha=0.5, lw=0.8,
             label='|C(f)| normiert [O3 H1×L1, 4096s]')
    ax1.plot(f[mask], gamma_rft[mask], 'r-', lw=2.5,
             label=f'Γ_RFT(f) = cos²(πf/2f₀)')
    
    # Glättung
    from scipy.ndimage import uniform_filter1d
    C_smooth = uniform_filter1d(C_plot, size=50)
    ax1.plot(f[mask], C_smooth[mask], 'g-', lw=2,
             label='|C(f)| geglättet (50-Pkt-Mittel)')
    
    ax1.axvline(f0, color='orange', ls=':', lw=1.5,
                label=f'f₀ = {f0:.1f} Hz')
    ax1.set_xlabel('Frequenz f [Hz]')
    ax1.set_ylabel('Γ(f) [normiert]')
    ax1.set_title('RT-58b: RFT Γ(f)-Analyse — LIGO O3 H1×L1 (4096s Segment)')
    ax1.legend(fontsize=9)
    ax1.set_xlim(10, 500)
    ax1.set_ylim(-0.1, 1.3)
    ax1.grid(True, alpha=0.3)
    
    ax2 = axes[1]
    ax2.plot(f[mask], C[mask], 'b-', alpha=0.4, lw=0.6,
             label='Re[C(f)] (Vorzeichen)')
    ax2.axhline(0, color='gray', lw=0.8)
    ax2.axvline(f0, color='orange', ls=':', lw=1.5)
    ax2.set_xlabel('Frequenz f [Hz]')
    ax2.set_ylabel('Re[C(f)]')
    ax2.set_title('RT-58b: Vorzeichen-Struktur des CC-Spektrums')
    ax2.set_xlim(10, 500)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9)
    
    plt.tight_layout()
    out = os.path.join(outdir, 'rt58_sgwb_analyse.png')
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot: {out}")
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--h1', required=True)
    parser.add_argument('--l1', required=True)
    parser.add_argument('--outdir', default='rt58_sgwb_output')
    args = parser.parse_args()
    
    print("=" * 60)
    print("RT-58b: CC-Spektrum aus LOSC v2 — Γ(f)-Analyse (RFT)")
    print("=" * 60)
    
    print(f"\nLade H1: {args.h1}")
    s_h1, dt, t0 = load_losc_v2(args.h1)
    print(f"  {len(s_h1)} Samples, fs={1/dt:.0f} Hz, GPS_start={t0:.0f}")
    
    print(f"Lade L1: {args.l1}")
    s_l1, dt_l1, t0_l1 = load_losc_v2(args.l1)
    print(f"  {len(s_l1)} Samples, fs={1/dt_l1:.0f} Hz, GPS_start={t0_l1:.0f}")
    
    n = min(len(s_h1), len(s_l1))
    print(f"\nBerechne CC-Spektrum über {n} Samples = {n*dt/60:.1f} min Daten...")
    
    f, C, sigma = compute_cc_spectrum(s_h1[:n], s_l1[:n], dt)
    
    gamma_rft, f0 = rft_gamma(f)
    
    # Epsilon-Analyse im LIGO-Band
    mask_band = (f >= 20) & (f <= 200)
    C_norm = np.abs(C) / np.nanpercentile(np.abs(C[mask_band]), 99)
    eps_mean = np.nanmean(C_norm[mask_band])
    eps_std  = np.nanstd(C_norm[mask_band])
    eps0 = 0.6847
    delta_sigma = abs(eps_mean - eps0) / eps_std if eps_std > 0 else np.nan
    
    # Erste Nullstelle
    sign_changes = np.where(np.diff(np.sign(C[mask_band])))[0]
    f_band = f[mask_band]
    f_null_obs = f_band[sign_changes[0]] if len(sign_changes) > 0 else np.nan
    
    print(f"\n--- ERGEBNISSE ---")
    print(f"f₀ geometrisch    = {f0:.2f} Hz")
    print(f"f₀ beobachtet     = {f_null_obs:.2f} Hz  (1. Vorzeichenwechsel)")
    print(f"ε_mean (20-200Hz) = {eps_mean:.4f} ± {eps_std:.4f}")
    print(f"ε₀ = Ω_Λ          = {eps0}")
    print(f"Abweichung        = {delta_sigma:.2f}σ")
    
    save_cc_dat(f, C, sigma, args.outdir)
    plot_results(f, C, gamma_rft, f0, args.outdir)
    
    out = os.path.join(args.outdir, 'rt58_sgwb_ergebnis.txt')
    with open(out, 'w', encoding='utf-8') as fp:
        fp.write("RT-58b: LIGO O3 CC-Spektrum Γ(f)-Analyse\n")
        fp.write("=" * 50 + "\n")
        fp.write(f"f₀ geometrisch  = {f0:.2f} Hz\n")
        fp.write(f"f₀ beobachtet   = {f_null_obs:.2f} Hz\n")
        fp.write(f"ε_mean 20-200Hz = {eps_mean:.4f} ± {eps_std:.4f}\n")
        fp.write(f"ε₀ (Ω_Λ)        = {eps0}\n")
        fp.write(f"Abweichung      = {delta_sigma:.2f}σ\n")
        fp.write(f"Daten: {n} Samples = {n*dt/60:.1f} min\n")
    print(f"Ergebnis: {out}")
    print("=" * 60)

if __name__ == '__main__':
    main()
