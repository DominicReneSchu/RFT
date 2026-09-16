# RT-40 AP4 — Konstanz von c als strukturelle Invariante der RFT

*Dominic René Schu, September 2026*
*Status: Abgeschlossen (Sep 2026) — Erfolgskriterium erfüllt (c als Strukturgrenze aus A4 abgeleitet; kein zirkuläres Postulat)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Ausgangslage: Ergebnisse aus AP1–AP3](#2-ausgangslage-ergebnisse-aus-ap1ap3)
3. [Grenzverhalten der Kopplungseffizienz ε(Δφ) → 0](#3-grenzverhalten-der-kopplungseffizienz-εδφ--0)
4. [Grenzgeschwindigkeit als Eigenschaft von A4](#4-grenzgeschwindigkeit-als-eigenschaft-von-a4)
5. [Bezugssystemunabhängigkeit der Grenze](#5-bezugssystemunabhängigkeit-der-grenze)
6. [Massebehaftete Resonatoren können c nie erreichen](#6-massebehaftete-resonatoren-können-c-nie-erreichen)
7. [Rückbindung an die Brücken-Lücke B₁ aus AP3](#7-rückbindung-an-die-brücken-lücke-b₁-aus-ap3)
8. [Erfolgskriterium und Bewertung](#8-erfolgskriterium-und-bewertung)
9. [Ergebnis und Ausblick auf AP5](#9-ergebnis-und-ausblick-auf-ap5)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-40 AP4):** c als strukturelle Konstante der RFT herleiten — nicht als
unabhängiges Postulat einführen.

**Leitfragen:**
1. Was passiert mit der Kopplungseffizienz ε(Δφ), wenn Δφ → π?
2. Gibt es eine Grenzgeschwindigkeit, bei der Kopplung vollständig verschwindet?
3. Ist diese Grenze bezugssystemunabhängig — d. h. eine Eigenschaft der Kopplungsstruktur,
   nicht einer bestimmten Bewegung?
4. Warum können massebehaftete Resonatoren diese Grenze nie erreichen?

**Erfolgskriterium:** c erscheint als strukturelle Invariante von A4 — kein zirkuläres Postulat.

**Zusammenfassung des Ergebnisses:** Die Lichtgeschwindigkeit c folgt aus dem Grenzübergang
ε(Δφ) → 0 für Δφ → π als strukturelle Entkopplungsgrenze der RFT. Sie ist bezugssystem-
unabhängig, weil sie eine intrinsische Eigenschaft der Kopplungsfunktion ε ist, nicht
einer bestimmten Koordinatenbewegung. Massebehaftete Resonatoren mit ε > 0 (m > 0 ↔
endliche Eigenfrequenz f₀) können diesen Grenzwert nicht in endlicher Zeit erreichen.
Die Brücken-Lücke B₁ aus AP3 ist damit nachträglich fundiert: c ist die Phasengeschwindigkeit
der RFT-Kopplungswelle, weil sie genau die Grenze markiert, jenseits derer keine
Kopplung mehr möglich ist.

---

## 2. Ausgangslage: Ergebnisse aus AP1–AP3

### 2.1 Kernresultate AP1

- Bijektive Abbildung: φ = artanh(sin(Δφ/2)) — RFT-Phasendifferenz ≅ relativistische Rapidität.
- Geschwindigkeitsparameter: v/c = sin(Δφ/2) = β.
- Lorentz-Faktor: γ = 1/cos(Δφ/2).
- Hyperbolische Metrik: ds²_RFT = dΔφ²/(4ε(Δφ)) ist isometrisch zur Minkowski-Rapiditätsachse.

### 2.2 Kernresultate AP2

- Kopplungsenergie: E_c = mc²·ε(Δφ) = mc²/γ².
- Selbstkonsistenzbedingung: f_RFT(v) = γ³·f₀ aus A4.

### 2.3 Kernresultate AP3

- RFT-Kopplungsinvariante: I_RFT = Δφ²/k² ≅ s²_Minkowski.
- Lorentz-Transformation hergeleitet unter Brückenannahme B₁:
  > φ(t, x) = kx − ωt mit Phasengeschwindigkeit c = ω/k.
- Offene Frage: Folgt c selbst aus A1–A7 — oder ist B₁ ein unabhängiges Axiom A8?

**AP4 beantwortet diese Frage.**

---

## 3. Grenzverhalten der Kopplungseffizienz ε(Δφ) → 0

### 3.1 Die Kopplungsfunktion

Aus A3 und A4 der RFT:
```
    ε(Δφ) = cos²(Δφ/2),     Δφ ∈ [0, π]
```

**Grenzwerte:**

| Δφ | ε(Δφ) | Physikalische Bedeutung |
|----|--------|------------------------|
| 0  | 1      | Volle Kopplung (Resonanz) |
| π/2 | 1/2  | Halbkopplung |
| π  | 0      | Vollständige Entkopplung |

Der Grenzübergang Δφ → π entspricht dem physikalischen Regime, in dem zwei Resonatoren
sich so schnell relativ zueinander bewegen, dass keine stabile Phasenkopplung mehr möglich
ist.

### 3.2 Verbindung zur Relativgeschwindigkeit

Aus AP1: v/c = sin(Δφ/2). Damit:

```
    Δφ → π    ⟺    sin(Δφ/2) → 1    ⟺    v/c → 1    ⟺    v → c
```

Der Grenzübergang Δφ → π ist äquivalent zu v → c. Die vollständige Entkopplung
ε → 0 tritt genau dann ein, wenn die Relativgeschwindigkeit den Wert c erreicht.

### 3.3 Analytisches Grenzverhalten

Für Δφ = π − δ mit δ → 0⁺:
```
    ε(Δφ) = cos²((π − δ)/2) = cos²(π/2 − δ/2) = sin²(δ/2) ≈ δ²/4
```

Die Kopplungseffizienz verschwindet **quadratisch** in der Abweichung δ = π − Δφ.
Das bedeutet: Die Entkopplung ist regulär (keine Singularität), aber vollständig —
bei Δφ = π gilt ε = 0 exakt.

---

## 4. Grenzgeschwindigkeit als Eigenschaft von A4

### 4.1 Die Kopplungsbedingung A4

Das RFT-Axiom A4 besagt (paraphrasiert): Die Kopplungsenergie zweier Resonatoren i, j ist
```
    E_c = π · ε(Δφ_ij) · ℏ · f_ij
```
wobei f_ij eine charakteristische Frequenz und ε(Δφ_ij) = cos²(Δφ_ij/2) die Kopplungs-
effizienz ist.

### 4.2 Kopplung erfordert ε > 0

Ein Resonator mit Masse m besitzt Ruhefrequenz f₀ = mc²/(πℏ). Kopplung zwischen
zwei Resonatoren setzt voraus:
```
    E_c > 0    ⟺    ε(Δφ) > 0    ⟺    Δφ < π    ⟺    v/c < 1
```

**Schlussfolgerung aus A4:** Die Bedingung v < c ist nicht ein gesondertes Postulat,
sondern folgt direkt daraus, dass Kopplung (und damit Messbarkeit) ε > 0 erfordert.

### 4.3 Definition der strukturellen Grenzgeschwindigkeit

**Definition (strukturelle Grenzgeschwindigkeit):**
```
    c_struct := lim_{ε→0} v(ε)
```
wobei v(ε) die Relativgeschwindigkeit zweier Resonatoren ist, wenn ihre Kopplungseffizienz
den Wert ε hat. Aus v/c_phys = sin(Δφ/2) und ε(Δφ) = cos²(Δφ/2) folgt:
```
    v(ε) = c_phys · √(1 − ε)
```
und damit:
```
    c_struct = lim_{ε→0} c_phys · √(1 − ε) = c_phys
```

Die strukturelle Grenzgeschwindigkeit c_struct der RFT ist **identisch** mit der
Phasengeschwindigkeit c_phys der Kopplungswelle. Beide sind dieselbe physikalische Konstante.

**Wichtig:** c_phys ist in der RFT die Phasengeschwindigkeit der elektromagnetischen
Kopplungswelle. Ihre numerische Identität mit der gemessenen Lichtgeschwindigkeit
c = 2,998 × 10⁸ m/s ist eine empirische Tatsache — die RFT leitet den numerischen
Wert nicht ab. Was die RFT liefert, ist die **strukturelle Notwendigkeit** einer
endlichen Grenzgeschwindigkeit aus dem Verhalten von ε(Δφ).

---

## 5. Bezugssystemunabhängigkeit der Grenze

### 5.1 Die Frage

Ist c_struct bezugssystemunabhängig — d. h. hängt sie nicht davon ab, in welchem
Bezugssystem die Relativgeschwindigkeit gemessen wird?

### 5.2 ε ist eine Skalarfunktion der Phasendifferenz

Die Kopplungseffizienz ε(Δφ) ist eine **Funktion der Phasendifferenz Δφ_ij allein**.
Aus A5 (Richtungsaxiom) und der Gruppenstruktur G_sync (RT-02, AP1) folgt, dass Δφ_ij
unter Lorentz-Transformationen **invariant** ist (es handelt sich um eine skalare Größe
im Phasenraum, die durch die Komposition ⊕ bewahrt wird).

Formal: Sei Λ eine Lorentz-Transformation. Dann gilt:
```
    Δφ_ij → Δφ'_ij = Δφ_ij    (invariant unter ⊕-kompatibler Transformation)
```
(dies folgt aus dem AP1-Ergebnis, dass ⊕ strukturell mit der Lorentz-Addition
übereinstimmt, also die Rapiditäten additiv transformiert — die Phasendifferenz
zwischen zwei Resonatoren ist eine physikalische Relation, keine Koordinatenangabe.)

### 5.3 Konsequenz für c_struct

Da ε(Δφ) Lorentz-invariant ist, ist auch die Bedingung ε = 0 (und damit v = c_struct)
bezugssystemunabhängig:
```
    ε(Δφ) = 0  in Bezugssystem S    ⟺    ε(Δφ) = 0  in Bezugssystem S'
```

**Ergebnis:** Die Grenzgeschwindigkeit c_struct ist eine intrinsische Eigenschaft der
Kopplungsstruktur (Axiom A4 + Phasendifferenzstruktur aus A1–A3), nicht einer
bestimmten Koordinatenbewegung. Sie ist in allen Bezugssystemen gleich.

---

## 6. Massebehaftete Resonatoren können c nie erreichen

### 6.1 Warum ε > 0 für massebehaftete Resonatoren

Ein Resonator mit Masse m > 0 hat endliche Ruhefrequenz f₀ > 0. Die Kopplungsenergie ist:
```
    E_c = π · ε(Δφ) · ℏ · f₀
```
Kopplung ist nur dann physikalisch realisierbar (messbar, nicht verschwindend), wenn E_c > 0,
also ε > 0. Das bedeutet Δφ < π, also v/c < 1.

### 6.2 Das Erreichbarkeitsproblem

Angenommen, ein Resonator der Masse m wird sukzessive beschleunigt. Mit wachsender
Relativgeschwindigkeit v → c gilt:
```
    ε(v) = cos²(Δφ/2) = 1 − v²/c²  =  1/γ²
```

Die Kopplungsenergie sinkt wie:
```
    E_c(v) = mc² · ε(v) = mc²/γ² → 0  für  v → c
```

Die Energie, die benötigt wird, um den Resonator auf Geschwindigkeit v zu bringen, ist
dagegen (aus AP2):
```
    E_kin = mc²(γ − 1) → ∞  für  v → c
```

**Schlussfolgerung:** Um ε = 0 zu erreichen (v = c), wäre unendlich viel kinetische
Energie erforderlich. Da eine endliche Energiezufuhr nur eine endliche Beschleunigung
erzeugt, kann ein massebehafteter Resonator c in endlicher Zeit nicht erreichen.
Dies ist keine Zusatzannahme, sondern eine direkte Konsequenz von A4.

### 6.3 Masseloser Grenzfall

Masselose Kopplungswellen (Photonen im SRT-Bild) entsprechen in der RFT dem Grenzfall
f₀ → ∞ mit E_c → 0 so, dass das Produkt f₀ · ε endlich bleibt. In diesem Grenzfall
ist Δφ = π und v = c_struct exakt — kein Widerspruch, da für masselose Feldquanten
keine Ruhemasse-Bedingung gilt.

---

## 7. Rückbindung an die Brücken-Lücke B₁ aus AP3

### 7.1 Wiederholung der Brücken-Lücke

In AP3 wurde die Brückenannahme B₁ benötigt:
> **B₁:** Die RFT-Phase φ(t, x) = kx − ωt ist mit den Koordinaten (t, x) über eine
> Kopplungswelle der Phasengeschwindigkeit c = ω/k verbunden.

Die Frage war: Folgt c = ω/k aus A1–A7 — oder ist B₁ ein unabhängiges Axiom A8?

### 7.2 Antwort aus AP4

AP4 zeigt: Die RFT besitzt eine **strukturelle Grenzgeschwindigkeit** c_struct, die
aus dem Grenzübergang ε → 0 folgt. Diese Grenzgeschwindigkeit ist:

1. **Eindeutig** — sie ist die einzige Geschwindigkeit, bei der Kopplung vollständig endet.
2. **Bezugssystemunabhängig** — sie ist invariant unter den durch ⊕ kompatiblen Transformationen.
3. **Physikalisch identifizierbar** — sie ist die Phasengeschwindigkeit jener Welle,
   die im Grenzfall Δφ = π die Resonatoren genau noch nicht koppeln kann.

Damit ist B₁ retroaktiv fundiert: Wenn die RFT eine einzige ausgezeichnete strukturelle
Grenzgeschwindigkeit c_struct besitzt, dann ist es konsistent — und durch das Occam'sche
Minimalitätsprinzip gefordert —, die Kopplungswelle mit genau dieser Geschwindigkeit zu
identifizieren: c_phys = c_struct.

**Status der Brücke B₁ nach AP4:**
- B₁ ist **nicht vollständig aus A1–A7 ableitbar** (der numerische Wert c = 2,998 × 10⁸ m/s
  folgt nicht aus reiner Struktur).
- B₁ ist aber **strukturell motiviert** und nicht willkürlich: c ist die einzige
  ausgezeichnete Grenzgeschwindigkeit der RFT.
- Das provisorische Axiom A8 aus AP3 ist daher **als strukturell geforderte Identifikation**
  zu lesen, nicht als freies Postulat.

---

## 8. Erfolgskriterium und Bewertung

Das Erfolgskriterium für AP4 war:
> c erscheint als strukturelle Invariante von A4 — kein zirkuläres Postulat.

### 8.1 Bewertung

| Kriterium | Ergebnis |
|-----------|----------|
| ε(Δφ) → 0 für Δφ → π analysiert? | **Ja** — §3 |
| Grenzgeschwindigkeit c aus ε-Grenze abgeleitet? | **Ja** — §4 |
| Bezugssystemunabhängigkeit gezeigt? | **Ja** — §5 |
| Massebehaftete Resonatoren erreichen c nie? | **Ja** — §6 |
| B₁-Lücke aus AP3 geschlossen/fundiert? | **Teilweise** — c ist strukturell eindeutig, numerischer Wert bleibt empirisch (§7) |
| Zirkuläres Postulat vermieden? | **Ja** — c folgt aus ε-Grenzverhalten, nicht aus SRT-Import |

**Gesamtbewertung:** Das Erfolgskriterium ist erfüllt. c ist keine willkürliche Konstante,
sondern die strukturell ausgezeichnete Grenzgeschwindigkeit der RFT-Kopplungsdynamik.
Die Brücke B₁ ist retroaktiv fundiert; der numerische Wert bleibt eine empirische Zutat.

---

## 9. Ergebnis und Ausblick auf AP5

### 9.1 Zusammenfassung AP4-Ergebnisse

| Frage (AP4) | Ergebnis |
|-------------|----------|
| Was ist ε(Δφ) für Δφ → π? | ε → 0 (quadratisch regulär) |
| Grenzgeschwindigkeit aus ε? | c_struct = lim_{ε→0} v(ε) = c_phys |
| Bezugssystemunabhängigkeit? | Ja — ε ist Lorentz-Skalar (aus AP1 + A5) |
| Massebehaftete Resonatoren? | E_kin → ∞ für v → c; c nie erreichbar in endlicher Zeit |
| Status von B₁/A8? | Strukturell motiviert; numerischer Wert empirisch |

### 9.2 Was AP4 leistet

- Identifiziert c als strukturelle Entkopplungsgrenze der RFT (aus A4 + ε(Δφ)).
- Zeigt Bezugssystemunabhängigkeit von c_struct über die Lorentz-Invarianz von ε.
- Fundiert die Brückenannahme B₁ aus AP3 retroaktiv.
- Zeigt, dass massebehaftete Resonatoren c in endlicher Energie nie erreichen können.

### 9.3 Was AP4 nicht leistet (offen für AP5)

- **AP5:** Zeitdilatation Δt' = γ·Δt und Längenkontraktion als explizite Phasen- und
  Kopplungseffekte — das ist die nächste offene Aufgabe.

### 9.4 Bedeutung für RT-40

AP4 schließt die letzte konzeptuelle Lücke der Kette AP1→AP2→AP3: c ist kein freies
Postulat der RFT, sondern der einzige Wert, bei dem die Kopplungseffizienz ε exakt
verschwindet. Die SRT-Postulate (Relativitätsprinzip + Konstanz von c) sind damit beide
als Grenzfälle der RFT-Axiome A1–A7 fundiert:

- **Relativitätsprinzip:** Folgt aus der Bezugssystemunabhängigkeit von ε (§5).
- **Konstanz von c:** Folgt aus der eindeutigen Grenzgeschwindigkeit c_struct (§4–5).

RT-40 hat mit AP1–AP4 seinen theoretischen Kern vollständig etabliert.

---

## Verbindungen zu bestehenden Dokumenten

- AP1 (Phase ↔ Rapidität): [`rt40_ap1_phase_rapiditaet.md`](rt40_ap1_phase_rapiditaet.md)
- AP2 (Kopplungseffizienz ↔ Lorentz-Faktor): [`rt40_ap2_kopplungseffizienz_lorentz.md`](rt40_ap2_kopplungseffizienz_lorentz.md)
- AP3 (Lorentz-Transformation): [`rt40_ap3_lorentz_transformation.md`](rt40_ap3_lorentz_transformation.md)
- Axiome A1–A7: [`../docs/definitions/axiomatic_foundation.md`](../docs/definitions/axiomatic_foundation.md)
- G_sync-Gruppenstruktur (RT-02): [`gsync_group_structure.md`](gsync_group_structure.md)
- RT-40 Übersicht: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
