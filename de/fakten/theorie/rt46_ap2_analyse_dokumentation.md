# RT-46 AP2–AP7 — Vollständige Analyse-Dokumentation

*Dominic-René Schu, November 2026*
*Status: ✅ Analyse-Pipeline fertig; Zenodo-Daten extern abrufen (RT-46 Kern offen)*

---

## Status: Was abgeschlossen ist, was noch fehlt

| Schritt | Status | Anmerkung |
|---------|--------|-----------|
| AP1: Datensatz-Identifikation | ✅ | Zenodo 6633719 identifiziert |
| AP2: Pre-Registrierung | ✅ | H0/H1, Falsifikationskriterien |
| AP3: Analyse-Pipeline | ✅ | Python-Skript fertig, getestet |
| AP4: Synthetische Validierung | ✅ | Pipeline funktioniert korrekt |
| AP5: Echter Daten-Test | ⚠️ **OFFEN** | Zenodo-Daten extern herunterladen |
| AP6: Robustheitsprüfung | ⚠️ Nach AP5 | Multiple Seeds, Fenstergröße |
| AP7: Dokumentation | ✅ | Diese Datei |

---

## Hypothesen (pre-registriert)

**H0 (Null):** ε_exp(Δφ) = const — keine Δφ-Abhängigkeit.
**H1 (RFT):** ε_exp(Δφ) = cos²(Δφ/2) — RFT-Kopplungsmuster.

**Falsifikationskriterium:**
χ²_red(H1) ≥ χ²_red(H0) → H1 (RFT) falsifiziert.
χ²_red(H1) < χ²_red(H0) → Konsistent mit RFT (kein Beweis, keine Falsifikation).

---

## Synthetische Validierung der Pipeline

Getestet mit bekannten Eingabedaten (ε = cos²(Δφ/2) eingebaut):
Pipeline erkennt H1 korrekt als bessere Anpassung als H0. ✅

---

## Konkreter nächster Schritt

```bash
# 1. Daten herunterladen
curl -L "https://zenodo.org/records/6633719/files/[filename].zip" -o data.zip
unzip data.zip -d RT46_data/

# 2. Analyse ausführen
python de/fakten/simulationen/doppelpendel/rt46_doppelpendel_analyse.py RT46_data/experiment_01.csv

# 3. Ergebnis prüfen
cat rt46_results.json
```

---

## Ehrliche Einschätzung (RT-46 Originalformulierung bestätigt)

> Die Wahrscheinlichkeit, dass die öffentlichen Daten **ausreichen**, ist **moderat bis hoch**.
> Die Wahrscheinlichkeit, dass RFT H1 signifikant **bestätigt** wird, ist **gering** —
> die Standard-Hamilton-Dynamik ist bereits extrem gut validiert.
>
> Ehrlichster Ausgang: RFT-Kopplungseffizienz konsistent aber nicht signifikant unterscheidbar.

---

*RT-46 AP2–AP7 — DominicReneSchu/RFT — November 2026*
