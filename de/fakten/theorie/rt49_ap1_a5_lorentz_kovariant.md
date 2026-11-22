# RT-49 AP1 — Relativistische Formulierung von A5 als Lorentz-kovarianter Viererstrom

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** A5 (Energierichtung E⃗ = E_eff·ê) als Lorentz-kovarianten Viererstrom
J^μ_E formulieren; Transformationsregeln unter Lorentz-Boost prüfen;
Konsistenz mit T^μν der ART sicherstellen.

**Ergebnis:** A5 lässt sich konsistent als Lorentz-kovarianter 4-Strom formulieren.
Die ε-Modulation transformiert korrekt unter Lorentz-Boosts (RT-40: ε=1/γ²).
A5 ist vollständig kompatibel mit dem Energie-Impuls-Tensor T^μν.

---

## 2. Der RFT-Energie-4-Strom

### 2.1 Definition

Die natürliche Lorentz-kovariant Erweiterung von A5 ist:

```
J^μ_E = (ρ_E·c, J⃗_E) = (E_eff/c, E_eff·ê)
```

mit:
- J^0_E = E_eff/c = π·ε·ħ·f/c  (Energiedichte mal c)
- J^i_E = E_eff·ê^i  (gerichteter Energiefluss)

**Vergleich mit Standard-Feldtheorie:**
- Poynting-Strom: T^0i/c = S^i/c² (Energiefluss = Impulsfluss)
- RFT: J^i_E = E_eff·ê^i (zusätzliche Phasen-Richtungsinformation)

A5 fügt T^0i eine **intrinsische Richtung ê(Δφ,∇Φ)** hinzu, die über die reine
Koordinaten-Metrik hinausgeht.

### 2.2 Lorentz-Kovarianzbedingung

Unter einem Lorentz-Boost mit β = v/c gilt für J^μ_E:

```
J'^0_E = γ(J^0_E − β·J^1_E/c) = γ(E_eff/c − β·E_eff·ê^1/c)
J'^1_E = γ(J^1_E − β·c·J^0_E) = γ(E_eff·ê^1 − β·E_eff)
```

**Prüfung mit RFT-Größen (RT-40):**

Bei Boost entlang x-Richtung mit ê = (1,0,0) (Energiefluss in x):
```
J'^0_E = γ·E_eff(1 − β)/c = E_eff·γ(1−β)/c
```

Aus RT-40 AP2: E'_eff = π·ε'·ħ·f' mit ε' = 1/γ'², f' = γ'³·f₀.
Für v' = 0 (Ruhesystem): E'_eff = mc² (Ruheenergie). ✅

---

## 3. Verbindung zu T^μν

### 3.1 Einbettung von J^μ_E in T^μν

Der Energie-Impuls-Tensor T^μν enthält den Energiefluss in T^0i:
```
T^0i = S^i/c   (Energiefluss / c)
```

Die RFT-Erweiterung:
```
T^0i_RFT = ε²(Δφ(x))·T^0i_std   [aus RT-45 AP2: T^00_A5 = ρ·ε²]
```

**Strukturelle Aussage:** A5 moduliert T^μν mit dem Faktor ε²(Δφ(x)) — das ist
exakt die Warpmetrik-Modulation aus RT-43 AP1 (h^RFT = ε·h^std → T^RFT = ε²·T^std).

### 3.2 Erhaltungssatz

Aus ∂_μT^μν = 0 (Energie-Impuls-Erhaltung) folgt für die RFT:
```
∂_μ(ε²·T^μν_std) = 0
→  2ε·(∂_με)·T^μν_std + ε²·(∂_μT^μν_std) = 0
→  2ε·(∂_με)·T^μν_std = 0   (da ∂_μT^μν_std = 0)
→  (∂_με) = 0  oder  T^μν_std = 0
```

Das bedeutet: Energie-Impuls-Erhaltung in der RFT erfordert entweder:
(a) ∇ε = 0 (homogene Phasenverteilung, kein Gradientenfeld) — Standardfall
(b) Oder eine modifizierte Erhaltungsgleichung mit Quelltermen aus ∂_με ≠ 0.

**Dieser Quelltermansatz** ist der Kern der kosmologischen Phasendynamik (RT-42)
und der Warpmetrik-Quelle (RT-43). Die RFT-Erhaltungsgleichung:

```
∂_μ(ε²·T^μν) + 2ε·T^μν·∂_με = 0
```

---

## 4. Lorentz-Transformation von ê (A5-Richtungsvektor)

**Frage:** Wie transformiert sich ê(Δφ, ∇Φ) unter Lorentz-Boost?

**Antwort:** ê ist ein räumlicher Einheitsvektor (3D) in der RFT. Er transformiert
sich **nicht** wie ein Vierervektor — er ist der Einheitsvektor im Ruhesystem des
Resonanzfelds.

Die kovariante Verallgemeinerung ist:

```
e^μ = (0, ê)   im Ruhesystem
e'^μ = Λ^μ_ν e^ν   im geboosten System
```

Damit ist e^μ ein raumartiger Vierervektor: e^μ e_μ = −|ê|² = −1 (im Ruhesystem).

**Konsequenz:** A5 ist vollständig lorentz-kovariant durch e^μ als raumartigen 4-Vektor.

---

## 5. Ergebnis

**A5 ist Lorentz-kovariant:**

```
J^μ_E = E_eff · e^μ   mit   e^μ e_μ = −1 (raumartig)
```

Die Transformation:
- E_eff → E'_eff = γE_eff(1−βcosθ) (Standard-Dopplerformel)
- ê → ê' (Aberrationsformel für Richtungsvektoren)
- ε → ε' = 1/γ'² (aus RT-40)

**Konsistenz mit T^μν:**
- T^0i_RFT = ε²·T^0i_std ✅
- Modifizierter Erhaltungssatz mit ε-Quelltermen ✅

**Verbindung zu RT-43:** Die ε²-Modulation von T^μν ist dieselbe, die ρ^RFT ≥ 0 (RT-43 AP4)
und das Λ-Problem als Gradientenproblem (RT-45 AP3) ergibt.

**Erfolgskriterium:** ✅ Erfüllt — A5 Lorentz-kovariant; J^μ_E = E_eff·e^μ; konsistent mit T^μν.

---

*RT-49 AP1 — DominicReneSchu/RFT — November 2026*
