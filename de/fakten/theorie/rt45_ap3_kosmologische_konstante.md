# RT-45 AP3 — Kosmologisches Konstantenproblem als Gradientenproblem

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Das kosmologische Konstantenproblem als Gradientenproblem reformulieren.

**Ergebnis:** Das kosmologische Konstantenproblem löst sich konzeptionell auf,
wenn A5 (Energie wirkt nur durch Gradienten) konsequent angewendet wird.
Eine homogene Vakuumenergie hat keine physikalische Wirkung — das 122-Größenordnungen-
Problem ist ein Artefakt der skalaren Behandlung.

---

## 2. Das kosmologische Konstantenproblem (Standard)

**Standard-QFT-Vorhersage:**
```
ρ_Λ^QFT ~ m_Planck⁴ / (ħ³c³) ~ 10⁹⁶ kg/m³
```

**Beobachtet:**
```
ρ_Λ^obs ~ 10⁻²⁶ kg/m³
```

**Diskrepanz:** ~122 Größenordnungen — das größte ungelöste Problem der theoretischen Physik.

**Warum problematisch?** Weil die QFT erwartet, dass jeder Quantenfeldmode mit
Energie ~ħω/2 zur Vakuumenergie beiträgt — und diese zur Kosmologie-Konstante
summiert werden müsste.

---

## 3. RFT-Reformulierung: A5 und Gradienten

**Kern von A5:** Energie hat Richtung und wirkt physikalisch nur durch Gradienten.

**Konsequenz:** Eine **streng homogene** Vakuumenergie ρ_Λ^hom = const hat:
```
∇ρ_Λ^hom = 0   →   keine Kraft, kein Energiefluss, keine physikalische Wirkung
```

In der RFT gilt: Das Gravitationsfeld koppelt an den **Phasengradienten** ∇Δφ,
nicht an die skalare Dichte ρ. Damit:

```
G_μν = 8πG · T_μν^(grad)   statt   G_μν = 8πG · T_μν^(scalar) + Λg_μν
```

mit T_μν^(grad) ∝ ∂_μΔφ · ∂_νΔφ (Phasengradient-Stressenergietensor).

---

## 4. Modifizierte Friedmann-Gleichung

Aus RT-42 (Phasendynamik) und A5 (Energierichtung) folgt die modifizierte
Friedmann-Gleichung:

```
H² = (8πG/3) · [ρ_m + ρ_r + ρ_grad(∇Δφ)] − kc²/a²
```

mit dem Gradiententerm:

```
ρ_grad = (1/2) · (∂_μΔφ)² · f_RFT²
       = (1/2) · |∇Δφ|² · f_RFT²
```

**Warum ist ρ_grad klein?** Auf kosmologischen Skalen (R_H ~ 10²⁶ m) ist:

```
|∇Δφ| ~ Δφ/R_H ~ π / 10²⁶ m ~ 10⁻²⁶ m⁻¹
ρ_grad ~ 10⁻⁵² · f_RFT²
```

Für f_RFT ~ H₀ ~ 10⁻¹⁸ Hz:
```
ρ_grad ~ 10⁻⁵² · 10⁻³⁶ ~ 10⁻⁸⁸   (in Planck-Einheiten)
```

Das ist um viele Größenordnungen kleiner als die QFT-Vorhersage, aber **nicht
präzise gleich** ρ_Λ^obs. Eine vollständige quantitative Abstimmung erfordert
die relativistische Erweiterung der RFT.

---

## 5. Warum verschwindet die homogene Vakuumenergie?

In der Standard-QFT summiert jeder Quantenfeldmode ħω/2 zur Vakuumenergie.
In der RFT gilt A5: Jeder homogene Modenbeitrag (∇ε = 0, ∇Δφ = 0) hat
**keine physikalische Wirkung**.

Die effektive kosmologische Konstante in der RFT ist:

```
Λ_eff = Λ_bare − ⟨ρ_vac^homo⟩_RFT = 0
```

weil ρ_vac^homo per A5 unbeobachtbar ist. Nur die **gradientenreichen Anteile**
der Vakuumstruktur (Quantenfluktuationen, die ∇Δφ ≠ 0 erzeugen) tragen zur
beobachtbaren kosmologischen Konstante bei.

**Strukturelles Argument:**

```
⟨ρ_Λ⟩_obs = ⟨ρ_vac⟩_grad = ⟨(∂_μΔφ)²⟩/2 · f_RFT²
```

Das ist klein, weil Quantenfluktuationen auf kosmologischen Skalen mitteln.

---

## 6. Status und offene Fragen

**Was ist gelöst:**
- Konzeptionelle Auflösung: Homogene Vakuumenergie wirkt per A5 nicht (∇ρ = 0).
- Gradiententerm ρ_grad ist strukturell klein (~H₀²/c²).

**Was ist noch offen:**
- Quantitative Übereinstimmung mit ρ_Λ^obs erfordert relativistische RFT-Erweiterung.
- Renormierung der QFT-Vakuumenergie im RFT-Rahmen (wie muss die normale Ordnung angepasst werden?).

---

## 7. Ergebnis

Das kosmologische Konstantenproblem ist in der RFT ein **konzeptionelles Gradientenproblem**:

```
ρ_Λ^problem → verschwindet, weil:
∇ρ_hom = 0 → homogene Vakuumenergie physikalisch wirkungslos (A5)
ρ_obs ← nur aus Phasengradienten ∇Δφ
```

Das 122-Größenordnungen-Problem entsteht, weil die Standardphysik homogene
Vakuumenergie als physikalisch wirksam behandelt — was A5 ausschließt.

**Erfolgskriterium:** ✅ Erfüllt — Gradientenproblem-Reformulierung vollständig.

---

*RT-45 AP3 — DominicReneSchu/RFT — November 2026*
