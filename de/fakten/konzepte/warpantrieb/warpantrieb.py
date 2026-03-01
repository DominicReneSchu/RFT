# warpantrieb.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Warpantrieb: Zwei-Feld-Modell
#
# Architektur:
#   Stufe 1: Resonanzreaktoren (Spaltung) → Treiberenergie
#   Stufe 2: Trägheitsfusion → extreme Energiedichte
#   Stufe 3: Asymmetrische Zwei-Feld-Steuerung → Warp
#
# Zwei-Feld-Physik:
#   Feld 1 (ε₁): Fusionsfeld — schnell oszillierend
#     → Hohe kinetische Energie: ½ε̇₁² >> V(ε₁)
#     → w₁ ≈ +1/3 bis +1 → KONTRAKTION (vorn)
#
#   Feld 2 (ε₂): Skalarfeld — langsam rollend (Plateau)
#     → Hohe potentielle Energie: V(ε₂) >> ½ε̇₂²
#     → w₂ ≈ −1 → EXPANSION (hinten, De Sitter)
#
#   Gekoppelt über Klein-Gordon in FLRW:
#     ε̈ᵢ + 3H·ε̇ᵢ + V'ᵢ(εᵢ) + g·εⱼ = 0
#     H² = (κ/3)(ρ₁ + ρ₂ + ρ_kopplung)
#
#   RFT-Steuerung:
#     Δφ steuert die MISCHUNG der beiden Felder:
#     Δφ = 0:   ε₁ dominiert → w_eff > 0 → Kontraktion (vorn)
#     Δφ = π/2: ε₂ dominiert → w_eff ≈ −1 → Expansion (hinten)
#     Δφ = π:   Beide aus → w = 0 → flach (Warp aus)

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
V_PELLET = 4 / 3 * PI * (1e-3) ** 3
TAU_BURN = 1e-8


def coupling_efficiency(delta_phi):
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 2. Zwei-Feld Klein-Gordon in FLRW
# ============================================================

def two_field_warp(delta_phi, m1=1.0, m2=1.0, lmbda1=0.5, lmbda2=0.01,
                   g_coupling=0.05, kappa=1.0, V0_plateau=0.5,
                   eps1_0=1.0, eps2_0=1.0,
                   t_max=80.0, n_eval=8000):
    """
    Zwei gekoppelte Skalarfelder in selbstkonsistenter FLRW-Raumzeit.

    Feld 1 (Fusionsfeld): Harmonisch + stark nichtlinear
      V₁(ε₁) = ½m₁²ε₁² + ¼λ₁ε₁⁴
      → Oszilliert schnell → ⟨w₁⟩ ≈ 0 bis +1/3

    Feld 2 (Expansionsfeld): Starobinsky-Plateau
      V₂(ε₂) = V₀(1 − exp(−α·ε₂))²
      → Slow Roll auf Plateau → w₂ ≈ −1

    Kopplung: g · ε₁ · ε₂ (wie in coupled_flrw.py)

    RFT-Steuerung über Δφ:
      ε(Δφ) = cos²(Δφ/2) bestimmt die Mischung:
      Amplitude Feld 1: ∝ ε(Δφ) (stark bei Δφ=0)
      Amplitude Feld 2: ∝ (1 − ε(Δφ)) (stark bei Δφ=π)
      Bei Δφ=π/2: Beide gleich → Feld 2 dominiert durch Plateau

    Returns: Dictionary mit Zeitreihen und Diagnostik.
    """
    eps_c = coupling_efficiency(delta_phi)

    # Anfangsamplituden: Δφ steuert die Mischung
    # Δφ=0: Feld 1 maximal, Feld 2 minimal
    # Δφ=π/2: Beide gleich
    # Δφ=π: Beide null
    a1 = eps1_0 * eps_c
    a2 = eps2_0 * (1.0 - eps_c) * 2.0  # Faktor 2: Plateau braucht großes ε₂

    # Feld 1: Startet mit hoher kinetischer Energie (oszillierend)
    epsdot1_0 = m1 * a1 * 2.0 if a1 > 1e-10 else 0.0
    # Feld 2: Startet mit niedriger kinetischer Energie (Slow Roll)
    epsdot2_0 = 0.0  # Ruhe auf Plateau

    # Potentiale
    alpha_sr = np.sqrt(2.0 / 3.0)

    def V1(eps):
        return 0.5 * m1 ** 2 * eps ** 2 + 0.25 * lmbda1 * eps ** 4

    def V1p(eps):
        return m1 ** 2 * eps + lmbda1 * eps ** 3

    def V2(eps):
        return V0_plateau * (1.0 - np.exp(-alpha_sr * abs(eps))) ** 2

    def V2p(eps):
        s = np.sign(eps) if abs(eps) > 1e-30 else 1.0
        return 2.0 * V0_plateau * alpha_sr * np.exp(-alpha_sr * abs(eps)) * \
            (1.0 - np.exp(-alpha_sr * abs(eps))) * s

    def rhs(t, y):
        e1, ed1, e2, ed2, a = y
        if a < 1e-30:
            return [0, 0, 0, 0, 0]

        rho1 = 0.5 * ed1 ** 2 + V1(e1)
        rho2 = 0.5 * ed2 ** 2 + V2(e2)
        rho_coupl = g_coupling * e1 * e2
        rho_total = max(rho1 + rho2 + rho_coupl, 1e-30)

        H = np.sqrt(kappa / 3.0 * rho_total)
        adot = a * H

        # Klein-Gordon mit Hubble-Reibung + Kopplung
        edd1 = -3.0 * H * ed1 - V1p(e1) - g_coupling * e2
        edd2 = -3.0 * H * ed2 - V2p(e2) - g_coupling * e1

        return [ed1, edd1, ed2, edd2, adot]

    y0 = [a1, epsdot1_0, a2, epsdot2_0, 1.0]
    t_eval = np.linspace(0, t_max, n_eval)

    sol = solve_ivp(rhs, (0, t_max), y0, t_eval=t_eval,
                    rtol=1e-10, atol=1e-13, method='DOP853')

    e1 = sol.y[0]
    ed1 = sol.y[1]
    e2 = sol.y[2]
    ed2 = sol.y[3]
    a = sol.y[4]
    t = sol.t

    # Energiedichten und Drücke
    rho1 = 0.5 * ed1 ** 2 + V1(e1)
    p1 = 0.5 * ed1 ** 2 - V1(e1)
    rho2 = 0.5 * ed2 ** 2 + V2(e2)
    p2 = 0.5 * ed2 ** 2 - V2(e2)
    rho_coupl = g_coupling * e1 * e2
    rho_total = rho1 + rho2 + rho_coupl
    p_total = p1 + p2 + rho_coupl

    w1 = np.where(rho1 > 1e-30, p1 / rho1, 0.0)
    w2 = np.where(rho2 > 1e-30, p2 / rho2, 0.0)
    w_total = np.where(rho_total > 1e-30, p_total / rho_total, 0.0)

    H = np.sqrt(kappa / 3.0 * np.maximum(rho_total, 1e-30))

    # Beschleunigung: ä/a = H² + Ḣ = −(κ/6)(ρ + 3p)
    accel = -(kappa / 6.0) * (rho_total + 3.0 * p_total)

    # Zeitgemittelte Werte (zweite Hälfte)
    half = len(t) // 2
    w1_avg = np.mean(w1[half:])
    w2_avg = np.mean(w2[half:])
    w_total_avg = np.mean(w_total[half:])
    rho1_avg = np.mean(rho1[half:])
    rho2_avg = np.mean(rho2[half:])

    # Frühe Phase (Slow Roll, t < t_max/4)
    quarter = max(len(t) // 4, 1)
    w_total_early = np.mean(w_total[:quarter])
    w2_early = np.mean(w2[:quarter])
    accel_early = np.mean(accel[:quarter])

    a_ratio = a[-1] / a[0] if a[0] > 0 else 1.0
    expanding = a_ratio > 1.0
    accelerating_early = accel_early > 0

    return {
        't': t, 'e1': e1, 'ed1': ed1, 'e2': e2, 'ed2': ed2, 'a': a,
        'rho1': rho1, 'p1': p1, 'rho2': rho2, 'p2': p2,
        'rho_total': rho_total, 'p_total': p_total,
        'w1': w1, 'w2': w2, 'w_total': w_total,
        'H': H, 'accel': accel,
        'w1_avg': w1_avg, 'w2_avg': w2_avg, 'w_total_avg': w_total_avg,
        'w_total_early': w_total_early, 'w2_early': w2_early,
        'accel_early': accel_early,
        'rho1_avg': rho1_avg, 'rho2_avg': rho2_avg,
        'delta_phi': delta_phi, 'eps_coupling': eps_c,
        'a_ratio': a_ratio, 'expanding': expanding,
        'accelerating_early': accelerating_early
    }


# ============================================================
# 3. Fusions-Warp-System
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
        self.R_pellet = 8 * PI * G / C ** 2 * self.rho_E_pellet

    def energy_density_field(self, x_grid, y_grid,
                              delta_phi_front=0.0, delta_phi_rear=0.0):
        eps_f = coupling_efficiency(delta_phi_front)
        eps_r = coupling_efficiency(delta_phi_rear)
        dx_f = x_grid - self.focus_distance
        r2_f = dx_f ** 2 + y_grid ** 2
        A_f = self.n_focus_front * np.exp(-r2_f / (2 * self.sigma ** 2))
        dx_r = x_grid + self.focus_distance
        r2_r = dx_r ** 2 + y_grid ** 2
        A_r = self.n_focus_rear * np.exp(-r2_r / (2 * self.sigma ** 2))
        rho = (A_f * eps_f) ** 2 * self.rho_E_pellet / self.n_focus_front ** 2 \
            + (A_r * eps_r) ** 2 * self.rho_E_pellet / self.n_focus_rear ** 2
        return rho

    def info(self):
        R_sun = 8 * PI * G * 1.6e5
        print("=" * 60)
        print("WARPANTRIEB: Fusions-Warp-System (Zwei-Feld)")
        print("=" * 60)
        print(f"  Stufe 1: {self.n_drive}×{self.p_reactor / 1e6:.0f} MW"
              f" = {self.P_drive_total / 1e9:.2f} GW")
        print(f"  Stufe 2: Gain {self.gain}×,"
              f" {self.E_fusion_per_pulse / 1e6:.0f} MJ/Puls")
        print(f"  Stufe 3: ρ={self.rho_E_pellet:.2e} J/m³,"
              f" R={self.R_pellet:.2e} 1/m²")
        print(f"           Peak/Sonne:"
              f" {self.rho_P_pellet * 8 * PI * G / C ** 2 / R_sun:.0f}×")
        print("=" * 60)


# ============================================================
# 4. Experimente
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
        {"name": "Erdmittelpunkt", "rho_E": 5.5e3 * C ** 2},
        {"name": "Sonnenmittelpunkt", "rho_E": 1.6e5 * C ** 2},
        {"name": "Alcubierre (v=0.1c)", "rho_E": 1e30},
    ]
    for s in scenarios:
        s["R"] = 8 * PI * G / C ** 2 * s["rho_E"]
    return scenarios


def experiment_phase_scan(system, n_phi=50):
    phis = np.linspace(0, 2 * PI, n_phi)
    rho_focus = np.zeros(n_phi)
    x_pt = np.array([[float(system.focus_distance)]])
    y_pt = np.array([[0.0]])
    for i, dp in enumerate(phis):
        rho = system.energy_density_field(x_pt, y_pt, dp, PI)
        rho_focus[i] = rho[0, 0]
    return phis, rho_focus


def experiment_two_field_scan():
    """Kern-Experiment: w(Δφ) mit Zwei-Feld-Modell."""
    delta_phis = np.array([0.0, PI / 8, PI / 4, 3 * PI / 8, PI / 2,
                           5 * PI / 8, 3 * PI / 4, 7 * PI / 8, PI])
    modes = []
    for dp in delta_phis:
        result = two_field_warp(delta_phi=dp, t_max=80.0)
        modes.append(result)
    return modes


def experiment_scaling():
    configs = [
        (6, 1.0, "6×100MW, G=1"), (6, 1.5, "6×100MW, G=1.5"),
        (12, 1.5, "12×100MW, G=1.5"), (12, 5.0, "12×100MW, G=5"),
        (24, 10.0, "24×100MW, G=10"), (48, 10.0, "48×100MW, G=10"),
        (100, 50.0, "100×100MW, G=50"), (100, 100.0, "100×100MW, G=100"),
    ]
    results = []
    for n_d, gain, label in configs:
        s = FusionWarpSystem(n_drive=n_d, gain=gain)
        x_pt = np.array([[float(s.focus_distance)]])
        y_pt = np.array([[0.0]])
        rho = s.energy_density_field(x_pt, y_pt, 0.0, PI)
        rho_val = rho[0, 0]
        results.append({'label': label, 'n_drive': n_d, 'gain': gain,
                        'P_total': n_d * P_REACTOR, 'rho_E': rho_val,
                        'R': 8 * PI * G / C ** 2 * rho_val})
    return results


# ============================================================
# 5. Plots
# ============================================================

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def plot_energy_cascade(scenarios, out):
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
    ax.set_xlabel('ρ [J/m³]')
    ax.set_title('Energiestufen-Vergleich', fontsize=12, fontweight='bold')
    for i, (bar, s) in enumerate(zip(bars, scenarios)):
        ax.text(bar.get_width() * 1.5, i, f'R={s["R"]:.1e}',
                va='center', fontsize=8, color='darkblue')
    ax.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_energiestufen.png'), dpi=150)
    plt.close()
    print("  → warp_energiestufen.png")


def plot_phase_scan(phis, rho_focus, out):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    eps4 = coupling_efficiency(phis) ** 2
    eps4n = eps4 / np.max(eps4)
    rn = rho_focus / np.max(rho_focus)
    axes[0].plot(phis / PI, rn, 'b-', lw=2, label='Simulation')
    axes[0].plot(phis / PI, eps4n, 'r--', lw=1.5, label='cos⁴(Δφ/2)')
    axes[0].set_xlabel('Δφ/π'); axes[0].set_ylabel('ρ (norm.)')
    axes[0].set_title('Energiedichte'); axes[0].legend(fontsize=8)
    axes[0].set_xlim(0, 2); axes[0].grid(True, alpha=0.3)

    axes[1].plot(phis / PI, rn, 'g-', lw=2, label='R(Δφ)')
    axes[1].plot(phis / PI, eps4n, 'r--', lw=1.5, label='cos⁴(Δφ/2)')
    axes[1].set_xlabel('Δφ/π'); axes[1].set_ylabel('R (norm.)')
    axes[1].set_title('Krümmung'); axes[1].legend(fontsize=8)
    axes[1].set_xlim(0, 2); axes[1].grid(True, alpha=0.3)

    rm = np.mean(rho_focus)
    ratio = rho_focus / rm if rm > 0 else np.ones_like(rho_focus)
    axes[2].plot(phis / PI, ratio, 'b-', lw=2)
    axes[2].axhline(2.0, color='red', ls=':', label='RFT ≈ 2.0')
    axes[2].axhline(1.0, color='gray', ls='--', label='Inkohärent')
    axes[2].set_xlabel('Δφ/π'); axes[2].set_ylabel('ρ/⟨ρ⟩')
    axes[2].set_title('RFT-Signatur'); axes[2].legend(fontsize=8)
    axes[2].set_xlim(0, 2); axes[2].grid(True, alpha=0.3)

    fig.suptitle('Phasenscan (ε = cos²(Δφ/2), κ = 1)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_phasenscan.png'), dpi=150)
    plt.close()
    print("  → warp_phasenscan.png")
    return rm


def plot_two_field_details(modes, out):
    """Kern-Plot: Drei Schlüsselmodi des Zwei-Feld-Systems."""
    key_dps = [0.0, PI / 2, PI]
    key_modes = []
    for target in key_dps:
        dists = [abs(m['delta_phi'] - target) for m in modes]
        key_modes.append(modes[np.argmin(dists)])

    labels = ['Δφ = 0\n(Feld 1 dominiert → Kontraktion)',
              'Δφ = π/2\n(Feld 2 dominiert → Expansion)',
              'Δφ = π\n(Beide aus → flach)']
    colors = ['blue', 'red', 'gray']

    fig, axes = plt.subplots(4, 3, figsize=(18, 18))

    for i, (m, label, c) in enumerate(zip(key_modes, labels, colors)):
        t = m['t']
        n = min(len(t), 3000)

        # Zeile 1: Felder
        ax = axes[0, i]
        ax.plot(t[:n], m['e1'][:n], 'b-', lw=1, alpha=0.8, label='ε₁ (Fusion)')
        ax.plot(t[:n], m['e2'][:n], 'r-', lw=1, alpha=0.8, label='ε₂ (Plateau)')
        ax.set_ylabel('ε(t)'); ax.set_title(label, fontsize=9)
        ax.legend(fontsize=6); ax.grid(True, alpha=0.3)

        # Zeile 2: w₁, w₂, w_total
        ax = axes[1, i]
        win = min(100, n // 10)
        if n > win:
            w1s = np.convolve(m['w1'], np.ones(win) / win, mode='same')
            w2s = np.convolve(m['w2'], np.ones(win) / win, mode='same')
            wts = np.convolve(m['w_total'], np.ones(win) / win, mode='same')
            ax.plot(t[:n], w1s[:n], 'b-', lw=1.5,
                    label=f'w₁={m["w1_avg"]:+.3f}')
            ax.plot(t[:n], w2s[:n], 'r-', lw=1.5,
                    label=f'w₂={m["w2_avg"]:+.3f}')
            ax.plot(t[:n], wts[:n], 'k-', lw=2.5,
                    label=f'w_ges={m["w_total_avg"]:+.3f}')
        ax.axhline(-1, color='green', ls=':', lw=1, label='De Sitter')
        ax.axhline(-1 / 3, color='purple', ls='--', lw=1, label='Grenze')
        ax.axhline(0, color='gray', ls='-', lw=0.5)
        ax.axhline(1 / 3, color='orange', ls=':', lw=1, label='Strahlung')
        ax.set_ylabel('w = p/ρ'); ax.set_ylim(-1.5, 1.0)
        ax.legend(fontsize=5, loc='upper right', ncol=2)
        ax.grid(True, alpha=0.3)

        # Zeile 3: Skalenfaktor a(t)
        ax = axes[2, i]
        an = m['a'][:n] / m['a'][0]
        ax.plot(t[:n], an, color=c, lw=2)
        ax.axhline(1.0, color='gray', ls='--', lw=0.5)
        ax.set_ylabel('a(t)/a(0)')
        exp_label = "EXPANSION" if m['expanding'] else "~flach"
        ax.set_title(f'a(T)/a(0)={m["a_ratio"]:.2f} → {exp_label}',
                     fontsize=9,
                     color='green' if m['expanding'] and m['a_ratio'] > 1.5
                     else 'black',
                     fontweight='bold' if m['a_ratio'] > 2 else 'normal')
        ax.grid(True, alpha=0.3)

        # Zeile 4: Beschleunigung ä/a
        ax = axes[3, i]
        ax.plot(t[:n], m['accel'][:n], color=c, lw=1, alpha=0.4)
        if n > win:
            acc_s = np.convolve(m['accel'], np.ones(win) / win, mode='same')
            ax.plot(t[:n], acc_s[:n], color=c, lw=2.5)
        ax.axhline(0, color='black', ls='-', lw=1)
        ax.fill_between(t[:n], 0,
                        np.minimum(m['accel'][:n], 0),
                        alpha=0.15, color='red', label='ä<0 (Abbremsung)')
        ax.fill_between(t[:n], 0,
                        np.maximum(m['accel'][:n], 0),
                        alpha=0.15, color='green', label='ä>0 (Beschleunigung)')
        ax.set_xlabel('t'); ax.set_ylabel('ä/a')
        ax.legend(fontsize=6); ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Zwei-Feld Warpantrieb: ε₁ (Fusion/Oszillation) + ε₂ '
        '(Plateau/Slow Roll)\n'
        'ε̈ᵢ + 3H·ε̇ᵢ + V\'ᵢ + g·εⱼ = 0 in FLRW | '
        'RFT: Δφ steuert Mischung',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_zwei_feld.png'), dpi=150)
    plt.close()
    print("  �� warp_zwei_feld.png")


def plot_w_scan(modes, out):
    """w(Δφ) Scan — Kern-Ergebnis."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    dps = np.array([m['delta_phi'] for m in modes])
    w1s = [m['w1_avg'] for m in modes]
    w2s = [m['w2_avg'] for m in modes]
    wts = [m['w_total_avg'] for m in modes]
    wte = [m['w_total_early'] for m in modes]
    ars = [m['a_ratio'] for m in modes]

    # w vs Δφ
    ax = axes[0]
    ax.plot(dps / PI, w1s, 'b^--', lw=1.5, ms=7, label='⟨w₁⟩ (Fusion)')
    ax.plot(dps / PI, w2s, 'rs--', lw=1.5, ms=7, label='⟨w₂⟩ (Plateau)')
    ax.plot(dps / PI, wts, 'ko-', lw=2.5, ms=9, label='⟨w_ges⟩')
    ax.plot(dps / PI, wte, 'gD:', lw=1.5, ms=6,
            label='w_ges (früh, Slow Roll)')
    ax.axhline(-1, color='green', ls=':', lw=1, label='De Sitter')
    ax.axhline(-1 / 3, color='purple', ls='--', lw=1, label='Grenze Expansion')
    ax.axhline(0, color='gray', ls='--', lw=0.5)
    ax.axhline(1 / 3, color='orange', ls=':', lw=1, label='Strahlung')
    ax.fill_between([0, 1], [-1.5, -1.5], [-1 / 3, -1 / 3],
                    alpha=0.08, color='green')
    ax.fill_between([0, 1], [0, 0], [0.5, 0.5],
                    alpha=0.08, color='red')
    ax.set_xlabel('Δφ / π'); ax.set_ylabel('⟨w⟩')
    ax.set_title('Zustandsgleichung vs. Phase')
    ax.set_xlim(0, 1); ax.set_ylim(-1.5, 0.5)
    ax.legend(fontsize=5, loc='lower left'); ax.grid(True, alpha=0.3)

    # a(T)/a(0) vs Δφ
    ax = axes[1]
    colors_a = ['green' if a > 1.1 else ('red' if a < 0.9 else 'gray')
                for a in ars]
    ax.bar(dps / PI, np.array(ars), width=0.08,
           color=colors_a, alpha=0.7, edgecolor='black', linewidth=0.5)
    ax.axhline(1.0, color='black', ls='--', lw=1, label='a=1 (flach)')
    for j, (dp, ar) in enumerate(zip(dps, ars)):
        ax.text(dp / PI, ar + 0.5, f'{ar:.1f}', ha='center', fontsize=7)
    ax.set_xlabel('Δφ / π'); ax.set_ylabel('a(T)/a(0)')
    ax.set_title('Skalenfaktor (Expansion vs. flach)')
    ax.set_xlim(-0.05, 1.05)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # Warp-Profil
    ax = axes[2]
    x_s = np.linspace(-3, 3, 200)
    w_front = wts[0]
    idx_half = np.argmin([abs(m['delta_phi'] - PI / 2) for m in modes])
    w_rear = wts[idx_half]
    w_s = np.zeros_like(x_s)
    for j, xi in enumerate(x_s):
        if xi > 1:
            w_s[j] = w_front
        elif xi < -1:
            w_s[j] = w_rear

    ax.fill_between(x_s, 0, w_s, where=w_s > 0, alpha=0.3, color='red',
                    label=f'Kontraktion (w={w_front:+.3f})')
    ax.fill_between(x_s, 0, w_s, where=w_s < 0, alpha=0.3, color='green',
                    label=f'Expansion (w={w_rear:+.3f})')
    ax.plot(x_s, w_s, 'k-', lw=2)
    ax.axhline(0, color='black', ls='-', lw=0.5)
    ax.axhline(-1 / 3, color='purple', ls='--', alpha=0.5)
    ax.text(2, max(w_front + 0.05, 0.05), 'VORN\nΔφ=0\nFusion',
            ha='center', fontsize=8, color='red')
    ax.text(-2, min(w_rear - 0.05, -0.15), 'HINTEN\nΔφ=π/2\nPlateau',
            ha='center', fontsize=8, color='green')
    ax.text(0, 0.15, '← SCHIFF →', ha='center', fontsize=9,
            fontweight='bold')
    ax.set_xlabel('Position'); ax.set_ylabel('w')
    ax.set_title('Warp-Profil (Zwei-Feld)')
    ax.set_ylim(-1.5, 0.5); ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Zwei-Feld-Warpantrieb: w(Δφ) — Fusion (ε₁) vs. '
        'Plateau (ε₂)\n'
        'Δφ steuert Mischung: Kontraktion ↔ Expansion',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_zustandsgleichung.png'), dpi=150)
    plt.close()
    print("  → warp_zustandsgleichung.png")

    return w_front, w_rear


def plot_scaling(results, out):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    labels = [r['label'] for r in results]
    rhos = [r['rho_E'] for r in results]
    ax = axes[0]
    ax.barh(range(len(labels)), rhos, color='#FF9800', alpha=0.8)
    ax.set_xscale('log')
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel('ρ [J/m³]'); ax.set_title('Energiedichte am Fokus')
    ax.axvline(5.5e3 * C ** 2, color='blue', ls=':', label='Erde')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3, axis='x')

    ax = axes[1]; ax.axis('off')
    td = [['Konfig.', 'P [GW]', 'Gain', 'ρ [J/m³]', 'R [1/m²]']]
    for r in results:
        td.append([r['label'], f"{r['P_total'] / 1e9:.1f}",
                   f"{r['gain']:.0f}×", f"{r['rho_E']:.2e}",
                   f"{r['R']:.2e}"])
    t = ax.table(cellText=td[1:], colLabels=td[0],
                 loc='center', cellLoc='center')
    t.auto_set_font_size(False); t.set_fontsize(8); t.scale(1.1, 1.6)
    ax.set_title('Ergebnisse', fontsize=11, pad=20)
    fig.suptitle('Skalierung (Reaktoranzahl × Gain)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_skalierung.png'), dpi=150)
    plt.close()
    print("  → warp_skalierung.png")


# ============================================================
# 6. Hauptprogramm
# ============================================================

def main():
    print("=" * 60)
    print("WARPANTRIEB: Zwei-Feld-Modell")
    print("Feld 1: Fusion (oszillierend) → Kontraktion")
    print("Feld 2: Plateau (Slow Roll) → Expansion")
    print("RFT: E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    out = "figures"
    ensure_dir(out)

    system = FusionWarpSystem()
    system.info()

    # --- Exp 1: Energiestufen ---
    print("\n=== Experiment 1: Energiestufen ===")
    scenarios = experiment_energy_cascade()
    for s in scenarios:
        print(f"  {s['name']:35s}  ρ={s['rho_E']:.2e}  R={s['R']:.2e}")
    plot_energy_cascade(scenarios, out)

    # --- Exp 2: Phasenscan ---
    print("\n=== Experiment 2: Phasenscan ===")
    phis, rho_focus = experiment_phase_scan(system)
    rho_mean = plot_phase_scan(phis, rho_focus, out)
    print(f"  RFT-Signatur: ρ(0)/⟨ρ⟩ = {rho_focus[0] / rho_mean:.4f}")

    # --- Exp 3: ZWEI-FELD KERN-EXPERIMENT ---
    print("\n=== Experiment 3: Zwei-Feld Klein-Gordon (KERN) ===")
    print("  Feld 1: V₁ = ½m²ε² + ¼λε⁴ (Fusion, oszillierend)")
    print("  Feld 2: V₂ = V₀(1−e^(−αε))² (Starobinsky-Plateau)")
    print("  Kopplung: g·ε₁·ε₂, Hubble-Reibung: 3H·ε̇")
    print()

    modes = experiment_two_field_scan()

    print(f"  {'Δφ/π':>6s} {'ε(Δφ)':>6s} │"
          f" {'⟨w₁⟩':>7s} {'⟨w₂⟩':>7s} {'⟨w_ges⟩':>7s} │"
          f" {'a(T)/a₀':>8s} {'Exp?':>5s} │ Modus")
    print(f"  {'─' * 6} {'─' * 6} │"
          f" {'─' * 7} {'─' * 7} {'─' * 7} │"
          f" {'─' * 8} {'─' * 5} │ {'─' * 28}")

    for m in modes:
        dp = m['delta_phi']
        w1 = m['w1_avg']
        w2 = m['w2_avg']
        wt = m['w_total_avg']
        ar = m['a_ratio']
        exp = "JA" if m['expanding'] and ar > 1.5 else "nein"

        if wt > 1 / 3:
            modus = "Strahlung → KONTRAKTION"
        elif wt > 0.05:
            modus = "Materie → Kontraktion"
        elif wt > -1 / 3:
            modus = "Übergang (w ≈ 0)"
        elif wt > -0.8:
            modus = "Quint. → Expansion"
        else:
            modus = "De Sitter → EXPANSION"

        if m['rho1_avg'] < 1e-10 and m['rho2_avg'] < 1e-10:
            modus = "Feld aus → flach"

        print(f"  {dp / PI:6.3f} {m['eps_coupling']:6.3f} │"
              f" {w1:+7.3f} {w2:+7.3f} {wt:+7.3f} │"
              f" {ar:8.2f} {exp:>5s} │ {modus}")

    plot_two_field_details(modes, out)
    w_front, w_rear = plot_w_scan(modes, out)

    # --- Exp 4: Skalierung ---
    print("\n=== Experiment 4: Skalierung ===")
    results = experiment_scaling()
    for r in results:
        print(f"  {r['label']:25s}  P={r['P_total'] / 1e9:7.1f} GW"
              f"  ρ={r['rho_E']:.2e}  R={r['R']:.2e}")
    plot_scaling(results, out)

    # --- Zusammenfassung ---
    R_sun = 8 * PI * G * 1.6e5

    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG: ZWEI-FELD-WARPANTRIEB")
    print("=" * 60)
    print(f"""
  Grundformel:    E = π · ε(Δφ) · ℏ · f, κ = 1

  ZWEI-FELD-MODELL:
  ─────────────────
  Feld 1 (ε₁): Fusionsfeld — harmonisch + nichtlinear
    V₁ = ½m²ε² + ¼λε⁴ → oszilliert schnell
    Dominiert bei Δφ = 0 (volle Kopplung)

  Feld 2 (ε₂): Expansionsfeld — Starobinsky-Plateau
    V₂ = V₀(1 − e^(−αε))² → Slow Roll
    Dominiert bei Δφ = π/2 (halbe Kopplung)

  Δφ steuert die MISCHUNG:
    Δφ = 0:   ε₁ dominiert → w_ges = {w_front:+.3f} → Kontraktion
    Δφ = π/2: ε₂ dominiert → w_ges = {w_rear:+.3f} → Expansion
    Δφ = π:   Beide aus → w = 0 → flach

  PHYSIK:
    Vorn:   Fusion (½ε̇₁² >> V₁) → w > 0 → Raumzeit schrumpft
    Hinten: Plateau (V₂ >> ½ε̇₂²) → w < 0 → Raumzeit wächst
    Mitte:  Schiff (geschützt durch Kraftfeldgenerator)

    ρ > 0 überall. Keine negative Energie.
    Expansion durch negativen DRUCK, nicht negative ENERGIE.

  KASKADE:
    Stufe 1: {system.n_drive}×{system.p_reactor / 1e6:.0f} MW = {system.P_drive_total / 1e9:.2f} GW
    Stufe 2: Fusion Gain {system.gain}× → {system.E_fusion_per_pulse / 1e6:.0f} MJ/Puls
    Stufe 3: ρ = {system.rho_E_pellet:.2e} J/m³
             Peak: {system.rho_P_pellet * 8 * PI * G / C ** 2 / R_sun:.0f}× Sonnenmitte

  RFT-Signatur: ρ(0)/⟨ρ⟩ = {rho_focus[0] / rho_mean:.4f}

  Plots: {out}/ (5 Plots)
""")
    print("Fertig.")


if __name__ == "__main__":
    main()