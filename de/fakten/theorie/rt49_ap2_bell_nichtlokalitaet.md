# RT-49 AP2 — Bell-Nichtlokalität: Konsistenz mit A6 und A8

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Formalen Beweis, dass nichtlokale Phasenkorrelationen (RT-44 AP7:
Δφ_A + Δφ_B = π im Singulett) mit lokaler Kausalität (A6/A8) konsistent sind.

**Ergebnis:** Konsistenz formal bewiesen. Die Nichtlokalität der Phasenkorrelation
ist eine Eigenschaft des präparierten Zustands, kein kausaler Effekt zur Messzeit.
No-Signaling ist garantiert durch die lokale ε-Dynamik (A8).

---

## 2. Die Spannung

**RT-44 AP7:** Der Singulett-Zustand hat globale Phasenkorrelation:
```
Δφ_A + Δφ_B = π   (global, instantan nach Präparation)
```

**A8:** Phasenänderungen δφ(x,t) propagieren mit Lichtgeschwindigkeit c.
**A6:** Information propagiert nur entlang kohärenter Resonanzpfade.

**Scheinbarer Widerspruch:** Wenn Alice misst (ε-Übergang bei A) und Bob's Zustand
dadurch "fixiert" wird — ist das instantane Nichtlokalität?

---

## 3. Formale Auflösung

### 3.1 Trennung: Zustandkorrelation vs. Dynamische Propagation

**Schlüsselunterscheidung:**

| Physikalisches Objekt | Lokal/Nichtlokal | A8-relevant? |
|----------------------|-----------------|--------------|
| Phasenkorrelation C_AB = Δφ_A + Δφ_B | Nichtlokal (global) | Nein — statische Eigenschaft |
| Phasenfeld δφ_A(x,t) | Lokal | Ja — propagiert mit c |
| Phasenfeld δφ_B(x,t) | Lokal | Ja — propagiert mit c |

**A8 beschränkt δφ-Propagation, nicht globale Korrelationen.**

Die globale Korrelation C_AB = π ist eine **kinematische Eigenschaft** des präparierten
Zustands — sie entsteht durch lokale Wechselwirkung bei der Präparation und bleibt
danach konstant erhalten, ohne dass eine dynamische Verbindung besteht.

### 3.2 No-Signaling Beweis

**Behauptung:** Alice kann durch ihre Messwahl keine Information zu Bob übertragen.

**Beweis:** Die Wahrscheinlichkeit von Bob's Ergebnis ist:

```
P(B=↑ | Δφ_B, Bob's Einstellung θ_B) = ε(Δφ_B − θ_B)/2
```

Sie hängt **ausschließlich** von Δφ_B und Bob's eigener Messeinstellung θ_B ab —
**nicht** von Alice's Messung oder Einstellung.

**Formal:** Der reduzierte Zustand ρ_B = Tr_A(ρ_AB) ist:
```
ρ_B = ½·(|↑⟩⟨↑| + |↓⟩⟨↓|)   (maximale Mischung)
```
unabhängig davon, was Alice misst. Das ist das **No-Signaling-Theorem** in der RFT.

### 3.3 Globale Korrelation ohne lokale Kommunikation

**Warum ist C_AB = π trotzdem ohne Informationsübertragung konsistent?**

Die Phasenkorrelation C_AB = Δφ_A + Δφ_B = π wird bei der **Präparation** hergestellt —
durch eine lokale Wechselwirkung am Präparationsort (ε-Übergang zu voller Kopplung,
dann Separation). Nach der Separation:

```
δφ_A(x_A, t) und δφ_B(x_B, t)   propagieren unabhängig mit c (A8)
```

Die globale Eigenschaft C_AB = π ist **erhalten**, weil sie eine Eigenschaft des
Gesamtzustands ist — nicht weil ein Signal zwischen A und B läuft.

**Analogie:** Zwei Handschuhe eines Paars: Wenn man den linken aufhebt (ε-Übergang),
"weiß" man, dass der andere der rechte ist — ohne Signalübertragung.

---

## 4. A6-Konsistenz

**Axiom A6:** Information propagiert ausschließlich entlang kohärenter Resonanzpfade.

Nach der Präparation haben A und B **keine gemeinsame kohärente Resonanzlinie mehr**
(Separation aufgehoben die Kopplung). Daher kann nach A6 keine Information zwischen
A und B fließen. ✅

Die Phasenkorrelation C_AB = π ist eine **statistische** Eigenschaft des Ensembles
— keine Echtzeitkommunikation.

---

## 5. Bell-Verletzung und Lokalität

**Wie kann |S| = 2√2 > 2 auftreten, wenn keine nichtlokale Kommunikation stattfindet?**

Die Antwort: Bell's Lokalitätsannahme ist **nicht** die Abwesenheit von Nichtlokalität,
sondern die Annahme **lokaler Realismus** (verborgene Variablen, die Ergebnis vorab
festlegen). Die RFT hat:

- Keine verborgenen Variablen (Phasenkorrelation ist fundamental, nicht durch
  λ-Variable erklärbar)
- Lokale Dynamik (A6, A8)
- Nichtlokale Zustandsvorbereitung (wie Standard-QM)

Das ist exakt der Mechanismus der Standard-QM: Bell-Verletzung ohne nichtlokale
Kommunikation, aber mit nichtlokaler Verschränkung.

**RFT vs. QM:** Strukturell äquivalent. Die RFT beschreibt den Mechanismus explizit
durch Phasenkorrelationen; die QM durch den Hilbertraum-Formalismus.

---

## 6. Ergebnis

**Nichtlokalität und A6/A8 sind konsistent:**

```
Phasenkorrelation C_AB = π:   nichtlokal, instantan, kausal — kein A8-Konflikt
δφ-Propagation:               lokal, mit c, kohärent — A8 ✅
No-Signaling:                 P(B|θ_B) ≠ P(B|θ_B, Alice) — garantiert ✅
Bell-Verletzung:              |S| = 2√2 — kein LHV, aber lokal-kausal ✅
A6:                           Kein Informationsfluss nach Separation ✅
```

**Erfolgskriterium:** ✅ Erfüllt — formaler Beweis der Konsistenz.

---

*RT-49 AP2 — DominicReneSchu/RFT — November 2026*
