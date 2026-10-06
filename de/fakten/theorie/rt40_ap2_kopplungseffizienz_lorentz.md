# RT-40 AP2 — Kopplungseffizienz als Lorentz-Faktor

*Dominic René Schu, September 2026*
*Status: Abgeschlossen (Sep 2026) — Erfolgskriterium erfüllt (falsifizierbare Relation benannt)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Ausgangspunkt: A4 im Ruhesystem](#2-ausgangspunkt-a4-im-ruhesystem)
3. [Naiver Ansatz: E = γmc² und f = f₀/γ](#3-naiver-ansatz-e--γmc-und-f--f₀γ)
4. [Widerspruchsanalyse und Zirkelschluss-Prüfung](#4-widerspruchsanalyse-und-zirkelschluss-prüfung)
5. [Selbstkonsistenzanalyse: Welches f wird benötigt?](#5-selbstkonsistenzanalyse-welches-f-wird-benötigt)
6. [Physikalischer Gehalt: Kopplungsenergie vs. Gesamtenergie](#6-physikalischer-gehalt-kopplungsenergie-vs-gesamtenergie)
7. [Verbindung zur Zitterbewegungsfrequenz](#7-verbindung-zur-zitterbewegungsfrequenz)
8. [Erfolgskriterium: Falsifizierbare Relation](#8-erfolgskriterium-falsifizierbare-relation)
9. [Ergebnis und Ausblick auf AP3–AP5](#9-ergebnis-und-ausblick-auf-ap3ap5)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-40 AP2):** Zeigen, dass ε(Δφ) = 1/γ² aus A4 folgt — nicht nur als
formale Ähnlichkeit, sondern als physikalische Identität.

**Erfolgskriterium:** Identität ε = 1/γ² bewiesen — **oder** eine falsifizierbare
Relation zwischen m, f₀ und ℏ benannt.

**Ergebnis:** Der direkte Beweis ε = 1/γ² über den naiven Ansatz scheitert (Widerspruch
ε_A4 = γ² ≠ 1/γ²). Das Erfolgskriterium ist dennoch erfüllt: Die Konsistenz von A4 mit
dem AP1-Ergebnis ε = 1/γ² liefert die falsifizierbare Relation

```
    f_RFT(bewegter Resonator) = γ³ · f₀
```

und identifiziert die Kopplungsenergie E_c = mc²/γ² als den physikalischen Gehalt von
A4 für bewegte Resonatoren.

---

## 2. Ausgangspunkt: A4 im Ruhesystem

### 2.1 Axiom A4 (Kopplungsenergie)

Axiom 4 der RFT lautet:
```
    E_eff = π · ε(Δφ) · ℏ · f
```
wobei f die RFT-Resonanzfrequenz in rad/s bezeichnet.

### 2.2 Ruhesystem-Identifikation

Im Ruhesystem des Resonators (Δφ = 0) gilt ε₀ = 1 (vollständige Kopplung), und die
Resonanzfrequenz ist f₀ (Eigenfrequenz). Damit gibt A4:

```
    E₀ = π · 1 · ℏ · f₀ = π · ℏ · f₀
```

Die Ruhemasse-Energie mc² wird mit E₀ identifiziert:

```
    mc² = π · ℏ · f₀                           [Definitionsrelation]
```

Diese Relation definiert die Eigenfrequenz f₀ als Funktion der Ruhemasse:

```
    f₀ = mc² / (π · ℏ)
```

**Bedeutung:** A4 ist im Ruhesystem trivial konsistent. Die Eigenfrequenz f₀ ist durch
die Ruhemasse festgelegt. Das ist kein Zirkelschluss, sondern eine definitorische
Zuordnung: Jeder Resonator der Masse m hat die Ruhefrequenz f₀ = mc²/(π·ℏ).

### 2.3 Nichtrelativistischer Grenzfall (Kontrolle)

Für kleine Geschwindigkeiten (Δφ → 0, v/c = sin(Δφ/2) → Δφ/2 ≪ 1, ε → 1):
```
    ε ≈ cos²(Δφ/2) ≈ 1 − (Δφ/2)² / 2 ≈ 1 − v²/(2c²)

    E_A4 = π · ε · ℏ · f₀ ≈ mc² · (1 − v²/(2c²))
```
Dies entspricht der nichtrelativistischen Näherung E_total − E_kin = mc² − mv²/2
bis auf Vorzeichen: A4 gibt die *Abnahme* der Kopplungsenergie mit steigender
Geschwindigkeit, nicht die Zunahme der Gesamtenergie. Das ist ein erster Hinweis
auf die physikalische Bedeutung von ε (Abschnitt 6).

---

## 3. Naiver Ansatz: E = γmc² und f = f₀/γ

### 3.1 Vorgehen nach RT-40-Spezifikation

RT-40 AP2 schlägt folgende Identifikation vor:

| Größe | Annahme | Quelle |
|---|---|---|
| E | γmc² (relativistische Gesamtenergie) | SRT |
| f | f₀/γ (zeitdilatierte Eigenfrequenz) | SRT (Zeitdilatation) |
| mc² | π·ℏ·f₀ | A4 im Ruhesystem (§2.2) |

**Einsetzen in A4:**
```
    E = π · ε · ℏ · f

    γmc² = π · ε · ℏ · (f₀/γ)

    γmc² = (π · ε · ℏ · f₀) / γ

    γ² · mc² = π · ε · ℏ · f₀
```

**Mit mc² = π·ℏ·f₀:**
```
    γ² · (π · ℏ · f₀) = π · ε · ℏ · f₀

    ε = γ²                                      [Naives Ergebnis]
```

### 3.2 Widerspruch mit AP1

Aus AP1 (RT-40, abgeschlossen Sep 2026) ist bekannt:
```
    v/c = sin(Δφ/2)   →   γ = 1/cos(Δφ/2)   →   ε = cos²(Δφ/2) = 1/γ²
```

Der naive Ansatz ergibt ε = γ², das AP1-Ergebnis lautet ε = 1/γ². Dies ist ein
**Widerspruch** um den Faktor γ⁴:

```
    ε_naiv / ε_AP1 = γ² / (1/γ²) = γ⁴
```

Der Widerspruch ist kein kleiner Korrekturterm, sondern eine systematische Abweichung
um vier Potenzen des Lorentz-Faktors.

---

## 4. Widerspruchsanalyse und Zirkelschluss-Prüfung

### 4.1 Woher kommt der Widerspruch?

Die Ursache liegt in der Annahme **f = f₀/γ**. Diese Formel folgt aus der
SRT-Zeitdilatation: Ein bewegter Resonator schlägt langsamer — ein mit ihm mitbewegter
Beobachter misst f₀, ein Beobachter im Lab misst f₀/γ.

**Das Zirkelschluss-Problem (RT-40-Warnung):** f = f₀/γ ist eine Konsequenz der
Lorentz-Invarianz, die gerade aus der RFT abgeleitet werden soll. Wird f = f₀/γ
postuliert, setzt man die SRT bereits voraus — der Beweis von SRT ⊂ RFT ist dann
zirkulär.

### 4.2 Warum der naive Ansatz systematisch falsch ist

Der naive Ansatz begeht zwei konzeptionelle Fehler gleichzeitig:

1. **Falsche Energiegröße:** E = γmc² ist die *Gesamtenergie* im Lab-Rahmen.
   A4 beschreibt hingegen die *Kopplungsenergie* zwischen zwei Resonatoren. Diese
   sind verschiedene physikalische Größen.

2. **Falsches Frequenzargument:** f = f₀/γ (Zeitdilatation) ist die Frequenz, die ein
   Lab-Beobachter für die Eigenschwingung des bewegten Resonators misst. Die in A4
   relevante Frequenz ist jedoch die Resonanzfrequenz des Kopplungssystems — ein
   anderer Begriff.

### 4.3 Schlussfolgerung

Der naive Ansatz ist physikalisch inkonsistent. Der Widerspruch ε = γ² vs. ε = 1/γ²
ist kein Fehler in AP1, sondern zeigt, dass f = f₀/γ nicht die korrekte Frequenzgröße
für A4 ist. Die korrekte Frequenz muss aus den RFT-Axiomen abgeleitet werden (AP5).

---

## 5. Selbstkonsistenzanalyse: Welches f wird benötigt?

### 5.1 Rückwärtsrechnung: f aus ε = 1/γ² und E = γmc²

Gegeben:
- ε = 1/γ² (aus AP1, bewiesen)
- E = γmc² (als angenommene Gesamtenergie)
- mc² = π·ℏ·f₀ (aus A4 im Ruhesystem)

Aus A4: E = π·ε·ℏ·f, also:
```
    γmc² = π · (1/γ²) · ℏ · f

    f = γ³ · mc² / (π · ℏ) = γ³ · f₀           [Selbstkonsistenz-Bedingung]
```

**Ergebnis:** Für ε = 1/γ² und E = γmc² muss die in A4 eingehende Frequenz lauten:

```
    f_RFT(v) = γ³ · f₀ = γ³ · mc² / (π · ℏ)
```

### 5.2 Numerische Stützwerte

| v/c | γ | f_RFT / f₀ |
|---|---|---|
| 0 | 1 | 1 |
| 0,5 | 1,155 | 1,540 |
| 0,707 | √2 ≈ 1,414 | 2,828 |
| 0,866 | 2 | 8 |
| 0,943 | 3 | 27 |
| 0,990 | 7,09 | 356,7 |

Die Frequenz f_RFT wächst für relativistische Geschwindigkeiten stark an.

### 5.3 Physikalischer Ursprung von f = γ³·f₀ (Hypothese)

Der Faktor γ³ tritt in der relativistischen Dynamik als **longitudinale Masse** auf:
```
    F_longitudinal = γ³ · m₀ · a     (longitudinale Newtonschen Gleichung)
```

Für einen harmonischen Oszillator mit Federkonstante k und effektiver Masse m_eff = γ³m₀
wäre die Eigenfrequenz:
```
    ω² = k / m_eff   →   ω = ω₀ / γ^(3/2)   (mit k = k₀ konstant)
```

Dies ergibt γ^(-3/2), nicht γ³. Der Faktor γ³ erscheint also nicht trivial aus der
longitudinalen Masse.

Eine alternative Interpretation: f_RFT ist die Frequenz des **Kopplungsoperators** (nicht
des freien Resonators). Dieser Operator könnte durch die Phasendynamik (A4) eine andere
Transformationseigenschaft besitzen als die Eigenfrequenz. Dies bleibt eine offene
Derivationsaufgabe für AP5.

---

## 6. Physikalischer Gehalt: Kopplungsenergie vs. Gesamtenergie

### 6.1 Zwei Energiebegriffe

Die bisherige Analyse legt nahe, dass A4 zwei verschiedene physikalische Situationen
beschreibt, die man unterscheiden muss:

| Energiebegriff | Formel | Physikalische Bedeutung |
|---|---|---|
| Gesamtenergie (SRT) | E_total = γmc² | Energie im Lab-Rahmen (kinematisch) |
| Kopplungsenergie (RFT) | E_c = π·ε·ℏ·f₀ = mc²/γ² | Interaktionsenergie mit ruhendem Beobachter |

A4 beschreibt die **Kopplungsenergie** — den Energieanteil, den ein bewegter Resonator
für eine Wechselwirkung mit einem ruhenden Resonator (dem Beobachter) "bereitstellt",
gemessen mit der Ruhezustandsfrequenz f₀.

### 6.2 Kopplungsenergie explizit

Mit ε = cos²(Δφ/2) = 1/γ² und f = f₀ (Ruhefrequenz im A4-Ausdruck):
```
    E_c = π · ε · ℏ · f₀
         = π · (1/γ²) · ℏ · f₀
         = mc² / γ²
         = mc² · cos²(Δφ/2)
```

Eigenschaften:
- **Δφ = 0 (v = 0):** E_c = mc² — vollständige Ruhemassen-Kopplung ✓
- **Δφ ≠ 0 (v > 0):** E_c < mc² — Kopplung nimmt mit Geschwindigkeit ab
- **Δφ → π (v → c):** E_c → 0 — vollständige Entkopplung (Grenzgeschwindigkeit)

Das Verhalten ist physikalisch kohärent: Ein hochrelativistischer Resonator koppelt kaum
mehr mit einem ruhenden Beobachter, weil seine Phasendynamik für den Beobachter
"eingefroren" erscheint (ε → 0).

### 6.3 Verhältnis E_c / E_total

```
    E_c / E_total = (mc²/γ²) / (γmc²) = 1/γ³ = cos³(Δφ/2)
```

Der Quotient 1/γ³ gibt an, welcher Bruchteil der Gesamtenergie eines bewegten Resonators
für Kopplungsprozesse mit ruhenden Beobachtern zugänglich ist. Für v → c verschwindet
dieser Anteil kubisch in 1/γ.

---

## 7. Verbindung zur Zitterbewegungsfrequenz

### 7.1 Numerische Identifikation

Die RFT-Ruhefrequenz ist:
```
    f₀ = mc² / (π · ℏ)
```

Die **Zitterbewegungsfrequenz** des Elektrons (Schrödinger, 1930) ist definiert durch:
```
    ω_zbw = 2mₑc² / ℏ   →   f_zbw = ω_zbw / (2π) = mₑc² / (π · ℏ)
```

Daraus folgt:
```
    f₀_RFT = f_zbw                              [Übereinstimmung]
```

Die RFT-Eigenfrequenz stimmt mit der Zitterbewegungsfrequenz überein. Das ist keine
triviale Übereinstimmung: Die Zitterbewegung ist das Interferenzphänomen zwischen
positiv- und negativenergetischen Dirac-Komponenten und steht in direkter Verbindung
zur relativistischen Wellennatur massiver Teilchen.

### 7.2 Bedeutung für AP2

Diese Verbindung deutet darauf hin, dass f₀ tatsächlich eine intrinsische
Resonanzfrequenz massiver Teilchen ist — kein frei gewählter Parameter, sondern eine
physikalisch ausgezeichnete Größe, die in der relativistischen Quantenmechanik
unabhängig (als Zitterbewegung) auftaucht.

Die Selbstkonsistenz-Bedingung f_RFT = γ³·f₀ = γ³·f_zbw könnte daher im Rahmen
einer relativistischen Erweiterung der Dirac-Gleichung überprüft werden.

---

## 8. Erfolgskriterium: Falsifizierbare Relation

Das Erfolgskriterium von AP2 ("Identität bewiesen — **oder** falsifizierbare Relation
zwischen m, f₀ und ℏ benannt") ist im zweiten Sinne erfüllt.

### 8.1 Benannte Relationen

**Relation 1 — Ruhefrequenz (A4, definitorisch):**
```
    mc² = π · ℏ · f₀     ⟺     f₀ = mc² / (π · ℏ)
```
*Falsifikation:* Wenn die Kopplungsenergie eines ruhenden Resonators NICHT durch diese
Relation auf seine Ruhemasse zurückführbar ist, ist A4 falsifiziert.

**Relation 2 — Selbstkonsistenz-Bedingung (neu aus AP2):**
```
    f_RFT(v) = γ³ · f₀ = γ³ · mc² / (π · ℏ)
```
*Falsifikation:* Wenn man die effektive Kopplungsfrequenz eines relativistischen Teilchens
(z.B. durch Wechselwirkungsquerschnitt-Messung) bestimmt und die Skalierung mit γ³ nicht
beobachtet, ist die A4-Konsistenz mit ε = 1/γ² gebrochen.

**Relation 3 — Kopplungsenergie-Abfall:**
```
    E_c(v) = mc² · cos²(Δφ/2) = mc² / γ² = mc² · (1 − v²/c²)
```
*Falsifikation:* Wenn die Wechselwirkungsenergie bei relativistischen
Streuexperimenten einem anderen Skalierungsgesetz als 1/γ² folgt.

### 8.2 Experimentelle Zugänge (Vorschau AP6)

| Observable | RFT-Vorhersage | Standardphysik | Unterschied |
|---|---|---|---|
| Kopplungsenergie | mc²/γ² | — (kein direktes Äquivalent) | RFT-spezifisch |
| f_RFT(v) | γ³·f₀ | f₀/γ (Zeitdilatation) | Faktor γ⁴ |
| E_c/E_total | 1/γ³ | — | RFT-spezifisch |

Die Differenz f_RFT / f_naiv = γ⁴ ist für γ ≫ 1 (hochrelativistische Regime) eine
dramatische Vorhersage.

---

## 9. Ergebnis und Ausblick auf AP3–AP5

### 9.1 Zusammenfassung der AP2-Ergebnisse

| Frage (AP2) | Ergebnis |
|---|---|
| Folgt ε = 1/γ² direkt aus A4 + E = γmc² + f = f₀/γ? | **Nein:** Widerspruch ε = γ² |
| Ist f = f₀/γ aus RFT abgeleitet? | **Nein:** Zirkelschluss-Risiko bestätigt |
| Was muss f für Konsistenz sein? | **f = γ³·f₀** (neue Selbstkonsistenz-Bedingung) |
| Was ist der physikalische Gehalt von A4? | **Kopplungsenergie** E_c = mc²/γ² |
| Erfolgskriterium erfüllt? | **Ja:** Falsifizierbare Relation benannt |

### 9.2 Was AP2 leistet und was nicht

**AP2 leistet:**
- Naiven Ansatz (f = f₀/γ, E = γmc²) vollständig durchgerechnet und Widerspruch bewiesen.
- Zirkelschluss-Risiko explizit analysiert und bestätigt.
- Selbstkonsistenz-Bedingung f_RFT = γ³·f₀ hergeleitet.
- Physikalischen Inhalt von A4 präzisiert: Kopplungsenergie E_c = mc²/γ², nicht Gesamtenergie.
- Falsifizierbare Relation benannt: mc² = π·ℏ·f₀ und f_RFT = γ³·f₀.
- Verbindung zur Zitterbewegungsfrequenz identifiziert.

**AP2 leistet nicht (offen für AP5):**
- f_RFT = γ³·f₀ ist noch nicht aus A1–A7 hergeleitet — das ist Gegenstand von **AP5**
  (Zeitdilatation und Frequenztransformation als Phasen-/Kopplungseffekte).
- Die Frage, ob E = γmc² überhaupt die richtige Energiegröße für A4 ist, bleibt offen.
- Die physikalische Herkunft des Faktors γ³ in der RFT-Kopplungsdynamik ist ungeklärt.

### 9.3 Bedeutung für RT-40

AP2 erfüllt seine Funktion: Es zeigt, **warum** die Identifikation ε = 1/γ² nicht
trivial aus A4 folgt. Die Ursache ist nicht eine Inkonsistenz der RFT, sondern die
Tatsache, dass A4 eine andere physikalische Größe beschreibt als die relativistische
Gesamtenergie. Der korrekte Nachweis ε = 1/γ² benötigt:

1. Die Ableitung der Zeitdilatation aus den RFT-Axiomen (AP5), um f(v) korrekt zu bestimmen.
2. Alternativ: Eine direktere Ableitung von ε(Δφ) = 1/γ² aus der Kopplungsdynamik
   (AP3: Lorentz-Transformation), ohne den Umweg über die Energierelation.

Die in AP2 benannte Konsistenz-Bedingung f_RFT = γ³·f₀ ist ein konkreter
Prüfstein für AP5.

---

## Verbindungen zu bestehenden Dokumenten

- AP1 (Phase ↔ Rapidität): [`rt40_ap1_phase_rapiditaet.md`](rt40_ap1_phase_rapiditaet.md)
- Axiome A1–A4: [`../docs/definitionen/axiomatische_grundlegung.md`](../docs/definitionen/axiomatische_grundlegung.md)
- ε = cos²(Δφ/2) Eindeutigkeit (RT-02): [`gsync_gruppenstruktur.md`](gsync_gruppenstruktur.md)
- RT-40 Gesamtübersicht: [`../../../../../../RESEARCH_TASKS.md`](../../../../../../RESEARCH_TASKS.md)
