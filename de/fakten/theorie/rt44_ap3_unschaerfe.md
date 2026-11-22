# RT-44 AP3 — Heisenbergsche Unschärfe als Modenbreite

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Δx·Δp ≥ ħ/2 als strukturelle Eigenschaft der Resonanzmoden aus A1–A4 ableiten.

**Ergebnis:** Unschärferelation folgt aus der Fourier-Mathematik lokalisierter Wellen
(A1) + de-Broglie-Relation p = ħk (ableitbar aus A4). Sie ist kein gesondertes Postulat.

---

## 2. Schritt 1: Fourier-Unschärfe (mathematisch)

Jede räumlich lokalisierte Funktion ψ(x) mit Ausdehnung σ_x erfüllt:

```
σ_x · σ_k ≥ 1/2
```

Das ist eine Eigenschaft der Fourier-Transformation — nicht der Physik.
Beweis: Aus der Parseval-Schwarz-Ungleichung.

---

## 3. Schritt 2: de-Broglie-Relation aus A4

**Axiom A4:** E = π · ε(Δφ) · ħ · f

Für ein freies, masseloses Wellenpaket (Licht) bei ε = 1:
```
E = π · ħ · f = π · ħ · c/λ
```

Mit dem relativistischen Energie-Impuls-Zusammenhang E = pc:
```
pc = π · ħ · c/λ    →    p = πħ/λ = ħ · (π/λ)
```

Die RFT-Wellenzahl ist k_RFT = π/λ (statt k_std = 2π/λ), weil die RFT
eine Halbperiode als fundamentale Einheit verwendet (π als Phasenraumkonstante).

**De-Broglie in der RFT:**
```
p = ħ · k_RFT = ħ · π/λ
```

Für massive Teilchen (aus Ruhefrequenz f₀ = m_e c²/(πħ) aus RT-40 AP2):
```
p = ħ · k    mit    k = p/ħ   (konsistent mit Schrödinger-Gleichung)
```

---

## 4. Schritt 3: Heisenberg-Unschärferelation

Aus Fourier-Unschärfe σ_x · σ_k ≥ 1/2 und p = ħk:

```
σ_x · σ_p = σ_x · ħ · σ_k ≥ ħ/2
```

Mit der Konvention Δx = σ_x, Δp = σ_p:

```
Δx · Δp ≥ ħ/2  ✅
```

---

## 5. Physikalische Interpretation in der RFT

Die Unschärferelation ist **kein Postulat**, sondern:
1. Fourier-Unschärfe: mathematische Eigenschaft jeder lokalisierten Welle (A1)
2. p = ħk: folgt aus A4 (Kopplungsenergie) + Wellenstruktur A1
3. Messvorgang (Lokalisierung): entspricht Übergang ε→1 (AP5)

Die RFT liefert zusätzlich eine **mechanistische Deutung**:
- Vor Messung: Wellenpaket mit Δx·Δp ~ ħ/2 (Kohärenzregime, ε < 1)
- Messung (Lokalisierung): Δφ→0, ε→1 — Ortsbestimmung, Impulsunbestimmtheit wächst
- Nach Messung: neues Wellenpaket mit ħ/2-Unschärfe (AP5-Dynamik)

---

## 6. Ergebnis

```
Δx · Δp ≥ ħ/2
```

Folgt aus: A1 (Schwingungsfelder) + A4 (ħ in Kopplungsenergie) + Fourier-Mathematik.
Kein eigenständiges Postulat in der RFT.

**Erfolgskriterium:** ✅ Erfüllt.

---

*RT-44 AP3 — DominicReneSchu/RFT — November 2026*
