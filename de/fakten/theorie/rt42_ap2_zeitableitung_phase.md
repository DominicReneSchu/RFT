# RT-42 AP2 — Zeitableitung der Phase

*Dominic-René Schu, September 2026*
*Status: ✅ Abgeschlossen (Sep 2026)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Kopplungsdynamik und Ausgangslage](#2-kopplungsdynamik-und-ausgangslage)
3. [Ableitung der Differentialgleichung für Δφ(t)](#3-ableitung-der-differentialgleichung-für-δφt)
4. [Identifikation mit der Expansionsrate H](#4-identifikation-mit-der-expansionsrate-h)
5. [Stationäre und dynamische Lösungen](#5-stationäre-und-dynamische-lösungen)
6. [Konsistenz mit A8 — Phasendynamik und Lichtgeschwindigkeit](#6-konsistenz-mit-a8--phasendynamik-und-lichtgeschwindigkeit)
7. [Prüfung des Erfolgskriteriums](#7-prüfung-des-erfolgskriteriums)
8. [Ergebnis und Ausblick auf AP3–AP7](#8-ergebnis-und-ausblick-auf-ap3ap7)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-42 AP2):** Bestimme Δφ̇(t) aus der Kopplungsdynamik und interpretiere
es als Expansionsrate.

**Erfolgskriterium:** Geschlossene Differentialgleichung für Δφ(t), vergleichbar mit
Friedmann-Lösungen.

**Ergebnis:** Das Erfolgskriterium ist erfüllt. Die Differentialgleichung
```
    Δφ̇ = β · tan(Δφ/2)
```
ist eine geschlossene, analytisch lösbare ODE für Δφ(t). Die Lösung liefert eine
Friedmann-vergleichbare Expansionsdynamik:
```
    ε(t) = 1 − sin²(Δφ₀/2) · e^{βt}
    H(t) = H₀ · √ε(t)
```
Der Hubble-Parameter H(t) folgt direkt aus der Phasendynamik, ohne separaten Λ-Term.

---

## 2. Kopplungsdynamik und Ausgangslage

### 2.1 Homogenes Feld (RT-42 Ausgangslage)

Im kosmologischen Grenzfall (AP1: räumlich homogene Phase Δφ(t)) lautet die
Kopplungsdynamik:
```
    dK/dt = α · G · cos(Δφ) − β · K
```

| Symbol | Bedeutung |
|--------|-----------|
| K      | Kopplungsstärke zwischen Resonatoren |
| α      | Wachstumsrate der Kopplung |
| G      | G_sync-Kopplungskonstante (Axiom A5) |
| β      | Dissipationsrate (β > 0) |
| Δφ(t)  | Globale Phasendifferenz (AP1) |

### 2.2 Adiabatische Bedingung und K₀

Im adiabatischen Gleichgewicht (dK/dt = 0) gilt:
```
    K_stat = (α·G/β) · cos(Δφ)
```

Wir parametrisieren die Kopplungsstärke konsistent mit A4:
```
    K(t) = K₀ · ε(Δφ(t))  =  K₀ · cos²(Δφ(t)/2)
```

Da in der Gleichgewichtslösung K_stat ∝ cos(Δφ) und K ∝ cos²(Δφ/2) = (1 + cos Δφ)/2
denselben qualitativen Verlauf aufweisen, identifizieren wir:
```
    K₀ = α·G/β
```

Diese Wahl ist konsistent: Für Δφ = 0 gilt K = K₀ = αG/β = K_stat (maximale Kopplung).

---

## 3. Ableitung der Differentialgleichung für Δφ(t)

### 3.1 Differenziation der Kopplungsparametrisierung

Wir differenzieren K(t) = K₀ cos²(Δφ(t)/2) nach der Zeit:
```
    dK/dt = K₀ · d/dt[cos²(Δφ/2)]
           = K₀ · 2cos(Δφ/2) · (−sin(Δφ/2)) · (Δφ̇/2)
           = −(K₀/2) · sin(Δφ) · Δφ̇
```

### 3.2 Gleichsetzen mit der Kopplungsgleichung

Einsetzen in dK/dt = αG cos(Δφ) − βK:
```
    −(K₀/2) · sin(Δφ) · Δφ̇  =  α·G · cos(Δφ) − β·K₀·cos²(Δφ/2)
```

Mit K₀ = αG/β:
```
    −(αG/2β) · sin(Δφ) · Δφ̇  =  αG · cos(Δφ) − αG · cos²(Δφ/2)
```

Division durch αG:
```
    −(1/2β) · sin(Δφ) · Δφ̇  =  cos(Δφ) − cos²(Δφ/2)
```

### 3.3 Trigonometrische Vereinfachung

Mit der Identität cos(Δφ) = 2cos²(Δφ/2) − 1:
```
    cos(Δφ) − cos²(Δφ/2)  =  [2cos²(Δφ/2) − 1] − cos²(Δφ/2)
                            =  cos²(Δφ/2) − 1
                            =  −sin²(Δφ/2)
```

Damit:
```
    −(1/2β) · sin(Δφ) · Δφ̇  =  −sin²(Δφ/2)
```

### 3.4 Geschlossene ODE für Δφ(t)

Umformen mit sin(Δφ) = 2sin(Δφ/2)cos(Δφ/2):
```
    (1/2β) · 2sin(Δφ/2)cos(Δφ/2) · Δφ̇  =  sin²(Δφ/2)
    (1/β) · sin(Δφ/2)cos(Δφ/2) · Δφ̇  =  sin²(Δφ/2)
```

Division durch sin(Δφ/2) (gültig für Δφ ≠ 0, 2π):
```
    (1/β) · cos(Δφ/2) · Δφ̇  =  sin(Δφ/2)
```

**Geschlossene ODE:**
```
    Δφ̇ = β · tan(Δφ/2)
```

Dies ist das zentrale Ergebnis von AP2: eine autonome, nichtlineare ODE erster Ordnung
für die kosmologische Phasendifferenz Δφ(t), die vollständig aus der RFT-
Kopplungsdynamik hervorgeht.

---

## 4. Identifikation mit der Expansionsrate H

### 4.1 Direkte Identifikation Δφ̇ ≠ H

Aus AP1 gilt: H(t) = H₀ · cos(Δφ/2)

Aus AP2: Δφ̇ = β · tan(Δφ/2) = β · sin(Δφ/2)/cos(Δφ/2)

Das Verhältnis:
```
    Δφ̇ / H = (β · sin(Δφ/2)/cos(Δφ/2)) / (H₀ · cos(Δφ/2))
            = (β/H₀) · sin(Δφ/2)/cos²(Δφ/2)
```

hängt explizit von Δφ ab und ist nicht konstant. **Eine direkte Identifikation
Δφ̇ = H ist daher nicht möglich** (außer in trivialen Spezialfällen).

### 4.2 Indirekte Beziehung über ε̇

Die physikalisch relevante Verbindung geht über die Kopplungseffizienz ε = cos²(Δφ/2):
```
    ε̇ = d/dt[cos²(Δφ/2)] = −sin(Δφ/2)cos(Δφ/2) · Δφ̇
       = −sin(Δφ/2)cos(Δφ/2) · β · tan(Δφ/2)
       = −β · sin²(Δφ/2)
       = −β · (1 − ε)
```

Die Gleichung
```
    ε̇ = −β (1 − ε)
```
ist das Friedmann-Analogon: Sie beschreibt, wie die Kopplungseffizienz ε (und damit
die kosmologische Dichte Ω = ε aus AP1) mit der Rate β abnimmt.

### 4.3 Modifizierte Raychaudhuri-Gleichung

Aus H = H₀√ε folgt Ḣ durch Differentiation:
```
    Ḣ = H₀ · ε̇ / (2√ε)  =  H₀ · (−β(1−ε)) / (2√ε)
```

Mit H = H₀√ε → √ε = H/H₀:
```
    Ḣ = −(βH₀²/2) · (1−ε) / H
```

Da H² = H₀²ε und damit ε = H²/H₀²:
```
    Ḣ = −(β/2) · (H₀² − H²) / H
```

**Modifizierte RFT-Raychaudhuri-Gleichung:**
```
    Ḣ = −(β/2) · (H₀² − H²) / H
```

Vergleich mit der Standard-Raychaudhuri-Gleichung: Ḣ = −4πG(ρ + p)

Identifikation:
```
    4πG(ρ + p)  =  (β/2)(H₀² − H²)/H
```

Dies zeigt, dass der Dissipationsparameter β die effektive Zustandsgleichung (ρ + p)
der RFT-Kosmologie steuert.

---

## 5. Stationäre und dynamische Lösungen

### 5.1 Stationäre Lösung (Δφ̇ = 0)

Aus Δφ̇ = β tan(Δφ/2) = 0 folgt:
```
    tan(Δφ/2) = 0  →  Δφ = 0  (mod 2π)
```

| Δφ | ε | H | Interpretation |
|----|---|---|----------------|
| 0  | 1 | H₀ | Maximale Kopplung — statisches de-Sitter-artiges Universum |
| π  | 0 | 0  | Vollständiger Kopplungsverlust — instabiler Fixpunkt (nicht physikalisch erreichbar) |

Der Fixpunkt Δφ = 0 entspricht einem statischen Universum mit maximaler Kopplungseffizienz.
Jede infinitesimale Störung Δφ > 0 treibt das System in die Expansion (Δφ̇ > 0 für β > 0).

### 5.2 Analytische Lösung der ODE

Die ODE Δφ̇ = β tan(Δφ/2) ist trennbar:
```
    dΔφ / tan(Δφ/2) = β · dt
    (cos(Δφ/2)/sin(Δφ/2)) · dΔφ = β · dt
```

Substitution u = sin(Δφ/2), du = (cos(Δφ/2)/2) dΔφ:
```
    2 du/u = β dt
    2 ln|u| = βt + C
    sin(Δφ(t)/2) = sin(Δφ₀/2) · e^{βt/2}
```

**Allgemeine Lösung:**
```
    Δφ(t) = 2 · arcsin(sin(Δφ₀/2) · e^{βt/2})
```

Gültig für t ∈ [0, t_max) mit:
```
    t_max = (2/β) · ln(1 / sin(Δφ₀/2))
```

### 5.3 Darstellung über Kopplungseffizienz

Da ε = cos²(Δφ/2) = 1 − sin²(Δφ/2):
```
    ε(t) = 1 − sin²(Δφ₀/2) · e^{βt}
```

**Hubble-Parameter als Funktion der Zeit:**
```
    H(t) = H₀ · √(1 − sin²(Δφ₀/2) · e^{βt})
```

| Zeitbereich | Verhalten |
|------------|-----------|
| t = 0 | H(0) = H₀ · cos(Δφ₀/2) = H₀√ε₀ (Anfangsbedingung AP1) |
| t ≪ t_max | H(t) ≈ H₀√ε₀ · (1 − sin²(Δφ₀/2)(e^{βt}−1)/(2ε₀)) (langsame Abnahme) |
| t → t_max | H(t) → 0 (Ende der Expansionsphase) |

### 5.4 Vergleich mit Friedmann-Lösungen

| Modell | H(t) | Charakteristik |
|--------|------|----------------|
| Materiedominanz (ΛCDM) | H₀(1+z)^{3/2} | Potenzgesetz-Abfall |
| Strahlungsdominanz | H₀(1+z)² | Potenzgesetz-Abfall |
| de Sitter (Λ > 0) | H₀ = const | Exponentiell |
| **RFT AP2** | H₀√(1 − sin²(Δφ₀/2)e^{βt}) | Abnahme mit Sättigungscharakter |

Die RFT-Lösung liegt strukturell zwischen Potenzgesetz und de Sitter: Für kleine
β·t verhält sie sich näherungsweise wie ein Potenzgesetz; für große Zeiten nähert
sie sich einem Endzustand H → 0.

---

## 6. Konsistenz mit A8 — Phasendynamik und Lichtgeschwindigkeit

### 6.1 A8 und die kosmologische Phasendynamik

Axiom A8 (RT-41) legt die Kopplungswellengeschwindigkeit fest:
```
    c = 1/√(μ₀ε₀)
```

Änderungen der Phasendifferenz Δφ(x⃗, t) propagieren mit Lichtgeschwindigkeit c.
Im homogenen Grenzfall (AP1) ist Δφ(t) ein globaler Freiheitsgrad — keine räumliche
Propagation, sondern eine kollektive Mode.

**Konsequenz:** A8 beschränkt Δφ̇ nicht direkt, da Δφ(t) keine räumliche Ausbreitung
darstellt.

### 6.2 Indirekte Schranke: kosmologische Zeitskala

Die charakteristische Zeitskala der ODE Δφ̇ = β tan(Δφ/2) ist β⁻¹. Damit die
Phasendynamik mit einer realistischen kosmologischen Expansion vereinbar ist, muss:
```
    β ~ H₀  →  β⁻¹ ~ H₀⁻¹  (Hubble-Zeit ≈ 14 Mrd. Jahre)
```

Für β ≫ H₀ wäre die Phasendynamik viel schneller als die Hubble-Expansion —
inkonsistent mit Beobachtungen. Für β ≪ H₀ würde die Expansion nicht stattfinden.

Die A8-Konsistenz ist also durch die **Skalenverträglichkeit** β ~ H₀ gesichert.

### 6.3 Phasengradient und Hubble-Radius

Für inhomogene Perturbationen δΔφ(x⃗, t) um den homogenen Hintergrund Δφ(t) gilt
die Dispersionsrelation (aus A8):
```
    ω²  =  c² · k²    (Wellengleichung für δΔφ)
```

Eine kosmologische Phasenschwankung auf dem Hubble-Radius R_H = c/H₀ hat:
```
    ω_H = c · k_H = c · H₀/c = H₀
```

Dies zeigt: Die kosmologische Phasendynamik (Zeitskala β⁻¹ ~ H₀⁻¹) ist genau auf
dem Hubble-Horizont kausal konsistent — A8 wird nicht verletzt.

---

## 7. Prüfung des Erfolgskriteriums

**Erfolgskriterium:** Geschlossene Differentialgleichung für Δφ(t), vergleichbar mit
Friedmann-Lösungen.

**Bewertung:**

✅ **Geschlossene ODE abgeleitet.** Die Differentialgleichung
```
    Δφ̇ = β · tan(Δφ/2)
```
ist eine autonome ODE erster Ordnung, die vollständig aus der RFT-Kopplungsdynamik
folgt (A4, A5, AP1-Homogenisierung). Sie besitzt eine analytische Lösung und ist
daher Friedmann-Lösungen vergleichbar.

✅ **Äquivalente Form über Kopplungseffizienz:**
```
    ε̇ = −β(1 − ε)
```
mit Lösung ε(t) = 1 − (1 − ε₀)e^{βt} — direkte Friedmann-Analogie.

✅ **Hubble-Parameter explizit:**
```
    H(t) = H₀ √(1 − sin²(Δφ₀/2) · e^{βt})
```

✅ **Modifizierte Raychaudhuri-Gleichung:**
```
    Ḣ = −(β/2)(H₀² − H²)/H
```

⚠️ **Direkte Identifikation Δφ̇ = H nicht möglich:** Δφ̇ und H sind verschiedene
Funktionen von Δφ. Die physikalische Verbindung läuft über ε̇ (Abschnitt 4.2).

✅ **A8-Konsistenz:** Für β ~ H₀ ist die Phasendynamik kausal konsistent mit dem
Hubble-Horizont. Keine Verletzung von Axiom A8.

✅ **Erfolgskriterium erfüllt** (mit dokumentierter Einschränkung zur direkten
Identifikation).

---

## 8. Ergebnis und Ausblick auf AP3–AP7

**Zentrales Ergebnis von AP2:**

Die Zeitableitung Δφ̇(t) der kosmologischen Phase folgt aus der RFT-Kopplungsdynamik
als geschlossene ODE:
```
    Δφ̇ = β · tan(Δφ/2)
```

Die vollständige Lösung lautet:
```
    sin(Δφ(t)/2) = sin(Δφ₀/2) · e^{βt/2}
    ε(t) = 1 − sin²(Δφ₀/2) · e^{βt}
    H(t) = H₀ · √(1 − sin²(Δφ₀/2) · e^{βt})
```

Die Phasendynamik ist Friedmann-Lösungen vergleichbar: Sie beschreibt ein Universum,
das von maximaler Kopplung (Δφ = 0, H = H₀) zu vollständigem Kopplungsverlust
(Δφ → π, H → 0) übergeht, angetrieben durch den Dissipationsparameter β ~ H₀.

**Ausblick:**

- **AP3:** Prüfung, ob ein Phasengradient ∇Δφ einen effektiven Λ-Term erzeugt —
  AP2 zeigt w ∈ [−1/3, +1/3] aus RT-33; ob w = −1 erreichbar ist, bleibt offen
- **AP4:** Kosmologische Einordnung der 28-Größenordnungen-Diskrepanz:
  β ∼ H₀ ∼ 10⁻¹⁸ Hz als natürliche Skala; Warp-Regime β ∼ f_Resonator unvereinbar
- **AP5:** Aus ε(t) = 1 − sin²(Δφ₀/2)e^{βt} folgt H(z) — vergleichbar mit
  Planck/SH0ES, da β und Δφ₀ freie Parameter der RFT-Kosmologie sind
- **AP6:** ε̇ = −β(1−ε) als Bewegungsgleichung des Phaseneffekts: kosmische
  Expansion ist vollständig durch Kopplungsverlust beschrieben
- **AP7:** Konsistenzprüfung mit RT-33 (w(Δφ)), RT-40 (Lorentz-Struktur) und
  RT-41 (A8, Kausalität)

**Verbindung zu bestehenden Ergebnissen:**
- RT-42 AP1: H = H₀ cos(Δφ/2) — AP2 liefert die Bewegungsgleichung für diese Größe
- RT-40 AP2: ε = 1/γ² — Kopplungseffizienz trägt Energieinformation; hier: ε trägt kosmologische Dichte
- RT-33: w(Δφ) = (1/3)[2ε − 1]; aus ε̇ = −β(1−ε) folgt ẇ = −(2β/3)ε (dynamische Zustandsgleichung)
- RT-41 (A8): β ~ H₀ sichert kausale Konsistenz auf dem Hubble-Horizont

---

*RT-42 AP2 — DominicReneSchu/RFT — September 2026*
