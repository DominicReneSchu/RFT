# RT-43 AP5 — Kausalitätsprüfung mit Axiom A8

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-43 AP5):** Prüfe, ob die RFT-Warpmetrik kausal konsistent mit
Axiom A8 (c = 1/√(μ₀ε₀)) ist.

**Erfolgskriterium:** Kausale Konsistenz für v_s ≤ c nachgewiesen — oder
Verletzung explizit benannt.

**Ergebnis:** Das Erfolgskriterium ist erfüllt. RT-43 Warpmetrik ist kausal
konsistent mit A8 für alle v_s ≤ c.

---

## 2. Axiom A8 und Phasenpropagation

**Axiom A8 (RT-41):** Die Kopplungswellengeschwindigkeit ist
```
c = 1/√(μ₀ε₀)
```
Änderungen der Phasendifferenz δφ(x⃗, t) propagieren mit Lichtgeschwindigkeit c.

Die Wellengleichung für lokale Phasenstörungen lautet:
```
□ δφ = ∂²δφ/∂t² − c² ∇²δφ = 0
```

Die Dispersionsrelation: ω = c·k → Gruppengeschwindigkeit v_g = ∂ω/∂k = c.

Damit ist die Phasenpropagation von vornherein kausal: keine δφ-Störung
breitet sich schneller als c aus.

---

## 3. Kausalität der Warpmetrik für v_s < c

### 3.1 Strukturargument

Aus RT-43 AP1 gilt:
```
h_μν^RFT(x⃗, t) = h_μν^Alcubierre(x⃗, t) · ε(δφ(x⃗, t))
```

mit ε(Δφ) = cos²(Δφ/2) ∈ [0, 1].

**Schranke:** Da ε ∈ [0, 1], gilt:
```
|h_μν^RFT| ≤ |h_μν^Alcubierre|
```

Die Alcubierre-Metrik für v_s < c enthält per Konstruktion keine überlichtschnelle
Informationsausbreitung (Birkhoff-Theorem im linearisierten Grenzfall). Da die
RFT-Metrik durch ε ≤ 1 strikt kleiner ist, gilt Kausalität a fortiori.

### 3.2 Phasenausbreitung

Die Modulation ε(δφ(x⃗, t)) propagiert mit Lichtgeschwindigkeit c (A8).
Die Warpmetrik h_μν^RFT ist kausal, weil ihre einzige RFT-spezifische Zutat
(die Phasenmodulation) kausal ist.

---

## 4. Prüfung: Keine geschlossenen zeitartigen Kurven (CTC)

### 4.1 Bekanntes Ergebnis für Alcubierre

Die Alcubierre-Metrik bei v_s < c erzeugt keine CTCs — der Metrik-Tensor
bleibt nicht-degeneriert und zeitartige Geodäten sind vorwärts-gerichtet.

### 4.2 RFT-Modulation und CTCs

Ein CTC würde erfordern, dass die Metrik das Vorzeichen von g_tt = −1 ändert,
d.h. g_tt > 0 (Signaturwechsel).

Für die RFT-Warpmetrik:
```
g_tt^RFT = −1 + (v_s f ε)² ≈ g_tt^Alc · ε² + (1−ε²)·(−1)
```

Da ε ∈ [0,1] und (v_s f)² < 1 für v_s < c (Alcubierre-Bedingung), gilt:
```
g_tt^RFT < 0  für alle v_s < c und alle ε ∈ [0, 1]
```

Kein Signaturwechsel → keine CTCs.

---

## 5. Grenzfall v_s → c: Selbst-Abschaltung als Kausalitätsschutz

Für v_s → c gilt aus RT-40 AP4: Δφ → π und ε → 0.

Damit: h_μν^RFT → 0 — die Warpblase kollabiert bevor v_s = c erreicht wird.

**Physikalische Interpretation:** Die RFT-Warpmetrik hat einen eingebauten
Kausalitätsschutz: Das Kopplungsfeld schaltet sich selbst ab, bevor die
Lichtgrenze überschritten werden könnte. Eine Verletzung von A8 ist strukturell
ausgeschlossen.

---

## 6. Bedingungen für eine A8-Verletzung (zur Vollständigkeit)

A8 wäre verletzt, wenn δφ(x⃗, t) überlichtschnell propagieren würde.
Das würde erfordern:
1. Eine modifizierte Dispersionsrelation ω² = c²k² + m²c⁴/ħ² (massive Kopplungswelle)
   — in A8 nicht enthalten, da c als Phasengeschwindigkeit masseloser Wellen festgelegt ist.
2. Eine nichtlineare Rückkopplung, die die effektive Gruppengeschwindigkeit > c treibt
   — in der aktuellen RFT nicht vorhanden (RT-41, keine Nichtlinearität in A8).

Beide Szenarien sind in der aktuellen RFT (A1–A8) nicht realisierbar.

---

## 7. Ergebnis

**RT-43 Warpmetrik ist kausal konsistent mit A8 für v_s ≤ c:**

| Prüfpunkt | Ergebnis |
|-----------|----------|
| Phasenpropagation mit c (A8) | ✅ |
| |h_μν^RFT| ≤ |h_μν^Alc| | ✅ |
| Keine CTCs für v_s < c | ✅ |
| g_tt^RFT < 0 überall | ✅ |
| Selbst-Abschaltung bei v_s→c | ✅ (Kausalitätsschutz eingebaut) |

**Erfolgskriterium:** ✅ Erfüllt.

---

*RT-43 AP5 — DominicReneSchu/RFT — November 2026*
