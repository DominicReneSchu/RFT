# Simulation gekoppelter Oszillatoren

Interaktive Python-Simulation zweier gekoppelter harmonischer
Oszillatoren. Demonstriert Kopplungseffekte, Energieaustausch,
Resonanzerkennung und Energiebilanz im Rahmen der
Resonanzfeldtheorie (Axiome A1–A4).

<p align="center">
  <img src="animation.gif" alt="Gekoppelte Oszillatoren" width="800"/>
</p>

---

## Axiom-Bezug

| Axiom | Umsetzung |
|-------|-----------|
| A1 Schwingung | Zwei harmonische Oszillatoren mit ω₁, ω₂ |
| A2 Superposition | Überlagerung der Auslenkungen |
| A3 Resonanzbedingung | f₁/f₂ ≈ n/m wird live geprüft und angezeigt |
| A4 Kopplungsenergie | ε = exp(−α·\|f₁−f₂\|), E_res = π·ε·h·f |

---

## Grundformel (Axiom 4)

$$
E_{\text{res}} = \pi \cdot \varepsilon \cdot h \cdot f
$$

Der Kopplungsoperator ε = exp(−α·|f₁−f₂|) modelliert die
frequenzabhängige Kopplung: Maximum bei f₁ = f₂ (perfekte
Resonanz), exponentieller Abfall bei Frequenzdifferenz.

---

## Funktionen

* Numerische Lösung gekoppelter DGL (`solve_ivp`)
* Interaktive Live-Animation mit Spurverfolgung
* Resonanzerkennung (Axiom 3) mit visueller Anzeige
* Slider: Frequenzen, Kopplungsschärfe α, Toleranz, Geschwindigkeit
* Energieplot: kinetisch, potenziell, Kopplung, gesamt
* Kopplungsoperator ε und Resonanzenergien E_res(f₁), E_res(f₂)
* Resonanz-Divergenz |E_mech − E_res|
* Export: CSV und GIF

---

## Struktur

| Datei | Funktion |
|-------|----------|
| [`run.py`](run.py) | Einstiegspunkt, UI, Slider, Animation |
| [`parameters_and_functions.py`](parameters_and_functions.py) | Physik: ODE, Kopplungsoperator, Energie |
| [`animation.py`](animation.py) | Plot-Update, Energielinien |
| [`coupled_oscillators.py`](coupled_oscillators.py) | Minimalbeispiel (standalone) |
| [`export_csv.py`](export_csv.py) | CSV-Export |

---

## Ausführung

```bash
pip install numpy matplotlib scipy
python run.py
```

Standalone-Minimalbeispiel (ohne Slider):

```bash
python coupled_oscillators.py
```

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

## Querbestätigung innerhalb der RFT

Dieses Ergebnis bestätigt und wird bestätigt durch unabhängige Resultate aus anderen Bereichen:

| Ergebnis hier | Bestätigt durch | Bereich | Link |
|---|---|---|---|
| Energieaustausch bei Resonanz, ε = exp(−α·|f₁−f₂|) | Schrödinger-Simulation: quantenmechanisches Pendant, Fidelity = 1.000000000000 | Quantenmechanik | [→ Schrödinger](../schrödinger/README.md) |
| Nichtlineare Kopplung zweier Oszillatoren | Doppelpendel: nichtlineare Erweiterung derselben Kopplungslogik | Klassische Mechanik | [→ Doppelpendel](../doppelpendel/begleitkapitel_doppelpendel.md) |
| PCI und MI aus Kopplungslogik | Resonanzfeld-Simulation: PCI → MI zeigt direktionale Energieflusskontrolle | Feldtheorie | [→ Resonanzfeld](../resonanzfeld/simulation_resonanzfeldtheorie.md) |
| E_res = π·ε·h·f, klassische Kopplung | ResoCalc: Drehmoment als Spezialfall der Oszillatorkopplung | Ingenieurwesen | [→ ResoCalc](../../konzepte/ResoCalc/resocalc.md) |

> **Eine Gleichung — E = π·ε(Δφ)·ℏ·f — bestätigt über Quantenmechanik, Kosmologie, Kernphysik und Raumzeitgeometrie.**

---

⬅️ [zurück zur Übersicht](../../../README.md#simulationen)