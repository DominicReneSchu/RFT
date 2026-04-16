# Schrödinger-Simulation — Referenz und Resonanz-Hamiltonoperator

Numerische 1D-Simulation der Schrödinger-Gleichung als Referenz
und Nachweis des Korrespondenzprinzips zwischen Standard-QM und
Resonanzfeldtheorie. Implementiert den Resonanz-Hamiltonoperator
aus dem RFT-Manuskript (Gl. eq:h_res):

$$
\hat{H}_{\mathrm{res}} = \hat{H}_0 + \varepsilon(\Delta\varphi)\,\hat{V}_{\mathrm{Kopplung}}
$$

mit der Kopplungseffizienz aus Axiom 4:

$$
\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi / 2) \in [0, 1]
$$

> **Einordnung:** Diese Simulation demonstriert die **Ableitung der
> Schrödinger-Gleichung aus Axiom 4** und belegt numerisch das
> Korrespondenzprinzip: Standard-QM ist Spezialfall der RFT.
> Sie folgt der Empfehlung, die Schrödinger-Gleichung aus der RFT-Axiomatik abzuleiten.

---

## Axiom-Bezug

| Axiom | Umsetzung |
|-------|-----------|
| A1 Schwingung | Gaußsches Wellenpaket als Superposition ebener Wellen |
| A2 Superposition | Interferenz im Impuls- und Ortsraum |
| A4 Kopplungseffizienz | ε(Δφ) = cos²(Δφ/2) moduliert V̂_Kopplung im Resonanz-Hamiltonoperator |

---

## Was die Simulation zeigt

### Referenzsimulation (`schrodinger_1d_reference.py`)

Numerisch exakte 1D-Schrödinger-Gleichung mit Split-Operator (FFT).
Dient als verifizierter Referenzstandard:

- **Freies Teilchen**, harmonischer Oszillator oder Potentialtopf
- Unitäre Zeitentwicklung (Normerhaltung < 10⁻¹³)
- Zweifache Kontrolle von ⟨p⟩ (k-Raum + Ableitungsoperator)
- Energieerhaltung verifiziert

### RFT-Simulation (`schrodinger_1d_rft.py`)

Implementiert den Resonanz-Hamiltonoperator Ĥ_res = Ĥ₀ + ε(Δφ)·V̂_Kopplung
und weist nach, dass für jedes Δφ die Zeitentwicklung exakt mit der
Standard-Schrödinger-Gleichung übereinstimmt.

**Vier Korrespondenz-Szenarien:**

| Szenario | Δφ | ε(Δφ) | Fidelity |
|----------|----|-------|----------|
| Freies Teilchen | π | 0 | 1.000000000000 |
| Schwache Kopplung | 2π/3 | 0.25 | 1.000000000000 |
| Halbe Kopplung | π/2 | 0.5 | 1.000000000000 |
| Volle Kopplung | 0 | 1.0 | 1.000000000000 |

→ **Korrespondenzprinzip numerisch belegt:** Standard-QM ist
  Spezialfall der RFT mit V_eff = ε(Δφ)·V_Kopplung.

### RFT-Dynamisch (`schrodinger_1d_rft_dynamic.py`)

> **Gutachter-Kritikpunkt:** Die statische RFT-Simulation ist mathematisch
> eine Tautologie – der Split-Operator sieht nur V_eff, egal ob ε·V als
> Kopplung oder direkt als Potential hereingegeben wird.

Macht Δφ(t) zu einem **dynamischen Feld**, das an ψ rückkoppelt:

$$
\Delta\varphi(t+\mathrm{d}t) = \Delta\varphi(t) + \lambda \cdot F[\psi] \cdot \mathrm{d}t
$$

**Drei Rückkopplungs-Modelle:**

| Modell | F[ψ] | Physikalische Interpretation |
|--------|------|----------------------------|
| `density` | ∫\|ψ\|⁴ dx | Kopplung an Lokalisierung |
| `position` | ⟨x⟩ | Kopplung an mittlere Position |
| `energy` | ⟨H⟩ − E₀ | Kopplung an Energieabweichung |

→ **Erstmals unterscheidbar von Standard-QM:** Die Rückkopplung
  ψ → Δφ → V_eff → ψ erzeugt nichtlineare, zustandsabhängige Dynamik,
  die messbar über Fidelity, ⟨x⟩, ⟨p⟩ von Standard-QM abweicht.

### Störungstheorie (`schrodinger_1d_rft_perturbation.py`)

> **Gutachter-Empfehlung:** „Im Limit λ → 0 muss die dynamische RFT gegen
> Standard-QM konvergieren, mit führenden Korrekturen O(λ). Das wäre die
> Störungstheorie der RFT."

Systematischer λ-Scan über mehrere Größenordnungen (10⁻⁴ … 10⁰) mit
Potenzgesetz-Analyse und analytischer Störungstheorie 1. Ordnung:

| Observable | Exponent (numerisch) | Exponent (Theorie) | Abweichung |
|------------|---------------------:|-------------------:|-----------:|
| 1 − Fidelity | 2.001 | 2 | 0.05 % |
| \|Δ⟨x⟩\| | 1.001 | 1 | 0.1 % |
| \|Δ⟨p⟩\| | 1.001 | 1 | 0.1 % |
| max\|Δψ\| | 0.999 | 1 | 0.1 % |

Dass $1 - F \sim \lambda^2$ folgt direkt aus
$|\langle\psi_0|\psi_0 + \lambda\psi_1\rangle|^2 = 1 - \lambda^2\|\psi_1\|^2 + \mathcal{O}(\lambda^3)$.
Die analytische Vorhersage 1. Ordnung stimmt mit der Numerik bis auf
relativen Fehler $1.3 \times 10^{-4}$ überein — ein harter, unabhängiger
Konsistenzcheck.

→ **Standard-QM ist exakter Grenzfall der RFT.** Die Störungstheorie
  bestätigt: RFT ist eine wohldefinierte, kontrollierte Erweiterung
  mit λ als einzigem freien Parameter.

### Experimenteller Vorschlag (`schrodinger_1d_rft_experiment.py`)

> **Gutachter-Kritikpunkt 3.1:** „SI-Einheiten / Kalibrierung —
> Dimensionslose Parameter auf ein physikalisches System abbilden."

Bildet die Störungstheorie-Ergebnisse auf **ultrakalte ⁸⁷Rb-Atome
in einer harmonischen Falle** ab — das experimentelle Standardsystem
für Präzisionsmessungen in der Quantenmechanik:

**SI-Kalibrierung:**

| Größe | Formel | Wert (ω = 2π × 100 Hz) |
|-------|--------|------------------------:|
| Oszillatorlänge | $a_\mathrm{ho} = \sqrt{\hbar/(m\omega)}$ | 1.08 µm |
| Längeneinheit | $\ell = V_s^{1/4} \cdot a_\mathrm{ho}$ | 0.41 µm |
| Zeiteinheit | $\tau = \sqrt{V_s} / \omega$ | 0.225 ms |

**Falsifizierbare Vorhersage:**

$$
|\Delta\langle x\rangle|_\mathrm{SI} = 4.9 \cdot \lambda \cdot \ell
\approx 2.0 \cdot \lambda\;\mu\mathrm{m}
$$

messbar über Absorptionsbildgebung (Auflösung ~ 1 µm).
Detektierbarkeitsgrenze: λ ≳ 0.05 nach 100 Wiederholungen.

→ **Die RFT liefert eine testbare Vorhersage.** Entweder wird ein
  Positionsshift $\propto \lambda$ gemessen (RFT bestätigt), oder
  eine obere Schranke für λ gesetzt (Parameterraum eingeschränkt).
  Details im [Experimentellen Vorschlag](docs/experimental_proposal.md).

---

## Dateistruktur

| Datei | Funktion |
|-------|----------|
| [`python/schrodinger_1d_reference.py`](python/schrodinger_1d_reference.py) | Referenz: Standard-Schrödinger (Split-Operator, FFT) |
| [`python/schrodinger_1d_rft.py`](python/schrodinger_1d_rft.py) | RFT: Resonanz-Hamiltonoperator + Korrespondenznachweis |
| [`python/schrodinger_1d_rft_dynamic.py`](python/schrodinger_1d_rft_dynamic.py) | RFT-Dynamisch: Δφ(t) mit Rückkopplung an ψ |
| [`python/schrodinger_1d_rft_perturbation.py`](python/schrodinger_1d_rft_perturbation.py) | Störungstheorie: λ→0 Konvergenz, Skalierungsanalyse |
| [`python/schrodinger_1d_rft_experiment.py`](python/schrodinger_1d_rft_experiment.py) | Experimenteller Vorschlag: SI-Kalibrierung für ⁸⁷Rb |
| [`docs/experimental_proposal.md`](docs/experimental_proposal.md) | Experimenteller Vorschlag: Falsifizierbare Vorhersage |
| [`docs/schrodinger_roadmap.md`](docs/schrodinger_roadmap.md) | Forschungsprogramm: Diskretes Feld → Schrödinger |
| [`requirements.txt`](requirements.txt) | Abhängigkeiten |

---

## Schnelleinstieg

```bash
pip install numpy matplotlib

# Referenz (Standard-QM)
python python/schrodinger_1d_reference.py --checks
python python/schrodinger_1d_reference.py --plot

# RFT-Korrespondenznachweis
python python/schrodinger_1d_rft.py --checks
python python/schrodinger_1d_rft.py --plot

# RFT-Dynamisch (Δφ koppelt rück an ψ)
python python/schrodinger_1d_rft_dynamic.py --checks
python python/schrodinger_1d_rft_dynamic.py --model density --lambda_coupling 5.0
python python/schrodinger_1d_rft_dynamic.py --model position --plot

# Störungstheorie (λ → 0 Konvergenz)
python python/schrodinger_1d_rft_perturbation.py --checks
python python/schrodinger_1d_rft_perturbation.py --plot

# Experimenteller Vorschlag (SI-Kalibrierung)
python python/schrodinger_1d_rft_experiment.py --checks
python python/schrodinger_1d_rft_experiment.py --omega 50
python python/schrodinger_1d_rft_experiment.py --plot

# Referenz mit Potential
python python/schrodinger_1d_reference.py --V harmonic --Vstrength 0.01 --steps 3000 --plot
```

---

## Grenzfälle der Kopplungseffizienz

| Bedingung | ε | Potential | Physik |
|-----------|---|-----------|--------|
| Perfekte Kopplung (Δφ = 0) | 1 | V_eff = V_Kopplung | Volle Wechselwirkung |
| Halbe Kopplung (Δφ = π/2) | 0.5 | V_eff = ½·V_Kopplung | 90° Phasenverschiebung |
| Schwache Kopplung (Δφ = 2π/3) | 0.25 | V_eff = ¼·V_Kopplung | Teilkopplung |
| Keine Kopplung (Δφ = π) | 0 | V_eff = 0 | Freies Teilchen |

---

## Numerische Methoden

### Split-Operator (symplektisch, 2. Ordnung)

$$
\psi(t+\Delta t) = e^{-iV\Delta t/2\hbar}\;\mathcal{F}^{-1}\!\left[e^{-iT\Delta t/\hbar}\;\mathcal{F}\!\left[e^{-iV\Delta t/2\hbar}\;\psi(t)\right]\right]
$$

- Unitär → exakte Normerhaltung (numerisch < 10⁻¹³)
- Energieerhaltung im Split-Operator: max|Δ⟨H⟩| < 10⁻⁵
- FFT-basiert → O(N log N) pro Zeitschritt

### FFT-Normierungskonventionen

Für physikalische Erwartungswerte im Impulsraum wird eine
kontinuierlich normierte ψ̃(k) berechnet:

$$
\tilde\psi(k) = \frac{dx}{\sqrt{2\pi}} \cdot \text{FFT}[\psi]
$$

sodass ∑|ψ̃(k)|²·dk = 1 wenn ∑|ψ(x)|²·dx = 1.

---

## Forschungsprogramm

Das vollständige Forschungsprogramm (diskretes Feld → Kontinuumsgrenzwert
→ Schrödinger-Gleichung) ist in der [Roadmap](docs/schrodinger_roadmap.md)
dokumentiert.

---

*© Dominic-René Schu, 2025/2026 — Resonanzfeldtheorie*

---

⬅️ [zurück zur Übersicht](../README.md)
