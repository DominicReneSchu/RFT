# 🌀 Warpantrieb

*Dominic-René Schu, 2025/2026*

Der **Warpantrieb** überträgt das Prinzip des Kraftfeldgenerators
auf die Raumzeit: Statt Ultraschall-Transducer fokussieren
Resonanzreaktoren kohärente Energie auf einen Punkt. Die
Energiedichte erzeugt über Einsteins Feldgleichungen lokale
Raumzeitkrümmung — steuerbar über ε(Δφ) = cos²(Δφ/2).

> **Gleiche Gleichung. Von Schall über Kernphysik
> bis zur Raumzeit.**

---

## Stufen

| Stufe | Inhalt | Status |
|-------|--------|--------|
| 1. Etabliert | RFT + ART: η = cos² in FLRW-Raumzeit | ✅ Simuliert |
| 2. Extrapolation | Fokussierte Reaktoren → lokale Krümmung | ⚠️ Simuliert |
| 3. Vision | Alcubierre-Blase durch asymmetrische Anordnung | ❌ Offen |

---

## Ergebnisse

| Messgröße | Wert |
|-----------|------|
| Phasenscan | ρ(Δφ) ∝ cos⁴(Δφ/2) bestätigt |
| Skalierung | ρ ∝ N² (kohärent) |
| Asymmetrie | ρ_vorn >> ρ_hinten (Warp-Geometrie) |
| Steuerung | Δφ=0 (an), Δφ=π (aus) |
| Energielücke | ~10⁴³ (ehrlich dokumentiert) |

---

## Dokumente

| Datei | Beschreibung |
|-------|-------------|
| [warpantrieb.md](warpantrieb.md) | Physik, Ergebnisse, Energielücke |
| [warpantrieb.py](warpantrieb.py) | Simulation: 4 Experimente |

---

## Ausführung

```bash
python warpantrieb.py    # → figures/ (4 Plots)
```

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)