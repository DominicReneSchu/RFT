# nichtlineare_resonanzanalyse.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Nichtlinearer Oszillator mit RFT-Phasenkopplung
#
# Physik:
#   m·ẍ + d(E)·ẋ + k·x + β·x³ = F₀·ε(Δφ)·cos(ω_f·t)
#   ε(Δφ) = cos²(Δφ/2)  (RFT-Kopplungseffizienz)
#   d(E) = d₀ · (1 + α_d · E)  (energieabhängige Dämpfung)
#
# Nutzung:
#   python nichtlineare_resonanzanalyse.py          → Matplotlib (4 Plots)
#   streamlit run nichtlineare_resonanzanalyse.py   → Interaktive App

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.signal import spectrogram
import os

# ============================================================
# 1. RFT-Kopplungseffizienz
# ============================================================

PI = np.pi


def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """ε(Δφ) = cos²(Δφ/2) — universelle Kopplungsfunktion (RFT)."""
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 2. Nichtlinearer Oszillator
# ============================================================

class NonlinearOscillator:
    """
    Nichtlinearer gedämpfter Oszillator mit RFT-Kopplung.

    m·ẍ + d(E)·ẋ + k·x + β·x³ = F₀·ε(Δφ)·cos(ω_f·t)

    d(E) = d₀ · (1 + α_d · E)
    ε(Δφ) = cos²(Δφ/2)
    """

    def __init__(self, m: float = 0.1, k: float = 10.0, d0: float = 0.05,
                 F0: float = 0.1, beta: float = 0.0,
                 alpha_d: float = 0.0) -> None:
        self.m = m
        self.k = k
        self.d0 = d0
        self.F0 = F0
        self.beta = beta        # Duffing-Nichtlinearität
        self.alpha_d = alpha_d  # Energieabhängige Dämpfung

        # Abgeleitete Größen
        self.omega_0 = np.sqrt(k / m)
        self.f_0 = self.omega_0 / (2 * PI)
        self.Q_theo = np.sqrt(m * k) / d0

    def equations(self, t: float, y: list[float], omega_f: float,
                  delta_phi: float) -> list[float]:
        """Bewegungsgleichung für solve_ivp."""
        x, v = y

        # Momentane Energie
        E = 0.5 * self.m * v**2 + 0.5 * self.k * x**2

        # Energieabhängige Dämpfung
        d = self.d0 * (1.0 + self.alpha_d * E)

        # RFT-Kopplungseffizienz
        eps = coupling_efficiency(delta_phi)

        # Kräfte
        F_drive = self.F0 * eps * np.cos(omega_f * t)
        F_spring = -self.k * x - self.beta * x**3
        F_damp = -d * v

        a = (F_drive + F_spring + F_damp) / self.m
        return [v, a]

    def simulate(self, omega_f: float, delta_phi: float, T: float = 100.0,
                 dt: float = 0.005) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Simuliert das System. Gibt t, x, v zurück."""
        t_eval = np.arange(0, T, dt)
        sol = solve_ivp(
            self.equations, [0, T], [0.0, 0.0],
            args=(omega_f, delta_phi),
            method='RK45', t_eval=t_eval,
            max_step=dt, rtol=1e-8, atol=1e-10
        )
        return sol.t, sol.y[0], sol.y[1]

    def info(self) -> None:
        print(f"  m = {self.m} kg, k = {self.k} N/m, d₀ = {self.d0} N·s/m")
        print(f"  F₀ = {self.F0} N, β = {self.beta}, α_d = {self.alpha_d}")
        print(f"  f₀ = {self.f_0:.4f} Hz, ω₀ = {self.omega_0:.4f} rad/s")
        print(f"  Q = {self.Q_theo:.1f}")


# ============================================================
# 3. Analyse-Funktionen
# ============================================================

def analyze(sys: NonlinearOscillator, t: np.ndarray, x: np.ndarray,
            v: np.ndarray, omega_f: float,
            delta_phi: float) -> dict[str, Any]:
    """Berechnet Energien, Feldarbeit, Kenngrößen."""
    E_kin = 0.5 * sys.m * v**2
    E_pot = 0.5 * sys.k * x**2
    if sys.beta > 0:
        E_pot += 0.25 * sys.beta * x**4
    E_mech = E_kin + E_pot

    eps = coupling_efficiency(delta_phi)
    F_drive = sys.F0 * eps * np.cos(omega_f * t)
    dt = t[1] - t[0]
    W_cum = np.cumsum(F_drive * v) * dt

    n_half = len(t) // 2
    A_stat = np.max(np.abs(x[n_half:]))
    E_stat = np.mean(E_mech[n_half:])

    return {
        'E_kin': E_kin, 'E_pot': E_pot, 'E_mech': E_mech,
        'F_drive': F_drive, 'W_cum': W_cum,
        'A_stat': A_stat, 'E_stat': E_stat,
        'eps': eps, 'n_half': n_half
    }


def phase_scan(sys: NonlinearOscillator, omega_f: float, T: float = 100.0,
               dt: float = 0.005,
               n_phi: int = 25) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Phasenscan: Δφ von 0 bis 2π."""
    phi_vals = np.linspace(0, 2 * PI, n_phi)
    amp = np.zeros(n_phi)
    energy = np.zeros(n_phi)

    for idx, dp in enumerate(phi_vals):
        t, x, v = sys.simulate(omega_f, dp, T=T, dt=dt)
        n_half = len(t) // 2
        E_kin = 0.5 * sys.m * v**2
        E_pot = 0.5 * sys.k * x**2
        if sys.beta > 0:
            E_pot += 0.25 * sys.beta * x**4
        amp[idx] = np.max(np.abs(x[n_half:]))
        energy[idx] = np.mean((E_kin + E_pot)[n_half:])

    return phi_vals, amp, energy


def duffing_scan(sys: NonlinearOscillator, omega_f: float,
                 delta_phi: float = 0.0, T: float = 100.0,
                 dt: float = 0.005) -> list[dict[str, Any]]:
    """Scannt β von 0 bis 50, zeigt Nichtlinearitäts-Effekt."""
    betas = [0.0, 1.0, 5.0, 20.0, 50.0]
    results = []

    for b in betas:
        sys_b = NonlinearOscillator(
            m=sys.m, k=sys.k, d0=sys.d0, F0=sys.F0,
            beta=b, alpha_d=sys.alpha_d
        )
        t, x, v = sys_b.simulate(omega_f, delta_phi, T=T, dt=dt)
        n_half = len(t) // 2
        E_kin = 0.5 * sys.m * v**2
        E_pot = 0.5 * sys.k * x**2
        if b > 0:
            E_pot += 0.25 * b * x**4

        # Regime-Erkennung via FFT
        x_stat = x[n_half:]
        n_fft = len(x_stat)
        window = np.hamming(n_fft)
        fft_vals = np.abs(np.fft.rfft(x_stat * window))
        n_sig = np.sum(fft_vals > 0.01 * np.max(fft_vals))
        if n_sig > 100:
            regime = "Chaotisch"
        elif n_sig > 20:
            regime = "Quasiperiodisch"
        else:
            regime = "Periodisch"

        results.append({
            'beta': b, 't': t, 'x': x, 'v': v,
            'A_stat': np.max(np.abs(x[n_half:])),
            'E_stat': np.mean((E_kin + E_pot)[n_half:]),
            'regime': regime, 'n_half': n_half
        })

    return results


# ============================================================
# 4. Plots (Matplotlib, direkt via python)
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def plot_main_dashboard(sys: NonlinearOscillator, t: np.ndarray,
                        x: np.ndarray, v: np.ndarray,
                        res: dict[str, Any], omega_f: float,
                        delta_phi: float, output_dir: str) -> None:
    """Plot 1: 6-Panel-Dashboard."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    eps = res['eps']
    n_half = res['n_half']
    dt = t[1] - t[0]
    f_0 = sys.f_0

    fig.suptitle(
        f'Nichtlineare Resonanzanalyse: ω_f = {omega_f:.2f} rad/s, '
        f'Δφ = {delta_phi:.2f}, ε = {eps:.4f}, β = {sys.beta}',
        fontsize=13, fontweight='bold'
    )

    # 1. Zeitverlauf
    ax = axes[0, 0]
    ax.plot(t, x * 1000, 'b-', linewidth=0.3)
    ax.set_xlabel('Zeit [s]')
    ax.set_ylabel('x [mm]')
    ax.set_title(f'Zeitverlauf — A_stat = {res["A_stat"]*1000:.1f} mm')
    ax.grid(True, alpha=0.3)

    # 2. Phasenraum (stationär)
    ax = axes[0, 1]
    ax.plot(x[n_half:] * 1000, v[n_half:] * 1000,
            'b-', linewidth=0.1, alpha=0.5)
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('v [mm/s]')
    ax.set_title('Phasenraum (stationär)')
    ax.grid(True, alpha=0.3)

    # 3. Poincaré-Schnitt
    ax = axes[0, 2]
    if omega_f > 0:
        poincare_idx = []
        for i in range(n_half, len(t)):
            phase = (omega_f * t[i]) % (2 * PI)
            if abs(phase) < omega_f * dt * 1.5:
                poincare_idx.append(i)
        if poincare_idx:
            pi_arr = np.array(poincare_idx)
            ax.plot(x[pi_arr] * 1000, v[pi_arr] * 1000,
                    'k.', markersize=3)
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('v [mm/s]')
    ax.set_title('Poincaré-Schnitt')
    ax.grid(True, alpha=0.3)

    # 4. FFT (stationär)
    ax = axes[1, 0]
    x_stat = x[n_half:]
    n_fft = len(x_stat)
    window = np.hamming(n_fft)
    fft_vals = np.abs(np.fft.rfft(x_stat * window))
    freq_vals = np.fft.rfftfreq(n_fft, dt)
    ax.semilogy(freq_vals, fft_vals, 'b-', linewidth=0.5)
    ax.axvline(f_0, color='r', ls=':', alpha=0.7,
               label=f'f₀ = {f_0:.2f} Hz')
    ax.axvline(omega_f / (2 * PI), color='orange', ls='--',
               alpha=0.7, label=f'f_drive = {omega_f/(2*PI):.2f} Hz')
    ax.set_xlabel('Frequenz [Hz]')
    ax.set_ylabel('Amplitude (log)')
    ax.set_title('Frequenzspektrum')
    ax.set_xlim(0, min(5 * f_0, freq_vals[-1]))
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # 5. Spektrogramm
    ax = axes[1, 1]
    nperseg = min(1024, len(x) // 4)
    if nperseg > 16:
        f_spec, t_spec, Sxx = spectrogram(
            x, fs=1/dt, nperseg=nperseg, noverlap=nperseg//2
        )
        pcm = ax.pcolormesh(
            t_spec, f_spec, 10 * np.log10(Sxx + 1e-20),
            shading='gouraud', cmap='inferno'
        )
        ax.set_ylim(0, min(5 * f_0, f_spec[-1]))
        fig.colorbar(pcm, ax=ax, label='dB')
    ax.set_xlabel('Zeit [s]')
    ax.set_ylabel('Frequenz [Hz]')
    ax.set_title('Spektrogramm (STFT)')

    # 6. Energieverlauf
    ax = axes[1, 2]
    ax.plot(t, res['E_mech'] * 1e6, 'k-', linewidth=0.5, label='E_mech')
    ax.plot(t, res['E_kin'] * 1e6, 'r-', linewidth=0.3, alpha=0.4,
            label='E_kin')
    ax.plot(t, res['E_pot'] * 1e6, 'b-', linewidth=0.3, alpha=0.4,
            label='E_pot')
    ax.plot(t, res['W_cum'] * 1e6, 'g-', linewidth=1,
            label='W_feld (kum.)')
    ax.set_xlabel('Zeit [s]')
    ax.set_ylabel('Energie [µJ]')
    ax.set_title('Energieverlauf')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'nichtlinear_dashboard.png'),
                dpi=150)
    plt.close()
    print("  → nichtlinear_dashboard.png")


def plot_phase_scan(sys: NonlinearOscillator, phis: np.ndarray,
                    amp: np.ndarray, energy: np.ndarray,
                    output_dir: str) -> float:
    """Plot 2: Phasenscan — RFT-Signatur."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    eps_theo = coupling_efficiency(phis)

    # Amplitude
    ax = axes[0]
    amp_norm = amp / np.max(amp) if np.max(amp) > 0 else amp
    eps_norm = eps_theo / np.max(eps_theo)
    ax.plot(phis / PI, amp_norm, 'b-', linewidth=2, label='Simulation')
    ax.plot(phis / PI, eps_norm, 'r--', linewidth=1.5,
            label='Theorie: cos²(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Normierte Amplitude')
    ax.set_title('Amplitude vs. Δφ')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # Energie
    ax = axes[1]
    en_norm = energy / np.max(energy) if np.max(energy) > 0 else energy
    eps_sq = eps_theo**2
    eps_sq_norm = eps_sq / np.max(eps_sq)
    ax.plot(phis / PI, en_norm, 'g-', linewidth=2, label='Simulation')
    ax.plot(phis / PI, eps_sq_norm, 'r--', linewidth=1.5,
            label='Theorie: cos⁴(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Normierte Energie')
    ax.set_title('⟨E_mech⟩ vs. Δφ')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # Verhältnis
    ax = axes[2]
    mean_ink = np.mean(energy)
    ratio = energy / mean_ink if mean_ink > 0 else np.ones_like(energy)
    ax.plot(phis / PI, ratio, 'b-', linewidth=2)
    ax.axhline(2.0, color='red', ls=':', label='RFT: Ratio ≈ 2.0')
    ax.axhline(1.0, color='gray', ls='--', label='Inkohärent: 1.0')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('E(Δφ) / ⟨E⟩_ink')
    ax.set_title('RFT-Signatur: Kohärent vs. Inkohärent')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Nichtlineare Resonanzanalyse: Phasenscan '
        '(RFT: ε = cos²(Δφ/2), κ = 1)',
        fontsize=12, fontweight='bold'
    )
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'nichtlinear_phasenscan.png'),
                dpi=150)
    plt.close()
    print("  → nichtlinear_phasenscan.png")

    return mean_ink


def plot_duffing_comparison(results: list[dict[str, Any]],
                           sys: NonlinearOscillator,
                           output_dir: str) -> None:
    """Plot 3: Duffing-Nichtlinearität — β-Scan."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    colors = ['blue', 'green', 'orange', 'red', 'purple']

    # Phasenräume
    ax = axes[0]
    for r, c in zip(results, colors):
        n_half = r['n_half']
        ax.plot(r['x'][n_half:] * 1000, r['v'][n_half:] * 1000,
                color=c, linewidth=0.1, alpha=0.4,
                label=f"β={r['beta']}")
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('v [mm/s]')
    ax.set_title('Phasenraum vs. Duffing-Stärke β')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Zeitverläufe (letzten 20%)
    ax = axes[1]
    for r, c in zip(results, colors):
        n_90 = int(0.9 * len(r['t']))
        ax.plot(r['t'][n_90:], r['x'][n_90:] * 1000,
                color=c, linewidth=0.5, label=f"β={r['beta']}")
    ax.set_xlabel('Zeit [s]')
    ax.set_ylabel('x [mm]')
    ax.set_title('Stationäres Zeitsignal')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Ergebnistabelle als Plot
    ax = axes[2]
    ax.axis('off')
    table_data = [['β', 'A_stat [mm]', 'E_stat [µJ]', 'Regime']]
    for r in results:
        table_data.append([
            f"{r['beta']:.1f}",
            f"{r['A_stat']*1000:.1f}",
            f"{r['E_stat']*1e6:.1f}",
            r['regime']
        ])
    table = ax.table(cellText=table_data[1:], colLabels=table_data[0],
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)
    ax.set_title('Ergebnisse Duffing-Scan', fontsize=11, pad=20)

    fig.suptitle(
        f'Nichtlineare Resonanzanalyse: Duffing-Scan '
        f'(Δφ = 0, ω_f = ω₀)',
        fontsize=12, fontweight='bold'
    )
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'nichtlinear_duffing.png'),
                dpi=150)
    plt.close()
    print("  → nichtlinear_duffing.png")


def plot_damping_energy(sys: NonlinearOscillator,
                       output_dir: str) -> None:
    """Plot 4: Energieabhängige Dämpfung — α_d-Scan."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    alphas = [0.0, 0.01, 0.1, 0.5, 1.0]
    colors = ['blue', 'green', 'orange', 'red', 'purple']

    omega_f = sys.omega_0
    T = 100.0
    dt = 0.005

    for alpha, c in zip(alphas, colors):
        sys_a = NonlinearOscillator(
            m=sys.m, k=sys.k, d0=sys.d0, F0=sys.F0,
            beta=sys.beta, alpha_d=alpha
        )
        t, x, v = sys_a.simulate(omega_f, 0.0, T=T, dt=dt)
        n_half = len(t) // 2

        axes[0].plot(t, x * 1000, color=c, linewidth=0.3,
                     label=f'α_d = {alpha}')

        E_kin = 0.5 * sys.m * v**2
        E_pot = 0.5 * sys.k * x**2
        axes[1].plot(t, (E_kin + E_pot) * 1e6, color=c, linewidth=0.5,
                     label=f'α_d = {alpha}')

    axes[0].set_xlabel('Zeit [s]')
    axes[0].set_ylabel('x [mm]')
    axes[0].set_title('Zeitverlauf vs. Energiedämpfung α_d')
    axes[0].legend(fontsize=7)
    axes[0].grid(True, alpha=0.3)

    axes[1].set_xlabel('Zeit [s]')
    axes[1].set_ylabel('E_mech [µJ]')
    axes[1].set_title('Mechanische Energie vs. α_d')
    axes[1].legend(fontsize=7)
    axes[1].grid(True, alpha=0.3)

    fig.suptitle(
        'Nichtlineare Resonanzanalyse: Energieabhängige Dämpfung',
        fontsize=12, fontweight='bold'
    )
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'nichtlinear_daempfung.png'),
                dpi=150)
    plt.close()
    print("  → nichtlinear_daempfung.png")


# ============================================================
# 5. Hauptprogramm (python nichtlineare_resonanzanalyse.py)
# ============================================================

def main() -> None:
    print("=" * 60)
    print("NICHTLINEARE RESONANZANALYSE")
    print("Resonanzfeldtheorie: E = π · ε(Δφ) · ℏ · f")
    print("ε(Δφ) = cos²(Δφ/2), κ = 1 (parameterfrei)")
    print("=" * 60)

    output_dir = "figures"
    ensure_dir(output_dir)

    # --- System (linear als Baseline) ---
    sys_lin = NonlinearOscillator(
        m=0.1, k=10.0, d0=0.05, F0=0.1,
        beta=0.0, alpha_d=0.0
    )
    print("\nSystem (linear):")
    sys_lin.info()

    omega_f = sys_lin.omega_0  # Resonanz
    delta_phi = 0.0            # Maximale Kopplung
    T = 100.0
    dt = 0.005

    # --- Experiment 1: Dashboard (linear, Resonanz) ---
    print("\n=== Experiment 1: Dashboard (linear, Δφ = 0) ===")
    t, x, v = sys_lin.simulate(omega_f, delta_phi, T=T, dt=dt)
    res = analyze(sys_lin, t, x, v, omega_f, delta_phi)
    print(f"  A_stat = {res['A_stat']*1000:.1f} mm")
    print(f"  ⟨E_mech⟩ = {res['E_stat']*1e6:.1f} µJ")
    plot_main_dashboard(sys_lin, t, x, v, res, omega_f, delta_phi,
                        output_dir)

    # --- Experiment 2: Phasenscan ---
    print("\n=== Experiment 2: Phasenscan (25 Punkte) ===")
    phis, amp, energy = phase_scan(sys_lin, omega_f, T=T, dt=dt, n_phi=25)
    mean_ink = plot_phase_scan(sys_lin, phis, amp, energy, output_dir)

    # Ergebnisse
    print(f"  Δφ = 0:   A = {amp[0]*1000:.2f} mm, "
          f"E = {energy[0]*1e6:.1f} µJ")
    print(f"  Δφ = π/2: A = {amp[len(phis)//4]*1000:.2f} mm, "
          f"E = {energy[len(phis)//4]*1e6:.1f} µJ")
    print(f"  Δφ = π:   A = {amp[len(phis)//2]*1000:.2f} mm, "
          f"E = {energy[len(phis)//2]*1e6:.1f} µJ")
    if mean_ink > 0:
        ratio = energy[0] / mean_ink
        print(f"\n  RFT-Signatur:")
        print(f"    E(Δφ=0) / ⟨E⟩_ink = {ratio:.4f}")
        print(f"    Theorie:              "
              f"{1.0 / np.mean(coupling_efficiency(phis)**2):.4f}")

    # --- Experiment 3: Duffing-Scan ---
    print("\n=== Experiment 3: Duffing-Nichtlinearität ===")
    sys_nl = NonlinearOscillator(
        m=0.1, k=10.0, d0=0.05, F0=0.1,
        beta=5.0, alpha_d=0.0
    )
    results = duffing_scan(sys_nl, omega_f, delta_phi=0.0, T=T, dt=dt)
    for r in results:
        print(f"  β = {r['beta']:5.1f}  →  A = {r['A_stat']*1000:7.1f} mm, "
              f"E = {r['E_stat']*1e6:10.1f} µJ, {r['regime']}")
    plot_duffing_comparison(results, sys_nl, output_dir)

    # --- Experiment 4: Energieabhängige Dämpfung ---
    print("\n=== Experiment 4: Energieabhängige Dämpfung ===")
    plot_damping_energy(sys_lin, output_dir)
    print("  α_d = 0.0 → 1.0: Sättigung der Amplitude bei hoher Energie")

    # --- Zusammenfassung ---
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("=" * 60)
    ratio_str = f"{ratio:.4f}" if mean_ink > 0 else "N/A"
    print(f"""
  Nichtlineare Resonanzanalyse

  Grundformel:    E = π · ε(Δφ) · ℏ · f
  Kopplung:       ε(Δφ) = cos²(Δφ/2), κ = 1

  Lineares System (β = 0):
    f₀ = {sys_lin.f_0:.4f} Hz, Q = {sys_lin.Q_theo:.1f}
    A_stat = {res['A_stat']*1000:.1f} mm bei Resonanz
    RFT-Signatur: E_koh / ⟨E⟩_ink = {ratio_str}
    Amplitude folgt cos²(Δφ/2), Energie folgt cos⁴(Δφ/2)

  Nichtlinearität:
    β > 0 (Duffing): Frequenzverschiebung, Chaosübergang
    α_d > 0: Amplitudensättigung durch Energiedämpfung
    RFT-Kopplung ε(Δφ) bleibt auf allen Niveaus gültig

  4 Plots gespeichert unter: {output_dir}/
    nichtlinear_dashboard.png    (6-Panel: Zeit, Phase, Poincaré, FFT, STFT, Energie)
    nichtlinear_phasenscan.png   (RFT-Signatur: cos², cos⁴, koh/ink)
    nichtlinear_duffing.png      (β-Scan: Phasenraum, Zeitverlauf, Ergebnistabelle)
    nichtlinear_daempfung.png    (α_d-Scan: Sättigung bei hoher Energie)
""")
    print("Fertig.")


# ============================================================
# 6. Streamlit-Modus (optional)
# ============================================================

def run_streamlit() -> None:
    """Interaktive Streamlit-App (falls installiert)."""
    import streamlit as st

    st.set_page_config(
        page_title="Nichtlineare Resonanzanalyse (RFT)",
        layout="wide"
    )
    st.title("⚡ Nichtlineare Resonanzanalyse")
    st.markdown(
        "**Resonanzfeldtheorie:** E = π · ε(Δφ) · ℏ · f, "
        "ε(Δφ) = cos²(Δφ/2), κ = 1"
    )

    # Sidebar
    st.sidebar.header("🔧 System")
    m = st.sidebar.number_input("m [kg]", 0.01, 10.0, 0.1, step=0.01)
    k = st.sidebar.number_input("k [N/m]", 0.1, 100.0, 10.0, step=0.1)
    d0 = st.sidebar.slider("d₀", 0.001, 2.0, 0.05, step=0.001)
    F0 = st.sidebar.slider("F₀ [N]", 0.001, 5.0, 0.1, step=0.001)

    omega_0 = np.sqrt(k / m)
    f_0 = omega_0 / (2 * PI)

    st.sidebar.header("🌊 Anregung")
    omega_f = st.sidebar.slider("ω_f", 0.1, 50.0, float(omega_0), step=0.01)
    delta_phi = st.sidebar.slider("Δφ [rad]", 0.0, 2*PI, 0.0, step=0.01)

    st.sidebar.header("🔀 Nichtlinear")
    beta = st.sidebar.slider("β (Duffing)", 0.0, 50.0, 0.0, step=0.1)
    alpha_d = st.sidebar.slider("α_d (Energiedämpfung)", 0.0, 1.0, 0.0,
                                step=0.01)
    T = st.sidebar.slider("T [s]", 10, 500, 100, step=5)

    eps = coupling_efficiency(delta_phi)
    st.sidebar.markdown(f"**ε = {eps:.4f}**, f₀ = {f_0:.3f} Hz, "
                        f"Q = {np.sqrt(m*k)/d0:.0f}")

    if st.button("▶️ Simulation starten", type="primary"):
        sys = NonlinearOscillator(m=m, k=k, d0=d0, F0=F0,
                                   beta=beta, alpha_d=alpha_d)
        with st.spinner("Simulation..."):
            t, x, v = sys.simulate(omega_f, delta_phi, T=T, dt=0.005)
            res = analyze(sys, t, x, v, omega_f, delta_phi)

        # Dashboard
        n_half = res['n_half']
        dt = t[1] - t[0]
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))

        axes[0, 0].plot(t, x*1000, 'b-', lw=0.3)
        axes[0, 0].set_title(f"x(t) — A={res['A_stat']*1000:.1f} mm")
        axes[0, 0].set_xlabel('t [s]')
        axes[0, 0].set_ylabel('x [mm]')

        axes[0, 1].plot(x[n_half:]*1000, v[n_half:]*1000, 'b-', lw=0.1)
        axes[0, 1].set_title('Phasenraum')

        # Poincaré
        if omega_f > 0:
            pi_idx = [i for i in range(n_half, len(t))
                      if abs((omega_f*t[i]) % (2*PI)) < omega_f*dt*1.5]
            if pi_idx:
                pa = np.array(pi_idx)
                axes[0, 2].plot(x[pa]*1000, v[pa]*1000, 'k.', ms=2)
        axes[0, 2].set_title('Poincaré')

        x_s = x[n_half:]
        fft_v = np.abs(np.fft.rfft(x_s * np.hamming(len(x_s))))
        freq_v = np.fft.rfftfreq(len(x_s), dt)
        axes[1, 0].semilogy(freq_v, fft_v, 'b-', lw=0.5)
        axes[1, 0].set_xlim(0, 5*f_0)
        axes[1, 0].set_title('FFT')

        nperseg = min(1024, len(x)//4)
        if nperseg > 16:
            fs, ts, Sxx = spectrogram(x, fs=1/dt, nperseg=nperseg,
                                       noverlap=nperseg//2)
            axes[1, 1].pcolormesh(ts, fs, 10*np.log10(Sxx+1e-20),
                                   shading='gouraud', cmap='inferno')
            axes[1, 1].set_ylim(0, 5*f_0)
        axes[1, 1].set_title('Spektrogramm')

        axes[1, 2].plot(t, res['E_mech']*1e6, 'k-', lw=0.5)
        axes[1, 2].plot(t, res['W_cum']*1e6, 'g-', lw=1)
        axes[1, 2].set_title('Energie')

        plt.tight_layout()
        st.pyplot(fig)

        # Phasenscan
        st.markdown("### Phasenscan")
        with st.spinner("Phasenscan..."):
            phis, amp_p, en_p = phase_scan(sys, omega_f, T=T, n_phi=25)

        fig2, ax2 = plt.subplots(1, 3, figsize=(16, 4.5))
        eps_t = coupling_efficiency(phis)
        a_n = amp_p/np.max(amp_p) if np.max(amp_p) > 0 else amp_p
        ax2[0].plot(phis/PI, a_n, 'b-', lw=2, label='Sim')
        ax2[0].plot(phis/PI, eps_t, 'r--', lw=1.5, label='cos²')
        ax2[0].legend()
        ax2[0].set_title('Amplitude vs Δφ')

        e_n = en_p/np.max(en_p) if np.max(en_p) > 0 else en_p
        ax2[1].plot(phis/PI, e_n, 'g-', lw=2, label='Sim')
        ax2[1].plot(phis/PI, eps_t**2/np.max(eps_t**2), 'r--', lw=1.5,
                    label='cos⁴')
        ax2[1].legend()
        ax2[1].set_title('Energie vs Δφ')

        mi = np.mean(en_p)
        r = en_p/mi if mi > 0 else np.ones_like(en_p)
        ax2[2].plot(phis/PI, r, 'b-', lw=2)
        ax2[2].axhline(2.0, color='r', ls=':')
        ax2[2].axhline(1.0, color='gray', ls='--')
        ax2[2].set_title('RFT-Signatur')

        plt.tight_layout()
        st.pyplot(fig2)

        if mi > 0:
            st.success(f"E(Δφ=0)/⟨E⟩ = **{en_p[0]/mi:.4f}**")
    else:
        st.info("Klicke ▶️ Simulation starten")


# ============================================================
# 7. Entry Point
# ============================================================

if __name__ == "__main__":
    # Prüfe ob Streamlit die App gestartet hat
    try:
        import streamlit as st
        # Wenn Streamlit den Prozess steuert, gibt es einen runtime
        if hasattr(st, 'runtime') and st.runtime.exists():
            run_streamlit()
        else:
            # Streamlit installiert, aber via `python` gestartet
            main()
    except ImportError:
        # Kein Streamlit → reiner Matplotlib-Modus
        main()
    except Exception:
        # Fallback
        main()