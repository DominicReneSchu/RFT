# Resonanzintegrale — Analytische Methoden der Resonanzfeldtheorie

*Dominic-René Schu, 2025/2026*

---

## 1. Einleitung

Die Resonanzfeldtheorie liefert nicht nur ein physikalisches
Rahmenwerk, sondern auch einen systematischen Zugang zu einer
Klasse analytischer Integrale, die in der Physik fundamentale
Bedeutung haben: **Resonanzintegrale**.

Dieses Kapitel zeigt, wie die Axiome der RFT (insbesondere
Superposition, Resonanzbedingung und Kopplungsenergie) eine
einheitliche Methode zur Berechnung und Interpretation dieser
Integrale bereitstellen.

---

## 2. Das Dirichlet-Integral als Resonanzenergie

### 2.1 Das Problem

Das bestimmte Integral:

```
    I = ∫₀^∞ sin(x)/x dx
```

ist eines der bekanntesten Integrale der Analysis. Sein Wert
ist exakt bekannt:

```
    I = π/2
```

Das unbestimmte Integral ∫ sin(x)/x dx ist nicht-elementar
(Liouville-Theorie). Die Funktion sin(x)/x — die sinc-Funktion —
taucht in Signalverarbeitung, Optik, Quantenmechanik und
Informationstheorie auf.

### 2.2 Herleitung über Modenzerlegung (Axiome 1, 2)

Die sinc-Funktion besitzt eine exakte Fourier-Darstellung als
Superposition ebener Wellen:

```
    sin(x)/x = (1/2) ∫_{-1}^{1} e^{iωx} dω
```

Dies ist eine direkte Anwendung von Axiom 1 (jede Entität ist
durch periodische Schwingungen beschreibbar) und Axiom 2
(Superposition): sin(x)/x ist die gleichgewichtete Überlagerung
aller Frequenzen ω im Band [−1, 1].

### 2.3 Integration über alle Zeiten

```
    ∫₀^∞ sin(x)/x dx = (1/2) ∫_{-1}^{1} [∫₀^∞ e^{iωx} dx] dω
```

Das innere Integral ergibt im distributionellen Sinn:

```
    ∫₀^∞ e^{iωx} dx = π · δ(ω) + i · P(1/ω)
```

Einsetzen und Auswertung:

```
    I = (1/2) ∫_{-1}^{1} [π · δ(ω) + i · P(1/ω)] dω
      = (1/2) · [π · 1 + i · 0]
      = π/2
```

Der Imaginärteil verschwindet durch Symmetrie von P(1/ω) auf
dem symmetrischen Intervall [−1, 1].

### 2.4 RFT-Interpretation

In der Sprache der Resonanzfeldtheorie:

- **sin(x)/x ist ein Resonanzfenster**: Die sinc-Funktion ist die
  Fourier-Transformierte eines Rechteckfensters im Frequenzraum —
  sie beschreibt ein ideales Resonanzband mit scharfen Grenzen

- **Das Integral berechnet die Kopplungsenergie**: Die Gesamtenergie
  aller Moden innerhalb des Resonanzfensters [−1, 1]

- **Das Ergebnis π/2 ist die halbe Kopplungsenergie**:

```
    Aus Axiom 4:    E_eff = π · ε · h · f

    Für ε = 1/2 (halbe Kopplung, Δφ = π/2):
    E_eff = (π/2) · h · f

    Das Dirichlet-Integral ist (normiert auf h·f = 1):
    ∫₀^∞ sin(x)/x dx = π/2 = E_eff(ε = 1/2)
```

Das Dirichlet-Integral entspricht der Kopplungsenergie bei halber
Kopplungseffizienz — konsistent mit der Tatsache, dass nur die
positive Halbachse [0, ∞) integriert wird (halber Phasenraum).


---

## 3. Familie der Resonanzintegrale

Die Modenzerlegungsmethode liefert systematisch exakte Ergebnisse
für verwandte Integrale.

### 3.1 Skalierte Resonanzfrequenz (Axiom 7: Invarianz)

```
    ∫₀^∞ sin(ax)/x dx = (π/2) · sgn(a)
```

**RFT-Interpretation:** Frequenzskalierung f → a·f ändert das
Ergebnis nicht (für a > 0). Dies ist eine direkte Konsequenz
von Axiom 7 (Invarianz unter synchronen Transformationen):
Die Kopplungsenergie ist skalierungsinvariant.

### 3.2 Gedämpfte Resonanz (endliche Kopplungseffizienz)

```
    ∫₀^∞ e^{−bx} · sin(ax)/x dx = arctan(a/b)     (b > 0)
```

**RFT-Interpretation:** Der Dämpfungsfaktor e^{−bx} modelliert
eine abklingende Kopplungseffizienz ε(x) = e^{−bx}. Das Ergebnis
arctan(a/b) ist der Phasenwinkel der resultierenden Kopplung.

**Grenzfälle:**
- b → 0 (keine Dämpfung): arctan(∞) = π/2 → Dirichlet-Integral
- b → ∞ (starke Dämpfung): arctan(0) = 0 → keine Kopplung
- a = b: arctan(1) = π/4 → Gleichgewicht Resonanz/Dämpfung

### 3.3 Energiedichte des Resonanzfensters

```
    ∫₀^∞ [sin(x)/x]² dx = π/2
```

**RFT-Interpretation:** Die Energiedichte (∝ Amplitude²) des
Resonanzfensters integriert zum selben Wert π/2 wie die Amplitude
selbst — Ausdruck der Parseval-Identität (Energieerhaltung im
Frequenzraum, konsistent mit Axiom 2).

### 3.4 Kopplung zweier Resonanzfenster (Axiom 3)

```
    ∫₀^∞ [sin(ax)/x] · [sin(bx)/x] dx = (π/2) · min(a, b)
                                           für a, b > 0
```

**RFT-Interpretation:** Das Kopplungsintegral zweier
Resonanzfenster mit Grenzfrequenzen a und b ergibt die Energie
des überlappenden Frequenzbands — direkte Anwendung von Axiom 3:
Resonanz tritt nur im gemeinsamen Frequenzbereich auf.

**Konsequenz:** Für a ≠ b ist die Kopplung durch das schmalere
Band begrenzt. Für a = b ergibt sich π·a/2 — maximale Kopplung.

### 3.5 Mehrfach-Resonanzprodukte

```
    ∫_{-∞}^{∞} ∏_{k=1}^{n} sin(a_k x)/(a_k x) dx
    = π / max(a_k)    falls Σ a_k ≤ max(a_k) · n/(n-1)
```

**RFT-Interpretation:** Bei n gekoppelten Moden wird die
Gesamtenergie durch die Überlappung aller Resonanzfenster
bestimmt — eine Mehrmodenkopplung gemäß Axiom 4.

---

## 4. Resonanzoperatoren: Erweiterung klassischer Operatoren

Die Modenzerlegungsmethode motiviert resonanzangepasste Operatoren.

### 4.1 Resonanzgewichtete Integration

Definition eines resonanzgewichteten Integrals:

```
    ∫_ε f(x) dx  :=  ∫ f(x) · ε(x) dx
```

wobei ε(x) die ortsabhängige Kopplungseffizienz ist.

**Beispiel:** Für ε(x) = e^{−bx} und f(x) = sin(ax)/x:

```
    ∫_0^∞ sin(ax)/x · e^{-bx} dx = arctan(a/b)
```

### 4.2 Resonanzableitung

Die Ableitung eines resonanzgekoppelten Felds berücksichtigt
die Kopplungsstruktur:

```
    d_ε/dx [A · sin(ωx + φ)] = A · ω · cos(ωx + φ) · ε(Δφ)
```

Nur der phasenkohärente Anteil der Ableitung trägt bei.

---

## 5. Zusammenfassung

| Integral | Wert | RFT-Interpretation |
|----------|------|-------------------|
| ∫₀^∞ sin(x)/x dx | π/2 | Kopplungsenergie bei ε = 1/2 |
| ∫₀^∞ e^{−bx} sin(ax)/x dx | arctan(a/b) | Phasenwinkel gedämpfter Kopplung |
| ∫₀^∞ [sin(x)/x]² dx | π/2 | Energieerhaltung (Parseval) |
| ∫₀^∞ sin(ax)/x · sin(bx)/x dx | (π/2)·min(a,b) | Kopplung im überlappenden Band |
| ∫₀^∞ sin(ax)/x dx | (π/2)·sgn(a) | Skalierungsinvarianz (A7) |

Die RFT liefert eine einheitliche physikalische Interpretation
für eine Familie analytischer Integrale. Die sinc-Funktion als
Resonanzfenster, die Modenzerlegung als Methode und die
Kopplungseffizienz als Gewichtung bilden ein konsistentes
Berechnungsframework.

---

## 6. Ausblick

- Erweiterung auf mehrdimensionale Resonanzintegrale
- Resonanzgewichtete Lösungen partieller Differentialgleichungen
- Numerische Effizienzvergleiche mit klassischen Methoden
- Anwendungen in der Signalverarbeitung und Quantenoptik

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)