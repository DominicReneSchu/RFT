# 🌀 Warpantrieb

*Dominic-René Schu, 2025/2026*

Der **Warpantrieb** nutzt ein Zwei-Feld-Modell:
Fusionsfeld (Kontraktion) + Plateau-Feld (Expansion),
gesteuert über ε(Δφ) = cos²(Δφ/2).

> **Der Raum vorn schrumpft, hinten wächst.
> Das Schiff ruht lokal — keine Beschleunigung.
> ρ > 0 überall. Keine negative Energie nötig.**

---

## Kern-Ergebnis

| Messgröße | Wert |
|-----------|------|
| w(Δφ=0) | **+0.034** (Kontraktion, vorn) |
| w(Δφ=π/2) | **−0.024** (Expansion, hinten) |
| Δw (Gradient) | **+0.057** |
| Negative Energie? | **Nicht nötig** (ρ > 0 überall) |
| Beschleunigung im Schiff? | **Keine** (v_lokal = 0) |
| Effektive Geschwindigkeit | **Unbegrenzt** |
| Peak-Krümmung | 299× Sonnenmitte |
| RFT-Signatur | 2.5806 (exakt) |
| κ | 1 (parameterfrei) |

---

## Stufen

| Stufe | Inhalt | Status |
|-------|--------|--------|
| 1. Kaskade | Spaltung → Fusion → Energiedichte | ✅ |
| 2. Zwei-Feld | Kontraktion (ε₁) + Expansion (ε₂) | ✅ |
| 3. Warp-Profil | Vorzeichenwechsel Δw = +0.057 | ✅ |
| 4. Optimierung | V₀=0.5, λ₁=0.5, ε₂₀=3.0 | ✅ |
| 5. Energielücke | ~10⁵ Peak, Skalierungsgesetz ρ∝R⁻², R*>>1 AU (RT-33) | ✅ |
| 6. 3D-Blase | Vollständige Warp-Geometrie | ✅ |

---

## Dokumente

| Datei | Beschreibung |
|-------|-------------|
| [warpantrieb.md](warpantrieb.md) | Physik, Ergebnisse, Literatur |
| [warpantrieb.py](warpantrieb.py) | Simulation: 5 Experimente, 6 Plots |
| [warp_3d.py](warp_3d.py) | RT-34: 3D-Blase, GR-Solver, Falsifizierungstest |
| [analyse/rt33_energieluecke.py](analyse/rt33_energieluecke.py) | RT-33: Skalierungsgesetz, 4 Plots, CSV |
| [analyse/rt34_warpblase_3d.py](analyse/rt34_warpblase_3d.py) | RT-34: 3D-Analyse, Falsifizierung, GR-Solver |

---

## Ausführung

```bash
python warpantrieb.py    # → figures/ (6 Plots)
python warp_3d.py        # → figures/ (4 Plots, Falsifizierungstest, GR-Solver)
python analyse/rt34_warpblase_3d.py  # → RT-34 vollständige Analyse
```

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)