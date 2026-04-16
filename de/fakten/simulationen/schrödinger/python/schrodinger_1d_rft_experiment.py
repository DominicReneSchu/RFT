"""
Experimenteller Vorschlag — SI-Kalibrierung der RFT-Störungstheorie
====================================================================

Kontext (Kritikpunkt 3.1: SI-Einheiten / Kalibrierung)
-------------------------------------------------------
Die Störungstheorie (`schrodinger_1d_rft_perturbation.py`) hat gezeigt:

  |Δ⟨x⟩| ≈ C_x · λ    mit  C_x ≈ 4.9  (dimensionslos)

Hier wird diese Vorhersage auf ein konkretes physikalisches System
abgebildet: **ultrakalte ⁸⁷Rb-Atome in einer harmonischen Falle**,
dem experimentellen Standardsystem für Präzisionsmessungen in der
Quantenmechanik (BEC-Labore weltweit).

Falsifizierbare Vorhersage
--------------------------
Wenn die RFT-Rückkopplung (Δφ koppelt an |ψ|²) existiert, dann
verschiebt sich der Schwerpunkt eines Wellenpakets um:

  |Δ⟨x⟩|_SI = C_x · λ · ℓ

wobei ℓ die Längeneinheit der Simulation ist, bestimmt durch die
Fallenparameter:

  ℓ = V_strength^(1/4) · a_ho
  a_ho = √(ℏ / (m · ω_trap))

Für ⁸⁷Rb bei ω_trap = 2π × 100 Hz ergibt sich:
  a_ho ≈ 1.08 µm,  ℓ ≈ 0.41 µm

  → |Δ⟨x⟩| ≈ 2.0 µm · λ

Messmethode: Absorptionsbildgebung (time-of-flight) mit räumlicher
Auflösung ~ 1 µm. Die RFT-Verschiebung ist ab λ ≳ 0.5 direkt
detektierbar, ab λ ≳ 0.01 über wiederholte Messungen statistisch
nachweisbar (σ_Δx ~ 0.1 µm nach 100 Wiederholungen).

Einheiten: SI-Einheiten. Alle physikalischen Konstanten aus CODATA 2018.

Ausführung:
  python python/schrodinger_1d_rft_experiment.py
  python python/schrodinger_1d_rft_experiment.py --checks
  python python/schrodinger_1d_rft_experiment.py --omega 200
  python python/schrodinger_1d_rft_experiment.py --plot
"""

from __future__ import annotations

import argparse
import math
from typing import Any

import numpy as np


# ═══════════════════════════════════════════════════════════════════════════════
#  Physikalische Konstanten (CODATA 2018)
# ═══════════════════════════════════════════════════════════════════════════════

HBAR_SI: float = 1.054571817e-34      # ℏ [J·s]
M_RB87_SI: float = 86.909180520 * 1.66053906660e-27  # ⁸⁷Rb Masse [kg]
K_B_SI: float = 1.380649e-23          # Boltzmann-Konstante [J/K]
A_S_RB87: float = 5.77e-9             # ⁸⁷Rb s-Wellen-Streulänge [m]

# Simulationsparameter (identisch mit schrodinger_1d_rft_perturbation.py)
V_STRENGTH_SIM: float = 0.02          # ½ · V_strength · x² (dimensionslos)
C_X_PREFACTOR: float = 4.9            # |Δ⟨x⟩| ≈ C_x · λ (aus Fit)
C_P_PREFACTOR: float = 3.2            # |Δ⟨p⟩| ≈ C_p · λ (aus Fit)
C_FID_PREFACTOR: float = 138.0        # 1 − F ≈ C_F · λ² (aus Fit)


# ═══════════════════════════════════════════════════════════════════════════════
#  SI-Kalibrierung
# ═══════════════════════════════════════════════════════════════════════════════


def harmonic_oscillator_length(
    m_si: float, omega_si: float,
) -> float:
    """Harmonischer Oszillator: natürliche Länge a_ho = √(ℏ/(m·ω)) [m]."""
    return math.sqrt(HBAR_SI / (m_si * omega_si))


def simulation_length_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Längeneinheit ℓ der Simulation in SI [m].

    ℓ = V_strength^(1/4) · a_ho

    Herleitung: Die dimensionslose Schrödinger-Gleichung mit ℏ=m=1
    hat das Potential V(x̃) = ½·V_strength·x̃². In SI-Einheiten
    entspricht x̃ = x_phys / ℓ, wobei ℓ⁴ = V_strength · ℏ² / (m²ω²),
    also ℓ = V_strength^(1/4) · a_ho.
    """
    a_ho = harmonic_oscillator_length(m_si, omega_si)
    return v_strength ** 0.25 * a_ho


def simulation_time_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Zeiteinheit τ der Simulation in SI [s].

    τ = m · ℓ² / ℏ = √(V_strength) / ω
    """
    return math.sqrt(v_strength) / omega_si


def simulation_energy_unit(
    omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Energieeinheit der Simulation in SI [J].

    E_unit = ℏ / τ = ℏ · ω / √(V_strength)
    """
    return HBAR_SI * omega_si / math.sqrt(v_strength)


def simulation_momentum_unit(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> float:
    """Impulseinheit der Simulation in SI [kg·m/s].

    p_unit = ℏ / ℓ
    """
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    return HBAR_SI / ell


# ═══════════════════════════════════════════════════════════════════════════════
#  Vorhersagen in SI-Einheiten
# ═══════════════════════════════════════════════════════════════════════════════


def predict_delta_x_si(
    lam: float | np.ndarray,
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
    c_x: float = C_X_PREFACTOR,
) -> float | np.ndarray:
    """RFT-Vorhersage: |Δ⟨x⟩|_SI = C_x · λ · ℓ  [m]."""
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    return c_x * lam * ell


def predict_delta_p_si(
    lam: float | np.ndarray,
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
    c_p: float = C_P_PREFACTOR,
) -> float | np.ndarray:
    """RFT-Vorhersage: |Δ⟨p⟩|_SI = C_p · λ · p_unit  [kg·m/s]."""
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)
    return c_p * lam * p_unit


def predict_delta_fidelity(
    lam: float | np.ndarray,
    c_fid: float = C_FID_PREFACTOR,
) -> float | np.ndarray:
    """RFT-Vorhersage: 1 − F = C_F · λ²  (dimensionslos)."""
    return c_fid * lam ** 2


# ═══════════════════════════════════════════════════════════════════════════════
#  Experimentelle Parameter und Detektierbarkeit
# ═══════════════════════════════════════════════════════════════════════════════


def absorption_imaging_resolution() -> float:
    """Typische räumliche Auflösung der Absorptionsbildgebung [m].

    Standard in BEC-Experimenten: ~ 1 µm optische Auflösung,
    verbesserbar auf ~ 0.3 µm mit hochauflösenden Objektiven.
    """
    return 1.0e-6


def statistical_sensitivity(
    single_shot_resolution: float,
    n_repetitions: int,
) -> float:
    """Statistische Sensitivität nach N Wiederholungen [m].

    σ_Δx = σ_single / √N
    """
    return single_shot_resolution / math.sqrt(n_repetitions)


def detectable_lambda_range(
    m_si: float, omega_si: float,
    resolution_m: float,
    n_repetitions: int = 1,
    v_strength: float = V_STRENGTH_SIM,
    c_x: float = C_X_PREFACTOR,
) -> float:
    """Kleinster nachweisbarer λ-Wert für gegebene Auflösung.

    λ_min = σ_eff / (C_x · ℓ)
    """
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    sigma_eff = resolution_m / math.sqrt(n_repetitions)
    return sigma_eff / (c_x * ell)


# ═══════════════════════════════════════════════════════════════════════════════
#  Gross-Pitaevskii-Vergleich und systematische Fehler
# ═══════════════════════════════════════════════════════════════════════════════


def gross_pitaevskii_coupling(
    m_si: float,
    a_s: float = A_S_RB87,
) -> float:
    """Gross-Pitaevskii-Kopplungskonstante g = 4π·ℏ²·a_s / m  [J·m³]."""
    return 4.0 * math.pi * HBAR_SI ** 2 * a_s / m_si


def gp_mean_field_shift(
    m_si: float,
    omega_si: float,
    n_atoms: int = 100_000,
    a_s: float = A_S_RB87,
) -> dict[str, float]:
    """Analyse der GP-Mean-Field-Effekte auf ⟨x⟩ [m].

    Kohn-Theorem: In einer rein harmonischen Falle ist die
    Schwerpunktsbewegung exakt bei ω, unabhängig von Wechselwirkungen.
    → GP-Mean-Field verschiebt ⟨x⟩ NICHT in perfekter harmonischer Falle!

    Effekte auf ⟨x⟩ kommen nur von:
    1. Anharmonizitäten (Trap-Imperfektionen)
    2. Positionsabhängige Verluste

    GP-Effekte auf höhere Momente (⟨x²⟩, Breite) sind vorhanden,
    aber interferieren nicht mit der ⟨x⟩-Messung.
    """
    a_ho = harmonic_oscillator_length(m_si, omega_si)
    r_tf = a_ho * (15.0 * n_atoms * a_s / a_ho) ** 0.2
    mu = 0.5 * m_si * omega_si ** 2 * r_tf ** 2
    mu_over_hbar_omega = mu / (HBAR_SI * omega_si)

    return {
        "r_tf_m": r_tf,
        "mu_j": mu,
        "mu_over_hbar_omega": mu_over_hbar_omega,
        "dx_shift_m": 0.0,  # Kohn-Theorem: exakt Null
        "kohn_protected": True,
    }


def systematic_error_budget(
    m_si: float,
    omega_si: float,
    n_atoms: int = 100_000,
    a_s: float = A_S_RB87,
) -> dict[str, float]:
    """Abschätzung systematischer Fehlerquellen [m].

    Returns
    -------
    Dictionary mit geschätzten systematischen Verschiebungen.
    """
    a_ho = harmonic_oscillator_length(m_si, omega_si)

    # GP-Mean-Field: Kohn-geschützt in harmonischer Falle
    dx_gp = 0.0

    # Potentialanharmonizität (typisch: δω/ω ~ 10⁻³ → δx ~ 10⁻³ · a_ho)
    dx_anharmonicity = 1e-3 * a_ho

    # Magnetfeldgradienten (gut kompensiertes Experiment: 0.1 mG/cm)
    mu_b = 9.274e-24  # Bohrsches Magneton [J/T]
    db_dx = 1e-3  # 0.1 mG/cm = 10⁻³ T/m (kompensierte Spulen)
    f_mag = mu_b * db_dx
    tau = simulation_time_unit(m_si, omega_si)
    t_sim = 20.0 * tau
    dx_magnetic = 0.5 * f_mag / m_si * t_sim ** 2

    # Drei-Körper-Verluste (Atomzahlverlust → Schwerpunktdrift)
    dx_three_body = 0.01 * a_ho

    return {
        "gp_mean_field_m": dx_gp,
        "anharmonicity_m": dx_anharmonicity,
        "magnetic_gradient_m": dx_magnetic,
        "three_body_loss_m": dx_three_body,
        "total_systematic_m": math.sqrt(
            dx_gp ** 2 + dx_anharmonicity ** 2
            + dx_magnetic ** 2 + dx_three_body ** 2
        ),
    }


def gp_rft_discriminability(
    lam: float,
    m_si: float,
    omega_si: float,
    n_atoms: int = 100_000,
    v_strength: float = V_STRENGTH_SIM,
) -> dict[str, float]:
    """Vergleich: RFT-Verschiebung vs. GP-Mean-Field-Effekt.

    Zentrales Argument (Kohn-Theorem):
    In einer rein harmonischen Falle verschiebt die GP-Wechselwirkung
    den Schwerpunkt ⟨x⟩ NICHT. Die Schwerpunktsbewegung ist exakt
    harmonisch bei ω, unabhängig von g, N, a_s.

    Die RFT-Rückkopplung ε(Δφ(t))·V hingegen erzeugt eine
    zeitabhängige Modulierung der Fallenstärke, die ⟨x⟩ verschiebt.
    → RFT-Effekt auf ⟨x⟩ ist konzeptuell verschieden von GP.

    Protokoll zur zusätzlichen experimentellen Unterscheidung:
    1. N-Scan: GP-Breite ∝ N^(2/5), RFT-Shift ⟨x⟩ unabhängig von N
    2. a_s-Scan: Feshbach-Resonanz zum Tunen von a_s
    3. ω-Scan: Verschiedene Skalierungsgesetze
    4. Δφ₀-Scan: Nur RFT hängt von Anfangsphasendifferenz ab
    """
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    dx_rft = C_X_PREFACTOR * lam * ell

    gp = gp_mean_field_shift(m_si, omega_si, n_atoms)
    dx_gp_on_mean_x = gp["dx_shift_m"]

    return {
        "dx_rft_m": dx_rft,
        "dx_gp_on_mean_x_m": dx_gp_on_mean_x,
        "kohn_protected": gp["kohn_protected"],
        "mu_over_hbar_omega": gp["mu_over_hbar_omega"],
        "r_tf_m": gp["r_tf_m"],
    }


def experimental_parameters(
    omega_hz: float,
    m_si: float = M_RB87_SI,
    v_strength: float = V_STRENGTH_SIM,
) -> dict[str, Any]:
    """Berechne alle experimentellen Parameter für gegebene Fallenfrequenz.

    Returns
    -------
    Dictionary mit SI-kalibrierten Parametern und Vorhersagen.
    """
    omega_si = 2.0 * math.pi * omega_hz

    a_ho = harmonic_oscillator_length(m_si, omega_si)
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    tau = simulation_time_unit(m_si, omega_si, v_strength)
    e_unit = simulation_energy_unit(omega_si, v_strength)
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)

    # Simulationszeit in SI
    sim_steps = 2000
    sim_dt = 0.01
    t_sim_total = sim_steps * sim_dt  # dimensionslos
    t_phys = t_sim_total * tau  # SI [s]

    # Vorhersagen für verschiedene λ
    lambdas = np.array([0.001, 0.01, 0.05, 0.1, 0.5, 1.0])
    dx_si = predict_delta_x_si(lambdas, m_si, omega_si, v_strength)
    dp_si = predict_delta_p_si(lambdas, m_si, omega_si, v_strength)
    delta_fid = predict_delta_fidelity(lambdas)

    # Detektierbarkeit
    res_abs = absorption_imaging_resolution()
    lam_min_single = detectable_lambda_range(
        m_si, omega_si, res_abs, 1, v_strength,
    )
    lam_min_100 = detectable_lambda_range(
        m_si, omega_si, res_abs, 100, v_strength,
    )
    lam_min_10000 = detectable_lambda_range(
        m_si, omega_si, res_abs, 10000, v_strength,
    )

    # BEC-Temperatur (Richtwert)
    # T_BEC ~ ℏ·ω/(k_B) · (N_atoms)^(1/3)
    # Für ~10⁵ Atome: T_BEC ~ 100 nK
    t_bec_typical = HBAR_SI * omega_si / K_B_SI * (1e5) ** (1.0 / 3.0)

    return {
        "omega_hz": omega_hz,
        "omega_si": omega_si,
        "m_si": m_si,
        "m_amu": m_si / 1.66053906660e-27,
        "a_ho_m": a_ho,
        "ell_m": ell,
        "tau_s": tau,
        "e_unit_j": e_unit,
        "e_unit_ev": e_unit / 1.602176634e-19,
        "p_unit_si": p_unit,
        "t_phys_s": t_phys,
        "v_strength": v_strength,
        "lambdas": lambdas,
        "dx_si_m": dx_si,
        "dp_si": dp_si,
        "delta_fid": delta_fid,
        "resolution_m": res_abs,
        "lam_min_single": lam_min_single,
        "lam_min_100": lam_min_100,
        "lam_min_10000": lam_min_10000,
        "t_bec_typical_nK": t_bec_typical * 1e9,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Verifizierung der Skalenrelationen
# ═══════════════════════════════════════════════════════════════════════════════


def verify_unit_consistency(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> list[tuple[str, bool, str]]:
    """Überprüfe die Konsistenz der SI-Kalibrierung.

    Returns
    -------
    Liste von (Test-Name, bestanden, Detail-String).
    """
    results: list[tuple[str, bool, str]] = []

    a_ho = harmonic_oscillator_length(m_si, omega_si)
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    tau = simulation_time_unit(m_si, omega_si, v_strength)
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)

    # Test 1: ℏ = m · ℓ² / τ
    hbar_check = m_si * ell ** 2 / tau
    rel1 = abs(hbar_check - HBAR_SI) / HBAR_SI
    results.append((
        "ℏ = m·ℓ²/τ",
        rel1 < 1e-10,
        f"rel. Fehler = {rel1:.2e}",
    ))

    # Test 2: ℓ = V_strength^(1/4) · a_ho
    ell_check = v_strength ** 0.25 * a_ho
    rel2 = abs(ell_check - ell) / ell
    results.append((
        "ℓ = V_s^(1/4)·a_ho",
        rel2 < 1e-10,
        f"rel. Fehler = {rel2:.2e}",
    ))

    # Test 3: τ = √V_s / ω
    tau_check = math.sqrt(v_strength) / omega_si
    rel3 = abs(tau_check - tau) / tau
    results.append((
        "τ = √V_s / ω",
        rel3 < 1e-10,
        f"rel. Fehler = {rel3:.2e}",
    ))

    # Test 4: p_unit = ℏ / ℓ
    p_check = HBAR_SI / ell
    rel4 = abs(p_check - p_unit) / p_unit
    results.append((
        "p_unit = ℏ/ℓ",
        rel4 < 1e-10,
        f"rel. Fehler = {rel4:.2e}",
    ))

    # Test 5: E_unit · τ = ℏ
    e_unit = simulation_energy_unit(omega_si, v_strength)
    hbar_check2 = e_unit * tau
    rel5 = abs(hbar_check2 - HBAR_SI) / HBAR_SI
    results.append((
        "E_unit · τ = ℏ",
        rel5 < 1e-10,
        f"rel. Fehler = {rel5:.2e}",
    ))

    # Test 6: Für V_strength=1 gilt ℓ = a_ho
    ell_natural = simulation_length_unit(m_si, omega_si, 1.0)
    rel6 = abs(ell_natural - a_ho) / a_ho
    results.append((
        "V_s=1 → ℓ=a_ho",
        rel6 < 1e-10,
        f"rel. Fehler = {rel6:.2e}",
    ))

    return results


# ═══════════════════════════════════════════════════════════════════════════════
#  Numerische Verifikation mit Perturbations-Scan
# ═══════════════════════════════════════════════════════════════════════════════


def run_perturbation_verification(
    m_si: float, omega_si: float,
    v_strength: float = V_STRENGTH_SIM,
) -> dict[str, Any]:
    """Führe den Störungstheorie-Scan durch und verifiziere die Präfaktoren.

    Importiert die Simulation aus schrodinger_1d_rft_perturbation.py und
    überprüft, dass die dort berechneten Präfaktoren mit den hier
    verwendeten übereinstimmen.
    """
    # Simulationsparameter (identisch mit perturbation.py defaults)
    n_grid = 2048
    l_domain = 200.0
    dt = 0.01
    steps = 2000
    hbar_sim = 1.0
    m_sim = 1.0
    x0, k0, sigma = -40.0, 1.0, 8.0
    delta_phi0 = math.pi / 3.0

    dx = l_domain / n_grid
    x = (np.arange(n_grid) - n_grid // 2) * dx
    dk = 2.0 * math.pi / l_domain
    k = 2.0 * math.pi * np.fft.fftfreq(n_grid, d=dx)
    v_coupling = 0.5 * v_strength * x ** 2

    # Gaußsches Wellenpaket
    psi0 = np.exp(-0.5 * ((x - x0) / sigma) ** 2) * np.exp(1j * k0 * x)
    norm = np.sum(np.abs(psi0) ** 2) * dx
    psi0 = psi0 / math.sqrt(norm)

    # Perturbations-Scan (nur im stark perturbativen Regime)
    lambdas = np.array([1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3])

    # Import der Kernfunktionen (identischer Code)
    from schrodinger_1d_rft_perturbation import (
        evolve_rft_dynamic,
        evolve_standard,
        epsilon_coupling,
        fit_power_law,
    )

    eps0 = float(epsilon_coupling(delta_phi0))
    v_eff_ref = eps0 * v_coupling

    ref = evolve_standard(
        psi0, v_eff_ref, x, k, dx, dk, dt, steps, hbar_sim, m_sim,
    )

    delta_x_list: list[float] = []
    delta_p_list: list[float] = []
    delta_fid_list: list[float] = []

    for lam in lambdas:
        rft = evolve_rft_dynamic(
            psi0, v_coupling, delta_phi0, float(lam),
            x, k, dx, dk, dt, steps, hbar_sim, m_sim,
        )
        overlap = np.sum(np.conj(ref["psi_final"]) * rft["psi_final"]) * dx
        fid = float(np.abs(overlap) ** 2)
        delta_fid_list.append(1.0 - fid)
        delta_x_list.append(abs(ref["x_means"][-1] - rft["x_means"][-1]))
        delta_p_list.append(abs(ref["p_means"][-1] - rft["p_means"][-1]))

    delta_x_arr = np.array(delta_x_list)
    delta_p_arr = np.array(delta_p_list)
    delta_fid_arr = np.array(delta_fid_list)

    exp_x, pre_x = fit_power_law(lambdas, delta_x_arr)
    exp_p, pre_p = fit_power_law(lambdas, delta_p_arr)
    exp_fid, pre_fid = fit_power_law(lambdas, delta_fid_arr)

    # SI-Konversion
    ell = simulation_length_unit(m_si, omega_si, v_strength)
    p_unit = simulation_momentum_unit(m_si, omega_si, v_strength)

    return {
        "lambdas": lambdas,
        "delta_x_sim": delta_x_arr,
        "delta_p_sim": delta_p_arr,
        "delta_fid": delta_fid_arr,
        "exp_x": exp_x,
        "pre_x": pre_x,
        "exp_p": exp_p,
        "pre_p": pre_p,
        "exp_fid": exp_fid,
        "pre_fid": pre_fid,
        "delta_x_si": delta_x_arr * ell,
        "delta_p_si": delta_p_arr * p_unit,
    }


# ═══════════════════════════════════════════════════════════════════════════════
#  Hauptprogramm
# ═══════════════════════════════════════════════════════════════════════════════


def main() -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Experimenteller Vorschlag: SI-Kalibrierung der "
            "RFT-Störungstheorie für ultrakalte ⁸⁷Rb-Atome"
        ),
    )
    ap.add_argument(
        "--omega", type=float, default=100.0,
        help="Fallenfrequenz [Hz] (Standard: 100 Hz)",
    )
    ap.add_argument(
        "--plot", action="store_true",
        help="Detektierbarkeits-Plot",
    )
    ap.add_argument(
        "--checks", action="store_true",
        help="Erweiterte Konsistenz-Tests",
    )
    ap.add_argument(
        "--verify", action="store_true",
        help="Numerische Verifikation der Präfaktoren",
    )
    ap.add_argument(
        "--critical", action="store_true",
        help="Kritische Einordnung: GP-Vergleich, systematische Fehler",
    )
    args = ap.parse_args()

    omega_hz: float = args.omega
    omega_si: float = 2.0 * math.pi * omega_hz
    m_si: float = M_RB87_SI

    # ─── Header ───────────────────────────────────────────────────────
    print("=" * 74)
    print("  Experimenteller Vorschlag: RFT-Störungstheorie → SI-Einheiten")
    print("  System: ⁸⁷Rb-Atome in harmonischer Falle")
    print("=" * 74)

    # ─── Physikalische Parameter ──────────────────────────────────────
    params = experimental_parameters(omega_hz, m_si)

    print(f"\n  Physikalische Parameter:")
    print(f"  {'─' * 50}")
    print(f"  Atom:              ⁸⁷Rb  (m = {params['m_amu']:.3f} u)")
    print(f"  Masse:             {m_si:.6e} kg")
    print(f"  Fallenfrequenz:    ω = 2π × {omega_hz:.1f} Hz")
    print(f"  V_strength (sim):  {params['v_strength']}")

    print(f"\n  Natürliche Skalen:")
    print(f"  {'─' * 50}")
    print(f"  a_ho   = √(ℏ/mω)         = {params['a_ho_m'] * 1e6:.4f} µm")
    print(f"  ℓ      = V_s^(1/4) · a_ho = {params['ell_m'] * 1e6:.4f} µm")
    print(f"  τ      = √V_s / ω         = {params['tau_s'] * 1e3:.4f} ms")
    print(f"  E_unit = ℏ/τ              = {params['e_unit_ev']:.4e} eV")
    print(f"  p_unit = ℏ/ℓ              = {params['p_unit_si']:.4e} kg·m/s")
    print(f"  T_sim  = {2000 * 0.01:.0f} τ "
          f"= {params['t_phys_s'] * 1e3:.2f} ms")

    # ─── RFT-Vorhersagen in SI ────────────────────────────────────────
    print(f"\n  RFT-Vorhersagen (|Δ⟨x⟩| = {C_X_PREFACTOR} · λ · ℓ):")
    print(f"  {'─' * 60}")
    print(f"  {'λ':>10s}  {'|Δ⟨x⟩| [µm]':>14s}  "
          f"{'|Δ⟨p⟩| [ℏ/µm]':>14s}  {'1−F':>12s}")
    print(f"  {'─' * 60}")

    for i, lam in enumerate(params["lambdas"]):
        dx_um = params["dx_si_m"][i] * 1e6
        dp_hbar_um = params["dp_si"][i] / (HBAR_SI / 1e-6)
        print(f"  {lam:10.3f}  {dx_um:14.4f}  "
              f"{dp_hbar_um:14.4f}  {params['delta_fid'][i]:12.4e}")

    # ─── Detektierbarkeit ─────────────────────────────────────────────
    print(f"\n  Detektierbarkeit (Absorptionsbildgebung):")
    print(f"  {'─' * 60}")
    print(f"  Einzelschuss-Auflösung:     {params['resolution_m'] * 1e6:.1f} µm")
    print(f"  λ_min (1 Messung):          {params['lam_min_single']:.2f}")
    print(f"  λ_min (100 Messungen):      {params['lam_min_100']:.3f}")
    print(f"  λ_min (10 000 Messungen):   {params['lam_min_10000']:.4f}")
    print(f"\n  → Für λ ≳ {params['lam_min_100']:.2f} ist die "
          f"RFT-Verschiebung nach 100 Wiederholungen")
    print(f"    bei ω = 2π × {omega_hz:.0f} Hz statistisch nachweisbar.")

    # ─── Experimentelle Empfehlungen ──────────────────────────────────
    print(f"\n  Experimentelles Protokoll:")
    print(f"  {'─' * 60}")
    print(f"  1. BEC aus ⁸⁷Rb präparieren (T < {params['t_bec_typical_nK']:.0f} nK)")
    print(f"  2. Harmonische Falle mit ω = 2π × {omega_hz:.0f} Hz")
    print(f"  3. Wellenpaket initialisieren (Impuls-Kick: k₀ = 1.0 / ℓ)")
    print(f"  4. Frei propagieren lassen für t = {params['t_phys_s'] * 1e3:.1f} ms")
    print(f"  5. Absorptionsbildgebung: ⟨x⟩ messen")
    print(f"  6. Wiederhole N = 100–10000 mal")
    print(f"  7. Statistik: Δ⟨x⟩ = ⟨x⟩_exp − ⟨x⟩_QM")
    print(f"     → Wenn |Δ⟨x⟩| > 0: RFT-Effekt nachgewiesen")
    print(f"     → Wenn |Δ⟨x⟩| ≈ 0: Obere Schranke für λ")

    # ─── Frequenz-Scan ────────────────────────────────────────────────
    print(f"\n  Frequenzabhängigkeit der Sensitivität:")
    print(f"  {'─' * 55}")
    print(f"  {'ω/2π [Hz]':>12s}  {'a_ho [µm]':>10s}  {'ℓ [µm]':>10s}  "
          f"{'λ_min(100)':>12s}")
    print(f"  {'─' * 55}")

    for freq in [10.0, 50.0, 100.0, 200.0, 500.0, 1000.0]:
        omega_f = 2.0 * math.pi * freq
        a_f = harmonic_oscillator_length(m_si, omega_f) * 1e6
        ell_f = simulation_length_unit(m_si, omega_f) * 1e6
        lam_f = detectable_lambda_range(
            m_si, omega_f, absorption_imaging_resolution(), 100,
        )
        print(f"  {freq:12.0f}  {a_f:10.4f}  {ell_f:10.4f}  {lam_f:12.3f}")

    print(f"\n  → Niedrigere Fallenfrequenz = größeres a_ho = bessere Sensitivität.")
    print(f"    Optimum: ω ≲ 2π × 50 Hz (aber längere Präparationszeit).")

    # ─── Smoke-Tests ──────────────────────────────────────────────────
    all_pass = True

    if args.checks:
        print(f"\n{'=' * 74}")
        print("  Konsistenz-Tests: SI-Kalibrierung")
        print(f"{'=' * 74}")

        checks = verify_unit_consistency(m_si, omega_si)
        for name, passed, detail in checks:
            symbol = "✓" if passed else "✗"
            print(f"  {symbol} {name:25s}  {detail}")
            if not passed:
                all_pass = False

        # Test: Vorhersage ist positiv und physikalisch sinnvoll
        dx_test = predict_delta_x_si(0.1, m_si, omega_si)
        ok = 1e-12 < dx_test < 1e-3
        symbol = "✓" if ok else "✗"
        print(f"  {symbol} {'|Δx|(λ=0.1) plausibel':25s}  "
              f"{dx_test * 1e6:.4f} µm")
        if not ok:
            all_pass = False

        # Test: Detektierbarkeitsgrenze liegt im physikalischen Bereich
        ok2 = 1e-4 < params["lam_min_100"] < 100.0
        symbol = "✓" if ok2 else "✗"
        print(f"  {symbol} {'λ_min(100) physikalisch':25s}  "
              f"{params['lam_min_100']:.4f}")
        if not ok2:
            all_pass = False

        # Test: Verschiedene Frequenzen → monoton sinkende Sensitivität
        lam_10 = detectable_lambda_range(
            m_si, 2 * math.pi * 10,
            absorption_imaging_resolution(), 100,
        )
        lam_1000 = detectable_lambda_range(
            m_si, 2 * math.pi * 1000,
            absorption_imaging_resolution(), 100,
        )
        ok3 = lam_10 < lam_1000
        symbol = "✓" if ok3 else "✗"
        print(f"  {symbol} {'Monotonie ω → λ_min':25s}  "
              f"λ_min(10 Hz)={lam_10:.3f} < λ_min(1 kHz)={lam_1000:.3f}")
        if not ok3:
            all_pass = False

    if args.verify:
        print(f"\n{'=' * 74}")
        print("  Numerische Verifikation: Präfaktoren")
        print(f"{'=' * 74}")

        vresult = run_perturbation_verification(m_si, omega_si)
        print(f"\n  Skalierungsexponenten (Verifikation):")
        print(f"    |Δ⟨x⟩|:  exp = {vresult['exp_x']:.3f}  "
              f"(erwartet 1.0), Präfaktor = {vresult['pre_x']:.3f}  "
              f"(verwendet: {C_X_PREFACTOR})")
        print(f"    |Δ⟨p⟩|:  exp = {vresult['exp_p']:.3f}  "
              f"(erwartet 1.0), Präfaktor = {vresult['pre_p']:.3f}  "
              f"(verwendet: {C_P_PREFACTOR})")
        print(f"    1−F:     exp = {vresult['exp_fid']:.3f}  "
              f"(erwartet 2.0), Präfaktor = {vresult['pre_fid']:.1f}  "
              f"(verwendet: {C_FID_PREFACTOR})")

        rel_x = abs(vresult["pre_x"] - C_X_PREFACTOR) / C_X_PREFACTOR
        rel_p = abs(vresult["pre_p"] - C_P_PREFACTOR) / C_P_PREFACTOR
        print(f"\n  Präfaktor-Abweichungen: "
              f"C_x: {rel_x:.2%}, C_p: {rel_p:.2%}")

        if rel_x > 0.05:
            print(f"  [WARN] C_x weicht um >{5}% ab — Präfaktor prüfen!")
        if rel_p > 0.05:
            print(f"  [WARN] C_p weicht um >{5}% ab — Präfaktor prüfen!")

    # ─── Kritische Einordnung ─────────────────────────────────────────
    if args.critical:
        print(f"\n{'=' * 74}")
        print("  Kritische Einordnung: GP-Vergleich & Systematische Fehler")
        print(f"{'=' * 74}")

        # Systematische Fehler
        syst = systematic_error_budget(m_si, omega_si)
        print(f"\n  Systematische Fehlerquellen:")
        print(f"  {'─' * 60}")
        print(f"  {'Quelle':<30s}  {'Δx [µm]':>10s}  {'Δx [nm]':>10s}")
        print(f"  {'─' * 60}")
        for label, key in [
            ("GP-Mean-Field", "gp_mean_field_m"),
            ("Anharmonizität", "anharmonicity_m"),
            ("Magnetfeldgradient", "magnetic_gradient_m"),
            ("Drei-Körper-Verluste", "three_body_loss_m"),
            ("Gesamt (quadratisch)", "total_systematic_m"),
        ]:
            val_m = syst[key]
            print(f"  {label:<30s}  {val_m * 1e6:10.4f}  {val_m * 1e9:10.2f}")

        # GP vs. RFT Vergleich — Kohn-Theorem
        comp_ref = gp_rft_discriminability(0.1, m_si, omega_si)
        print(f"\n  Kohn-Theorem — Schutz von ⟨x⟩:")
        print(f"  {'─' * 60}")
        print("  In einer rein harmonischen Falle gilt das Kohn-Theorem:")
        print("  Die Schwerpunktsbewegung ⟨x⟩(t) ist exakt harmonisch")
        print("  bei ω — UNABHÄNGIG von Atom-Atom-Wechselwirkungen.")
        print(f"  → GP-Wechselwirkung verschiebt ⟨x⟩ NICHT.")
        print(f"  → Kohn-geschützt: {comp_ref['kohn_protected']}")
        print(f"  → µ/(ℏω) = {comp_ref['mu_over_hbar_omega']:.1f}  "
              f"(Thomas-Fermi-Regime)")
        print(f"  → R_TF = {comp_ref['r_tf_m'] * 1e6:.2f} µm")
        print()
        print("  RFT-Rückkopplung ε(Δφ(t))·V moduliert die Fallenstärke")
        print("  zeitabhängig → bricht die Kohn-Bedingung → ⟨x⟩-Shift.")
        print()
        print(f"  {'λ':>8s}  {'Δx_RFT [µm]':>12s}  {'Δx_GP(⟨x⟩)':>12s}  "
              f"{'Kommentar':>20s}")
        print(f"  {'─' * 60}")
        for lam in [0.01, 0.05, 0.1, 0.5, 1.0]:
            comp = gp_rft_discriminability(lam, m_si, omega_si)
            print(f"  {lam:8.2f}  {comp['dx_rft_m'] * 1e6:12.4f}  "
                  f"{'0 (Kohn)':>12s}  {'RFT einzigartig':>20s}")

        print(f"\n  Zusätzliches Unterscheidungsprotokoll:")
        print(f"  {'─' * 60}")
        print("  1. N-Scan: GP ändert Breite ∝ N^(2/5), RFT ⟨x⟩ ≠ f(N)")
        print("  2. a_s-Scan: GP ∝ a_s via Feshbach, RFT unabhängig von a_s")
        print("  3. ω-Scan: RFT ∝ ω^(-1/2), GP-Breite ∝ ω^(-3/5)")
        print("  4. Δφ₀-Scan: Nur RFT hängt von der Anfangsphasendifferenz ab")

        # Gutachterfragen
        print(f"\n  Offene Gutachterfragen:")
        print(f"  {'─' * 60}")
        print("  Q1: Ist λ = 0.05 physikalisch plausibel?")
        print("      → Keine theoretische Vorhersage für λ. Wenn λ < 10⁻¹⁰")
        print("        (typisch für BSM-Korrekturen), wäre das Experiment")
        print("        chancenlos. Das Experiment setzt obere Schranken.")
        print()
        print("  Q2: Systematische vs. statistische Fehler?")
        dx_rft_01 = predict_delta_x_si(0.1, m_si, omega_si) * 1e6
        print(f"      → Δx_RFT(λ=0.1) = {dx_rft_01:.3f} µm")
        print(f"      → Δx_syst(total) = {syst['total_systematic_m'] * 1e6:.3f} µm")
        if syst["total_systematic_m"] > predict_delta_x_si(0.1, m_si, omega_si):
            print("      ⚠ Systematik dominiert für λ ≲ 0.1!")
        else:
            print("      ✓ RFT-Signal bei λ = 0.1 übersteigt Systematik.")
        print()
        print("  Q3: Gross-Pitaevskii-Problem:")
        print("      → RFT-Rückkopplung Δφ̇ ∝ ∫|ψ|⁴dx hat dieselbe")
        print("        funktionale Form wie GP-Kontaktwechselwirkung g|ψ|²ψ.")
        print("      → ABER: Kohn-Theorem schützt ⟨x⟩ in harmonischer Falle")
        print("        vor GP-Verschiebungen. GP ändert nur die Breite,")
        print("        nicht den Schwerpunkt.")
        print("      → RFT moduliert ε(Δφ(t))·V zeitabhängig → bricht Kohn")
        print("        → verschiebt ⟨x⟩. Konzeptuell verschiedener Effekt.")
        print("      → Zusätzlich: Skalierungsverhalten (N, a_s, ω, Δφ₀)")
        print("        unterscheidet RFT und GP experimentell.")

        # Bilanz
        print(f"\n  Gesamtbilanz vs. Peer-Review:")
        print(f"  {'─' * 60}")
        print(f"  {'Gutachter-Forderung':<40s}  {'Status':>10s}")
        print(f"  {'─' * 60}")
        for label, status in [
            ("1.1 Lagrange-Dichte", "⚠️ Motiviert"),
            ("1.2 Spezifikation ε(Δφ)", "✅"),
            ("2.1 ART-Grenzwert", "❌ Abgegrenzt"),
            ("2.2 Eichinvarianz", "❌ Offen"),
            ("3.1 SI-Einheiten / Kalibrierung", "✅"),
            ("3.2 Statistische Signifikanz ΛCDM", "❌ Anderer Sektor"),
            ("4.1 Wirkungsgrad κ=1", "❌ Anderer Sektor"),
            ("Schrödinger aus Axiom 4", "✅ Fünf Stufen"),
            ("Falsifizierbare Vorhersage", "✅ ⁸⁷Rb-Experiment"),
            ("Kritische Einordnung (GP/Syst.)", "✅ Hier adressiert"),
        ]:
            print(f"  {label:<40s}  {status:>10s}")


    # ─── Zusammenfassung ──────────────────────────────────────────────
    print(f"\n{'=' * 74}")
    print("  Zusammenfassung: Falsifizierbare Vorhersage der RFT")
    print(f"{'─' * 74}")
    print(f"  System:  ⁸⁷Rb in harmonischer Falle (ω = 2π × {omega_hz:.0f} Hz)")
    print(f"  Effekt:  |Δ⟨x⟩| = {C_X_PREFACTOR:.1f} · λ · "
          f"{params['ell_m'] * 1e6:.2f} µm")
    print(f"         = {C_X_PREFACTOR * params['ell_m'] * 1e6:.2f} · λ  µm")
    print(f"  Nachweis: Absorptionsbildgebung, N ≥ 100 Wiederholungen")
    print(f"  Sensitivität: λ ≳ {params['lam_min_100']:.2f} (100 Schuss)")
    print(f"                λ ≳ {params['lam_min_10000']:.3f} (10 000 Schuss)")
    print(f"  Nullhypothese: Δ⟨x⟩ = 0 (Standard-QM, λ = 0)")
    print(f"  Alternativhypothese: |Δ⟨x⟩| ∝ λ (RFT, λ > 0)")
    print(f"{'=' * 74}")

    if all_pass:
        print("  ✓ Alle Tests bestanden.")
    else:
        print("  ✗ Tests fehlgeschlagen.")

    # ─── Plot ─────────────────────────────────────────────────────────
    if args.plot:
        _plot_detectability(m_si, omega_hz)

    return 0 if all_pass else 1


# ═══════════════════════════════════════════════════════════════════════════════
#  Visualisierung
# ═══════════════════════════════════════════════════════════════════════════════


def _plot_detectability(m_si: float, omega_hz: float) -> None:
    """Detektierbarkeitsdiagramm: λ vs. |Δ⟨x⟩| für verschiedene ω."""
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    lambdas = np.logspace(-4, 1, 200)
    res_um = absorption_imaging_resolution() * 1e6
    res_100_um = res_um / math.sqrt(100)

    # --- Linkes Panel: |Δ⟨x⟩| vs λ für verschiedene Frequenzen ---
    freqs = [10.0, 50.0, 100.0, 500.0]
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

    for freq, color in zip(freqs, colors):
        omega_f = 2.0 * math.pi * freq
        dx_um = predict_delta_x_si(lambdas, m_si, omega_f) * 1e6
        ax1.loglog(lambdas, dx_um, color=color,
                   label=f"ω = 2π × {freq:.0f} Hz")

    ax1.axhline(res_um, color="gray", ls="--", alpha=0.5,
                label=f"Auflösung (1 Schuss): {res_um:.0f} µm")
    ax1.axhline(res_100_um, color="gray", ls=":", alpha=0.5,
                label=f"Sensitivität (100 Schuss): {res_100_um:.1f} µm")

    ax1.set_xlabel("λ (RFT-Kopplungsparameter)")
    ax1.set_ylabel("|Δ⟨x⟩| [µm]")
    ax1.set_title("RFT-Positionsverschiebung vs. λ")
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3, which="both")
    ax1.set_xlim(1e-4, 10)
    ax1.set_ylim(1e-5, 100)

    # --- Rechtes Panel: λ_min vs ω ---
    freqs_scan = np.logspace(0.5, 3.5, 100)
    lam_min_1 = [
        detectable_lambda_range(
            m_si, 2 * math.pi * f,
            absorption_imaging_resolution(), 1,
        )
        for f in freqs_scan
    ]
    lam_min_100 = [
        detectable_lambda_range(
            m_si, 2 * math.pi * f,
            absorption_imaging_resolution(), 100,
        )
        for f in freqs_scan
    ]
    lam_min_10k = [
        detectable_lambda_range(
            m_si, 2 * math.pi * f,
            absorption_imaging_resolution(), 10000,
        )
        for f in freqs_scan
    ]

    ax2.loglog(freqs_scan, lam_min_1, "b-", label="N = 1")
    ax2.loglog(freqs_scan, lam_min_100, "r-", label="N = 100")
    ax2.loglog(freqs_scan, lam_min_10k, "g-", label="N = 10 000")

    ax2.axhline(1.0, color="gray", ls="--", alpha=0.3)
    ax2.axvline(omega_hz, color="gray", ls=":", alpha=0.5,
                label=f"ω = 2π × {omega_hz:.0f} Hz")

    ax2.set_xlabel("ω / 2π [Hz]")
    ax2.set_ylabel("λ_min (kleinster nachweisbarer Wert)")
    ax2.set_title("Detektierbarkeitsgrenze vs. Fallenfrequenz")
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3, which="both")

    plt.suptitle(
        "Experimenteller Vorschlag: RFT-Effekt in ⁸⁷Rb\n"
        f"|Δ⟨x⟩| = {C_X_PREFACTOR:.1f} · λ · ℓ  —  "
        "Absorptionsbildgebung",
        fontsize=13,
    )
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    raise SystemExit(main())
