# resonanzgenerator.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Simulation: Resonanzgenerator – Energiegewinnung durch
#             kohärente Feldkopplung an einen mechanischen Oszillator
#
# Physik:
#   Bewegungsgleichung: m·ẍ + d·ẋ + k·x = F_feld(t, Δφ)
#   Resonanzfeldkraft:  F_feld = F₀ · ε(Δφ) · cos(ω·t)
#   Kopplungseffizienz: ε(Δφ) = cos²(Δφ/2)  (aus RFT, κ = 1)
#   Grundformel:        E = π · ε(Δφ) · ℏ · f
#
# Die Simulation demonstriert:
#   1. Frequenz-Sweep: Resonanzkurve, Q-Faktor, Energieanalyse
#   2. Phasenscan: ε(Δφ) = cos²(Δφ/2) als messbare Signatur
#   3. Vergleich: Resonanz vs. Off-Resonanz, kohärent vs. inkohärent

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq
import os

# ============================================================
# 1. Naturkonstanten
# ============================================================

HBAR = 1.054571817e-34     # ℏ in J·s
PI = np.pi


# ============================================================
# 2. RFT-Kopplungseffizienz
# ============================================================

def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """
    ε(Δφ) = cos²(Δφ/2)

    Aus der RFT-Grundformel: E = π · ε · ℏ · f
    Die Identität ε = η (Kopplungseffizienz = Resonanzeffizienz)
    wurde in FLRW-Simulationen (1.530 Läufe) und
    Monte-Carlo-Analysen (1.500.000 Simulationen) validiert.
    """
    return np.cos(delta_phi / 2) ** 2


# ============================================================
# 3. Systemparameter
# ============================================================

class OscillatorSystem:
    """
    Gedämpfter harmonischer Oszillator mit Resonanzfeldkopplung.

    Bewegungsgleichung:
        m · ẍ + d · ẋ + k · x = F₀ · ε(Δφ) · cos(ω·t)

    Parameter sind so gewählt, dass sie einem realen
    makroskopischen System entsprechen (z.B. Piezo-Harvester
    auf einem Schwingungstisch).
    """

    def __init__(self, m: float = 0.1, k: float = 10.0, d: float = 0.05,
                 F0: float = 0.1) -> None:
        self.m = m          # Masse [kg]
        self.k = k          # Federkonstante [N/m]
        self.d = d          # Dämpfungskoeffizient [N·s/m]

        # Abgeleitete Größen
        self.omega_0 = np.sqrt(k / m)                    # Eigenkreisfrequenz [rad/s]
        self.f_0 = self.omega_0 / (2 * PI)               # Eigenfrequenz [Hz]
        self.Q_theo = np.sqrt(m * k) / d                  # Theoretischer Q-Faktor
        self.tau = 2 * m / d                              # Abklingzeit [s]

        # Resonanzfeldkraft
        # F₀ ist die Amplitude der externen Anregung.
        # In der RFT-Interpretation: F₀ = π · ℏ · ω₀ · N_eff
        # wobei N_eff die effektive Feldstärke (Photonenzahl o.ä.) ist.
        # Für ein makroskopisches Demonstrationssystem setzen wir
        # F₀ direkt als physikalische Kraftamplitude.
        self.F0 = F0        # Kraftamplitude [N]

    def resonance_force(self, t: float | np.ndarray, omega: float,
                        delta_phi: float = 0.0) -> float | np.ndarray:
        """
        F_feld(t, Δφ) = F₀ · ε(Δφ) · cos(ω·t)

        Args:
            t: Zeit [s]
            omega: Anregungskreisfrequenz [rad/s]
            delta_phi: Phasendifferenz [rad]

        Returns:
            Kraft [N]
        """
        eps = coupling_efficiency(delta_phi)
        return self.F0 * eps * np.cos(omega * t)

    def rft_energy(self, f: float, delta_phi: float = 0.0) -> float:
        """
        E_RFT = π · ε(Δφ) · ℏ · f

        Energie eines einzelnen Feldquants bei Frequenz f.
        """
        return PI * coupling_efficiency(delta_phi) * HBAR * f

    def info(self) -> None:
        """Druckt Systemparameter."""
        print("=" * 60)
        print("RESONANZGENERATOR: Systemparameter")
        print("=" * 60)
        print(f"  Masse m:              {self.m} kg")
        print(f"  Federkonstante k:     {self.k} N/m")
        print(f"  Dämpfung d:           {self.d} N·s/m")
        print(f"  Eigenfrequenz f₀:     {self.f_0:.4f} Hz")
        print(f"  Eigenkreisfrequenz ω₀: {self.omega_0:.4f} rad/s")
        print(f"  Q-Faktor (theor.):    {self.Q_theo:.1f}")
        print(f"  Abklingzeit τ:        {self.tau:.2f} s")
        print(f"  Kraftamplitude F₀:    {self.F0} N")
        print(f"  E_RFT(f₀, Δφ=0):     {self.rft_energy(self.f_0):.4e} J")
        print("=" * 60)


# ============================================================
# 4. Simulation: Euler-Integration
# ============================================================

def simulate(sys: OscillatorSystem, omega: float, delta_phi: float,
             x0: float, v0: float, t_array: np.ndarray,
             dt: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Simuliert den gedämpften Oszillator mit Resonanzfeldkopplung.

    Returns:
        x, v, E_kin, E_pot, E_field, F_field_array
    """
    n = len(t_array)
    x = np.zeros(n)
    v = np.zeros(n)
    E_kin = np.zeros(n)
    E_pot = np.zeros(n)
    F_field_arr = np.zeros(n)

    x[0] = x0
    v[0] = v0

    for i in range(n - 1):
        F_f = sys.resonance_force(t_array[i], omega, delta_phi)
        F_spring = -sys.k * x[i]
        F_damp = -sys.d * v[i]
        F_total = F_f + F_spring + F_damp

        a = F_total / sys.m
        v[i + 1] = v[i] + a * dt
        x[i + 1] = x[i] + v[i + 1] * dt  # Symplektisches Euler

        E_kin[i] = 0.5 * sys.m * v[i] ** 2
        E_pot[i] = 0.5 * sys.k * x[i] ** 2
        F_field_arr[i] = F_f

    # Letzter Zeitschritt
    E_kin[-1] = 0.5 * sys.m * v[-1] ** 2
    E_pot[-1] = 0.5 * sys.k * x[-1] ** 2
    F_field_arr[-1] = sys.resonance_force(t_array[-1], omega, delta_phi)

    # Kumulierte Feldarbeit
    E_field = np.cumsum(F_field_arr * v) * dt

    return x, v, E_kin, E_pot, E_field, F_field_arr


# ============================================================
# 5. Experiment 1: Frequenz-Sweep
# ============================================================

def frequency_sweep(sys: OscillatorSystem, f_min: float = 0.5,
                    f_max: float = 15.0, n_f: int = 200,
                    t_max: float = 20.0, dt: float = 0.0005,
                    delta_phi: float = 0.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Scannt die Anregungsfrequenz und misst:
    - Maximale Amplitude (stationär)
    - Energiegewinn ΔE
    - Integrierte Feldarbeit
    - Q-Faktor aus Halbwertsbreite
    """
    t_array = np.arange(0, t_max, dt)
    frequencies = np.linspace(f_min, f_max, n_f)
    x0, v0 = 0.0, 0.0  # Start aus Ruhe (kein Bias!)

    max_amp = np.zeros(n_f)
    field_work = np.zeros(n_f)
    mean_energy = np.zeros(n_f)

    for idx, f in enumerate(frequencies):
        omega = 2 * PI * f
        x, v, Ek, Ep, Ef, Ff = simulate(sys, omega, delta_phi,
                                          x0, v0, t_array, dt)
        # Stationärer Bereich (letzte 50%)
        n_half = len(t_array) // 2
        max_amp[idx] = np.max(np.abs(x[n_half:]))
        mean_energy[idx] = np.mean(Ek[n_half:] + Ep[n_half:])
        field_work[idx] = Ef[-1]

    return frequencies, max_amp, mean_energy, field_work


# ============================================================
# 6. Experiment 2: Phasenscan (RFT-Signatur)
# ============================================================

def phase_scan(sys: OscillatorSystem, n_phi: int = 50, t_max: float = 20.0,
               dt: float = 0.0005) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Scannt Δφ von 0 bis 2π bei f = f₀.
    Misst die stationäre Amplitude und Energie.

    RFT-Vorhersage: Amplitude ∝ ε(Δφ) = cos²(Δφ/2)
    """
    t_array = np.arange(0, t_max, dt)
    omega_0 = sys.omega_0
    x0, v0 = 0.0, 0.0

    delta_phis = np.linspace(0, 2 * PI, n_phi)
    max_amp = np.zeros(n_phi)
    mean_energy = np.zeros(n_phi)
    field_work = np.zeros(n_phi)

    for idx, dp in enumerate(delta_phis):
        x, v, Ek, Ep, Ef, Ff = simulate(sys, omega_0, dp,
                                          x0, v0, t_array, dt)
        n_half = len(t_array) // 2
        max_amp[idx] = np.max(np.abs(x[n_half:]))
        mean_energy[idx] = np.mean(Ek[n_half:] + Ep[n_half:])
        field_work[idx] = Ef[-1]

    return delta_phis, max_amp, mean_energy, field_work


# ============================================================
# 7. Experiment 3: Detailanalyse am Resonanzpunkt
# ============================================================

def resonance_detail(sys: OscillatorSystem, delta_phi: float = 0.0,
                     t_max: float = 20.0,
                     dt: float = 0.0005) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Detaillierte Analyse bei f = f₀ und gegebenem Δφ.
    Zeigt: Zeitsignal, Energieverlauf, Phasenraum, FFT.
    """
    t_array = np.arange(0, t_max, dt)
    omega_0 = sys.omega_0

    x, v, Ek, Ep, Ef, Ff = simulate(sys, omega_0, delta_phi,
                                      0.0, 0.0, t_array, dt)

    return t_array, x, v, Ek, Ep, Ef, Ff


# ============================================================
# 8. Plots
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def plot_frequency_sweep(sys: OscillatorSystem, freqs: np.ndarray,
                        amp: np.ndarray, energy: np.ndarray,
                        work: np.ndarray, output_dir: str) -> None:
    """Plot 1: Resonanzkurve + Energieanalyse."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Resonanzkurve
    ax = axes[0]
    ax.plot(freqs, amp * 1000, 'b-', linewidth=1.5)
    ax.axvline(sys.f_0, color='r', ls=':', linewidth=1,
               label=f'f₀ = {sys.f_0:.2f} Hz')

    # Q-Faktor aus Halbwertsbreite
    peak_idx = np.argmax(amp)
    peak_amp = amp[peak_idx]
    half = peak_amp / np.sqrt(2)
    above = amp > half
    if np.any(above):
        f_left = freqs[np.argmax(above)]
        f_right = freqs[len(above) - 1 - np.argmax(above[::-1])]
        if f_right > f_left:
            Q_meas = freqs[peak_idx] / (f_right - f_left)
            ax.axhline(half * 1000, color='gray', ls='--', alpha=0.5,
                       label=f'FWHM → Q = {Q_meas:.0f}')
            ax.axvspan(f_left, f_right, alpha=0.1, color='red')

    ax.set_xlabel('Feldfrequenz f [Hz]')
    ax.set_ylabel('Max. Amplitude [mm]')
    ax.set_title('Resonanzkurve')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Mittlere Energie
    ax = axes[1]
    ax.plot(freqs, energy * 1e6, 'g-', linewidth=1.5)
    ax.axvline(sys.f_0, color='r', ls=':', linewidth=1,
               label=f'f₀ = {sys.f_0:.2f} Hz')
    ax.set_xlabel('Feldfrequenz f [Hz]')
    ax.set_ylabel('⟨E_mech⟩ [µJ]')
    ax.set_title('Mittlere mechanische Energie')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Feldarbeit
    ax = axes[2]
    ax.plot(freqs, work * 1e3, 'orange', linewidth=1.5)
    ax.axvline(sys.f_0, color='r', ls=':', linewidth=1,
               label=f'f₀ = {sys.f_0:.2f} Hz')
    ax.set_xlabel('Feldfrequenz f [Hz]')
    ax.set_ylabel('Feldarbeit W_feld [mJ]')
    ax.set_title('Kumulierte Feldarbeit')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    fig.suptitle(f'Resonanzgenerator: Frequenz-Sweep (F₀ = {sys.F0} N, '
                 f'd = {sys.d}, Δφ = 0)', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'frequenz_sweep.png'), dpi=150)
    plt.close()
    print("  → frequenz_sweep.png")


def plot_phase_scan(sys: OscillatorSystem, phis: np.ndarray,
                    amp: np.ndarray, energy: np.ndarray,
                    work: np.ndarray, output_dir: str) -> None:
    """Plot 2: Phasenscan — die RFT-Signatur."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Normierte Amplitude vs. Δφ
    ax = axes[0]
    amp_norm = amp / np.max(amp) if np.max(amp) > 0 else amp
    ax.plot(phis / PI, amp_norm, 'b-', linewidth=2, label='Simulation')
    # Theoretische Kurve
    eps_theo = coupling_efficiency(phis)
    # Stationäre Amplitude ∝ F₀·ε/(d·ω₀) → ∝ ε
    eps_norm = eps_theo / np.max(eps_theo)
    ax.plot(phis / PI, eps_norm, 'r--', linewidth=1.5,
            label='Theorie: ε(Δφ) = cos²(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Normierte Amplitude')
    ax.set_title('Amplitude vs. Phasendifferenz')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # Energie vs. Δφ
    ax = axes[1]
    energy_norm = energy / np.max(energy) if np.max(energy) > 0 else energy
    ax.plot(phis / PI, energy_norm, 'g-', linewidth=2, label='Simulation')
    # Energie ∝ Amplitude² ∝ ε² = cos⁴(Δφ/2)
    eps_sq = eps_theo ** 2
    eps_sq_norm = eps_sq / np.max(eps_sq)
    ax.plot(phis / PI, eps_sq_norm, 'r--', linewidth=1.5,
            label='Theorie: ε² = cos⁴(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Normierte Energie')
    ax.set_title('⟨E_mech⟩ vs. Phasendifferenz')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # Verhältnis kohärent/inkohärent
    ax = axes[2]
    # Signal: Energie bei Δφ vs. Energie gemittelt über alle Phasen
    mean_ink = np.mean(energy)  # ≈ Energie bei η = 0.5
    if mean_ink > 0:
        ratio = energy / mean_ink
    else:
        ratio = np.ones_like(energy)
    ax.plot(phis / PI, ratio, 'b-', linewidth=2)
    ax.axhline(2.0, color='red', ls=':', label='Δφ=0: Ratio = 2.0 (RFT)')
    ax.axhline(1.0, color='gray', ls='--', label='Inkohärent: Ratio = 1.0')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('E(Δφ) / ⟨E⟩_inkohärent')
    ax.set_title('RFT-Signatur: Kohärent vs. Inkohärent')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    fig.suptitle(f'Resonanzgenerator: Phasenscan bei f = f₀ '
                 f'(RFT: ε = cos²(Δφ/2), κ = 1)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'phasenscan.png'), dpi=150)
    plt.close()
    print("  → phasenscan.png")


def plot_resonance_detail(sys: OscillatorSystem, t: np.ndarray,
                         x: np.ndarray, v: np.ndarray, Ek: np.ndarray,
                         Ep: np.ndarray, Ef: np.ndarray,
                         Ff: np.ndarray, output_dir: str) -> None:
    """Plot 3: Detailanalyse am Resonanzpunkt."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Zeitsignal
    ax = axes[0, 0]
    ax.plot(t, x * 1000, 'b-', linewidth=0.5)
    ax.set_xlabel('Zeit [s]')
    ax.set_ylabel('Auslenkung x [mm]')
    ax.set_title(f'Zeitsignal am Resonanzpunkt (f₀ = {sys.f_0:.2f} Hz)')
    ax.grid(True, alpha=0.3)

    # Energieverlauf
    ax = axes[0, 1]
    E_total = Ek + Ep
    ax.plot(t, E_total * 1e6, 'k-', linewidth=1, label='E_ges')
    ax.plot(t, Ek * 1e6, 'r--', linewidth=0.5, alpha=0.5, label='E_kin')
    ax.plot(t, Ep * 1e6, 'b--', linewidth=0.5, alpha=0.5, label='E_pot')
    ax.plot(t, Ef * 1e6, 'g-', linewidth=1, label='W_feld (kumuliert)')
    ax.set_xlabel('Zeit [s]')
    ax.set_ylabel('Energie [µJ]')
    ax.set_title('Energieverlauf')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Phasenraum
    ax = axes[1, 0]
    # Nur stationären Teil plotten
    n_half = len(t) // 2
    ax.plot(x[n_half:] * 1000, v[n_half:] * 1000, 'b-', linewidth=0.3)
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('v [mm/s]')
    ax.set_title('Phasenraum (stationär)')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    # FFT
    ax = axes[1, 1]
    N = len(x)
    xf = rfftfreq(N, t[1] - t[0])
    Xf = np.abs(rfft(x))
    ax.semilogy(xf, Xf, 'b-', linewidth=0.5)
    ax.axvline(sys.f_0, color='r', ls=':', label=f'f₀ = {sys.f_0:.2f} Hz')
    ax.set_xlabel('Frequenz [Hz]')
    ax.set_ylabel('Amplitude (log)')
    ax.set_title('Frequenzspektrum (FFT)')
    ax.set_xlim(0, 3 * sys.f_0)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    fig.suptitle('Resonanzgenerator: Detailanalyse am Resonanzpunkt (Δφ = 0)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'resonanz_detail.png'), dpi=150)
    plt.close()
    print("  → resonanz_detail.png")


def plot_damping_comparison(sys: OscillatorSystem,
                           output_dir: str) -> None:
    """Plot 4: Vergleich verschiedener Dämpfungen."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    dampings = [0.01, 0.05, 0.1, 0.5, 1.0]
    colors = ['red', 'orange', 'green', 'blue', 'purple']

    for d_val, color in zip(dampings, colors):
        sys_d = OscillatorSystem(m=sys.m, k=sys.k, d=d_val, F0=sys.F0)
        Q_val = sys_d.Q_theo
        freqs, amp, energy, work = frequency_sweep(
            sys_d, f_min=0.5, f_max=15.0, n_f=150,
            t_max=20.0, dt=0.0005
        )
        axes[0].plot(freqs, amp * 1000, color=color, linewidth=1.5,
                     label=f'd = {d_val}, Q = {Q_val:.0f}')
        axes[1].plot(freqs, energy * 1e6, color=color, linewidth=1.5,
                     label=f'd = {d_val}')

    for ax in axes:
        ax.axvline(sys.f_0, color='gray', ls=':', alpha=0.5)
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('Feldfrequenz f [Hz]')

    axes[0].set_ylabel('Max. Amplitude [mm]')
    axes[0].set_title('Resonanzkurve vs. Dämpfung')
    axes[1].set_ylabel('⟨E_mech⟩ [µJ]')
    axes[1].set_title('Mittlere Energie vs. Dämpfung')

    fig.suptitle('Resonanzgenerator: Einfluss der Dämpfung (Q-Faktor)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'daempfung_vergleich.png'), dpi=150)
    plt.close()
    print("  → daempfung_vergleich.png")


# ============================================================
# 9. Hauptprogramm
# ============================================================

def main() -> None:
    print("=" * 60)
    print("RESONANZGENERATOR: Frequenz-Sweep + Phasenscan")
    print("Resonanzfeldtheorie: E = π · ε(Δφ) · ℏ · f")
    print("ε(Δφ) = cos²(Δφ/2), κ = 1 (parameterfrei)")
    print("=" * 60)

    output_dir = "figures"
    ensure_dir(output_dir)

    # --- System initialisieren ---
    sys = OscillatorSystem(m=0.1, k=10.0, d=0.05, F0=0.1)
    sys.info()

    # --- Experiment 1: Frequenz-Sweep ---
    print("\n=== Experiment 1: Frequenz-Sweep (Δφ = 0) ===")
    freqs, amp, energy, work = frequency_sweep(
        sys, f_min=0.5, f_max=15.0, n_f=200,
        t_max=20.0, dt=0.0005, delta_phi=0.0
    )

    peak_idx = np.argmax(amp)
    print(f"  Resonanzfrequenz (gemessen): {freqs[peak_idx]:.4f} Hz")
    print(f"  Eigenfrequenz (theor.):      {sys.f_0:.4f} Hz")
    print(f"  Max. Amplitude:              {amp[peak_idx]*1000:.2f} mm")
    print(f"  Max. ⟨E_mech⟩:              {energy[peak_idx]*1e6:.2f} µJ")
    print(f"  Feldarbeit am Peak:          {work[peak_idx]*1e3:.4f} mJ")

    # Wirkungsgrad: eingespeiste Energie vs. mechanische Energie
    # Eingespeiste Leistung: P_in = F₀²/(2·d) (bei Resonanz, stationär)
    P_in_theo = sys.F0**2 / (2 * sys.d)
    t_max_sim = 20.0
    W_in_theo = P_in_theo * t_max_sim
    eta = energy[peak_idx] / (W_in_theo / t_max_sim) if W_in_theo > 0 else 0
    print(f"  P_in (theor., Resonanz):     {P_in_theo:.4f} W")
    print(f"  η = ⟨E_mech⟩ / P_in:        {eta:.4f}")
    print(f"  Q-Faktor (theor.):           {sys.Q_theo:.1f}")

    plot_frequency_sweep(sys, freqs, amp, energy, work, output_dir)

    # --- Experiment 2: Phasenscan ---
    print("\n=== Experiment 2: Phasenscan bei f = f₀ ===")
    phis, amp_p, energy_p, work_p = phase_scan(
        sys, n_phi=50, t_max=20.0, dt=0.0005
    )

    print(f"  Δφ = 0 (Resonanz):    A = {amp_p[0]*1000:.4f} mm, "
          f"E = {energy_p[0]*1e6:.4f} µJ")
    print(f"  Δφ = π/2:             A = {amp_p[len(phis)//4]*1000:.4f} mm, "
          f"E = {energy_p[len(phis)//4]*1e6:.4f} µJ")
    print(f"  Δφ = π (Anti):        A = {amp_p[len(phis)//2]*1000:.4f} mm, "
          f"E = {energy_p[len(phis)//2]*1e6:.4f} µJ")

    # Verhältnis kohärent / inkohärent
    E_koh = energy_p[0]
    E_ink = np.mean(energy_p)  # Mittel über alle Phasen ≈ η = 0.5
    if E_ink > 0:
        ratio = E_koh / E_ink
        print(f"\n  RFT-Signatur:")
        print(f"    E(Δφ=0) / ⟨E⟩_ink = {ratio:.4f}")
        print(f"    Theorie (cos⁴/⟨cos⁴⟩): ≈ {1.0 / np.mean(coupling_efficiency(phis)**2):.4f}")
    else:
        print("  (Kein Energietransfer)")

    plot_phase_scan(sys, phis, amp_p, energy_p, work_p, output_dir)

    # --- Experiment 3: Detailanalyse ---
    print("\n=== Experiment 3: Detailanalyse am Resonanzpunkt ===")
    t, x, v, Ek, Ep, Ef, Ff = resonance_detail(
        sys, delta_phi=0.0, t_max=20.0, dt=0.0005
    )
    n_half = len(t) // 2
    E_stat = np.mean(Ek[n_half:] + Ep[n_half:])
    A_stat = np.max(np.abs(x[n_half:]))
    print(f"  Stationäre Amplitude:  {A_stat*1000:.4f} mm")
    print(f"  Stationäre ⟨E_mech⟩:  {E_stat*1e6:.4f} µJ")
    print(f"  Kumulierte Feldarbeit: {Ef[-1]*1e3:.4f} mJ")

    plot_resonance_detail(sys, t, x, v, Ek, Ep, Ef, Ff, output_dir)

    # --- Experiment 4: Dämpfungsvergleich ---
    print("\n=== Experiment 4: Dämpfungsvergleich ===")
    plot_damping_comparison(sys, output_dir)

    # --- Zusammenfassung ---
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("=" * 60)
    print(f"""
  Resonanzgenerator: Mechanischer Oszillator mit Feldkopplung

  Grundformel:    E = π · ε(Δφ) · ℏ · f
  Kopplung:       ε(Δφ) = cos²(Δφ/2), κ = 1

  System:
    m = {sys.m} kg, k = {sys.k} N/m, d = {sys.d} N·s/m
    f₀ = {sys.f_0:.4f} Hz, Q = {sys.Q_theo:.1f}
    F₀ = {sys.F0} N

  Ergebnisse:
    Resonanzpeak bei f = {freqs[peak_idx]:.4f} Hz (theor.: {sys.f_0:.4f})
    Max. Amplitude: {amp[peak_idx]*1000:.2f} mm
    Stationäre Energie: {E_stat*1e6:.2f} µJ

  Phasenscan:
    E(Δφ=0) / ⟨E⟩ = {ratio:.4f}
    Amplitude folgt cos²(Δφ/2)
    Energie folgt cos⁴(Δφ/2)

  Gleiche Physik wie Resonanzreaktor (GDR, Am-241):
    Makro: f₀ ~ 1 Hz,    F = F₀·ε·cos(ωt)
    Nuklear: f₀ ~ 10²¹ Hz, λ_eff = λ₀ + η·Φ·σ_GDR
    Beide: ε = η = cos²(Δφ/2), κ = 1
""")
    print("Plots gespeichert unter:", output_dir)
    print("Fertig.")


if __name__ == "__main__":
    main()