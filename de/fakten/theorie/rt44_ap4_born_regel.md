# RT-44 AP4 — Born-Regel: Ableitung oder irreduzibles Postulat?

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** P(a) = |⟨a|ψ⟩|² aus ε-Struktur ableiten — oder als irreduzibles Postulat einordnen.

**Dies ist die stärkste offene Flanke von RT-44.**

**Ergebnis:** Die Born-Regel ist in der aktuellen RFT ein **irreduzibles Postulat**
(analog zu A5 und A8) — sie kann nicht allein aus ε(Δφ) abgeleitet werden.
Die RFT liefert jedoch eine strukturelle Motivation und eine konsistente Einbettung.

---

## 2. Zwei Ableitungsansätze

### Ansatz 1: Born-Regel als Kopplungsenergie

**Idee:** Der Energieübertrag bei einer Messung ist:
```
E_Messung = π · ε(Δφ_as) · ħ · f_as
```
wobei Δφ_as die Phasendifferenz zwischen System und Apparat ist.

Bei Projektion auf Eigenzustand |a⟩:
```
⟨E_Messung⟩ ∝ ε(Δφ_as) = cos²(Δφ_as/2)
```

**Problem:** ε ist eine Funktion der Phasendifferenz zwischen System und Apparat,
nicht von |⟨a|ψ⟩|². Es fehlt eine Verbindung zwischen der Phasenstruktur und
dem Skalarprodukt im Hilbertraum. Der Ansatz liefert die Form der Kopplungsstärke,
nicht die Wahrscheinlichkeit des Messergebnisses.

**Fazit:** Ansatz 1 ist eine **strukturelle Analogie**, keine Ableitung.

### Ansatz 2: Gleasons Theorem

**Gleasons Theorem (1957):** Sei H ein Hilbertraum der Dimension ≥ 3. Dann gilt:
Jedes normierte, additive Wahrscheinlichkeitsmaß auf den abgeschlossenen Unterräumen
von H hat die Form P(a) = Tr(ρ P_a) mit einem Dichteoperator ρ.

Für reine Zustände ρ = |ψ⟩⟨ψ|: P(a) = |⟨a|ψ⟩|² (Born-Regel).

**Verbindung zur RFT:** Die RFT-Zustände sind Resonanzmoden in einem Funktionenraum
(A1). Wenn dieser Funktionenraum Hilbertraum-Struktur hat (was die Schrödinger-
Simulation mit Fidelity = 1,0 bestätigt), dann erzwingt Gleasons Theorem die Born-Regel.

**Einschränkung:** Gleasons Theorem setzt die Hilbertraum-Struktur voraus. In der RFT
wird diese durch A2 (lineare Superposition) + A4 (ħ als Wirkungsquantum) impliziert —
aber nicht explizit als Axiom formuliert.

---

## 3. Einordnung: Warum Born kein Korollar von ε ist

**Strukturelle Lücke:** ε(Δφ) = cos²(Δφ/2) beschreibt die **Stärke** der Kopplung
zwischen zwei Systemen — nicht die **Wahrscheinlichkeit** eines Messergebnisses.

Der Unterschied:
- ε = Kopplungseffizienz im Resonanzfeld (kontinuierlich, deterministische Dynamik)
- P(a) = Wahrscheinlichkeit bei Messung (stochastisch, aus Superposition)

Die Verbindung zwischen beiden würde eine **Brücke zwischen Dynamik und Statistik**
erfordern, die in A1–A7 nicht explizit enthalten ist.

**Analogie zu A5 und A8:**
- A5: Vektorialität der Energie — irreduzibles Postulat (RT-36)
- A8: Kopplungswellengeschwindigkeit c — irreduzibles Postulat (RT-41)
- **Born-Regel:** irreduzibles Postulat — hier analog als A_Born zu formulieren

---

## 4. Formulierung als A_Born (Entwurf)

**Axiom A_Born (Entwurf):**
> Die Messwahrscheinlichkeit des Zustands |a⟩ bei einer Projektion aus dem
> RFT-Resonanzfeld |ψ⟩ ist P(a) = |⟨a|ψ⟩|². Dies ist das einzige mit
> A2 (Superposition) konsistente Wahrscheinlichkeitsmaß (Gleasons Theorem).

**Status:** A_Born ist nicht aus A1–A7 ableitbar. Es ist das messtheoretische Bindeglied
zwischen der deterministischen Resonanzfelddynamik und dem stochastischen Messprozess.

---

## 5. Konsistenz mit ε-Struktur

Obwohl Born kein Korollar von ε ist, sind beide konsistent:

| Situation | ε | P(a) |
|-----------|---|------|
| Resonanz (Δφ=0, ε=1) | 1 | P(a) ≡ 1 für Eigenzustand |a⟩ = |ψ⟩ |
| Entkopplung (Δφ=π, ε=0) | 0 | P(a) = 0 (kein Energieübertrag) |
| Superposition | ε(Δφ) | P(a) = |⟨a|ψ⟩|² (A_Born) |

Die Born-Regel und ε ergänzen sich: ε beschreibt die Kopplungsdynamik,
Born beschreibt die Messstatistik.

---

## 6. Ergebnis

**Born-Regel ist irreduzibles Postulat A_Born in der RFT.**

Sie kann strukturell durch Gleasons Theorem motiviert werden (Hilbertraum + A2 → Born),
aber nicht aus der ε-Kopplungsstruktur allein abgeleitet werden.

**Ehrliche Einschätzung:** Das ist kein Scheitern der RFT. Die Born-Regel ist in der
Standard-QM ebenfalls ein Postulat — Gleasons Theorem erklärt ihre Form, aber nicht
ihre Notwendigkeit. Die RFT befindet sich hier in derselben Lage wie die SRT (c als
Postulat in A8) oder die Vektorialität (A5).

**Erfolgskriterium:** ✅ Erfüllt — klare Aussage: irreduzibles Postulat A_Born,
mit Motivation durch Gleasons Theorem und konsistenter Einbettung in ε-Struktur.

---

*RT-44 AP4 — DominicReneSchu/RFT — November 2026*
