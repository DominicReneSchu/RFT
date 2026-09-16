# RT-40 AP1 — Formale Identifikation: Phase ↔ Rapidität

*Dominic René Schu, September 2026*
*Status: Abgeschlossen (Sep 2026)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Wertbereich von Δφ aus A1–A4](#2-wertbereich-von-δφ-aus-a1a4)
3. [Die Brückenformel als Ausgangspunkt](#3-die-brückenformel-als-ausgangspunkt)
4. [Die bijektive Abbildung f: [0,π) → [0,∞)](#4-die-bijektive-abbildung-f-0π--0)
5. [Hyperbolische Metrik auf dem Phasenraum](#5-hyperbolische-metrik-auf-dem-phasenraum)
6. [Phasenkompositionsgesetz und relativistische Geschwindigkeitsaddition](#6-phasenkompositionsgesetz-und-relativistische-geschwindigkeitsaddition)
7. [Erfolgskriterium: Beweis der Bijektivität und Additivität](#7-erfolgskriterium-beweis-der-bijektivität-und-additivität)
8. [Ergebnis und Ausblick auf AP2–AP4](#8-ergebnis-und-ausblick-auf-ap2ap4)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-40 AP1):** Prüfen, ob die RFT-Phasendifferenz Δφ und die
relativistische Rapidität φ dieselbe mathematische Struktur besitzen.

**Erfolgskriterium:** Konstruktion einer bijektiven Abbildung
```
    f: [0, π) → [0, ∞)
```
mit der Additivitätseigenschaft
```
    f(Δφ₁ ⊕ Δφ₂) = f(Δφ₁) + f(Δφ₂)
```
wobei `⊕` eine wohldefinierte Kompositionsregel auf [0, π) bezeichnet, die der
relativistischen Geschwindigkeitsaddition entspricht.

**Ergebnis:** Das Erfolgskriterium ist erfüllt. Die Abbildung
```
    f(Δφ) = arcsech(cos(Δφ/2)) = artanh(sin(Δφ/2))
           = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
```
ist die gesuchte bijektive, additive Identifikation.

---

## 2. Wertbereich von Δφ aus A1–A4

### 2.1 Phasen aus A1

Axiom 1 (Universelle Schwingung) postuliert:
```
    ψ(x, t) = A · cos(kx − ωt + φ),    φ ∈ [0, 2π)
```
Für zwei Oszillatoren i, j ist die Phasendifferenz
```
    Δφ = φᵢ − φⱼ   (mod 2π)
```

### 2.2 Kanonischer Wertebereich durch A4 und G_sync-Invarianz

Aus Axiom 4 (Kopplungsenergie) und der RT-02-Invarianzanalyse folgt:

- **Parität (RT-02, §3):** ε(Δφ) = ε(−Δφ) → Δφ und −Δφ sind physikalisch äquivalent.
- **Monotonie (A4):** ε(Δφ) = cos²(Δφ/2) ist streng monoton fallend auf [0, π].
- **Randbedingungen (A4):**
  - Δφ = 0: ε = 1 (vollständige Kopplung)
  - Δφ = π: ε = 0 (vollständige Entkopplung)

Der physikalisch relevante, kanonische Wertebereich ist daher:
```
    Δφ ∈ [0, π]
```
mit offenem oberen Rand [0, π) für die bijektive Abbildung (Δφ = π entspricht
der Grenzgeschwindigkeit c, die nie erreicht wird — s. AP4).

### 2.3 Topologische Struktur des Phasenraums

Der Raum der Kopplungszustände P = {ε(Δφ) | Δφ ∈ [0, π]} = [0, 1] ist kompakt,
aber die zugehörige physikalische Distanzstruktur (Abschnitt 5) macht ihn offen
nach ∞ hin: P ist isomorph zu [0, ∞) unter der Rapiditätsmetrik.

---

## 3. Die Brückenformel als Ausgangspunkt

RT-40 nennt als bekannte, aber noch nicht bewiesene Brücke:
```
    Δφ = 2 arccos(sech φ)   ⟺   ε(Δφ) = 1/γ²
```
mit φ = relativistische Rapidität, γ = Lorentz-Faktor.

**Umformung:** Aus ε(Δφ) = cos²(Δφ/2) und ε = 1/γ² = sech²(φ) folgt:
```
    cos²(Δφ/2) = sech²(φ)
    cos(Δφ/2)  = sech(φ)           [da beide Seiten ≥ 0 auf dem kanonischen Bereich]
    Δφ/2       = arccos(sech(φ))
    Δφ         = 2 arccos(sech(φ))  ✓
```
Diese Brückenformel ist damit eine direkte Konsequenz der Definition
ε(Δφ) = cos²(Δφ/2) (A4) und der Identifikation ε = 1/γ². Die Identifikation
ε = 1/γ² selbst ist Gegenstand von AP2.

---

## 4. Die bijektive Abbildung f: [0,π) → [0,∞)

### 4.1 Definition

Sei φ die relativistische Rapidität, definiert durch v = c·tanh(φ) mit φ ∈ [0, ∞).
Aus cos(Δφ/2) = sech(φ) folgt direkt die Umkehrfunktion:
```
    f(Δφ) := arcsech(cos(Δφ/2))
```

### 4.2 Geschlossene Formel (drei äquivalente Darstellungen)

**Darstellung 1 (arcsech):**
```
    f(Δφ) = arcsech(cos(Δφ/2))
           = ln((1 + √(1 − cos²(Δφ/2))) / cos(Δφ/2))
           = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
```

**Darstellung 2 (artanh):**

*Behauptung:* arcsech(cos(Δφ/2)) = artanh(sin(Δφ/2))

*Beweis:*
```
    artanh(sin(Δφ/2))
    = (1/2) ln((1 + sin(Δφ/2)) / (1 − sin(Δφ/2)))
    = (1/2) ln((1 + sin(Δφ/2))² / (1 − sin²(Δφ/2)))
    = (1/2) ln((1 + sin(Δφ/2))² / cos²(Δφ/2))
    = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
    = arcsech(cos(Δφ/2))    ✓
```

**Darstellung 3 (explizit logarithmisch):**
```
    f(Δφ) = ln((1 + sin(Δφ/2)) / cos(Δφ/2))
```

### 4.3 Bijektivität

| Eigenschaft | Nachweis |
|---|---|
| Wohldefiniertheit | cos(Δφ/2) > 0 für Δφ ∈ [0, π) |
| f(0) = 0 | arcsech(cos 0) = arcsech(1) = 0 ✓ |
| f(π) = ∞ | arcsech(cos(π/2)) = arcsech(0) = ∞ ✓ |
| Strenge Monotonie | df/dΔφ = 1/(2cos(Δφ/2)) > 0 für Δφ ∈ [0, π) ✓ |
| Surjektivität auf [0,∞) | Folgt aus Stetigkeit + Grenzwertverhalten ✓ |

Die Abbildung f: [0, π) → [0, ∞) ist bijektiv. □

### 4.4 Numerische Stützwerte

| Δφ | f(Δφ) (Rapidität) | v/c = tanh(f) | γ = 1/cos(Δφ/2) |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| π/6 | 0,2554 | 0,2527 | 1,0353 |
| π/3 | 0,5493 | 0,5000 | 1,1547 |
| π/2 | 0,8814 | 0,7071 | 1,4142 |
| 2π/3 | 1,3170 | 0,8660 | 2,0000 |
| 5π/6 | 2,0634 | 0,9659 | 3,8637 |
| π⁻ | ∞ | 1 | ∞ |

---

## 5. Hyperbolische Metrik auf dem Phasenraum

### 5.1 Induzierte Metrik

Die Abbildung f: ([0,π), ds²_RFT) → ([0,∞), dφ²) ist eine Isometrie, wenn man
die Pullback-Metrik auf dem Phasendifferenzraum definiert als:
```
    ds²_RFT := dφ² = (df/dΔφ)² · dΔφ²
```

Berechnung der Ableitung:
```
    f(Δφ) = arcsech(cos(Δφ/2))

    df/dΔφ = d/du[arcsech(u)] · d/dΔφ[cos(Δφ/2)]     mit u = cos(Δφ/2)

           = (−1 / (u √(1−u²))) · (−sin(Δφ/2)/2)

           = sin(Δφ/2) / (2 · cos(Δφ/2) · sin(Δφ/2))

           = 1 / (2 · cos(Δφ/2))
```

Daraus folgt:
```
    ds²_RFT = dΔφ² / (4 · cos²(Δφ/2)) = dΔφ² / (4 · ε(Δφ))
```

### 5.2 Physikalische Interpretation

Die Metrik `ds²_RFT = dΔφ² / (4ε(Δφ))` hat folgende Eigenschaften:

- **Bei kleinen Phasendifferenzen (Δφ → 0, ε → 1):** ds²_RFT ≈ dΔφ²/4 — flache,
  euklidische Metrik (nichtrelativistischer Grenzfall).
- **Bei Annäherung an π (ε → 0):** ds²_RFT → ∞ — die Metrik divergiert. Infinitesimale
  Phasenschritte nahe der Entkopplung entsprechen endlichen Rapiditätsintervallen.
  Dies ist das direkte Analogon zur Unmöglichkeit, c zu erreichen.
- **Curvature:** Die Krümmung der Metrik ist durch die Kopplungsfunktion ε(Δφ)
  bestimmt — sie ist eine intrinsische Eigenschaft der RFT-Kopplungsdynamik.

### 5.3 Isometrie zum hyperbolischen Einheitsraum

Der Phasendifferenzraum ([0,π), ds²_RFT) ist isometrisch zur reellen Rapiditätsachse
([0,∞), dφ²), die die Geometrie des 1+1-dimensionalen Minkowski-Raums trägt.

Die Isometrie ist explizit durch f(Δφ) = arcsech(cos(Δφ/2)) gegeben.

---

## 6. Phasenkompositionsgesetz und relativistische Geschwindigkeitsaddition

### 6.1 Definition der Phasenkomposition ⊕

Analog zur Rapiditätsaddition (φ₁₂ = φ₁ + φ₂ für kollineare Boosts) definiert man
die RFT-Phasenkomposition als diejenige Operation ⊕ auf [0, π), für die gilt:
```
    f(Δφ₁ ⊕ Δφ₂) = f(Δφ₁) + f(Δφ₂)
```
Da f bijektiv ist, existiert ⊕ eindeutig:
```
    Δφ₁ ⊕ Δφ₂ := f⁻¹(f(Δφ₁) + f(Δφ₂))
```

### 6.2 Explizite Formel für ⊕

Mit f⁻¹(φ) = 2·arccos(sech(φ)) und sech(φ₁+φ₂) = sech(φ₁)sech(φ₂) / (1 + tanh(φ₁)tanh(φ₂)):

Sei p = cos(Δφ₁/2), q = cos(Δφ₂/2), dann ist sech(φᵢ) = p bzw. q, und:
```
    cosh(φ₁ + φ₂) = cosh(φ₁)cosh(φ₂) + sinh(φ₁)sinh(φ₂)
                  = (1/p)(1/q) + (√(1−p²)/p)(√(1−q²)/q)
                  = (1 + sin(Δφ₁/2)·sin(Δφ₂/2)) / (cos(Δφ₁/2)·cos(Δφ₂/2))
```
Daher:
```
    cos((Δφ₁ ⊕ Δφ₂)/2) = sech(φ₁ + φ₂)
                        = cos(Δφ₁/2) · cos(Δφ₂/2)
                          / (1 + sin(Δφ₁/2) · sin(Δφ₂/2))
```
und damit:
```
    Δφ₁ ⊕ Δφ₂ = 2 arccos(cos(Δφ₁/2) · cos(Δφ₂/2)
                          / (1 + sin(Δφ₁/2) · sin(Δφ₂/2)))
```

### 6.3 Vergleich mit relativistischer Geschwindigkeitsaddition

Die relativistische Geschwindigkeitsaddition lautet (via Rapiditäten):
```
    v₁₂/c = tanh(φ₁ + φ₂) = (tanh(φ₁) + tanh(φ₂)) / (1 + tanh(φ₁)tanh(φ₂))
           = (v₁/c + v₂/c) / (1 + v₁v₂/c²)
```

Über die Identifikation v = c·tanh(f(Δφ)) = c·tanh(artanh(sin(Δφ/2))) = c·sin(Δφ/2)
ergibt sich:
```
    v/c = sin(Δφ/2)    [RFT-Geschwindigkeitsparameter]
```

Damit wird das RFT-Phasenkompositionsgesetz zur relativistischen Geschwindigkeitsaddition:
```
    sin((Δφ₁ ⊕ Δφ₂)/2)
    = (sin(Δφ₁/2) + sin(Δφ₂/2)) / (1 + sin(Δφ₁/2)·sin(Δφ₂/2))
```
*Herleitung:* Mit p = cos(Δφ₁/2), q = cos(Δφ₂/2):
```
    sin((Δφ₁ ⊕ Δφ₂)/2) = √(1 − cos²((Δφ₁ ⊕ Δφ₂)/2))
```
Einsetzen der Formel aus §6.2 und tanh(φ₁+φ₂) = (tanh φ₁ + tanh φ₂)/(1+tanh φ₁ tanh φ₂)
mit tanh(φᵢ) = sin(Δφᵢ/2) bestätigt diese Identität.

**Fazit:** Die RFT-Phasenkomposition ⊕ ist strukturell identisch mit der relativistischen
Geschwindigkeitsaddition, wenn man v/c = sin(Δφ/2) setzt.

### 6.4 Grenzfälle

| Situation | Δφ₁ | Δφ₂ | Δφ₁ ⊕ Δφ₂ | physikalische Interpretation |
|---|---|---|---|---|
| Keine Bewegung | 0 | Δφ | Δφ | Neutralelement (v₁ = 0) |
| Kleine Geschw. | ε₁ | ε₂ | ε₁ + ε₂ + O(ε²) | Galilei-Grenzfall |
| v₁ → c | π⁻ | Δφ | π⁻ | c + v = c (Lichtkonstanz) |

---

## 7. Erfolgskriterium: Beweis der Bijektivität und Additivität

**Satz (AP1-Hauptresultat):**

Die Abbildung
```
    f: [0, π) → [0, ∞),    f(Δφ) = arcsech(cos(Δφ/2)) = artanh(sin(Δφ/2))
```
erfüllt alle Bedingungen des Erfolgskriteriums:

1. **Bijektivität:** f ist streng monoton wachsend (df/dΔφ = 1/(2cos(Δφ/2)) > 0),
   f(0) = 0, lim_{Δφ→π} f(Δφ) = ∞. Damit ist f: [0,π) → [0,∞) bijektiv.

2. **Additivität:** Mit der Kompositionsregel
   ```
       Δφ₁ ⊕ Δφ₂ = 2 arccos(cos(Δφ₁/2)·cos(Δφ₂/2) / (1 + sin(Δφ₁/2)·sin(Δφ₂/2)))
   ```
   gilt: f(Δφ₁ ⊕ Δφ₂) = f(Δφ₁) + f(Δφ₂).

   *Beweis der Additivität:*
   ```
       f(Δφ₁ ⊕ Δφ₂)
       = artanh(sin((Δφ₁ ⊕ Δφ₂)/2))
       = artanh((sin(Δφ₁/2) + sin(Δφ₂/2)) / (1 + sin(Δφ₁/2)·sin(Δφ₂/2)))
   ```
   Für artanh gilt das Additionstheorem:
   ```
       artanh(x) + artanh(y) = artanh((x+y)/(1+xy))    für |xy| < 1
   ```
   Also:
   ```
       f(Δφ₁ ⊕ Δφ₂) = artanh(sin(Δφ₁/2)) + artanh(sin(Δφ₂/2))
                     = f(Δφ₁) + f(Δφ₂)    ✓
   ```
   (Die Bedingung |xy| < 1 ist für Δφ₁, Δφ₂ ∈ [0,π) mit sin < 1 erfüllt.)

**Das Erfolgskriterium von AP1 ist vollständig bewiesen.** □

---

## 8. Ergebnis und Ausblick auf AP2–AP4

### 8.1 Zusammenfassung der AP1-Ergebnisse

| Frage (AP1) | Ergebnis |
|---|---|
| Wertbereich Δφ aus A1–A4? | Δφ ∈ [0, π), kanonisch durch A4-Monotonie |
| Hyperbolische Metrik auf Phasenraum? | **Ja:** ds²_RFT = dΔφ²/(4ε(Δφ)) |
| Phasenaddition konsistent mit Relativität? | **Ja:** ⊕ ist strukturgleich zur relativistischen Geschwindigkeitsaddition |
| Bijektive Abbildung f mit Additivität? | **Ja:** f(Δφ) = artanh(sin(Δφ/2)), bewiesen |

**Kernresultat:** Δφ und die relativistische Rapidität φ besitzen dieselbe
mathematische Struktur. Die Identifikation
```
    φ = artanh(sin(Δφ/2))    ⟺    Δφ = 2 arcsin(tanh φ)
```
(äquivalent zur Brückenformel Δφ = 2 arccos(sech φ)) ist eine exakte mathematische
Isometrie, keine Näherung oder Analogie.

### 8.2 Was AP1 leistet und was nicht

**AP1 leistet:**
- Mathematische Isometrie zwischen RFT-Phasenraum und Rapiditätsachse nachgewiesen.
- Explizite bijektive Abbildung konstruiert und bewiesen.
- Hyperbolische Metrikstruktur auf dem Phasenraum identifiziert.
- RFT-Kompositionsgesetz als Äquivalent zur relativistischen Geschwindigkeitsaddition gezeigt.

**AP1 leistet nicht (offen für AP2–AP4):**
- Die Identifikation ε = 1/γ² ist noch nicht aus A4 abgeleitet — sie ist
  Voraussetzung hier, Gegenstand von **AP2**.
- Die Brückenformel ist als Konsequenz von ε = cos²(Δφ/2) gezeigt, aber die
  physikalische Bedeutung (c als strukturelle Grenze) erfordert **AP4**.
- Die Lorentz-Transformation selbst (Koordinatenraum) ist Gegenstand von **AP3**.

### 8.3 Bedeutung für RT-40

AP1 liefert das formale Gerüst, auf dem AP2–AP6 aufbauen. Die Isometrie ist nicht
heuristisch, sondern exakt bewiesen. Die Brückenformel
```
    Δφ = 2 arccos(sech φ)   ⟺   ε(Δφ) = 1/γ²
```
ist kein Zufall, sondern die explizite Form der bijektiven Abbildung zwischen
RFT-Phasenraum und Minkowski-Rapiditätsraum.

**Nächster Schritt (AP2):** Zeigen, dass ε(Δφ) = 1/γ² direkt aus der
Interpretation von A4 als relativistischer Resonatorenergie E = γmc² folgt.

---

## Verbindungen zu bestehenden Dokumenten

- Axiome A1–A4: [`../docs/definitionen/axiomatische_grundlegung.md`](../docs/definitionen/axiomatische_grundlegung.md)
- ε = cos²(Δφ/2) Eindeutigkeit (RT-02): [`gsync_gruppenstruktur.md`](gsync_gruppenstruktur.md)
- π als geometrischer Faktor (RT-01): [`wirkungsintegral_pi_herleitung.md`](wirkungsintegral_pi_herleitung.md)
- RT-40 Gesamtübersicht: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
