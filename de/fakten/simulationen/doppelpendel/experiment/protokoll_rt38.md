# RT-38 — Öffentliches Experimentprotokoll: Tabletop-Falsifizierungstest ε(Δφ) = cos²(Δφ/2)

**Status:** ✅ Protokoll abgeschlossen (Aug 2026) — Durchführung extern  
**Axiom:** A4 — Kopplungseffizienz ε(Δφ) = cos²(Δφ/2)  
**Budget:** ~100–300 €, ein Smartphone genügt  
**Auswertungssoftware:** bereits vorhanden (RT-08), siehe §5

> **Einladung zur Replikation:** Dieses Protokoll ist als offene Einladung formuliert.
> Wer diesen Test durchführt und Daten teilt, trägt zur empirischen Basis der RFT bei.
> Daten-Upload: Zenodo oder GitHub Issues (https://github.com/DominicReneSchu/RFT/issues)

---

## §1 — Wissenschaftliche Fragestellung

### Was wird getestet?

Axiom A4 der Resonanzfeldtheorie (RFT) postuliert, dass die Kopplungseffizienz
zwischen zwei Pendeln von ihrer Phasendifferenz Δφ = θ₂ − θ₁ abhängt:

$$
\varepsilon(\Delta\varphi) = \cos^2\!\left(\frac{\Delta\varphi}{2}\right)
$$

Diese Formel ist gruppentheoretisch eindeutig: Sie folgt aus der k=1-Darstellung
von U(1) ⊂ G_sync und ist nicht frei wählbar. Das Experiment prüft, ob diese
spezifische Phasenabhängigkeit in realen Messdaten nachweisbar ist.

### Hypothesen

**H₀ (Nullhypothese — Lagrange):**
Die Kopplungseffizienz im Doppelpendel folgt keiner spezifischen Phasenabhängigkeit,
die über die klassische Lagrange-Mechanik hinausgeht. Der RFT-Zusatzterm hat Amplitude
A = 0. ε_exp(Δθ) ist durch reine Lagrange-Mechanik vollständig beschrieben.

**H₁ (RFT-Hypothese):**
ε_exp(Δθ) = cos²(Δθ/2) — die k=1-Darstellung von U(1) ⊂ G_sync beschreibt die
Phasenabhängigkeit der Energieübertragung messbar besser als H₀. Die Kopplungsamplitude
A > 0 ist statistisch signifikant.

### Falsifizierungskriterium (aus RT-08)

| χ²_red | Bewertung |
|--------|-----------|
| ≤ 1.5 | ✅ H₁ nicht falsifiziert — ε(Δφ) = cos²(Δφ/2) beschreibt Daten |
| 1.5 < χ²_red ≤ 2.0 | ⚠️ Grenzbereich — systematische Fehler prüfen |
| > 2.0 | ❌ H₁ abgelehnt auf 5%-Niveau |

### Peer-Review-kritischer Punkt

**Frage:** „Ist ε = cos²(Δφ/2) nicht schon in der Lagrange-Mechanik enthalten?"

**Antwort (klar):** Nein. Die Lagrange-Mechanik des Doppelpendels enthält als natürliche
Kopplung Terme der Form sin(Δφ) und cos(Δφ) aus der gemeinsamen Aufhängung — aber keinen
Term mit der spezifischen Form cos²(Δφ/2). Der RFT-Term

$$
\tau_{\text{RFT}} = A \cdot \cos^2\!\left(\frac{\Delta\varphi}{2}\right) \cdot \sin(\Delta\varphi)
$$

ist *zusätzlich* zur natürlichen Lagrange-Kopplung. H₁ testet, ob A > 0 signifikant und
die Phasenabhängigkeit exakt die Form cos²(Δφ/2) hat — und nicht z.B. cos²(Δφ) oder
eine konstante Kopplung.

### Limitation aus RT-08

Der bisherige χ²-Test (χ²_red = 2,42, RT-08, Aug 2026) wurde auf **synthetischen** Daten
aus reiner Lagrange-Simulation (A = 0) durchgeführt. Dieses Ergebnis dokumentiert die
erwartete Abweichung zwischen RFT-Formel und rein klassischer Nullhypothese — ist aber kein
Ersatz für echte Messdaten. RT-38 liefert das Protokoll, um diesen Mangel zu beheben.

---

## §2 — Mechanischer Aufbau

### Stückliste

| Komponente | Spezifikation | Bezugsquelle (Beispiel) | Kosten ca. |
|---|---|---|---|
| Pendelarm 1 | Aluminiumstab 300 mm × 10 mm × 5 mm | Baumarkt / Amazon | 3 € |
| Pendelarm 2 | Aluminiumstab 250 mm × 10 mm × 5 mm | Baumarkt / Amazon | 3 € |
| Gelenk 1 (Achse) | Kugellager 608ZZ (8 mm Innen-Ø, 22 mm Außen-Ø) | Amazon / Conrad | 2 € |
| Gelenk 2 (Achse) | Kugellager 608ZZ (identisch) | Amazon / Conrad | 2 € |
| Achsen | Gewindestab M8 × 30 mm (2×) | Baumarkt | 1 € |
| Masse m₁ | Stahlmutter M8 oder Scheibe, definierte Masse ±0.1 g | Baumarkt | 1 € |
| Masse m₂ | Stahlmutter M8 oder Scheibe, definierte Masse ±0.1 g | Baumarkt | 1 € |
| Rahmen | Stahlwinkel 40×40×3 mm, ca. 200 mm Länge | Baumarkt | 5 € |
| Wandbefestigung | Fischer-Dübel + Schrauben (4×) | Baumarkt | 3 € |
| Bohrplatte | Aluplatte 100×100×5 mm als Aufhängungsplattform | Baumarkt | 5 € |
| Markierungen Variante A | Retroreflektierende Klebepunkte Ø 10 mm (Packung à 100) | Bürobedarf / Amazon | 5 € |
| Magnet Variante B | Neodym-Scheibenmagnet Ø 6 mm × 2,5 mm (2×, für AS5600) | Amazon | 3 € |
| Encoder Variante B | AS5600 magnetischer 12-bit I²C-Encoder (2× Breakout-Board) | Amazon / AliExpress | 10 € |
| Mikrocontroller Var. B | Arduino Nano oder Raspberry Pi Pico | Amazon | 10 € |
| Smartphone-Stativ | Mini-Tischstativ mit Kugelkopf | Amazon | 10 € |
| **Gesamtbudget Var. A** | | | **~50–80 €** |
| **Gesamtbudget Var. B** | | | **~100–150 €** |

*Alle Preise ca.-Angaben Stand 2026. Wer bereits ein Smartphone besitzt, kommt mit Variante A
unter 100 €. Die Encoder-Variante B empfiehlt sich für χ²_red < 1.5 bei weniger als 5 Runs.*

### Geometrische Anforderungen

- **L₁, L₂:** Länge der Pendelarme vom Drehpunkt zum Massenmittelpunkt, auf ±1 mm vermessen
  und im Systemparameter-Template dokumentieren
- **m₁, m₂:** Massen (Arm + befestigte Masse) auf ±0.5 g gewogen und dokumentieren
- **Gelenke:** Kugellager reinigen (Entfetter), reibungsarm und ohne messbares Spiel einbauen
  — Testkriterium: Pendelarm schwingt > 30 s frei ohne messbare Dämpfung
- **Aufhängung:** Wandmontage auf massivem Mauerwerk oder Stahlträger
  — Testkriterium: Rahmen-Eigenfrequenz > 10 × Pendelgrundfrequenz
  (Pendelfrequenz ≈ (1/2π)·√(g/L₁) ≈ 0.9 Hz bei L₁ = 300 mm → Rahmen > 9 Hz)

### Zusammenbau-Reihenfolge

1. Rahmen an Wand montieren und Horizontalität mit Wasserwaage prüfen
2. Pendelarm 1 mit Kugellager 608ZZ an Rahmen montieren — Spielfreiheit prüfen
3. Pendelarm 2 mit Kugellager 608ZZ am Ende von Arm 1 montieren
4. Massen am jeweiligen unteren Ende befestigen (Schraubenmutter + Kontermutter)
5. L₁ (Aufhängungspunkt → Gelenk 2) und L₂ (Gelenk 2 → Massenmittelpunkt m₂) messen
6. m₁ (Arm 1 + Masse) und m₂ (Arm 2 + Masse) auf Briefwaage wägen
7. Markierungen für Variante A anbringen: je ein retroreflektierender Punkt auf
   Gelenk 1 (Aufhängung), Gelenk 2 (Verbindung), Masse m₂

---

## §3 — Messkette: Zwei vollständige Varianten

### Variante A — Smartphone-Kamera (Minimalaufwand)

**Hardware:**
- Smartphone ab 2020 mit mindestens 60 fps (empfohlen 120 fps)
  Beispiele: iPhone 13+, Samsung Galaxy S21+, Google Pixel 6+
- Mini-Stativ, Kamera frontal und orthogonal zur Schwingungsebene
- Abstand Kamera–Pendel: mindestens 1 m (reduziert perspektivische Verzerrung)
- Beleuchtung: Helle gleichmäßige Hintergrundbeleuchtung oder Ringlicht vor der Kamera
  (retroreflektierende Markierungen + Ringlicht ergeben bestes Kontrastverhältnis)

**Aufnahme:**
- Videoformat: 1080p oder 4K, mindestens 60 fps
- Exportformat: MP4 oder MOV
- Vor der Messung: Kalibrierungsaufnahme mit einem Lineal oder bekanntem Abstand im Bild

**Software:** `kamera_tracking.py` (in diesem Verzeichnis)
```bash
pip install opencv-python numpy pandas
python kamera_tracking.py \
    --video run_1_20260801.mp4 \
    --output run_1_20260801.csv \
    --cal-length-mm 300 \
    --pivot-auto
```

**Ausgabe:** CSV mit Spalten `t,theta1,theta2` (Winkel in Rad), normiert auf (−π, π]

**Genauigkeit:** ±0.01–0.03 rad bei guter Beleuchtung und korrekter Kalibrierung

**Kalibrierung:**
1. Pendelarme in Ruhelage (hängend senkrecht) → Video aufnehmen
2. In `kamera_tracking.py`: bekannte Länge im Bild (z.B. L₁ = 300 mm) als Kalibriermaßstab angeben
3. Pivot-Punkt = Aufhängungspunkt von Arm 1 (retroreflektierender Punkt oder manuell setzen)
4. Vorzeichen: θ > 0 = nach rechts ausgelenkt (Konvention im Tracking-Skript Standard)
5. Kalibrierungsplot `cal_check.png` prüfen: θ_gemessen vs. θ_bekannt muss Steigung 1.0 ± 0.05

### Variante B — Rotationsencoder (höhere Präzision)

**Hardware:**
- 2× AS5600 magnetischer 12-bit I²C-Encoder (Breakout-Board)
- 2× Neodym-Scheibenmagnet Ø 6 mm × 2,5 mm, auf Achse des jeweiligen Kugellagers geklebt
- Arduino Nano oder Raspberry Pi Pico (I²C, 3.3 V oder 5 V je nach Board)
- USB-Kabel zur seriellen Datenübertragung an PC/Laptop

**Sampling-Rate:** 100–500 Hz (konfigurierbar im Arduino-Sketch)

**Software:** `encoder_auslese.ino` (Arduino) + `encoder_to_csv.py` (Python)
```bash
# Arduino-Sketch flashen (Arduino IDE oder arduino-cli)
arduino-cli compile --fqbn arduino:avr:nano encoder_auslese.ino
arduino-cli upload  --fqbn arduino:avr:nano -p /dev/ttyUSB0 encoder_auslese.ino

# Serielle Auslese starten
pip install pyserial pandas
python encoder_to_csv.py --port /dev/ttyUSB0 --duration 120 --output run_1_20260801.csv
```

**Ausgabe:** CSV mit Spalten `t,theta1,theta2` (Winkel in Rad, bereits kalibriert)

**Genauigkeit:** ±0.001 rad (12-bit bei 2π → 4096 Schritte → ≈0.0015 rad Auflösung)

**Kalibrierung:**
1. Beide Pendelarme senkrecht hängend: AS5600 zeigt 0° → `ZERO_OFFSET` im Sketch setzen
2. Arm manuell auf +90° (π/2) auslenken, Encoder-Wert prüfen: muss π/2 ± 0.01 rad zeigen
3. Vorzeichen: Uhrzeigersinn = positiv (konfigurierbar via `SIGN_THETA1` im Sketch)
4. I²C-Adresse: AS5600 hat feste Adresse 0x36 — bei zwei Encodern benötigt man
   einen I²C-Multiplexer (TCA9548A, ~3 €) oder zwei separate I²C-Busse

---

## §4 — Messprotokoll

### Schritt-für-Schritt

**Vor jeder Messreihe:**
1. Pendel in Ruhelage bringen (frei hängen lassen, 30 s warten)
2. Kalibrierung durchführen (Nullposition setzen, Skalierung prüfen)
3. Systemparameter in `system_params.json` eintragen (L₁, L₂, m₁, m₂, g_lokal)

**Pro Run:**
1. **Startbedingung einstellen:** Pendelarme auf Startwinkel θ₁(0), θ₂(0) bringen
   (Winkelmesser oder gedruckter Winkelschablone verwenden)
2. **Startbedingung dokumentieren:** θ₁(0), θ₂(0) auf ±0.01 rad notieren
   — beide Arme kurz loslassen → ω₁(0) = ω₂(0) ≈ 0 (oder asymmetrisch für Run 5)
3. **Messung starten:** Aufnahme/Encoder starten, dann Pendel loslassen
4. **Mindestmessdauer:** 120 Sekunden kontinuierlich
   (ergibt ~7200 Datenpunkte bei 60 fps oder ~12000 bei 100 Hz Encoder)
5. **Messung beenden:** Aufnahme stoppen, Datei sofort benennen und sichern

### Pflicht-Runs (5 unabhängige Runs)

| Run | θ₁(0) | θ₂(0) | ω₁(0) | ω₂(0) | Beschreibung |
|-----|--------|--------|--------|--------|--------------|
| 1 | π/4 (45°) | π/4 (45°) | 0 | 0 | Gleiche Phase — maximale RFT-Kopplung erwartet |
| 2 | π/2 (90°) | 0 (0°) | 0 | 0 | Verschiedene Phase — mittlere Kopplung |
| 3 | π/3 (60°) | 2π/3 (120°) | 0 | 0 | Asymmetrische Auslenkung |
| 4 | π/6 (30°) | 5π/6 (150°) | 0 | 0 | Nahe Gegenphase — minimale RFT-Kopplung erwartet |
| 5 | π/2 (90°) | π/2 (90°) | 0.5 rad/s | 0 | Asymmetrische Anfangsgeschwindigkeit |

*Run 1 und Run 4 sind die informativen Extremfälle (maximale vs. minimale erwartete Kopplung)
und sollten zuerst durchgeführt werden.*

### Dateiformat und Benennung

```
experiment/daten/
├── run_1_YYYYMMDD.csv      # z.B. run_1_20260801.csv
├── run_2_YYYYMMDD.csv
├── run_3_YYYYMMDD.csv
├── run_4_YYYYMMDD.csv
├── run_5_YYYYMMDD.csv
└── system_params.json
```

CSV-Header (exakt, keine Abweichung):
```
t,theta1,theta2
0.000,0.785,0.785
0.017,0.784,0.786
...
```

- `t`: Zeit in Sekunden (Float, Dezimalpunkt)
- `theta1`: Winkel Pendelarm 1 in Rad, normiert auf (−π, π]
- `theta2`: Winkel Pendelarm 2 in Rad, normiert auf (−π, π]

`system_params.json` (vollständig ausfüllen):
```json
{
  "L1_m": 0.300,
  "L2_m": 0.250,
  "m1_kg": 0.150,
  "m2_kg": 0.120,
  "g_ms2": 9.812,
  "measurement_date": "2026-08-01",
  "location": "Berlin, Deutschland",
  "hardware": "iPhone 14 Pro, 120 fps",
  "fps_or_samplerate_hz": 120,
  "notes": "Kugellager 608ZZ, retroreflektierende Markierungen"
}
```

*g_lokal: Ortsspezifischer Wert (Berlin: 9.8128, München: 9.8072, Wien: 9.8086)*
*Quelle: https://www.ptb.de/cms/themen/metrologie/basisgroessen/masse/schwere.html*

---

## §5 — Auswertung

### Schritt-für-Schritt

```bash
# 1. Repository klonen
git clone https://github.com/DominicReneSchu/RFT.git
cd RFT

# 2. Abhängigkeiten installieren
pip install numpy matplotlib scipy pandas

# 3. Auswertungsskript starten (einzelner Run)
python de/fakten/simulationen/doppelpendel/analyse/rt08_doppelpendel_vergleich.py \
    --data de/fakten/simulationen/doppelpendel/experiment/daten/run_1_20260801.csv \
    --params de/fakten/simulationen/doppelpendel/experiment/daten/system_params.json

# 4. Alternativ: über Umgebungsvariable
export RT08_DATA_FILE=de/fakten/simulationen/doppelpendel/experiment/daten/run_1_20260801.csv
python de/fakten/simulationen/doppelpendel/analyse/rt08_doppelpendel_vergleich.py
```

### Erwartete Ausgabe

Terminal-Tabelle:
```
=== RT-08 χ²-Fit: ε_RFT vs. ε_exp ===
Datenpunkte N      : 7200
χ²                 : XXXX.XX
Freiheitsgrade     : 7199
χ²_red             : X.XX
p-Wert             : X.XXXX
Residuen µ         : ±X.XXX
Residuen σ         : X.XXX
Urteil             : [confirmed / borderline / rejected]
```

Plots (gespeichert in `analyse/`):
- `rt08_scatter.png` — ε_exp vs. ε_RFT Streudiagramm
- `rt08_timeseries.png` — θ₁(t), θ₂(t), ε(t) Zeitreihe
- `rt08_residuals.png` — Residuen-Histogramm
- `rt08_chi2dist.png` — χ²-Verteilung mit markiertem Messwert

### Interpretation der Ergebnisse

| Ergebnis | Bedeutung | Nächster Schritt |
|---|---|---|
| χ²_red ≤ 1.5 | H₁ nicht falsifiziert — ε(Δφ) = cos²(Δφ/2) beschreibt echte Daten | Veröffentlichen, RFT-Ergebnis einreichen, Daten auf Zenodo teilen |
| 1.5 < χ²_red ≤ 2.0 | Grenzbereich — systematische Fehler möglich | Messkette verbessern: Encoder statt Kamera, Reibung reduzieren |
| χ²_red > 2.0 | H₁ abgelehnt — RFT-Formel durch echte Daten nicht gestützt | Axiom A4 überprüfen, Messsystem validieren |

### Alle 5 Runs auswerten

Alle Runs zusammen ergeben ein robusteres Ergebnis. Das Auswertungsskript
kann nacheinander auf jeden Run angewendet werden; die χ²_red-Werte über
alle Runs gemittelt ergeben den Gesamtbefund:

```bash
for i in 1 2 3 4 5; do
  python de/fakten/simulationen/doppelpendel/analyse/rt08_doppelpendel_vergleich.py \
      de/fakten/simulationen/doppelpendel/experiment/daten/run_${i}_YYYYMMDD.csv
done
```

---

## §6 — Häufige Fehlerquellen und Abhilfen

| Fehlerquelle | Symptom | Abhilfe |
|---|---|---|
| Rahmenschwingung | Periodisches Rauschen auf θ₁(t) bei Pendelfrequenz des Rahmens | Rahmen versteifen, Wandmontage auf massivem Mauerwerk |
| Gelenk-Reibung | Exponentielle Dämpfung, kinetische Energie < 95% nach 30 s | Kugellager reinigen (Entfetter) oder ersetzen |
| Kamera-Parallaxe | Systematischer Winkeloffset (θ_gemessen ≠ θ_tatsächlich) | Kalibrierung mit bekanntem Winkel erzwingen; Kamera ≥ 1 m Abstand |
| Tracking-Verlust | NaN-Werte oder Sprünge in CSV | Retroreflektierende Punkte + Ringlicht; `--min-area` in Tracking-Skript erhöhen |
| Numerische Drift | θ₁/θ₂ überschreiten ±2π | Winkel-Normierung auf (−π, π] im Tracking-Skript aktiviert (Standard) |
| Falsche Nullposition | θ(t) ≠ 0 in Ruhelage | Kalibrierung wiederholen, `ZERO_OFFSET` im Encoder-Sketch korrigieren |
| Kameralatenz | t-Spalte nicht gleichmäßig (unregelmäßige Lücken) | fps-Override in Tracking-Skript verwenden: `--fps 60` |
| AS5600 I²C-Konflikt | Encoder-Werte bleiben konstant oder springen | TCA9548A I²C-Multiplexer verwenden (beide Encoder auf Adresse 0x36) |

---

## §7 — Reproduzierbarkeitsanforderungen

Was ein unabhängiges Labor dokumentieren und melden muss, damit das Ergebnis
in der RFT-Ergebnissammlung anerkannt werden kann:

**Pflichtangaben:**
- [ ] Vollständige Systemparameter: L₁, L₂, m₁, m₂ mit Messprotokoll und Unsicherheit
- [ ] Kalibrierungsplot: θ_gemessen vs. θ_bekannt (Steigung, R², Residuen)
- [ ] Alle 5 CSV-Rohdaten-Dateien als öffentliche Daten (Zenodo-Upload empfohlen)
- [ ] χ²-Auswertungsplot und Terminal-Ausgabe (Screenshot oder Log-Datei)
- [ ] Datum und Ort der Messung
- [ ] Verwendete Hardware (Smartphone-Modell + fps oder Encoder-Typ + Sampling-Rate)
- [ ] g_lokal mit Quellenangabe

**Empfohlen:**
- [ ] Foto des aufgebauten Experiments (für methodische Transparenz)
- [ ] Video-Clips der einzelnen Runs (für Tracking-Validierung)
- [ ] Energie-Zeitreihe aus dem Analyseskript

**Ergebnis melden:**
Daten und Ergebnis als GitHub Issue melden:
https://github.com/DominicReneSchu/RFT/issues
(Label: `RT-38-result`)

---

## §8 — Verweise

- **Auswertungsskript (RT-08):** [`analyse/rt08_doppelpendel_vergleich.py`](../analyse/rt08_doppelpendel_vergleich.py)
- **Simulation:** [`doppelpendel.py`](../doppelpendel.py)
- **Theorie A4:** [`de/fakten/theorie/axiomatische_grundlegung.md`](../../../theorie/axiomatische_grundlegung.md)
- **Gruppenstruktur:** [`de/fakten/theorie/gsync_gruppenstruktur.md`](../../../theorie/gsync_gruppenstruktur.md)
- **Tracking-Skript:** [`kamera_tracking.py`](kamera_tracking.py)
- **Encoder-Skript:** [`encoder_auslese.ino`](encoder_auslese.ino) + [`encoder_to_csv.py`](encoder_to_csv.py)
- **Systemparameter-Template:** [`system_params_template.json`](system_params_template.json)
- **EN-Version:** [`en/facts/simulations/double_pendulum/experiment/protocol_rt38.md`](../../../../../en/facts/simulations/double_pendulum/experiment/protocol_rt38.md)

---

*RT-38 — Öffentliches Experimentprotokoll — Tabletop-Falsifizierungstest ε(Δφ) = cos²(Δφ/2)*  
*© Dominic-René Schu, 2026 — Resonanzfeldtheorie*
