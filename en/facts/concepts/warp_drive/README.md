# 🌀 Warp Drive

*Dominic-René Schu, 2025/2026*

The **warp drive** uses a two-field model:
Fusion field (contraction) + plateau field (expansion),
controlled via ε(Δφ) = cos²(Δφ/2).

> **Space contracts in front, expands in the rear.
> The ship rests locally — no acceleration.
> ρ > 0 everywhere. No negative energy required.**

---

## Core Result

| Quantity | Value |
|----------|-------|
| w(Δφ=0) | **+0.034** (Contraction, front) |
| w(Δφ=π/2) | **−0.024** (Expansion, rear) |
| Δw (Gradient) | **+0.057** |
| Negative energy? | **Not required** (ρ > 0 everywhere) |
| Acceleration in the ship? | **None** (v_local = 0) |
| Effective velocity | **Unlimited** |
| Peak curvature | 299× solar core |
| RFT signature | 2.5806 (exact) |
| κ | 1 (parameter-free) |

---

## Stages

| Stage | Content | Status |
|-------|---------|--------|
| 1. Cascade | Fission → Fusion → Energy density | ✅ |
| 2. Two-field | Contraction (ε₁) + Expansion (ε₂) | ✅ |
| 3. Warp profile | Sign change Δw = +0.057 | ✅ |
| 4. Optimization | V₀=0.5, λ₁=0.5, ε₂₀=3.0 | ✅ |
| 5. Energy gap | ~10⁵ peak, scaling problem | ⚠️ |
| 6. 3D bubble | Complete warp geometry | ❌ |

---

## Documents

| File | Description |
|------|-------------|
| [warp_drive.md](warp_drive.md) | Physics, results, references |
| [warp_drive.py](warp_drive.py) | Simulation: 5 experiments, 6 plots |

---

## Execution

```bash
python warp_drive.py    # → figures/ (6 plots)
```

---

© Dominic-René Schu — Resonance Field Theory 2025/2026

---

[Back to overview](../../../README.md)
