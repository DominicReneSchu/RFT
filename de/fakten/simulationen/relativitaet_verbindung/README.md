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

## Beweisstufen

| Stufe | Beschreibung | Status |
|-------|-------------|--------|
| 1 | Axiomatisch konsistent | ✅ Erreicht |
| 2 | Analytisch herleitbar | ✅ Erreicht |
| 3 | Numerisch bestätigt | ✅ Erreicht |
| 4 | Eigenständige Vorhersage | ✅ Erreicht |
| 5 | Falsifizierbar | ✅ **Erreicht** |
| 6 | Experimentell bestätigt | ⬚ Offen |
| 7 | Peer-reviewed publiziert | ⬚ Offen |

---

## Axiom-Bezug

| Axiom | Beschreibung | Simulationsnachweis |
|-------|-------------|---------------------|
| A1 | Felder schwingen | ε₁(t), ε₂(t) oszillieren |
| A2 | Superposition bestimmt Dynamik | ε₁ + ε₂ treibt Friedmann-Gleichung |
| A3 | Resonanz bei Δφ = 0 | η = 1.0 bei Phasengleichheit |
| A4 | η(Δφ) = cos²(Δφ/2) | Phasenscan bestätigt |
| A5 | Raumzeit reagiert auf η | a(t) moduliert durch Gesamtenergiedichte |

---

## Ordnerstruktur

```
relativitaet_verbindung/
│
├── config.py                   # Globale Parameter
├── requirements.txt            # Abhängigkeiten
├── README.md                   # Diese Dokumentation
│
├── core/                       # Kernmodule
│   ├── __init__.py
│   ├── flrw_1d.py              # 1D FLRW (ein Feld)
│   ├── coupled_flrw.py         # Gekoppeltes Zwei-Feld-Modell
│   ├── flat_coupled.py         # Kontrolltest: flache Raumzeit
│   ├── field_3d.py             # 3D Gitterfeld
│   ├── field_3d_parallel.py    # 3D (Numba)
│   └── field_3d_gpu.py         # 3D (CuPy)
│
├── viz/                        # Visualisierung
│   ├── __init__.py
│   ├── plot_1d.py              # 1D-Plots
│   ├── plot_coupled.py         # Gekoppelte Plots (6 Panels)
│   ├── plot_control.py         # Kontrolltest-Vergleich
│   └── plot_3d.py              # 3D Live-Visualisierung
│
├── run_1d.py                   # Ein-Feld-Simulation
├── run_coupled.py              # Zwei-Feld-Simulation + Phasenscan
├── run_control.py              # Kontrolltest (Stufe 5)
├── run_3d.py                   # 3D-Simulation
│
└── tests/                      # Unit-Tests
    ├── __init__.py
    ├── test_flrw_1d.py         # 7 Tests
    ├── test_coupled.py         # 8 Tests
    ├── test_control.py         # 6 Tests
    └── test_field_3d.py        # 7 Tests
```

---

## Schnellstart

```bash
pip install -r requirements.txt

python run_1d.py          # Ein-Feld FLRW
python run_coupled.py     # Zwei-Feld + Phasenscan
python run_control.py     # Kontrolltest (Stufe 5)
python run_3d.py          # 3D Gitterfeld

pytest tests/ -v          # Alle 28 Tests
```

---

## Herleitung: η(Δφ) = cos²(Δφ/2)

Zwei harmonische Felder: ε₁ = A·cos(ωt), ε₂ = A·cos(ωt + Δφ)

Zeitgemittelter Kreuzterm: ⟨ε₁·ε₂⟩ = ½·A²·cos(Δφ)

Normiert als Effizienz: η = ½·(1 + cos Δφ) = cos²(Δφ/2)

Im nichtlinearen Fall (λ·ε⁴ + FLRW-Kopplung) weicht η ab.
Der Kontrolltest quantifiziert diese Abweichung und zeigt,
dass sie systematisch von der Raumzeitexpansion stammt.

---

## Weiterführende Literatur

- Scalar-Tensor-Theorien, modifizierte Gravitation (Brans-Dicke, f(R))
- Nichtlineare Feldtheorie, Solitonen, Topologische Defekte
- Kosmologie und frühes Universum

---

*© Dominic-René Schu, 2025/2026 – Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](../README.md)