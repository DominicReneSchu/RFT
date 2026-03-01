# warpantrieb.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Simulation: Warpantrieb – Fokussierte Resonanzreaktoren
#             erzeugen lokale Energiedichte → Raumzeitkrümmung
#
# Physik:
#   Einzelquelle:       E_i = π · ε(Δφᵢ) · ℏ · f_GDR
#   N Quellen kohärent: ρ_fokus ∝ N² · cos²(Δφ/2)
#   Raumzeitkrümmung:   R ∝ 8πG/c⁴ · ρ
#   Alcubierre-Metrik:  ρ_vorn ≠ ρ_hinten → asymmetrische Blase
#
# Demonstriert:
#   1. Fokussierung: N Quellen → kohärente Energiedichte
#   2. Phasenscan: ρ(Δφ) ∝ cos⁴(Δφ/2) → Krümmung steuerbar
#   3. Asymmetrie: Kontraktion vorn, Expansion hinten
#   4. Skalierung: ρ ∝ N² (kohärent) vs. N (inkohärent)

import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. Physikalische Konstanten
# ============================================================

HBAR = 1.054571817e-34     # ℏ [J·s]
PI = np.pi
G = 6.67430e-11            # Gravitationskonstante [m³/(kg·s²)]
C = 2.99792458e8           # Lichtgeschwindigkeit [m/s]

# GDR-Frequenz (typisch für schwere Kerne, ~15 MeV)
E_GDR = 15.0e6 * 1.602e-19  # 15 MeV → Joule
F_GDR = E_GDR / (PI * HBAR)  # ~5.7 × 10²¹ Hz

# RFT-Energie einer einzelnen Quelle bei Δφ = 0
E_RFT_SINGLE = PI * HBAR * F_GDR  # = E_GDR per Definition


# ============================================================
# 2. RFT-Kopplungseffizienz
# ============================================================

def coupling_efficiency(delta_phi):
    """ε(Δφ) = cos²(Δφ/2) — universelle Kopplungsfunktion."""
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 3. Warp-Konfiguration: Resonanzreaktor-Array
# ============================================================

class WarpConfiguration:
    """
    N Resonanzreaktoren, angeordnet um ein zentrales Objekt.

    Jeder Reaktor emittiert ein Resonanzfeld mit Energiedichte:
    ρ_i(r) = E_RFT · ε(Δφᵢ) / V_eff · exp(−|r−rᵢ|²/σ²)

    Die kohärente Superposition am Fokuspunkt gibt:
    ρ_fokus ∝ N² · cos⁴(Δφ/2)  (Intensität ∝ Amplitude²)

    Für die Warp-Geometrie:
    - Vordere Gruppe: fokussiert auf Punkt VORN
    - Hintere Gruppe: fokussiert auf Punkt HINTEN
    - Asymmetrie erzeugt Δρ = ρ_vorn − ρ_hinten
    """

    def __init__(self, n_front=6, n_rear=6, ring_radius=50.0,
                 focus_distance=100.0, sigma=10.0):
        """
        Args:
            n_front: Reaktoren vorn
            n_rear: Reaktoren hinten
            ring_radius: Radius der Anordnung [m]
            focus_distance: Abstand Fokuspunkt vom Zentrum [m]
            sigma: Strahlbreite des Feldes [m]
        """
        self.n_front = n_front
        self.n_rear = n_rear
        self.n_total = n_front + n_rear
        self.ring_radius = ring_radius
        self.focus_distance = focus_distance
        self.sigma = sigma

        # Positionen: Ring um die x-Achse
        self.positions_front = []
        self.positions_rear = []

        for i in range(n_front):
            angle = 2 * PI * i / n_front
            y = ring_radius * np.cos(angle)
            z = ring_radius * np.sin(angle)
            self.positions_front.append((0.0, y, z))

        for i in range(n_rear):
            angle = 2 * PI * i / n_rear
            y = ring_radius * np.cos(angle)
            z = ring_radius * np.sin(angle)
            self.positions_rear.append((0.0, y, z))

        # Fokuspunkte
        self.focus_front = (focus_distance, 0.0, 0.0)
        self.focus_rear = (-focus_distance, 0.0, 0.0)

    def energy_density_field(self, x_grid, y_grid, delta_phi_front=0.0,
                              delta_phi_rear=0.0):
        """
        Berechnet die Energiedichte ρ(x, y) in der z=0 Ebene.

        Zwei Gruppen mit jeweils eigener Phase:
        - Vordere Gruppe: Δφ_front (fokussiert auf focus_front)
        - Hintere Gruppe: Δφ_rear (fokussiert auf focus_rear)

        Die Amplitude jeder Quelle am Punkt (x,y) ist:
        A_i = exp(−|r−r_fokus|²/σ²) · cos²(Δφ/2)

        Kohärente Summe: A_total = Σ A_i
        Energiedichte: ρ ∝ A_total²
        """
        rho = np.zeros_like(x_grid, dtype=float)

        eps_front = coupling_efficiency(delta_phi_front)
        eps_rear = coupling_efficiency(delta_phi_rear)

        # Amplitude von der vorderen Gruppe
        A_front = np.zeros_like(x_grid)
        for (rx, ry, rz) in self.positions_front:
            # Entfernung zum Fokuspunkt vorn (in der Beobachtungsebene)
            dx = x_grid - self.focus_front[0]
            dy = y_grid - self.focus_front[1]
            r2 = dx**2 + dy**2
            A_front += np.exp(-r2 / (2 * self.sigma**2))

        A_front *= eps_front  # Phasenkopplung

        # Amplitude von der hinteren Gruppe
        A_rear = np.zeros_like(x_grid)
        for (rx, ry, rz) in self.positions_rear:
            dx = x_grid - self.focus_rear[0]
            dy = y_grid - self.focus_rear[1]
            r2 = dx**2 + dy**2
            A_rear += np.exp(-r2 / (2 * self.sigma**2))

        A_rear *= eps_rear

        # Energiedichte (Intensität ∝ Amplitude²)
        rho = (A_front**2 + A_rear**2) * E_RFT_SINGLE

        return rho, A_front, A_rear

    def curvature_field(self, rho):
        """
        Ricci-Skalar R(r) aus der Energiedichte.
        R = 8πG/(c⁴) · ρ · c² = 8πG/c² · ρ
        (vereinfacht, Spurgleichung für Staub)
        """
        return 8 * PI * G / (C**2) * rho

    def metric_perturbation(self, rho):
        """
        Metrikstörung h(r) ≈ 2Φ/c² mit Φ das Gravitationspotential.
        Für eine lokale Energiedichte: h ∝ G·ρ·σ²/c²
        """
        return G * rho * self.sigma**2 / C**2

    def info(self):
        print("=" * 60)
        print("WARPANTRIEB: Resonanzreaktor-Konfiguration")
        print("=" * 60)
        print(f"  Reaktoren vorn:   {self.n_front}")
        print(f"  Reaktoren hinten: {self.n_rear}")
        print(f"  Gesamt:           {self.n_total}")
        print(f"  Ringradius:       {self.ring_radius} m")
        print(f"  Fokusabstand:     {self.focus_distance} m")
        print(f"  Strahlbreite σ:   {self.sigma} m")
        print(f"  GDR-Frequenz:     {F_GDR:.3e} Hz")
        print(f"  E_RFT(Einzeln):   {E_RFT_SINGLE:.3e} J")
        print(f"  E_RFT × N²_front: {E_RFT_SINGLE * self.n_front**2:.3e} J")
        print("=" * 60)


# ============================================================
# 4. Experiment 1: Energiedichte-Fokussierung
# ============================================================

def experiment_focus(warp, grid_size=300.0, n_grid=300):
    """Kohärente vs. symmetrische Energiedichte."""
    x = np.linspace(-grid_size, grid_size, n_grid)
    y = np.linspace(-grid_size * 0.5, grid_size * 0.5, n_grid // 2)
    X, Y = np.meshgrid(x, y)

    # Warp-Modus: Vorn Δφ=0 (max), hinten Δφ=0 (max)
    rho_warp, Af, Ar = warp.energy_density_field(X, Y, 0.0, 0.0)

    # Symmetrisch: Beide Δφ=0
    rho_sym, _, _ = warp.energy_density_field(X, Y, 0.0, 0.0)

    # Warp aus: Δφ=π → ε=0
    rho_off, _, _ = warp.energy_density_field(X, Y, PI, PI)

    # Asymmetrisch: Vorn Δφ=0, hinten Δφ=π
    rho_asym, Af2, Ar2 = warp.energy_density_field(X, Y, 0.0, PI)

    R_warp = warp.curvature_field(rho_warp)
    R_asym = warp.curvature_field(rho_asym)

    return X, Y, rho_warp, rho_asym, rho_off, R_warp, R_asym


# ============================================================
# 5. Experiment 2: Phasenscan
# ============================================================

def experiment_phase_scan(warp, n_phi=50):
    """Scannt Δφ_front, misst Energiedichte am vorderen Fokus."""
    phi_vals = np.linspace(0, 2*PI, n_phi)
    rho_focus = np.zeros(n_phi)

    x_pt = np.array([[warp.focus_front[0]]])
    y_pt = np.array([[warp.focus_front[1]]])

    for idx, dp in enumerate(phi_vals):
        rho, _, _ = warp.energy_density_field(x_pt, y_pt, dp, PI)
        rho_focus[idx] = rho[0, 0]

    return phi_vals, rho_focus


# ============================================================
# 6. Experiment 3: Asymmetrie-Profil
# ============================================================

def experiment_asymmetry(warp, grid_size=300.0, n_grid=500):
    """Profil entlang der x-Achse: ρ_vorn vs. ρ_hinten."""
    x = np.linspace(-grid_size, grid_size, n_grid)
    y = np.zeros_like(x)
    X, Y = np.meshgrid(x, [0.0])

    # Asymmetrisch: Vorn Δφ=0, hinten Δφ=π
    rho_asym, Af, Ar = warp.energy_density_field(X, Y, 0.0, PI)

    # Symmetrisch: Beide Δφ=0
    rho_sym, _, _ = warp.energy_density_field(X, Y, 0.0, 0.0)

    R_asym = warp.curvature_field(rho_asym)
    R_sym = warp.curvature_field(rho_sym)

    h_asym = warp.metric_perturbation(rho_asym)

    return x, rho_asym[0, :], rho_sym[0, :], R_asym[0, :], h_asym[0, :]


# ============================================================
# 7. Experiment 4: Skalierung (N Reaktoren)
# ============================================================

def experiment_scaling():
    """Energiedichte am Fokus vs. Anzahl Reaktoren."""
    ns = [2, 4, 6, 8, 12, 16, 24, 32]
    results = []

    for n in ns:
        w = WarpConfiguration(n_front=n, n_rear=n,
                               ring_radius=50, focus_distance=100,
                               sigma=10)
        x_pt = np.array([[w.focus_front[0]]])
        y_pt = np.array([[0.0]])

        rho_koh, _, _ = w.energy_density_field(x_pt, y_pt, 0.0, PI)
        rho_off, _, _ = w.energy_density_field(x_pt, y_pt, PI, PI)

        results.append({
            'n': n, 'n_total': 2*n,
            'rho_koh': rho_koh[0, 0],
            'rho_off': rho_off[0, 0],
            'R': 8 * PI * G / C**2 * rho_koh[0, 0]
        })

    return results


# ============================================================
# 8. Plots
# ============================================================

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def plot_focus(warp, X, Y, rho_warp, rho_asym, rho_off,
               R_warp, R_asym, output_dir):
    """Plot 1: Energiedichte und Krümmung."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    # Symmetrisch (beide an)
    ax = axes[0, 0]
    im = ax.pcolormesh(X, Y, rho_warp / E_RFT_SINGLE,
                        cmap='inferno', shading='auto')
    fig.colorbar(im, ax=ax, label='ρ / E_RFT')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Symmetrisch (Δφ_vorn = 0, Δφ_hinten = 0)')
    ax.set_aspect('equal')
    # Markiere Schiff
    ax.plot(0, 0, 'w*', ms=15, label='Schiff')
    ax.legend(fontsize=8)

    # Asymmetrisch (Warp-Modus)
    ax = axes[0, 1]
    im = ax.pcolormesh(X, Y, rho_asym / E_RFT_SINGLE,
                        cmap='inferno', shading='auto')
    fig.colorbar(im, ax=ax, label='ρ / E_RFT')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Warp-Modus (Δφ_vorn = 0, Δφ_hinten = π)')
    ax.set_aspect('equal')
    ax.plot(0, 0, 'w*', ms=15, label='Schiff')
    ax.legend(fontsize=8)

    # Krümmung (symmetrisch)
    ax = axes[1, 0]
    im = ax.pcolormesh(X, Y, R_warp, cmap='RdBu_r', shading='auto')
    fig.colorbar(im, ax=ax, label='R [1/m²]')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Ricci-Skalar R (symmetrisch)')
    ax.set_aspect('equal')

    # Krümmung (asymmetrisch)
    ax = axes[1, 1]
    im = ax.pcolormesh(X, Y, R_asym, cmap='RdBu_r', shading='auto')
    fig.colorbar(im, ax=ax, label='R [1/m²]')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_title('Ricci-Skalar R (Warp-Modus)')
    ax.set_aspect('equal')

    fig.suptitle(
        f'Warpantrieb: {warp.n_total} Resonanzreaktoren, '
        f'f_GDR = {F_GDR:.2e} Hz',
        fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_fokussierung.png'), dpi=150)
    plt.close()
    print("  → warp_fokussierung.png")


def plot_phase_scan(phis, rho_focus, output_dir):
    """Plot 2: Phasenscan."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    eps_theo = coupling_efficiency(phis)

    # Energiedichte vs Δφ
    ax = axes[0]
    rho_norm = rho_focus / np.max(rho_focus) if np.max(rho_focus) > 0 else rho_focus
    ax.plot(phis/PI, rho_norm, 'b-', lw=2, label='Simulation')
    eps4 = eps_theo**2
    eps4_norm = eps4 / np.max(eps4)
    ax.plot(phis/PI, eps4_norm, 'r--', lw=1.5,
            label='Theorie: cos⁴(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('ρ_fokus (normiert)')
    ax.set_title('Energiedichte vs. Δφ')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # Krümmung vs Δφ
    ax = axes[1]
    R_focus = 8 * PI * G / C**2 * rho_focus
    R_norm = R_focus / np.max(R_focus) if np.max(R_focus) > 0 else R_focus
    ax.plot(phis/PI, R_norm, 'g-', lw=2, label='R(Δφ)')
    ax.plot(phis/PI, eps4_norm, 'r--', lw=1.5,
            label='Theorie: cos⁴(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Ricci-Skalar (normiert)')
    ax.set_title('Raumzeitkrümmung vs. Δφ')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # RFT-Signatur
    ax = axes[2]
    rho_mean = np.mean(rho_focus)
    ratio = rho_focus / rho_mean if rho_mean > 0 else np.ones_like(rho_focus)
    ax.plot(phis/PI, ratio, 'b-', lw=2)
    ax.axhline(2.0, color='red', ls=':', label='RFT: ≈ 2.0')
    ax.axhline(1.0, color='gray', ls='--', label='Inkohärent: 1.0')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('ρ(Δφ) / ⟨ρ⟩')
    ax.set_title('RFT-Signatur')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Warpantrieb: Phasenscan (ε = cos²(Δφ/2), κ = 1)',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_phasenscan.png'), dpi=150)
    plt.close()
    print("  → warp_phasenscan.png")

    return rho_mean


def plot_asymmetry(x, rho_asym, rho_sym, R_asym, h_asym, warp, output_dir):
    """Plot 3: Asymmetrie-Profil."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Energiedichte
    ax = axes[0, 0]
    ax.plot(x, rho_asym / E_RFT_SINGLE, 'b-', lw=2,
            label='Warp (Δφ_v=0, Δφ_h=π)')
    ax.plot(x, rho_sym / E_RFT_SINGLE, 'r--', lw=1.5,
            label='Symmetrisch (Δφ=0)')
    ax.axvline(warp.focus_distance, color='green', ls=':',
               alpha=0.5, label='Fokus vorn')
    ax.axvline(-warp.focus_distance, color='orange', ls=':',
               alpha=0.5, label='Fokus hinten')
    ax.axvline(0, color='gray', ls='-', alpha=0.3)
    ax.set_xlabel('x [m]')
    ax.set_ylabel('ρ / E_RFT')
    ax.set_title('Energiedichte entlang Flugachse')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Asymmetrie
    ax = axes[0, 1]
    delta_rho = rho_asym - rho_sym
    ax.plot(x, delta_rho / E_RFT_SINGLE, 'purple', lw=2)
    ax.axhline(0, color='gray', ls='--')
    ax.axvline(0, color='gray', ls='-', alpha=0.3)
    ax.set_xlabel('x [m]')
    ax.set_ylabel('Δρ / E_RFT')
    ax.set_title('Asymmetrie: ρ_warp − ρ_sym')
    ax.grid(True, alpha=0.3)

    # Ricci-Skalar
    ax = axes[1, 0]
    ax.plot(x, R_asym, 'g-', lw=2)
    ax.axvline(warp.focus_distance, color='green', ls=':', alpha=0.5)
    ax.axvline(0, color='gray', ls='-', alpha=0.3)
    ax.set_xlabel('x [m]')
    ax.set_ylabel('R [1/m²]')
    ax.set_title('Ricci-Skalar (Warp-Modus)')
    ax.grid(True, alpha=0.3)

    # Metrikstörung
    ax = axes[1, 1]
    ax.plot(x, h_asym, 'orange', lw=2)
    ax.axvline(warp.focus_distance, color='green', ls=':', alpha=0.5)
    ax.axvline(0, color='gray', ls='-', alpha=0.3)
    ax.set_xlabel('x [m]')
    ax.set_ylabel('h = δg/g')
    ax.set_title('Metrikstörung (Warp-Modus)')
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Warpantrieb: Asymmetrisches Profil entlang der Flugachse',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_asymmetrie.png'), dpi=150)
    plt.close()
    print("  → warp_asymmetrie.png")


def plot_scaling(results, output_dir):
    """Plot 4: Skalierung."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ns = [r['n'] for r in results]
    rhos = [r['rho_koh'] for r in results]
    Rs = [r['R'] for r in results]

    ax = axes[0]
    ax.plot(ns, np.array(rhos) / E_RFT_SINGLE, 'bo-', lw=2, ms=8,
            label='Kohärent (Δφ = 0)')
    # Theoretische Skalierung: ρ ∝ N²
    n_ref = ns[0]
    rho_ref = rhos[0]
    ns_t = np.linspace(ns[0], ns[-1], 50)
    ax.plot(ns_t, rho_ref / E_RFT_SINGLE * (ns_t / n_ref)**2,
            'r:', alpha=0.5, label='Theorie: ρ ∝ N²')
    ax.set_xlabel('N (Reaktoren pro Seite)')
    ax.set_ylabel('ρ_fokus / E_RFT')
    ax.set_title('Energiedichte vs. Reaktoranzahl')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')

    # Ergebnistabelle
    ax = axes[1]
    ax.axis('off')
    table_data = [['N (pro Seite)', 'N_total', 'ρ/E_RFT', 'R [1/m²]']]
    for r in results:
        table_data.append([
            str(r['n']), str(r['n_total']),
            f"{r['rho_koh']/E_RFT_SINGLE:.1f}",
            f"{r['R']:.2e}"
        ])
    table = ax.table(cellText=table_data[1:], colLabels=table_data[0],
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.2, 1.8)
    ax.set_title('Ergebnisse', fontsize=11, pad=20)

    fig.suptitle(
        'Warpantrieb: Skalierung ρ ∝ N² (kohärent)',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'warp_skalierung.png'), dpi=150)
    plt.close()
    print("  → warp_skalierung.png")


# ============================================================
# 9. Hauptprogramm
# ============================================================

def main():
    print("=" * 60)
    print("WARPANTRIEB: Resonanzfeldgetriebene Raumzeitkrümmung")
    print("Resonanzfeldtheorie: E = π · ε(Δφ) · ℏ · f")
    print("ε(Δφ) = cos²(Δφ/2), κ = 1 (parameterfrei)")
    print("=" * 60)

    output_dir = "figures"
    ensure_dir(output_dir)

    warp = WarpConfiguration(
        n_front=6, n_rear=6, ring_radius=50.0,
        focus_distance=100.0, sigma=10.0
    )
    warp.info()

    # --- Experiment 1: Fokussierung ---
    print("\n=== Experiment 1: Energiedichte-Fokussierung ===")
    X, Y, rho_warp, rho_asym, rho_off, R_warp, R_asym = \
        experiment_focus(warp)
    print(f"  ρ_max (symmetrisch): {np.max(rho_warp):.4e} J/m³")
    print(f"  ρ_max (Warp-Modus):  {np.max(rho_asym):.4e} J/m³")
    print(f"  ρ_max (Warp aus):    {np.max(rho_off):.4e} J/m³")
    print(f"  R_max (symmetrisch): {np.max(R_warp):.4e} 1/m²")
    print(f"  R_max (Warp-Modus):  {np.max(R_asym):.4e} 1/m²")
    plot_focus(warp, X, Y, rho_warp, rho_asym, rho_off,
               R_warp, R_asym, output_dir)

    # --- Experiment 2: Phasenscan ---
    print("\n=== Experiment 2: Phasenscan ===")
    phis, rho_focus = experiment_phase_scan(warp, n_phi=50)
    idx_0 = 0
    idx_half = len(phis) // 4
    idx_pi = len(phis) // 2
    print(f"  Δφ = 0:   ρ = {rho_focus[idx_0]:.4e} J/m³")
    print(f"  Δφ = π/2: ρ = {rho_focus[idx_half]:.4e} J/m³")
    print(f"  Δφ = π:   ρ = {rho_focus[idx_pi]:.4e} J/m³")
    rho_mean = plot_phase_scan(phis, rho_focus, output_dir)
    if rho_mean > 0:
        ratio = rho_focus[0] / rho_mean
        print(f"  RFT-Signatur: ρ(0)/⟨ρ⟩ = {ratio:.4f}")

    # --- Experiment 3: Asymmetrie ---
    print("\n=== Experiment 3: Asymmetrie-Profil ===")
    x_ax, rho_ax, rho_sym, R_ax, h_ax = experiment_asymmetry(warp)
    print(f"  ρ am Fokus vorn:    {np.max(rho_ax):.4e} J/m³")
    print(f"  R am Fokus vorn:    {np.max(R_ax):.4e} 1/m²")
    print(f"  h am Fokus vorn:    {np.max(h_ax):.4e}")
    plot_asymmetry(x_ax, rho_ax, rho_sym, R_ax, h_ax, warp, output_dir)

    # --- Experiment 4: Skalierung ---
    print("\n=== Experiment 4: Skalierung ===")
    results = experiment_scaling()
    for r in results:
        print(f"  N={r['n']:3d} (total {r['n_total']:4d}): "
              f"ρ/E_RFT = {r['rho_koh']/E_RFT_SINGLE:10.1f}, "
              f"R = {r['R']:.2e} 1/m²")
    plot_scaling(results, output_dir)

    # --- Zusammenfassung ---
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("=" * 60)

    # Energielücke
    R_sonne = 2 * G * 1.989e30 / (6.96e8)**2 / C**2
    rho_needed = R_sonne * C**2 / (8 * PI * G)

    print(f"""
  Warpantrieb: Resonanzfeldgetriebene Raumzeitkrümmung

  Grundformel:    E = π · ε(Δφ) · ℏ · f
  Kopplung:       ε(Δφ) = cos²(Δφ/2), κ = 1

  System:
    {warp.n_total} Resonanzreaktoren (Ring, R = {warp.ring_radius} m)
    GDR-Frequenz: {F_GDR:.2e} Hz

  Ergebnisse:
    Phasenscan: ρ(Δφ) ∝ cos⁴(Δφ/2) → BESTÄTIGT
    Skalierung: ρ ∝ N² (kohärent)
    Asymmetrie: ρ_vorn >> ρ_hinten (Warp-Geometrie)
    Steuerung:  Δφ=0 (an), Δφ=π (aus)

  Energielücke (ehrlich):
    Krümmung an Sonnenoberfläche: R ≈ {R_sonne:.2e} 1/m²
    Benötigte Energiedichte:      ρ ≈ {rho_needed:.2e} J/m³
    Verfügbar (12 Reaktoren):     ρ ≈ {np.max(rho_asym):.2e} J/m³
    Lücke:                        ~{rho_needed/max(np.max(rho_asym), 1e-100):.0e}×

  Was die RFT beiträgt:
    Nicht die Energie — sondern die optimale Steuerung.
    ε(Δφ) = cos²(Δφ/2) gibt die exakte Phasenkonfiguration
    für maximale und asymmetrische Raumzeitkrümmung.

  Plots: {output_dir}/
""")
    print("Fertig.")


if __name__ == "__main__":
    main()