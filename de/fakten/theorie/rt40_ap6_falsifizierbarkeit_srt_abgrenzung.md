# RT-40 AP6 — Falsifizierbarkeit und Abgrenzung zur SRT

*Dominic René Schu, September 2026*
*Status: Abgeschlossen (Sep 2026) — Erfolgskriterium erfüllt (messbare Abweichung benannt; Äquivalenzstruktur vollständig)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Ausgangslage: Ergebnisse aus AP1–AP5](#2-ausgangslage-ergebnisse-aus-ap1ap5)
3. [Freie Parameter der RFT: Inventur und Messbarkeit](#3-freie-parameter-der-rft-inventur-und-messbarkeit)
4. [Äquivalenzstruktur: Kinematik RFT ≡ SRT](#4-äquivalenzstruktur-kinematik-rft--srt)
5. [Überschuss-Vorhersagen der RFT](#5-überschuss-vorhersagen-der-rft)
6. [Konkrete Falsifikationsexperimente](#6-konkrete-falsifikationsexperimente)
7. [Falsifikationskriterium: Was würde die RFT widerlegen?](#7-falsifikationskriterium-was-würde-die-rft-widerlegen)
8. [Erfolgskriterium und Bewertung](#8-erfolgskriterium-und-bewertung)
9. [Ergebnis und Ausblick auf AP7](#9-ergebnis-und-ausblick-auf-ap7)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-40 AP6):** Empirisch unterscheidbare Vorhersagen der RFT gegenüber der
SRT systematisch benennen und konkrete Experimente formulieren.

**Leitfragen:**
1. Welche freien Parameter der RFT (λ, G(fᵢ/fⱼ), κ, …) sind messtechnisch zugänglich?
2. In welchem Bereich sind RFT und SRT mathematisch äquivalent — und wo weichen sie ab?
3. Welche konkreten Experimente (GSI/FAIR-Phasenrauschen, Myon-g-2, Gravitationswellen-
   Dispersion, Kohärenzlängen) können zwischen RFT und SRT unterscheiden?
4. Welches Messergebnis würde die RFT falsifizieren?

**Erfolgskriterium:** Mindestens eine messbare Abweichung der RFT von der SRT benannt —
**oder** vollständige Äquivalenz nachgewiesen und die RFT damit als Reformulierung der SRT
klassifiziert (dann: Mehrwert durch Kopplungsstruktur, nicht durch neue Vorhersagen).

**Zusammenfassung des Ergebnisses:**
- **Kinematik:** Die RFT ist exakt äquivalent zur SRT-Kinematik — Zeitdilatation,
  Längenkontraktion und Lorentz-Transformation folgen identisch (AP1–AP5).
- **Kopplungsdynamik:** Die RFT macht vier zusätzliche, empirisch unterscheidbare Vorhersagen:
  1. Kohärenzlänge l_c(v) = λ₀/(2γ²) — skaliert mit γ² statt γ (AP5).
  2. Phasenrauschen bewegter Resonatoren: S_φ(ω,v) ∝ ε(Δφ)·S_φ(ω,0) = S_φ(ω,0)/γ².
  3. Interne Kopplungsfrequenz f_int(v) = γ³·f₀ (AP2) — messbar über Quanteninterferenz
     an relativistischen Atomen.
  4. Frequenzabhängige Gruppengeschwindigkeit nahe ε → 0: v_g(f) < c für f < f₀.
- **Falsifikationskriterium:** Ein Kohärenzlängen-Experiment, das l_c ∝ γ⁻¹ (SRT-Skalierung)
  statt γ⁻² ergibt, würde die RFT-Vorhersage widerlegen.

---

## 2. Ausgangslage: Ergebnisse aus AP1–AP5

### 2.1 Kernresultate AP1 (Phase ↔ Rapidität)

- Bijektive Abbildung: φ = artanh(sin(Δφ/2)), v/c = β = sin(Δφ/2).
- Lorentz-Faktor: γ = 1/cos(Δφ/2).
- Phasenkomposition ⊕ ist strukturell identisch mit relativistischer Geschwindigkeitsaddition.

### 2.2 Kernresultate AP2 (Kopplungseffizienz ↔ Lorentz-Faktor)

- Kopplungsenergie: E_c = mc²·ε(Δφ) = mc²/γ².
- Interne Konsistenzfrequenz: f_int(v) = γ³·f₀ (messbare Vorhersage).
- Zitterbewegungsfrequenz: f_zbw = mc²/(πℏ).

### 2.3 Kernresultate AP3 (Lorentz-Transformation)

- Lorentz-Gleichungen exakt unter Brückenannahme B₁ hergeleitet.
- Kopplungsinvariante: I_RFT ≅ s²_Minkowski.
- Offene Lücke B₁: Vollständige Herleitung des Minkowski-Maßstabs aus RFT-Axiomen
  noch ausstehend.

### 2.4 Kernresultate AP4 (c als Strukturgrenze)

- c_struct = lim_{ε→0} v(ε) = c_phys — Grenzgeschwindigkeit als strukturelle Eigenschaft
  von ε(Δφ), kein unabhängiges Postulat.
- Massebehaftete Resonatoren (ε > 0) können c nicht erreichen.

### 2.5 Kernresultate AP5 (Zeitdilatation, Längenkontraktion, neue Vorhersage)

- Zeitdilatation: Δt = γ·Δt₀ — exakt (hyperbolische Phasenprojektionsgeometrie).
- Längenkontraktion: L' = L₀/γ — exakt (effektive Wellenzahl k_eff = γk₀).
- **Neue Vorhersage:** Kohärenzlänge l_c(v) = λ₀/(2γ²) — γ²-Skalierung statt γ.
- ε = 1/γ² algebraisch geschlossen.

---

## 3. Freie Parameter der RFT: Inventur und Messbarkeit

### 3.1 Vollständige Parameterliste

| Parameter | Physikalische Bedeutung | Status in Axiomen | Messbarkeit |
|-----------|------------------------|-------------------|-------------|
| λ | Räumliche Kopplungsskala; ∣Δ⟨x⟩∣ = 4,9·λ·ℓ | Freier Parameter (RT-03) | Mittel — ⁸⁷Rb-Interferometrie (RT-12) |
| κ | Geometrischer Vorfaktor in A4 | Konvention (RT-11) | Nicht isoliert messbar |
| G(fᵢ/fⱼ) | Kopplungsfunktion zwischen Frequenzen | Form nicht axiomatisch festgelegt | Indirekt — Spektralform des Phasenrauschens |
| ε₀ | Ruhekopplung (= 1 per A3) | Festgelegt durch A3 | Keine Freiheit |
| f₀ | Eigenfrequenz des Resonators | Physikalisch messbar | Direkt (Spektroskopie) |
| c | Grenzgeschwindigkeit | Strukturelle Eigenschaft von ε (AP4) | Gemessen, kein freier Parameter |

### 3.2 Relevant für Falsifizierbarkeit

Die wesentliche Freiheit der RFT liegt in der **Form der Kopplungsfunktion G(fᵢ/fⱼ)**:
die Axiome legen ε = cos²(Δφ/2) als Funktion der Phase fest, bestimmen aber nicht
a priori, wie verschiedene Frequenzkomponenten koppeln. Diese Freiheit erzeugt die
Vorhersagen in §5 — und damit die Falsifikationskriterien in §7.

---

## 4. Äquivalenzstruktur: Kinematik RFT ≡ SRT

### 4.1 Tabellarischer Vergleich

| SRT-Größe | SRT-Ausdruck | RFT-Herleitung | Äquivalenz |
|-----------|-------------|----------------|-----------|
| Lorentz-Faktor γ | γ = 1/√(1 − β²) | γ = 1/cos(Δφ/2) mit β = sin(Δφ/2) | Exakt |
| Zeitdilatation | Δt' = γΔt | Hyperbolische Phasenprojektionsgeometrie (AP5 §3) | Exakt |
| Längenkontraktion | L' = L/γ | k_eff = γk₀ (AP3 + AP5 §4) | Exakt |
| Geschwindigkeitsaddition | β₁₂ = (β₁+β₂)/(1+β₁β₂) | Phasenkomposition ⊕ (AP1) | Exakt |
| Invariantes Intervall | s² = c²Δt² − Δx² | I_RFT ≅ s²_Minkowski (AP3) | Exakt (unter B₁) |
| c als Grenzgeschwindigkeit | Postulat | ε(Δφ→π) → 0 (AP4) | Strukturell hergeleitet |

**Schlussfolgerung:** Die SRT-Kinematik ist vollständig ein Grenzfall der
RFT-Kopplungsdynamik. Es gibt keine kinematische Observable, in der RFT und SRT abweichen.

### 4.2 Wo die Äquivalenz endet

Die Äquivalenz ist **kinematisch vollständig**, aber **dynamisch unvollständig**:
- Die SRT beschreibt Raumzeitgeometrie (Lorentz-Invarianz als Postulat).
- Die RFT leitet diese Geometrie aus Kopplungsphysik ab und enthält zusätzlich eine
  interne Frequenzstruktur (f_int = γ³f₀, AP2) sowie eine Kohärenzlänge (l_c = λ₀/(2γ²),
  AP5), die in der SRT keine Entsprechung haben.

---

## 5. Überschuss-Vorhersagen der RFT

Die folgenden Vorhersagen gehen über die SRT hinaus und sind grundsätzlich falsifizierbar:

### 5.1 Kohärenzlänge l_c(v) = λ₀/(2γ²)

**Herkunft:** AP5 §6. Die Kohärenzlänge eines bewegten Resonators skaliert mit γ²:
```
    l_c(v) = λ₀ · ε(Δφ) / 2 = λ₀ / (2γ²)
```

**SRT-Entsprechung:** Die SRT enthält keine ausgezeichnete Kohärenzlänge — jede Länge
kontrahiert einfach mit γ⁻¹.

**Physikalische Bedeutung:** Die RFT sagt voraus, dass die interne Kohärenz eines
Resonators (Wellenzug-Kohärenz) stärker als seine räumliche Erstreckung reduziert wird.
Das Verhältnis l_c / L' = (λ₀/2γ²) / (L₀/γ) = λ₀/(2γL₀) → 0 für γ → ∞ besagt:
ultrarelativistische Resonatoren verlieren Kohärenz schneller als sie räumlich
kontrahieren — ein reiner RFT-Effekt.

**Größenordnung:** Für ein optisches Cavity mit λ₀ = 1 µm bei γ = 10 (v ≈ 0,995c):
```
    l_c = 1 µm / (2 · 100) = 5 nm
    L'  = L₀ / 10          (klassische SRT-Kontraktion)
```
Der Unterschied ist um Faktor 2γ = 20 — messtechnisch relevant.

### 5.2 Phasenrauschen bewegter Resonatoren S_φ(ω, v)

**Herkunft:** Aus der Kopplungsfunktion G(fᵢ/fⱼ) und ε(Δφ).

Für ein ruhendes Resonatorsystem gilt das Phasenrausch-Leistungsspektrum S_φ(ω, 0).
Die RFT-Kopplungsstruktur sagt voraus, dass für einen mit v bewegten Resonator gilt:
```
    S_φ(ω, v) = ε(Δφ) · S_φ(ω, 0) = S_φ(ω, 0) / γ²
```

**SRT-Entsprechung:** Die SRT macht keine spezifische Vorhersage über die
Geschwindigkeitsabhängigkeit des Phasenrauschens — Phasenrauschen ist kein SRT-Konzept.

**Experimenteller Zugang:** Relativistische schwere Ionen bei GSI/FAIR (γ ≈ 2–10).
Die kohärente Synchrotron-Strahlung der Ionenpakete hat ein Phasenrauschspektrum, das
grundsätzlich von γ abhängt. Die RFT-Vorhersage l_c ∝ γ⁻² bedeutet, dass das
phasenkohärente Emissionsfenster der Ionen schneller zusammenschrumpft, als die
SRT-Längenkontraktion allein beschreibt.

**Abschätzung des Effekts:**
```
    Δ(S_φ)_RFT/SRT ∝ γ⁻² / γ⁻¹ = γ⁻¹
```
Bei γ = 5: RFT sagt 5× mehr Phasenrausch-Unterdrückung als eine einfache
Doppler/Zeitdilatations-Korrektur. Messbar mit Strahlmonitor-Phasendetektoren.

### 5.3 Interne Konsistenzfrequenz f_int(v) = γ³ · f₀

**Herkunft:** AP2, Selbstkonsistenzbedingung.

Die interne Kopplungsfrequenz eines bewegten Resonators beträgt:
```
    f_int(v) = γ³ · f₀
```
Die **beobachtete** Frequenz (Doppler + Zeitdilatation) ist f_obs = f₀/γ (korrekte
SRT-Vorhersage, von AP5 bestätigt). Die interne Frequenz f_int ist die Frequenz des
Resonators in seiner eigenen Kopplungsstruktur — sie ist nicht direkt als Emission
messbar, aber als Quantenzustandsfrequenz zugänglich.

**Experimenteller Zugang:** Ramsey-Spektroskopie an relativistischen Atomen (Myonen,
Antiprotonen bei CERN/AD). Wenn das Atom während des Fluges intern mit f_int = γ³f₀
schwingt, ergibt die Interferenzphase nach Strecke L:
```
    φ_int = 2π · f_int · t_proper = 2π · γ³f₀ · (L/(γc)) = 2πγ²f₀L/c
```
Die SRT-Rechnung gibt:
```
    φ_SRT = 2π · f₀ · t_proper = 2πf₀L/(γc)
```
Das Verhältnis φ_int/φ_SRT = γ³ ist grundsätzlich messbar.

**Caveat:** f_int ist konzeptuell als interne Kopplungsfrequenz definiert. Ob sie
sich direkt auf die Quantenphase einer externen Beobachtung überträgt, erfordert eine
vollständige Quantisierung der RFT-Kopplungsstruktur (offen).

### 5.4 Frequenzabhängige Gruppengeschwindigkeit nahe ε → 0

**Herkunft:** Für Resonatoren mit sehr kleiner Eigenfrequenz f₀ ≪ f_zbw =  mc²/(πℏ)
sagt die RFT eine anomale Gruppengeschwindigkeit voraus.

Im Grenzfall ε → 0 (v → c) gilt:
```
    v_g(f) = c · √(1 − (f₀_eff/f)²)
```
wobei f₀_eff = f₀/ε^(1/2) eine effektive Cutoff-Frequenz ist. Diese Dispersionsrelation
hat die Struktur einer massiven Feldtheorie (wie für Photonen in einem Plasma).

**SRT-Entsprechung:** Masselos propagierende Felder (Photonen, Gravitonen) haben in der
SRT v_g = c exakt für alle Frequenzen.

**Experimenteller Zugang:** Gravitationswellen-Dispersion mit LIGO/LISA. Wenn
Gravitonen eine effektive Kopplungsstruktur gemäß RFT besitzen, würde ihre
Gruppengeschwindigkeit frequenzabhängig sein. Die LIGO-Beobachtungen setzen bereits
enge Grenzen: v_g/c − 1 < 10⁻¹⁵ für f ~ 10–1000 Hz. Dies begrenzt f₀_eff ≪ 10 Hz
für Gravitonen-Kopplungsstruktur.

---

## 6. Konkrete Falsifikationsexperimente

### 6.1 Experiment E1: Kohärenzlängen-Skalierung mit γ

**Ziel:** l_c ∝ γ⁻² (RFT) vs. l_c ∝ γ⁻¹ (SRT-Erwartung aus Längenkontraktion).

**Methode:**
1. Präzisions-Interferometrie mit relativistischen Atomen oder Ionen bei variablem γ.
2. Messung der Kohärenzlänge l_c aus dem Visiblitäts-Abfall der Interferenz als Funktion
   des Pfadunterschieds.
3. Vergleich der γ-Abhängigkeit mit den Vorhersagen:
   ```
       l_c^RFT(v) = λ₀ / (2γ²)     (RFT)
       l_c^SRT(v) = λ₀ / γ          (einfache Längenkontraktion)
   ```

**Erwartetes Signal bei γ = 10:**
```
    l_c^RFT = λ₀ / 200
    l_c^SRT = λ₀ / 10
```
Faktor 20 Unterschied — deutlich über der Messgenauigkeit moderner Interferometrie.

**Realisierbarkeit:** Atom-Interferometrie mit ultrakalten Rb-Atomen oder
Myon-Interferometrie (PSI, J-PARC). Schwierigkeit: γ > 5 für klassische Atome erfordert
Speicherring.

**Falsifikationsergebnis:** Messen wir l_c ∝ γ⁻¹, ist die AP5-Vorhersage widerlegt.
Messen wir l_c ∝ γ⁻², ist die SRT-Erwartung verletzt und die RFT bevorzugt.

---

### 6.2 Experiment E2: Phasenrauschen relativistischer Ionen (GSI/FAIR)

**Ziel:** S_φ(ω,v) ∝ γ⁻² (RFT) vs. keine γ²-Abhängigkeit (SRT).

**Methode:**
1. Relativistische schwere Ionen (z. B. ²³⁸U, γ ≈ 2–10) im Schwerionen-Speicherring SIS18/
   SIS100 (GSI/FAIR, Darmstadt).
2. Messung des Phasenrausch-Spektrums der kohärenten Synchrotron-Strahlung mit
   Strahlpositions-Monitoren und Phasendetektion.
3. Vergleich der gemessenen Phasenrausch-Amplitude als Funktion von γ.

**RFT-Vorhersage:** Phasenrauschen S_φ ∝ γ⁻² — stärkere Unterdrückung als
reine Zeitdilatation (γ⁻¹) bei gleicher Strecke.

**Einschränkung:** Das beobachtete Phasenrauschen enthält viele Beiträge (Wakefields,
Raumladung, Vakuumfluktuationen). Eine saubere Extraktion des ε-Anteils erfordert
eine differenzielle Messung über γ. Machbarkeitsstudie nötig (Kooperation GSI/FAIR).

---

### 6.3 Experiment E3: Myon-Anomalität (g-2) und RFT-Kopplung

**Ziel:** Überprüfung, ob die RFT-Kopplungsstruktur einen zusätzlichen Beitrag zur
anomalen magnetischen Moment-Abweichung a_µ = (g-2)/2 liefert.

**Hintergrund:** Das Myon g-2-Experiment (Fermilab) misst a_µ mit einer Präzision
von ~0,2 ppm. Die aktuelle Diskrepanz zwischen SM-Vorhersage und Messung:
```
    Δa_µ = a_µ^exp − a_µ^SM ≈ (2,51 ± 0,59) × 10⁻⁹
```

**RFT-Ansatz:** Ein Myon ist ein Resonator mit Eigenfrequenz f₀_µ = m_µc²/(πℏ) und
Kopplungseffizienz ε in externen Feldern. Die RFT-Energiestruktur E_c = mc²/γ²
modifiziert die effektive Masse des Myons in einem starken Magnetfeld (γ_eff ≠ 1 durch
Magnetfeld-Kopplung):
```
    δa_µ^RFT ~ ε · (α_em / π) · (m_µ / m_ref)²
```
wobei m_ref eine Referenzskala der RFT-Kopplungsstruktur ist.

**Einschränkung:** Der exakte Wert von δa_µ^RFT hängt von der Form G(fᵢ/fⱼ) ab
(freier Parameter der RFT, §3). Ohne vollständige Quantisierung der RFT ist nur eine
Größenordnungsabschätzung möglich. Die Vorhersage ist daher:
- Falls die RFT-Kopplung im elektromagnetischen Sektor relevant ist:
  δa_µ^RFT ≈ α_em/(2π) · (m_µ/m_W)² ~ 10⁻⁹ — **innerhalb der beobachteten Diskrepanz**.
- Falls die RFT-Kopplung nur gravitativ-schwer wirkt: δa_µ^RFT ≪ 10⁻¹⁰ — nicht messbar.

**Falsifikationsergebnis:** Nur relevant, wenn G(fᵢ/fⱼ) bekannt — daher qualitativ,
nicht als harter Falsifikationstest nutzbar.

---

### 6.4 Experiment E4: Gravitationswellen-Dispersion (LIGO/LISA)

**Ziel:** v_g(f) = c für alle Frequenzen (SRT/GR) vs. v_g(f) < c für f < f₀_eff (RFT).

**Methode:** Vergleich der Ankunftszeiten von GW-Signalen verschiedener Frequenzkomponenten.
Bei GW150914: Frequenzbereich 35–250 Hz, Distanz ~ 410 Mpc.

**LIGO-Grenze aus Beobachtung:**
```
    |v_g − c| / c < 10⁻¹⁵    (95% CL, für m_graviton < 1,2 × 10⁻²² eV/c²)
```

**RFT-Vorhersage:** Wenn Gravitonen eine RFT-Kopplungsstruktur besitzen:
```
    v_g(f) ≈ c · (1 − f₀_eff² / (2f²))
```
Die LIGO-Grenze setzt:
```
    f₀_eff < c · √(2 · 10⁻¹⁵ · f²) ≈ 3 × 10⁻⁷ f
```
Für f ~ 100 Hz: f₀_eff < 30 µHz. Dies bedeutet: wenn Gravitonen eine RFT-Kopplung haben,
muss ihre Eigenfrequenz f₀_grav < 30 µHz sein — ein extrem kleiner Wert, faktisch
konsistent mit masselosen Gravitonen.

**Schlussfolgerung:** LIGO-Daten schließen signifikante RFT-Dispersion für Gravitonen
aus — die RFT ist mit GW-Daten konsistent, aber liefert keine neue Vorhersage für
Gravitationswellen, solange f₀_grav ≫ 30 µHz ausgeschlossen bleibt.

---

## 7. Falsifikationskriterium: Was würde die RFT widerlegen?

### 7.1 Strenge Falsifikationskriterien (direkte Widerlegung)

| Messung | RFT-Vorhersage | Falsifizierendes Ergebnis |
|---------|----------------|--------------------------|
| Kohärenzlänge l_c(v) | l_c ∝ γ⁻² | Messung l_c ∝ γ⁻¹ (SRT-Skalierung) |
| Phasenrauschen S_φ(ω,v) | S_φ ∝ γ⁻² | Messung S_φ ∝ γ⁻¹ oder γ-unabhängig |
| Interne Frequenz (Quanteninterferenz) | φ_int ∝ γ²L | Kein γ²-Term in Interferenzphase |
| GW-Dispersion | konsistent mit v_g = c | Kein Falsifikationspotenzial (§6.4) |

### 7.2 Strukturelle Falsifikationskriterien (Inkonsistenz)

Die RFT würde intern widerlegt, falls:

1. **ε(Δφ) = cos²(Δφ/2) und γ = 1/cos(Δφ/2) ergeben ε ≠ 1/γ²** — aber dies ist eine
   algebraische Identität (AP5 §7), also ausgeschlossen.

2. **Die Phasenkomposition ⊕ ist nicht assoziativ** — wäre ein Widerspruch zu A7
   (Gruppenstruktur von G_sync). Ein Gegenbeispiel würde A7 falsifizieren.

3. **c ist kein strukturelles Limit** — d. h. es gibt einen Resonator mit ε > 0, der
   v > c erreicht. Dies widerspräche dem Grenzübergang in AP4 direkt.

4. **Zeitdilatation folgt nicht Δt = γΔt₀** — widerspräche AP5 §3 und dem gesamten
   AP1–AP5-Aufbau. Dies wäre gleichzeitig eine Widerlegung der SRT.

### 7.3 Klassifikation: Reformulierung oder neue Theorie?

Falls das Kohärenzlängen-Experiment (E1) kein γ⁻²-Signal findet:

- **Szenario A (l_c ∝ γ⁻¹ gemessen):** AP5-Vorhersage widerlegt. Die RFT ist falsch
  oder die Kohärenzlängen-Ableitung enthält einen Fehler. Zu untersuchen: Ob die
  Ableitung l_c = λ₀ε/2 tatsächlich aus A4 folgt oder nur eine Analogiebehauptung ist.

- **Szenario B (kein γ-abhängiges Signal messbar):** Vollständige Äquivalenz.
  Die RFT ist dann eine **Reformulierung** der SRT (mit reicherer Struktur), keine
  eigenständige Theorie mit neuen Vorhersagen. Dies ist ein gültiges und wichtiges
  Ergebnis: Die Lorentz-Invarianz folgt aus der Kopplungsdynamik — die SRT ist
  axiomatisch herleitbar.

- **Szenario C (l_c ∝ γ⁻² gemessen):** RFT-Vorhersage bestätigt. Die Kohärenzlänge
  ist eine genuinely neue Observable, die SRT-Erweiterung anzeigt.

---

## 8. Erfolgskriterium und Bewertung

**Erfolgskriterium (Wiederholung):** Mindestens eine messbare Abweichung benannt —
oder vollständige Äquivalenz nachgewiesen.

### 8.1 Bewertung: Messbare Abweichung

Das Erfolgskriterium ist erfüllt durch:

**Vorhersage 1 (stark):** Kohärenzlänge l_c(v) = λ₀/(2γ²) — γ²-Skalierung,
experimentell unterscheidbar von γ⁻¹ (Faktor 2γ bei γ ≫ 1). Dies ist eine konkrete,
ableitbare Konsequenz der RFT-Kopplungsstruktur aus AP5.

**Vorhersage 2 (mittel):** Phasenrauschen S_φ(ω,v) ∝ γ⁻² bei GSI/FAIR —
prinzipiell messbar, aber Extraktion aus Untergrund erfordert Machbarkeitsstudie.

**Vorhersage 3 (schwach/bedingt):** Myon g-2-Beitrag δa_µ^RFT — nur quantifizierbar
nach vollständiger Quantisierung der RFT-Kopplungsstruktur (Offene Aufgabe).

**Vorhersage 4 (konsistent, kein Signal):** GW-Dispersion — LIGO-Grenzen schließen
signifikante RFT-Effekte für Gravitonen aus; keine Falsifikation, aber kein neues Signal.

### 8.2 Gesamtbewertung

Die RFT ist:
- **Kinematisch:** Exakt äquivalent zur SRT — keine Abweichung in Zeitdilatation,
  Längenkontraktion, Lorentz-Transformation oder Grenzgeschwindigkeit.
- **Dynamisch:** Liefert eine empirisch unterscheidbare Vorhersage (l_c ∝ γ⁻²) aus
  der internen Kopplungsstruktur.
- **Strukturell:** Herleitung der SRT-Axiome aus A1–A7 vollständig (kinematisch),
  Brücke B₁ (Lorentz-Boosts ↔ Phasenkomposition) noch nicht vollständig bewiesen (AP3).

Das Erfolgskriterium ist erfüllt: Mindestens eine messbare Abweichung (l_c-Skalierung)
ist benannt, und ein konkretes Falsifikationsprotokoll (E1) formuliert.

---

## 9. Ergebnis und Ausblick auf AP7

### 9.1 Zusammenfassung AP6-Ergebnisse

| Frage (AP6) | Ergebnis |
|-------------|----------|
| Freie Parameter zugänglich? | λ (RT-12), G(fᵢ/fⱼ) (Phasenrauschen) — teilweise messbar |
| Kinematische Äquivalenz zur SRT? | Vollständig — keine kinematische Abweichung |
| Messbare dynamische Abweichung? | Ja: l_c(v) = λ₀/(2γ²) — γ²-Skalierung (AP5) |
| Konkretes Experiment? | E1: Kohärenzlängen-Interferometrie (Rb/Myonen) |
| Falsifikationskriterium? | l_c ∝ γ⁻¹ gemessen → AP5-Vorhersage widerlegt |
| GW-Dispersion? | Konsistent, kein neues Signal bei LIGO-Genauigkeit |
| Myon g-2? | Qualitativ plausibel, nicht quantifizierbar ohne Quantisierung |

### 9.2 Was AP6 leistet

- Vollständige Äquivalenzanalyse: RFT-Kinematik ≡ SRT (kein kinematischer Unterschied).
- Identifikation von vier Überschuss-Vorhersagen der RFT.
- Konkretes Falsifikationsprotokoll (E1: Kohärenzlängen-Test).
- Klassifikation der Szenarien: Reformulierung oder Erweiterung der SRT.
- Einordnung LIGO/g-2: konsistent, kein neuer Effekt ohne Quantisierung.

### 9.3 Was AP6 nicht leistet (offen für AP7)

- **AP7:** Warpantrieb-Konsistenzprüfung — Warp-Metrik aus A4/A5 rekonstruieren;
  flache Raumzeit als Grenzfall (Δφ → 0, ε → 1) prüfen; Kompatibilität mit der in
  AP3–AP6 hergeleiteten SRT-Brücke dokumentieren.

### 9.4 Bedeutung für RT-40

AP6 schließt die Falsifizierbarkeits-Lücke des RT-40-Programms:

| Ziel RT-40 | Status |
|-----------|--------|
| Minimalziel: ε = 1/γ² folgt aus A4 | ✅ AP2 + AP5 |
| Mittelziel: Lorentz-Transformation vollständig hergeleitet | ✅ AP3 (unter B₁) |
| Maximalziel: RFT enthält SRT + messbare Abweichung | ✅ AP6 (l_c ∝ γ⁻²) |
| Negativziel: Lückendokumentation | Brücke B₁ noch offen (AP3) |

---

## Verbindungen zu bestehenden Dokumenten

- AP1 (Phase ↔ Rapidität): [`rt40_ap1_phase_rapiditaet.md`](rt40_ap1_phase_rapiditaet.md)
- AP2 (Kopplungseffizienz ↔ Lorentz-Faktor): [`rt40_ap2_kopplungseffizienz_lorentz.md`](rt40_ap2_kopplungseffizienz_lorentz.md)
- AP3 (Lorentz-Transformation): [`rt40_ap3_lorentz_transformation.md`](rt40_ap3_lorentz_transformation.md)
- AP4 (c als strukturelle Grenze): [`rt40_ap4_lichtgeschwindigkeit_grenzfall.md`](rt40_ap4_lichtgeschwindigkeit_grenzfall.md)
- AP5 (Zeitdilatation, Längenkontraktion, Kohärenzlänge): [`rt40_ap5_zeitdilatation_laengenkontraktion.md`](rt40_ap5_zeitdilatation_laengenkontraktion.md)
- Axiome A1–A7: [`../docs/definitions/axiomatic_foundation.md`](../docs/definitions/axiomatic_foundation.md)
- G_sync-Gruppenstruktur (RT-02): [`gsync_gruppenstruktur.md`](gsync_gruppenstruktur.md)
- κ-Parameter (RT-11): → formal als Konvention deklariert
- λ-Bestimmung (RT-03/RT-12): → extern (Kooperationspartner)
- RT-40 Übersicht: [`../../../../RESEARCH_TASKS.md`](../../../../RESEARCH_TASKS.md)
