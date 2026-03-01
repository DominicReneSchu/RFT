# 🛡️ Kraftfeldgenerator

*Dominic-René Schu, 2025/2026*

Der **Kraftfeldgenerator** erzeugt räumlich strukturierte
akustische Druckfelder durch phasengesteuerte Transducer-Arrays.
Stehende Ultraschallwellen bilden unsichtbare Barrieren, die
Partikel (Staub, Insekten, Aerosole) aufhalten, aber für
Menschen durchlässig bleiben.

> **Die RFT-Grundgleichung E = π · ε(Δφ) · ℏ · f optimiert
> die Phasensteuerung der Transducer: ε(Δφ) = cos²(Δφ/2) gibt
> das exakte Optimum für maximale Energiedichte am Fokuspunkt.**

---

## Zentrale Ergebnisse

| Messgröße | Wert |
|-----------|------|
| Transducer-Array | 16×16 = 256 Elemente bei 40 kHz |
| Fokusgewinn (RFT-optimiert vs. inkohärent) | Faktor 2.0× |
| Druckfeld am Fokus (Δφ = 0) | max. P_rad ∝ N² |
| Phasensignatur | ε(Δφ) = cos²(Δφ/2) exakt bestätigt |
| Barrierenbreite | Steuerbar über Phasenprofil |
| κ | 1 (parameterfrei, wie Resonanzgenerator und -reaktor) |

---

## Anwendungen

### 1. Insektenschutz (Fenster/Türen)
```
Ultraschall-Array im Türrahmen → stehende Welle
→ Partikel > 0.5 mm werden in Druckknoten gehalten
→ Menschen gehen durch (Wellenlänge << Körper)
→ Insekten werden abgelenkt/gestoppt
```

### 2. Reinraumbarrieren (Industrie/Pharma)
```
Akustische Vorhänge zwischen Zonen
→ Partikel < 10 µm in Druckknoten gefangen
→ Kein physischer Vorhang nötig
→ Freier Durchgang für Personal und Material
```

### 3. Staubschutz (Museen, Optik, Elektronik)
```
Lokale Barriere um empfindliche Objekte
→ Schwebende Partikel von Oberfläche fernhalten
→ Berührungsloser Schutz
```

---

## Axiom-Zuordnung

| Axiom | Anwendung |
|-------|----------|
| A1 (Universelle Schwingung) | Luft als Schwingungsmedium, f = 40 kHz |
| A3 (Resonanzbedingung) | Stehende Welle bei Barrierenresonanz |
| A4 (Kopplungsenergie) | E = π · ε · ℏ · f bestimmt Energiedichte |
| A5 (Energierichtung) | Transducer → Fokuspunkt → Barriere |
| A7 (Invarianz) | Gleiche Gleichung wie Resonanzgenerator/Reaktor |

---

## Dokumente

| Datei | Beschreibung |
|-------|-------------|
| [kraftfeldgenerator.md](kraftfeldgenerator.md) | Physik, Ergebnisse, Anwendungen |
| [kraftfeldgenerator.py](kraftfeldgenerator.py) | Simulation: Transducer-Array, Phasenscan, Barriere |
| [wand_animation_ultimate.py](wand_animation_ultimate.py) | Visualisierung: 2D-Feldanimation (Legacy) |

---

## Ausführung

```bash
python kraftfeldgenerator.py       # → figures/ (4 Plots + Konsole)
```

---

## Zusammenfassung

```
Grundformel:   E = π · ε(Δφ) · ℏ · f
Kopplung:      ε = cos²(Δφ/2), κ = 1
Bestätigt:     Fokusgewinn 2× durch Phasenoptimierung
Anwendung:     Akustische Barrieren (Insektenschutz, Reinraum)
Verbindung:    Gleiche Formel wie Resonanzgenerator und -reaktor
```

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)