#!/usr/bin/env python3
"""
RT-58: LIGO GW150914 — Extraktion der 32s-Eventdaten und Γ(f)-Analyse
Resonanzfeldtheorie (RFT)

Verwendung:
  python rt58_extract_and_analyze.py \
    --h1 H-H1_LOSC_4_V2-1126257414-4096.hdf5 \
    --l1 L-L1_LOSC_4_V2-1126257414-4096.hdf5 \
    --outdir output/

Benötigte Pakete: pip install h5py numpy scipy matplotlib
"""

import argparse
import os
import sys
import numpy as np

def load_hdf5_strain(filepath):
    """Lädt Strain-Daten aus GWOSC HDF5-Datei."""
    try:
        import h5py
    except ImportError:
        print("Bitte installieren: pip install h5py")
        sys.exit(1)
    
    with h5py.File(filepath, 'r') as f:
        # GWOSC v1-Format (LOSC_4_V2)
        if 'strain' in f:
            strain = f['strain/Strain'][:]
            meta = dict(f['strain/Strain'].attrs)
            dt = meta.get('Xspacing', 1.0/4096)
            t0 = meta.get('Xstart', 0)
        # GWOSC v2-Format
        elif 'meta' in f:
            strain = f['strain/Strain'][:]
            dt = float(f['meta/PSD_Y_Spacing'][()])
            t0 = float(f['meta/GPSstart'][()])
        else:
            # Generischer Versuch
            keys = list(f.keys())
            print(f"HDF5-Schlüssel: {keys}")
            # Typischerweise: strain/Strain
            strain = f['strain/Strain'][:]
            dt = 1.0/4096
            t0 = 0
    
    return strain, float(dt), float(t0)

def extract_event_window(strain, dt, t0, event_gps=1126259462.4, window_sec=32):
    """Extrahiert 32s-Fenster um das GW150914-Ereignis."""
    fs = 1.0 / dt
    offset_sec = event_gps - t0
    center_sample = int(offset_sec * fs)
    half = int(window_sec * fs / 2)
    
    if center_sample - half < 0 or center_sample + half > len(strain):
        print(f"WARNUNG: Ereignis bei GPS {event_gps} liegt außerhalb des Datenfensters")
        print(f"  Datei: GPS {t0} bis {t0 + len(strain)*dt:.1f}")
        print(f"  Offset: {offset_sec:.1f}s, Mitte: Sample {center_sample}")
        return None, None
    
    segment = strain[center_sample - half : center_sample + half]
    t_rel = np.linspace(-window_sec/2, window_sec/2, len(segment))
    return segment, t_rel

def save_32s_hdf5(strain_h1, strain_l1, dt, event_gps, outdir):
    """Speichert die 32s-Segmente als kleine HDF5-Dateien."""
    try:
        import h5py
    except ImportError:
        return
    
    os.makedirs(outdir, exist_ok=True)
    
    for label, strain in [('H1', strain_h1), ('L1', strain_l1)]:
        fname = os.path.join(outdir, f"{label}_GW150914_32s.hdf5")
        with h5py.File(fname, 'w') as f:
            ds = f.create_dataset('strain', data=strain)
            ds.attrs['dt'] = dt
            ds.attrs['event_gps'] = event_gps
            ds.attrs['detector'] = label
            ds.attrs['description'] = 'GW150914 32s window, centered on event'
        print(f"Gespeichert: {fname} ({os.path.getsize(fname)/1024:.1f} KB)")

def compute_gamma_f(strain_h1, strain_l1, dt, nperseg=4096):
    """
    Berechnet die normalisierte Kreuzkorrelation Γ(f) im Frequenzbereich.
    
    Γ(f) = |S_HL(f)| / sqrt(S_H(f) · S_L(f))
    
    Theoretische Vorhersage RFT: 
    - Erste Nullstelle bei f_0 ≈ c/(2·d_HL) ≈ 50 Hz
    - ε-Modulation: Γ(f) sollte cos²-artige Struktur zeigen
    """
    from scipy.signal import welch, csd
    
    fs = 1.0 / dt
    
    # Cross-spectral density
    f, Sxy = csd(strain_h1, strain_l1, fs=fs, nperseg=nperseg)
    
    # Auto-spectral densities
    _, Sxx = welch(strain_h1, fs=fs, nperseg=nperseg)
    _, Syy = welch(strain_l1, fs=fs, nperseg=nperseg)
    
    # Γ(f) = |S_HL| / sqrt(S_H · S_L)
    denom = np.sqrt(Sxx * Syy)
    gamma = np.abs(Sxy) / np.where(denom > 0, denom, np.nan)
    
    return f, gamma, Sxy, Sxx, Syy

def rft_gamma_prediction(f, d_HL_m=3002e3):
    """
    RFT-Vorhersage für Γ(f).
    
    Overlap Reduction Function (ORF) nach Flanagan 1993:
    γ_ORF(f) = Fensterfunktion × Phasenfaktor
    
    Erste Nullstelle: f_null = c / (2·d_HL)
    Für H1-L1: d_HL ≈ 3002 km → f_null ≈ 50 Hz
    
    RFT-ε-Modulation: Γ_RFT(f) = ε(Δφ(f)) = cos²(π·f/f_null / 2)
    """
    c = 299792458  # m/s
    f_null = c / (2 * d_HL_m)
    
    # Einfache cos²-Modulation als RFT-Vorhersage
    gamma_rft = np.cos(np.pi * f / (2 * f_null))**2
    
    # Standard ORF (Flanagan 1993) für Vergleich
    alpha = 2 * np.pi * f * d_HL_m / c
    gamma_orf = np.sinc(2 * alpha / np.pi) * (1 - 1/(8*(alpha+1e-10)**2) + 1/(24*(alpha+1e-10)**4))
    
    return gamma_rft, np.abs(gamma_orf), f_null

def plot_results(f, gamma_obs, gamma_rft, gamma_orf, f_null, outdir):
    """Erstellt und speichert Analyseplots."""
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib nicht verfügbar — kein Plot")
        return None
    
    os.makedirs(outdir, exist_ok=True)
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # Oberes Panel: Γ(f) Vergleich
    ax1 = axes[0]
    mask = (f >= 10) & (f <= 500)
    ax1.plot(f[mask], gamma_obs[mask], 'b-', alpha=0.7, linewidth=1, label='Γ_obs(f) [LIGO GW150914]')
    ax1.plot(f[mask], gamma_rft[mask], 'r-', linewidth=2, label=f'Γ_RFT(f) = cos²(πf/2f₀)')
    ax1.plot(f[mask], gamma_orf[mask], 'g--', linewidth=1.5, label='Γ_ORF(f) [Flanagan 1993]')
    ax1.axvline(f_null, color='orange', linestyle=':', label=f'f₀ = {f_null:.1f} Hz (c/2d_HL)')
    ax1.set_xlabel('Frequenz f [Hz]')
    ax1.set_ylabel('Γ(f)')
    ax1.set_title('RT-58: RFT Γ(f)-Analyse — GW150914 (H1 × L1)')
    ax1.legend(fontsize=9)
    ax1.set_xlim(10, 500)
    ax1.set_ylim(0, 1.1)
    ax1.grid(True, alpha=0.3)
    
    # Unteres Panel: Log-Skala für Rauschen
    ax2 = axes[1]
    ax2.semilogy(f[mask], gamma_obs[mask], 'b-', alpha=0.7, linewidth=1)
    ax2.semilogy(f[mask], gamma_rft[mask], 'r-', linewidth=2)
    ax2.axvline(f_null, color='orange', linestyle=':')
    ax2.set_xlabel('Frequenz f [Hz]')
    ax2.set_ylabel('Γ(f) [log]')
    ax2.set_title('RT-58: Γ(f) logarithmisch')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(10, 500)
    
    plt.tight_layout()
    outfile = os.path.join(outdir, 'rt58_gamma_analysis.png')
    plt.savefig(outfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot gespeichert: {outfile}")
    return outfile

def compute_rft_epsilon(gamma_obs, f, f_null):
    """
    Berechnet ε aus den gemessenen Γ(f)-Werten.
    
    Aus RFT: Γ(f) = ε(Δφ(f)) = cos²(Δφ/2)
    → Δφ(f) = 2·arccos(√Γ)
    → ε(f) = Γ(f)
    """
    mask = (f >= 20) & (f <= 200)
    gamma_band = gamma_obs[mask]
    
    # Mittlere Kopplungseffizienz im LIGO-Band
    epsilon_mean = np.nanmean(gamma_band)
    epsilon_std = np.nanstd(gamma_band)
    
    # Vergleich mit ε₀ = Ω_Λ = 0.6847
    epsilon_0 = 0.6847
    delta_sigma = abs(epsilon_mean - epsilon_0) / epsilon_std if epsilon_std > 0 else np.nan
    
    return epsilon_mean, epsilon_std, delta_sigma

def main():
    parser = argparse.ArgumentParser(description='RT-58: LIGO Γ(f)-Analyse')
    parser.add_argument('--h1', required=True, help='H1 HDF5-Datei')
    parser.add_argument('--l1', required=True, help='L1 HDF5-Datei')
    parser.add_argument('--outdir', default='rt58_output', help='Ausgabeverzeichnis')
    parser.add_argument('--event-gps', type=float, default=1126259462.4,
                        help='GPS-Zeit des Ereignisses')
    args = parser.parse_args()
    
    print("=" * 60)
    print("RT-58: LIGO GW150914 — Γ(f)-Analyse (RFT)")
    print("=" * 60)
    
    # Daten laden
    print(f"\nLade H1: {args.h1}")
    strain_h1, dt, t0_h1 = load_hdf5_strain(args.h1)
    print(f"  Länge: {len(strain_h1)} Samples, dt={dt*1000:.4f} ms, GPS_start={t0_h1}")
    
    print(f"\nLade L1: {args.l1}")
    strain_l1, dt_l1, t0_l1 = load_hdf5_strain(args.l1)
    print(f"  Länge: {len(strain_l1)} Samples, dt={dt_l1*1000:.4f} ms, GPS_start={t0_l1}")
    
    # 32s-Segmente extrahieren
    print(f"\nExtrahiere 32s-Fenster um GPS {args.event_gps}...")
    seg_h1, t_rel = extract_event_window(strain_h1, dt, t0_h1, args.event_gps)
    seg_l1, _ = extract_event_window(strain_l1, dt_l1, t0_l1, args.event_gps)
    
    if seg_h1 is None or seg_l1 is None:
        print("FEHLER: Konnte 32s-Segment nicht extrahieren.")
        sys.exit(1)
    
    print(f"  Segment: {len(seg_h1)} Samples = {len(seg_h1)*dt:.1f}s")
    
    # Kleine Dateien speichern
    save_32s_hdf5(seg_h1, seg_l1, dt, args.event_gps, args.outdir)
    
    # Γ(f) berechnen
    print("\nBerechne Γ(f)...")
    f, gamma_obs, Sxy, Sxx, Syy = compute_gamma_f(seg_h1, seg_l1, dt)
    
    # RFT-Vorhersage
    gamma_rft, gamma_orf, f_null = rft_gamma_prediction(f)
    print(f"  Erste Nullstelle: f₀ = {f_null:.2f} Hz")
    
    # ε aus Γ(f)
    eps_mean, eps_std, delta_sig = compute_rft_epsilon(gamma_obs, f, f_null)
    
    print(f"\n--- ERGEBNISSE ---")
    print(f"ε_mean (20–200 Hz) = {eps_mean:.4f} ± {eps_std:.4f}")
    print(f"ε₀ = Ω_Λ = 0.6847")
    print(f"Abweichung: {delta_sig:.2f}σ")
    
    # Plots
    plot_results(f, gamma_obs, gamma_rft, gamma_orf, f_null, args.outdir)
    
    # Ergebnis als Text
    result_txt = os.path.join(args.outdir, 'rt58_ergebnis.txt')
    with open(result_txt, 'w', encoding='utf-8') as fp:
        fp.write(f"RT-58: LIGO GW150914 Γ(f)-Analyse\n")
        fp.write(f"=" * 50 + "\n")
        fp.write(f"ε_mean (20-200 Hz) = {eps_mean:.4f} ± {eps_std:.4f}\n")
        fp.write(f"ε₀ (Ω_Λ) = 0.6847\n")
        fp.write(f"Abweichung: {delta_sig:.2f}σ\n")
        fp.write(f"f_null = {f_null:.2f} Hz\n")
        fp.write(f"Daten: GW150914, GPS {args.event_gps}\n")
    
    print(f"\nErgebnis gespeichert: {result_txt}")
    print("=" * 60)

if __name__ == '__main__':
    main()
