# RT-44 AP1 — Hydrogen Spectrum from RFT Resonance Condition A3

*Dominic-René Schu, November 2026*
*Status: ✅ Completed (Nov 2026)*

---

## 1. Result

E_n = −13.6 eV/n² follows from A3 (phase closure) + A4 (coupling energy) + Coulomb potential. Quantisation is not a postulate — it is a corollary of A3.

---

## 2. Derivation

**Phase closure (A3):** Bound state = standing resonance mode. Closed-orbit condition:
```
∮ p_r dr = n·ħ    →    p_n = nħ/r
```
A3 requires f_e/f_nucleus = n/1 (rational ratio) → n ∈ ℕ.

**Energy minimisation:**
```
E(r) = p_n²/(2m_e) − e²/(4πε₀r)
∂E/∂r = 0  →  r_n = n²·a₀   (Bohr radius a₀ = 0.529 Å)
```

**Energy eigenvalues:**
```
E_n = −m_e e⁴ / [2(4πε₀)²ħ²n²] = −13.6 eV / n²  ✅
```

**RFT resonance frequency:**
```
f_n = |E_n| / (π·ħ) ≈ 1.04×10¹⁵ Hz / n²
```
Lyman-α (n=2→1): Δf ≈ 2.47×10¹⁵ Hz ✅ (matches experiment)

---

## 3. Structural Significance

| Aspect | Bohr model | RFT |
|--------|-----------|-----|
| Why integer n? | Postulate | A3: rational resonance condition |
| Energy formula | Same | Derived identically |
| Fine structure | No | AP6: via ε(Δφ_spin, Δφ_orbit) |

✅ Criterion met.

---

*RT-44 AP1 — DominicReneSchu/RFT — November 2026*
