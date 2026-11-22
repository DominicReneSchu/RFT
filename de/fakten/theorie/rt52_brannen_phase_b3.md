# RT-52 — Brannen-Phasenwinkel θ: Brücke B₃ zur elektroschwachen Skala

*Dominic-René Schu, November 2026*
*Status: 🔄 Offen — AP1 📋 AP2 📋 AP3 📋 AP4 📋*
*Vorgänger: RT-47 (Koide Q=2/3), RT-51 (Yukawa-Matrix), Energiekugel-Dokumente*

---

## Zielsetzung

Die Koide-Formel (RT-47) zeigt, dass die drei Leptonen-Massen auf einem **Kreis im √m-Raum** liegen
(Brannen-Parameterisierung): √m_n = M·(1 + √2·cos(θ + 2π(n-1)/3)).

RT-47 leitet aus A3+A7 ab, **warum** es ein Kreis ist (Q = 2/3). Offen bleibt:
**Welcher Mechanismus bestimmt die Orientierung θ ≈ 132.7323° dieses Kreises?**

---

## Zentrales Ergebnis aus Energiekugel + Resonanzkoordinaten

### Beweis: G_sync allein kann θ nicht fixieren

Aus der Koide-Symmetrie (A3+A7) gilt für ALLE θ:

```
Σ cos(θ + 2π(n-1)/3) = 0   (n = 1,2,3)
```

Das ist eine **exakte algebraische Identität**. Sie besagt: Die Gesamtkopplung der drei Leptonen-Moden
an **jede** Referenzrichtung in der Energiekugel ist null, unabhängig von θ. Damit ist:

> **G_sync-Invarianz allein ist prinzipiell ungeeignet, θ festzulegen.**

Das ist kein quantitatives Argument — es ist ein Strukturbeweis. Jeder Versuch, θ aus A1–A9 abzuleiten,
muss an dieser algebraischen Schranke scheitern, es sei denn, er führt eine **asymmetrische**
Referenzrichtung ein.

### Die notwendige Erweiterung: Brücke B₃

Analog zu:
- **B₁** (RT-41): c als Kopplungswellengeschwindigkeit → SRT
- **B₂** (RT-49): Clifford-Algebra Cl(1,3) → Dirac-Gleichung

wird eine **Brücke B₃** benötigt:

> **B₃ (Entwurf):** Das Higgs-Feld / elektroschwache Vakuum definiert eine ausgezeichnete
> Richtung ê_EW in der Energiekugel. Die Orientierung des Lepton-Kreises relativ zu ê_EW
> bestimmt θ.

---

## Sensititivät: Warum θ durch Massen kaum prüfbar ist

Die Empfindlichkeit von θ gegenüber m_τ:

```
dθ/dm_τ ≈ 0.000497 Grad/MeV
Inverse: dm_τ/dθ ≈ 2013 MeV/Grad
```

Das bedeutet: Eine Änderung von θ um 1° erfordert Δm_τ ≈ 2013 MeV —
weit außerhalb jeder physikalischen Massenmessung. Der Wert θ ≈ 132.73°
ist durch keine einfache algebraische Zahl (√5, π/2 + 3θ_W/2, etc.) exakt
reproduzierbar, ohne m_τ um Tausende von MeV zu verschieben.

**Konsequenz:** θ kann nicht durch Verfeinerung der Koide-Hypothese allein bestimmt werden.
Es braucht ein unabhängiges physikalisches Prinzip.

---

## Die vier Arbeitspakete

### AP1 — Energiekugel als Lepton-Massenraum

**Aufgabe:** Formuliere die Brannen-Parameterisierung als geometrisches Objekt auf der Energiekugel
(aus `de/fakten/docs/mathematik/energiekugel.md`).

1. Die drei Leptonen-Moden sind Punkte auf einem **großen Kreis** der Energiekugel.
2. Der Kreis hat Radius √2·M und Mittelpunkt bei Energie M² (= "Äquator").
3. Die Tangens-Halbwinkel-Parametrisierung (Resonanzkoordinaten) bildet den Kreis auf
   die projektive Gerade ab: t = tan(θ/2), z(t) = e^{iθ} ∈ U(1).
4. **Zu zeigen:** Welche Eigenschaft der Energiekugel beschreibt die LAGE des großen Kreises
   relativ zum Vakuumvektor ê (A5, `energierichtung.md`)?

**Erfolgskriterium:** Kompakte geometrische Formulierung: θ als "Neigungswinkel des Leptonen-Kreises
gegenüber dem Vakuumvektor ê".

---

### AP2 — Higgs-Kopplung als Brücke B₃

**Aufgabe:** Formuliere Brücke B₃: Higgs-Feld als asymmetrische Richtung in der Energiekugel.

1. Das Higgs-Feld hat einen Vakuum-Erwartungswert v ≈ 174 GeV in SU(2)-Raum.
2. In der Energiekugel entspricht der Higgs-VEV einer ausgezeichneten Richtung ê_H.
3. Die Yukawa-Kopplung der Leptonen (y_e, y_μ, y_τ) an das Higgs-Feld projiziert den
   Leptonen-Kreis auf ê_H.
4. Die Projektion ergibt einen charakteristischen Winkel — das ist θ.

**Konkrete Frage:** Ist θ = arccos(ê_Lepton · ê_H) mit ê_H aus dem Higgs-VEV ableitbar?

**Status von B₃:** Minimal notwendige Erweiterung — analog B₁ (c als Kopplungswelle) und B₂ (Cl(1,3)).
Sie ist nicht aus A1–A9 ableitbar, aber durch die Energiekugel-Geometrie strukturell motiviert.

---

### AP3 — Verbindung zur elektroschwachen Skala

**Aufgabe:** Prüfe, ob M (die Koide-Massenskala ≈ 17.7156 MeV^{1/2}) und θ gemeinsam
aus der elektroschwachen Skala folgen.

Die absolute Massenskala: M² ≈ 313.84 MeV. Ist:
```
M² ~ m_e · (m_H / m_e)^α   für ein geeignetes α?
```
oder eine andere Kombination aus Higgs-Masse (125,09 GeV), Fermi-Konstante (G_F), Weinberg-Winkel (θ_W)?

**Falsifikationskriterium RT-52-F1:** Wenn B₃ einen Wert θ_pred liefert, der von θ_PDG
um mehr als 0,001° abweicht (entspricht ~2 MeV in m_τ) → B₃-Formulierung widerlegt.

---

### AP4 — Verbindung zu Neutrino-Massen

**Aufgabe:** Prüfe, ob der gleiche Mechanismus B₃ die Neutrino-Massenhierarchie erklärt.

Für Neutrinos (keine QCD, aber schwache Kopplung via Higgs/Seesaw):
- Koide-Hypothese für Neutrinos: Q_ν = 2/3 (RT-47 Vorhersage)
- Brannen-Phase θ_ν: vermutlich verschieden von θ_lept (verschiedene Higgs-Kopplung)

**Vorhersage (wenn B₃ korrekt):** θ_ν ≠ θ_lept, aber durch denselben B₃-Mechanismus bestimmbar.

---

## Falsifikationskriterien

| Kriterium | Bedingung | Test |
|-----------|-----------|------|
| **RT-52-F1** | θ_pred ≠ θ_PDG bei > 0,001° (wenn B₃ formuliert) | Präzise m_τ-Messung |
| **RT-52-F2** | M² nicht aus EW-Skala ableitbar | Theoretische Analyse |
| **RT-52-F3** | Q_ν ≠ 2/3 bei > 3σ (RT-47 F-Γ4) | KATRIN / Project 8 |

---

## Ehrliche Einschätzung

Die Wahrscheinlichkeit, dass RT-52 B₃ **vollständig** ableitet, ist **gering** —
das ist ein offenes Problem der theoretischen Physik, das im Standardmodell ungelöst ist.

Die Wahrscheinlichkeit, dass RT-52 die **richtige Frage** präzise formuliert und
einen **konsistenten geometrischen Rahmen** (Energiekugel + B₃) liefert, ist **hoch**.

Das wäre kein kleines Ergebnis: Es würde den ersten strukturellen Zusammenhang zwischen
dem RFT-Lepton-Massenraum und der elektroschwachen Skala etablieren.

---

## Kerndokumente

- `de/fakten/docs/mathematik/energiekugel.md` — Geometrie der Energiekugel
- `de/fakten/docs/mathematik/energierichtung.md` — A5: Energie als Vektor
- `de/fakten/docs/mathematik/resonanzkoordinaten.md` — Tangens-Halbwinkel, U(1)
- `de/fakten/theorie/rt47_ap2_koide_formel.md` — Koide Q=2/3 aus A3+A7
- `de/fakten/theorie/rt49_ap1_a5_lorentz_kovariant.md` — A5 Lorentz-kovariant
- `de/fakten/theorie/rt51_ap1_yukawa_matrix.md` — Yukawa-Struktur

---

*RT-52 — DominicReneSchu/RFT — November 2026 (v1.0)*
