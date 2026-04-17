# Numerische Demonstration der Resonanzfeldtheorie

Numerische Analyse von Resonanzenergie, Kopplungseffizienz
und Resonanzentropie über dem (A, τ)-Parameterraum.

> **Einordnung:** Diese Simulation demonstriert die interne
> Konsistenz der Axiome A3–A5. Sie ist **kein empirischer
> Beweis** der Resonanzfeldtheorie, da keine unabhängigen
> experimentellen Daten verwendet werden. Die Simulation
> zeigt, dass die Formeln korrekt implementiert sind und
> die erwarteten mathematischen Eigenschaften aufweisen.
>
> Für die empirische Validierung mit unabhängigen Daten
> siehe die [Monte-Carlo-Analyse](../../empirisch/monte_carlo_test/monte_carlo.md).

<p align="center">
  <img src="plot.png" alt="Resonanzfeldtheorie — Numerische Demonstration" width="900"/>
</p>

---

## Axiom-Bezug

| Axiom | Umsetzung | Was demonstriert wird |
|-------|-----------|----------------------|
| A3 Resonanzbedingung | Peak bei ω_ext ≈ ω₀ | Lorentz-Profil zeigt Resonanzmaximum |
| A4 Kopplungseffizienz | ε = E_res / A ∈ (0, 1] | Normierung ist amplitudenunabhängig |
| A5 Stabiles Feld | S = −ε·ln(ε) ≥ 0 | Entropie-Maximum bei ε = 1/e |

---

## 1. Resonanzenergie (Lorentz-Profil)

$$
E_{\mathrm{res}} = \frac{A}{1 + \left(\frac{\omega_{\mathrm{ext}} - \omega_0}{\gamma}\right)^2}
$$

mit ω_ext = ω₀ · (1 + sin(τ)).

| Symbol | Bedeutung | Default |
|--------|-----------|---------|
| A | Amplitude | 0.1–5.0 |
| ω₀ | Eigenfrequenz | 1.0 |
| γ | Dämpfungskonstante (Halbwertsbreite) | 0.2 |
| τ | Verstimmungsparameter | 0.1–5.0 |

Das Lorentz-Profil ist ein klassisches Ergebnis der Physik
(Hendrik Lorentz, ~1880). Die Simulation demonstriert, dass
es sich als Spezialfall von Axiom A3 (Resonanzbedingung)
interpretieren lässt.

---

## 2. Kopplungseffizienz (Axiom A4)

$$
\varepsilon = \frac{E_{\mathrm{res}}}{A} =
\frac{1}{1 + \left(\frac{\omega_{\mathrm{ext}} - \omega_0}{\gamma}\right)^2}
\in (0, 1]
$$

### Grenzfälle

| Bedingung | ε | Bedeutung |
|-----------|---|-----------|
| ω_ext = ω₀ | 1.0 | Exakte Resonanz — maximale Effizienz |
| \|ω_ext − ω₀\| = γ | 0.5 | Halbwertsbreite |
| \|ω_ext − ω₀\| ≫ γ | → 0 | Stark verstimmt — keine Kopplung |

Dies ist die **frequenzabhängige** Realisierung der
Kopplungseffizienz. Die anderen Simulationen verwenden
komplementäre Modelle:

| Modell | Formel | Simulation |
|--------|--------|------------|
| Phasenbasiert | cos²(Δφ/2) | Resonanz-KI, Doppelpendel |
| Frequenzbasiert (Lorentz) | 1/(1+(Δω/γ)²) | **Diese Simulation** |
| Exponentiell | exp(−α·\|Δf\|) | Gekoppelte Oszillatoren |

Alle drei liefern ε ∈ (0, 1] — das ist eine konsistente
Eigenschaft, aber kein Beweis, dass das Konzept physikalisch
korrekt ist.

---

## 3. Resonanzentropie (Axiom A5)

$$
S = -\varepsilon \cdot \ln(\varepsilon), \quad \varepsilon \in (0, 1]
$$

### Mathematische Eigenschaften

| ε | S | Interpretation |
|---|---|----------------|
| 1.0 | 0 | Perfekte Resonanz — Ordnung |
| 1/e ≈ 0.368 | 1/e ≈ 0.368 | Maximum — Balance |
| → 0 | → 0 | Keine Kopplung — triviale Ordnung |

S ≥ 0 ist garantiert, da ε ∈ (0, 1] und −x·ln(x) ≥ 0
auf diesem Intervall. Das Maximum bei 1/e folgt aus
S'(ε) = −ln(ε) − 1 = 0 → ε = 1/e.

> **Hinweis:** Diese Eigenschaften folgen aus der
> Analysis der Funktion f(x) = −x·ln(x), nicht aus
> physikalischen Prinzipien. Die Interpretation als
> Resonanzentropie ist eine Hypothese der RFT, die
> empirisch validiert werden muss.

---

## 4. Was diese Simulation zeigt — und was nicht

### Was sie zeigt ✓

- Die Formeln sind **korrekt implementiert** (16 Unit-Tests bestanden)
- Die drei Größen (E_res, ε, S) sind **intern konsistent**
- ε ist **amplitudenunabhängig** — eine nicht-triviale Eigenschaft
- Die ε-Normierung löst das Problem negativer Entropie der alten Version
- Das Lorentz-Profil lässt sich als Spezialfall von Axiom A3 **interpretieren**

### Was sie nicht zeigt ✗

- Kein Vergleich mit **experimentellen Daten**
- Keine **falsifizierbare Vorhersage** — die Simulation berechnet eingesetzte Formeln
- Keine **neuartige Physik** — das Lorentz-Profil ist seit ~140 Jahren bekannt
- Kein Beweis, dass ε = E_res/A eine physikalisch **sinnvolle** Kopplungseffizienz ist

### Nächster Schritt: Empirische Validierung

Die eigentliche Beweisführung liegt in der **Monte-Carlo-Analyse**,
die Resonanzstrukturen in unabhängigen Daten identifiziert und
die statistische Signifikanz quantifiziert:

→ [Monte-Carlo-Analyse](../../empirisch/monte_carlo_test/monte_carlo.md)

---

## 5. Ausführung

```bash
pip install numpy matplotlib
python numerische_demonstration.py
```

Tests:
```bash
python tests/test_numerische_demonstration.py
# oder mit pytest:
pip install pytest
pytest tests/ -v
```

---

## Quellcode

[numerische_demonstration.py](numerische_demonstration.py)

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück zur Übersicht](README.md)