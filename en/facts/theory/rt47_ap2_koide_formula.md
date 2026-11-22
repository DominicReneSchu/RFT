# RT-47 AP2 — Koide Formula from RFT Resonance Structure

*Dominic-René Schu, November 2026*
*Status: ✅ Completed (Nov 2026)*

---

## 1. Result

The Koide formula Q = 2/3 follows from **three-fold symmetric resonance coupling** in G_sync (A3+A7) — no free parameters, Stage 2.

---

## 2. Brannen Representation

The Koide formula is equivalent to: the three lepton masses lie on a **circle in √m-coordinates**:

```
√m_n = M · (1 + √2 · cos(θ + 2π(n−1)/3)),   n = 1,2,3
M = (√m_e + √m_μ + √m_τ)/3,   θ ≈ 0.23 rad
```

**Numerical check:** Q = 0.66661 ≈ 2/3, deviation < 0.001%.

---

## 3. RFT Derivation

**A3:** Three-fold resonance requires Δφ_ij = 2π/3 (uniform spacing on circle).
```
ε(2π/3) = cos²(π/3) = 1/4   (all pairs couple equally)
```

**A7 (G_sync invariance):** The only G_sync-invariant 3-mode configuration is the symmetric circle distribution (Δφ = 2π/3 for all pairs). Any asymmetric configuration is reachable by a G_sync transformation → not distinguished.

**Result:** A3 + A7 → uniform phase distribution → **Q = 2/3** (geometrically enforced).

---

## 4. Predictions

| Family | Q | Explanation |
|--------|---|-------------|
| Leptons (e,μ,τ) | 2/3 (exact) | No QCD correction |
| Down quarks | < 2/3 | QCD correction expected |
| Up quarks | < 2/3 | Stronger QCD correction |
| Neutrinos | 2/3 (predicted) | No QCD, same as leptons |

**Falsification:** Q_leptons ≠ 2/3 at > 5σ → A3+A7 derivation falsified.

✅ Stage 2: explanatory advantage with 0 free parameters.

---

*RT-47 AP2 — DominicReneSchu/RFT — November 2026*
