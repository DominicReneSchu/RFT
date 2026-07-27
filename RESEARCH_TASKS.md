# RFT — Offene Forschungsaufgaben

Generiert: Juli 2026
Status: Aktiv

---

## Kategorie 1: Theoretische Herleitungen

### RT-01 — Wirkungsintegral-Herleitung von π
**Motivation:** Der Faktor π in E = π·ε·ℏ·ω ist derzeit ein Postulat (K-1).
**Aufgabe:** Herleitung über Wirkungsintegral S[ψ, Δφ] — π soll als
Sattelpunktsbeitrag der stationären Phase folgen.
**Ansatz:** Pfadintegral-Formulierung der Kopplungsenergie.
**Falsifizierung:** Wenn S[ψ, Δφ] keinen π-Beitrag liefert, muss A4 neu formuliert werden.

**RT-01 (Erweiterung):** Der exakte Grenzübergang der RFT-Formel E = π·ε·ℏ·f zur Standard-Planck-Relation E = hf_Hz ist eine offene mathematische Frage. Der nächste Planck-Grenzwert liegt bei ε = 1/(2π), nicht bei ε = 1. Die Frage lautet: Existiert eine physikalisch motivierte Erweiterung des ε-Wertebereichs oder eine alternative Frequenzdefinition, die den sauberen Grenzübergang ermöglicht?

### RT-02 — Gruppentheoretischer Beweis der Skalentransformation (A7)
**Motivation:** A7 behauptet Skalentransformation über CMB-, Kern- und Finanzskalen (M-2).
**Aufgabe:** Formaler Beweis, dass G_sync über alle Skalen dieselbe Kopplungsstruktur erhält.
**Ansatz:** Darstellungstheorie von G_sync; Renormierungsgruppen-Analyse.

### RT-03 — Unabhängige Bestimmung von λ (⁸⁷Rb-Vorhersage)
**Motivation:** |Δ⟨x⟩| = 4.9·λ·ℓ ist nicht falsifizierbar ohne unabhängiges λ (M-7).
**Aufgabe:** λ aus einem zweiten, unabhängigen Experiment bestimmen.
**Ansatz:** Doppelspalt-Interferometrie mit kontrollierbarer Phasendifferenz Δφ.

---

## Kategorie 2: Simulationen mit öffentlichen Daten

### RT-04 — FLRW-Simulation mit SI-Einheiten (Friedmann-Gleichung)
**Motivation:** h0_scan.py arbeitet dimensionslos ohne physikalische Einheitenbrücke (K-4).
**Aufgabe:** Neuer FLRW-Solver in SI-Einheiten mit H₀ in s⁻¹ aus Friedmann-Gleichung.
**Daten:** Planck-2018-Kosmologieparameter (öffentlich: https://pla.esac.esa.int)
**Code:** Python mit `astropy.cosmology` als Referenzimplementierung.
**Falsifizierung:** RFT-Kurve muss Planck-Fehlerbalken schneiden.

### RT-05 — CMB-Vergleich mit CAMB/CLASS
**Motivation:** generate_lcdm_bestfit() ist ein Spielzeugmodell (K-5).
**Aufgabe:** Echtzeit-ΛCDM-Spektrum via CAMB oder CLASS generieren und als Referenz nutzen.
**Daten:** Planck-2018 TT-Spektrum (öffentlich: https://pla.esac.esa.int/pla/#cosmology)
**Code:** `pip install camb` — CAMB Python-Interface verfügbar.
**Vorteil:** Δχ² wird dann gegenüber echtem ΛCDM berichtet.

### RT-06 — (γ,α)-Wirkungsquerschnitt für Am-241 aus EXFOR-Datenbank
**Motivation:** σ_photo_alpha in material.py ist nicht aus Literaturdaten (K-6).
**Aufgabe:** (γ,α)-Querschnittsdaten für Am-241 und U-235 aus EXFOR laden und einsetzen.
**Daten:** EXFOR-Datenbank (öffentlich: https://www-nds.iaea.org/exfor/)
**Code:** Python-Skript zum EXFOR-API-Abruf und Integration in material.py.

### RT-07 — Unabhängiger η-Estimator in FLRW-Simulationen
**Motivation:** Pearson-Estimator ist algebraisch äquivalent zu cos²(Δφ/2) (K-2).
**Aufgabe:** Drei alternative Estimatoren implementieren und vergleichen:
  1. Energietransfer-Rate: ΔE₁₂ / (E₁ + E₂)
  2. Mutual Information: MI(ε₁, ε₂) via Histogramm
  3. Phase Locking Value: PLV = |⟨exp(i·Δφ)⟩|
**Erwartung:** Alle drei sollten cos²(Δφ/2) approximieren — falls nicht, muss
ε = η neu bewertet werden.
**Code:** Neue Funktion `compute_eta_independent(sol)` in `coupled_flrw.py`.

### RT-08 — Doppelpendel: Experimentaldaten vs. RFT-Vorhersage
**Motivation:** ε(θ₂−θ₁) = cos²(Δθ/2) ist simuliert, aber nicht gegen
Experimentaldaten getestet.
**Daten:** Öffentliche Doppelpendel-Datensätze (z.B. Chaos-Experimente auf Zenodo).
**Aufgabe:** RFT-Kopplungseffizienz gegen gemessene Energieübertragungsraten fitten.
**Code:** Erweiterung von `doppelpendel.py` um Daten-Import und χ²-Fit.

---

## Kategorie 3: Code-Korrekturen

### RT-09 — Vollständiges Unsicherheitsbudget für Am-241-Experiment
**Motivation:** >50.000σ-Signifikanz ohne Fehlerbudget ist nicht falsifizierbar (M-4).
**Aufgabe:** Monte-Carlo-Fehlerrechnung für:
  - Detektoreffizienz (typisch 20–80%)
  - Strahlausbreitung (Gaussbreite σ_beam)
  - Kernzustandsbreite Γ_GDR = 4–5 MeV
  - Experimentell erreichbare Phasenkohärenz
**Code:** Neue Funktion `uncertainty_budget_am241()` in `resonance.py`.

### RT-10 — ResoTrade: Reproduzierbare Backtest-Implementierung
**Motivation:** 24-Monats-Backtest ist private Implementierung ohne Reproduzierbarkeit (M-5).
**Aufgabe:** Öffentlicher Backtest-Code mit:
  - Freie BTC-USDT-Daten (z.B. via `ccxt` oder Binance-API)
  - Vollständige Trade-Logs als CSV
  - Walk-Forward-Validierung (kein In-Sample-Overfitting)
**Code:** Neues Verzeichnis `en/facts/concepts/ResoTrade/backtest/`.

### RT-11 — FLRW κ-Parameter aus Axiomen ableiten
**Motivation:** κ = 1 ist im Code ein freier Parameter trotz Ableitungsanspruch (Minor-9).
**Aufgabe:** Formale Ableitung von κ = 8πG aus den RFT-Axiomen oder
explizite Deklaration als Konvention κ_RFT = 1.

---

## Kategorie 4: Experimentelle Vorhersagen (extern testbar)

### RT-12 — ⁸⁷Rb-Interferometrie-Experiment
**Vorhersage:** |Δ⟨x⟩| = 4.9·λ·ℓ (nach unabhängiger λ-Bestimmung aus RT-03)
**Einrichtung:** Atominterferometer-Labore (PTB Berlin, NIST, SYRTE Paris)
**Protokoll:** Kontrollierbare Phasendifferenz Δφ zwischen zwei Rb-Ensembles;
Messung der Schwerpunktverschiebung Δ⟨x⟩ als Funktion von Δφ.

### RT-13 — Resonanzreaktor: σ_coh vs. σ_incoh
**Vorhersage:** σ_coh(Δφ=0) > σ_incoh (RFT) vs. σ_coh = σ_incoh (Standard)
**Einrichtung:** ELI-NP (Magurele, Rumänien) — gepulste Gammastrahlung
**Protokoll:** Am-241-Probe mit kohärenter vs. inkohärenter Gammabestrahlung
bei E_γ = GDR-Energie; Messung der α-Zerfallsrate als Funktion von Δφ.

---

*Zuletzt aktualisiert: Juli 2026*
*Für Fragen und Beiträge: siehe README.md*
