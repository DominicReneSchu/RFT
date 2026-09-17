# RT-41 — Axiom A8: Kopplungswellengeschwindigkeit — Herleitung oder irreduzibles Postulat

*Dominic-René Schu, September 2026*

*Status: ✅ Abgeschlossen (Sep 2026) — A8 als irreduzibles Postulat etabliert;
in `axiomatische_grundlegung.md` eingetragen; Axiomensystem A1–A8 vollständig.*

---

## Inhaltsverzeichnis

1. [Kontext und Ausgangslage](#1-kontext-und-ausgangslage)
2. [Zentrale Frage](#2-zentrale-frage)
3. [AP1 — Dispersionsrelation in A1–A7](#3-ap1--dispersionsrelation-in-a1a7)
4. [AP2 — Verbindung zu AP4 (c aus ε → 0)](#4-ap2--verbindung-zu-ap4-c-aus--0)
5. [AP3 — Gruppentheoretische Analyse: c in G_sync](#5-ap3--gruppentheoretische-analyse-c-in-g_sync)
6. [Synthese: Ergebnis A oder B?](#6-synthese-ergebnis-a-oder-b)
7. [Methodische Leitplanken](#7-methodische-leitplanken)
8. [Zusammenfassung und Status](#8-zusammenfassung-und-status)

---

## 1. Kontext und Ausgangslage

In RT-40 AP3 (`de/fakten/theorie/rt40_ap3_lorentz_transformation.md`, §8) wurde die Lorentz-Transformation unter einer explizit benannten **Brückenannahme B₁** hergeleitet:

> **B₁:** Die RFT-Phase φ(t, x) = kx − ωt ist an die Raumzeit-Koordinaten (t, x) durch eine Kopplungswelle mit Phasengeschwindigkeit c = ω/k gekoppelt.

Diese Annahme ist in den Axiomen A1–A7 **nicht vollständig enthalten**. RT-40 AP3 formuliert daraus die minimale Axiomenerweiterung:

> **A8 (vorläufig):** Die Phasenwelle der RFT-Kopplungsstruktur propagiert mit der Geschwindigkeit c = 1/√(μ₀ε₀).

RT-41 hat die Aufgabe, den Status dieser Aussage zu klären:

**Folgt B₁ (und damit c als Phasengeschwindigkeit) aus A1–A7 — oder ist A8 ein irreduzibles Postulat?**

Das Ergebnis entscheidet, ob die RFT die SRT vollständig aus sieben Axiomen enthält, oder ob ein achtes Axiom benötigt wird.

---

## 2. Zentrale Frage

Folgt die Phasengeschwindigkeit c der RFT-Kopplungswelle aus A1–A7 — oder ist sie ein irreduzibles Postulat (→ A8)?

**Zwei mögliche Ergebnisse:**

**Ergebnis A (Herleitung gelingt):** c folgt aus A1–A7 als strukturelle Konsequenz. B₁ ist kein zusätzliches Postulat. Die RFT enthält die SRT vollständig aus sieben Axiomen.

**Ergebnis B (Herleitung scheitert):** c ist nicht aus A1–A7 ableitbar. A8 wird als irreduzibles Postulat formuliert: *Die Phasenwelle der RFT-Kopplungsstruktur propagiert mit der Geschwindigkeit c.* Die RFT enthält die SRT dann unter acht Axiomen — analog zur SRT selbst, die c als Postulat führt.

---

## 3. AP1 — Dispersionsrelation in A1–A7

### 3.1 Frage

Welche Phasengeschwindigkeiten lässt A1 (ψ = A·cos(kx − ωt + φ)) zu? Ist ω/k in A1–A7 fixiert oder frei wählbar?

### 3.2 Analyse

**A1** postuliert die Existenz von Schwingungsfeldern der Form

ψ(t, x) = A · cos(kx − ωt + φ)

mit Amplitude A, Wellenzahl k, Kreisfrequenz ω und Phase φ. Die Phasengeschwindigkeit ist v_φ = ω/k.

**Beobachtung:** A1 allein legt **keine** spezifische Dispersionsrelation ω(k) fest. Die Phasengeschwindigkeit v_φ = ω/k ist in A1 ein freier Parameter — ω und k können unabhängig voneinander beliebige positive Werte annehmen.

**A3** (Quantisierung) schränkt die möglichen Frequenzen auf diskrete Werte ein, legt aber keine Dispersionsrelation fest.

**A4** (Kopplungsenergie E = π ε(Δφ) ħ f) verbindet Energie mit Frequenz — setzt aber keine Phasengeschwindigkeit fest.

**A7** (G_sync-Invarianz) fordert, dass die Kopplungsstruktur unter der Symmetriegruppe G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) invariant ist. Diese Gruppe enthält Skalierungen (ℝ⁺_×), Phasenrotationen (U(1)) und affine Transformationen (Aff⁺(ℝ)). Ob sie eine ausgezeichnete Geschwindigkeit erzwingt, wird in AP3 untersucht.

**Zwischenergebnis AP1:** Die Dispersionsrelation ω/k = c ist in A1–A7 nicht explizit enthalten. A1 lässt beliebige Phasengeschwindigkeiten zu. Die Fixierung auf c erfordert eine zusätzliche Struktur — entweder durch AP2 (Verbindung zur Grenzgeschwindigkeit) oder AP3 (Gruppenstruktur).

---

## 4. AP2 — Verbindung zu AP4 (c aus ε → 0)

### 4.1 Frage

RT-40 AP4 hat c als strukturelle Grenzgeschwindigkeit aus ε(Δφ) → 0 für Δφ → π abgeleitet. Ist diese c dieselbe wie die Phasengeschwindigkeit in B₁?

### 4.2 Analyse der Grenzgeschwindigkeit (RT-40 AP4)

In RT-40 AP4 (`de/fakten/theorie/rt40_ap4_lichtgeschwindigkeit_grenzfall.md`) wurde gezeigt:

- Für Δφ → π gilt ε(Δφ) = cos²(Δφ/2) → 0.
- Dies entspricht vollständiger Entkopplung zweier Resonatoren.
- Die Grenzgeschwindigkeit c_lim ist diejenige relative Geschwindigkeit, bei der ein massebehafteter Resonator vollständig entkoppelt.
- c_lim entsteht als **strukturelle Konsequenz** der Kopplungsgeometrie — nicht als empirischer Parameter.

### 4.3 Vergleich mit B₁

**B₁** setzt voraus: φ(t, x) = kx − ωt mit v_φ = ω/k = c.

Hier wird c als **Phasengeschwindigkeit** einer Kopplungswelle verwendet — d. h. als Ausbreitungsgeschwindigkeit der Phasenfronten.

**c_lim aus AP4** ist dagegen eine **Grenzgeschwindigkeit** — die maximale Geschwindigkeit, bei der Kopplung noch möglich ist.

### 4.4 Sind c_lim und c_φ identisch?

**Argument für Identität:**
- In der SRT gilt: Die Lichtgeschwindigkeit ist sowohl die Ausbreitungsgeschwindigkeit elektromagnetischer Wellen (Phasengeschwindigkeit) als auch die maximale Signalgeschwindigkeit (Grenzgeschwindigkeit). Beide sind strukturell dasselbe.
- Wenn die RFT konsistent mit der SRT ist (RT-40 Gesamtergebnis), sollte c_lim = c_φ gelten.

**Argument gegen automatische Identität:**
- c_lim ist eine **kinematische** Grenze (maximale relative Bewegung unter erhaltener Kopplung).
- c_φ ist eine **dynamische** Eigenschaft (Ausbreitungsgeschwindigkeit der Phasenfronten der Kopplungswelle).
- Ohne zusätzliche Annahme über die Wellengleichung der Kopplungsstruktur folgt c_lim = c_φ nicht automatisch.

**Befund AP2:** Die Verbindung c_lim = c_φ ist plausibel und konsistent mit den RT-40-Ergebnissen, aber sie folgt **nicht zwingend** aus A1–A7. Sie würde B₁ rückwirkend fundieren — jedoch nur, wenn zusätzlich gezeigt wird, dass die Phasenfronten der Kopplungswelle genau mit c_lim propagieren. Dies erfordert eine Aussage über die Dynamik der Kopplungswelle, die in A1–A7 nicht enthalten ist.

**Zwischenergebnis AP2:** c_lim und c_φ sind konzeptuell verschieden. Ihre Gleichheit ist konsistenzverträglich, aber nicht beweisbar aus A1–A7 allein. B₁ wird durch AP4 teilweise motiviert, aber nicht vollständig hergeleitet.

---

## 5. AP3 — Gruppentheoretische Analyse: c in G_sync

### 5.1 Frage

Enthält G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) eine ausgezeichnete Geschwindigkeit? Erzwingt die affine Komponente Aff⁺(ℝ) eine invariante Phasengeschwindigkeit c?

### 5.2 Struktur von G_sync

Nach RT-02 (`de/fakten/theorie/gsync_gruppenstruktur.md`) ist G_sync die minimale Symmetriegruppe der RFT-Kopplungsstruktur:

G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ)

mit:
- **ℝ⁺_×**: Skalierungen der Amplitude (A → λA, λ > 0)
- **U(1)**: Globale Phasenrotationen (φ → φ + α)
- **Aff⁺(ℝ)**: Orientierungserhaltende affine Transformationen der Zeitachse (t → at + b, a > 0)

### 5.3 Analyse: Erzwingt G_sync eine Phasengeschwindigkeit?

**Skalierungskomponente ℝ⁺_×:** Skalierungen der Amplitude ändern k und ω nicht — sie legen keine Dispersionsrelation fest.

**Phasenkomponente U(1):** Globale Phasenrotationen verschieben φ → φ + α — sie betreffen nicht das Verhältnis ω/k.

**Affine Komponente Aff⁺(ℝ):** Die Transformation t → at + b wirkt auf die Frequenz durch ω → ω/a. Eine simultane Transformation x → ax + b' (falls Aff⁺(ℝ) auch auf den Ort wirkt) würde k → k/a ergeben — und ω/k = (ω/a)/(k/a) bleibt invariant. Das bedeutet: v_φ = ω/k ist unter simultaner Skalierung von Raum und Zeit invariant, aber **kein spezifischer Wert** von v_φ wird ausgezeichnet.

**Entscheidende Beobachtung:** G_sync ist eine **interne Symmetriegruppe** der Kopplungsstruktur — sie wirkt auf die Phasen und Amplituden der Resonatoren, aber **nicht auf die Raumzeit-Koordinaten** (t, x) als eigenständige geometrische Objekte. Die Verbindung zwischen Phasendynamik und Raumzeit-Geometrie ist genau das, was B₁ herstellt — und was G_sync allein nicht leisten kann.

**Formales Argument:** G_sync enthält keine Untergruppe, die einer Lorentz-Boost-Gruppe isomorph wäre. Die Boost-Gruppe SO(1,1) (hyperbolische Rotationen) ist nicht in G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) enthalten. Eine ausgezeichnete Invarianzgeschwindigkeit (das Analogon zu c in der Lorentz-Gruppe) ist daher aus G_sync allein nicht ableitbar.

**Zwischenergebnis AP3:** G_sync erzwingt keine ausgezeichnete Phasengeschwindigkeit c. Die affine Komponente Aff⁺(ℝ) erhält das Verhältnis ω/k, aber legt seinen Wert nicht fest. B₁ folgt nicht aus A7 (G_sync-Invarianz).

---

## 6. Synthese: Ergebnis A oder B?

### 6.1 Zusammenfassung der drei Arbeitspakete

| Arbeitspaket | Frage | Ergebnis |
|:-------------|:------|:---------|
| AP1 | Ist ω/k in A1–A7 fixiert? | Nein — freier Parameter |
| AP2 | Folgt c_φ aus c_lim (RT-40 AP4)? | Konsistent, aber nicht beweisbar aus A1–A7 |
| AP3 | Erzwingt G_sync eine ausgezeichnete Geschwindigkeit? | Nein — G_sync enthält keine SO(1,1)-Untergruppe |

### 6.2 Schlussfolgerung

**Ergebnis B tritt ein:** Die Phasengeschwindigkeit c der RFT-Kopplungswelle folgt **nicht** aus A1–A7.

Die Brückenannahme B₁ ist eine **Identifikations-Hypothese**, die:
- nicht aus der Dispersionsstruktur von A1 ableitbar ist (AP1),
- nicht zwingend aus der Grenzgeschwindigkeit von RT-40 AP4 folgt (AP2),
- nicht aus der Gruppenstruktur G_sync hergeleitet werden kann (AP3).

**A8 ist ein irreduzibles Postulat**, das die Lücke zwischen RFT-Phasendynamik und Raumzeit-Geometrie schließt.

### 6.3 Formulierung von A8

> **A8 (Kopplungswellengeschwindigkeit):** Die Phasenwelle der RFT-Kopplungsstruktur propagiert mit der Geschwindigkeit c = 1/√(μ₀ε₀) im Vakuum.

**Eigenschaften von A8:**
- **Irreduzibel:** Folgt nicht aus A1–A7 (RT-41 AP1–AP3).
- **Unabhängig:** Keine logische Redundanz mit A1–A7 nachweisbar.
- **Konsistent:** Verträglich mit RT-40 AP4 (c_lim = c als strukturelle Grenzgeschwindigkeit).
- **Empirisch testbar:** c = 1/√(μ₀ε₀) ist messtechnisch zugänglich (Michelson–Morley, moderne Präzisionsexperimente).
- **Analog zur SRT:** Die SRT postuliert c ebenfalls als Naturkonstante — A8 ist strukturell kohärent mit der SRT-Tradition.

### 6.4 Einordnung

Das Ergebnis B ist **kein Scheitern** der RFT. Es ist ein strukturell kohärentes Ergebnis:

- Die SRT benötigt zwei Postulate: (1) Relativitätsprinzip, (2) Konstanz von c.
- Die RFT benötigt unter A1–A8: sieben interne Axiome + A8 (Phasengeschwindigkeit c).
- Der Unterschied zur SRT: A1–A7 liefern eine **reichhaltigere interne Struktur** (Kopplungsdynamik, ε, G_sync), aus der die SRT als Grenzfall folgt — sobald A8 die Verbindung zur Raumzeit herstellt.

---

## 7. Methodische Leitplanken

1. **Kein Zirkelschluss:** In AP1–AP3 wurde c nicht stillschweigend vorausgesetzt. Die Analyse begann mit A1–A7 und prüfte, ob c als Phasengeschwindigkeit folgt.

2. **Unterscheidung der c-Konzepte:**
   - **(a) c als Grenzgeschwindigkeit** (RT-40 AP4, aus ε → 0): Strukturelle Konsequenz der Kopplungsgeometrie — in A1–A7 enthalten.
   - **(b) c als Phasengeschwindigkeit** (B₁): Ausbreitungsgeschwindigkeit der Phasenfronten — **nicht** in A1–A7 enthalten, erfordert A8.
   - **(c) c als Naturkonstante** (empirisch): c = 299 792 458 m/s — Messgröße, die A8 verankert.

3. **Ergebnis B als kohärentes Ergebnis:** Auch die SRT postuliert c. Ein A8 auf RFT-Ebene ist keine Schwäche, sondern eine präzise Lokalisierung der Annahme, die die Verbindung zur Raumzeit herstellt.

4. **Falsifizierung:** Wenn c_RFT (aus ε → 0, RT-40 AP4) ≠ c_phys (gemessen), ist die gesamte RT-40/RT-41-Struktur empirisch widerlegt.

---

## 8. Zusammenfassung und Status

| Aspekt | Ergebnis |
|:-------|:---------|
| Status B₁ in A1–A7 | Nicht herleitbar — freier Parameter (AP1) |
| c_lim = c_φ? | Konsistent, nicht beweisbar aus A1–A7 (AP2) |
| G_sync erzwingt c? | Nein — keine SO(1,1)-Untergruppe (AP3) |
| Ergebnis | **B: A8 ist irreduzibles Postulat** |
| A8 formuliert? | Ja — § 6.3 |
| Nächste Schritte | A8 in `axiomatische_grundlegung.md` eingetragen (Sep 2026) — abgeschlossen |

**Deliverables dieses Dokuments:**
- ✅ AP1–AP3 vollständig analysiert
- ✅ Ergebnis B dokumentiert
- ✅ A8 formal formuliert
- ✅ A8 in `axiomatische_grundlegung.md` eingetragen (AP4, abgeschlossen Sep 2026)
- ✅ EN-Spiegeldokument: `en/facts/theory/rt41_axiom_a8_coupling_wave.md` (vorhanden)

**Verbindung zu bestehenden Dokumenten:**
- RT-40 AP3: `de/fakten/theorie/rt40_ap3_lorentz_transformation.md` §8 (Ausgangspunkt)
- RT-40 AP4: `de/fakten/theorie/rt40_ap4_lichtgeschwindigkeit_grenzfall.md` (c als Grenzgeschwindigkeit)
- RT-02: `de/fakten/theorie/gsync_gruppenstruktur.md` (G_sync-Struktur)
- RT-36: `de/fakten/theorie/a5_vektorialitaet_herleitung.md` (Vorbild: irreduzibles Postulat)
- Axiomatische Grundlegung: `de/fakten/docs/definitionen/axiomatische_grundlegung.md`
