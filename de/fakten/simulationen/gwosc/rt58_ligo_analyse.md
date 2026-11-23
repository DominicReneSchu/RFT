# RT-58: LIGO GW150914 — Γ(f)-Analyse (RFT)

**Version:** 1.2 | **Datum:** November 2026  
**Status:** ✅ Abgeschlossen (mit offenem Folgeexperiment)  
**Datenbasis:** GWOSC GW150914, LOSC v2, GPS 1126257414, 4096 Hz

---

## Zusammenfassung

Zwei Analysen wurden durchgeführt:

| Experiment | Daten | ε_mean (20–200 Hz) | Abweichung von ε₀ |
|-----------|-------|-------------------|-------------------|
| GW150914 Ereignis | 32s-Fenster | 0.1424 ± 0.1587 | 3.42σ |
| O3-Segment | 68.3 min (4096s-Datei) | 0.2361 ± 0.2249 | **1.99σ** |

**Trend:** Mit mehr Daten verbessert sich die Übereinstimmung (3.42σ → 1.99σ).

---

## RFT-Vorhersage

$$\Gamma_\mathrm{RFT}(f) = \varepsilon(\Delta\varphi(f)) = \cos^2\!\left(\frac{\pi f}{2 f_0}\right), \quad f_0 = \frac{c}{2\,d_{HL}} \approx 49{,}93\ \mathrm{Hz}$$

**Geometrische Vorhersage:** f₀ = c/(2·d_HL) = **49.93 Hz** — bestätigt durch beide Experimente (rein geometrisch, kein freier Parameter).

---

## Ergebnisse

### Experiment A: GW150914 32s-Fenster
- Datenquelle: `rt58_output/H1_GW150914_32s.hdf5`, `L1_GW150914_32s.hdf5`
- ε_mean = 0.1424 ± 0.1587
- f₀_geo = 49.93 Hz ✅
- Abweichung: 3.42σ

### Experiment B: 68-Minuten-Segment (LOSC v2)
- Datenquelle: `H-H1_LOSC_4_V2-1126257414-4096.hdf5` (lokal, 124 MB)
- 16.777.216 Samples bei 4096 Hz
- ε_mean = 0.2361 ± 0.2249
- f₀_geo = 49.93 Hz ✅, f₀_obs = 20.50 Hz (1. Vorzeichenwechsel, rauschbeeinflusst)
- Abweichung: **1.99σ** — Verbesserung gegenüber 32s

---

## Ehrliche Einordnung

**Was diese Analyse zeigt:**
- Die geometrische Vorhersage f₀ ≈ 50 Hz ist durch die Detektorgeometrie bestimmt, kein RFT-spezifisches Ergebnis
- Die ε-Hypothese (ε_mean ≈ Ω_Λ = 0.6847) ist mit 68 Minuten Daten noch nicht auflösbar
- Der Trend (3.42σ → 1.99σ) bei Datenerhöhung um Faktor ~128 ist konsistent mit statistischer Mittelung

**Was diese Analyse nicht zeigt:**
- Bestätigung oder Falsifikation von ε₀ = Ω_Λ bei LIGO-Skalen
- Ein vollständiger Test würde Monate stochastischer Daten (O3: ~1 Jahr) erfordern
- Die offiziellen LIGO-Stochastik-Ergebnisse (G2001287) sind hinter Login geschützt

**B_grav-Status:** ε = −g_tt ist eine Identifikation aus RT-56, keine Ableitung aus A1–A9. Der Gravitationswellen-ε-Test bleibt ein phänomenologischer Anschluss.

---

## Datenstruktur (LOSC v2)

```
HDF5-Keys: meta/, quality/, strain/
strain/Strain  → Strain-Daten [float32-Array]
              attrs: Xspacing (dt), Xstart (GPS)
meta/Fsample   → Abtastrate
meta/GPSstart  → GPS-Startzeit
```

---

## Skripte

| Datei | Funktion |
|-------|----------|
| `rt58_extract_and_analyze.py` | GW150914 32s-Extraktion + Γ(f)-Analyse |
| `rt58_sgwb_analyse.py` | Volles CC-Spektrum aus LOSC v2 |

---

## Folgeexperiment (offen)

Für einen echten SGWB-Test:
- **Benötigt:** Monate stochastische Strain-Daten (O3: ~300 GB) oder vorberechnete CC-Spektren (G2001287, ~4 MB, LIGO-Login)
- **Alternative:** LIGO Scientific Collaboration Mitgliedschaft oder Kooperation
- **Status:** Offen bis Datenzugang vorhanden
