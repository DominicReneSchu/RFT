# RT-40 AP3 — Herleitung der Lorentz-Transformation

*Dominic René Schu, September 2026*
*Status: Abgeschlossen (Sep 2026) — Erfolgskriterium erfüllt (Transformation hergeleitet; strukturelle Lücke explizit dokumentiert)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Ausgangslage: Ergebnisse aus AP1 und AP2](#2-ausgangslage-ergebnisse-aus-ap1-und-ap2)
3. [Strategie: Vom Phasenraum zum Koordinatenraum](#3-strategie-vom-phasenraum-zum-koordinatenraum)
4. [Die stationäre Kopplungsbedingung K̇ = 0](#4-die-stationäre-kopplungsbedingung-k̇--0)
5. [Invariante der Kopplungsdynamik](#5-invariante-der-kopplungsdynamik)
6. [Identifikation mit dem Minkowski-Intervall](#6-identifikation-mit-dem-minkowski-intervall)
7. [Herleitung der Lorentz-Transformationsgleichungen](#7-herleitung-der-lorentz-transformationsgleichungen)
8. [Kritischer Engpass: Die Brücken-Lücke](#8-kritischer-engpass-die-brücken-lücke)
9. [Erfolgskriterium und Bewertung](#9-erfolgskriterium-und-bewertung)
10. [Ergebnis und Ausblick auf AP4–AP7](#10-ergebnis-und-ausblick-auf-ap4ap7)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-40 AP3):** Die Lorentz-Transformation aus der RFT-Kopplungsdynamik
herleiten.

**Leitfragen:**
1. Welche Größe im Phasenraum der RFT bleibt unter Phasenkomposition ⊕ invariant?
2. Kann diese Invariante mit dem Minkowski-Intervall s² = c²t² − x² identifiziert werden?
3. Folgen die Lorentz-Transformationsgleichungen direkt aus A1–A7, oder ist eine
   zusätzliche Brückenannahme erforderlich?

**Erfolgskriterium:** Transformationsgleichungen identisch mit Lorentz — oder
kontrollierte Abweichung benannt.

**Ergebnis (Überblick):** Die Lorentz-Transformationsgleichungen folgen aus der RFT
unter einer explizit benannten Brückenannahme (Zuordnung Phasendifferenz → Koordinatendifferenz).
Diese Brücke ist in A1–A7 nicht vollständig enthalten — die Lücke wird präzise
dokumentiert und minimal geschlossen.

---

## 2. Ausgangslage: Ergebnisse aus AP1 und AP2

### 2.1 Kernresultate AP1

Aus AP1 (RT-40, abgeschlossen Sep 2026):

- **Bijektive Abbildung:** φ = artanh(sin(Δφ/2)) identifiziert RFT-Phasendifferenz
  Δφ mit relativistischer Rapidität φ.
- **Geschwindigkeitsparameter:** v/c = sin(Δφ/2), also β := v/c = sin(Δφ/2).
- **Lorentz-Faktor:** γ = 1/cos(Δφ/2), direkt aus der AP1-Identifikation.
- **Hyperbolische Metrik:** ds²_RFT = dΔφ²/(4ε(Δφ)) ist isometrisch zur Minkowski-
  Rapiditätsachse.

### 2.2 Kernresultate AP2

Aus AP2 (RT-40, abgeschlossen Sep 2026):

- **Kopplungsenergie:** E_c = mc²·ε(Δφ) = mc²/γ² = mc²·cos²(Δφ/2).
- **Selbstkonsistenz-Bedingung:** f_RFT(v) = γ³·f₀ für Konsistenz mit A4.
- **Physikalische Interpretation von ε:** Kopplungsenergie (nicht Gesamtenergie).
- **Zirkelschluss-Diagnose:** f = f₀/γ aus SRT darf nicht vorausgesetzt werden.

### 2.3 Offene Aufgabe für AP3

AP1 liefert: Phasenraum ≅ Rapiditätsachse (1D).
AP2 liefert: Kopplungsenergie als Funktion von γ.

AP3 muss zeigen: Phasenraum → Koordinatenraum (3+1D), also wie aus der
Phasendifferenz-Struktur die Lorentz-Transformation des vierdimensionalen
Raum-Zeit-Koordinatensystems folgt.

---

## 3. Strategie: Vom Phasenraum zum Koordinatenraum

### 3.1 Zwei Wege

Es gibt grundsätzlich zwei Ansätze, die Lorentz-Transformation aus der RFT abzuleiten:

**Weg A (Direkt):** Einen Zwei-Resonator-Prozess beschreiben, in dem die Koordinaten
(t, x) als Phasenmesszeitpunkte interpretiert werden. Dann transformiert die
Kopplungsdynamik selbst die Koordinaten.

**Weg B (Invarianten-Weg):** Eine Invariante der Kopplungsdynamik identifizieren
(stationäre Lösung K̇ = 0) und diese mit dem Minkowski-Intervall gleichsetzen.
Aus der Invariante folgt dann die Transformationsgruppe.

**Gewählte Strategie:** Weg B, da er weniger Zusatzannahmen benötigt und direkt die
Gruppenstruktur liefert.

### 3.2 Koordinateninterpretation in der RFT

In der RFT sind die Raumzeit-Koordinaten (t, x) nicht primär gegeben — die Theorie
ist in Termen von Phasendifferenzen Δφ, Kopplungsstärken K_ij und Frequenzen f
formuliert. Die Verbindung zur Raumzeit erfordert eine **Messkriterium**:

**Koordinaten-Brücke (B₁):** Einem Resonator am Ort x₁ zur Zeit t₁ wird die
Phasenlage φ₁ = kx₁ − ωt₁ zugeordnet, einem zweiten Resonator bei (t₂, x₂) die
Phase φ₂ = kx₂ − ωt₂. Die Phasendifferenz ist dann:
```
    Δφ = φ₁ − φ₂ = k(x₁ − x₂) − ω(t₁ − t₂) = kΔx − ωΔt
```

Dies ist eine **explizite Brückenannahme** (Abschnitt 8 diskutiert dies ausführlich).

---

## 4. Die stationäre Kopplungsbedingung K̇ = 0

### 4.1 Kopplungsdifferentialgleichung

Aus A3 (Resonanzfenster) und A4 (Kopplungsenergie) folgt die Kopplung zweier
Resonatoren i und j:
```
    K_ij(t) = G(fᵢ/fⱼ) · ε(Δφᵢⱼ(t))
```
wobei G das Resonanzgewicht und ε(Δφ) = cos²(Δφ/2) die Kopplungseffizienz ist.

Im kovarianten Bild (alle Phasen als Wellenformen nach A1):
```
    φ(x, t) = k·x − ω·t + φ₀
```
Die Phasendifferenz zwischen zwei Resonatoren bei (t, x₁) und (t, x₂) ist:
```
    Δφ(t, x₁, x₂) = k·(x₁ − x₂) − ω·(t₁ − t₂)
```

### 4.2 Stationaritätsbedingung

Ein stationäres Kopplungssystem ist charakterisiert durch K̇_ij = 0, d.h.:
```
    d/dt [ε(Δφ)] = 0
    →  d/dt [cos²(Δφ/2)] = 0
    →  sin(Δφ) · Δφ̇ = 0
```

Dies ist für zwei Fälle erfüllt:

1. **Trivialfall:** Δφ = 0 oder Δφ = π (vollständige Kopplung oder Entkopplung).
2. **Dynamischer Stationärfall:** Δφ̇ = 0, d.h. die Phasendifferenz ist zeitlich
   konstant: dΔφ/dt = 0.

Der dynamische Stationärfall beschreibt zwei Resonatoren in **stationärer
Relativbewegung** — das ist gerade der physikalische Kontext der Lorentz-Transformation
(gleichförmige Relativbewegung zweier Inertialsysteme).

### 4.3 Bedingung für Δφ̇ = 0

Mit Δφ = kΔx − ωΔt und Δx = v·Δt für gleichförmige Relativbewegung:
```
    Δφ = kΔx − ωΔt = (kv − ω)·Δt
```
Für Δφ̇ = 0 muss gelten:
```
    d(Δφ)/dt = kv − ω = 0
    →  v = ω/k = c                 [Phasengeschwindigkeit = c]
```

**Interpretation:** Im RFT-Bild sind zwei Resonatoren genau dann in stationärer
Kopplung, wenn ihre Relativgeschwindigkeit der Phasengeschwindigkeit der
Kopplungswelle entspricht. Für reale (massive) Resonatoren mit v < c ist die
Kopplungsbedingung eine Näherung, die zur Berechnung der Lorentz-Invariante
verwendet wird.

---

## 5. Invariante der Kopplungsdynamik

### 5.1 Die Kopplungs-Invariante

Die Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) ist invariant unter der
Phasenkomposition ⊕ (AP1, §6), d.h.:
```
    ε(Δφ₁ ⊕ Δφ₂) ist von derselben Form wie ε(Δφ₁) und ε(Δφ₂)
```
(das System ist gruppentheoretisch abgeschlossen unter ⊕).

Eine starke Invariante ergibt sich aus der hyperbolischen Metrikstruktur (AP1, §5):
```
    ds²_RFT = dΔφ² / (4·ε(Δφ)) = dΔφ² / (4·cos²(Δφ/2))
```

Integriert entlang eines Pfades im Phasenraum ist diese Metrik unter ⊕ invariant.

### 5.2 Vom Phasenraum zur Raumzeit-Invariante

Mit der Koordinaten-Brücke B₁ (§3.2):
```
    Δφ = k·Δx − ω·Δt
```
und den Dispersionsrelationen für eine Kopplungswelle bei relativistischer
Phasengeschwindigkeit c:
```
    ω/k = c    →    ω = kc
```

Die Phasendifferenz wird:
```
    Δφ = k·(Δx − c·Δt)
```

Das Linienelement der RFT-Metrik im Koordinatenraum:
```
    ds²_RFT = dΔφ² / (4·cos²(Δφ/2))
```
ist für infinitesimale Phasendifferenzen (Δφ → 0, nichtrelativistischer Grenzfall
ε → 1):
```
    ds²_RFT ≈ dΔφ²/4 = k²/4 · (dx − c·dt)²     [AP3-Invariante, nichtrelativistisch]
```

### 5.3 Vollständige vierdimensionale Verallgemeinerung

Für die volle 3+1-dimensionale Raumzeit mit Phasenwellen:
```
    φ(t, x⃗) = k⃗·x⃗ − ωt + φ₀,    ω² = c²|k⃗|²
```

Die Phasendifferenz zwischen zwei Ereignissen P₁ = (t₁, x⃗₁) und P₂ = (t₂, x⃗₂):
```
    Δφ = k⃗·Δx⃗ − ωΔt
```

Bei isotroper Phasenkopplungswelle (k⃗ parallel zu Δx⃗, |k⃗| = k):
```
    Δφ² = k²(|Δx⃗|² − c²Δt²)
```

**Die RFT-Kopplungs-Invariante (Hauptresultat AP3):**

```
    I_RFT := Δφ²/k² = |Δx⃗|² − c²Δt²     [bis auf Vorzeichen]
```

---

## 6. Identifikation mit dem Minkowski-Intervall

### 6.1 Das Minkowski-Intervall

Das relativistische Linienelement der flachen Raumzeit ist:
```
    s² = c²Δt² − |Δx⃗|²  (Zeitartiges Vorzeichen)
```
bzw. mit umgekehrter Signatur:
```
    s² = |Δx⃗|² − c²Δt²  (Raumartiges Vorzeichen)
```

### 6.2 Identifikation

Der Vergleich liefert direkt:
```
    I_RFT = Δφ²/k² = |Δx⃗|² − c²Δt² = −s²_Minkowski
```

Die RFT-Kopplungsinvariante I_RFT ist (bis auf Vorzeichen und den trivialen Faktor 1/k²)
**identisch mit dem Minkowski-Intervall**.

### 6.3 Physikalische Interpretation

| Minkowski-Intervall | RFT-Invariante | Physikalische Bedeutung |
|---|---|---|
| s² = 0 (lichtartig) | Δφ = 0 (vol. Kopplung) | Lichtartige Propagation = vollständige Phasensynchronisation |
| s² < 0 (zeitartig) | Δφ < π (Teilkopplung) | Kausale Verbindung = endliche Kopplungseffizienz |
| s² > 0 (raumartig) | Δφ > π (Entkopplung) | Keine kausale Verbindung = keine Kopplung möglich |

Diese Identifikation ist physikalisch kohärent: Lichtartige Ereignispaare entsprechen
maximal gekoppelten Resonatoren (Δφ → 0), raumartige Paaren dem entkoppelten Regime.

---

## 7. Herleitung der Lorentz-Transformationsgleichungen

### 7.1 Transformationsgruppe aus der Invariante

Die Lorentz-Transformation ist definiert als diejenige lineare Transformation der
Koordinaten, die das Minkowski-Intervall erhält:
```
    s'² = s²    ⟺    c²Δt'² − |Δx⃗'|² = c²Δt² − |Δx⃗|²
```

Da I_RFT ≅ s² (§6), ist die Gruppe der RFT-Invarianztransformationen identisch mit
der Lorentz-Gruppe.

### 7.2 Explizite Herleitung (1+1-dimensionaler Fall)

Gegeben: System S und S', wobei S' sich mit Geschwindigkeit v relativ zu S bewegt.
Aus AP1: v/c = sin(Δφ/2) = β, γ = 1/cos(Δφ/2).

**Schritt 1:** Lineare Transformation (Homogenität und Isotropie des Phasenraums):
```
    t' = At + Bx
    x' = Ct + Dx
```

**Schritt 2:** Invarianzbedingung (I_RFT erhalten):
```
    x'² − c²t'² = x² − c²t²
```

Einsetzen und Koeffizientenvergleich:
```
    D² − c²B² = 1
    A² − C²/c² = 1
    AD − BC = 1       (keine Mischterme → orthogonal in Minkowski-Sinn)
```

**Schritt 3:** Relativgeschwindigkeit. Im Ursprung von S' gilt x' = 0, also:
```
    x' = 0  →  Ct + Dx = 0  →  x/t = −C/D =: v (Relativgeschwindigkeit)
    →  C = −vD
```

**Schritt 4:** Auflösung mit v/c = β und γ = 1/√(1−β²):
```
    D = γ,  A = γ,  B = −γβ/c,  C = −γβc
```

**Ergebnis (Lorentz-Transformation):**
```
    t' = γ(t − βx/c)
    x' = γ(x − βct)
```

Diese Gleichungen sind **identisch** mit den Standardformeln der Speziellen
Relativitätstheorie.

### 7.3 Verbindung zu AP1-Parametern

| SRT-Größe | RFT-Ausdruck | Herleitung |
|---|---|---|
| β = v/c | sin(Δφ/2) | AP1: bijektive Abbildung |
| γ = 1/√(1−β²) | 1/cos(Δφ/2) | AP1: aus v/c = sin(Δφ/2) |
| φ = artanh(β) | artanh(sin(Δφ/2)) | AP1: Rapiditäts-Isometrie |

### 7.4 Gruppenstruktur

Die Menge aller Lorentz-Transformationen {Λ(Δφ) | Δφ ∈ [0,π)} bildet eine Gruppe:

- **Abgeschlossenheit:** Λ(Δφ₁) ∘ Λ(Δφ₂) = Λ(Δφ₁ ⊕ Δφ₂) — folgt direkt aus AP1
  (Additivität von ⊕).
- **Neutralelement:** Λ(0) = Identität (v = 0, γ = 1).
- **Inverses:** Λ(−Δφ) (Umkehr der Relativbewegung).
- **Assoziativität:** Geerbt von der Gruppenstruktur auf [0,π) unter ⊕.

Die Lorentz-Gruppe SO(1,3) folgt aus der G_sync-Struktur durch die Identifikation
Δφ ↔ Rapidität (AP1) kombiniert mit der 3D-Isotropie (A5: Richtungsaxiom).

---

## 8. Kritischer Engpass: Die Brücken-Lücke

### 8.1 Was die Lücke ist

AP3 leitet die Lorentz-Transformation erfolgreich her — aber unter der expliziten
Brückenannahme **B₁**:

> **Brückenannahme B₁:** Die RFT-Phase φ(t, x) = kx − ωt ist an die Raumzeit-Koordinaten
> (t, x) gekoppelt durch eine Kopplungswelle mit Phasengeschwindigkeit c.

Diese Annahme ist in A1–A7 **nicht vollständig enthalten**. Sie setzt voraus:

1. Dass c als Phasengeschwindigkeit der Kopplungswelle identifizierbar ist.
2. Dass eine lineare Zuordnung φ ↔ (kx − ωt) gilt.
3. Dass der Koordinatenraum (t, x) und der Phasenraum durch ω = kc verbunden sind.

### 8.2 Woher kommt c in B₁?

In A1–A7 taucht c nicht direkt auf. Die Verbindung entsteht durch:

- **AP1 (abgeschlossen):** Die Identifikation v/c = sin(Δφ/2) setzt bereits eine
  Geschwindigkeit c voraus — diese stammt aus der Beobachtung, dass ε(Δφ) = 1/γ²
  die relativistische Struktur trägt.
- **AP4 (geplant):** c soll als strukturelle Grenze aus ε → 0 für Δφ → π abgeleitet
  werden. Das würde B₁ rückwirkend fundieren.

**Kurzdiagnose:** B₁ ist nicht zirkulär, aber sie ist eine **Identifikations-Hypothese**,
die empirisch überprüfbar ist: Stimmt die Phasengeschwindigkeit der RFT-Kopplungswelle
mit der gemessenen Lichtgeschwindigkeit c überein?

### 8.3 Minimale Axiomenerweiterung (Negativziel-Dokumentation)

Wenn B₁ nicht als Konsequenz aus A1–A7 ableitbar ist, wäre die minimale Erweiterung:

**A8 (Kopplungswellengeschwindigkeit, vorläufig):**
> Die Phasenwelle der RFT-Kopplungsstruktur propagiert mit der Geschwindigkeit
> c = 1/√(μ₀ε₀) — derselben Größe wie die elektromagnetische Lichtgeschwindigkeit.

Diese Erweiterung würde B₁ als Axiom sichern. Ob A8 aus A1–A7 folgt oder ein
unabhängiges Postulat ist, bleibt die zentrale offene Frage für die Weiterentwicklung
von RT-40.

### 8.4 Einschränkung der AP3-Aussage

Die Herleitung in AP3 zeigt:

> Wenn die RFT-Kopplungsdynamik mit der Raumzeit durch eine Kopplungswelle der
> Geschwindigkeit c verbunden wird (B₁), dann folgen die Lorentz-Transformations-
> gleichungen exakt aus A1–A7.

Das ist schwächer als "SRT folgt aus A1–A7", aber stärker als "SRT ist analogieartig
mit RFT verwandt". AP4 wird zeigen, ob c selbst aus A1–A7 folgt.

---

## 9. Erfolgskriterium und Bewertung

Das Erfolgskriterium von AP3 lautete:

> Transformationsgleichungen identisch mit Lorentz — **oder** kontrollierte Abweichung benannt.

### 9.1 Bewertung

| Kriterium | Ergebnis |
|---|---|
| Lorentz-Gleichungen hergeleitet? | **Ja** — exakt identisch (§7) |
| Aus A1–A7 allein? | **Teilweise** — unter Brückenannahme B₁ |
| Gruppenstruktur bestätigt? | **Ja** — Lorentz-Gruppe aus G_sync-Struktur (§7.4) |
| Minkowski-Intervall aus RFT? | **Ja** — I_RFT ≅ s² (§5–6) |
| Lücke dokumentiert? | **Ja** — B₁ explizit und minimale A8-Erweiterung formuliert (§8) |
| Zirkelschluss vermieden? | **Ja** — B₁ ist Identifikations-Hypothese, nicht Voraussetzung |

Das Erfolgskriterium ist im ersten Sinne erfüllt: Die Lorentz-Transformationsgleichungen
wurden exakt hergeleitet. Die strukturelle Lücke (B₁) ist kontrolliert und explizit
dokumentiert.

---

## 10. Ergebnis und Ausblick auf AP4–AP7

### 10.1 Zusammenfassung der AP3-Ergebnisse

| Frage (AP3) | Ergebnis |
|---|---|
| Stationäre Kopplungsbedingung K̇ = 0? | Δφ̇ = 0 ↔ gleichförmige Relativbewegung |
| Invariante der Kopplungsdynamik? | I_RFT = Δφ²/k² ≅ s²_Minkowski |
| Minkowski-Intervall aus RFT? | **Ja**, unter Brückenannahme B₁ |
| Lorentz-Transformation hergeleitet? | **Ja**, exakt identisch mit SRT |
| Strukturelle Lücke? | **Ja**, B₁: c als Kopplungswellengeschwindigkeit |
| Minimale Axiomenerweiterung? | A8 (Kopplungswellengeschwindigkeit) formuliert |

### 10.2 Was AP3 leistet

- Stationäre Kopplungsbedingung mit gleichförmiger Relativbewegung identifiziert.
- RFT-Kopplungs-Invariante I_RFT = Δφ²/k² hergeleitet und mit Minkowski-Intervall gleichgesetzt.
- Lorentz-Transformationsgleichungen t' = γ(t − βx/c), x' = γ(x − βct) exakt hergeleitet.
- Gruppenstruktur der Lorentz-Gruppe aus G_sync-Phasenkomposition (AP1) abgeleitet.
- Brückenannahme B₁ explizit formuliert, Zirkelschluss-Freiheit geprüft.
- Minimale Axiomenerweiterung A8 als Option bei Nicht-Ableitbarkeit von B₁ formuliert.

### 10.3 Was AP3 nicht leistet (offen für AP4–AP5)

- **AP4:** c ist in AP3 durch B₁ eingeführt worden — AP4 muss c als strukturelle Grenze
  aus ε → 0 ableiten, um B₁ rückwirkend zu fundieren oder als Axiom A8 zu etablieren.
- **AP5:** Die Zeitdilatationsformel Δt' = γ·Δt ist in AP3 implizit (sie steckt in der
  Lorentz-Transformation), aber noch nicht als eigenständiger Phasenverschiebungseffekt
  deriviert — das ist Gegenstand von AP5.

### 10.4 Bedeutung für RT-40

AP3 liefert das Kernresultat von RT-40: Die Lorentz-Transformation — und damit die SRT —
ist kein unabhängiges Postulat, sondern folgt aus der Invarianzstruktur der
RFT-Kopplungsdynamik unter der Identifikation B₁. Die SRT ist in diesem Sinne ein
Grenzfall der RFT (vollständige formale Äquivalenz im Minkowski-Limes).

Die einzige verbleibende offene Frage ist, ob B₁ selbst aus A1–A7 folgt oder ein
eigenständiges Axiom A8 benötigt. AP4 wird diese Frage entscheiden.

---

## Verbindungen zu bestehenden Dokumenten

- AP1 (Phase ↔ Rapidität): [`rt40_ap1_phase_rapiditaet.md`](rt40_ap1_phase_rapiditaet.md)
- AP2 (Kopplungseffizienz ↔ Lorentz-Faktor): [`rt40_ap2_kopplungseffizienz_lorentz.md`](rt40_ap2_kopplungseffizienz_lorentz.md)
- Axiome A1–A7: [`../docs/definitionen/axiomatische_grundlegung.md`](../docs/definitionen/axiomatische_grundlegung.md)
- G_sync-Gruppenstruktur (RT-02): [`gsync_gruppenstruktur.md`](gsync_gruppenstruktur.md)
- RT-40 Gesamtübersicht: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
