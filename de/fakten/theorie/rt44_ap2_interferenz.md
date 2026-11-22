# RT-44 AP2 — Interferenz und Welle-Teilchen-Dualismus als ε-Regime

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Doppelspalt-Interferenz aus A2 + ε-Struktur ableiten;
Welle-Teilchen-Übergang als ε-Regime beschreiben.

**Ergebnis:** Interferenzmuster formal aus A1+A2 ableitbar.
ε(Δφ) ist das Kohärenzmaß: ε=1 → vollständige Kohärenz, ε=0 → vollständige Dekohärenz.

---

## 2. Doppelspalt-Interferenz aus A1 und A2

### 2.1 Superposition

**Axiom A2:** Schwingungen überlagern sich linear.

Zwei Quellen ψ₁ = A₁ e^{i(k·r₁ − ωt)}, ψ₂ = A₂ e^{i(k·r₂ − ωt)}:

```
Ψ(x,t) = ψ₁ + ψ₂   (A2)
```

### 2.2 Intensitätsmuster

```
I = |Ψ|² = |ψ₁|² + |ψ₂|² + 2 Re(ψ₁* ψ₂)
         = I₁ + I₂ + 2√(I₁I₂) cos(Δφ)
```

mit Phasendifferenz Δφ = k(r₁ − r₂).

### 2.3 Verbindung zu ε(Δφ)

Die Kopplungseffizienz:
```
ε(Δφ) = cos²(Δφ/2) = (1 + cos Δφ)/2
→  cos Δφ = 2ε(Δφ) − 1
```

Damit lässt sich der Interferenzterm ausdrücken als:
```
I = I₁ + I₂ + 2√(I₁I₂) · (2ε(Δφ) − 1)
  = I₁ + I₂ − 2√(I₁I₂) + 4√(I₁I₂) · ε(Δφ)
```

Für gleiche Amplituden (I₁ = I₂ = I₀):
```
I = 2I₀ · (1 + cos Δφ) = 4I₀ · ε(Δφ)
```

**ε(Δφ) ist direkt proportional zur Interferenzintensität.** Bei ε=1 (Δφ=0):
I = 4I₀ (konstruktive Interferenz). Bei ε=0 (Δφ=π): I = 0 (destruktive Interferenz).

---

## 3. Welle-Teilchen-Dualismus als ε-Übergang

| ε-Wert | Physikalisches Regime | Verhalten |
|--------|----------------------|-----------|
| ε = 1 (Δφ=0) | Vollständige Kohärenz | Wellenregime: Interferenz maximal |
| ε ∈ (0,1) | Partielle Kopplung | Übergangsregime: Dekohärenz |
| ε = 0 (Δφ=π) | Vollständige Entkopplung | Teilchenregime: klassischer Pfad |

**Physikalische Interpretation:**
- **Wellenregime (ε→1):** Das Teilchen koppelt an beide Spalte simultan; Superposition
  aus A2 gilt voll. Interferenzmuster erscheint.
- **Teilchenregime (ε→0):** Das Teilchen koppelt an genau einen Pfad (Lokalisierung
  durch Messung); Superposition kollabiert. Kein Interferenzmuster.
- **Dekohärenz (0 < ε < 1):** Partielle Kopplung, z.B. durch Welcher-Weg-Detektor.
  Interferenzkontrast fällt mit ε: V = I_max/(I_max + I_min) ∝ ε.

---

## 4. Quantitatives Dekohärenz-Modell

Die Sichtbarkeit (Kontrast) des Interferenzmusters:

```
V = (I_max − I_min)/(I_max + I_min) = |⟨ε⟩| = |⟨cos²(Δφ/2)⟩_avg
```

Für partielle Kohärenz mit mittlerer Phasendifferenz ⟨Δφ⟩ und Streubreite σ_Δφ:

```
V = exp(−σ_Δφ²/2) · ε(⟨Δφ⟩)
```

Bei σ_Δφ → 0 (monochromatische Quelle): V = ε(⟨Δφ⟩) = cos²(⟨Δφ⟩/2).
Bei σ_Δφ → ∞ (inkoheränt): V → 0.

**Falsifikationskriterium:** Wenn Interferenzkontrast V ≠ cos²(Δφ/2) → RFT-Kohärenzmodell widerlegt.

---

## 5. Ergebnis

```
I(Δφ) = 4I₀ · ε(Δφ) = 4I₀ · cos²(Δφ/2)   [für gleiche Amplituden]
```

Doppelspalt-Interferenz folgt direkt aus A2 (Superposition) + A1 (Schwingungsfelder).
Die Kopplungseffizienz ε(Δφ) ist das natürliche Kohärenzmaß der RFT:
Interferenz = vollständige Kopplung (ε=1), klassisches Teilchen = Entkopplung (ε=0).

**Erfolgskriterium:** ✅ Erfüllt.

---

*RT-44 AP2 — DominicReneSchu/RFT — November 2026*
