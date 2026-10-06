# RT-42 AP1 — Formale Analogie: Phase ↔ Skalenfaktor

*Dominic-René Schu, September 2026*
*Status: ✅ Abgeschlossen (Sep 2026)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Homogenisierung des RFT-Feldes](#2-homogenisierung-des-rft-feldes)
3. [Verhalten von Δφ unter Expansion](#3-verhalten-von-δφ-unter-expansion)
4. [Kopplungseffizienz als effektive kosmologische Dichte](#4-kopplungseffizienz-als-effektive-kosmologische-dichte)
5. [Friedmann-Analogie ohne Λ-Term](#5-friedmann-analogie-ohne-λ-term)
6. [Explizite Abbildung Δφ(t) → a(t)](#6-explizite-abbildung-δφt--at)
7. [Prüfung des Erfolgskriteriums](#7-prüfung-des-erfolgskriteriums)
8. [Ergebnis und Ausblick auf AP2–AP7](#8-ergebnis-und-ausblick-auf-ap2ap7)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-42 AP1):** Prüfen, ob die RFT-Phasendifferenz Δφ(t) als dynamische
Variable fungiert, die den kosmischen Skalenfaktor a(t) steuert.

**Erfolgskriterium:** Konstruktion einer expliziten Abbildung
```
    Δφ(t) → a(t)
```
oder formaler Nachweis ihrer Nichtexistenz.

**Ergebnis:** Das Erfolgskriterium ist erfüllt. Die Abbildung
```
    a(t) = a₀ · ε(Δφ(t))^(−1/3)  mit  ε(Δφ) = cos²(Δφ/2)
```
liefert eine konsistente Friedmann-artige Gleichung ohne separaten Λ-Term.
Die Abbildung ist bijektiv auf dem physikalisch relevanten Bereich Δφ ∈ [0, π/2).

---

## 2. Homogenisierung des RFT-Feldes

### 2.1 Ausgangslage

Die Resonanzfeldtheorie beschreibt ein Feld von Phasendifferenzen Δφ(x⃗, t) zwischen
Resonatoren. Im allgemeinen Fall hängt Δφ sowohl von Ort als auch von der Zeit ab.

Für die Kosmologie (homogene, isotrope Näherung) verlangen wir:

**Kosmologisches Prinzip auf RFT-Ebene:**
```
    Δφ(x⃗, t) → Δφ(t)    (räumlich homogen, isotrop)
```

Dies ist das RFT-Analogon zur FLRW-Annahme in der Standardkosmologie.

### 2.2 Begründung aus A1–A8

Axiom A1 (Universelle Schwingung) postuliert Felder ψ_i(x⃗, t) = A_i · cos(ω_i·t − k_i·x⃗ + φ_i).
Im kosmologischen Grenzfall verschwindet die räumliche Inhomogenität auf Skalen ≫ l_c:

```
    k_i · x⃗  →  k_i · |x⃗|  →  konstant    für  |x⃗| ≫ l_c
```

Damit reduziert sich Δφ(x⃗, t) auf eine globale Phasendifferenz Δφ(t), die nur noch
von der kosmischen Zeit t abhängt.

Axiom A8 (Kopplungswellengeschwindigkeit, RT-41) legt c = 1/√(μ₀ε₀) fest: Änderungen
von Δφ propagieren mit Lichtgeschwindigkeit. Im homogenen Grenzfall ist diese
Propagation kausaler Hintergrund, nicht dynamischer Freiheitsgrad.

---

## 3. Verhalten von Δφ unter Expansion

### 3.1 Kopplungsdynamik

Die Kopplungsdynamik (gegeben in der Ausgangslage von RT-42) lautet:
```
    dK_ij/dt = α·G·cos(Δφ) − β·K_ij
```

Im homogenen, sich langsam ändernden Grenzfall (adiabatische Näherung):
```
    K_ij  →  K(t)  =  (α·G/β) · cos(Δφ(t))
```

### 3.2 Expansionsabhängigkeit

Wenn das Universum expandiert, wächst der Abstand zwischen Resonatoren:
```
    l(t) = a(t) · l₀
```

Die Wellenzahl skaliert invers mit dem Skalenfaktor (Rotverschiebung):
```
    k(t) = k₀ / a(t)
```

Die Phasendifferenz zwischen zwei Resonatoren im Abstand l(t) ist
```
    Δφ(t) = k(t) · l(t) = k₀ · l₀ = const    (adiabatisch ohne Quellen)
```

Dies beschreibt den **statischen** Fall (kein Phasenantrieb). Für eine expandierende
Lösung muss eine Zeitabhängigkeit von Δφ eingeführt werden — entweder durch eine
externe Phasenquelle oder durch die Kopplungsrückkopplung selbst.

### 3.3 Aktive Phasendynamik

Wir parametrisieren die kosmologische Phasendynamik durch:
```
    Δφ(t) = Δφ₀ + δφ(t)
```

wobei δφ(t) die zeitliche Abweichung vom Gleichgewichtswert Δφ₀ beschreibt.

Eine monoton wachsende Phase Δφ(t) ∈ [0, π/2) entspricht einer Verringerung der
Kopplungseffizienz ε und damit einer kosmologischen Expansion (siehe Abschnitt 6).

---

## 4. Kopplungseffizienz als effektive kosmologische Dichte

### 4.1 Definition

Die Kopplungseffizienz aus A4:
```
    ε(t) = cos²(Δφ(t)/2)    ∈ (0, 1]
```

Wir identifizieren ε mit dem normierten kosmologischen Dichteanteil:
```
    ε(t)  ↔  ρ(t)/ρ_c(t)    =  Ω(t)
```

Hier ist ρ_c = 3H²/(8πG) die kritische Dichte und Ω der dimensionslose Dichteparameter.

### 4.2 Grenzfälle

| Δφ | ε(Δφ) | kosmologische Interpretation |
|----|--------|------------------------------|
| 0  | 1      | maximale Kopplung, Gleichgewichtszustand (flache Raumzeit) |
| π/4 | 1/2 + √2/4 ≈ 0,854 | moderates Universum |
| π/3 | 3/4  | Materiedominanz-Analogon |
| π/2 | 1/2  | kritisches Universum (Ω = 1/2) |
| → π | → 0 | vollständiger Kopplungsverlust — kosmologische Singularität |

### 4.3 Begründung

Diese Identifikation ist motiviert durch:
- RT-33: Zustandsgleichung w(θ) = (1/3)[2ε(Δφ(θ)) − 1]; für ε = 1/2 ergibt sich w = −1/3
- RT-40 AP5: ε = 1/γ² — Kopplungseffizienz trägt Energie- und Dichteinformation
- RT-34: ρ_RFT ≥ 0 für alle Δφ — keine negative Energiedichte

---

## 5. Friedmann-Analogie ohne Λ-Term

### 5.1 RFT-Energiedichte

Wir definieren die RFT-Materiedichte:
```
    ρ_RFT(t) = ρ_c · ε(t) = ρ_c · cos²(Δφ(t)/2)
```

### 5.2 Modifizierte Friedmann-Gleichung

Einsetzen in die Standard-Friedmann-Gleichung (k = 0, flaches Universum):
```
    H²(t) = (8πG/3) · ρ_RFT(t)
           = (8πG/3) · ρ_c · cos²(Δφ(t)/2)
           = H₀² · cos²(Δφ(t)/2)
```

Damit gilt:
```
    H(t) = H₀ · |cos(Δφ(t)/2)|
```

Dies ist eine **Friedmann-artige Gleichung ohne separaten Λ-Term**: Der Hubble-Parameter
H(t) ist vollständig durch die Phase Δφ(t) bestimmt.

### 5.3 Vergleich mit ΛCDM

| Größe | ΛCDM | RFT-Kosmologie (AP1) |
|-------|------|----------------------|
| H(t) | √(Ω_m a⁻³ + Ω_Λ) · H₀ | H₀ · cos(Δφ/2) |
| Dunkle Energie | Ω_Λ ≈ 0,68 | entfällt — in Phasendynamik enthalten |
| Ω gesamt | = 1 (beobachtet) | ε(Δφ) parametrisiert Ω |
| w | −1 (Λ) | w(Δφ) = (1/3)[2ε − 1] ∈ [−1/3, +1/3] |

**Wichtige Einschränkung:** Der Wertebereich der Zustandsgleichung
w ∈ [−1/3, +1/3] aus RT-33 reicht nicht bis w = −1 (ΛCDM-Wert).
Für exakte Übereinstimmung mit dem beobachteten Wert w ≈ −1 ist AP3 erforderlich
(Erweiterung um eine dynamische Phasenquelle oder Kopplungsterm).

---

## 6. Explizite Abbildung Δφ(t) → a(t)

### 6.1 Herleitung

Der Hubble-Parameter ist definiert als:
```
    H = ȧ/a
```

Aus der RFT-Friedmann-Gleichung (Abschnitt 5.2):
```
    ȧ/a = H₀ · cos(Δφ(t)/2)
```

Sei Δφ(t) eine monoton wachsende Funktion. Wir wählen das Ansatz:
```
    Δφ(t) = 2 · arccos(e^{−H₀·t})    (für t > 0)
```

Dann gilt:
```
    cos(Δφ(t)/2) = e^{−H₀·t}
    ε(t) = e^{−2H₀·t}
```

Einsetzen:
```
    ȧ/a = H₀ · e^{−H₀·t}
    a(t) = a₀ · exp(1 − e^{−H₀·t})
```

Für kleine Zeiten t ≪ H₀⁻¹:
```
    a(t) ≈ a₀ · exp(H₀·t) = a₀ · e^{H₀·t}    (de-Sitter-artige Expansion)
```

Für große Zeiten t ≫ H₀⁻¹:
```
    a(t) → a₀ · e    (konvergiert zu einem endlichen Wert)
```

### 6.2 Alternative Parametrisierung

Eine allgemeinere Abbildung mit Zeitkonstante τ:
```
    cos(Δφ(t)/2) = (1 + t/τ)^{−n}    mit  n > 0
```

ergibt:
```
    ȧ/a = H₀ · (1 + t/τ)^{−n}
    a(t) = a₀ · exp(H₀·τ/(n−1) · [1 − (1 + t/τ)^{1−n}])    für n ≠ 1
```

Für n = 1:
```
    a(t) = a₀ · (1 + t/τ)^{H₀·τ}    (Potenzgesetz-Expansion)
```

Diese Parametrisierung umfasst Materiedominanz (n = 3/2) und Strahlungsdominanz (n = 2)
als Spezialfälle.

### 6.3 Bijektivität

Auf dem physikalisch relevanten Bereich Δφ ∈ [0, π/2) ist:
- cos(Δφ/2) strikt monoton fallend: [1, 1/√2)
- ε(Δφ) = cos²(Δφ/2) strikt monoton fallend: [1, 1/2)
- Die Abbildung Δφ ↦ a ist bijektiv (gegeben eine monotone Phase Δφ(t))

Damit ist die Abbildung Δφ(t) → a(t) eindeutig und invertierbar:
```
    Δφ(t) = 2 · arccos(√ε(t)) = 2 · arccos(√(ρ(t)/ρ_c(t)))
```

---

## 7. Prüfung des Erfolgskriteriums

**Erfolgskriterium:** Explizite Abbildung Δφ(t) → a(t) — oder Nachweis ihrer
Nichtexistenz.

**Bewertung:**

✅ **Abbildung konstruiert.** Die explizite Abbildung
```
    H(t) = H₀ · cos(Δφ(t)/2)
    a(t) = a₀ · exp(∫₀ᵗ H₀·cos(Δφ(s)/2) ds)
```
ist wohldefiniert, bijektiv (für monotones Δφ) und liefert eine Friedmann-artige
Gleichung ohne separaten Λ-Term.

✅ **Physikalisch konsistent.** Aus RT-34: ρ_RFT ≥ 0 für alle Δφ — keine negative
Energie. Aus RT-33: Zustandsgleichung w ∈ [−1/3, +1/3].

⚠️ **Offene Einschränkung:** Der Bereich w ∈ [−1/3, +1/3] deckt w = −1 (ΛCDM) nicht
ab. Für eine vollständige Dunkle-Energie-Analogie ist eine Erweiterung über AP3 nötig.

✅ **Erfolgskriterium erfüllt** (mit dokumentierter Einschränkung).

---

## 8. Ergebnis und Ausblick auf AP2–AP7

**Zentrales Ergebnis von AP1:**

Die RFT-Phasendifferenz Δφ(t) fungiert als dynamische Variable des kosmischen
Skalenfaktors a(t) über die Beziehung:
```
    H(t) = H₀ · cos(Δφ(t)/2)
    ε(t) = cos²(Δφ(t)/2)  ↔  Ω(t) = ρ(t)/ρ_c(t)
```

Die Friedmann-artige Gleichung
```
    H² = H₀² · ε(Δφ)  =  (8πG/3) · ρ_c · ε(Δφ)
```
kommt ohne separaten Λ-Term aus, sofern die Phasendynamik Δφ(t) physikalisch
hergeleitet werden kann (→ AP2).

**Ausblick:**

- **AP2:** Herleitung von Δφ̇(t) aus der Kopplungsdynamik — liefert die
  Bewegungsgleichung für ε(t) und damit H(t)
- **AP3:** Prüfung, ob der RFT-Zustandsparameter w auf −1 erweitert werden kann
  (Dunkle-Energie-Analogon)
- **AP4:** Kosmologische Einordnung der 28-Größenordnungen-Diskrepanz
  (ρ_Λ vs. Warp-Energiedichte)
- **AP5:** Falsifizierbare Abweichungen vom ΛCDM-Modell
- **AP6:** Kosmische Expansion als globaler Phaseneffekt
- **AP7:** Konsistenzprüfung mit RT-33, RT-40 und RT-41

**Verbindung zu bestehenden Ergebnissen:**
- RT-40 AP1: Phase ↔ Rapidität (hyperbolische Geometrie); hier: Phase ↔ Skalenfaktor (kosmische Geometrie)
- RT-33: w(θ) = (1/3)[2ε − 1] — direkt verwendet in Abschnitt 5.3
- RT-34: ρ_RFT ≥ 0 — fundiert positive Energiedichte in Abschnitt 4.3
- RT-41 (A8): c als Kopplungswellengeschwindigkeit — fundiert die kausale Struktur in Abschnitt 2.2

---

*RT-42 AP1 — DominicReneSchu/RFT — September 2026*
