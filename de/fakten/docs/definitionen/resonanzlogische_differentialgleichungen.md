# Resonanzlogische Differentialgleichungen

*Dominic-René Schu, 2025/2026*

> Nicht die Differentialgleichung beschreibt das System, sondern
> das System erzeugt ihre Gleichung durch Resonanzkopplung.

---

## 1. Motivation

**Klassischer Ansatz:**
- Differentialgleichungen (DGL) als vorgegebene Modelle
- Auswahl phänomenologisch (Erfahrung, Beobachtung)
- Jede DGL-Klasse wird separat behandelt

**Resonanzfeldansatz:**
- Die DGL entsteht als Projektion einer allgemeinen
  Resonanzkopplungsrelation
- Klassische DGL-Typen sind Spezialfälle dieser Relation
- Dynamik = Kopplung aller relevanten Moden im Resonanzfeld

---

## 2. Axiomatische Grundlage

Die resonanzlogische Differentialgleichung (rDGL) baut auf
folgenden Axiomen der RFT auf
(siehe [axiomatische Grundlegung](axiomatische_grundlegung.md)):

- **Axiom 1 (Universelle Schwingung):** Jede Entität besitzt
  periodische Schwingungsmoden → der Zustand x(t) ist
  schwingungsfähig
- **Axiom 2 (Superposition):** Moden überlagern sich linear
  → die Feldstruktur Φ ist Superposition aller Kopplungen
- **Axiom 3 (Resonanzbedingung):** Kopplung tritt bei rationalen
  Frequenzverhältnissen auf → selektive Kopplung zwischen Moden
- **Axiom 4 (Kopplungsenergie):** E = π·ε·h·f → die
  Kopplungsstärke bestimmt die Energetik der Dynamik
- **Axiom 7 (Invarianz):** Die Kopplungsstruktur ist
  skalierungsinvariant → die rDGL gilt auf allen Zeitskalen

Zusätzlich gilt die interpretative Erweiterung E2
(Resonanz-Inklusion, siehe axiomatische Grundlegung §5.2):
Alle Systemanteile — explizit und implizit — sind durch
Resonanzkopplung verschränkt.

---

## 3. Allgemeine Form der rDGL

### 3.1 Urform

```
    R(x, x', x'', t, Φ) = 0
```

- **x:** Systemzustand
- **x', x'':** Zeitliche Ableitungen (Antwortverhalten)
- **t:** Evolutionsparameter (Zeit, Raum, Zyklus, Index)
- **Φ:** Feldstruktur (Kopplungen, Rückwirkung, Topologie,
  Gedächtnis, Störgrößen)

### 3.2 Erweiterte Form

```
    x'' + α(x,t)·x' + β(x,t) + ∫ γ(x,τ) dτ + η(x,x',t,Φ) = 0
```

| Term | Bedeutung | Axiom-Bezug |
|------|-----------|-------------|
| α(x,t)·x' | Dämpfung / Selbstresonanz | A4 (Kopplungseffizienz ε) |
| β(x,t) | Nichtlineare Rückkopplung | A3 (Resonanzbedingung) |
| ∫ γ(x,τ) dτ | Gedächtniseffekte (Hysterese) | A6 (Informationsfluss) |
| η(x,x',t,Φ) | Feldkopplung (extern) | A2 (Superposition), A7 (Invarianz) |

Die erweiterte Form enthält alle klassischen DGL-Typen als
Spezialfälle (siehe §4).

---

## 4. Ableitungsbaum: Klassische DGLs als Projektionen

```
R(x, x', x'', t, Φ) = 0
├── Harmonischer Oszillator
│   └── x'' + ω²x = 0                [α, β, γ, η = 0]
├── Gedämpfter Oszillator
│   └── x'' + 2γ·x' + ω²x = 0       [α ≠ 0]
├── Nichtlinearer Oszillator (Van-der-Pol)
│   └── x'' − μ(1−x²)·x' + x = 0    [α = −μ(1−x²), β = x]
├── Schwellen-/Schaltmodell (FitzHugh-Nagumo)
│   └── Gekoppeltes System             [Φ enthält Schwelle]
├── Stochastische DGL
│   └── dx = f(x,t)dt + g(x,t)dW_t   [Φ enthält Rauschen]
├── Partielle DGL (Diffusion/Wellen)
│   └── ∂_t x = D·∇²x + f(x)        [Φ enthält Raumkopplung]
├── Netzwerkdynamik (gekoppelte Systeme)
│   └── x'_i = F_i(x, Φ)            [Φ = Kopplungsmatrix]
└── Gedächtnismodell (Hysterese)
    └── x'' + ∫ γ(x,τ) dτ = 0       [γ ≠ 0]
```

---

## 5. Projektionstabelle

| Klassischer Typ | Spezialfall der rDGL | Aktive Terme | Resonanzbemerkung |
|-----------------|---------------------|-------------|-------------------|
| Harmonischer Oszillator | x'' + ω²x = 0 | Keine | Reine Schwingung (A1) |
| Gedämpfter Oszillator | x'' + 2γ·x' + ω²x = 0 | α | Kopplung mit Dissipation (ε < 1) |
| Van-der-Pol | x'' − μ(1−x²)·x' + x = 0 | α, β | Amplitudenabhängige Kopplung |
| FitzHugh–Nagumo | Gekoppeltes System | α, β, Φ | Schwellenresonanz |
| Stochastische DGL | dx = f·dt + g·dW_t | η | Rauschfeld in Φ |
| Partielle DGL | ∂_t x = D·∇²x + f(x) | η | Raumkopplung in Φ |
| Netzwerkdynamik | x'_i = F_i(x, Φ) | η | Topologie als Kopplungsmatrix |
| Gedächtnismodell | x'' + ∫ γ(x,τ) dτ = 0 | γ | Nichtlokale Kopplung (A6) |

---

## 6. Physikalische Interpretation

### 6.1 Die rDGL als Kopplungsrelation

Die Urform R(x, x', x'', t, Φ) = 0 ist keine einzelne Gleichung,
sondern eine **Kopplungsrelation**: Sie beschreibt die Bedingung,
unter der ein Zustand x(t) mit dem Resonanzfeld Φ konsistent ist.

Klassische DGLs entstehen als **Projektionen** dieser Relation
durch Einschränkung der Feldstruktur Φ:

```
    lim_{Φ → 0} R(x, x', x'', t, Φ) = klassische DGL
```

### 6.2 Verbindung zur Kopplungseffizienz

Der Dämpfungsterm α ist direkt mit der Kopplungseffizienz ε
verknüpft (Axiom 4):

- α = 0 entspricht ε = 1 (perfekte Kopplung, ungedämpft)
- α > 0 entspricht ε < 1 (Energieverlust durch Phasenverschiebung)
- α < 0 entspricht Energiezufuhr (angetriebenes System)

### 6.3 Verbindung zur Kopplungsdynamik

Die zeitliche Entwicklung der Kopplungsstärke K_ij
(axiomatische Grundlegung §4.3):

```
    dK_ij/dt = α · G(f_i/f_j) · cos(Δφ_ij) − β · K_ij
```

ist selbst ein Spezialfall der rDGL mit x = K_ij und
Φ = {Frequenzen, Phasen, Dämpfung}.

---

## 7. Anwendungen

| Bereich | Beispiel | rDGL-Projektion |
|---------|----------|----------------|
| Physik | Erzwungene Schwingung | α, η ≠ 0 |
| Biologie | Neuronale Erregung | FitzHugh-Nagumo (Schwelle in Φ) |
| Technik | Adaptive Regelung | Netzwerkdynamik (Φ = Regelstruktur) |
| Finanzmärkte | Preisdynamik | Stochastische DGL + Gedächtnis (γ, η) |
| KI/Robotik | Kontextadaptive Netze | Netzwerkdynamik + Lernen (Φ adaptiv) |

---

## 8. Ausblick

### 8.1 Kurznotation

Einführung einer kompakten Notation für rDGL-Typen:

```
    R_{α,β,γ,η}^{Φ}
```

Beispiele:
- R_{0,0,0,0}^{0} = Harmonischer Oszillator
- R_{α,0,0,0}^{0} = Gedämpfter Oszillator
- R_{α,β,0,η}^{Φ} = Allgemeine Netzwerkdynamik

### 8.2 Limeslogik

Analyse klassischer Gleichungen als Grenzfälle:

```
    lim_{Φ → 0} R = klassische DGL
    lim_{γ → 0} R = gedächtnisfreie DGL
    lim_{η → 0} R = feldfreie DGL
```

### 8.3 Implementierung

Symbolische Implementierung der rDGL-Struktur mit automatischen
Projektionen (Python-Modul):

```python
    R = ResonanzDGL(alpha=0, beta=0, gamma=0, eta=0, Phi=None)
    R.project("harmonisch")      # → x'' + ω²x = 0
    R.project("van_der_pol")     # → x'' − μ(1−x²)x' + x = 0
    R.project("netzwerk", Phi=K) # → x'_i = F_i(x, K)
```

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)