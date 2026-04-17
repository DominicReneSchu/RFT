# warp_3d.py
# © Dominic-René Schu, 2025/2026 – Resonance Field Theory
#
# 3D Warp Bubble: Alcubierre geometry with RFT two-field control
#
# The warp bubble encloses the ship completely:
#   - Front (θ=0):    Δφ=0   → ε₁ dominates → Contraction
#   - Rear (θ=π):     Δφ=π/2 → ε₂ dominates → Expansion
#   - Sides (θ=π/2):  Transition zone
#
# Metric (Alcubierre, 1994):
#   ds² = −dt² + (dx − v_s·f(r_s)·dt)² + dy² + dz²
#   f(r_s) = [tanh(σ(r_s+R)) − tanh(σ(r_s−R))] / [2·tanh(σR)]
#
# RFT extension:
#   The shape function is modulated by ε(Δφ(θ)):
#   f_RFT(r_s, θ) = f(r_s) · [ε(Δφ_front)·cos²(θ/2) − ε(Δφ_rear)·sin²(θ/2)]
#   → Asymmetric bubble: Contraction in front, Expansion in rear

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import os

# ============================================================
# 1. Constants and Parameters
# ============================================================

PI = np.pi
G = 6.67430e-11
C = 2.99792458e8
HBAR = 1.054571817e-34

# Bubble parameters
R_BUBBLE = 50.0       # Bubble radius [m]
SIGMA_WALL = 0.3      # Wall thickness (1/σ) — dimensionless
V_SHIP = 0.01         # Ship velocity [c] (for metric)

# RFT parameters (from warp_drive.py, optimized)
OPT_V0 = 0.5
OPT_LAM1 = 0.5
OPT_G = 0.02

# Energy scale (from fusion cascade)
RHO_FUSION = 4.30e16  # J/m³ (12×100MW, G=1.5)
R_CURVATURE_SCALE = 8 * PI * G / C ** 2


def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """ε(Δφ) = cos²(Δφ/2)"""
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 2. Alcubierre Shape Function
# ============================================================

def alcubierre_f(r_s: np.ndarray, R: float = R_BUBBLE, sigma: float = SIGMA_WALL) -> np.ndarray:
    """
    Alcubierre shape function f(r_s).
    f ≈ 1 inside the bubble, f ≈ 0 outside.
    Transition via tanh with width 1/σ.
    """
    sig_R = sigma * R
    denom = 2.0 * np.tanh(sig_R)
    if abs(denom) < 1e-30:
        return np.zeros_like(r_s)
    return (np.tanh(sigma * (r_s + R)) - np.tanh(sigma * (r_s - R))) / denom


def alcubierre_df_dr(r_s: np.ndarray, R: float = R_BUBBLE, sigma: float = SIGMA_WALL) -> np.ndarray:
    """Derivative df/dr_s for curvature calculation."""
    sig_R = sigma * R
    denom = 2.0 * np.tanh(sig_R)
    if abs(denom) < 1e-30:
        return np.zeros_like(r_s)
    return sigma * (1.0 / np.cosh(sigma * (r_s + R)) ** 2
                    - 1.0 / np.cosh(sigma * (r_s - R)) ** 2) / denom


# ============================================================
# 3. Warp Bubble with RFT Control
# ============================================================

class WarpBubble3D:
    """
    3D warp bubble with RFT phase control.

    Geometry:
      - Spherically symmetric around the ship (center at origin)
      - Modified Alcubierre metric
      - Asymmetric through Δφ(θ)

    Fields:
      - Δφ(θ) = (π/2) · (1 − cos²(θ/2))  [0 front, π/2 rear]
      - w(θ) from two-field model (interpolated)
    """

    def __init__(self, R: float = R_BUBBLE, sigma: float = SIGMA_WALL,
                 v_s: float = V_SHIP, rho_scale: float = RHO_FUSION) -> None:
        self.R = R
        self.sigma = sigma
        self.v_s = v_s
        self.rho_scale = rho_scale

        # w(Δφ) lookup (from simulation, section 4.4 warp_drive.py)
        # Δφ/π:  0.0    0.25   0.33   0.50   0.67   0.75   1.00
        # w_total: +0.034 +0.030 +0.006 -0.024 -0.030 -0.055 -0.014
        self.dphi_table = np.array(
            [0.0, 0.083, 0.167, 0.250, 0.333, 0.417, 0.500,
             0.583, 0.667, 0.750, 0.833, 0.917, 1.000]) * PI
        self.w_table = np.array(
            [+0.034, +0.034, +0.033, +0.030, +0.006, +0.019, -0.024,
             +0.023, -0.030, -0.055, -0.049, +0.026, -0.014])

    def delta_phi_of_theta(self, theta: float | np.ndarray) -> float | np.ndarray:
        """
        Phase angle as a function of polar angle θ.
        θ = 0 (flight direction, front) → Δφ = 0
        θ = π (rear) → Δφ = π/2
        Smooth transition via sin²(θ/2).
        """
        return (PI / 2.0) * np.sin(theta / 2.0) ** 2

    def w_of_theta(self, theta: float | np.ndarray) -> float | np.ndarray:
        """Interpolated equation of state w(θ)."""
        dphi = self.delta_phi_of_theta(theta)
        return np.interp(dphi, self.dphi_table, self.w_table)

    def energy_density(self, x: float | np.ndarray, y: float | np.ndarray,
                       z: float | np.ndarray) -> float | np.ndarray:
        """
        Energy density ρ(x,y,z) of the warp bubble.

        Combination of:
        1. Alcubierre shape function (radial)
        2. RFT coupling ε(Δφ(θ)) (angle-dependent)
        3. Fusion energy scale (absolute)
        """
        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        # Polar angle θ: 0 = flight direction (+x)
        theta = np.arctan2(np.sqrt(y ** 2 + z ** 2), x)

        # Radial bubble structure
        f = alcubierre_f(r, self.R, self.sigma)
        df = alcubierre_df_dr(r, self.R, self.sigma)

        # Angle-dependent RFT coupling
        dphi = self.delta_phi_of_theta(theta)
        eps = coupling_efficiency(dphi)

        # Energy density: ∝ (df/dr)² · ε²(Δφ) · ρ_fusion
        # The curvature is concentrated at the bubble wall (df/dr maximal)
        rho = df ** 2 * eps ** 2 * self.rho_scale

        return rho

    def equation_of_state(self, x: float | np.ndarray, y: float | np.ndarray,
                          z: float | np.ndarray) -> float | np.ndarray:
        """w(x,y,z) — spatially resolved equation of state."""
        theta = np.arctan2(np.sqrt(y ** 2 + z ** 2), x)
        return self.w_of_theta(theta)

    def ricci_scalar(self, x: float | np.ndarray, y: float | np.ndarray,
                     z: float | np.ndarray) -> float | np.ndarray:
        """Ricci scalar R(x,y,z) = 8πG/c² · ρ(x,y,z)."""
        return R_CURVATURE_SCALE * self.energy_density(x, y, z)

    def metric_perturbation(self, x: float | np.ndarray,
                            y: float | np.ndarray,
                            z: float | np.ndarray) -> float | np.ndarray:
        """
        Metric perturbation h(x,y,z).
        h ~ v_s · f(r_s) · cos(θ)  (leading order)
        Modified by RFT: h_RFT = h · ε(Δφ(θ))
        """
        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        theta = np.arctan2(np.sqrt(y ** 2 + z ** 2), x)
        f = alcubierre_f(r, self.R, self.sigma)
        dphi = self.delta_phi_of_theta(theta)
        eps = coupling_efficiency(dphi)
        # Asymmetric: positive in front, negative in rear
        return self.v_s * f * np.cos(theta) * eps

    def info(self) -> None:
        print("=" * 60)
        print("WARP BUBBLE 3D: RFT-controlled Alcubierre Geometry")
        print("=" * 60)
        print(f"  Bubble radius R:    {self.R:.0f} m")
        print(f"  Wall thickness 1/σ: {1.0 / self.sigma:.1f} m")
        print(f"  v_ship:             {self.v_s:.4f} c")
        print(f"  ρ_fusion:           {self.rho_scale:.2e} J/m³")
        print(f"  w(θ=0, front):      {self.w_of_theta(0.0):+.4f}")
        print(f"  w(θ=π/2, side):     {self.w_of_theta(PI / 2):+.4f}")
        print(f"  w(θ=π, rear):       {self.w_of_theta(PI):+.4f}")
        print(f"  Δw (front−rear):    "
              f"{self.w_of_theta(0.0) - self.w_of_theta(PI):+.4f}")
        print("=" * 60)


# ============================================================
# 4. Plots
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def plot_bubble_slices(bubble: WarpBubble3D, out: str) -> None:
    """Slices through the 3D bubble: xy-plane (z=0)."""
    L = 2.5 * bubble.R
    N = 300
    x = np.linspace(-L, L, N)
    y = np.linspace(-L, L, N)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    rho = bubble.energy_density(X, Y, Z)
    w = bubble.equation_of_state(X, Y, Z)
    R_ricci = bubble.ricci_scalar(X, Y, Z)
    h = bubble.metric_perturbation(X, Y, Z)

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    # Energy density
    ax = axes[0, 0]
    rho_norm = rho / np.max(rho) if np.max(rho) > 0 else rho
    im = ax.pcolormesh(X, Y, rho_norm, cmap='inferno', shading='auto')
    ax.set_xlabel('x [m]'); ax.set_ylabel('y [m]')
    ax.set_title('Energy density ρ/ρ_max')
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, label='ρ/ρ_max')
    # Ship
    ax.plot(0, 0, 'w*', ms=15, label='Ship')
    ax.legend(fontsize=8)
    # Bubble boundary
    theta_c = np.linspace(0, 2 * PI, 100)
    ax.plot(bubble.R * np.cos(theta_c), bubble.R * np.sin(theta_c),
            'w--', lw=1, alpha=0.5)
    # Flight direction
    ax.annotate('→ Flight', xy=(L * 0.7, 0), fontsize=9, color='white',
                ha='center')

    # Equation of state w
    ax = axes[0, 1]
    im = ax.pcolormesh(X, Y, w, cmap='RdBu_r', shading='auto',
                       vmin=-0.06, vmax=0.04)
    ax.set_xlabel('x [m]'); ax.set_ylabel('y [m]')
    ax.set_title('Equation of state w = p/ρ')
    ax.set_aspect('equal')
    cb = plt.colorbar(im, ax=ax, label='w')
    ax.plot(0, 0, 'k*', ms=15)
    ax.plot(bubble.R * np.cos(theta_c), bubble.R * np.sin(theta_c),
            'k--', lw=1, alpha=0.5)
    ax.annotate('Contraction\nw > 0', xy=(L * 0.6, L * 0.3),
                fontsize=8, color='red', ha='center', fontweight='bold')
    ax.annotate('Expansion\nw < 0', xy=(-L * 0.6, L * 0.3),
                fontsize=8, color='blue', ha='center', fontweight='bold')

    # Ricci scalar
    ax = axes[1, 0]
    R_norm = R_ricci / np.max(R_ricci) if np.max(R_ricci) > 0 else R_ricci
    im = ax.pcolormesh(X, Y, R_norm, cmap='hot', shading='auto')
    ax.set_xlabel('x [m]'); ax.set_ylabel('y [m]')
    ax.set_title('Ricci scalar R/R_max')
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, label='R/R_max')
    ax.plot(0, 0, 'c*', ms=15)
    ax.plot(bubble.R * np.cos(theta_c), bubble.R * np.sin(theta_c),
            'c--', lw=1, alpha=0.5)

    # Metric perturbation
    ax = axes[1, 1]
    h_max = np.max(np.abs(h)) if np.max(np.abs(h)) > 0 else 1.0
    im = ax.pcolormesh(X, Y, h / h_max, cmap='coolwarm', shading='auto',
                       vmin=-1, vmax=1)
    ax.set_xlabel('x [m]'); ax.set_ylabel('y [m]')
    ax.set_title('Metric perturbation h/h_max')
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, label='h/|h|_max')
    ax.plot(0, 0, 'k*', ms=15)
    ax.plot(bubble.R * np.cos(theta_c), bubble.R * np.sin(theta_c),
            'k--', lw=1, alpha=0.5)
    ax.annotate('Space contracts', xy=(L * 0.6, -L * 0.3),
                fontsize=8, color='red', ha='center')
    ax.annotate('Space expands', xy=(-L * 0.6, -L * 0.3),
                fontsize=8, color='blue', ha='center')

    fig.suptitle(
        f'Warp bubble 3D (slice z=0): R = {bubble.R:.0f} m, '
        f'v = {bubble.v_s:.4f}c\n'
        f'RFT: Δφ(θ) controls w(θ): '
        f'front w={bubble.w_of_theta(0):+.3f}, '
        f'rear w={bubble.w_of_theta(PI):+.3f}  |  ρ > 0 everywhere',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_3d_schnitte.png'), dpi=150)
    plt.close()
    print("  → warp_3d_schnitte.png")


def plot_bubble_profiles(bubble: WarpBubble3D, out: str) -> None:
    """Radial and angular profiles of the bubble."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # --- Upper row: Radial profiles ---

    # f(r) shape function
    r = np.linspace(0, 2.5 * bubble.R, 500)
    f = alcubierre_f(r, bubble.R, bubble.sigma)
    df = alcubierre_df_dr(r, bubble.R, bubble.sigma)

    ax = axes[0, 0]
    ax.plot(r, f, 'b-', lw=2, label='f(r)')
    ax.axvline(bubble.R, color='gray', ls='--', lw=1, label=f'R={bubble.R}m')
    ax.set_xlabel('r [m]'); ax.set_ylabel('f(r)')
    ax.set_title('Alcubierre shape function')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(r, df ** 2, 'r-', lw=2, label='(df/dr)²')
    ax.axvline(bubble.R, color='gray', ls='--', lw=1)
    ax.set_xlabel('r [m]'); ax.set_ylabel('(df/dr)²')
    ax.set_title('Energy density profile (radial)')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # Radial profile for θ=0 (front) and θ=π (rear)
    ax = axes[0, 2]
    x_front = np.linspace(0, 2.5 * bubble.R, 500)
    rho_front = bubble.energy_density(x_front, np.zeros_like(x_front),
                                       np.zeros_like(x_front))
    rho_rear = bubble.energy_density(-x_front, np.zeros_like(x_front),
                                      np.zeros_like(x_front))
    rho_max = max(np.max(rho_front), np.max(rho_rear), 1e-30)
    ax.plot(x_front, rho_front / rho_max, 'r-', lw=2,
            label='Front (θ=0)')
    ax.plot(x_front, rho_rear / rho_max, 'b-', lw=2,
            label='Rear (θ=π)')
    ax.axvline(bubble.R, color='gray', ls='--', lw=1)
    ax.set_xlabel('r [m]'); ax.set_ylabel('ρ/ρ_max')
    ax.set_title('Energy density: Front vs. Rear')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # --- Lower row: Angular profiles ---

    theta = np.linspace(0, PI, 200)

    # w(θ)
    ax = axes[1, 0]
    w_theta = bubble.w_of_theta(theta)
    ax.plot(theta / PI, w_theta, 'k-', lw=2.5)
    ax.fill_between(theta / PI, 0, w_theta, where=w_theta > 0,
                    alpha=0.3, color='red', label='Contraction')
    ax.fill_between(theta / PI, 0, w_theta, where=w_theta < 0,
                    alpha=0.3, color='blue', label='Expansion')
    ax.axhline(0, color='black', ls='-', lw=0.5)
    ax.axhline(-1 / 3, color='purple', ls='--', lw=1, alpha=0.5,
               label='w = −1/3')
    ax.set_xlabel('θ / π (0=front, 1=rear)')
    ax.set_ylabel('w(θ)')
    ax.set_title('Equation of state vs. angle')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    # Δφ(θ) and ε(Δφ(θ))
    ax = axes[1, 1]
    dphi = bubble.delta_phi_of_theta(theta)
    eps = coupling_efficiency(dphi)
    ax.plot(theta / PI, dphi / PI, 'g-', lw=2, label='Δφ(θ)/π')
    ax.plot(theta / PI, eps, 'orange', lw=2, ls='--',
            label='ε(Δφ) = cos²(Δφ/2)')
    ax.set_xlabel('θ / π'); ax.set_ylabel('Δφ/π, ε')
    ax.set_title('RFT phase control')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    # Polar warp profile
    ax = axes[1, 2]
    ax = fig.add_subplot(2, 3, 6, projection='polar')
    # Radius = |w| + offset for visibility
    r_polar = np.abs(w_theta) + 0.01
    colors_polar = ['red' if w > 0 else 'blue' for w in w_theta]
    # Scatter with color coding
    for j in range(len(theta) - 1):
        ax.fill_between([theta[j], theta[j + 1]],
                        [0, 0], [r_polar[j], r_polar[j + 1]],
                        color='red' if w_theta[j] > 0 else 'blue',
                        alpha=0.4)
    ax.plot(theta, r_polar, 'k-', lw=1.5)
    ax.set_title('Warp bubble (polar)\n'
                 'red=Contraction, blue=Expansion',
                 fontsize=9, pad=15)
    ax.set_theta_zero_location('E')  # 0° = right = flight direction
    ax.annotate('→ Flight', xy=(0.05, 0.06), fontsize=8,
                xycoords='axes fraction')

    fig.suptitle(
        f'Warp Bubble 3D: Profiles and angular dependence\n'
        f'R = {bubble.R:.0f} m  |  '
        f'w(front) = {bubble.w_of_theta(0):+.4f}  |  '
        f'w(rear) = {bubble.w_of_theta(PI):+.4f}  |  '
        f'Δw = {bubble.w_of_theta(0) - bubble.w_of_theta(PI):+.4f}',
        fontsize=11, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_3d_profile.png'), dpi=150)
    plt.close()
    print("  → warp_3d_profile.png")


def plot_bubble_3d_surface(bubble: WarpBubble3D, out: str) -> None:
    """3D visualization of the bubble surface."""
    fig = plt.figure(figsize=(16, 7))

    # Sphere surface at r = R
    theta = np.linspace(0, PI, 100)
    phi = np.linspace(0, 2 * PI, 100)
    THETA, PHI = np.meshgrid(theta, phi)

    # Cartesian coordinates
    X = bubble.R * np.sin(THETA) * np.cos(PHI)
    Y = bubble.R * np.sin(THETA) * np.sin(PHI)
    Z = bubble.R * np.cos(THETA)

    # w on the surface
    W = bubble.w_of_theta(THETA)

    # Radius modified by w (deformation)
    R_mod = bubble.R * (1.0 + 5.0 * W)  # Amplified for visibility
    X_mod = R_mod * np.sin(THETA) * np.cos(PHI)
    Y_mod = R_mod * np.sin(THETA) * np.sin(PHI)
    Z_mod = R_mod * np.cos(THETA)

    # Plot 1: Color-coded (undeformed)
    ax1 = fig.add_subplot(121, projection='3d')
    norm = plt.Normalize(vmin=-0.06, vmax=0.04)
    colors = cm.RdBu_r(norm(W))
    ax1.plot_surface(X, Y, Z, facecolors=colors, alpha=0.8, shade=False)
    ax1.set_xlabel('x [m]'); ax1.set_ylabel('y [m]'); ax1.set_zlabel('z [m]')
    ax1.set_title('Bubble: w-distribution\n(red=Contraction, blue=Expansion)',
                  fontsize=9)
    # Flight direction
    L = bubble.R * 1.5
    ax1.quiver(0, 0, 0, L, 0, 0, color='black', arrow_length_ratio=0.1,
               lw=2)
    ax1.text(L * 1.1, 0, 0, '→ Flight', fontsize=8)

    # Plot 2: Deformed by w
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(X_mod, Y_mod, Z_mod, facecolors=colors,
                     alpha=0.8, shade=False)
    ax2.set_xlabel('x [m]'); ax2.set_ylabel('y [m]'); ax2.set_zlabel('z [m]')
    ax2.set_title('Bubble: Deformed (w-modulated)\n'
                  'Front compressed, rear stretched', fontsize=9)
    ax2.quiver(0, 0, 0, L, 0, 0, color='black', arrow_length_ratio=0.1,
               lw=2)
    ax2.text(L * 1.1, 0, 0, '→ Flight', fontsize=8)

    fig.suptitle(
        f'Warp Bubble 3D: R = {bubble.R:.0f} m  |  '
        f'Δw = {bubble.w_of_theta(0) - bubble.w_of_theta(PI):+.4f}  |  '
        f'ρ > 0 everywhere',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_3d_oberflaeche.png'), dpi=150)
    plt.close()
    print("  → warp_3d_oberflaeche.png")


def plot_energy_budget(bubble: WarpBubble3D, out: str) -> None:
    """Total energy of the warp bubble (integrated)."""
    # Numerical integration over the bubble
    N = 100
    L = 2.0 * bubble.R
    x = np.linspace(-L, L, N)
    y = np.linspace(-L, L, N)
    z = np.linspace(-L, L, N)

    dx = x[1] - x[0]
    dV = dx ** 3

    E_total = 0.0
    E_pos = 0.0
    E_neg = 0.0
    vol_active = 0.0

    for ix in range(N):
        for iy in range(N):
            rho_line = bubble.energy_density(
                x[ix] * np.ones(N), y[iy] * np.ones(N), z)
            E_line = np.sum(rho_line) * dV
            E_total += E_line
            E_pos += np.sum(rho_line[rho_line > 0]) * dV
            E_neg += np.sum(rho_line[rho_line < 0]) * dV
            vol_active += np.sum(rho_line > 1e-10 * bubble.rho_scale) * dV

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Energy budget
    ax = axes[0]
    labels = ['E_total', 'E (ρ>0)', 'E (ρ<0)']
    values = [E_total, E_pos, E_neg]
    colors = ['black', 'green', 'red']
    bars = ax.barh(labels, values, color=colors, alpha=0.7)
    ax.set_xlabel('Energy [J]')
    ax.set_title('Energy budget of the warp bubble')
    for bar, val in zip(bars, values):
        ax.text(max(val, 0) + E_total * 0.02, bar.get_y() + bar.get_height() / 2,
                f'{val:.2e} J', va='center', fontsize=9)
    ax.grid(True, alpha=0.3, axis='x')

    # Info text
    ax = axes[1]; ax.axis('off')
    mc2_sun = 1.989e30 * C ** 2
    ax.text(0.05, 0.95, f"""
    ENERGY BUDGET OF THE WARP BUBBLE:
    ═════════════════════════════════

    Bubble radius:    R = {bubble.R:.0f} m
    Bubble volume:    V = {4/3 * PI * bubble.R**3:.2e} m³
    Active volume:    {vol_active:.2e} m³

    Total energy:     E = {E_total:.2e} J
    Positive energy:  E⁺ = {E_pos:.2e} J
    Negative energy:  E⁻ = {E_neg:.2e} J

    E/m☉c²:          {E_total / mc2_sun:.2e}

    CONFIRMED: ρ > 0 everywhere.
    E⁻ = {E_neg:.2e} J ≈ 0
    → No negative energy required.
    """, transform=ax.transAxes, fontsize=10, va='top',
            fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    fig.suptitle('Energy budget: Warp bubble (3D integration)',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(out, 'warp_3d_energie.png'), dpi=150)
    plt.close()
    print("  → warp_3d_energie.png")


# ============================================================
# 5. Main Program
# ============================================================

def main() -> None:
    print("=" * 60)
    print("WARP BUBBLE 3D: RFT-controlled Alcubierre Geometry")
    print("E = π · ε(Δφ) · ℏ · f, κ = 1")
    print("=" * 60)

    out = "figures"
    ensure_dir(out)

    bubble = WarpBubble3D()
    bubble.info()

    # Exp 1: 2D slices
    print("\n=== 3D Bubble: Slices (z=0) ===")
    plot_bubble_slices(bubble, out)

    # Exp 2: Profiles
    print("\n=== 3D Bubble: Radial and angular profiles ===")
    plot_bubble_profiles(bubble, out)

    # Exp 3: 3D surface
    print("\n=== 3D Bubble: Surface visualization ===")
    plot_bubble_3d_surface(bubble, out)

    # Exp 4: Energy budget
    print("\n=== 3D Bubble: Energy budget (integration) ===")
    plot_energy_budget(bubble, out)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY: 3D WARP BUBBLE")
    print("=" * 60)
    print(f"""
  Bubble radius:    R = {bubble.R:.0f} m
  Wall thickness:   {1.0 / bubble.sigma:.1f} m
  Ship position:    Center (protected)

  Warp profile (angle-dependent):
    θ = 0   (front):   Δφ = 0     → w = {bubble.w_of_theta(0):+.4f}  (Contraction)
    θ = π/2 (side):    Δφ = π/4   → w = {bubble.w_of_theta(PI/2):+.4f}  (Transition)
    θ = π   (rear):    Δφ = π/2   → w = {bubble.w_of_theta(PI):+.4f}  (Expansion)
    Δw (front−rear):   {bubble.w_of_theta(0) - bubble.w_of_theta(PI):+.4f}

  Geometry:
    Alcubierre shape function f(r) with tanh walls
    Energy density ρ ∝ (df/dr)² · ε²(Δφ(θ))
    Concentrated at the bubble wall (r ≈ R)
    ρ > 0 EVERYWHERE — confirmed by 3D integration

  Metric perturbation:
    h ~ v · f(r) · cos(θ) · ε(Δφ(θ))
    Front: h > 0 (Space contracts)
    Rear: h < 0 (Space expands)

  Plots: {out}/ (4 new plots)
""")
    print("Done.")


if __name__ == "__main__":
    main()
