# RT-01b — Numerisches Pfadintegral: π-Herleitung

*Dominic René Schu, August 2026*

## Zweck

Dieses Verzeichnis enthält die numerische Auswertung des Pfadintegrals der
Resonanzkopplung im Rahmen von RT-01b. Es schließt die drei offenen Punkte aus
RT-01 §6:

1. **Stufe 1** — Numerische Auswertung des Pfadintegrals (Konvergenztest)
2. **Stufe 2** — Quantifizierung der Nicht-Gaussian-Korrekturen
3. **Stufe 3** — Potenzial-Unabhängigkeit des π-Beitrags

## Dateien

| Datei | Beschreibung |
|---|---|
| `rt01b_path_integral.py` | Hauptskript: Pfadintegral, Korrekturen, Potenzialvergleich |
| `README.md` | Diese Datei |

## Verwendung

```bash
python rt01b_path_integral.py
```

Voraussetzungen: Python 3.10+, NumPy ≥ 2.0, SciPy

## Ergebnisse (August 2026)

### Stufe 1 — Konvergenz

| N | π-Schätzung | Fehler |
|---|---|---|
| 100 | 3.14159265 | < 1e-15 |
| 500 | 3.14159265 | < 1e-15 |
| 1000 | 3.14159265 | < 1e-15 |

Das numerische Pfadintegral konvergiert gegen π mit maschinengenauer Präzision.

### Stufe 2 — Nicht-Gaussian-Korrekturen

| Korrektur | Wert |
|---|---|
| c_3 (dritte Ordnung) | 0 (verschwindet aus Symmetriegründen) |
| c_4 (vierte Ordnung) | ≈ 5.5 × 10⁻¹¹ |
| \|c_3 + c_4\| | ≈ 5.5 × 10⁻¹¹ < 10⁻³ |

**Gaussian-Näherung kontrolliert**: Die Nicht-Gaussian-Korrekturen sind mehr als acht
Größenordnungen unterhalb der Anforderungsschranke von 10⁻³.

### Stufe 3 — Potenzial-Unabhängigkeit

| Potential | ∫V dφ | 2·∫V dφ | Beitrag π? |
|---|---|---|---|
| cos²(φ/2) [RT-01 Original] | π/2 | π | ✓ |
| sin²(φ/2) [komplementär] | π/2 | π | ✓ |
| φ(π−φ)/π² [parabolisch] | π/6 | π/3 | ~ |
| 1/2 [konstant] | π/2 | π | ✓ |
| 1 [trivial] | π | 2π | ~ |

π tritt für alle Potenziale mit Mittelwert 1/2 auf dem Intervall [0,π] auf.
**Schlussfolgerung:** π ist eine Eigenschaft der Phasenraumgeometrie [0,π],
nicht des spezifischen Potenzials.

## Einordnung

Diese Simulation ist Bestandteil von RT-01b (August 2026) und dokumentiert die
unabhängige Bestätigung der π-Herleitung aus RT-01. Die Ergebnisse fließen in
§4.5 und §9 von `wirkungsintegral_pi_herleitung.md` ein.

---

*Verwandt:* [../../../wirkungsintegral_pi_herleitung.md](../../../wirkungsintegral_pi_herleitung.md) |
[../../../../../RESEARCH_TASKS.md](../../../../../RESEARCH_TASKS.md) RT-01b
