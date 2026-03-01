# 🌀 Warpantrieb

*Dominic-René Schu, 2025/2026*

Der **Warpantrieb** nutzt eine dreistufige Kaskade:
Resonanzreaktoren (Spaltung) treiben Trägheitsfusion,
die Fusionsenergie erzeugt lokale Raumzeitkrümmung —
steuerbar über ε(Δφ) = cos²(Δφ/2).

> **Gleiche Gleichung. Der Resonanzreaktor liefert die
> Treiberenergie. Der Kraftfeldgenerator schützt das Schiff.
> Die Fusion liefert die Dichte. Die Phase steuert alles.**

---

## Stufen

| Stufe | Inhalt | Status |
|-------|--------|--------|
| 1. Etabliert | RFT + ART: η = cos² in FLRW-Raumzeit | ✅ Simuliert |
| 2. Extrapolation | Spaltung → Fusion → lokale Krümmung | ⚠️ Simuliert |
| 3. Vision | Alcubierre-Blase (Lücke: ~10⁵ Peak) | ❌ Offen |

---

## Zentrale Ergebnisse

| Messgröße | Wert |
|-----------|------|
| Treiberleistung | 12 × 100 MW = 1.2 GW |
| Fusionsenergie | 180 MJ / Puls (Gain 1.5×) |
| ρ_Pellet (zeitgemittelt) | 4.3 × 10¹⁶ J/m³ |
| ρ_Peak (während Burn, 10 ns) | 4.3 × 10²⁴ W/m³ |
| R_Pellet | 8.0 × 10⁻¹⁰ 1/m² |
| R_Peak | 8.0 × 10⁻² 1/m² (300× Sonnenmitte) |
| Phasenscan | ρ(Δφ) ∝ cos⁴(Δφ/2) bestätigt |
| RFT-Signatur | ρ(0)/⟨ρ⟩ = 2.5806 (exakt) |
| Asymmetrie | ρ_vorn >> ρ_hinten (Warp-Geometrie) |
| Energielücke zu Alcubierre | ~10⁵ (Peak), ~10¹³ (stetig) |
| κ | 1 (parameterfrei) |

---

## Dokumente

| Datei | Beschreibung |
|-------|-------------|
| [warpantrieb.md](warpantrieb.md) | Physik, Kaskade, Ergebnisse, Energielücke |
| [warpantrieb.py](warpantrieb.py) | Simulation: 4 Experimente, 4 Plots |

---

## Ausführung

```bash
python warpantrieb.py    # → figures/ (4 Plots)
```

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)