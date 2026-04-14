"""
Resonanz-KI-Modell — Zwei gekoppelte Akteure und Feldanalyse

Simuliert die Kopplung zweier schwingender Akteure im Rahmen
der Resonanzfeldtheorie (Axiome A1–A4).

Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) wird dynamisch aus
der Phasendifferenz der Akteure berechnet.

Abhängigkeiten: numpy, matplotlib
Ausführung: python resonanz_ki.py
"""

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


# --- Kopplungseffizienz (Axiom 4) ---

def kopplungseffizienz(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """ε(Δφ) = cos²(Δφ/2) ∈ [0, 1]

    Maximale Effizienz bei Phasengleichheit (Δφ = 0),
    keine Kopplung bei Gegenphase (Δφ = π).
    """
    return np.cos(delta_phi / 2) ** 2


# --- Resonanzbedingung (Axiom 3) ---

def check_resonance(f1: float, f2: float, tolerance: float = 0.02) -> tuple[bool, int, int]:
    """Prüfe ob f1/f2 ≈ n/m mit n, m ∈ ℤ⁺."""
    if f2 == 0:
        return False, 0, 1
    ratio = Fraction(f1 / f2).limit_denominator(10)
    n, m = ratio.numerator, ratio.denominator
    is_resonant = np.isclose(f1 / f2, n / m, rtol=tolerance)
    return is_resonant, n, m


# --- Parameter ---

def init_parameter() -> dict[str, Any]:
    return {
        "f_akteur1": 1.0,
        "f_akteur2": 1.3,
        "phi1": 0.0,
        "phi2": 0.0,
        "h": 1.0,
        "t": np.linspace(0, 20, 2000),
    }


# --- Schwingung (Axiom 1) ---

def berechne_schwingung(f: float, t: np.ndarray, phi: float = 0.0) -> np.ndarray:
    """ψ(t) = cos(2πft + φ)"""
    return np.cos(2 * np.pi * f * t + phi)


# --- Resonanzfeld (Axiom 2: Superposition + Axiom 4: Kopplung) ---

def berechne_resonanzfeld(psi1: np.ndarray, psi2: np.ndarray, eps: float) -> np.ndarray:
    """Symmetrische Kopplung mit Kreuzterm.

    Φ = (1−ε)·ψ₁ + ε·ψ₂ + ε·ψ₁·ψ₂

    Der Kreuzterm modelliert nichtlineare Resonanzkopplung.
    """
    superposition = (1 - eps) * psi1 + eps * psi2
    coupling = eps * psi1 * psi2
    return superposition + coupling


# --- Resonanzenergie (Axiom 4) ---

def resonanzenergie(f1: float, f2: float, eps: float, h: float = 1.0) -> float:
    """E_eff = π · ε · h · f_res

    f_res = (f1 + f2) / 2 als mittlere Resonanzfrequenz.
    """
    f_res = (f1 + f2) / 2
    return np.pi * eps * h * f_res


# --- Fourier-Analyse ---

def fourier_analyse(signal: np.ndarray, t: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Normiertes Amplitudenspektrum."""
    n = len(t)
    dt_val = t[1] - t[0]
    f = np.fft.rfftfreq(n, dt_val)
    fft_abs = np.abs(np.fft.rfft(signal)) / n * 2
    return f, fft_abs


# --- Visualisierung ---

def plot_resonanzmodell(t: np.ndarray, psi1: np.ndarray, psi2: np.ndarray,
                        resonanzfeld: np.ndarray, params: dict[str, Any],
                        f: np.ndarray, fft_abs: np.ndarray) -> None:
    eps = params["eps"]
    delta_phi = params["delta_phi"]
    E_res = params["E_res"]
    is_resonant = params["is_resonant"]
    n_ratio = params["n_ratio"]
    m_ratio = params["m_ratio"]
    f1 = params["f_akteur1"]
    f2 = params["f_akteur2"]

    fig, axs = plt.subplots(3, 1, figsize=(12, 10))
    fig.canvas.manager.set_window_title(
        'Resonanz-KI-Modell (Axiome A1–A4)')

    # --- Plot 1: Schwingungen und Resonanzfeld ---
    axs[0].plot(t, psi1, label=f"Akteur 1: f₁ = {f1} Hz", alpha=0.7)
    axs[0].plot(t, psi2, label=f"Akteur 2: f₂ = {f2} Hz", alpha=0.7)
    axs[0].plot(t, resonanzfeld,
                label=f"Resonanzfeld (ε = {eps:.3f})",
                linewidth=2, color="k")
    res_text = (f"✓ Resonanz: f₁/f₂ ≈ {n_ratio}/{m_ratio}"
                if is_resonant
                else f"✗ Keine Resonanz: f₁/f₂ ≈ {f1/f2:.3f}")
    color = '#90EE90' if is_resonant else '#FFB6C1'
    axs[0].text(0.02, 0.92, res_text,
                transform=axs[0].transAxes, fontsize=9,
                verticalalignment='top',
                bbox=dict(facecolor=color, alpha=0.7))
    axs[0].set_title(f"A1 & A2: Schwingung und Superposition "
                     f"(E_res ≈ {E_res:.2f})")
    axs[0].set_xlabel("Zeit [s]")
    axs[0].set_ylabel("Amplitude")
    axs[0].legend(loc='upper right', fontsize=8)
    axs[0].grid(True, alpha=0.3)

    # --- Plot 2: Fourier-Analyse ---
    f_max = max(f1, f2) * 3
    mask = f <= f_max
    axs[1].stem(f[mask], fft_abs[mask], linefmt='purple',
                markerfmt='o', basefmt='gray')
    axs[1].set_title("Fourier-Analyse des Resonanzfelds")
    axs[1].set_xlabel("Frequenz [Hz]")
    axs[1].set_ylabel("Amplitude (normiert)")
    axs[1].set_xlim(0, f_max)
    axs[1].grid(True, alpha=0.3)

    # --- Plot 3: Kopplungseffizienz über Phasendifferenz ---
    phi_range = np.linspace(0, np.pi, 200)
    eps_range = kopplungseffizienz(phi_range)
    axs[2].plot(phi_range, eps_range, 'b-', linewidth=2,
                label=r'$\varepsilon(\Delta\varphi) = '
                      r'\cos^2(\Delta\varphi/2)$')
    axs[2].axvline(abs(delta_phi), color='red', linestyle='--',
                   label=f'Δφ = {delta_phi:.2f} → ε = {eps:.3f}')
    axs[2].axhline(eps, color='red', linestyle=':', alpha=0.5)
    axs[2].set_title("A4: Kopplungseffizienz")
    axs[2].set_xlabel("Phasendifferenz Δφ [rad]")
    axs[2].set_ylabel("ε (Kopplungseffizienz)")
    axs[2].set_xlim(0, np.pi)
    axs[2].set_ylim(-0.05, 1.05)
    axs[2].legend(fontsize=9)
    axs[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


# --- Hauptfunktion ---

def main() -> None:
    p = init_parameter()

    # Phasendifferenz und Kopplungseffizienz (Axiom 4)
    delta_phi = p["phi2"] - p["phi1"]
    eps = kopplungseffizienz(delta_phi)

    # Axiom 3: Resonanzcheck
    is_resonant, n, m = check_resonance(p["f_akteur1"],
                                        p["f_akteur2"])

    # Axiom 1: Schwingungen
    psi1 = berechne_schwingung(p["f_akteur1"], p["t"], p["phi1"])
    psi2 = berechne_schwingung(p["f_akteur2"], p["t"], p["phi2"])

    # Axiom 2 + 4: Superposition + Kopplung
    feld = berechne_resonanzfeld(psi1, psi2, eps)

    # Axiom 4: Resonanzenergie
    E_res = resonanzenergie(p["f_akteur1"], p["f_akteur2"],
                            eps, p["h"])

    # Fourier
    f, fft_abs = fourier_analyse(feld, p["t"])

    # Parameter-Zusammenfassung
    params = {
        **p,
        "eps": eps,
        "delta_phi": delta_phi,
        "E_res": E_res,
        "is_resonant": is_resonant,
        "n_ratio": n,
        "m_ratio": m,
    }

    # Konsolen-Output
    print("Resonanz-KI-Modell")
    print("=" * 50)
    print(f"f₁ = {p['f_akteur1']} Hz, f₂ = {p['f_akteur2']} Hz")
    print(f"Δφ = {delta_phi:.2f} rad")
    print(f"ε(Δφ) = cos²({delta_phi/2:.2f}) = {eps:.4f}")
    print(f"E_eff = π · {eps:.4f} · {p['h']} · "
          f"{(p['f_akteur1'] + p['f_akteur2'])/2:.2f} = {E_res:.4f}")
    print(f"Resonanz (A3): {is_resonant} (f₁/f₂ ≈ {n}/{m})")
    print("=" * 50)

    plot_resonanzmodell(p["t"], psi1, psi2, feld, params,
                        f, fft_abs)


if __name__ == "__main__":
    main()