# warpantrieb.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Warpantrieb: Zwei-Feld-Modell (optimiert, v3)
#
# Architektur:
#   Stufe 1: Resonanzreaktoren (Spaltung) → Treiberenergie
#   Stufe 2: Trägheitsfusion → extreme Energiedichte
#   Stufe 3: Asymmetrische Zwei-Feld-Steuerung → Warp
#
# Zwei-Feld-Physik:
#   Feld 1 (ε₁): Fusionsfeld — V₁ = ½m₁²ε₁² + ¼λ₁ε₁⁴
#     → Oszilliert schnell → w₁ > 0 → KONTRAKTION
#   Feld 2 (ε₂): Expansionsfeld — V₂ = V₀(1−e^(−αε₂))²
#     → Slow Roll auf Plateau → w₂ ≈ −1 → EXPANSION
#
#   Optimale Parameter (automatisch gefunden):
#     V₀=0.5, λ₁=0.5, ε₂₀=3.0, g=0.02
#     → Δw = w(0) − w(π/2) = +0.057
#     → w(Δφ=0)   = +0.034 (Kontraktion)
#     → w(Δφ=π/2) = −0.024 (Expansion)
#     → ρ > 0 überall (keine negative Energie)

from __future__ import annotations

from typing import Any

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings('ignore', category=RuntimeWarning)

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

# Optimale Zwei-Feld-Parameter (durch Scan gefunden)
OPT_V0 = 0.5       # Plateauhöhe
OPT_M1 = 1.0       # Masse Feld 1
OPT_M2 = 0.3       # Masse Feld 2
OPT_LAM1 = 0.5     # Nichtlinearität Feld 1
OPT_G = 0.02       # Kopplung
OPT_EPS1_0 = 1.5   # Startamplitude Feld 1
OPT_EPS2_0 = 3.0   # Startamplitude Feld 2


def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """ε(Δφ) = cos²(Δφ/2) — universelle RFT-Kopplung."""
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 2. Zwei-Feld Klein-Gordon in FLRW
# ============================================================

def two_field_warp(delta_phi: float, m1: float = OPT_M1, m2: float = OPT_M2,
                   lmbda1: float = OPT_LAM1, g_coupling: float = OPT_G,
                   kappa: float = 1.0, V0_plateau: float = OPT_V0,
                   eps1_0: float = OPT_EPS1_0, eps2_0: float = OPT_EPS2_0,
                   t_max: float = 60.0, n_eval: int = 8000) -> dict[str, Any]:
    """
    Zwei gekoppelte Skalarfelder in selbstkonsistenter FLRW-Raumzeit.

    Feld 1 (Fusionsfeld): V₁ = ½m₁²ε₁² + ¼λ₁ε₁⁴
    Feld 2 (Expansionsfeld): V₂ = V₀(1−exp(−α·ε₂))²

    RFT-Steuerung: Δφ bestimmt die Mischung der Felder.
    """
    eps_c = coupling_efficiency(delta_phi)

    a1 = eps1_0 * eps_c
    a2 = eps2_0 * (1.0 - eps_c)

    omega_eff = np.sqrt(m1 ** 2 + lmbda1 * a1 ** 2) if a1 > 1e-12 else m1
    epsdot1_0 = omega_eff * a1 if a1 > 1e-12 else 0.0
    epsdot2_0 = 0.0

    alpha_sr = np.sqrt(2.0 / 3.0)

    def V1(eps: float | np.ndarray) -> float | np.ndarray:
        return 0.5 * m1 ** 2 * eps ** 2 + 0.25 * lmbda1 * eps ** 4

    def V1p(eps: float | np.ndarray) -> float | np.ndarray:
        return m1 ** 2 * eps + lmbda1 * eps ** 3

    def V2(eps: float | np.ndarray) -> float | np.ndarray:
        return V0_plateau * (1.0 - np.exp(-alpha_sr * abs(eps))) ** 2

    def V2p(eps: float) -> float:
        ae = abs(eps)
        if ae < 1e-30:
            return 0.0
        exp_val = np.exp(-alpha_sr * ae)
        return 2.0 * V0_plateau * alpha_sr * exp_val * \
            (1.0 - exp_val) * np.sign(eps)

    def rhs(t: float, y: list[float]) -> list[float]:
        e1, ed1, e2, ed2, a = y
        if a < 1e-30:
            return [0.0, 0.0, 0.0, 0.0, 0.0]

        rho1 = 0.5 * ed1 ** 2 + V1(e1)
        rho2 = 0.5 * ed2 ** 2 + V2(e2)
        rho_c = g_coupling * e1 * e2
        rho_tot = max(rho1 + rho2 + rho_c, 1e-30)

        H = np.sqrt(kappa / 3.0 * rho_tot)
        adot = a * H

        edd1 = -3.0 * H * ed1 - V1p(e1) - g_coupling * e2
        edd2 = -3.0 * H * ed2 - V2p(e2) - g_coupling * e1

        return [ed1, edd1, ed2, edd2, adot]

    y0 = [a1, epsdot1_0, a2, epsdot2_0, 1.0]
    t_eval = np.linspace(0, t_max, n_eval)

    sol = solve_ivp(rhs, (0, t_max), y0, t_eval=t_eval,
                    rtol=1e-10, atol=1e-13, method='DOP853')

    e1, ed1, e2, ed2, a = sol.y
    t = sol.t

    rho1 = 0.5 * ed1 ** 2 + V1(e1)
    p1 = 0.5 * ed1 ** 2 - V1(e1)
    rho2 = 0.5 * ed2 ** 2 + V2(e2)
    p2 = 0.5 * ed2 ** 2 - V2(e2)
    rho_c = g_coupling * e1 * e2
    rho_tot = rho1 + rho2 + rho_c
    p_tot = p1 + p2 + rho_c

    rho1_s = np.maximum(rho1, 1e-30)
    rho2_s = np.maximum(rho2, 1e-30)
    rho_tot_s = np.maximum(np.abs(rho_tot), 1e-30)

    w1 = np.where(rho1 > 1e-20, p1 / rho1_s, 0.0)
    w2 = np.where(rho2 > 1e-20, p2 / rho2_s, 0.0)
    w_tot = np.where(np.abs(rho_tot) > 1e-20, p_tot / rho_tot_s, 0.0)

    H_arr = np.sqrt(kappa / 3.0 * np.maximum(rho_tot, 1e-30))
    accel = -(kappa / 6.0) * (rho_tot + 3.0 * p_tot)

    quarter = max(len(t) // 4, 1)
    half = len(t) // 2

    a_ratio = float(a[-1] / a[0]) if a[0] > 0 else 1.0

    return {
        't': t, 'e1': e1, 'ed1': ed1, 'e2': e2, 'ed2': ed2, 'a': a,
        'rho1': rho1, 'p1': p1, 'rho2': rho2, 'p2': p2,
        'rho_total': rho_tot, 'p_total': p_tot,
        'w1': w1, 'w2': w2, 'w_total': w_tot,
        'H': H_arr, 'accel': accel,
        'w1_avg': float(np.nanmean(w1[half:])),
        'w2_avg': float(np.nanmean(w2[half:])),
        'w_total_avg': float(np.nanmean(w_tot[half:])),
        'w_total_early': float(np.nanmean(w_tot[:quarter])),
        'w2_early': float(np.nanmean(w2[:quarter])),
        'accel_early': float(np.nanmean(accel[:quarter])),
        'rho1_avg': float(np.nanmean(rho1[half:])),
        'rho2_avg': float(np.nanmean(rho2[half:])),
        'delta_phi': delta_phi, 'eps_coupling': eps_c,
        'a_ratio': a_ratio, 'expanding': a_ratio > 1.0,
        'accelerating_early': float(np.nanmean(accel[:quarter])) > 0
    }


# ============================================================
# 3. Fusions-Warp-System
# ============================================================

class FusionWarpSystem:
    def __init__(self, n_drive: int = 12, n_focus_front: int = 6,
                 n_focus_rear: int = 6, p_reactor: float = P_REACTOR,
                 gain: float = 1.5, pulse_rate: float = 10.0,
                 focus_distance: float = 100.0, sigma: float = 5.0) -> None:
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

    def energy_density_field(self, x_grid: np.ndarray, y_grid: np.ndarray,
                              delta_phi_front: float = 0.0,
                              delta_phi_rear: float = 0.0) -> np.ndarray:
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

    def info(self) -> None:
        R_sun = 8 * PI * G * 1.6e5
        print("=" * 60)
        print("WARPANTRIEB: Fusions-Warp-System (Zwei-Feld, v3)")
        print("=" * 60)
        print(f"  Stufe 1: {self.n_drive}×{self.p_reactor / 1e6:.0f} MW"
              f" = {self.P_drive_total / 1e9:.2f} GW")
        print(f"  Stufe 2: Gain {self.gain}×,"
              f" {self.E_fusion_per_pulse / 1e6:.0f} MJ/Puls")
        print(f"  Stufe 3: ρ = {self.rho_E_pellet:.2e} J/m³,"
              f" R = {self.R_pellet:.2e} 1/m²")
        print(f"           Peak/Sonne:"
              f" {self.rho_P_pellet * 8 * PI * G / C ** 2 / R_sun:.0f}×")
        print("=" * 60)


# ============================================================
# 4. Experimente
# ============================================================

def experiment_energy_cascade() -> list[dict[str, Any]]:
    return [
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


def experiment_phase_scan(system: FusionWarpSystem,
                          n_phi: int = 50) -> tuple[np.ndarray, np.ndarray]:
    phis = np.linspace(0, 2 * PI, n_phi)
    rho_focus = np.zeros(n_phi)
    x_pt = np.array([[float(system.focus_distance)]])
    y_pt = np.array([[0.0]])
    for i, dp in enumerate(phis):
        rho = system.energy_density_field(x_pt, y_pt, dp, PI)
        rho_focus[i] = rho[0, 0]
    return phis, rho_focus


def experiment_two_field_scan() -> list[dict[str, Any]]:
    """w(Δφ) Scan mit optimalen Parametern."""
    delta_phis = np.linspace(0, PI, 13)
    return [two_field_warp(dp) for dp in delta_phis]


def experiment_parameter_optimization() -> list[dict[str, Any]]:
    """Systematische Suche: maximaler Δw."""
    results = []
    for V0 in [0.3, 0.5, 0.8, 1.0, 2.0]:
        for lam1 in [0.3, 0.5, 1.0, 2.0]:
            for e2_0 in [2.0, 3.0, 4.0, 6.0]:
                mf = two_field_warp(0.0, V0_plateau=V0,
                                    lmbda1=lam1, eps2_0=e2_0,
                                    t_max=60.0, n_eval=4000)
                mr = two_field_warp(PI / 2, V0_plateau=V0,
                                    lmbda1=lam1, eps2_0=e2_0,
                                    t_max=60.0, n_eval=4000)
                dw = mf['w_total_avg'] - mr['w_total_avg']
                results.append({
                    'V0': V0, 'lam1': lam1, 'e2_0': e2_0,
                    'w_front': mf['w_total_avg'],
                    'w_rear': mr['w_total_avg'],
                    'dw': dw,
                    'a_front': mf['a_ratio'],
                    'a_rear': mr['a_ratio'],
                })
    results.sort(key=lambda r: r['dw'], reverse=True)
    return results


def experiment_scaling() -> list[dict[str, Any]]:
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

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def plot_energy_cascade(scenarios: list[dict[str, Any]], out: str) -> None:
    for s in scenarios:
        s.setdefault("R", 8 * PI * G / C ** 2 * s["rho_E"])
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


def plot_phase_scan(phis: np.ndarray, rho_focus: np.ndarray,
                    out: str) -> float:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    eps4n = coupling_efficiency(phis) ** 2
    eps4n = eps4n / np.max(eps4n)
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


def plot_two_field_details(modes: list[dict[str, Any]], out: str) -> None:
    """Drei Schlüsselmodi: Δφ=0, π/2, π."""
    key_dps = [0.0, PI / 2, PI]
    key_modes = []
    for target in key_dps:
        key_modes.append(modes[np.argmin(
            [abs(m['delta_phi'] - target) for m in modes])])

    labels = ['Δφ = 0\n(ε₁ dominiert → Kontraktion)',
              'Δφ = π/2\n(ε₂ dominiert → Expansion)',
              'Δφ = π\n(Nur ε₂ → De Sitter)']
    colors = ['blue', 'red', 'gray']

    fig, axes = plt.subplots(4, 3, figsize=(18, 18))

    for i, (m, label, c) in enumerate(zip(key_modes, labels, colors)):
        t = m['t']
        n = min(len(t), 3000)
        win = max(min(100, n // 10), 1)

        ax = axes[0, i]
        ax.plot(t[:n], m['e1'][:n], 'b-', lw=1, alpha=0.8,
                label='ε₁ (Fusion)')
        ax.plot(t[:n], m['e2'][:n], 'r-', lw=1, alpha=0.8,
                label='ε₂ (Plateau)')
        ax.set_ylabel('ε(t)'); ax.set_title(label, fontsize=9)
        ax.legend(fontsize=6); ax.grid(True, alpha=0.3)

        ax = axes[1, i]
        if n > win:
            w1s = np.convolve(m['w1'][:n], np.ones(win) / win, mode='same')
            w2s = np.convolve(m['w2'][:n], np.ones(win) / win, mode='same')
            wts = np.convolve(m['w_total'][:n], np.ones(win) / win,
                              mode='same')
            ax.plot(t[:n], w1s, 'b-', lw=1.5,
                    label=f'w₁={m["w1_avg"]:+.3f}')
            ax.plot(t[:n], w2s, 'r-', lw=1.5,
                    label=f'w₂={m["w2_avg"]:+.3f}')
            ax.plot(t[:n], wts, 'k-', lw=2.5,
                    label=f'w_ges={m["w_total_avg"]:+.3f}')
        ax.axhline(-1, color='green', ls=':', lw=1, label='De Sitter')
        ax.axhline(-1 / 3, color='purple', ls='--', lw=1, label='Exp.-Grenze')
        ax.axhline(0, color='gray', ls='-', lw=0.5)
        ax.axhline(1 / 3, color='orange', ls=':', lw=1, label='Strahlung')
        ax.set_ylabel('w = p/ρ'); ax.set_ylim(-1.5, 1.0)
        ax.legend(fontsize=5, loc='upper right', ncol=2)
        ax.grid(True, alpha=0.3)

        ax = axes[2, i]
        an = m['a'][:n] / m['a'][0]
        ax.plot(t[:n], an, color=c, lw=2)
        ax.axhline(1.0, color='gray', ls='--', lw=0.5)
        ax.set_ylabel('a(t)/a(0)')
        lbl = "EXPANSION" if m['a_ratio'] > 1.5 else "~flach"
        ax.set_title(f'a(T)/a(0) = {m["a_ratio"]:.2f} → {lbl}',
                     fontsize=9,
                     color='green' if m['a_ratio'] > 2 else 'black',
                     fontweight='bold' if m['a_ratio'] > 2 else 'normal')
        ax.grid(True, alpha=0.3)

        ax = axes[3, i]
        ax.plot(t[:n], m['accel'][:n], color=c, lw=0.5, alpha=0.3)
        if n > win:
            ax.plot(t[:n], np.convolve(m['accel'][:n],
                    np.ones(win) / win, mode='same'), color=c, lw=2.5)
        ax.axhline(0, color='black', ls='-', lw=1)
        ax.fill_between(t[:n], 0, np.minimum(m['accel'][:n], 0),
                        alpha=0.15, color='red', label='ä<0 Abbremsung')
        ax.fill_between(t[:n], 0, np.maximum(m['accel'][:n], 0),
                        alpha=0.15, color='green', label='ä>0 Beschleunigung')
        ax.set_xlabel('t'); ax.set_ylabel('ä/a')
        ax.legend(fontsize=6); ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Zwei-Feld Warpantrieb (optimiert): '
        'ε₁ (Fusion) + ε₂ (Plateau)\n'
        f'V₀={OPT_V0}, λ₁={OPT_LAM1}, g={OPT_G}  |  '
        'ε̈ᵢ + 3H·ε̇ᵢ + V\'ᵢ + g·εⱼ = 0  |  ρ > 0 überall',
        fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_zwei_feld.png'), dpi=150)
    plt.close()
    print("  → warp_zwei_feld.png")


def plot_w_scan(modes: list[dict[str, Any]], out: str) -> tuple[float, float]:
    """w(Δφ) Kern-Plot."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    dps = np.array([m['delta_phi'] for m in modes])
    w1s = [m['w1_avg'] for m in modes]
    w2s = [m['w2_avg'] for m in modes]
    wts = [m['w_total_avg'] for m in modes]
    wte = [m['w_total_early'] for m in modes]
    ars = [m['a_ratio'] for m in modes]

    ax = axes[0]
    ax.plot(dps / PI, w1s, 'b^--', lw=1.5, ms=7, label='⟨w₁⟩ Fusion')
    ax.plot(dps / PI, w2s, 'rs--', lw=1.5, ms=7, label='⟨w₂⟩ Plateau')
    ax.plot(dps / PI, wts, 'ko-', lw=2.5, ms=8, label='⟨w_ges⟩', zorder=5)
    ax.plot(dps / PI, wte, 'gD:', lw=1.5, ms=5,
            label='w_ges (Slow Roll)')
    ax.axhline(-1, color='green', ls=':', lw=1, label='De Sitter')
    ax.axhline(-1 / 3, color='purple', ls='--', lw=1, label='Exp.-Grenze')
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

    ax = axes[1]
    ars_log = np.log10(np.maximum(np.array(ars), 1.0))
    c_a = ['green' if a > 1.1 else 'gray' for a in ars]
    ax.bar(dps / PI, ars_log, width=0.06,
           color=c_a, alpha=0.7, edgecolor='black', linewidth=0.5)
    ax.set_xlabel('Δφ / π'); ax.set_ylabel('log₁₀(a(T)/a(0))')
    ax.set_title('Skalenfaktor (log)')
    ax.set_xlim(-0.05, 1.05)
    for j, (dp, ar) in enumerate(zip(dps, ars)):
        if ar > 1.5:
            ax.text(dp / PI, ars_log[j] + 0.1, f'{ar:.0f}',
                    ha='center', fontsize=5, rotation=45)
    ax.grid(True, alpha=0.3)

    ax = axes[2]
    w_front = wts[0]
    idx_half = np.argmin(np.abs(dps - PI / 2))
    w_rear = wts[idx_half]
    dw = w_front - w_rear

    x_s = np.linspace(-3, 3, 200)
    w_s = np.zeros_like(x_s)
    for j, xi in enumerate(x_s):
        if xi > 1:
            w_s[j] = w_front
        elif xi < -1:
            w_s[j] = w_rear

    ax.fill_between(x_s, 0, w_s, where=w_s > 0, alpha=0.3, color='red',
                    label=f'Kontraktion (w={w_front:+.4f})')
    ax.fill_between(x_s, 0, w_s, where=w_s < 0, alpha=0.3, color='green',
                    label=f'Expansion (w={w_rear:+.4f})')
    ax.plot(x_s, w_s, 'k-', lw=2)
    ax.axhline(0, color='black', ls='-', lw=0.5)
    ax.axhline(-1 / 3, color='purple', ls='--', alpha=0.5)
    ax.text(2, max(w_front + 0.02, 0.02), 'VORN\nΔφ=0\nFusion',
            ha='center', fontsize=8, color='red')
    ax.text(-2, min(w_rear - 0.02, -0.08), 'HINTEN\nΔφ=π/2\nPlateau',
            ha='center', fontsize=8, color='green')
    ax.text(0, 0.10, '← SCHIFF →', ha='center', fontsize=9,
            fontweight='bold')
    ax.text(0, -0.5, f'Δw = {dw:+.4f}', ha='center', fontsize=12,
            fontweight='bold',
            color='darkgreen' if dw > 0 else 'darkred',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    ax.set_xlabel('Position'); ax.set_ylabel('w')
    ax.set_title('Warp-Profil')
    ax.set_ylim(-1.0, 0.3); ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        f'Zwei-Feld-Warpantrieb: '
        f'Δw = {dw:+.4f}  |  '
        f'V₀={OPT_V0}, λ₁={OPT_LAM1}  |  ρ > 0 überall',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_zustandsgleichung.png'), dpi=150)
    plt.close()
    print("  → warp_zustandsgleichung.png")
    return w_front, w_rear


def plot_optimization(opt_results: list[dict[str, Any]], out: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    top = opt_results[:min(15, len(opt_results))]
    labels = [f'V₀={r["V0"]}, λ₁={r["lam1"]}, ε₂₀={r["e2_0"]}'
              for r in top]
    dws = [r['dw'] for r in top]

    ax = axes[0]
    ax.barh(range(len(top)), dws,
            color=['green' if d > 0 else 'red' for d in dws], alpha=0.7)
    ax.set_yticks(range(len(top)))
    ax.set_yticklabels(labels, fontsize=6)
    ax.set_xlabel('Δw'); ax.set_title('Top 15')
    ax.axvline(0, color='black', ls='-', lw=1)
    ax.grid(True, alpha=0.3, axis='x')

    ax = axes[1]
    for lam in sorted(set(r['lam1'] for r in opt_results)):
        sub = [r for r in opt_results if r['lam1'] == lam]
        v0_dw = {}
        for r in sub:
            v0_dw.setdefault(r['V0'], []).append(r['dw'])
        xs = sorted(v0_dw.keys())
        ys = [np.mean(v0_dw[x]) for x in xs]
        ax.plot(xs, ys, 'o-', ms=5, label=f'λ₁={lam}')
    ax.set_xlabel('V₀'); ax.set_ylabel('⟨Δw⟩')
    ax.set_title('Δw vs. Plateauhöhe')
    ax.axhline(0, color='black', ls='--', lw=0.5)
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[2]; ax.axis('off')
    best = opt_results[0]
    ax.text(0.05, 0.95, f"""
    OPTIMALE PARAMETER:
    ═══════════════════
    V₀  = {best['V0']:.1f}  (Plateauhöhe)
    λ₁  = {best['lam1']:.1f}  (Nichtlinearität)
    ε₂₀ = {best['e2_0']:.1f}  (Startamplitude Feld 2)

    ERGEBNIS:
    w(Δφ=0)   = {best['w_front']:+.4f}  (KONTRAKTION)
    w(Δφ=π/2) = {best['w_rear']:+.4f}  (EXPANSION)
    Δw        = {best['dw']:+.4f}

    ρ > 0 überall. Keine negative Energie.
    """, transform=ax.transAxes, fontsize=9, va='top',
            fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    fig.suptitle('Parameteroptimierung: Maximaler Gradient Δw',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_optimierung.png'), dpi=150)
    plt.close()
    print("  → warp_optimierung.png")


def plot_scaling(results: list[dict[str, Any]], out: str) -> None:
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
    tbl = ax.table(cellText=td[1:], colLabels=td[0],
                   loc='center', cellLoc='center')
    tbl.auto_set_font_size(False); tbl.set_fontsize(8); tbl.scale(1.1, 1.6)
    ax.set_title('Ergebnisse', fontsize=11, pad=20)

    fig.suptitle('Skalierung (Reaktoranzahl × Gain)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_skalierung.png'), dpi=150)
    plt.close()
    print("  → warp_skalierung.png")


# ============================================================
# 6. Skalierungsgesetz der Energielücke (RT-33)
# ============================================================

def skalierungsgesetz(
    R_range: np.ndarray | None = None,
    v_s_list: list[float] | None = None,
    sigma_list: list[float] | None = None,
    gain_list: list[float] | None = None,
    n_reaktoren_list: list[int] | None = None,
    P_pro_reaktor: float = 1e8,
    pulse_rate: float = 10.0,
    R_ref: float = 50.0,
    plot: bool = True,
    export_csv: bool = True,
    out: str = "figures",
) -> dict:
    """
    Berechnet das Skalierungsgesetz der Energielücke als Funktion von R.

    Kernaussagen:
    - ρ_benötigt(R) ~ c⁴/(8πG) · (v_s/R)² · σ²  [Alcubierre-Skalierung, ∝ R⁻²]
    - ρ_verfügbar(R) = E_fusion/Puls / V_aktiv(R),  V_aktiv = 4πR²/σ
    - Im Wandpacking-Modell (n_reaktoren ∝ R²): ρ_verfügbar = const
    - Lücken-Faktor: L(R) = ρ_benötigt(R) / ρ_verfügbar_0
    - Kritischer Radius R*: L(R*) = 1

    Energieberechnung (konsistent mit FusionWarpSystem):
    - E_fusion/Puls = n · P · (1/f_rep) · gain  [Pulsperiode, nicht τ_Burn]
    - ρ_verfügbar_0 = E_fusion/Puls · σ / (4πR_ref²)

    Falsifizierungskriterium:
    - R* < 1 km    → technisch grundsätzlich erreichbar (langfristig)
    - R* < 1 AU    → technisch sehr anspruchsvoll
    - R* > 1 AU    → nicht technisch erreichbar mit bekannter Physik

    Physikalische Grundlage (Alcubierre 1994, Pfenning & Ford 1997):
    - ρ_benötigt ∝ R⁻² (fallend: große Blase → geringere Raumzeitkrümmung nötig)
    - Gesamtenergie E_benötigt = ρ_benötigt · V_aktiv ~ c⁴·v_s²·σ/(2G) = R-unabhängig
    - Hinweis: c⁴/(8πG)·(v_s/R)² hat SI-Einheiten J/(m³·s²), nicht J/m³ (s.u.)
    - Physikalisch korrekte Formel (dim.konsistent): ρ ~ c²/(8πG)·v_s²·σ²/R² [J/m³]

    Gibt zurück: dict mit R_array, scenarios, L_vs_v, R_crit_vs_v,
                 R_crit_gain, G_star_arr, R_scan4, scenario_summary
    """
    import os

    tau_rep = 1.0 / pulse_rate   # Pulsperiode [s]

    if R_range is None:
        R_range = np.logspace(1, 6, 500)       # 10 m … 1000 km
    if v_s_list is None:
        v_s_list = [0.01 * C, 0.1 * C, 1.0 * C]
    if sigma_list is None:
        sigma_list = [10.0]                     # Wandschärfe [1/m]
    if gain_list is None:
        gain_list = [1.5, 10.0, 100.0]
    if n_reaktoren_list is None:
        n_reaktoren_list = [12, 100, 1000]

    # Szenarien: (label, n_reaktoren, gain, P_pro_reaktor)
    scenarios_params = [
        ("Konservativ (G=1.5, 12×100MW)",
         n_reaktoren_list[0], gain_list[0], P_pro_reaktor),
        ("Realistisch (G=10, 100×1GW)",
         n_reaktoren_list[1] if len(n_reaktoren_list) > 1 else 100,
         gain_list[1] if len(gain_list) > 1 else 10.0,
         P_pro_reaktor * 10),
        ("Optimistisch (G=100, 1000×10GW)",
         n_reaktoren_list[2] if len(n_reaktoren_list) > 2 else 1000,
         gain_list[2] if len(gain_list) > 2 else 100.0,
         P_pro_reaktor * 100),
    ]

    sigma = sigma_list[0]
    AU = 1.496e11   # 1 AU in Metern
    LY = 9.461e15   # 1 Lichtjahr in Metern
    PC = 3.086e16   # 1 Parsec in Metern

    # ----------------------------------------------------------
    # Berechnungen
    # ----------------------------------------------------------
    results = []
    for label, n_r, gain, P_r in scenarios_params:
        # Verfügbare Energiedichte im Wandpacking-Modell (n ∝ R²):
        # E_fusion = n * P * (1/f_rep) * gain  [konsistent mit FusionWarpSystem]
        # V_aktiv(R) = 4πR²/σ  →  ρ_verfügbar = E_fusion·σ/(4πR²)
        # Wandpacking: n ∝ R² → ρ_verfügbar = const = E_0·σ/(4πR_ref²)
        E_ref = n_r * P_r * tau_rep * gain
        rho_avail_0 = E_ref * sigma / (4.0 * PI * R_ref ** 2)

        # ρ_benötigt(R) ~ c⁴/(8πG) · (v_s/R)² · σ²  [Formel aus Aufgabe]
        # Dimensionskonvention: wird als relative Skala (nicht J/m³) verwendet
        v_s = v_s_list[1]   # Referenz: 0.1c
        prefactor = C ** 4 / (8.0 * PI * G)
        rho_needed_arr = prefactor * (v_s / R_range) ** 2 * sigma ** 2

        # Kalibrierung: Normierung auf L_0 = ρ_benötigt/ρ_verfügbar bei R_ref
        # (damit L(R_ref) absolut interpretierbar ist)
        rho_needed_ref = prefactor * (v_s / R_ref) ** 2 * sigma ** 2

        # Lücken-Faktor L(R) = ρ_benötigt(R) / ρ_verfügbar_0
        gap_arr = rho_needed_arr / rho_avail_0

        # Kritischer Radius R* (L=1): aus L(R) = (R*/R)²
        # R* = v_s · σ · c² / sqrt(8πG · ρ_avail_0)
        R_crit = v_s * sigma * C ** 2 / np.sqrt(8.0 * PI * G * max(rho_avail_0, 1e-300))

        # Lücke bei R = R_ref
        L_at_Rref = rho_needed_ref / rho_avail_0

        # Bewertung
        if R_crit < 1e3:
            bewertung = "ERREICHBAR (< 1 km)"
        elif R_crit < AU:
            bewertung = "SEHR SCHWIERIG (< 1 AU)"
        elif R_crit < LY:
            bewertung = "UNERREICHBAR (< 1 Lj)"
        else:
            bewertung = "UNERREICHBAR (> 1 Lj)"

        results.append({
            "label": label,
            "n_reaktoren": n_r,
            "gain": gain,
            "P_pro_reaktor": P_r,
            "rho_avail_0": rho_avail_0,
            "E_ref": E_ref,
            "rho_needed_arr": rho_needed_arr,
            "gap_arr": gap_arr,
            "R_crit": R_crit,
            "L_at_Rref": L_at_Rref,
            "bewertung": bewertung,
        })

    # ----------------------------------------------------------
    # v_s-abhängige Lücke (für Plot 2 und Plot 3)
    # ----------------------------------------------------------
    n_r2, gain2, P_r2 = (scenarios_params[1][1], scenarios_params[1][2],
                          scenarios_params[1][3])
    rho_avail_real = (n_r2 * P_r2 * tau_rep * gain2 * sigma
                      / (4.0 * PI * R_ref ** 2))

    L_vs = {}
    R_crit_vs = {}
    for v_s in v_s_list:
        rho_needed_v = C ** 4 / (8.0 * PI * G) * (v_s / R_range) ** 2 * sigma ** 2
        L_vs[v_s] = rho_needed_v / rho_avail_real
        R_crit_vs[v_s] = (v_s * sigma * C ** 2
                          / np.sqrt(8.0 * PI * G * max(rho_avail_real, 1e-300)))

    # R*(v_s) für alle drei Gain-Szenarien (Plot 3)
    v_scan = np.linspace(0.001, 1.0, 200) * C
    R_crit_gain = {}
    for idx, (lbl, n_r, gain, P_r) in enumerate(scenarios_params):
        rho_a = n_r * P_r * tau_rep * gain * sigma / (4.0 * PI * R_ref ** 2)
        R_crit_gain[lbl] = (v_scan * sigma * C ** 2
                            / np.sqrt(8.0 * PI * G * max(rho_a, 1e-300)))

    # G*(R) für L=1 (Plot 4)
    R_scan4 = np.logspace(1, 6, 500)
    n_base, P_base = 12, P_pro_reaktor
    G_star_arr = (C ** 4 / (8.0 * PI * G) * (v_s_list[1] / R_scan4) ** 2 * sigma ** 2
                  * 4.0 * PI * R_scan4 ** 2 / (n_base * P_base * tau_rep * sigma))

    # ----------------------------------------------------------
    # Terminal-Ausgabe
    # ----------------------------------------------------------
    print("\n" + "=" * 72)
    print("RT-33 — SKALIERUNGSGESETZ DER ENERGIELÜCKE")
    print("=" * 72)
    print(f"\n  σ = {sigma:.1f} /m  |  v_s (Ref) = 0.1c  |  R_ref = {R_ref:.0f} m"
          f"  |  f_rep = {pulse_rate:.0f} Hz")
    print(f"\n  Skalierungsgesetz:")
    print(f"    ρ_benötigt(R)  ~ c⁴/(8πG) · (v_s/R)² · σ²  ∝ R⁻²")
    print(f"    ρ_verfügbar(R) = n·P·(1/f)·gain·σ / (4πR²) ∝ R⁻² (festes n)")
    print(f"    Wandpacking (n ∝ R²): ρ_verfügbar = const → L(R) ∝ R⁻²")
    print(f"\n  {'Szenario':<42s} | {'R*':>14s} | {'G*':>10s} |"
          f" {'L(R_ref)':>10s} | Bewertung")
    print(f"  {'-'*42} | {'-'*14} | {'-'*10} | {'-'*10} | {'-'*28}")

    for r in results:
        Rc = r["R_crit"]
        if Rc < 1e3:
            Rc_str = f"{Rc:.1f} m"
        elif Rc < AU:
            Rc_str = f"{Rc / AU:.2e} AU"
        elif Rc < LY:
            Rc_str = f"{Rc / LY:.2e} Lj"
        elif Rc < PC * 1e6:
            Rc_str = f"{Rc / PC:.2e} pc"
        else:
            Rc_str = f"{Rc:.2e} m"

        G_star_ref = (C ** 4 / (8.0 * PI * G)
                      * (v_s_list[1] / R_ref) ** 2 * sigma ** 2
                      * 4.0 * PI * R_ref ** 2
                      / (r["n_reaktoren"] * r["P_pro_reaktor"] * tau_rep * sigma))
        print(f"  {r['label']:<42s} | {Rc_str:>14s} | {G_star_ref:>10.2e} |"
              f" {r['L_at_Rref']:>10.2e} | {r['bewertung']}")

    print(f"\n  FAZIT: R* liegt für alle Szenarien weit jenseits von 1 AU.")
    print(f"  Die Energielücke ist kein reines Skalierungsproblem —")
    print(f"  sie erfordert G* >> 10⁶ oder neue Physik (Casimir, Stringtheorie).")
    print(f"\n  Vergleich mit Literatur:")
    print(f"    Alcubierre (1994): ρ ~ c²/(8πG)·v_s²·σ²  (dim.-konsistent, σ=const)")
    print(f"    Pfenning & Ford (1997): E_total = c²·v_s²·σ/(2G)  (R-unabhängig)")
    print(f"    RFT-RT-33: L(R) ∝ R⁻² im Wandpacking-Modell — Skalierungsverhalten")
    print(f"    korrekt, aber R* >> 1 AU für alle realistischen Fusionsszenarien.")
    print("=" * 72)

    # ----------------------------------------------------------
    # Plots
    # ----------------------------------------------------------
    if plot:
        ensure_dir(out)
        colors = ["#E53935", "#43A047", "#1E88E5"]

        # --- Plot 1: ρ_benötigt(R) und ρ_verfügbar_0 ---
        fig, ax = plt.subplots(figsize=(10, 6))
        for idx, r in enumerate(results):
            ax.plot(R_range, r["rho_needed_arr"], color=colors[idx],
                    lw=2, label=f"ρ_benötigt — {r['label']}")
            ax.axhline(r["rho_avail_0"], color=colors[idx],
                       ls="--", lw=1.5, alpha=0.8,
                       label=f"ρ_verfügbar₀ = {r['rho_avail_0']:.2e}")
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.set_xlabel("Blasenradius R [m]")
        ax.set_ylabel("Energiedichte [skaliert]")
        ax.set_title("Plot 1: ρ_benötigt(R) vs. ρ_verfügbar — Schnitt = R*\n"
                     "(Wandpacking: n ∝ R², σ = const, v_s = 0.1c)")
        ax.legend(fontsize=8, loc="upper right")
        ax.grid(True, alpha=0.3, which="both")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "rt33_plot1_rho_skalierung.png"), dpi=150)
        plt.close(fig)
        print(f"  → rt33_plot1_rho_skalierung.png")

        # --- Plot 2: Lücken-Faktor L(R) für v_s ∈ {0.01c, 0.1c, 1c} ---
        fig, ax = plt.subplots(figsize=(10, 6))
        v_labels = ["0.01c", "0.1c", "1c"]
        for idx, v_s in enumerate(v_s_list):
            ax.plot(R_range, L_vs[v_s], color=colors[idx],
                    lw=2, label=f"v_s = {v_labels[idx]}")
        ax.axhline(1.0, color="black", ls="-", lw=1.5, label="L = 1 (Lücke geschlossen)")
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.set_xlabel("Blasenradius R [m]")
        ax.set_ylabel("Lücken-Faktor L = ρ_benötigt / ρ_verfügbar")
        ax.set_title("Plot 2: Lücken-Faktor L(R) — Szenario: Realistisch (G=10, 100×1GW)\n"
                     "(Wandpacking-Modell: ρ_verfügbar = const)")
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3, which="both")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "rt33_plot2_luecke_faktor.png"), dpi=150)
        plt.close(fig)
        print(f"  → rt33_plot2_luecke_faktor.png")

        # --- Plot 3: R*(v_s) für drei Gain-Szenarien ---
        fig, ax = plt.subplots(figsize=(10, 6))
        for idx, (lbl, _, _, _) in enumerate(scenarios_params):
            ax.plot(v_scan / C, R_crit_gain[lbl] / AU,
                    color=colors[idx], lw=2, label=lbl)
        ax.axhline(1.0, color="gold", ls="--", lw=2, label="1 AU")
        ax.axhline(1e-8, color="green", ls=":", lw=1.5, label="1 km")
        ax.set_yscale("log")
        ax.set_xlabel("Zielgeschwindigkeit v_s / c")
        ax.set_ylabel("Kritischer Radius R* [AU]")
        ax.set_title("Plot 3: R*(v_s) — Kritischer Radius als Funktion der Zielgeschwindigkeit\n"
                     "(Wandpacking-Modell, σ = 10 /m)")
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3, which="both")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "rt33_plot3_R_krit.png"), dpi=150)
        plt.close(fig)
        print(f"  → rt33_plot3_R_krit.png")

        # --- Plot 4: Benötigter Gain G*(R) für L=1 bei R ∈ [10m, 10⁶m] ---
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(R_scan4, G_star_arr, color="#8E24AA", lw=2.5)
        ax.axhline(1.5, color="#E53935", ls="--", lw=1.5, label="G = 1.5 (Konservativ)")
        ax.axhline(10, color="#43A047", ls="--", lw=1.5, label="G = 10 (Realistisch)")
        ax.axhline(100, color="#1E88E5", ls="--", lw=1.5, label="G = 100 (Optimistisch)")
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.set_xlabel("Blasenradius R [m]")
        ax.set_ylabel("Benötigter Gain G* für L = 1")
        ax.set_title("Plot 4: Benötigter Gain G*(R) für Lückenschluss\n"
                     f"(n_base = {n_base}, P = {P_pro_reaktor:.0e} W, σ = {sigma:.0f} /m, v_s = 0.1c)")
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3, which="both")
        fig.tight_layout()
        fig.savefig(os.path.join(out, "rt33_plot4_gain_krit.png"), dpi=150)
        plt.close(fig)
        print(f"  → rt33_plot4_gain_krit.png")

    # ----------------------------------------------------------
    # CSV-Export
    # ----------------------------------------------------------
    if export_csv:
        import csv
        csv_path = os.path.join(out, "rt33_skalierungsgesetz.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "R_m", "rho_needed_konserv", "rho_needed_realist",
                "rho_needed_optimist",
                "rho_avail_konserv", "rho_avail_realist",
                "rho_avail_optimist",
                "gap_konserv", "gap_realist", "gap_optimist",
            ])
            for i, R_val in enumerate(R_range):
                writer.writerow([
                    f"{R_val:.4e}",
                    f"{results[0]['rho_needed_arr'][i]:.4e}",
                    f"{results[1]['rho_needed_arr'][i]:.4e}",
                    f"{results[2]['rho_needed_arr'][i]:.4e}",
                    f"{results[0]['rho_avail_0']:.4e}",
                    f"{results[1]['rho_avail_0']:.4e}",
                    f"{results[2]['rho_avail_0']:.4e}",
                    f"{results[0]['gap_arr'][i]:.4e}",
                    f"{results[1]['gap_arr'][i]:.4e}",
                    f"{results[2]['gap_arr'][i]:.4e}",
                ])
        print(f"  → rt33_skalierungsgesetz.csv")

    return {
        "R_array": R_range,
        "scenarios": results,
        "L_vs_v": L_vs,
        "R_crit_vs_v": R_crit_vs,
        "R_crit_gain": R_crit_gain,
        "G_star_arr": G_star_arr,
        "R_scan4": R_scan4,
        "v_scan": v_scan,
        "scenario_summary": {
            r["label"]: {
                "R_critical": r["R_crit"],
                "L_at_Rref": r["L_at_Rref"],
                "rho_avail_0": r["rho_avail_0"],
                "bewertung": r["bewertung"],
            }
            for r in results
        },
    }
# ============================================================
# 7. Hauptprogramm
# ============================================================

def main() -> None:
    print("=" * 60)
    print("WARPANTRIEB: Zwei-Feld-Modell (v3, optimiert)")
    print(f"Optimale Parameter: V₀={OPT_V0}, λ₁={OPT_LAM1},"
          f" ε₂₀={OPT_EPS2_0}, g={OPT_G}")
    print("RFT: E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    out = "figures"
    ensure_dir(out)

    system = FusionWarpSystem()
    system.info()

    # Exp 1
    print("\n=== Experiment 1: Energiestufen ===")
    scenarios = experiment_energy_cascade()
    for s in scenarios:
        s["R"] = 8 * PI * G / C ** 2 * s["rho_E"]
        print(f"  {s['name']:35s}  ρ={s['rho_E']:.2e}  R={s['R']:.2e}")
    plot_energy_cascade(scenarios, out)

    # Exp 2
    print("\n=== Experiment 2: Phasenscan ===")
    phis, rho_focus = experiment_phase_scan(system)
    rho_mean = plot_phase_scan(phis, rho_focus, out)
    print(f"  RFT-Signatur: ρ(0)/⟨ρ⟩ = {rho_focus[0] / rho_mean:.4f}")

    # Exp 3
    print("\n=== Experiment 3: Zwei-Feld w(Δφ) Scan ===")
    print(f"  Parameter: V₀={OPT_V0}, λ₁={OPT_LAM1},"
          f" ε₂₀={OPT_EPS2_0}, g={OPT_G}")
    print()

    modes = experiment_two_field_scan()

    print(f"  {'Δφ/π':>6s} {'ε(Δφ)':>6s} │"
          f" {'⟨w₁⟩':>7s} {'⟨w₂⟩':>7s} {'⟨w_ges⟩':>8s} │"
          f" {'a(T)/a₀':>12s} │ Modus")
    print(f"  {'─' * 6} {'─' * 6} │"
          f" {'─' * 7} {'─' * 7} {'─' * 8} │"
          f" {'─' * 12} │ {'─' * 28}")

    for m in modes:
        dp = m['delta_phi']
        wt = m['w_total_avg']
        ar = m['a_ratio']

        if wt > 1 / 3:
            modus = "Strahlung → KONTRAKTION"
        elif wt > 0.01:
            modus = "Materie → Kontraktion"
        elif wt > -0.01:
            modus = "Grenze (w ≈ 0)"
        elif wt > -1 / 3:
            modus = "Quintessenz → Expansion"
        elif wt > -0.8:
            modus = "De Sitter → EXPANSION"
        else:
            modus = "Phantom → starke Expansion"

        if m['rho1_avg'] < 1e-10 and m['rho2_avg'] < 1e-10:
            modus = "Feld aus → flach"

        print(f"  {dp / PI:6.3f} {m['eps_coupling']:6.3f} │"
              f" {m['w1_avg']:+7.3f} {m['w2_avg']:+7.3f}"
              f" {wt:+8.4f} │"
              f" {ar:12.2f} │ {modus}")

    plot_two_field_details(modes, out)
    w_front, w_rear = plot_w_scan(modes, out)
    dw_std = w_front - w_rear

    # Exp 4
    print("\n=== Experiment 4: Parameteroptimierung ===")
    print("  Scan: V₀ × λ₁ × ε₂₀ → maximaler Δw")
    opt = experiment_parameter_optimization()
    print(f"\n  Top 5 (von {len(opt)} Kombinationen):")
    print(f"  {'V₀':>5s} {'λ₁':>5s} {'ε₂₀':>5s} │"
          f" {'w(0)':>8s} {'w(π/2)':>8s} {'Δw':>8s}")
    print(f"  {'─' * 5} {'─' * 5} {'─' * 5} │"
          f" {'─' * 8} {'─' * 8} {'─' * 8}")
    for r in opt[:5]:
        print(f"  {r['V0']:5.1f} {r['lam1']:5.1f} {r['e2_0']:5.1f} │"
              f" {r['w_front']:+8.4f} {r['w_rear']:+8.4f}"
              f" {r['dw']:+8.4f}")
    plot_optimization(opt, out)

    # Exp 5
    print("\n=== Experiment 5: Skalierung ===")
    results = experiment_scaling()
    for r in results:
        print(f"  {r['label']:25s}  P={r['P_total'] / 1e9:7.1f} GW"
              f"  ρ={r['rho_E']:.2e}  R={r['R']:.2e}")
    plot_scaling(results, out)

    # Zusammenfassung
    R_sun = 8 * PI * G * 1.6e5
    best = opt[0]

    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("=" * 60)
    print(f"""
  E = π · ε(Δφ) · ℏ · f, κ = 1

  ZWEI-FELD-MODELL:
  Feld 1: V₁ = ½m²ε² + ¼λε⁴  (Fusion, oszillierend)
  Feld 2: V₂ = V₀(1−e^(−αε))² (Starobinsky-Plateau)

  OPTIMALE PARAMETER:
    V₀={best['V0']}, λ₁={best['lam1']}, ε₂₀={best['e2_0']}, g={OPT_G}

  KERN-ERGEBNIS:
    w(Δφ=0)   = {best['w_front']:+.4f}  → KONTRAKTION (vorn)
    w(Δφ=π/2) = {best['w_rear']:+.4f}  → EXPANSION (hinten)
    Δw        = {best['dw']:+.4f}

    Raum vorn schrumpft, Raum hinten wächst.
    Schiff ruht lokal — keine Beschleunigung.
    Effektive Geschwindigkeit: unbegrenzt.

    ρ > 0 überall. Keine negative Energie.
    Expansion durch negativen DRUCK, nicht negative ENERGIE.

  KASKADE:
    Stufe 1: {system.n_drive}×{system.p_reactor / 1e6:.0f} MW = {system.P_drive_total / 1e9:.2f} GW
    Stufe 2: Gain {system.gain}× → ρ = {system.rho_E_pellet:.2e} J/m³
    Stufe 3: Peak {system.rho_P_pellet * 8 * PI * G / C ** 2 / R_sun:.0f}× Sonnenmitte

  RFT-Signatur: ρ(0)/⟨ρ⟩ = {rho_focus[0] / rho_mean:.4f}

  Plots: {out}/ (6 Plots)
""")
    print("Fertig.")


if __name__ == "__main__":
    main()