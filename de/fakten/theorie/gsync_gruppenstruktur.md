# G_sync — Gruppenstruktur und Invarianzbeweise (RT-02)

*Dominic René Schu, August 2026*
*Status: Abgeschlossen (Aug 2026)*

---

## Übersicht

Dieses Dokument enthält den vollständigen gruppentheoretischen Beweis zu RT-02
in vier Stufen:

1. [Stufe 1 — Gruppenstruktur von G_sync](#stufe-1--gruppenstruktur-von-g_sync)
2. [Stufe 2 — Invarianz von G(fᵢ/fⱼ) unter G_sync](#stufe-2--invarianz-von-gfᵢfⱼ-unter-g_sync)
3. [Stufe 3 — Invarianz von ε(Δφ) und Eindeutigkeit von cos²(Δφ/2)](#stufe-3--invarianz-von-εδφ-und-eindeutigkeit-von-cos²δφ2)
4. [Stufe 4 — Irreduzible Darstellungen von G_sync](#stufe-4--irreduzible-darstellungen-von-g_sync)

**Verwandte Dateien:**
- Symbolische Verifikation: `simulationen/rt02/rt02_gsync_verification.py`
- Axiom A7: `../docs/definitionen/axiomatische_grundlegung.md` §A7
- Offene Forschungsaufgaben: `../../../../RESEARCH_TASKS.md` (RT-02)
- RT-01b Stufe 3 (Potenzial-Unabhängigkeit): `wirkungsintegral_pi_herleitung.md` §4.4

---

## Stufe 1 — Gruppenstruktur von G_sync

### Definition

Eine synchrone Transformation ist eine Abbildung

```
T(λ, φ₀, a, b) : (fᵢ, φᵢ, t) ↦ (λ fᵢ, φᵢ + φ₀, at + b)
```

mit Parametern λ ∈ ℝ⁺, φ₀ ∈ [0, 2π), a ∈ ℝ⁺, b ∈ ℝ.

Die Menge aller solcher Transformationen heißt G_sync.

### Verknüpfung

Die Komposition zweier Transformationen T₁ = T(λ₁, φ₀¹, a₁, b₁) und
T₂ = T(λ₂, φ₀², a₂, b₂) ergibt:

```
(T₁ ∘ T₂)(fᵢ, φᵢ, t)
  = T₁(λ₂ fᵢ, φᵢ + φ₀², a₂t + b₂)
  = (λ₁λ₂ fᵢ,  φᵢ + φ₀² + φ₀¹,  a₁(a₂t + b₂) + b₁)
  = (λ₁λ₂ fᵢ,  φᵢ + (φ₀¹ + φ₀²),  (a₁a₂)t + (a₁b₂ + b₁))
```

Also: T₁ ∘ T₂ = T(λ₁λ₂,  φ₀¹ + φ₀² mod 2π,  a₁a₂,  a₁b₂ + b₁).

### Beweis der vier Gruppenaxiome

**G1 — Abgeschlossenheit.**
Sei T₁, T₂ ∈ G_sync. Dann ist λ₁λ₂ ∈ ℝ⁺, (φ₀¹ + φ₀²) mod 2π ∈ [0, 2π),
a₁a₂ ∈ ℝ⁺, und a₁b₂ + b₁ ∈ ℝ. Damit ist T₁ ∘ T₂ ∈ G_sync. □

**G2 — Assoziativität.**
Für T₁, T₂, T₃ ∈ G_sync gilt komponentenweise:

- Frequenz: (λ₁λ₂)λ₃ = λ₁(λ₂λ₃)   [Assoziativität in ℝ⁺]
- Phase: ((φ₀¹ + φ₀²) + φ₀³) = (φ₀¹ + (φ₀² + φ₀³)) mod 2π   [Assoziativität in ℝ/2πℤ]
- Zeit — a-Komponente: (a₁a₂)a₃ = a₁(a₂a₃)   [Assoziativität in ℝ⁺]
- Zeit — b-Komponente:
  (T₁ ∘ T₂) ∘ T₃ liefert b-Parameter: (a₁a₂)b₃ + (a₁b₂ + b₁)
                                      = a₁a₂b₃ + a₁b₂ + b₁
  T₁ ∘ (T₂ ∘ T₃) liefert b-Parameter: a₁(a₂b₃ + b₂) + b₁
                                      = a₁a₂b₃ + a₁b₂ + b₁  ✓

Damit ist G_sync assoziativ. □

**G3 — Neutralelement.**
Setze T_e = T(1, 0, 1, 0). Dann:

```
(T_e ∘ T)(λ, φ₀, a, b) = T(1·λ, 0+φ₀, 1·a, 1·b+0) = T(λ, φ₀, a, b)  ✓
(T ∘ T_e)(λ, φ₀, a, b) = T(λ·1, φ₀+0, a·1, a·0+b) = T(λ, φ₀, a, b)  ✓
```

T_e ist das neutrale Element. □

**G4 — Inverses.**
Für T = T(λ, φ₀, a, b) setze T⁻¹ = T(1/λ, −φ₀, 1/a, −b/a). Dann:

```
T ∘ T⁻¹ = T(λ·(1/λ), φ₀+(−φ₀), a·(1/a), a·(−b/a)+b)
         = T(1, 0, 1, −b+b)
         = T(1, 0, 1, 0) = T_e  ✓

T⁻¹ ∘ T = T((1/λ)·λ, (−φ₀)+φ₀, (1/a)·a, (1/a)·b+(−b/a))
         = T(1, 0, 1, b/a − b/a)
         = T_e  ✓
```

Jedes Element besitzt ein Inverses. □

### Gruppenstruktur: direktes Produkt

Die Parameterkomposition entkoppelt vollständig:

| Komponente | Menge | Gruppe |
|------------|-------|--------|
| Frequenzskalierung λ | ℝ⁺ | (ℝ⁺, ·) ≅ (ℝ, +) via log |
| Phasenverschiebung φ₀ | ℝ/2πℤ | U(1) |
| Affine Zeittransformation (a, b) | ℝ⁺ × ℝ | Aff⁺(ℝ) |

**Ergebnis:**

```
G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ)
```

Dabei ist Aff⁺(ℝ) = { t ↦ at + b | a > 0, b ∈ ℝ } die orientierungserhaltende
affine Gruppe der reellen Geraden. Aff⁺(ℝ) ist nicht abelsch:

```
(a₁, b₁) ∘ (a₂, b₂) = (a₁a₂, a₁b₂ + b₁)  ≠  (a₁a₂, a₂b₁ + b₂)  (im Allgemeinen)
```

G_sync ist daher **nicht abelsch** (wegen des Aff⁺(ℝ)-Faktors), aber auflösbar
(da Aff⁺(ℝ) auflösbar ist).

---

## Stufe 2 — Invarianz von G(fᵢ/fⱼ) unter G_sync

### Gewichtungsfunktion

Die Resonanzgewichtung ist definiert als:

```
G(fᵢ/fⱼ) = exp(−(|fᵢ/fⱼ − m/n| / δ)²)
```

mit Resonanzquantenzahlen m, n ∈ ℤ⁺ und Breite δ > 0.

### Invarianz unter Frequenzskalierung

Unter T : fᵢ ↦ λfᵢ gilt:

```
G(T(fᵢ)/T(fⱼ)) = G(λfᵢ/λfⱼ) = G(fᵢ/fⱼ)
```

weil λ sich im Quotienten herauslöscht. **G(fᵢ/fⱼ) ist exakt invariant unter
der Frequenzskalierung λ ∈ ℝ⁺_×.** □

### Invarianz unter Phasenverschiebung

Die Gewichtung G hängt nur von Frequenzen ab, nicht von Phasen. Damit:

```
G(fᵢ/fⱼ) invariant unter φᵢ ↦ φᵢ + φ₀  □
```

### Nicht-Invarianz unter affiner Zeittransformation

Die Frequenzen fᵢ sind (im stationären Sinne) unabhängig von der globalen
Zeitparametrisierung t ↦ at + b, solange keine zeitabhängige Frequenzmodulation
vorliegt. **Im stationären Resonanzmodell (fᵢ = const) gilt:**

```
G(fᵢ/fⱼ) invariant unter t ↦ at + b  □  (stationär)
```

**Nicht-stationärer Fall:** Wenn fᵢ = fᵢ(t) zeitabhängig ist (z.B. chirped
signals), führt t ↦ at zu fᵢ(at) ≠ λ fᵢ(t), und G ist i.A. nicht mehr invariant.

### Teilaussagen von A7 — beweisbar vs. postuliert

| Teilaussage | Status |
|-------------|--------|
| G(fᵢ/fⱼ) invariant unter λ-Skalierung | **Bewiesen** (algebraisch, exakt) |
| G(fᵢ/fⱼ) invariant unter Phasenshift φ₀ | **Bewiesen** (trivial, fᵢ unabhängig von φ) |
| G(fᵢ/fⱼ) invariant unter t ↦ at+b (stationär) | **Bewiesen** (stationäres Modell) |
| G(fᵢ/fⱼ) invariant unter t ↦ at+b (dynamisch) | **Postulat** — nur für zeitunabhängige fᵢ |
| Skalierung über CMB/Kern/Finanzdomänen | **Analogie** — kein formaler Beweis |

**Konsequenz:** A7 gilt vollständig und algebraisch nachweisbar für den
Frequenzquotient-Teil G(fᵢ/fⱼ) im stationären Regime. Die Domänenübertragung
(CMB ↔ Kernphysik ↔ Finanzmärkte) bleibt ein motiviertes Postulat.

---

## Stufe 3 — Invarianz von ε(Δφ) und Eindeutigkeit von cos²(Δφ/2)

### Direkte Invarianz

Für T : φᵢ ↦ φᵢ + φ₀ gilt:

```
T(φᵢ) − T(φⱼ) = (φᵢ + φ₀) − (φⱼ + φ₀) = φᵢ − φⱼ = Δφᵢⱼ
```

Damit: ε(T(φᵢ) − T(φⱼ)) = ε(Δφᵢⱼ) für **jede** Funktion ε, die nur von der
Phasendifferenz abhängt. Die Invarianz ist eine Eigenschaft der Argumentstruktur,
nicht der konkreten Funktion ε.

### Charakterisierung der invarianten Funktionenklasse

**Definition:** Sei F die Klasse aller Funktionen f : [0, 2π] → [0, 1] mit:

1. f(0) = 1    (vollständige Kopplung bei Gleichphase)
2. f(π) = 0    (Gegenphasen-Entkopplung)
3. f(2π) = 1   (Periodizität)
4. f monoton fallend auf [0, π]   (eindeutige Kopplungsstärke)
5. f(Δφ) = f(−Δφ)   (Parität — Kopplung hängt nicht von Vorzeichen der Differenz ab)

Alle f ∈ F sind unter Phasenverschiebungen invariant (s.o.).

### Ist cos²(Δφ/2) die eindeutige Funktion in F?

**Nein — die Klasse F ist unendlich groß.**

Gegenbeispiel: Für beliebiges n ∈ ℕ mit n ≥ 1 erfüllt

```
fₙ(Δφ) = cos²ⁿ(Δφ/2)
```

alle fünf Bedingungen. Insbesondere:

- f₁(Δφ) = cos²(Δφ/2)       [Standard-RFT]
- f₂(Δφ) = cos⁴(Δφ/2)
- f₃(Δφ) = cos⁶(Δφ/2)

Weiteres Beispiel: fₛ(Δφ) = (1 + cos(Δφ))/2 = cos²(Δφ/2) — dies ist dieselbe
Funktion, aber als trigonometrisches Polynom geschrieben.

Dagegen erfüllt sin⁴(Δφ/2) die Bedingungen **nicht**, weil:
sin⁴(0) = 0 ≠ 1  (verletzt Bedingung 1).

### Zusatzbedingung: Eindeutigkeitscharakterisierung

cos²(Δφ/2) ist innerhalb von F **eindeutig** ausgezeichnet durch folgende
Kombination von Zusatzeigenschaften:

**Z1 — Minimalität im Fourier-Sinn:**
cos²(Δφ/2) = (1 + cos(Δφ))/2 ist das einzige nicht-triviale trigonometrische
Polynom in F mit **minimaler Fourier-Entwicklung** (nur die Terme k=0 und k=1).
Jede andere Funktion in F, die über ein trigonometrisches Polynom darstellbar ist,
benötigt Terme höherer Ordnung (k ≥ 2).

**Z2 — Darstellungstheorie von U(1):**
Die irreduziblen unitären Darstellungen von U(1) sind e^(ikφ) für k ∈ ℤ.
Die reellen Invarianten (unter φ → −φ) sind 1 und cos(kΔφ) für k ∈ ℕ.
Eine Funktion f ∈ F, die ausschließlich zur irreduziblen Darstellung k=1
von U(1) gehört (neben dem trivialen k=0), ist zwingend:

```
f(Δφ) = α + β cos(Δφ),  mit f(0)=1, f(π)=0:
  α + β = 1
  α − β = 0
  ⟹ α = β = 1/2
  ⟹ f(Δφ) = (1 + cos(Δφ))/2 = cos²(Δφ/2)
```

**Ergebnis Stufe 3:**

> cos²(Δφ/2) ist die **eindeutig** ausgezeichnete Funktion in F, die ausschließlich
> zur fundamentalen (k=1) und trivialen (k=0) irreduziblen Darstellung von U(1)
> gehört.

Jede andere Funktion in F (z.B. cos⁴(Δφ/2)) mischt höhere irreduzible
Darstellungen (k=2, 4, …) ein und ist damit nicht durch die minimale
Darstellungsstruktur erzwungen.

### Verbindung zu RT-01b Stufe 3

RT-01b Stufe 3 fragte: Ist das Potential V(φ) = cos²(φ/2) unabhängig von der
speziellen Wahl der Potenzialklasse?

**Antwort (RT-02 Stufe 3):**
V(φ) = cos²(φ/2) ist nicht frei gewählt, sondern gruppentheoretisch ausgezeichnet:
Es ist die eindeutige Funktion, die zur k=1-Darstellung von U(1) ⊂ G_sync gehört
und die Randbedingungen f(0)=1, f(π)=0 erfüllt. Die Potenzial-Unabhängigkeit
in RT-01b gilt daher nicht für beliebige normierte Potenziale, sondern erklärt,
warum genau cos²(φ/2) das natürliche Potential ist: Es minimiert die
Darstellungsordnung.

**RT-01b Stufe 3: Durch RT-02 Stufe 3 geschlossen.**

---

## Stufe 4 — Irreduzible Darstellungen von G_sync

### Lie-Algebra von G_sync

G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) ist eine reelle Lie-Gruppe der Dimension 4.
Die Lie-Algebra g_sync = Lie(G_sync) besitzt die Basis {D, L, H, P} mit
Erzeugern:

| Erzeuger | Wirkung | Physikalische Interpretation |
|----------|---------|------------------------------|
| D | fᵢ ↦ fᵢ + εfᵢ (Dilatation) | Frequenzskalierung |
| L | φᵢ ↦ φᵢ + ε (Translation) | Phasenverschiebung |
| H | t ↦ t + εt (Skalierung) | Zeitstreckung |
| P | t ↦ t + ε (Translation) | Zeitverschiebung |

**Kommutatoren der Lie-Algebra:**

```
[D, L] = 0      [D, H] = 0      [D, P] = 0
[L, H] = 0      [L, P] = 0
[H, P] = P      (einziger nicht-trivialer Kommutator)
```

Der nicht-triviale Kommutator [H, P] = P spiegelt die Nicht-Abelschheit von
Aff⁺(ℝ) wider. g_sync ist auflösbar (da [g, g] = span{P} abelsch ist).

### Irreduzible Darstellungen

Da G_sync = ℝ⁺_× × U(1) × Aff⁺(ℝ) direktes Produkt ist, faktorisiert jede
irreduzible Darstellung:

```
π = π_D ⊗ π_L ⊗ π_Aff
```

#### Darstellungen von ℝ⁺_× (Frequenzskalierung)

Alle irreduziblen unitären Darstellungen von (ℝ⁺, ·) sind Charaktere:

```
χ_s : λ ↦ λ^(is),  s ∈ ℝ
```

(Unitär auf L²(ℝ⁺, dλ/λ); Hauptserienparameter s ∈ ℝ)

Für physikalische Anwendungen relevant: s = 0 (trivialer Charakter, skalare
Größen) und s ≠ 0 (frequenztransformierende Größen).

#### Darstellungen von U(1) (Phasenverschiebung)

```
χ_k : φ₀ ↦ e^(ikφ₀),  k ∈ ℤ
```

- k = 0: triviale Darstellung (phaseninvariante Größen)
- k = 1: fundamentale Darstellung (Kopplungseffizienz ε)
- k = 2, 3, …: höhere harmonische Terme

#### Darstellungen von Aff⁺(ℝ) (affine Zeitgruppe)

Aff⁺(ℝ) besitzt zwei Klassen irreduzibler unitärer Darstellungen:

**Eindimensionale Darstellungen (Charaktere):**
```
χ_α : (a, b) ↦ a^α,  α ∈ ℂ
```
Diese wirken trivial auf b (Zeitverschiebung).

**Unendlichdimensionale irreduzible Darstellungen:**
Auf L²(ℝ, dt) wirkt Aff⁺(ℝ) durch
```
(π(a,b) ψ)(t) = a^(1/2) ψ(at + b)
```
Diese Darstellung ist irreduzibel und unitär — sie entspricht der
Wavelet-Transformation.

### Darstellungstabelle G_sync

| Physikalische Größe | D-Darst. | L-Darst. | Aff-Darst. | Transformationsverhalten |
|---------------------|----------|----------|------------|--------------------------|
| ε(Δφ) | s=0 (skalar) | k=1 | χ₀ (skalar) | invariant unter D, H, P; k=1 unter L |
| G(fᵢ/fⱼ) | s=0 (skalar) | k=0 | χ₀ (skalar) | vollständig invariant |
| Kᵢⱼ (Kopplungsmatrix) | s=0 | k=1 | χ₀ | wie ε |
| E (Kopplungsenergie) | s=0 | k=0 | χ₀ | vollständig invariant |
| fᵢ (Frequenz) | s=1 (fundamental) | k=0 | χ₁ | kovariante Skalierung |
| t (Zeit) | s=0 | k=0 | Wavelet-Darst. | Zeitparameter |

### Quantisierungsbedingung

Die irreduziblen Darstellungen von U(1) sind durch k ∈ ℤ parametrisiert.
Die physikalische Forderung, dass ε(Δφ) reell und positiv ist, schränkt k ein:

- ε muss reellwertig sein: k und −k treten paarweise auf
- ε muss ε(0) = 1, ε(π) = 0 erfüllen: nur k=1 (fundamentale Darstellung)

Damit folgt aus der Darstellungsstruktur von U(1) ⊂ G_sync:

> Die Resonanzquantenzahlen m, n ∈ ℤ⁺ (A3) sind genau die Werte, bei denen
> der Frequenzquotient fᵢ/fⱼ = m/n unter der fundamentalen Darstellung von
> ℝ⁺_× invariant ist. Die Quantisierung fᵢ/fⱼ ∈ ℚ ist damit eine direkte
> Konsequenz der Darstellungsstruktur von G_sync.

---

## Zusammenfassung der Ergebnisse

| Stufe | Frage | Ergebnis |
|-------|-------|---------|
| 1 | Ist G_sync eine Gruppe? | **Ja** — algebraisch bewiesen (alle vier Axiome) |
| 1 | Welche Struktur hat G_sync? | G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) |
| 2 | G(fᵢ/fⱼ) invariant? | **Ja** (unter λ und φ₀); stationäres Zeitmodell |
| 2 | Welche A7-Teile sind Postulate? | Domänenübertragung CMB/Kern/Finanzen |
| 3 | ε(Δφ) invariant? | **Ja** — für alle Funktionen der Phasendifferenz |
| 3 | cos²(Δφ/2) eindeutig? | **Ja** — innerhalb der k=1-Darstellung von U(1) |
| 3 | RT-01b Stufe 3 geschlossen? | **Ja** — Potential gruppentheoretisch erzwungen |
| 4 | Irreduzible Darstellungen? | Tabelle oben; Quantisierung fᵢ/fⱼ ∈ ℚ aus G_sync |

---

## Verweise

- `simulationen/rt02/rt02_gsync_verification.py` — Symbolische Verifikation (SymPy)
- `../docs/definitionen/axiomatische_grundlegung.md` §A7 — Axiomformulierung
- `wirkungsintegral_pi_herleitung.md` §4.4 — RT-01b Stufe 3
- `../../../../RESEARCH_TASKS.md` — RT-02 Gesamtstatus
- `../../../../PEER_REVIEW_READINESS.md` — Peer-Review-Bereitschaft
