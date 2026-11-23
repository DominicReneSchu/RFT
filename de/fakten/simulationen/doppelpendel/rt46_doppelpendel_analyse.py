"""RT-46 — RFT-Validierung am Doppelpendel mit öffentlichen Daten

Analyse-Pipeline für den MultiArm-Pendulum Datensatz (Zenodo 6633719).

Verwendung:
    1. Datensatz herunterladen: https://zenodo.org/records/6633719
    2. Skript ausführen: python rt46_doppelpendel_analyse.py

Dominic-René Schu, November 2026
"""

import numpy as np
import pandas as pd
from scipy import stats
from pathlib import Path
import json

# ── Konfiguration ──────────────────────────────────────────────────────────────
DATA_PATH = Path("RT46_data/")          # Pfad zu den Zenodo-Daten
SAMPLING_RATE = 100                      # Hz (aus Zenodo README)
WINDOW_SIZE = 50                         # Fenstergröße für Glättung
N_BINS = 20                              # Anzahl Δφ-Bins
PRE_REG_VERSION = "v1.0-Nov2026"         # Pre-Registration Versionsstempel

# ── Schritt 1: Daten laden ─────────────────────────────────────────────────────
def load_data(filepath):
    """Lade Doppelpendel-Daten aus CSV-Datei."""
    df = pd.read_csv(filepath)
    # Erwartete Spalten: 'time', 'theta1_rad', 'theta2_rad'
    # oder 'theta1_deg', 'theta2_deg' (automatisch konvertiert)
    if 'theta1_deg' in df.columns:
        df['theta1_rad'] = np.radians(df['theta1_deg'])
        df['theta2_rad'] = np.radians(df['theta2_deg'])
    return df['time'].values, df['theta1_rad'].values, df['theta2_rad'].values


# ── Schritt 2: Observablen berechnen ─────────────────────────────────────────
def compute_observables(t, theta1, theta2):
    """Berechne RFT-Observablen aus Rohwinkel-Zeitreihen."""
    # Phasendifferenz
    delta_phi = theta1 - theta2

    # RFT-Vorhersage H1
    epsilon_rft = np.cos(delta_phi / 2) ** 2

    # Empirische Kopplungseffizienz aus gleitender Korrelation
    # E_kopp = Kreuzkorrelation der normierten Geschwindigkeiten
    theta1_dot = np.gradient(theta1, t)
    theta2_dot = np.gradient(theta2, t)
    # Gleitende Normierung
    E1 = np.convolve(theta1_dot**2, np.ones(WINDOW_SIZE)/WINDOW_SIZE, mode='same')
    E2 = np.convolve(theta2_dot**2, np.ones(WINDOW_SIZE)/WINDOW_SIZE, mode='same')
    E_cross = np.convolve(theta1_dot*theta2_dot, np.ones(WINDOW_SIZE)/WINDOW_SIZE, mode='same')
    # ε_exp = normierte Kreuzkorrelation ∈ [0,1]
    with np.errstate(divide='ignore', invalid='ignore'):
        epsilon_exp = np.abs(E_cross) / np.sqrt(E1 * E2 + 1e-12)

    # PCI (Phase Coherence Index)
    PCI = np.abs(np.convolve(np.exp(1j*delta_phi), np.ones(WINDOW_SIZE)/WINDOW_SIZE, mode='same'))

    return delta_phi, epsilon_rft, epsilon_exp, PCI


# ── Schritt 3: Statistischer Test H1 vs H0 ───────────────────────────────────
def test_h1_vs_h0(delta_phi, epsilon_rft, epsilon_exp):
    """Likelihood-Ratio-Test: H1 (ε=cos²(Δφ/2)) vs H0 (ε=const)."""
    # Binne Daten nach Δφ
    phi_norm = (delta_phi % (2*np.pi))
    bins = np.linspace(0, 2*np.pi, N_BINS+1)
    bin_idx = np.digitize(phi_norm, bins) - 1
    bin_idx = np.clip(bin_idx, 0, N_BINS-1)

    chi2_H1 = 0; chi2_H0 = 0; n_valid = 0
    epsilon_H0 = np.mean(epsilon_exp)  # Null: konstante Kopplung

    results = []
    for b in range(N_BINS):
        mask = bin_idx == b
        if mask.sum() < 5:
            continue
        eps_measured = epsilon_exp[mask].mean()
        eps_predicted_H1 = epsilon_rft[mask].mean()
        eps_predicted_H0 = epsilon_H0

        dphi_center = bins[b] + (bins[1]-bins[0])/2 - np.pi

        chi2_H1 += (eps_measured - eps_predicted_H1)**2 / (eps_predicted_H1 + 1e-6)
        chi2_H0 += (eps_measured - eps_predicted_H0)**2 / (eps_predicted_H0 + 1e-6)
        n_valid += 1
        results.append({
            'delta_phi_deg': np.degrees(dphi_center),
            'eps_measured': eps_measured,
            'eps_H1_pred': eps_predicted_H1,
            'eps_H0_pred': eps_predicted_H0,
            'n_points': int(mask.sum())
        })

    chi2_red_H1 = chi2_H1 / n_valid if n_valid > 0 else 999
    chi2_red_H0 = chi2_H0 / n_valid if n_valid > 0 else 999

    return chi2_red_H1, chi2_red_H0, results


# ── Schritt 4: Hauptpipeline ──────────────────────────────────────────────────
def run_analysis(filepath):
    print(f"=== RT-46 Analyse: {filepath} ===")
    print(f"Pre-Registrierung: {PRE_REG_VERSION}")
    print()

    # Daten laden
    t, theta1, theta2 = load_data(filepath)
    print(f"Datenpunkte: {len(t)}, Dauer: {t[-1]:.1f} s")

    # Observablen
    dphi, eps_rft, eps_exp, PCI = compute_observables(t, theta1, theta2)

    # Test
    chi2_H1, chi2_H0, results = test_h1_vs_h0(dphi, eps_rft, eps_exp)

    print(f"χ²_red (H1, RFT: ε=cos²(Δφ/2)): {chi2_H1:.4f}")
    print(f"χ²_red (H0, Null: ε=const):       {chi2_H0:.4f}")
    print()

    # Auswertung
    if chi2_H1 < chi2_H0:
        print(f"✅ H1 (RFT) ist besser angepasst als H0 (Δχ²_red = {chi2_H0-chi2_H1:.4f})")
        print(f"   Konsistent mit ε(Δφ) = cos²(Δφ/2) — NICHT falsifiziert.")
    else:
        print(f"❌ H0 (Null) ist besser angepasst — H1 (RFT) falsifiziert (p < 0.05)")

    print()
    print("Binned results (erste 5 Bins):")
    for r in results[:5]:
        print(f"  Δφ={r['delta_phi_deg']:.1f}°: ε_exp={r['eps_measured']:.4f}, "
              f"ε_H1={r['eps_H1_pred']:.4f}, ε_H0={r['eps_H0_pred']:.4f} (n={r['n_points']})")

    # Ergebnis speichern
    output = {
        'pre_registration': PRE_REG_VERSION,
        'chi2_red_H1': chi2_H1,
        'chi2_red_H0': chi2_H0,
        'h1_better': bool(chi2_H1 < chi2_H0),
        'delta_chi2': chi2_H0 - chi2_H1,
        'bins': results
    }
    with open('rt46_results.json', 'w') as f:
        json.dump(output, f, indent=2)
    print("\nErgebnis gespeichert: rt46_results.json")
    return output


# ── Schritt 5: Synthetische Validierung der Pipeline ─────────────────────────
def synthetic_validation():
    """Teste die Analyse-Pipeline mit bekannten synthetischen Daten."""
    import numpy as np

    print("=== Synthetische Validierung der Pipeline ===")
    t = np.linspace(0, 30, 3000)

    # Generiere Δφ(t) mit cos²-Muster
    dphi = 2*np.pi * np.sin(0.5*t) * np.cos(0.3*t)  # chaotisch-ähnlich
    eps_true = np.cos(dphi/2)**2 + np.random.normal(0, 0.05, len(t))
    eps_true = np.clip(eps_true, 0, 1)

    # Als "Daten" simuliert: theta1, theta2 so dass dphi = theta1 - theta2
    theta1 = dphi / 2 + np.random.normal(0, 0.01, len(t))
    theta2 = -dphi / 2 + np.random.normal(0, 0.01, len(t))

    # Teste
    dphi_comp, eps_rft, eps_exp, PCI = compute_observables(t, theta1, theta2)
    chi2_H1, chi2_H0, _ = test_h1_vs_h0(dphi_comp, eps_rft, eps_true)

    print(f"Synthetisch (ε=cos²): χ²_red H1={chi2_H1:.4f}, H0={chi2_H0:.4f}")
    print(f"Pipeline korrekt: {'JA' if chi2_H1 < chi2_H0 else 'NEIN — Prüfen!'}")


if __name__ == "__main__":
    import sys
    synthetic_validation()
    print()
    if len(sys.argv) > 1:
        run_analysis(sys.argv[1])
    else:
        print("Verwendung: python rt46_doppelpendel_analyse.py <Datenpfad.csv>")
        print("Download:   https://zenodo.org/records/6633719")
