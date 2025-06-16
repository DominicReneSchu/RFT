# Resonanzfeldtheorie Framework

Dieses Framework bietet eine modulare, moderne Infrastruktur zur Simulation und Analyse skalarer Resonanzfelder in flacher und gekrümmter Raumzeit. Es verbindet numerische Methoden, Visualisierung und wissenschaftliche Dokumentation und legt besonderen Fokus auf Energiehaltung, Stabilität und Erweiterbarkeit.

---

## Inhalt und Motivation

**Was ist die Resonanzfeldtheorie?**  
Die Resonanzfeldtheorie beschreibt ein skalares Feld (epsilon, ε) mit nichtlinearem Potential, das an die Raumzeitgeometrie – speziell an den Ricci-Skalar (R) – gekoppelt ist. Solche Felder sind relevant in der modernen Kosmologie (z.B. modifizierte Gravitation, Inflatonmodelle, skalare Solitonen, Topologische Defekte) und in der Feldtheorie (Domänenwände, Symmetriebrüche).

**Was kann das Framework?**  
- **1D/FLRW-Modell:** Direkte Zeitentwicklung des Resonanzfelds und des kosmologischen Skalenfaktors (a(t)), gekoppelt über modifizierte Einsteingleichungen. Energiehaltung und Dynamik werden überwacht.
- **3D-Resonanzfeld:** Klassische Gitter-Simulation (explizite Zeitentwicklung) für nichtlineare Wellengleichungen, inkl. Visualisierung von Schnitten und Mittelwerten. Erweiterbar auf parallele oder GPU-basierte Berechnung.
- **Theorie, Tests, Doku:** Alle Gleichungen, Methoden und Skripte sind dokumentiert und mit Unittests versehen. Die Struktur erlaubt eine schnelle Anpassung für eigene Fragestellungen.

---

## Zentrale Erkenntnisse und Highlights

- **Numerische Energieüberwachung**: Die 1D/FLRW-Implementierung prüft und visualisiert die Energieerhaltung als Qualitätsmaß für die numerische Integrität – ein entscheidender Aspekt für jede Feldsimulation.
- **Flexible Modellierung**: Potenziale (Masse, Selbstkopplung, mexikanischer Hut etc.) und Kopplungen (Ricci-Skalar, nichtlinear) sind leicht anpassbar und ermöglichen eine Vielzahl physikalischer Szenarien.
- **Visualisierung & Analyse**: Live-Plots von Feldern, Skalenfaktoren und deren Mittelwerten geben schnellen Einblick in Dynamik, Stabilität und Musterbildung (z.B. Solitonen, Ausbreitung, Relaxation).
- **Erweiterbarkeit**: Parallele (Numba) und GPU-basierte (CuPy) 3D-Algorithmen ermöglichen größere Simulationen mit wenig Codeänderung. Die klare Trennung von Kernlogik, Visualisierung und Steuerung macht das Framework robust und wartbar.
- **Wissenschaftliche Reproduzierbarkeit**: Mit zentraler Konfiguration, dokumentierten Testfällen und klaren Skripten ist das Framework ideal für kollaborative Forschung und Lehre.

---

## Ordnerstruktur

```
relativitaet_verbindung/
│
├── config.py                  # Globale Parameter & Optionen
├── requirements.txt           # Python-Abhängigkeiten
├── README.md                  # Diese Dokumentation
│
├── core/                      # Kernmodule: Modelle & Methoden
│   ├── flrw_1d.py             # 1D/FLRW-Integrator
│   ├── field_3d.py            # 3D Gitterfeld (Basis)
│   ├── field_3d_parallel.py   # 3D (Numba-parallelisiert)
│   └── field_3d_gpu.py        # 3D (GPU/CuPy)
│
├── viz/                       # Visualisierungsmodule
│   ├── plot_1d.py
│   └── plot_3d.py
│
├── run_1d.py                  # Startskript 1D-Simulation
├── run_3d.py                  # Startskript 3D-Simulation
│
└── tests/                     # Unittests
    ├── test_flrw_1d.py
    └── test_field_3d.py
```

---

## Anwendung: Schnellstart

1. **Installation**
   ```bash
   pip install -r requirements.txt
   ```

2. **1D-FLRW-Simulation starten**
   ```bash
   python run_1d.py
   ```
   → Plots für ε(t), Skalenfaktor a(t) und Energieänderung.

3. **3D-Resonanzfeldsimulation starten**
   ```bash
   python run_3d.py
   ```
   → Live-Visualisierung von Schnitten und Mittelwerten des Feldes.

4. **Tests ausführen**
   ```bash
   pytest tests/
   ```

---

## Beispiel: Physikalische Szenarien und Erkenntnisse

- **Kosmische Felddynamik:**  
  Wie koppelt ein skalares Feld an die Expansion des Universums? Welche Wechselwirkungen dominieren die Dynamik?
- **Nichtlineare Phänomene:**  
  Wie entstehen Solitonen, Domänenwände oder Relaxationsphänomene aus dem Potential?
- **Numerische Stabilität:**  
  Wie wirkt sich die Wahl von Schrittweite, Potentialparametern und Kopplung auf die Energiehaltung aus?
- **Vergleich von CPU, Parallelisierung und GPU:**  
  Wie lässt sich die Simulation für große Gitter und lange Zeitentwicklungen effizient beschleunigen?

---

## Typische Erweiterungen

- Neue Felder/Kopplungen (z.B. komplexe Felder, Tensorfelder)
- Erweiterte Potenziale und Anfangsbedingungen
- Spezielle Visualisierungen (3D-Volumen, Animationen, Interaktivität)
- Einbindung experimenteller oder beobachteter Daten

---

## Weiterführende Literatur und Hintergründe

- Scalar-Tensor-Theorien, modifizierte Gravitation (z.B. Brans-Dicke, f(R)-Gravitation)
- Nichtlineare Feldtheorie, Solitonen, Topologische Defekte
- Kosmologie und frühes Universum


---

*© Dominic Schu, 2025 – Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](../README.md)
