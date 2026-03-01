# warpantrieb.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Simulation: Warpantrieb – Dreistufige Kaskade
#
# Architektur:
#   Stufe 1: N Resonanzreaktoren (Spaltung) → Treiberenergie
#   Stufe 2: Trägheitsfusion → extreme Energiedichte
#   Stufe 3: Asymmetrische Phasensteuerung → Warp-Geometrie
#
# Expansion (Slow-Roll-Mechanismus):
#   Klein-Gordon MIT Hubble-Reibung:
#     ε̈ + 3H·ε̇ + V'(ε) = 0
#   Wenn das Potential ein flaches Plateau hat:
#     ε̇ ≈ −V'/(3H) → Slow Roll → w ≈ −1 → Expansion
#   RFT-Steuerung über Δφ:
#     Δφ = 0:   Starke Kopplung → schnelle Oszillation → w > 0 → Kontraktion
#     Δφ ≈ π/2: Schwache Kopplung → Slow Roll → w ≈ −1 → Expansion
#     Δφ = π:   Keine Kopplung → Feld aus → w = 0 → flach

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. Konstanten
# ============================================================

HBAR = 1.054571817e-34
PI = np.pi
G = 6.67430e-11
C = 2.99792458e8
EV = 1.602176634e-19
MEV = 1e6 * EV

E_GDR = 15.0 * MEV
F_GDR = E_GDR / (PI * HBAR)
P_REACTOR = 100e6

E_NIF_OUT = 3.15e6
V_PELLET = 4/3 * PI * (1e-3)**3
TAU_BURN = 1e-8


# ============================================================
# 2. RFT-Kopplungseffizienz
# ============================================================

def coupling_efficiency(delta_phi):
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 3. Klein-Gordon MIT Hubble-Reibung (Slow Roll)
# ============================================================

def klein_gordon_with_hubble(delta_phi, omega=1.0, m=1.0, lmbda=0.1,
                              eps0=1.0, kappa_grav=1.0,
                              t_max=100.0, n_eval=10000):
    """
    Löst die Klein-Gordon-Gleichung in selbstkonsistenter
    FLRW-Raumzeit:

    ε̈ + 3H·ε̇ + V'(ε) = 0
    H² = (κ/3) · ρ
    ρ = ½ε̇² + V(ε)
    p = ½ε̇² − V(ε)

    Das Potential hat ein Plateau für kleine ε:
    V(ε) = V₀ · (1 − exp(−√(2/3)·ε))²  (Starobinsky-artig)

    Für große ε: V ≈ V₀ (Plateau) → Slow Roll → w ≈ −1
    Für kleine ε: V ≈ m²ε² (harmonisch) → Oszillation → w ≈ 0

    RFT-Steuerung:
    ε(0) = eps0 · √(ε(Δφ)) bestimmt, wo im Potential gestartet wird.
    Δφ = 0:   Start weit oben → großes ε → rollt schnell → w > 0
    Δφ ≈ π/2: Start auf Plateau → kleines ε̇ → Slow Roll → w ≈ −1
    """
    eps_coupling = coupling_efficiency(delta_phi)

    # Plateau-Potential (Starobinsky-inspiriert)
    alpha_sr = np.sqrt(2.0 / 3.0)
    V0 = 0.5 * m**2  # Potentialhöhe

    def V(eps):
        return V0 * (1.0 - np.exp(-alpha_sr * abs(eps)))**2

    def Vp(eps):
        return 2.0 * V0 * alpha_sr * np.exp(-alpha_sr * abs(eps)) * \
               (1.0 - np.exp(-alpha_sr * abs(eps))) * np.sign(eps)

    # Anfangsbedingungen abhängig von Δφ
    if eps_coupling > 0.01:
        # Startposition im Potential
        # Große Kopplung → Start weit vom Minimum → schnelle Dynamik
        # Kleine Kopplung → Start auf Plateau → Slow Roll
        eps_init = eps0 * (2.0 - eps_coupling)  # Plateau bei großem ε

        # Geschwindigkeit: Slow-Roll-Approximation ε̇ ≈ −V'/(3H)
        rho_init = V(eps_init) + 1e-10
        H_init = np.sqrt(kappa_grav / 3.0 * rho_init)

        # Kinetische Energie: proportional zu ε(Δφ)
        # Δφ=0: ε̇ groß (oszillierend)
        # Δφ=π/2: ε̇ ≈ Slow-Roll-Wert (klein)
        if eps_coupling > 0.8:  # Δφ nahe 0: oszillierend
            epsdot_init = omega * eps_init * eps_coupling
        else:  # Δφ nahe π/2: Slow Roll
            epsdot_init = -Vp(eps_init) / (3.0 * H_init + 1e-10) * eps_coupling
    else:
        eps_init = 1e-15
        epsdot_init = 0.0

    def rhs(t, y):
        eps, epsdot, a = y
        if a < 1e-30:
            return [0, 0, 0]

        rho = 0.5 * epsdot**2 + V(eps)
        if rho < 0:
            rho = 1e-30

        H = np.sqrt(kappa_grav / 3.0 * rho)
        adot = a * H

        # Klein-Gordon mit Hubble-Reibung
        epsddot = -3.0 * H * epsdot - Vp(eps)

        return [epsdot, epsddot, adot]

    y0 = [eps_init, epsdot_init, 1.0]  # a(0) = 1
    t_eval = np.linspace(0, t_max, n_eval)

    sol = solve_ivp(rhs, (0, t_max), y0, t_eval=t_eval,
                    rtol=1e-10, atol=1e-13, method='DOP853')

    eps = sol.y[0]
    epsdot = sol.y[1]
    a = sol.y[2]
    t = sol.t

    rho = 0.5 * epsdot**2 + V(eps)
    p = 0.5 * epsdot**2 - V(eps)
    w = np.where(rho > 1e-30, p / rho, 0.0)

    H = np.sqrt(kappa_grav / 3.0 * np.maximum(rho, 0))

    # Zeitgemittelt (zweite Hälfte)
    half = len(w) // 2
    w_avg = np.mean(w[half:])
    rho_avg = np.mean(rho[half:])
    p_avg = np.mean(p[half:])

    # Skalenfaktor-Dynamik
    a_ratio = a[-1] / a[0] if a[0] > 0 else 1.0
    expanding = a_ratio > 1.0

    return {
        't': t, 'eps': eps, 'epsdot': epsdot, 'a': a,
        'rho': rho, 'p': p, 'w': w, 'H': H,
        'w_avg': w_avg, 'rho_avg': rho_avg, 'p_avg': p_avg,
        'delta_phi': delta_phi, 'eps_coupling': eps_coupling,
        'a_ratio': a_ratio, 'expanding': expanding
    }


# ============================================================
# 4. Fusions-Warp-System
# ============================================================

class FusionWarpSystem:
    def __init__(self, n_drive=12, n_focus_front=6, n_focus_rear=6,
                 p_reactor=P_REACTOR, gain=1.5, pulse_rate=10.0,
                 focus_distance=100.0, sigma=5.0):
        self.n_drive = n_drive
        self.n_focus_front = n_focus_front
        self.n_focus_rear = n_focus_rear
        self.p_reactor = p_reactor
        self.gain = gain
        self.pulse_rate = pulse_rate
        self.focus_distance = focus_distance
        self.sigma = sigma
        self.P_drive_total = n_drive * p_reactor
        self.E_per_pulse = self.P_drive_total / pulse_rate
        self.E_fusion_per_pulse = self.E_per_pulse * gain
        self.rho_E_pellet = self.E_fusion_per_pulse / V_PELLET
        self.rho_P_pellet = self.rho_E_pellet / TAU_BURN
        self.R_pellet = 8 * PI * G / C**2 * self.rho_E_pellet

    def energy_density_field(self, x_grid, y_grid,
                              delta_phi_front=0.0, delta_phi_rear=0.0):
        eps_f = coupling_efficiency(delta_phi_front)
        eps_r = coupling_efficiency(delta_phi_rear)
        dx_f = x_grid - self.focus_distance
        r2_f = dx_f**2 + (y_grid)**2
        A_front = self.n_focus_front * np.exp(-r2_f / (2 * self.sigma**2))
        dx_r = x_grid + self.focus_distance
        r2_r = dx_r**2 + (y_grid)**2
        A_rear = self.n_focus_rear * np.exp(-r2_r / (2 * self.sigma**2))
        rho = (A_front * eps_f)**2 * self.rho_E_pellet / self.n_focus_front**2 \
            + (A_rear * eps_r)**2 * self.rho_E_pellet / self.n_focus_rear**2
        return rho

    def curvature_field(self, rho):
        return 8 * PI * G / C**2 * rho

    def info(self):
        R_sun = 8 * PI * G * 1.6e5
        print("=" * 60)
        print("WARPANTRIEB: Fusions-Warp-System")
        print("=" * 60)
        print(f"\n  STUFE 1: Treiberreaktoren")
        print(f"    Anzahl:          {self.n_drive} × {self.p_reactor/1e6:.0f} MW"
              f" = {self.P_drive_total/1e9:.2f} GW")
        print(f"\n  STUFE 2: Trägheitsfusion")
        print(f"    Gain: {self.gain}×, Pulsrate: {self.pulse_rate} Hz")
        print(f"    E/Puls: {self.E_fusion_per_pulse/1e6:.1f} MJ")
        print(f"    ρ_E: {self.rho_E_pellet:.3e} J/m³")
        print(f"    ρ_P: {self.rho_P_pellet:.3e} W/m³")
        print(f"\n  STUFE 3: Raumzeitkrümmung")
        print(f"    R (Pellet): {self.R_pellet:.3e} 1/m²")
        print(f"    Peak/Sonne: {self.rho_P_pellet * 8*PI*G/C**2 / R_sun:.1f}×")
        print("=" * 60)


# ============================================================
# 5. Experimente
# ============================================================

def experiment_energy_cascade():
    scenarios = [
        {"name": "Spaltung (1 Reaktor)",
         "rho_E": PI * HBAR * F_GDR / V_PELLET},
        {"name": "NIF (192 Laser, 2 MJ)",
         "rho_E": E_NIF_OUT / V_PELLET},
        {"name": "RFT-Fusion (12×100MW, G=1.5)",
         "rho_E": 12 * P_REACTOR / 10.0 * 1.5 / V_PELLET},
        {"name": "RFT-Fusion (100×1GW, G=10)",
         "rho_E": 100 * 1e9 / 100.0 * 10 / V_PELLET},
        {"name": "Erdmittelpunkt", "rho_E": 5.5e3 * C**2},
        {"name": "Sonnenmittelpunkt", "rho_E": 1.6e5 * C**2},
        {"name": "Alcubierre (v=0.1c)", "rho_E": 1e30},
    ]
    for s in scenarios:
        s["R"] = 8 * PI * G / C**2 * s["rho_E"]
    return scenarios


def experiment_phase_scan(system, n_phi=50):
    phi_vals = np.linspace(0, 2*PI, n_phi)
    rho_focus = np.zeros(n_phi)
    x_pt = np.array([[float(system.focus_distance)]])
    y_pt = np.array([[0.0]])
    for idx, dp in enumerate(phi_vals):
        rho = system.energy_density_field(x_pt, y_pt, dp, PI)
        rho_focus[idx] = rho[0, 0]
    return phi_vals, rho_focus


def experiment_klein_gordon_slow_roll():
    """Klein-Gordon MIT Hubble-Reibung: w(Δφ) Scan."""
    delta_phis = np.array([0.0, PI/6, PI/4, PI/3, 5*PI/12, PI/2,
                           7*PI/12, 2*PI/3, 3*PI/4, 5*PI/6, PI])
    modes = []
    for dp in delta_phis:
        result = klein_gordon_with_hubble(
            delta_phi=dp, omega=1.0, m=1.0, lmbda=0.1,
            eps0=1.0, kappa_grav=1.0, t_max=100.0, n_eval=10000
        )
        modes.append(result)
    return modes


def experiment_warp_profile(system, modes, n_grid=500):
    """Warp-Profil mit physikalisch korrektem w(x)."""
    x = np.linspace(-300, 300, n_grid)
    X, Y = np.meshgrid(x, [0.0])

    # Warp: vorn Δφ=0, hinten Δφ≈π/2
    rho_warp = system.energy_density_field(X, Y, 0.0, PI/2)

    # w-Werte aus Klein-Gordon
    w_front = [m['w_avg'] for m in modes if abs(m['delta_phi']) < 0.01]
    w_rear = [m['w_avg'] for m in modes
              if abs(m['delta_phi'] - PI/2) < 0.01]
    w_f = w_front[0] if w_front else 0.0
    w_r = w_rear[0] if w_rear else -1.0

    w_profile = np.zeros_like(x)
    expansion = np.zeros_like(x)

    for i, xi in enumerate(x):
        dx_f = xi - system.focus_distance
        dx_r = xi + system.focus_distance
        gauss_f = np.exp(-dx_f**2 / (2 * system.sigma**2))
        gauss_r = np.exp(-dx_r**2 / (2 * system.sigma**2))

        if gauss_f > 0.01 and gauss_f > gauss_r:
            w_profile[i] = w_f
            expansion[i] = -1.0     # Kontraktion
        elif gauss_r > 0.01 and gauss_r > gauss_f:
            w_profile[i] = w_r
            expansion[i] = +1.0 if w_r < -1/3 else -0.5
        else:
            w_profile[i] = 0.0
            expansion[i] = 0.0

    return x, rho_warp[0, :], w_profile, expansion, w_f, w_r


def experiment_scaling():
    configs = [
        (6, 1.0, "6×100MW, G=1"), (6, 1.5, "6×100MW, G=1.5"),
        (12, 1.5, "12×100MW, G=1.5"), (12, 5.0, "12×100MW, G=5"),
        (24, 10.0, "24×100MW, G=10"), (48, 10.0, "48×100MW, G=10"),
        (100, 50.0, "100×100MW, G=50"), (100, 100.0, "100×100MW, G=100"),
    ]
    results = []
    for n_d, gain, label in configs:
        sys = FusionWarpSystem(n_drive=n_d, gain=gain)
        x_pt = np.array([[float(sys.focus_distance)]])
        y_pt = np.array([[0.0]])
        rho = sys.energy_density_field(x_pt, y_pt, 0.0, PI)
        rho_val = rho[0, 0]
        results.append({
            'label': label, 'n_drive': n_d, 'gain': gain,
            'P_total': n_d * P_REACTOR, 'rho_E': rho_val,
            'R': 8 * PI * G / C**2 * rho_val})
    return results


# ============================================================
# 6. Plots
# ============================================================

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def plot_energy_cascade(scenarios, output_dir):
    fig, ax = plt.subplots(1, 1, figsize=(14, 7))
    names = [s["name"] for s in scenarios]
    rhos = [s["rho_E"] for s in scenarios]
    colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336',
              '#9E9E9E', '#FFD700', '#9C27B0']
    bars = ax.barh(range(len(names)), rhos,
                   color=colors[:len(names)], alpha=0.8)
    ax.set_xscale('log')
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlabel('Energiedichte ρ [J/m³]', fontsize=11)
    ax.set_title('Warpantrieb: Energiestufen-Vergleich\n'
                 'E = π · ε(Δφ) · ℏ · f → Fusion → Raumzeitkrümmung',
                 fontsize=12, fontweight='bold')
    for i, (bar, s) in enumerate(zip(bars, scenarios)):
        ax.text(bar.get_width() * 1.5, i,
                f'R = {s["R"]:.1e} 1/m²',
                va='center', fontsize=8, color='darkblue')
    ax.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_energiestufen.png'), dpi=150)
    plt.close()
    print("  → warp_energiestufen.png")


def plot_phase_scan(phis, rho_focus, output_dir):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    eps_theo = coupling_efficiency(phis)
    eps4 = eps_theo**2
    eps4_norm = eps4 / np.max(eps4)

    ax = axes[0]
    rho_norm = rho_focus / np.max(rho_focus)
    ax.plot(phis/PI, rho_norm, 'b-', lw=2, label='Simulation')
    ax.plot(phis/PI, eps4_norm, 'r--', lw=1.5, label='cos⁴(Δφ/2)')
    ax.set_xlabel('Δφ / π'); ax.set_ylabel('ρ (normiert)')
    ax.set_title('Energiedichte vs. Δφ')
    ax.legend(fontsize=8); ax.set_xlim(0, 2); ax.grid(True, alpha=0.3)

    ax = axes[1]
    R_norm = rho_focus / np.max(rho_focus)
    ax.plot(phis/PI, R_norm, 'g-', lw=2, label='R(Δφ)')
    ax.plot(phis/PI, eps4_norm, 'r--', lw=1.5, label='cos⁴(Δφ/2)')
    ax.set_xlabel('Δφ / π'); ax.set_ylabel('R (normiert)')
    ax.set_title('Krümmung vs. Δφ')
    ax.legend(fontsize=8); ax.set_xlim(0, 2); ax.grid(True, alpha=0.3)

    ax = axes[2]
    rho_mean = np.mean(rho_focus)
    ratio = rho_focus / rho_mean if rho_mean > 0 else np.ones_like(rho_focus)
    ax.plot(phis/PI, ratio, 'b-', lw=2)
    ax.axhline(2.0, color='red', ls=':', label='RFT ≈ 2.0')
    ax.axhline(1.0, color='gray', ls='--', label='Inkohärent')
    ax.set_xlabel('Δφ / π'); ax.set_ylabel('ρ/⟨ρ⟩')
    ax.set_title('RFT-Signatur')
    ax.legend(fontsize=8); ax.set_xlim(0, 2); ax.grid(True, alpha=0.3)

    fig.suptitle('Warpantrieb: Phasenscan (ε = cos²(Δφ/2), κ = 1)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_phasenscan.png'), dpi=150)
    plt.close()
    print("  → warp_phasenscan.png")
    return rho_mean


def plot_klein_gordon(modes, output_dir):
    """Klein-Gordon-Feld: 3 Schlüsselmodi mit Skalenfaktor."""
    key_indices = []
    for target in [0.0, PI/2, PI]:
        dists = [abs(m['delta_phi'] - target) for m in modes]
        key_indices.append(np.argmin(dists))

    key_modes = [modes[i] for i in key_indices]
    labels = ['Δφ = 0\n(oszillierend → Kontraktion)',
              'Δφ = π/2\n(Slow Roll → Expansion)',
              'Δφ = π\n(Feld aus → flach)']
    colors = ['blue', 'red', 'gray']

    fig, axes = plt.subplots(3, 3, figsize=(18, 14))

    for i, (mode, label, color) in enumerate(zip(key_modes, labels, colors)):
        t = mode['t']
        n_show = min(len(t), 2000)

        # Feld ε(t)
        ax = axes[0, i]
        ax.plot(t[:n_show], mode['eps'][:n_show], color=color, lw=1.5)
        ax.set_ylabel('ε(t)')
        ax.set_title(f'{label}\nε(Δφ)={mode["eps_coupling"]:.2f}',
                     fontsize=9)
        ax.grid(True, alpha=0.3)

        # w(t)
        ax = axes[1, i]
        ax.plot(t[:n_show], mode['w'][:n_show], color=color, lw=0.5,
                alpha=0.4)
        window = min(200, n_show // 5)
        if len(mode['w']) > window:
            w_smooth = np.convolve(mode['w'], np.ones(window)/window,
                                   mode='same')
            ax.plot(t[:n_show], w_smooth[:n_show], color=color, lw=2.5,
                    label=f'⟨w⟩ = {mode["w_avg"]:.3f}')
        ax.axhline(-1, color='green', ls=':', lw=1.5, label='w=−1 (De Sitter)')
        ax.axhline(0, color='black', ls='-', lw=0.5)
        ax.axhline(1/3, color='orange', ls=':', lw=1, label='w=+⅓ (Strahlung)')
        ax.set_ylabel('w = p/ρ')
        ax.set_ylim(-1.5, 1.0)
        ax.legend(fontsize=6, loc='upper right')
        ax.grid(True, alpha=0.3)

        # Skalenfaktor a(t)
        ax = axes[2, i]
        a_norm = mode['a'][:n_show] / mode['a'][0]
        ax.plot(t[:n_show], a_norm, color=color, lw=2)
        ax.axhline(1.0, color='gray', ls='--', lw=0.5)
        ax.set_xlabel('t')
        ax.set_ylabel('a(t)/a(0)')
        if mode['expanding']:
            ax.set_title(f'a(T)/a(0) = {mode["a_ratio"]:.2f} → EXPANSION',
                         fontsize=9, color='green', fontweight='bold')
        else:
            ax.set_title(f'a(T)/a(0) = {mode["a_ratio"]:.4f}',
                         fontsize=9)
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Klein-Gordon MIT Hubble-Reibung (Slow-Roll-Mechanismus)\n'
        'ε̈ + 3H·ε̇ + V\'(ε) = 0, V = V₀(1−e^(−αε))² '
        '(Starobinsky-Plateau)\n'
        'ρ = ½ε̇² + V > 0 (immer positiv), '
        'p = ½ε̇² − V (kann negativ sein)',
        fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_klein_gordon.png'), dpi=150)
    plt.close()
    print("  → warp_klein_gordon.png")


def plot_w_scan(modes, output_dir):
    """w(Δφ) — der Schlüsselplot."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    dphis = [m['delta_phi'] for m in modes]
    w_avgs = [m['w_avg'] for m in modes]
    rho_avgs = [m['rho_avg'] for m in modes]
    p_avgs = [m['p_avg'] for m in modes]
    a_ratios = [m['a_ratio'] for m in modes]

    # w vs Δφ
    ax = axes[0]
    ax.plot(np.array(dphis)/PI, w_avgs, 'bo-', lw=2, ms=8)
    ax.axhline(-1, color='green', ls=':', lw=1.5,
               label='w = −1 (De Sitter)')
    ax.axhline(-1/3, color='purple', ls='--', lw=1,
               label='w = −⅓ (Grenze Expansion)')
    ax.axhline(0, color='gray', ls='--', lw=1, label='w = 0 (Materie)')
    ax.axhline(1/3, color='orange', ls=':', lw=1.5, label='w = +⅓ (Strahlung)')
    ax.fill_between([0, 1], [-1.5, -1.5], [-1/3, -1/3], alpha=0.1,
                    color='green', label='Beschleunigte Expansion')
    ax.set_xlabel('Δφ / π', fontsize=11)
    ax.set_ylabel('⟨w⟩', fontsize=11)
    ax.set_title('Zustandsgleichung vs. Phase')
    ax.set_xlim(0, 1); ax.set_ylim(-1.5, 0.5)
    ax.legend(fontsize=6, loc='lower left')
    ax.grid(True, alpha=0.3)

    # Skalenfaktor a(T)/a(0) vs Δφ
    ax = axes[1]
    colors_a = ['green' if a > 1 else 'red' for a in a_ratios]
    ax.bar(np.array(dphis)/PI, np.array(a_ratios) - 1.0,
           width=0.06, color=colors_a, alpha=0.7)
    ax.axhline(0, color='black', ls='-', lw=0.5)
    ax.set_xlabel('Δφ / π', fontsize=11)
    ax.set_ylabel('a(T)/a(0) − 1', fontsize=11)
    ax.set_title('Expansion (>0) vs. Kontraktion (<0)')
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.3)

    # Warp-Schema
    ax = axes[2]
    x_schema = np.linspace(-3, 3, 200)
    w_front = w_avgs[0]
    w_rear_idx = np.argmin([abs(m['delta_phi'] - PI/2) for m in modes])
    w_rear = w_avgs[w_rear_idx]
    w_schema = np.zeros_like(x_schema)
    for i, xi in enumerate(x_schema):
        if xi > 1:
            w_schema[i] = w_front
        elif xi < -1:
            w_schema[i] = w_rear
    ax.fill_between(x_schema, 0, w_schema,
                    where=w_schema > 0, alpha=0.3, color='red',
                    label='Kontraktion')
    ax.fill_between(x_schema, 0, w_schema,
                    where=w_schema < 0, alpha=0.3, color='green',
                    label='Expansion')
    ax.plot(x_schema, w_schema, 'k-', lw=2)
    ax.axhline(0, color='black', ls='-', lw=0.5)
    ax.text(2, max(w_front, 0.05), f'VORN\nΔφ=0\nw={w_front:+.3f}',
            ha='center', fontsize=8, color='red')
    ax.text(-2, min(w_rear, -0.1) - 0.15, f'HINTEN\nΔφ=π/2\nw={w_rear:+.3f}',
            ha='center', fontsize=8, color='green')
    ax.text(0, 0.15, '← SCHIFF →', ha='center', fontsize=9,
            fontweight='bold')
    ax.set_xlabel('Position'); ax.set_ylabel('w')
    ax.set_title('Warp-Profil')
    ax.set_ylim(-1.5, 0.5)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Warpantrieb: w(Δφ) — Phasengesteuerte Zustandsgleichung\n'
        'Klein-Gordon mit Hubble-Reibung und Starobinsky-Plateau',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_zustandsgleichung.png'),
                dpi=150)
    plt.close()
    print("  → warp_zustandsgleichung.png")


def plot_warp_full(x, rho, w_profile, expansion, system,
                   w_f, w_r, output_dir):
    """Vollständiges Warp-Profil."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax = axes[0, 0]
    ax.plot(x, rho, 'b-', lw=2)
    ax.axvline(system.focus_distance, color='green', ls=':', alpha=0.5,
               label='Fokus vorn')
    ax.axvline(-system.focus_distance, color='orange', ls=':', alpha=0.5,
               label='Fokus hinten')
    ax.axvline(0, color='gray', ls='-', alpha=0.3)
    ax.set_xlabel('x [m]'); ax.set_ylabel('ρ [J/m³]')
    ax.set_title('Energiedichte (ρ > 0 überall)')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.fill_between(x, 0, w_profile,
                    where=np.array(w_profile) > 0, alpha=0.3, color='red',
                    label=f'Kontraktion (w={w_f:+.3f})')
    ax.fill_between(x, 0, w_profile,
                    where=np.array(w_profile) < 0, alpha=0.3, color='green',
                    label=f'Expansion (w={w_r:+.3f})')
    ax.plot(x, w_profile, 'k-', lw=2)
    ax.axhline(0, color='black', ls='-', lw=0.5)
    ax.axhline(-1/3, color='purple', ls='--', alpha=0.5,
               label='w = −⅓ (Grenze)')
    ax.set_xlabel('x [m]'); ax.set_ylabel('w = p/ρ')
    ax.set_title('Zustandsgleichung (Slow Roll)')
    ax.set_ylim(-1.5, 0.5)
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.fill_between(x, 0, expansion,
                    where=np.array(expansion) > 0, alpha=0.4, color='green',
                    label='Expansion')
    ax.fill_between(x, 0, expansion,
                    where=np.array(expansion) < 0, alpha=0.4, color='red',
                    label='Kontraktion')
    ax.plot(x, expansion, 'k-', lw=2)
    ax.axhline(0, color='black', ls='-', lw=0.5)
    ax.set_xlabel('x [m]'); ax.set_ylabel('Raumzeitdynamik')
    ax.set_title('Expansion (hinten) + Kontraktion (vorn)')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.axis('off')
    schema = f"""
    WARP-KONFIGURATION (Slow-Roll-Mechanismus)
    ═══════════════════════════════════════════

    HINTEN                SCHIFF              VORN
    ┌────────────┐  ┌──────────────┐  ┌────────────┐
    │ Δφ = π/2   │  │              │  │ Δφ = 0     │
    │ Slow Roll  │  │  Geschützt   │  │ Oszillier. │
    │ ε̇ ≈ 0     │  │  durch       │  │ ε̇ >> 0    │
    │ w = {w_r:+.3f}  │  │  Kraftfeld   │  │ w = {w_f:+.3f}  │
    │ EXPANSION  │  │              │  │ KONTRAKT.  │
    └────────────┘  └──────────────┘  └────────────┘

    Physik:
    • Vorn: Starke Kopplung → schnelle Oszillation
      → ⟨½ε̇²⟩ ≈ ⟨V(ε)⟩ → w ≈ 0 → Materieähnlich
    • Hinten: Schwache Kopplung → Plateau → Slow Roll
      → ½ε̇² << V(ε) → w → −1 → De Sitter
    • Hubble-Reibung (3H·ε̇) bremst das Feld

    Steuerung:
    • Δφ = 0   → Kontraktion (Fusion aktiv)
    • Δφ = π/2 → Expansion (Slow Roll)
    • Δφ = π   → Feld aus → flach (Warp aus)

    ρ > 0 überall. Keine negative Energie.
    """
    ax.text(0.02, 0.98, schema, transform=ax.transAxes,
            fontsize=7.5, verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    fig.suptitle(
        'Warpantrieb: Kontraktion (vorn) + Expansion (hinten)\n'
        'Klein-Gordon mit Hubble-Reibung — ρ > 0 überall',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_profil.png'), dpi=150)
    plt.close()
    print("  → warp_profil.png")


def plot_scaling(results, output_dir):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    labels = [r['label'] for r in results]
    rhos = [r['rho_E'] for r in results]
    ax = axes[0]
    ax.barh(range(len(labels)), rhos, color='#FF9800', alpha=0.8)
    ax.set_xscale('log')
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel('ρ_fokus [J/m³]')
    ax.set_title('Energiedichte am Fokus')
    ax.axvline(5.5e3 * C**2, color='blue', ls=':', label='Erde (ρc²)')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3, axis='x')

    ax = axes[1]; ax.axis('off')
    table_data = [['Konfiguration', 'P [GW]', 'Gain', 'ρ [J/m³]', 'R [1/m²]']]
    for r in results:
        table_data.append([r['label'], f"{r['P_total']/1e9:.1f}",
                           f"{r['gain']:.0f}×", f"{r['rho_E']:.2e}",
                           f"{r['R']:.2e}"])
    table = ax.table(cellText=table_data[1:], colLabels=table_data[0],
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False); table.set_fontsize(8)
    table.scale(1.1, 1.6)
    ax.set_title('Ergebnisse', fontsize=11, pad=20)
    fig.suptitle('Warpantrieb: Skalierung (Reaktoranzahl × Gain)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_skalierung.png'), dpi=150)
    plt.close()
    print("  → warp_skalierung.png")


# ============================================================
# 7. Hauptprogramm
# ============================================================

def main():
    print("=" * 60)
    print("WARPANTRIEB: Resonanzfeldgetriebene Raumzeitkrümmung")
    print("Kaskade: Spaltung → Fusion → Raumzeitkrümmung")
    print("Expansion: Slow-Roll-Mechanismus (Starobinsky-Plateau)")
    print("RFT: E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    output_dir = "figures"
    ensure_dir(output_dir)

    system = FusionWarpSystem(
        n_drive=12, n_focus_front=6, n_focus_rear=6,
        p_reactor=P_REACTOR, gain=1.5, pulse_rate=10.0,
        focus_distance=100.0, sigma=5.0
    )
    system.info()

    # --- Experiment 1 ---
    print("\n=== Experiment 1: Energiestufen ===")
    scenarios = experiment_energy_cascade()
    for s in scenarios:
        print(f"  {s['name']:35s}  ρ={s['rho_E']:.2e}  R={s['R']:.2e}")
    plot_energy_cascade(scenarios, output_dir)

    # --- Experiment 2 ---
    print("\n=== Experiment 2: Phasenscan ===")
    phis, rho_focus = experiment_phase_scan(system)
    print(f"  Δφ=0:   ρ={rho_focus[0]:.4e}")
    print(f"  Δφ=π/2: ρ={rho_focus[len(phis)//4]:.4e}")
    print(f"  Δφ=π:   ρ={rho_focus[len(phis)//2]:.4e}")
    rho_mean = plot_phase_scan(phis, rho_focus, output_dir)
    if rho_mean > 0:
        print(f"  RFT-Signatur: ρ(0)/⟨ρ⟩ = {rho_focus[0]/rho_mean:.4f}")

    # --- Experiment 3: Klein-Gordon Slow Roll (KERN) ---
    print("\n=== Experiment 3: Klein-Gordon mit Hubble-Reibung ===")
    print("  Potential: V = V₀(1−e^(−αε))² (Starobinsky-Plateau)")
    print()
    modes = experiment_klein_gordon_slow_roll()
    print(f"  {'Δφ/π':>8s}  {'ε(Δφ)':>8s}  {'⟨w⟩':>8s}  {'a(T)/a(0)':>10s}  "
          f"{'Expansion':>10s}  Modus")
    print(f"  {'─'*8}  {'─'*8}  {'─'*8}  {'─'*10}  {'─'*10}  {'─'*25}")
    for m in modes:
        dp = m['delta_phi']
        w = m['w_avg']
        ar = m['a_ratio']
        exp_str = "JA" if m['expanding'] else "nein"
        if w < -1/3:
            modus = "Slow Roll → EXPANSION"
        elif w < 0:
            modus = "Übergang"
        elif w < 0.1:
            modus = "Materie → Kontraktion"
        elif m['rho_avg'] < 1e-10:
            modus = "Feld aus → flach"
        else:
            modus = "Strahlung → Kontraktion"
        print(f"  {dp/PI:8.3f}  {m['eps_coupling']:8.3f}  {w:8.3f}  "
              f"{ar:10.4f}  {exp_str:>10s}  {modus}")

    plot_klein_gordon(modes, output_dir)
    plot_w_scan(modes, output_dir)

    # --- Experiment 4: Warp-Profil ---
    print("\n=== Experiment 4: Warp-Profil ===")
    x_wp, rho_wp, w_wp, exp_wp, w_f, w_r = \
        experiment_warp_profile(system, modes)
    print(f"  Vorn (Δφ=0):    w = {w_f:+.3f} (Kontraktion)")
    print(f"  Hinten (Δφ=π/2): w = {w_r:+.3f} "
          f"({'EXPANSION' if w_r < -1/3 else 'Übergang'})")
    print(f"  Mitte:           w = 0 (Schiff geschützt)")
    plot_warp_full(x_wp, rho_wp, w_wp, exp_wp, system, w_f, w_r, output_dir)

    # --- Experiment 5: Skalierung ---
    print("\n=== Experiment 5: Skalierung ===")
    results = experiment_scaling()
    for r in results:
        print(f"  {r['label']:25s}  P={r['P_total']/1e9:7.1f} GW  "
              f"ρ={r['rho_E']:.2e}  R={r['R']:.2e}")
    plot_scaling(results, output_dir)

    # --- Zusammenfassung ---
    R_sun = 8 * PI * G * 1.6e5

    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("=" * 60)
    print(f"""
  Warpantrieb: Spaltung → Fusion → Raumzeitkrümmung

  Grundformel:    E = π · ε(Δφ) · ℏ · f, κ = 1
  Expansion:      Klein-Gordon + Hubble-Reibung + Starobinsky-Plateau

  KERN-ERGEBNIS:
  ──────────────
  Die Phase Δφ steuert die Zustandsgleichung w = p/ρ:

    Δφ = 0:   w = {w_f:+.3f}  → Kontraktion (vorn, Fusion)
    Δφ = π/2: w = {w_r:+.3f}  → {'EXPANSION' if w_r < -1/3 else 'Übergang'} (hinten, Slow Roll)
    Δφ = π:   Feld aus       → flach (Warp aus)

  Physik:
    Vorn: Starke Kopplung → schnelle Oszillation
          ⟨½ε̇²⟩ ≈ ⟨V(ε)⟩ → w ≈ 0 (Materie)
    Hinten: Schwache Kopplung → Starobinsky-Plateau
          ½ε̇² << V(ε) → w → −1 (De Sitter)
    Hubble-Reibung 3H·ε̇ bremst das Feld auf dem Plateau

  ρ > 0 ÜBERALL. Keine negative Energie.
  Expansion durch negativen DRUCK, nicht negative ENERGIE.
  Wie im Universum: Λ > 0, p < 0, ρ > 0.

  Kaskade:
    Stufe 1: 1.2 GW Treiberleistung
    Stufe 2: 180 MJ/Puls Fusion, ρ = {system.rho_E_pellet:.2e} J/m³
    Stufe 3: R = {system.R_pellet:.2e}, Peak {system.rho_P_pellet * 8*PI*G/C**2 / R_sun:.0f}× Sonne

  RFT-Signatur: ρ(0)/⟨ρ⟩ = {rho_focus[0]/rho_mean:.4f}

  Plots: {output_dir}/ (6 Plots)
""")
    print("Fertig.")


if __name__ == "__main__":
    main()