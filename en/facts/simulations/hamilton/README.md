# RT-31 — Resonance Hamiltonian: Hamilton Simulations

*Dominic René Schu, August 2026*
*Status: Completed (Aug 2026)*

---

## Overview

This directory contains the numerical simulations for RT-31:
Construction and verification of the resonance Hamiltonian

```
Ĥ_res = Ĥ₀ + ε(Δφ)·V̂_coupling
```

for two specific quantum systems. The simulations test the prediction that
ε(Δφ) = cos²(Δφ/2) is a universal coupling scaling parameter, following
from the k=1 representation of U(1) ⊂ G_sync (RT-02).

---

## Files

| File | System | Content |
|------|--------|---------|
| `rt31_phonon_coupling.py` | Phonon-Phonon | Two coupled harmonic oscillators, Fock space N=20 |
| `rt31_spin_orbit.py` | Spin-Orbit | Two-level system (Zeeman field + transverse drive) |

---

## System 1: Phonon-Phonon Coupling

**Hamiltonian:**
```
Ĥ_res = ℏω₁(a†₁a₁ + ½) + ℏω₂(a†₂a₂ + ½) + ε(Δφ)·ℏΩ·(a†₁a₂ + a₁a†₂)
```

**Physical subspace:** One-excitation subspace (basis |1,0⟩, |0,1⟩)

**RFT prediction:**
```
ΔE(Δφ) = ε(Δφ)·ΔE(0) = cos²(Δφ/2)·ΔE(0)
```

**Result (Aug 2026):**
- ✅ Prediction confirmed: max. deviation < 1e-14 (far below 1% threshold)
- ✅ A7-invariance confirmed: ΔE(Δφ+φ₀) = ε(Δφ+φ₀)·ΔE(0)
- ΔE_RFT(π/2) / ΔE_Standard = 0.50000000 (expected: ε(π/2) = 0.5)

**Parameters:** ω₁ = ω₂ = 1, Ω = 0.1, N_Fock = 20

---

## System 2: Spin-Orbit Coupling

**Hamiltonian:**
```
Ĥ_res = (ℏω₀/2)·σ_z + ε(Δφ)·ℏΩ·σ_x
```

**Analytical eigenvalues:**
```
E± = ±(ℏ/2)√(ω₀² + 4ε²(Δφ)·Ω²)
```

**RFT predictions:**
- Resonant case (ω₀=0): ΔE = 2·ε(Δφ)·ℏΩ = cos²(Δφ/2)·2ℏΩ
- σ_x transforms under k=1 of U(1) ⊂ G_sync → ε(Δφ)·σ_x is G_sync-covariant

**Result (Aug 2026):**
- ✅ Analytical eigenvalue formula exactly confirmed (Δ = 0 for all Δφ)
- ✅ Resonant case: ΔE = 2·ε·ℏΩ confirmed, deviation = 0
- Off-resonant case: Ω_eff(Δφ)/Ω_eff(0) ≠ cos(Δφ/2) — correct physics
  of the detuned two-level system (ω₀ floor term)
- Representation structure: Ĥ_res = Ĥ₀ + ε(Δφ)·ℏΩ·σ_x is the minimal
  realisation in the k=1 representation of U(1) ⊂ G_sync

**Parameters:** ω₀ = 1, Ω = 0.5

---

## Corollary A3 from A7 (RT-35)

The simulations confirm the quantisation condition derived in RT-02:

> **Corollary (A3 from A7):** The resonance condition fᵢ/fⱼ ∈ ℚ (Axiom A3)
> follows from the representation structure of the subgroup ℝ⁺_× ⊂ G_sync:
> Stable resonance configurations exist if and only if the frequency ratio
> is invariant under the fundamental representation of ℝ⁺_× — this is
> equivalent to fᵢ/fⱼ = m/n ∈ ℚ.

Formal documentation: `en/facts/theory/gsync_group_structure.md` §5

---

## Classification within the RFT research structure

| Task | Reference | Status |
|------|-----------|--------|
| RT-31 System 1 | `rt31_phonon_coupling.py` | ✅ Completed (Aug 2026) |
| RT-31 System 2 | `rt31_spin_orbit.py` | ✅ Completed (Aug 2026) |
| RT-02 G_sync proof | `en/facts/theory/gsync_group_structure.md` | ✅ Completed (Aug 2026) |
| RT-35 Corollary A3 | `en/facts/theory/gsync_group_structure.md` §5 | ✅ Resolved by RT-31 |
| RT-32 λε⁴ term | `RESEARCH_TASKS.md` | ⚠️ Open — next priority |

---

## Running the simulations

```bash
# System 1: Phonon-Phonon
python rt31_phonon_coupling.py

# System 2: Spin-Orbit
python rt31_spin_orbit.py
```

**Dependencies:** numpy, scipy

---

## References

- Theoretical basis: `en/facts/theory/gsync_group_structure.md`
- Axiom A7: `en/facts/docs/definitions/axiomatic_foundation.md` §A7
- Corollary A3: `en/facts/theory/gsync_group_structure.md` §5
- Predecessor simulations: `en/facts/theory/simulations/rt02/`
- German mirror: `de/fakten/simulationen/hamilton/`
- Research overview: `RESEARCH_TASKS.md` (RT-31)
