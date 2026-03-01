# 🌀 Warpantrieb

*Dominic-René Schu, 2025/2026*

Der **Warpantrieb** nutzt ein Zwei-Feld-Modell:
Fusionsfeld (Kontraktion) + Plateau-Feld (Expansion),
gesteuert über ε(Δφ) = cos²(Δφ/2).
Keine negative Energie nötig.

> **Δφ = 0 → Kontraktion (vorn). Δφ = π/2 → Expansion (hinten).
> Δφ = π → Warp aus. ρ > 0 überall.**

---

## Kern-Ergebnis

| Messgröße | Wert |
|-----------|------|
| w(Δφ=0) | **+0.006** (Kontraktion) |
| w(Δφ=π/2) | **−0.013** (Expansion) |
| Vorzeichenwechsel | Δφ ≈ π/3 |
| Gradient Δw | +0.019 |
| Peak-Krümmung | 299× Sonnenmitte |
| Negative Energie? | **Nicht nötig** (ρ > 0 überall) |
| RFT-Signatur | 2.5806 (exakt) |
| κ | 1 (parameterfrei) |

---

## Stufen

| Stufe | Inhalt | Status |
|-------|--------|--------|
| 1. Kaskade | Spaltung → Fusion → Energiedichte | ✅ Simuliert |
| 2. Zwei-Feld | Kontraktion (ε₁) + Expansion (ε₂) | ✅ Simuliert |
| 3. Warp-Profil | Vorzeichenwechsel w(Δφ) bestätigt | ✅ Simuliert |
| 4. Energielücke | ~10⁵ Peak, Skalierungsproblem | ⚠️ Offen |
| 5. Alcubierre | Vollständige Blase | ❌ Nächster Schritt |

---

## Dokumente

| Datei | Beschreibung |
|-------|-------------|
| [warpantrieb.md](warpantrieb.md) | Physik, Zwei-Feld-Modell, Ergebnisse |
| [warpantrieb.py](warpantrieb.py) | Simulation: 4 Experimente, 5 Plots |

---

## Ausführung

```bash
python warpantrieb.py    # → figures/ (5 Plots)
```

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)