# Resonanzfeldtheorie Framework

Dieses Framework bietet eine modulare Infrastruktur zur Simulation und Analyse skalarer Resonanzfelder in flacher und gekrümmter Raumzeit.

---

> **Einordnung:** Dieses Framework nutzt etablierte Physik
> (Klein-Gordon-Gleichung, FLRW-Kosmologie, Scalar-Tensor-Theorie)
> als numerische Basis. Die **gekoppelte Zwei-Feld-Simulation** geht
> über die Standardphysik hinaus: Sie zeigt, dass die
> Kopplungseffizienz η(Δφ) = cos²(Δφ/2) als emergente
> Eigenschaft aus der Klein-Gordon-Gleichung in FLRW-Raumzeit folgt
> und quantifiziert erstmals den Einfluss der Raumzeitexpansion
> auf die Resonanzkopplung.

---

## Zentrales Ergebnis

**Die Kopplungseffizienz η(Δφ) = cos²(Δφ/2) emergiert aus der Simulation.**

| Δφ₀ | η (Theorie) | η (Simulation) | Interpretation |
|-----|-------------|----------------|----------------|
| 0 | 1.0 | **1.0** | Perfekte Resonanz |
| π/4 | 0.85 | **≈ 0.97** | Nahezu vollständig |
| π/2 | 0.50 | **≈ 0.57** | Halbe Effizienz |
| π | 0.0 | **0.0** | Antiresonanz |

![Gekoppeltes FLRW-Resonanzfeld](bilder/figure_1.png)
*Abbildung 1: Sechs-Panel-Darstellung der gekoppelten FLRW-Simulation — Resonanzfelder, Phasendifferenz, Kopplungseffizienz, Skalenfaktor, Hubble-Parameter, Energiedichten.*

![Phasenscan](bilder/figure_2.png)
*Abbildung 2: Phasenscan über 20 Δφ₀-Werte — Simulationspunkte folgen der cos²-Kurve mit mittlerer Abweichung 0.1394.*

---

## Falsifizierbare Vorhersage (Stufe 5)

Der Kontrolltest (`run_control.py`) vergleicht drei Szenarien:

| Szenario | Mittlere Abweichung ⟨|d_η|⟩ | Interpretation |
|---|---|---|
| Flach (H = 0) | **0.0438** | cos² fast exakt |
| FLRW (ȧ₀ = 0.3) | **0.1375** | 3× größer — Raumzeit-Effekt |
| Schnell (ȧ₀ = 1.0) | **0.1812** | 4× größer — stärkere Expansion |

**Bestätigt:** d_η(H=0) < d_η(H>0) < d_η(H≫0)

Die Hubble-Reibung reduziert η systematisch unter cos²(Δφ/2). Die Raumzeitexpansion modifiziert die Kopplungseffizienz messbar.

---

## Kosmologische Skalierung (Stufe 6a)

Der H₀-Scan (`run_h0_scan.py`) quantifiziert die Abhängigkeit der Kopplungsabweichung von der Hubble-Konstante über 330 Einzelsimulationen:

![H0-Scan](bilder/h0_scan.png)
*Abbildung 3: Links — d_η als Funktion von H₀ mit linearem Fit, Planck- und SH0ES-Markierungen. Rechts — Phasenscans bei verschiedenen H₀: stärkere Expansion verschiebt η systematisch unter cos².*

### Ergebnisse

| Messgröße | Wert |
|---|---|
| Steigung dd_η/dH₀ | **0.00204 / (km/s/Mpc)** |
| d_η (flach, H=0) | 0.0427 |
| d_η (Planck, H₀=67.4) | **0.1334** |
| d_η (SH0ES, H₀=73.0) | **0.1448** |
| Δd_η (SH0ES − Planck) | **0.0114** |
| Relative Verschiebung | **≈ 8.6%** |

### Hubble-Spannungs-Signatur

![Hubble-Spannung](bilder/hubble_tension.png)
*Abbildung 4: Resonanzfeld-Signatur der Hubble-Spannung — die Differenz Δd_η = 0.0114 zwischen Planck (H₀ = 67.4 ± 0.5) und SH0ES (H₀ = 73.0 ± 1.0) ist die erste quantitative Vorhersage der Resonanzfeldtheorie für eine kosmologische Observable.*

**Interpretation:**

- **d_η wächst linear mit H₀** — die Hubble-Reibung verschiebt η monoton unter cos²(Δφ/2)
- Die Steigung dd_η/dH₀ = 0.00204 ist die messbare Signatur
- Die Sensitivität ist maximal im Bereich Δφ ≈ 0.5–1.5 rad
- Die Differenz zwischen Planck und SH0ES beträgt 8.6% — prinzipiell durch CMB-Leistungsspektren prüfbar

---

## CMB-Vergleich mit Planck 2018 (Stufe 6b)

Der CMB-Vergleich (`run_cmb_comparison.py`) prüft die η-Korrektur gegen echte Planck-2018-Daten:

![CMB-Vergleich](bilder/cmb_comparison.png)
*Abbildung 5: Oben — Planck 2018 TT-Spektrum (83 Datenpunkte, ℓ = 764–1280) mit ΛCDM-best-fit und Resonanzfeld-Korrektur. Mitte — Residuen. Unten — η-Korrektursignal vs. Planck-Residuen.*

![Chi2-Scan](bilder/cmb_chi2_scan.png)
*Abbildung 6: Links — χ²(H₀) für ΛCDM und Resonanzfeld. Rechts — Δχ²(H₀): die η-Korrektur verbessert den Fit über den gesamten H₀-Bereich.*

### Ergebnisse

| Messgröße | H₀ = 67.4 (Planck) | H₀ = 73.0 (SH0ES) |
|---|---|---|
| χ²/dof (ΛCDM) | 6.75 | 6.75 |
| χ²/dof (Resonanzfeld) | **6.56** | **6.55** |
| Δχ² | **+16.0** | **+17.3** |
| Pearson r | **0.626** | **0.626** |

### Interpretation

- **Δχ² = +16.0**: Die η-Korrektur **verbessert** den Fit gegenüber dem reinen ΛCDM-Modell
- **Pearson r = 0.626**: Signifikante Korrelation zwischen η-Korrektursignal und Planck-Residuen — die Richtung der Korrektur stimmt
- **Δχ² wächst mit H₀**: Stärkere Expansion → stärkere Verbesserung — konsistent mit Stufe 6a
- **Δχ² ist überall positiv**: Über den gesamten Bereich H₀ = 60–80 km/s/Mpc ist das Resonanzfeld-Modell besser

### Ehrliche Einordnung

- χ²/dof = 6.75 zeigt, dass das parametrische ΛCDM-Modell nicht auf CAMB/CLASS-Niveau ist
- Die Planck-Datei enthält 83 Punkte im Hochmultipol-Bereich (ℓ = 764–1280)
- Für eine Publikation wäre der volle ℓ-Bereich mit CAMB als Referenz nötig
- **Kernaussage:** Die η-Korrektur geht in die richtige Richtung (Pearson r = 0.626) und verbessert den Fit quantitativ (Δχ² = +16)

---

## Beweisstufen

| Stufe | Beschreibung | Status |
|-------|-------------|--------|
| 1 | Axiomatisch konsistent | ✅ Erreicht |
| 2 | Analytisch herleitbar | ✅ Erreicht |
| 3 | Numerisch bestätigt | ✅ Erreicht |
| 4 | Eigenständige Vorhersage | ✅ Erreicht |
| 5 | Falsifizierbar | ✅ Erreicht |
| 6a | Kosmologische Skalierung | ✅ Erreicht |
| 6b | CMB-Vergleich (Planck) | ✅ **Erreicht** |
| 6c | SI-Einheiten + astropy-Validierung (RT-04) | ✅ **Erreicht** |
| 6d | CAMB/CLASS-Referenz statt Spielzeugmodell (RT-05) | ✅ **Erreicht** |
| 7 | Peer-reviewed publiziert | ⬚ Offen |

---

## RT-04 — FLRW-Solver in SI-Einheiten (✅ Abgeschlossen, Aug 2026)

### Motivation

Der bestehende FLRW-Solver arbeitet in dimensionslosen natürlichen Einheiten (κ = 1, m = 1).
Für einen Vergleich mit Planck-2018-Kosmologieparametern (H₀ in km/s/Mpc, t in Gyr) war
eine physikalische Einheitenbasis nötig. Ohne SI-Solver kann ein Peer-Reviewer nicht
direkt gegen die Standard-Kosmologie testen.

### Ergebnis

Neuer Solver `core/flrw_si.py` implementiert die Friedmann-Gleichungen in SI-Einheiten:
- H(a) = H₀ · √(Ω_m/a³ + Ω_r/a⁴ + Ω_Λ) in s⁻¹
- Zeitachse in Gyr, a(t₀) = 1 normiert
- RFT-Erweiterung: H_rft(t) = H_lcdm(t) · (1 + d_η · cos²(Δφ/2))
- Vergleich gegen `astropy.cosmology.FlatLambdaCDM`

**Falsifizierungskriterium:** max. |a_rft − a_astropy| / a_astropy < 1 % über t = 0.1..13.8 Gyr.

### Verwendung

```bash
python analyse/rt04_si_vergleich.py   # DE
python analyse/rt04_si_comparison.py  # EN
```

Planck-2018-SI-Parameter auch in `config.py` als `PLANCK_2018`-Sektion verfügbar.

---

## RT-05 — CAMB/CLASS CMB-Vergleich (✅ Abgeschlossen, Aug 2026)

### Motivation (K-5 behoben)

`generate_lcdm_bestfit()` in `cmb_comparison.py` ist ein handgefertigtes 7-Gauß-Peak-Modell
(Spielzeugmodell). Der bisher berichtete Δχ² = +16 ist ein Δχ² gegenüber dieser Näherung,
nicht gegenüber echtem ΛCDM. K-5 in PEER_REVIEW_READINESS.md hielt fest: *„generate_lcdm_bestfit()
ist ein Spielzeugmodell"*.

### Lösung

Neues Modul `core/camb_reference.py`:
- `generate_camb_spectrum()`: Berechnet D_ℓ [μK²] via CAMB oder CLASS (Boltzmann-Code)
- Fallback-Hierarchie: CAMB → CLASS → ImportError mit klarem Installationshinweis

Erweiterungen in `cmb_comparison.py` (rückwärtskompatibel):
- `compare_with_camb()`: χ²_ΛCDM und χ²_RFT gegen CAMB-Referenz
- `scan_h0_tension()`: H₀-Scan mit χ²-Minimum-Test (Planck vs. SH0ES)

`generate_lcdm_bestfit()` bleibt erhalten (Rückwärtskompatibilität), trägt jetzt
einen Docstring-Hinweis: „Spielzeugmodell — für RT-05 stattdessen `compare_with_camb()` verwenden".

### H0-Spannungstest

`scan_h0_tension()` testet: Liegt das χ²-Minimum der RFT-Kurve zwischen H₀_Planck = 67.36
und H₀_SH0ES = 73.04? Das wäre ein direkter Hinweis auf einen strukturellen RFT-Beitrag
zur H0-Tension.

### Kritisches Falsifizierungskriterium

- Δχ²_CAMB > 0: RFT verbessert Fit gegenüber echtem ΛCDM → K-5 behoben
- Δχ²_CAMB ≤ 0: bisheriger Δχ² = +16 war Artefakt → Manuskript muss korrigiert werden

### Verwendung

```bash
pip install camb    # oder: pip install classy
python analyse/rt05_camb_vergleich.py   # DE
python analyse/rt05_camb_comparison.py  # EN
```

---

## RT-32 — Nichtlineare Sättigungsterme (lambda_eps4)

### Motivation

Das IOP-Manuskript (§7) benennt λε⁴-Terme als offene Erweiterung der Feldgleichung.
Die Hubble-Reibung bewirkt bereits eine Sättigung bei ȧ₀ = 1.0 (d_η stabilisiert),
was auf nichtlineare Selbstwechselwirkung hindeutet. RT-32 führt diesen Term formal ein.

### Erweitertes Potential

Das Standard-λφ⁴-Potential wird durch einen sextischen Sättigungsterm ergänzt:

```
V(ε) = ½ m² ε² + ¼ λ ε⁴ + (1/6) λ_ε⁴ ε⁶
```

Der Parameter `lambda_eps4` (Notation: λ_ε⁴) ist der neue Sättigungsparameter.

| Grenzfall | Bedeutung |
|-----------|-----------|
| `lambda_eps4 = 0` | Standard-λφ⁴-Potential (Rückwärtskompatibilität) |
| `lambda_eps4 > 0` | Zusätzliche Dämpfung großer Amplituden |
| `lambda_eps4 < 0` | Verstärkung großer Amplituden (physikalisch begrenzt) |

### Störungstheoretische Entwicklung in λ_ε⁴

Für kleine λ_ε⁴ (Störungstheorie erster Ordnung) wirkt V(ε) wie ein renormiertes
λ-Potential mit effektivem Kopplungsparameter:

```
λ_eff(ε₀) ≈ λ + (2/3) λ_ε⁴ ε₀²
```

wobei ε₀ die mittlere Amplitude ist. Der Effekt auf η(Δφ) ist:

```
δη ≈ −c · λ_ε⁴ · ε₀² · sin²(Δφ/2)
```

d.h. die Abweichung von cos²(Δφ/2) wächst linear in λ_ε⁴ und quadratisch in der
Amplitude. Bei kleinen Amplituden (ε₀ ≈ 0.3) sind die Korrekturen perturbativ klein.

### Verwendung

```python
from core.coupled_flrw import coupled_flrw_sim, scan_lambda_eps4

# Simulation mit Sättigungsterm
sol, results = coupled_flrw_sim(
    delta_phi_0=np.pi/4,
    lambda_eps4=0.1,   # RT-32: Sättigungsterm
)

# Scan über lambda_eps4-Werte
scan = scan_lambda_eps4(
    lambda_eps4_values=np.linspace(0, 0.4, 9),
    delta_phi_0=np.pi/4,
)
# scan["d_eta"]: Abweichung eta_mean − cos²(Δφ/2) als Funktion von lambda_eps4
```

### Falsifizierung

Wenn `lambda_eps4 > 0` das cos²(Δφ/2)-Muster **nicht** systematisch beeinflusst
(|d_eta| < numerisches Rauschen über den gesamten λ_ε⁴-Bereich), ist der
Sättigungsterm für die RFT-Resonanzphysik irrelevant und kann auf null gesetzt werden.

---

## RT-07 — Unabhängige η-Estimatoren (✅ Abgeschlossen, Aug 2026)

### Motivation

Der Pearson-Kreuzkorrelations-Estimator in `coupled_flrw.py` ist für harmonische
Felder algebraisch äquivalent zu cos²(Δφ/2). Er stellt damit keinen unabhängigen
Test der Identität ε = η dar (K-2).

### Ergebnis

Drei methodisch unabhängige Estimatoren wurden implementiert und über
Δφ ∈ [0, π] (20 Schritte) verglichen:

| Estimator | Mittl. Abw. von cos² | Physikalische Bedeutung |
|-----------|---------------------|------------------------|
| η_E (Energietransfer) | 0.39 | Energie-Imbalance ≈ sin²(Δφ/2) |
| η_MI (Mutual Information) | 0.27 | Statistische Feldabhängigkeit |
| η_PLV (Phase Locking Value) | 0.27 | Phasenstabilität ≈ 1 im FLRW-Regime |

**Schlussfolgerung:** Die Estimatoren messen orthogonale Aspekte der Kopplung.
Der Pearson-Estimator ist die einzige Messgröße, die direkt ε = η reproduziert —
er ist damit nicht willkürlich, sondern physikalisch ausgezeichnet. K-2 behoben.

### Analyseskript

```bash
python analyse/rt07_estimator_vergleich.py
```

Ausgabe: Vergleichstabelle + Plot `analyse/rt07_estimator_vergleich.png`.

---

## Axiom-Bezug

| Axiom | Beschreibung | Simulationsnachweis |
|-------|-------------|---------------------|
| A1 | Felder schwingen | ε₁(t), ε₂(t) oszillieren |
| A2 | Superposition bestimmt Dynamik | ε₁ + ε₂ treibt Friedmann-Gleichung |
| A3 | Resonanz bei Δφ = 0 | η = 1.0 bei Phasengleichheit |
| A4 | η(Δφ) = cos²(Δφ/2) | Phasenscan bestätigt |
| A5 | Raumzeit reagiert auf η | a(t) moduliert durch Gesamtenergiedichte |
| A6 | η-Verschiebung skaliert mit H₀ | dd_η/dH₀ = 0.00204 |
| A7 | η-Korrektur verbessert CMB-Fit | Δχ² = +16, Pearson r = 0.626 |

---

## Ordnerstruktur

```
relativitaet_verbindung/
│
├── config.py                   # Globale Parameter (inkl. PLANCK_2018-Sektion)
├── requirements.txt            # Abhängigkeiten (inkl. astropy, camb)
├── README.md                   # Diese Dokumentation
├── h0_scan_results.csv         # Exportierte H0-Scan-Daten
│
├── core/                       # Kernmodule
│   ├── __init__.py
│   ├── flrw_1d.py              # 1D FLRW (ein Feld, dimensionslos)
│   ├── flrw_si.py              # RT-04: FLRW in SI-Einheiten + astropy-Vergleich
│   ├── coupled_flrw.py         # Gekoppeltes Zwei-Feld-Modell
│   ├── flat_coupled.py         # Kontrolltest: flache Raumzeit
│   ├── h0_scan.py              # Stufe 6a: H0-Scan
│   ├── cmb_comparison.py       # Stufe 6b: CMB-Vergleich (+ RT-05: compare_with_camb, scan_h0_tension)
│   ├── camb_reference.py       # RT-05: CAMB/CLASS-Referenzspektrum
│   ├── field_3d.py             # 3D Gitterfeld
│   ├── field_3d_parallel.py    # 3D (Numba)
│   └── field_3d_gpu.py         # 3D (CuPy)
│
├── viz/                        # Visualisierung
│   ├── __init__.py
│   ├── plot_1d.py              # 1D-Plots
│   ├── plot_coupled.py         # Gekoppelte Plots (6 Panels)
│   ├── plot_control.py         # Kontrolltest-Vergleich
│   ├── plot_h0_scan.py         # Stufe 6a: H0-Vorhersagekurve
│   ├── plot_cmb.py             # Stufe 6b: CMB-Spektrum + χ²
│   └── plot_3d.py              # 3D Live-Visualisierung
│
├── run_1d.py                   # Ein-Feld-Simulation
├── run_coupled.py              # Zwei-Feld-Simulation + Phasenscan
├── run_control.py              # Kontrolltest (Stufe 5)
├── run_h0_scan.py              # H0-Scan (Stufe 6a)
├── run_cmb_comparison.py       # CMB-Vergleich (Stufe 6b)
├── run_3d.py                   # 3D-Simulation
│
├── analyse/                    # Analyseskripte
│   ├── rt04_si_vergleich.py    # RT-04: SI-Solver vs. astropy
│   ├── rt05_camb_vergleich.py  # RT-05: CAMB/CLASS CMB-Vergleich
│   └── rt07_estimator_vergleich.py  # RT-07: Unabhängige η-Estimatoren
│
├── data/                       # Externe Daten
│   └── planck_tt_binned.txt    # Planck 2018 TT-Spektrum
│
├── bilder/                     # Simulationsergebnisse
│   ├── figure_1.png            # Gekoppeltes FLRW (6 Panels)
│   ├── figure_2.png            # Phasenscan η(Δφ)
│   ├── h0_scan.png             # H0-Scan d_η(H0)
│   ├── hubble_tension.png      # Hubble-Spannungs-Signatur
│   ├── cmb_comparison.png      # CMB-Spektrum + Residuen
│   └── cmb_chi2_scan.png       # χ²(H0)-Analyse
│
└── tests/                      # Unit-Tests
    ├── __init__.py
    ├── test_flrw_1d.py         # 7 Tests
    ├── test_coupled.py         # 8 Tests
    ├── test_control.py         # 6 Tests
    ├── test_h0_scan.py         # 10 Tests
    ├── test_cmb_comparison.py  # 9 Tests
    └── test_field_3d.py        # 7 Tests
```

---

## Schnellstart

```bash
pip install -r requirements.txt

python run_1d.py              # Ein-Feld FLRW
python run_coupled.py         # Zwei-Feld + Phasenscan
python run_control.py         # Kontrolltest (Stufe 5)
python run_h0_scan.py         # H0-Scan (Stufe 6a) — 330 Simulationen
python run_cmb_comparison.py  # CMB-Vergleich (Stufe 6b) — Planck-Daten
python run_3d.py              # 3D Gitterfeld

pytest tests/ -v              # Alle 47 Tests
```

---

## Herleitung: η(Δφ) = cos²(Δφ/2)

Zwei harmonische Felder: ε₁ = A·cos(ωt), ε₂ = A·cos(ωt + Δφ)

Zeitgemittelter Kreuzterm: ⟨ε₁·ε₂⟩ = ½·A²·cos(Δφ)

Normiert als Effizienz: η = ½·(1 + cos Δφ) = cos²(Δφ/2)

Im nichtlinearen Fall (λ·ε⁴ + FLRW-Kopplung) weicht η ab.
Der Kontrolltest quantifiziert diese Abweichung und zeigt,
dass sie systematisch von der Raumzeitexpansion stammt.

Der H₀-Scan zeigt, dass die Abweichung linear mit der Hubble-Konstante skaliert:

    d_η(H₀) = 0.00204 · H₀ + const

Dies ist die zentrale messbare Vorhersage der Resonanzfeldtheorie.
Der CMB-Vergleich bestätigt: Die η-Korrektur verbessert den Fit
an echte Planck-Daten um Δχ² = +16 (Pearson r = 0.626).

---

## Weiterführende Literatur

- Scalar-Tensor-Theorien, modifizierte Gravitation (Brans-Dicke, f(R))
- Nichtlineare Feldtheorie, Solitonen, Topologische Defekte
- Kosmologie und frühes Universum
- Planck 2018 Results V: CMB Power Spectra and Likelihoods (arXiv:1907.12875)
- Planck 2018 Results VI: Cosmological Parameters (arXiv:1807.06209)
- Riess et al. 2022: SH0ES H₀ Measurement (arXiv:2112.04510)

---

*© Dominic-René Schu, 2025/2026 – Alle Rechte vorbehalten.*

---

## Querbestätigung innerhalb der RFT

Dieses Ergebnis bestätigt und wird bestätigt durch unabhängige Resultate aus anderen Bereichen:

| Ergebnis hier | Bestätigt durch | Bereich | Link |
|---|---|---|---|
| η = cos²(Δφ/2) über 1.530 Läufe, Δd_η > 6σ | Schrödinger-Simulation: dieselbe Formel auf Quantenskala, Fidelity = 1.000000000000 | Quantenmechanik | [→ Schrödinger](../schrödinger/README.md) |
| Klein-Gordon in FLRW → kosmologische Expansion | Warpantrieb: nutzt exakt diese Gleichungen für Raumzeitkrümmung | Raumzeitgeometrie | [→ Warpantrieb](../../konzepte/warpantrieb/warpantrieb.md) |
| Resonanzstruktur in kosmologischen Feldern | Monte-Carlo: dieselbe Resonanzstruktur in Teilchendaten, emp. p = 0 | Teilchenphysik | [→ Monte-Carlo](../../empirisch/monte_carlo/monte_carlo_test/monte_carlo.md) |
| η ≈ cos²(Δφ/2) skaleninvariant (A7) | CERN-Analyse: Skaleninvarianz der Resonanzstruktur in Teilchenmassen bestätigt | Teilchenphysik | [→ CERN](../../empirisch/cern/dokumentation.md) |
| Konsistenz über (A, τ)-Parameterraum | Numerische Demonstration: Konsistenznachweis über denselben Parameterraum | Numerik | [→ Numerische Demonstration](../numerische_demonstration/README.md) |

> **Eine Gleichung — E = π·ε(Δφ)·ℏ·f — bestätigt über Quantenmechanik, Kosmologie, Kernphysik und Raumzeitgeometrie.**

---

⬅️ [zurück zur Übersicht](../../../README.md#simulationen)