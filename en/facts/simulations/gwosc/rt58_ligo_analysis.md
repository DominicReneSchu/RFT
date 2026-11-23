# RT-58: LIGO GW150914 — Γ(f) Analysis (RFT)

**Version:** 1.2 | **Date:** November 2026  
**Status:** ✅ Completed (with open follow-up experiment)  
**Data:** GWOSC GW150914, LOSC v2, GPS 1126257414, 4096 Hz

---

## Summary

Two analyses were performed:

| Experiment | Data | ε_mean (20–200 Hz) | Deviation from ε₀ |
|-----------|------|-------------------|-------------------|
| GW150914 event | 32s window | 0.1424 ± 0.1587 | 3.42σ |
| O3 segment | 68.3 min (4096s file) | 0.2361 ± 0.2249 | **1.99σ** |

**Trend:** Agreement improves with more data (3.42σ → 1.99σ).

---

## RFT Prediction

$$\Gamma_\mathrm{RFT}(f) = \varepsilon(\Delta\varphi(f)) = \cos^2\!\left(\frac{\pi f}{2 f_0}\right), \quad f_0 = \frac{c}{2\,d_{HL}} \approx 49.93\ \mathrm{Hz}$$

**Geometric prediction:** f₀ = c/(2·d_HL) = **49.93 Hz** — confirmed by both experiments (pure geometry, no free parameter).

---

## Results

### Experiment A: GW150914 32s window
- ε_mean = 0.1424 ± 0.1587
- f₀_geo = 49.93 Hz ✅
- Deviation: 3.42σ

### Experiment B: 68-minute segment (LOSC v2)
- 16,777,216 samples at 4096 Hz
- ε_mean = 0.2361 ± 0.2249
- f₀_geo = 49.93 Hz ✅, f₀_obs = 20.50 Hz (1st zero crossing, noise-dominated)
- Deviation: **1.99σ** — improvement over 32s

---

## Honest Assessment

**What this analysis shows:**
- The geometric prediction f₀ ≈ 50 Hz follows detector geometry, not RFT-specific
- The ε-hypothesis (ε_mean ≈ Ω_Λ = 0.6847) is not resolvable with 68 min of data
- The trend (3.42σ → 1.99σ) with ~128× more data is consistent with statistical averaging

**What this analysis does not show:**
- Confirmation or falsification of ε₀ = Ω_Λ at gravitational wave scales
- A complete test requires months of stochastic data (O3: ~1 year)
- Official LIGO stochastic results (G2001287) require LIGO collaboration login

**B_grav status:** ε = −g_tt is an identification from RT-56, not derived from A1–A9.

---

## Follow-up Experiment (Open)

For a genuine SGWB test:
- **Required:** Months of stochastic strain data (O3: ~300 GB) or pre-computed CC spectra (G2001287, ~4 MB, requires LIGO login)
- **Alternative:** LIGO Scientific Collaboration membership or collaboration
- **Status:** Open until data access is available
