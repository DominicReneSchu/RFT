#!/usr/bin/env python3
"""
RT-58b: LIGO O3 Stochastischer Hintergrund — Γ(f)-Analyse (RFT)

Datenquelle: LIGO DCC G2001287 — C_O3_HL.dat
  https://dcc.ligo.org/LIGO-G2001287/public

Format: freq[Hz]  C(f)  sigma(f)
  C(f)     = normiertes Kreuzkorrelations-Spektrum
  sigma(f) = theoretische Sensitivität

RFT-Vorhersage: Γ_RFT(f) = cos²(πf / 2f₀), f₀ = c/(2·d_HL) ≈ 49.9 Hz

Verwendung:
  python rt58_sgwb_analyse.py --dat C_O3_HL.dat --outdir rt58_sgwb_output/
"""

import argparse, os, sys
import numpy as np

def load_cc_spectrum(filepath):
    """Lädt LIGO CC-Spektrum aus .dat-Datei."""
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) >= 3:
                try:
                    data.append([float(p) for p in parts[:3]])
                except ValueError:
                    continue
    arr = np.array(data)
    freq = arr[:, 0]
    C    = arr[:, 1]
    sigma = arr[:, 2]
    return freq, C, sigma

def rft_prediction(f, d_HL_m=3002e3):
    """RFT-Vorhersage: Γ_RFT(f) = cos²(πf / 2f₀)"""
    c = 299792458.0
    f0 = c / (2 * d_HL_m)
    return np.cos(np.pi * f / (2 * f0))**2, f0

def normalized_gamma(C, sigma):
    """Γ_obs(f) = |C(f)| / max(|C(f)|) als normierte Vergleichsgröße."""
    return np.abs(C) / (np.max(np.abs(C)) + 1e-30)

def snr_weighted_gamma(C, sigma):
    """SNR-gewichtete Korrelation: SNR(f) = |C(f)| / sigma(f)"""
    return np.abs(C) / (sigma + 1e-50)

def cosine_fit(f, gamma_obs, f0):
    """Passt cos²-Modell an und gibt Güte zurück."""
    from scipy.optimize import curve_fit
    
    mask = (f > 10) & (f < 500) & np.isfinite(gamma_obs)
    f_fit = f[mask]
    g_fit = gamma_obs[mask]
    
    # Modell: A * cos²(π·f / (2·f0·k)) + B
    def model(x, A, k, B):
        return A * np.cos(np.pi * x / (2 * f0 * k))**2 + B
    
    try:
        popt, pcov = curve_fit(model, f_fit, g_fit, p0=[1.0, 1.0, 0.0],
                               bounds=([0, 0.1, -0.5], [2.0, 10.0, 0.5]),
                               maxfev=5000)
        A_fit, k_fit, B_fit = popt
        f0_fit = f0 * k_fit
        
        # Residuen
        residuals = g_fit - model(f_fit, *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((g_fit - np.mean(g_fit))**2)
        r2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0
        
        return A_fit, f0_fit, B_fit, r2
    except Exception as e:
        return None, f0, 0, 0

def plot_results(f, gamma_obs, gamma_snr, gamma_rft, f0, f0_fit, r2, outdir):
    """Speichert Analyseplots."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib nicht verfügbar")
        return None
    
    os.makedirs(outdir, exist_ok=True)
    fig, axes = plt.subplots(2, 1, figsize=(11, 9))
    
    mask = (f >= 10) & (f <= 500)
    
    # Panel 1: Γ(f) normiert
    ax1 = axes[0]
    ax1.plot(f[mask], gamma_obs[mask], 'b-', alpha=0.6, lw=1,
             label='Γ_obs(f) = |C(f)|/max|C| [O3 H1×L1]')
    ax1.plot(f[mask], gamma_rft[mask], 'r-', lw=2.5,
             label=f'Γ_RFT(f) = cos²(πf/2f₀)')
    ax1.axvline(f0, color='orange', ls=':', lw=1.5,
                label=f'f₀_geo = {f0:.1f} Hz (c/2d_HL)')
    if f0_fit:
        ax1.axvline(f0_fit, color='green', ls='--', lw=1.5,
                    label=f'f₀_fit = {f0_fit:.1f} Hz (R²={r2:.3f})')
    ax1.set_xlabel('Frequenz f [Hz]')
    ax1.set_ylabel('Γ(f) [normiert]')
    ax1.set_title('RT-58b: RFT Γ(f)-Analyse — LIGO O3 Stochastischer Hintergrund (Monate Daten)')
    ax1.legend(fontsize=9)
    ax1.set_xlim(10, 500)
    ax1.set_ylim(-0.1, 1.2)
    ax1.grid(True, alpha=0.3)
    
    # Panel 2: SNR(f) = |C(f)|/σ(f)
    ax2 = axes[1]
    ax2.semilogy(f[mask], gamma_snr[mask], 'b-', alpha=0.6, lw=1,
                 label='SNR(f) = |C(f)|/σ(f)')
    ax2.axvline(f0, color='orange', ls=':', lw=1.5, label=f'f₀ = {f0:.1f} Hz')
    ax2.axhline(1.0, color='gray', ls='--', lw=1, label='SNR = 1')
    ax2.set_xlabel('Frequenz f [Hz]')
    ax2.set_ylabel('SNR(f) [log]')
    ax2.set_title('RT-58b: Signal-Rausch-Verhältnis des CC-Spektrums')
    ax2.legend(fontsize=9)
    ax2.set_xlim(10, 500)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    outfile = os.path.join(outdir, 'rt58_sgwb_analyse.png')
    plt.savefig(outfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot: {outfile}")
    return outfile

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dat', required=True, help='C_O3_HL.dat Datei')
    parser.add_argument('--outdir', default='rt58_sgwb_output')
    args = parser.parse_args()
    
    print("=" * 60)
    print("RT-58b: LIGO O3 SGWB — Γ(f)-Analyse (RFT)")
    print("=" * 60)
    
    freq, C, sigma = load_cc_spectrum(args.dat)
    print(f"Geladen: {len(freq)} Frequenzpunkte, {freq[0]:.1f}–{freq[-1]:.1f} Hz")
    
    gamma_rft, f0 = rft_prediction(freq)
    gamma_obs     = normalized_gamma(C, sigma)
    gamma_snr     = snr_weighted_gamma(C, sigma)
    
    # Fit
    A_fit, f0_fit, B_fit, r2 = cosine_fit(freq, gamma_obs, f0)
    
    # Epsilon im LIGO-Band
    mask_band = (freq >= 20) & (freq <= 200)
    eps_mean = np.nanmean(gamma_obs[mask_band])
    eps_std  = np.nanstd(gamma_obs[mask_band])
    eps0 = 0.6847
    delta_sigma = abs(eps_mean - eps0) / eps_std if eps_std > 0 else np.nan
    
    print(f"\n--- ERGEBNISSE ---")
    print(f"f₀ geometrisch    = {f0:.2f} Hz  (c/2·d_HL)")
    if f0_fit:
        print(f"f₀ Fit           = {f0_fit:.2f} Hz  (cos²-Anpassung, R²={r2:.4f})")
    print(f"ε_mean (20-200Hz) = {eps_mean:.4f} ± {eps_std:.4f}")
    print(f"ε₀ = Ω_Λ          = {eps0}")
    print(f"Abweichung        = {delta_sigma:.2f}σ")
    
    os.makedirs(args.outdir, exist_ok=True)
    result_file = os.path.join(args.outdir, 'rt58_sgwb_ergebnis.txt')
    with open(result_file, 'w', encoding='utf-8') as fp:
        fp.write("RT-58b: LIGO O3 SGWB Γ(f)-Analyse\n")
        fp.write("=" * 50 + "\n")
        fp.write(f"Datenquelle: C_O3_HL.dat (LIGO DCC G2001287)\n")
        fp.write(f"Frequenzpunkte: {len(freq)}, Bereich: {freq[0]:.1f}-{freq[-1]:.1f} Hz\n\n")
        fp.write(f"f₀ (geometrisch) = {f0:.2f} Hz\n")
        if f0_fit:
            fp.write(f"f₀ (cos²-Fit)   = {f0_fit:.2f} Hz  (R²={r2:.4f})\n")
        fp.write(f"ε_mean (20-200Hz) = {eps_mean:.4f} ± {eps_std:.4f}\n")
        fp.write(f"ε₀ (Ω_Λ)         = {eps0}\n")
        fp.write(f"Abweichung        = {delta_sigma:.2f}σ\n")
    print(f"Ergebnis: {result_file}")
    
    plot_results(freq, gamma_obs, gamma_snr, gamma_rft, f0, f0_fit, r2, args.outdir)
    print("=" * 60)

if __name__ == '__main__':
    main()
