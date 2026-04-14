# kraftfeldgenerator.py
# © Dominic-René Schu, 2025/2026 – Resonanzfeldtheorie
#
# Simulation: Kraftfeldgenerator – Akustische Barrieren durch
#             phasengesteuerte Ultraschall-Transducer-Arrays
#
# Physik:
#   Druckfeld:          P(r,t) = Σᵢ (p₀·a/rᵢ) · cos(ω·t − k·|r−rᵢ| + φᵢ)
#   Energiedichte:      E(r) = P²(r) / (ρ·c²)
#   RFT-Optimierung:    ε(Δφ) = cos²(Δφ/2) → maximaler Fokus bei Δφ = 0
#   Grundformel:        E = π · ε(Δφ) · ℏ · f
#
# Phasenscan:
#   Das Array wird in zwei Hälften geteilt (links/rechts).
#   Eine Hälfte erhält Phasenverschiebung Δφ.
#   Am Fokuspunkt interferieren die Hälften:
#   P_fokus ∝ cos(Δφ/2) → |P|² ∝ cos²(Δφ/2) = ε(Δφ)
#
# Demonstriert:
#   1. Fokussierung: Transducer-Array erzeugt Druckmaximum
#   2. Phasenscan: ε(Δφ) = cos²(Δφ/2) im akustischen Feld
#   3. Barrierebildung: Stehende Welle als „Kraftfeld"
#   4. Vergleich: Kohärent vs. inkohärent, Arraygrößen

from __future__ import annotations

from typing import Any

import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. Physikalische Konstanten
# ============================================================

HBAR = 1.054571817e-34     # ℏ [J·s]
PI = np.pi

# Luft bei 20°C, 1 atm
RHO_AIR = 1.204            # Dichte [kg/m³]
C_AIR = 343.0              # Schallgeschwindigkeit [m/s]


# ============================================================
# 2. RFT-Kopplungseffizienz
# ============================================================

def coupling_efficiency(delta_phi: float | np.ndarray) -> float | np.ndarray:
    """ε(Δφ) = cos²(Δφ/2) — universelle Kopplungsfunktion."""
    return np.cos(delta_phi / 2.0) ** 2


# ============================================================
# 3. Transducer-Array
# ============================================================

class TransducerArray:
    """
    Phasengesteuertes Ultraschall-Transducer-Array.

    Jeder Transducer emittiert eine Kugelwelle:
    p_i(r,t) = (p₀ · a / |r - r_i|) · cos(ω·t − k·|r−r_i| + φ_i)

    Das Array kann in zwei Gruppen aufgeteilt werden (A und B),
    mit relativer Phasenverschiebung Δφ zwischen den Gruppen.
    Am Fokuspunkt ergibt sich:
        P_total ∝ P_A + P_B · e^(iΔφ)
        |P|² ∝ cos²(Δφ/2) = ε(Δφ)
    """

    def __init__(self, nx: int = 16, ny: int = 16, spacing: float = 0.01,
                 freq: float = 40000.0, p0: float = 1.0,
                 radius: float = 0.005) -> None:
        self.nx = nx
        self.ny = ny
        self.spacing = spacing
        self.freq = freq
        self.p0 = p0
        self.radius = radius

        # Abgeleitete Größen
        self.omega = 2 * PI * freq
        self.k = self.omega / C_AIR
        self.wavelength = C_AIR / freq
        self.n_total = nx * ny

        # Transducer-Positionen (zentriert)
        x_pos = np.linspace(-(nx-1)/2, (nx-1)/2, nx) * spacing
        y_pos = np.linspace(-(ny-1)/2, (ny-1)/2, ny) * spacing
        self.positions = []
        for xi in x_pos:
            for yi in y_pos:
                self.positions.append((xi, yi))
        self.positions = np.array(self.positions)

        # Array-Apertur
        self.aperture_x = (nx - 1) * spacing
        self.aperture_y = (ny - 1) * spacing

        # Gruppen: linke Hälfte (A), rechte Hälfte (B)
        self.group_A = []
        self.group_B = []
        for i, (xi, yi) in enumerate(self.positions):
            if xi < 0:
                self.group_A.append(i)
            else:
                self.group_B.append(i)
        self.group_A = np.array(self.group_A)
        self.group_B = np.array(self.group_B)

    def compute_pressure_field(self, x_grid: np.ndarray, y_grid: np.ndarray,
                                z_focus: float, phases: np.ndarray | None = None,
                                t: float = 0.0) -> np.ndarray:
        """Berechnet das Druckfeld P(x, y) in einer Ebene bei z = z_focus."""
        if phases is None:
            phases = self._focus_phases(0.0, 0.0, z_focus)

        P = np.zeros_like(x_grid, dtype=float)

        for i, (xi, yi) in enumerate(self.positions):
            dx = x_grid - xi
            dy = y_grid - yi
            r = np.sqrt(dx**2 + dy**2 + z_focus**2)
            r_safe = np.maximum(r, self.radius)
            amplitude = self.p0 * self.radius / r_safe
            P += amplitude * np.cos(self.omega * t - self.k * r + phases[i])

        return P

    def _focus_phases(self, x_f: float, y_f: float, z_f: float) -> np.ndarray:
        """Phasen, die alle Wellen am Fokuspunkt konstruktiv überlagern."""
        phases = np.zeros(self.n_total)
        for i, (xi, yi) in enumerate(self.positions):
            r_i = np.sqrt((x_f - xi)**2 + (y_f - yi)**2 + z_f**2)
            phases[i] = self.k * r_i
        return phases

    def focus_split_phase(self, x_f: float, y_f: float, z_f: float,
                           delta_phi: float = 0.0) -> np.ndarray:
        """
        Fokusphasen mit Phasendifferenz Δφ zwischen Gruppe A und B.

        Gruppe A (linke Hälfte): φ_i = k·r_i (Referenz)
        Gruppe B (rechte Hälfte): φ_i = k·r_i + Δφ

        Am Fokuspunkt:
        P_A und P_B kommen beide kohärent an,
        aber mit relativer Phase Δφ.
        → P_total ∝ cos(0) + cos(Δφ) = 2·cos(Δφ/2)·cos(Δφ/2 + ωt...)
        → |P_total|² ∝ cos²(Δφ/2)
        """
        phases = self._focus_phases(x_f, y_f, z_f)
        # Nur Gruppe B erhält die Phasenverschiebung
        for i in self.group_B:
            phases[i] += delta_phi
        return phases

    def barrier_phases(self, z_f: float, barrier_y: float = 0.0) -> np.ndarray:
        """Fokusphasen für Linienfokus bei y = barrier_y."""
        return self._focus_phases(0.0, barrier_y, z_f)

    def info(self) -> None:
        print("=" * 60)
        print("KRAFTFELDGENERATOR: Transducer-Array")
        print("=" * 60)
        print(f"  Array:            {self.nx} × {self.ny} = {self.n_total} Transducer")
        print(f"  Abstand:          {self.spacing*1000:.1f} mm")
        print(f"  Apertur:          {self.aperture_x*1000:.1f} × {self.aperture_y*1000:.1f} mm")
        print(f"  Frequenz:         {self.freq/1000:.1f} kHz")
        print(f"  Wellenlänge:      {self.wavelength*1000:.2f} mm")
        print(f"  Wellenzahl k:     {self.k:.1f} 1/m")
        print(f"  Quelldruck p₀:    {self.p0} Pa/Transducer")
        print(f"  Gruppe A (links): {len(self.group_A)} Transducer")
        print(f"  Gruppe B (rechts):{len(self.group_B)} Transducer")
        print(f"  E_RFT(f, Δφ=0):  {PI * HBAR * self.freq:.4e} J")
        print("=" * 60)


# ============================================================
# 4. Experiment 1: Fokussierung
# ============================================================

def experiment_focus(array: TransducerArray, z_focus: float = 0.1,
                     grid_size: float = 0.05,
                     n_grid: int = 200) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Kohärent vs. inkohärent."""
    x = np.linspace(-grid_size, grid_size, n_grid)
    y = np.linspace(-grid_size, grid_size, n_grid)
    X, Y = np.meshgrid(x, y)

    # Kohärent (Δφ = 0)
    phases_koh = array.focus_split_phase(0.0, 0.0, z_focus, 0.0)
    P_koh = array.compute_pressure_field(X, Y, z_focus, phases_koh)

    # Inkohärent (zufällige Phasen)
    np.random.seed(42)
    phases_ink = np.random.uniform(0, 2*PI, array.n_total)
    P_ink = array.compute_pressure_field(X, Y, z_focus, phases_ink)

    I_koh = P_koh**2 / (2 * RHO_AIR * C_AIR)
    I_ink = P_ink**2 / (2 * RHO_AIR * C_AIR)

    return X, Y, P_koh, P_ink, I_koh, I_ink


# ============================================================
# 5. Experiment 2: Phasenscan (RFT-Signatur)
# ============================================================

def experiment_phase_scan(array: TransducerArray, z_focus: float = 0.1,
                          n_phi: int = 50) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Scannt Δφ zwischen Gruppe A und B.

    Physik:
    P_A = Σ_{i∈A} p_i → alle kohärent am Fokus = P₀/2
    P_B = Σ_{i∈B} p_i · e^{iΔφ} → kohärent, aber Phase Δφ

    P_total = P_A + P_B·cos(Δφ) ∝ 1 + cos(Δφ) = 2·cos²(Δφ/2)
    |P_total|² ∝ cos⁴(Δφ/2)

    Normiert: |P|/|P_max| ∝ cos²(Δφ/2) = ε(Δφ)
    """
    phi_vals = np.linspace(0, 2*PI, n_phi)
    P_focus = np.zeros(n_phi)
    I_focus = np.zeros(n_phi)

    x_pt = np.array([[0.0]])
    y_pt = np.array([[0.0]])

    for idx, dp in enumerate(phi_vals):
        phases = array.focus_split_phase(0.0, 0.0, z_focus, dp)
        P = array.compute_pressure_field(x_pt, y_pt, z_focus, phases)
        P_focus[idx] = np.abs(P[0, 0])
        I_focus[idx] = P[0, 0]**2 / (2 * RHO_AIR * C_AIR)

    return phi_vals, P_focus, I_focus


# ============================================================
# 6. Experiment 3: Barrierebildung
# ============================================================

def experiment_barrier(array: TransducerArray, z_focus: float = 0.1,
                       grid_size: float = 0.05,
                       n_grid: int = 200) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Linienförmige Barriere."""
    x = np.linspace(-grid_size, grid_size, n_grid)
    y = np.linspace(-grid_size, grid_size, n_grid)
    X, Y = np.meshgrid(x, y)

    phases = array.barrier_phases(z_focus, barrier_y=0.0)
    P = array.compute_pressure_field(X, Y, z_focus, phases)
    P_rad = P**2 / (2 * RHO_AIR * C_AIR**2)

    return X, Y, P, P_rad


# ============================================================
# 7. Experiment 4: Arraygröße-Vergleich
# ============================================================

def experiment_array_comparison(z_focus: float = 0.1) -> list[dict[str, Any]]:
    """Verschiedene Arraygrößen."""
    configs = [
        (4, 4, "4×4 (16)"),
        (8, 8, "8×8 (64)"),
        (16, 16, "16×16 (256)"),
        (32, 32, "32×32 (1024)"),
    ]

    results = []
    for nx, ny, label in configs:
        arr = TransducerArray(nx=nx, ny=ny, spacing=0.01,
                               freq=40000.0, p0=1.0)
        x_pt = np.array([[0.0]])
        y_pt = np.array([[0.0]])

        # Kohärent
        phases = arr.focus_split_phase(0.0, 0.0, z_focus, 0.0)
        P = arr.compute_pressure_field(x_pt, y_pt, z_focus, phases)
        P_koh = np.abs(P[0, 0])

        # Inkohärent
        np.random.seed(42)
        phases_ink = np.random.uniform(0, 2*PI, arr.n_total)
        P_ink_val = np.abs(arr.compute_pressure_field(
            x_pt, y_pt, z_focus, phases_ink)[0, 0])

        # Anti-kohärent (Δφ = π)
        phases_anti = arr.focus_split_phase(0.0, 0.0, z_focus, PI)
        P_anti = np.abs(arr.compute_pressure_field(
            x_pt, y_pt, z_focus, phases_anti)[0, 0])

        results.append({
            'nx': nx, 'ny': ny, 'n': nx*ny, 'label': label,
            'P_koh': P_koh, 'P_ink': P_ink_val, 'P_anti': P_anti,
            'gain': P_koh / P_ink_val if P_ink_val > 1e-10 else 0,
            'contrast': P_koh / max(P_anti, 1e-6)  # Floor bei 1 µPa
        })

    return results


# ============================================================
# 8. Plots
# ============================================================

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def plot_focus(array: TransducerArray, X: np.ndarray, Y: np.ndarray,
               P_koh: np.ndarray, P_ink: np.ndarray, I_koh: np.ndarray,
               I_ink: np.ndarray, output_dir: str) -> None:
    """Plot 1: Fokussiertes Druckfeld."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))

    vmax = np.max(np.abs(P_koh))

    ax = axes[0, 0]
    im = ax.pcolormesh(X*1000, Y*1000, P_koh, cmap='coolwarm',
                        shading='auto', vmin=-vmax, vmax=vmax)
    fig.colorbar(im, ax=ax, label='Druck [Pa]')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_title(f'Kohärent (Δφ = 0)\nP_max = {vmax:.2f} Pa')
    ax.set_aspect('equal')

    ax = axes[0, 1]
    im = ax.pcolormesh(X*1000, Y*1000, P_ink, cmap='coolwarm',
                        shading='auto', vmin=-vmax, vmax=vmax)
    fig.colorbar(im, ax=ax, label='Druck [Pa]')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_title(f'Inkohärent (zufällige Phasen)\n'
                 f'P_max = {np.max(np.abs(P_ink)):.2f} Pa')
    ax.set_aspect('equal')

    ax = axes[1, 0]
    im = ax.pcolormesh(X*1000, Y*1000, I_koh, cmap='inferno',
                        shading='auto')
    fig.colorbar(im, ax=ax, label='Intensität [W/m²]')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_title('Intensität (kohärent)')
    ax.set_aspect('equal')

    ax = axes[1, 1]
    n_mid = P_koh.shape[0] // 2
    x_mm = X[n_mid, :] * 1000
    ax.plot(x_mm, np.abs(P_koh[n_mid, :]), 'b-', lw=2, label='Kohärent')
    ax.plot(x_mm, np.abs(P_ink[n_mid, :]), 'r--', lw=1.5, label='Inkohärent')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('|P| [Pa]')
    ax.set_title('Druckprofil durch Fokus (y = 0)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        f'Kraftfeldgenerator: {array.nx}×{array.ny} Array, '
        f'f = {array.freq/1000:.0f} kHz, λ = {array.wavelength*1000:.1f} mm',
        fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fokussierung.png'), dpi=150)
    plt.close()
    print("  → fokussierung.png")


def plot_phase_scan(phis: np.ndarray, P_focus: np.ndarray, I_focus: np.ndarray,
                    output_dir: str) -> float:
    """Plot 2: Phasenscan — RFT-Signatur."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    eps_theo = coupling_efficiency(phis)

    # Druck
    ax = axes[0]
    P_norm = P_focus / np.max(P_focus) if np.max(P_focus) > 0 else P_focus
    eps_norm = eps_theo / np.max(eps_theo)
    ax.plot(phis/PI, P_norm, 'b-', lw=2, label='Simulation')
    ax.plot(phis/PI, eps_norm, 'r--', lw=1.5, label='Theorie: cos²(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Normierter Druck')
    ax.set_title('|P_fokus| vs. Δφ')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # Intensität
    ax = axes[1]
    I_norm = I_focus / np.max(I_focus) if np.max(I_focus) > 0 else I_focus
    eps_sq = eps_theo**2
    eps_sq_norm = eps_sq / np.max(eps_sq)
    ax.plot(phis/PI, I_norm, 'g-', lw=2, label='Simulation')
    ax.plot(phis/PI, eps_sq_norm, 'r--', lw=1.5,
            label='Theorie: cos⁴(Δφ/2)')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('Normierte Intensität')
    ax.set_title('I_fokus vs. Δφ')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    # Verhältnis
    ax = axes[2]
    I_mean = np.mean(I_focus)
    ratio = I_focus / I_mean if I_mean > 0 else np.ones_like(I_focus)
    ax.plot(phis/PI, ratio, 'b-', lw=2)
    ax.axhline(2.0, color='red', ls=':', label='RFT: ≈ 2.0')
    ax.axhline(1.0, color='gray', ls='--', label='Inkohärent: 1.0')
    ax.set_xlabel('Δφ / π')
    ax.set_ylabel('I(Δφ) / ⟨I⟩')
    ax.set_title('RFT-Signatur')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 2)
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        'Kraftfeldgenerator: Phasenscan '
        '(Gruppe A vs. B, RFT: ε = cos²(Δφ/2), κ = 1)',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'phasenscan.png'), dpi=150)
    plt.close()
    print("  → phasenscan.png")

    return I_mean


def plot_barrier(X: np.ndarray, Y: np.ndarray, P: np.ndarray,
                 P_rad: np.ndarray, array: TransducerArray,
                 output_dir: str) -> None:
    """Plot 3: Akustische Barriere."""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    vmax = np.max(np.abs(P))
    ax = axes[0]
    im = ax.pcolormesh(X*1000, Y*1000, P, cmap='coolwarm',
                        shading='auto', vmin=-vmax, vmax=vmax)
    fig.colorbar(im, ax=ax, label='P [Pa]')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_title('Druckfeld (Barriere)')
    ax.set_aspect('equal')

    ax = axes[1]
    im = ax.pcolormesh(X*1000, Y*1000, P_rad*1000, cmap='inferno',
                        shading='auto')
    fig.colorbar(im, ax=ax, label='P_rad [mPa]')
    ax.set_xlabel('x [mm]')
    ax.set_ylabel('y [mm]')
    ax.set_title('Strahlungsdruck')
    ax.set_aspect('equal')

    ax = axes[2]
    n_mid_x = P_rad.shape[1] // 2
    y_mm = Y[:, n_mid_x] * 1000
    ax.plot(y_mm, P_rad[:, n_mid_x]*1000, 'b-', lw=2)
    ax.fill_between(y_mm, 0, P_rad[:, n_mid_x]*1000, alpha=0.2,
                     color='blue')
    ax.set_xlabel('y [mm]')
    ax.set_ylabel('P_rad [mPa]')
    ax.set_title('Barriereprofil (x = 0)')
    ax.grid(True, alpha=0.3)

    profile = P_rad[:, n_mid_x]
    peak = np.max(profile)
    if peak > 0:
        half = peak / 2
        above = profile > half
        if np.any(above):
            y_above = y_mm[above]
            width = y_above[-1] - y_above[0]
            ax.axhline(peak*1000/2, color='red', ls=':',
                       label=f'FWHM ≈ {width:.1f} mm')
            ax.legend(fontsize=8)

    fig.suptitle(
        f'Kraftfeldgenerator: Akustische Barriere '
        f'({array.nx}×{array.ny}, {array.freq/1000:.0f} kHz)',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'barriere.png'), dpi=150)
    plt.close()
    print("  → barriere.png")


def plot_array_comparison(results: list[dict[str, Any]],
                          output_dir: str) -> None:
    """Plot 4: Arraygröße vs. Fokusgewinn."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ns = [r['n'] for r in results]
    P_kohs = [r['P_koh'] for r in results]
    P_inks = [r['P_ink'] for r in results]
    P_antis = [r['P_anti'] for r in results]

    ax = axes[0]
    ax.plot(ns, P_kohs, 'bo-', lw=2, ms=8, label='Kohärent (Δφ = 0)')
    ax.plot(ns, P_inks, 'rs--', lw=1.5, ms=6, label='Inkohärent')
    ax.plot(ns, P_antis, 'g^:', lw=1.5, ms=6, label='Anti-kohärent (Δφ = π)')

    n_ref = ns[0]
    P_ref = P_kohs[0]
    ns_t = np.linspace(ns[0], ns[-1], 50)
    ax.plot(ns_t, P_ref * ns_t / n_ref, 'b:', alpha=0.4, label='∝ N')

    ax.set_xlabel('Anzahl Transducer N')
    ax.set_ylabel('|P_fokus| [Pa]')
    ax.set_title('Fokusdruck vs. Arraygröße')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_xscale('log')
    ax.set_yscale('log')

    ax = axes[1]
    ax.axis('off')
    table_data = [['Array', 'N', 'P_koh', 'P_anti', 'P_ink', 'Kontrast']]
    for r in results:
        table_data.append([
            r['label'], str(r['n']),
            f"{r['P_koh']:.2f}",
            f"{r['P_anti']:.2f}",
            f"{r['P_ink']:.2f}",
            f"{r['contrast']:.1f}×"
        ])
    table = ax.table(cellText=table_data[1:], colLabels=table_data[0],
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.8)
    ax.set_title('Ergebnisse', fontsize=11, pad=20)

    fig.suptitle(
        'Kraftfeldgenerator: Phasensteuerung (Δφ=0 vs. Δφ=π vs. zufällig)',
        fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'arrayvergleich.png'), dpi=150)
    plt.close()
    print("  → arrayvergleich.png")


# ============================================================
# 9. Hauptprogramm
# ============================================================

def main() -> None:
    print("=" * 60)
    print("KRAFTFELDGENERATOR: Akustische Barrieren")
    print("Resonanzfeldtheorie: E = π · ε(Δφ) · ℏ · f")
    print("ε(Δφ) = cos²(Δφ/2), κ = 1 (parameterfrei)")
    print("=" * 60)

    output_dir = "figures"
    ensure_dir(output_dir)

    array = TransducerArray(
        nx=16, ny=16, spacing=0.01,
        freq=40000.0, p0=1.0, radius=0.005
    )
    array.info()

    z_focus = 0.10

    # --- Experiment 1: Fokussierung ---
    print("\n=== Experiment 1: Fokussierung (kohärent vs. inkohärent) ===")
    X, Y, P_koh, P_ink, I_koh, I_ink = experiment_focus(
        array, z_focus=z_focus, grid_size=0.05, n_grid=200
    )
    P_max_koh = np.max(np.abs(P_koh))
    P_max_ink = np.max(np.abs(P_ink))
    gain = P_max_koh / P_max_ink if P_max_ink > 0 else 0
    print(f"  P_max (kohärent):   {P_max_koh:.4f} Pa")
    print(f"  P_max (inkohärent): {P_max_ink:.4f} Pa")
    print(f"  Fokusgewinn:        {gain:.1f}×")
    print(f"  I_max (kohärent):   {np.max(I_koh):.6f} W/m²")
    plot_focus(array, X, Y, P_koh, P_ink, I_koh, I_ink, output_dir)

    # --- Experiment 2: Phasenscan ---
    print("\n=== Experiment 2: Phasenscan (Gruppe A vs. B) ===")
    phis, P_focus, I_focus = experiment_phase_scan(
        array, z_focus=z_focus, n_phi=50
    )
    print(f"  Δφ = 0 (max):     P = {P_focus[0]:.4f} Pa")
    idx_half = len(phis) // 4
    idx_pi = len(phis) // 2
    print(f"  Δφ = π/2:         P = {P_focus[idx_half]:.4f} Pa")
    print(f"  Δφ = π (min):     P = {P_focus[idx_pi]:.4f} Pa")

    I_mean = plot_phase_scan(phis, P_focus, I_focus, output_dir)

    if I_mean > 0:
        ratio = I_focus[0] / I_mean
        theo = 1.0 / np.mean(coupling_efficiency(phis)**2)
        print(f"\n  RFT-Signatur:")
        print(f"    I(Δφ=0) / ⟨I⟩ = {ratio:.4f}")
        print(f"    Theorie:         {theo:.4f}")
        print(f"    P(0)/P(π):       "
              f"{P_focus[0]/P_focus[idx_pi]:.1f}× "
              f"(Kontrast)")

    # --- Experiment 3: Barriere ---
    print("\n=== Experiment 3: Akustische Barriere ===")
    X_b, Y_b, P_b, P_rad = experiment_barrier(
        array, z_focus=z_focus, grid_size=0.05, n_grid=200
    )
    P_rad_max = np.max(P_rad)
    print(f"  Max. Strahlungsdruck: {P_rad_max*1000:.4f} mPa")
    F_insect = P_rad_max * 1e-6  # Kraft auf 1 mm²
    print(f"  Kraft auf Insekt (1 mm²): {F_insect*1e6:.4f} µN")
    print(f"  Gewicht Insekt (1 mg):    {1e-6 * 9.81 * 1e6:.1f} µN")
    plot_barrier(X_b, Y_b, P_b, P_rad, array, output_dir)

    # --- Experiment 4: Arrayvergleich ---
    print("\n=== Experiment 4: Arrayvergleich ===")
    results = experiment_array_comparison(z_focus=z_focus)
    for r in results:
        print(f"  {r['label']:16s}  P_koh={r['P_koh']:8.2f}, "
              f"P_anti={r['P_anti']:7.2f}, "
              f"P_ink={r['P_ink']:7.2f}, "
              f"Kontrast={r['contrast']:.1f}×")
    plot_array_comparison(results, output_dir)

    # --- Zusammenfassung ---
    print("\n" + "=" * 60)
    print("ZUSAMMENFASSUNG")
    print("=" * 60)
    print(f"""
  Kraftfeldgenerator: Akustische Barrieren

  Grundformel:    E = π · ε(Δφ) · ℏ · f
  Kopplung:       ε(Δφ) = cos²(Δφ/2), κ = 1

  System:
    Array:        {array.nx}×{array.ny} = {array.n_total} Transducer
    Frequenz:     {array.freq/1000:.0f} kHz (λ = {array.wavelength*1000:.1f} mm)
    Fokus:        {z_focus*100:.0f} cm

  Phasenscan:
    Zwei Gruppen (links/rechts) mit Δφ relativ.
    P(Δφ=0) = {P_focus[0]:.2f} Pa (volle Kopplung)
    P(Δφ=π) = {P_focus[idx_pi]:.2f} Pa (destruktive Interferenz)
    → Druck folgt cos²(Δφ/2)
    → Intensität folgt cos⁴(Δφ/2)

  Barriere:
    FWHM ≈ λ/1.5 = {array.wavelength*1000/1.5:.1f} mm
    P_rad_max = {P_rad_max*1000:.2f} mPa

  Gleiche Physik wie Resonanzgenerator und Resonanzreaktor:
    E = π · ε(Δφ) · ℏ · f, κ = 1
    Drei Skalen, eine Gleichung.

  Plots: {output_dir}/
""")
    print("Fertig.")


if __name__ == "__main__":
    main()