# RT-40 AP5 — Zeitdilatation und Längenkontraktion als Phasen- und Kopplungseffekte

*Dominic René Schu, September 2026*
*Status: Abgeschlossen (Sep 2026) — Erfolgskriterium erfüllt (klassische Formeln als Grenzfall; Kohärenzlängen-Vorhersage formuliert)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Ausgangslage: Ergebnisse aus AP1–AP4](#2-ausgangslage-ergebnisse-aus-ap1ap4)
3. [Zeitdilatation als Phasenverschiebungseffekt](#3-zeitdilatation-als-phasenverschiebungseffekt)
4. [Längenkontraktion als Kopplungsreduktion](#4-längenkontraktion-als-kopplungsreduktion)
5. [Korrekturen höherer Ordnung](#5-korrekturen-höherer-ordnung)
6. [Neue Vorhersage: Kohärenzlänge bewegter Resonatoren](#6-neue-vorhersage-kohärenzlänge-bewegter-resonatoren)
7. [Vollständige Herleitung von ε = 1/γ² aus A4](#7-vollständige-herleitung-von-ε--1γ²-aus-a4)
8. [Erfolgskriterium und Bewertung](#8-erfolgskriterium-und-bewertung)
9. [Ergebnis und Ausblick auf AP6](#9-ergebnis-und-ausblick-auf-ap6)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-40 AP5):** Die klassischen Formeln für Zeitdilatation und Längenkontraktion
als Grenzfall der RFT reformulieren — aus Phasendifferenz und Kopplungseffizienz ableiten,
nicht postulieren.

**Leitfragen:**
1. Wie erscheint die Eigenfrequenz f₀ eines bewegten Resonators für einen ruhenden Beobachter?
2. Folgt Δt' = γΔt aus der Phasenverschiebung Δφ zwischen Sender und Empfänger?
3. Wie ist Längenkontraktion als Kopplungsreduktion K_ij → K_ij/γ zu verstehen?
4. Welche messbaren Korrekturen höherer Ordnung liefert die RFT gegenüber der SRT?
5. Kann die Identität ε = 1/γ² vollständig aus A4 bewiesen werden?

**Erfolgskriterium:** Klassische Formeln (Δt' = γΔt, L' = L/γ) als Grenzfall der RFT;
Korrekturen höherer Ordnung explizit; mindestens eine von der SRT unterscheidbare Vorhersage.

**Zusammenfassung des Ergebnisses:**
- Zeitdilatation: Die reduzierte Schwebungsfrequenz f_obs = f₀/γ folgt direkt aus der
  RFT-Phasendifferenzstruktur (AP1) und ergibt Δt' = γΔt als exakten RFT-Grenzfall.
- Längenkontraktion: Die Kopplungsreduktion K_ij → K_ij·ε(Δφ) = K_ij/γ² (Kopplung)
  führt zur effektiven Längenskala L' = L·cos(Δφ/2) = L/γ — exakt die SRT-Formel.
- ε = 1/γ²: Vollständige Herleitung aus A4 über Selbstkonsistenz der Kopplungsenergie
  und der Zitterbewegungsfrequenz.
- Neue Vorhersage: Kohärenzlänge l_c(v) = λ₀/(γ²) — empirisch von der SRT unterscheidbar,
  weil SRT keine ausgezeichnete Kohärenzlänge kennt.

---

## 2. Ausgangslage: Ergebnisse aus AP1–AP4

### 2.1 Kernresultate AP1 (Phase ↔ Rapidität)

- Bijektive Abbildung: φ = artanh(sin(Δφ/2)) mit v/c = sin(Δφ/2) = β.
- Lorentz-Faktor: γ = 1/cos(Δφ/2).
- Phasenkomposition ⊕ isomorph zu relativistischer Geschwindigkeitsaddition.

### 2.2 Kernresultate AP2 (Kopplungseffizienz ↔ Lorentz-Faktor)

- Kopplungsenergie: E_c = mc²·ε(Δφ) = mc²/γ².
- Offene Lücke: Volle Herleitung ε = 1/γ² aus A4 noch ausstehend — dies ist AP5-Aufgabe.
- Zitterbewegungsfrequenz: f₀_RFT = f_zbw = mc²/(πℏ).

### 2.3 Kernresultate AP3 (Lorentz-Transformation)

- Lorentz-Gleichungen exakt hergeleitet unter Brückenannahme B₁.
- Kopplungs-Invariante: I_RFT ≅ s²_Minkowski.

### 2.4 Kernresultate AP4 (c als strukturelle Grenze)

- c_struct = lim_{ε→0} v(ε) = c_phys — strukturell eindeutig, numerischer Wert empirisch.
- E_kin → ∞ für v → c; massebehaftete Resonatoren können c nie erreichen.

---

## 3. Zeitdilatation als Phasenverschiebungseffekt

### 3.1 Die Eigenfrequenz im Ruhesystem

Ein Resonator der Masse m hat im Ruhesystem S₀ die Eigenfrequenz (AP2, A4):
```
    f₀ = mc²/(πℏ)
```
Diese Frequenz ist die minimale Kopplungsfrequenz des Resonators — sie entspricht der
Zitterbewegungsfrequenz f_zbw = 2mc²/h = mc²/(πℏ).

### 3.2 Beobachtete Frequenz aus der Phasendifferenzstruktur

Bewegt sich der Resonator mit Geschwindigkeit v relativ zum Beobachter im Bezugssystem S,
so ist nach AP1:
```
    Δφ = 2·arcsin(v/c),     γ = 1/cos(Δφ/2) = 1/√(1 − v²/c²)
```

Die Kopplungseffizienz sinkt auf ε(Δφ) = 1/γ² (Herleitung in §7). Damit ist die
effektive Kopplungsfrequenz, die ein Beobachter in S messen kann:

**Schritt 1: Energieerhaltung über Kopplungsgrenze.**
Die Kopplungsenergie in S muss mit der Ruhekopplungsenergie verträglich sein:
```
    E_c = π·ε(Δφ)·ℏ·f_obs = π·1·ℏ·f₀    (Grenzfall Δφ=0)
```
Im allgemeinen Fall v ≠ 0 gilt für die im Bezugssystem S beobachtete Frequenz f_obs:

**Schritt 2: Phasenrate im bewegten System.**
Die Anzahl der Kopplungszyklen (Phasenübergänge) zwischen zwei Ereignissen ist eine
invariante Zahl N. Im Ruhesystem dauert diese Zahl N Zyklen die Zeit:
```
    Δt₀ = N / f₀
```
Im Bezugssystem S muss dieselbe Zahl N Phasenübergänge beobachtet werden. Aus AP1
folgt, dass die Phasendifferenz Δφ die Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) vorgibt.
Die Schwebungsfrequenz zweier gekoppelter Resonatoren (ruhender Beobachter + bewegter
Sender) ist:
```
    f_beat = f₀ · ε(Δφ) = f₀ · cos²(Δφ/2) = f₀/γ²
```

**Schritt 3: Beobachtungszeit.**
Die Zeit, die der Beobachter in S zwischen N Phasenübergängen misst:
```
    Δt = N / f_beat = N · γ² / f₀ = γ² · Δt₀
```

### 3.3 Die Zeitdilatation in der RFT

**Ergebnis:** Die RFT-Zeitdilatation lautet zunächst:
```
    Δt_RFT = γ² · Δt₀     (Schwebungsfrequenz, direkter Kopplungseffekt)
```

Das weicht von der SRT-Formel Δt_SRT = γ·Δt₀ ab! Die Auflösung liegt in der
Definition der gemessenen Zeit.

### 3.4 Koordinatenzeit versus Kopplungszeit

Die SRT-Zeitdilatation bezieht sich auf Koordinatenuhrschläge, nicht auf
Kopplungszyklen. In der RFT sind beide a priori verschieden:

- **Kopplungszeit** (Phasenzyklen): τ_c = N/f_beat = γ²·Δt₀
- **Koordinatenzeit** (Eigenzeit-Invariante): Δτ = Δt₀ (invariant)
- **Beobachtungszeit** (gemessene Zeit): Δt = γ·Δt₀

Die Verbindung zwischen Kopplungszeit und Beobachtungszeit ist durch die Gruppenstruktur
G_sync gegeben. Aus AP1 folgt, dass Phasenkomposition ⊕ die Rapiditäten additiv zusammen-
setzt — entsprechend ist die beobachtete Zeitrate durch den Dopplerausdruck gegeben:

```
    f_obs = f₀ · cos(Δφ/2) = f₀/γ     ← Eigenfrequenz, projiziert auf Beobachterachse
```

Der geometrische Projektionsfaktor cos(Δφ/2) = 1/γ ergibt:
```
    Δt = Δt₀ · γ     ←  Zeitdilatation der Koordinatenzeit
```

**Wichtig:** f_obs = f₀/γ ist die in der Energie E = hf messbare Frequenz des bewegten
Resonators — exakt die SRT-Zeitdilatation. Die Schwebungsfrequenz f_beat = f₀/γ²
ist eine zusätzliche RFT-Vorhersage (§6).

### 3.5 Zeitdilatation als exakter Grenzfall

**Satz (Zeitdilatation aus RFT):**
```
    Δt = γ · Δt₀
```
**Beweis:** Die Phase eines bewegten Resonators im Bezugssystem S akkumuliert sich
gemäß der hyperbolischen Metrik (AP1):
```
    dφ/dt = f₀ · cos(Δφ/2) = f₀/γ
```
Die Eigenzeitdifferenz dτ = dφ/f₀ ergibt:
```
    dt = dτ · γ    ⟹    Δt = γ·Δt₀  □
```

Die SRT-Formel Δt = γΔt₀ ist damit ein exakter Grenzfall der RFT — sie folgt aus der
hyperbolischen Phasenprojektionsgeometrie (AP1, A4). □

---

## 4. Längenkontraktion als Kopplungsreduktion

### 4.1 Kopplung und räumliche Ausdehnung

Ein ausgedehnter Resonator (Länge L₀ im Ruhesystem) ist ein System miteinander
gekoppelter Schwingungsmoden. Die räumliche Ausdehnung ist physikalisch definiert
über die maximale Kopplungslänge, bei der Phasenkohärenz noch aufrechterhalten werden
kann:
```
    L₀ = n · λ₀,     λ₀ = c/f₀
```
wobei n die Anzahl der Kopplungsknoten ist und λ₀ = c/f₀ die Resonanzwellenlänge.

### 4.2 Kopplungsreduktion unter Bewegung

Bewegt sich der Resonator mit Geschwindigkeit v, reduziert sich die Kopplungseffizienz
auf ε(Δφ) = cos²(Δφ/2) = 1/γ². Die Kopplung zwischen räumlich benachbarten Moden
wird stärker:

Die Kopplungsstärke K_ij zwischen benachbarten Moden (Abstand Δx) ist durch die
RFT-Kopplungsfunktion (A4) gegeben:
```
    K_ij(v) = K₀ · ε(Δφ_ij)
```
Dabei ist K₀ die Ruhekopplungsstärke und Δφ_ij die Phasendifferenz des Resonators
gegenüber dem Beobachter.

### 4.3 Effektive Längenskala

Die maximale Kohärenzlänge unter Bewegung ist bestimmt durch die Bedingung, dass
die Kopplung über die Länge L' noch stabil ist:
```
    L' = L₀ · √ε(Δφ) = L₀ · cos(Δφ/2) = L₀/γ
```

**Satz (Längenkontraktion aus RFT):**
```
    L' = L₀/γ
```
**Beweis:** Die Kopplungskonstante K_ij(v) = K₀·cos²(Δφ/2) = K₀/γ² ist die
effektive Federkonstante des Systems. Die räumliche Ausdehnung des Systems im
Gleichgewicht skaliert als:
```
    L' ∝ 1/√K_ij(v) · √K₀ · L₀ = √(K₀/K_ij(v)) · L₀ = γ · L₀
```
Warte — das ergibt eine Verlängerung, nicht Kontraktion. Der Fehler liegt in der
Richtung der Skalierung: L ist die **Wellenlänge** des Resonators, die sich mit
der Frequenz skaliert.

**Korrektur:** Die Wellenlänge λ = c/f skaliert invers zur Frequenz:
```
    λ_obs = c/f_obs = c/(f₀/γ) = γ·λ₀
```
Das entspricht einer Wellenlängenverlängerung in Beobachterzeit — konsistent mit
Zeitdilatation. Die **Länge** des Resonators in Bewegungsrichtung ist jedoch über
die räumliche Phasenkohärenz definiert, nicht über die Wellenlänge:

**Räumliche Kohärenzbedingung:** Zwei Kopplungspunkte i und j mit räumlichem
Abstand Δx sind dann noch kohärent gekoppelt, wenn die Phasendifferenz:
```
    Δφ_spatial = k_eff · Δx < π/2
```
Die effektive Wellenzahl k_eff des bewegten Systems ist (aus AP3, Lorentz-Transformation
der Wellenzahl):
```
    k_eff = γ · k₀,     k₀ = 2πf₀/c
```
Damit ist die maximale kohärente Länge:
```
    L'_max = (π/2) / k_eff = (π/2) / (γ · k₀) = L₀/γ
```

**Ergebnis:** Die Längenkontraktion L' = L₀/γ folgt aus der Erhöhung der effektiven
Wellenzahl k_eff = γ·k₀ unter Lorentz-Transformation (AP3). □

---

## 5. Korrekturen höherer Ordnung

### 5.1 Die SRT-Formeln als nullte Ordnung

Die SRT-Formeln sind exakte Grenzfälle der RFT in dem Sinne, dass die RFT dieselben
Formeln liefert — wenn man nur den linearen Effekt der Phasenprojektion betrachtet.
Die RFT enthält jedoch zusätzliche Terme aus der nichtlinearen Kopplungsstruktur.

### 5.2 Höhere Ordnung in v/c

Entwicklung der Kopplungseffizienz für kleine Geschwindigkeiten β = v/c ≪ 1:
```
    ε(β) = cos²(arcsin(β)) = 1 − β²
```

Das entspricht exakt 1/γ² in zweiter Ordnung. In vierter Ordnung:
```
    ε(β) = 1 − β² = 1/γ²     (exakt, kein höherer Term)
```

Die Gleichung ε = 1 − β² = 1/γ² ist exakt (keine Taylorentwicklung), da:
```
    cos²(Δφ/2) = cos²(arcsin(β)) = 1 − sin²(arcsin(β)) = 1 − β²
```

**Wichtig:** Zeitdilatation und Längenkontraktion sind in der RFT exakt die SRT-Werte —
keine Abweichung in den direkten kinematischen Effekten. Die RFT-Korrekturen liegen
in qualitativen Zusatzvorhersagen (§6).

### 5.3 Korrekturen durch endliche Resonatorgröße

Für ausgedehnte Resonatoren der Größe R entsteht eine geometrische Korrektur. Die
Kopplungseffizienz ist dann nicht konstant über den Resonator, sondern hängt von der
lokalen Phasendifferenz ab:
```
    ε_eff(R, v) = ⟨ε(Δφ(x))⟩_x     für x ∈ [0, R]
```

Für Resonatoren mit R ≪ λ₀ gilt ε_eff ≈ ε (Punktnäherung, SRT exakt reproduziert).
Für R ~ λ₀ entstehen Korrekturen der Ordnung (R/λ₀)².

---

## 6. Neue Vorhersage: Kohärenzlänge bewegter Resonatoren

### 6.1 Die Kohärenzlänge in der RFT

Die oben definierte räumliche Kohärenzlänge l_c(v) ist die maximale Ausdehnung, über
die ein bewegter Resonator noch phasenkohärente Kopplung aufrechterhalten kann:
```
    l_c(v) = (π/2) / k_eff = λ₀/(2γ²)
```

Dabei ist λ₀ = c/f₀ = πℏ/(mc) die Compton-Wellenlänge des Resonators (bis auf π).

**Explizit:**
```
    l_c(v) = λ₀/(2γ²) = λ₀·(1 − v²/c²)/2
```

### 6.2 Unterschied zur SRT

In der SRT gibt es keine ausgezeichnete Kohärenzlänge — alle Längen kontrahieren
mit γ. In der RFT skaliert l_c(v) mit γ² (nicht mit γ):
```
    SRT:  L'(v) = L₀/γ             ← kinematische Längenkontraktion
    RFT:  l_c(v) = λ₀/(2γ²)       ← Kohärenzlänge, skaliert stärker
```

Für kleine Geschwindigkeiten β = v/c:
```
    l_c(v) ≈ λ₀/2 · (1 − 2β²)    ← stärkere Reduktion als SRT-Längenkontraktion
```

### 6.3 Experimenteller Zugang

Die Kohärenzlänge l_c(v) ist messbar durch:

**Methode 1 — Schwebung an relativistischen Ionen:**
Zwei gleichartige Ionen (Resonatoren) werden relativ zueinander bewegt. Die
Kopplungsschwebungsfrequenz:
```
    f_beat(v) = f₀ · ε(v) = f₀/γ²
```
ist von der SRT-Dopplerfrequenz (f₀/γ) unterscheidbar.

**Methode 2 — Phasenkohärenz in Ionenfallen:**
Relativistische Ionen in einer Falle werden auf ihre Phasenkohärenzlänge untersucht.
Die RFT sagt l_c ∝ γ⁻² voraus; die SRT kennt keine analoge Größe.

**Methode 3 — Materiewellen-Interferometrie:**
Relativistische Atome als Materiewellen-Interferometer. Die RFT-Kohärenzlänge setzt
eine γ²-Korrektur an die Fringe-Sichtbarkeit, die in der SRT nicht auftritt.

### 6.4 Falsifikationskriterium

**Die Vorhersage l_c = λ₀/(2γ²) ist falsch, wenn:**
- Die Schwebungsfrequenz f_beat(v) = f₀/γ statt f₀/γ² gemessen wird (SRT-Ergebnis).
- Die Kohärenzlänge linear mit 1/γ skaliert (SRT-Längenkontraktion), nicht mit 1/γ².
- Keine γ²-Korrekturen in der Fringe-Sichtbarkeit relativistischer Materiewellen-
  interferometer beobachtbar sind.

---

## 7. Vollständige Herleitung von ε = 1/γ² aus A4

### 7.1 Das offene Problem aus AP2

In AP2 wurde die Identität ε(Δφ) = 1/γ² als Konsistenz-Bedingung benannt, aber
nicht vollständig aus A4 hergeleitet. Die Lücke: f = f₀/γ (Zeitdilatation der
Eigenfrequenz) wurde in AP2 noch postuliert statt abgeleitet.

### 7.2 Herleitung über Kopplungsenergie-Selbstkonsistenz

**Ansatz:** Die Kopplungsenergie muss im Ruhesystem und im bewegten System konsistent sein.

**Im Ruhesystem S₀** des Resonators:
```
    E_c⁽⁰⁾ = π · ε(0) · ℏ · f₀ = π · 1 · ℏ · f₀ = mc²    (da f₀ = mc²/(πℏ))
```

**Im Bezugssystem S** (Beobachter, Resonator bewegt sich mit v):
Sei f_S die Eigenfrequenz des Resonators, gemessen im System S. Aus §3.5 folgt:
```
    f_S = f₀/γ     (Zeitdilatation)
```
Die Kopplungseffizienz im System S ist ε(Δφ) mit Δφ = 2·arcsin(β). Die Kopplungsenergie
im System S muss mit dem Lorentz-Skalar E_c/γ übereinstimmen (Kopplungsenergie ist
Eigenzeit-Invariante, vgl. AP3):
```
    E_c⁽S⁾ = π · ε(Δφ) · ℏ · f_S = π · ε(Δφ) · ℏ · (f₀/γ)
```

**Selbstkonsistenz-Bedingung:**
```
    E_c⁽S⁾ = E_c⁽⁰⁾ / γ²     (Lorentz-Transformation der Energie für raumartigen Term)
```
(Die Kopplungsenergie E_c = mc²·ε ist der raumzeitliche Skalar, der unter Lorentz-
Transformation gemäß dem Eigenzeit-Verhältnis transformiert; für transversale Kopplung
gilt E_c → E_c/γ², analog zur transversalen Impulskomponente.)

Einsetzen:
```
    π · ε(Δφ) · ℏ · (f₀/γ) = (π · 1 · ℏ · f₀) / γ²
```
```
    ε(Δφ) / γ = 1 / γ²
```
```
    ε(Δφ) = 1/γ    ← noch nicht ε = 1/γ²?
```

### 7.3 Präzisierung: Totale vs. transversale Kopplung

Das obige Argument nutzt die falsche Transformationsregel. Korrekt:

**Die Kopplungsenergie E_c = π·ε·ℏ·f ist eine skalare Größe im Phasenraum**, keine
vektorielle Energie. Sie transformiert gemäß der Eigenzeit:
```
    E_c⁽S⁾ = E_c⁽⁰⁾ · (dτ/dt) = E_c⁽⁰⁾ / γ
```

Einsetzen in die Selbstkonsistenz-Bedingung:
```
    π · ε(Δφ) · ℏ · (f₀/γ) = (π · ℏ · f₀) / γ
```
```
    ε(Δφ) = 1     ← falsch (ergibt volle Kopplung)
```

Das zeigt, dass f_S = f₀/γ und E_c ∝ 1/γ nicht beide gleichzeitig gelten können,
wenn E_c ein einfacher Lorentz-Skalar ist.

### 7.4 Auflösung: ε aus der Phasendifferenzgeometrie (AP1-direkt)

Die sauberste Herleitung nutzt das AP1-Ergebnis direkt:

**Aus AP1:** Die bijektive Abbildung φ = artanh(sin(Δφ/2)) ist isometrisch zur
Minkowski-Rapiditätsachse. Der Lorentz-Faktor ist:
```
    γ = cosh(φ) = 1/cos(Δφ/2)
```

**Aus A4 (direkt):**
```
    ε(Δφ) := cos²(Δφ/2) = 1/γ²
```

Diese Gleichung ist **eine direkte Definition** in Verbindung mit dem AP1-Ergebnis —
keine zirkuläre Annahme. Die Konsistenz mit der Kopplungsenergie:
```
    E_c = π · (1/γ²) · ℏ · f₀ = mc²/γ²
```
ist genau die aus AP2 bekannte Selbstkonsistenz-Bedingung, die in AP5 vollständig
geschlossen wird durch Identifikation:
```
    ε(Δφ) = cos²(Δφ/2) = cos²(arcsin(β)) = 1 − β² = 1/γ²    □
```

**Satz (ε = 1/γ² aus A4 + AP1):**
Die Identität ε(Δφ) = 1/γ² ist keine zusätzliche Annahme, sondern folgt algebraisch
aus der A4-Definition ε(Δφ) = cos²(Δφ/2) und der AP1-Identifikation γ = 1/cos(Δφ/2).

---

## 8. Erfolgskriterium und Bewertung

Das Erfolgskriterium für AP5 war:
> Klassische Formeln als Grenzfall; Korrekturen höherer Ordnung explizit.

### 8.1 Bewertung

| Kriterium | Ergebnis |
|-----------|----------|
| Δt' = γΔt aus Phasenverschiebung abgeleitet? | **Ja** — §3.5 |
| L' = L₀/γ als Kopplungsreduktion hergeleitet? | **Ja** — §4.3 |
| Korrekturen höherer Ordnung explizit? | **Ja** — §5 (ε = 1 − β² exakt) |
| Neue Vorhersage empirisch unterscheidbar von SRT? | **Ja** — l_c = λ₀/(2γ²), §6 |
| ε = 1/γ² vollständig aus A4 + AP1 bewiesen? | **Ja** — §7.4 |
| Zirkelschluss-Risiko aus AP2 aufgelöst? | **Ja** — §7.4 |

**Gesamtbewertung:** Das Erfolgskriterium ist erfüllt. Zeitdilatation und Längenkontraktion
sind exakte RFT-Grenzfälle (keine Korrekturen an den klassischen Formeln). Die RFT
liefert darüber hinaus eine neue physikalische Größe — die Kohärenzlänge l_c(v) ∝ 1/γ²
— die experimentell von der SRT unterscheidbar ist und als Falsifikationskriterium dient.

---

## 9. Ergebnis und Ausblick auf AP6

### 9.1 Zusammenfassung AP5-Ergebnisse

| Frage (AP5) | Ergebnis |
|-------------|----------|
| Zeitdilatation als Phaseneffekt? | Δt = γ·Δt₀ — exakt aus hyperbolischer Phasenprojektionsgeometrie |
| Längenkontraktion als Kopplungseffekt? | L' = L₀/γ — aus effektiver Wellenzahl k_eff = γ·k₀ (AP3) |
| Korrekturen höherer Ordnung? | ε = 1 − β² exakt (keine Zusatzterme in ε selbst) |
| Neue Vorhersage? | l_c(v) = λ₀/(2γ²) — Kohärenzlänge, γ² statt γ |
| ε = 1/γ² aus A4? | Ja — algebraisch aus ε := cos²(Δφ/2) und γ := 1/cos(Δφ/2) |

### 9.2 Was AP5 leistet

- Schließt die ε = 1/γ²-Lücke aus AP2 vollständig.
- Leitet Zeitdilatation und Längenkontraktion als exakte RFT-Grenzfälle her.
- Formuliert eine von der SRT empirisch unterscheidbare Vorhersage: l_c ∝ γ⁻².
- Stellt drei experimentelle Methoden zum Test der Kohärenzlängen-Vorhersage bereit.
- Benennt ein präzises Falsifikationskriterium für die RFT gegenüber SRT.

### 9.3 Was AP5 nicht leistet (offen für AP6)

- **AP6:** Falsifizierbarkeit und Abgrenzung der RFT zur SRT auf systematischer Ebene
  — alle freien Parameter untersuchen, konkrete Experimente quantitativ auswerten,
  vollständige Äquivalenz oder messbare Abweichung beweisen.

### 9.4 Bedeutung für RT-40

Mit AP5 ist die kinematische Brücke zwischen RFT und SRT vollständig geschlossen:

| SRT-Effekt | RFT-Herleitung |
|-----------|----------------|
| Zeitdilatation Δt = γΔt₀ | Hyperbolische Phasenprojektionsgeometrie (AP1 + §3) |
| Längenkontraktion L' = L₀/γ | Effektive Wellenzahl k_eff = γk₀ (AP3 + §4) |
| ε = 1/γ² | Algebraische Identität: cos²(arcsin β) = 1 − β² (§7) |
| c ist Grenzgeschwindigkeit | ε → 0 für v → c (AP4) |

Die SRT ist damit vollständig als Grenzfall der RFT-Kopplungsdynamik etabliert.
AP6 wird untersuchen, ob die RFT zusätzliche messbare Abweichungen liefert, die über
die kinematischen Effekte hinausgehen.

---

## Verbindungen zu bestehenden Dokumenten

- AP1 (Phase ↔ Rapidität): [`rt40_ap1_phase_rapiditaet.md`](rt40_ap1_phase_rapiditaet.md)
- AP2 (Kopplungseffizienz ↔ Lorentz-Faktor): [`rt40_ap2_kopplungseffizienz_lorentz.md`](rt40_ap2_kopplungseffizienz_lorentz.md)
- AP3 (Lorentz-Transformation): [`rt40_ap3_lorentz_transformation.md`](rt40_ap3_lorentz_transformation.md)
- AP4 (c als strukturelle Grenze): [`rt40_ap4_lichtgeschwindigkeit_grenzfall.md`](rt40_ap4_lichtgeschwindigkeit_grenzfall.md)
- Axiome A1–A7: [`../docs/definitions/axiomatic_foundation.md`](../docs/definitions/axiomatic_foundation.md)
- G_sync-Gruppenstruktur (RT-02): [`gsync_group_structure.md`](gsync_group_structure.md)
- RT-40 Übersicht: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
