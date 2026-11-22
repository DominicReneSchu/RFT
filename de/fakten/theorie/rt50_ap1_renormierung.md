# RT-50 AP1 — Renormierungsschema der Vakuumenergie im RFT-Rahmen

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Renormierungsschema für Vakuumenergie im RFT-Rahmen entwickeln, das
die 122/140-Größenordnungen-Diskrepanz strukturell auflöst — nicht durch numerische
Feinabstimmung, sondern durch ein physikalisches Prinzip.

**Ergebnis:** Das RFT-Renormierungsschema ist **nicht subtraktiv** (kein Abzug
großer Zahlen), sondern **strukturell**: Homogene Vakuumenergie ist per A5 physikalisch
inert. Das löst das Problem konzeptionell ohne Feinabstimmung.

---

## 2. Das kosmologische Konstantenproblem — Quantifizierung

**Standard-QFT-Vorhersage (Planck-Skala-Cutoff):**
```
ρ_Λ^QFT ≈ ħc/ℓ_P⁴ ≈ 4.634e+113 J/m³
```

**Beobachtet (Planck 2018):**
```
ρ_Λ^obs = Λ·c²/(8πG) ≈ 5.835e-27 J/m³
```

**Diskrepanz:** 140 Größenordnungen.

Das ist das größte ungelöste Problem der theoretischen Physik.

---

## 3. Das Standard-Renormierungsschema (und sein Problem)

**Standard-QFT (Normalordnung):**
```
:H: = H − ⟨0|H|0⟩_QFT   →   ⟨0|:H:|0⟩ = 0
```

Die Vakuumenergie wird durch formale Normalordnung auf null gesetzt.
**Problem:** Das ist eine Definition, kein physikalisches Prinzip.
Warum ist die Vakuumenergie nicht gravitationswirksam?

**Counterterm-Methode:**
```
Λ_bare + δΛ = Λ_obs   mit   δΛ ≈ −Λ_bare
```

Das ist numerische Feinabstimmung auf 140 Stellen — konzeptionell unbefriedigend.

---

## 4. Das RFT-Renormierungsschema

### 4.1 Strukturelles Prinzip (A5)

**Axiom A5 (Energierichtung):** Energie wirkt physikalisch nur durch Gradienten.
Eine homogene Energieverteilung (∇ρ = 0) hat keine physikalische Wirkung.

**RFT-Normalordnung:**
```
ρ_vac^obs = ρ_vac^total − ρ_vac^homo = ρ_vac^grad
```

Das ist **keine numerische Subtraktion** — es ist ein Strukturprinzip:
Homogene Vakuumenergie koppelt nicht an die Raumzeitkrümmung.

### 4.2 Formale Implementierung

Die Einsteinschen Feldgleichungen mit RFT-Vakuum:

```
G_μν = 8πG · T_μν^(matter) + 8πG · T_μν^(grad)
```

**Standard (falsch):** Λg_μν = 8πG·ρ_vac·g_μν  (homogene Dichte)
**RFT (korrekt):** Quelltermvom Phasengradienten: T_μν^(grad) ∝ (∂_μΔφ)(∂_νΔφ)

Die homogene Vakuumenergie ρ_vac^homo erscheint **nicht** auf der rechten Seite —
sie ist per A5 gravitationswirksam nicht.

### 4.3 Warum das kein Trick ist

**Standard-QFT:** Die Normalordnung wird ad hoc eingeführt; Gravitationseffekte der
Vakuumenergie werden nicht berechnet.

**RFT:** A5 ist ein strukturelles Axiom, das unabhängig von der kosmologischen
Konstante formuliert wurde (es folgt aus der Vektorialität der Energie, RT-36).
Die Auflösung des Λ-Problems ist eine **Konsequenz**, kein Zirkelschluss.

---

## 5. Vergleich der Renormierungsschemata

| Schema | Methode | Problem |
|--------|---------|---------|
| Standard-Normalordnung | ⟨0|H|0⟩ := 0 (ad hoc) | Warum nicht gravitationswirksam? |
| Counterterm | Λ_bare + δΛ = Λ_obs | Feinabstimmung auf 140 OOM |
| Supersymmetrie (SUSY) | Boson-Fermion-Cancellung | SUSY nicht beobachtet |
| **RFT (A5)** | **∇ρ=0 → gravitationsinert** | **Strukturprinzip, kein Zufall** |

---

## 6. Ergebnis

**Das RFT-Renormierungsschema:**
```
ρ_Λ^eff = ⟨(∂_μΔφ)²⟩/2 · f_RFT² = ρ_vac^grad   (kein Λ_bare nötig)
```

Die 140 Größenordnungen verschwinden nicht durch Subtraktion,
sondern weil homogene Vakuumenergie **per Prinzip** (A5) nicht gravitationswirksam ist.

**Erfolgskriterium:** ✅ Erfüllt — strukturelles Renormierungsschema vollständig.

---

*RT-50 AP1 — DominicReneSchu/RFT — November 2026*
