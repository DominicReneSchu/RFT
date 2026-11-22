# RT-52 AP1 — Energiekugel-Geometrie: Leptonen-Kreis und Phasenwinkel θ

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## Zielsetzung

Formuliere die Brannen-Parameterisierung als geometrisches Objekt auf der Energiekugel.
Identifiziere θ als "Neigungswinkel des Leptonen-Kreises gegenüber dem Vakuumvektor ê".

---

## 1. Die Brannen-Parameterisierung als Energiekugel-Objekt

Die Leptonen-Massen liegen auf einem **großen Kreis** im √m-Raum (RT-47 AP2):

```
√m_n = M · (1 + √2 · cos(θ + 2π(n-1)/3)),   n = 0,1,2 (e,μ,τ)
```

Auf der Energiekugel (Energiekugel-Dokument):
- Der große Kreis hat **Radius √2·M** und **Mittelpunkt bei E = M²** (Äquator der Kugel)
- Die drei Punkte sind im Phasenraum um 2π/3 gleichmäßig verteilt (Koide-Symmetrie, A3+A7)
- **θ** ist der Azimutwinkel des Elektronpunktes auf diesem Kreis

---

## 2. Tangens-Halbwinkel-Parametrisierung (Resonanzkoordinaten)

Aus `resonanzkoordinaten.md`: t = tan(θ/2) bildet den Kreis auf die projektive Gerade ab:

```
cos(θ) = (1-t²)/(1+t²) = (√m_e/M - 1)/√2 = -0.678574
t = tan(θ/2) = 2.285230
θ = 132.7323°
```

Die z(t)-Darstellung auf dem Einheitskreis (U(1)-Resonanz):
```
z(t) = (1 + it)/(1 - it) = e^{iθ} = -0.6786 + 0.7345i
```

---

## 3. Beweis: G_sync kann θ nicht fixieren

**Zentrales algebraisches Ergebnis (aus RT-52 Kerndokument):**

$$\sum_{n=0}^{2} \cos\!\left(\theta + \frac{2\pi n}{3}\right) = 0 \quad \text{für alle } \theta$$

Beweis:
```
Σ cos(θ + 2πn/3) 
= Re(e^{iθ} · Σ e^{2πin/3})
= Re(e^{iθ} · 0)   [da Σ e^{2πin/3} = 0, kubische Einheitswurzeln]
= 0  ✅
```

Das ist eine **exakte algebraische Identität** — kein Näherungsresultat.
Sie gilt für ALLE θ, unabhängig von Massen oder Kopplungen.

**Konsequenz:** Der Vakuumvektor ê in der Energiekugel "sieht" alle drei Leptonen-Moden
summiert immer zu null — ê kann daher die Orientierung θ nicht fixieren.

---

## 4. Yukawa-Raum: Identische θ-Struktur

Die Yukawa-Kopplungen y_n = √2·m_n/v definieren einen analogen Kreis in y-Raum:

```
√y_e = 0.002037,  √y_μ = 0.029296,  √y_τ = 0.120139
```

Brannen-Phase im Yukawa-Raum: θ_Y = 132.7323° ← **identisch mit θ_m** ✅

Das zeigt: θ ist eine fundamentale Eigenschaft der Lepton-Yukawa-Struktur —
kein Artefakt der Masseneinheiten.

---

## 5. Die Neigung des Leptonen-Kreises in der Energiekugel

**Geometrische Interpretation:**
- Der Leptonen-Kreis auf der Energiekugel ist um θ gegenüber der "Nullmeridian" geneigt
- Die Nullmeridian entspricht ê_0 (willkürliche Referenz ohne physikalische Auszeichnung)
- Eine **physikalische Auszeichnung** braucht ê_B₃ — einen bevorzugten Richtungsvektor

Das ist der geometrisch präzise Inhalt der Brücke B₃ (AP2–AP4):
> B₃ liefert ê_B₃ = physikalisch ausgezeichnete Richtung in der Energiekugel.

**Erfolgskriterium:** ✅ Erfüllt — θ als Neigungswinkel des Leptonen-Kreises
geometrisch identifiziert; Beweis G_sync ungenügend vollständig.

---

*RT-52 AP1 — DominicReneSchu/RFT — November 2026*
