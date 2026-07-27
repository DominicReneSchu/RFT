# RFT — Peer-Review-Bereitschaft: Aktueller Stand

Erstellt: Juli 2026  
Basis: Tiefenanalyse durch GitHub Copilot Deep Research Agent  
Status: Transparenzdokument — intern, nicht zur Einreichung

---

## Zusammenfassung

Die RFT ist ein eigenständig entwickeltes Framework mit ernsthafter Strukturierung,
öffentlichem Code und bemerkenswerter Selbstkritik in der Dokumentation.
Sie enthält jedoch mehrere fundamentale Probleme, die eine Einreichung bei einem
Peer-Review-Journal der Physik aktuell verhindern.

**Aktuelles Gesamturteil: Nicht peer-review-fähig (Stand Juli 2026)**  
**Projiziertes Urteil nach Umsetzung der RT-Aufgaben: Bedingt einreichbar** (siehe Abschnitt 4)

---

## 1. Axiomatik — Formaler Status

| Axiom | Inhalt | Status |
|-------|--------|--------|
| A1 | ψ(x,t) = A·cos(kx − ωt + φ) | Fourier-Theorem — mathematisch korrekt, physikalisch trivial |
| A2 | Φ = Σ ψᵢ | Standard-Superposition — unumstritten |
| A3 | \|f₁/f₂ − m/n\| < δ | Standard-Resonanz — δ undefiniert |
| A4 | E = π·ε(Δφ)·ℏ·f | **Explizites Postulat — nicht hergeleitet** |
| A5 | E⃗ = E_eff·ê(Δφ,∇Φ) | Nicht aus A1–A4 abgeleitet |
| A6 | I(X→Y) > 0 ⟺ PCI > 0 ∧ MI > 0 | Standard-Informationstheorie — kein neuer Inhalt |
| A7 | G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ)) | **Kein gruppentheoretischer Beweis vorhanden** |

**Kritisch:** A4 kodiert die Hauptbehauptung der Theorie als Axiom.
Die gesamte Validierungslast liegt damit auf empirischen Tests.

---

## 2. Kerngleichungen — Herleitung und Konsistenz

### E = π·ε·ℏ·f

Die Integration ∫₀^π cos²(φ/2) dφ = π/2 wird im Manuskript explizit als
*Motivation*, nicht als Herleitung bezeichnet. Die Normalisierung, die π·ε·ℏ·f
ergibt, setzt das Ergebnis voraus — zirkulär.

### Frequenzdefinitions-Inkonsistenz (fatal, ungelöst)

Die Definitionstabelle setzt f = E/(π·ℏ). Eingesetzt in A4:

```
E = π·ε·ℏ·[E/(π·ℏ)] = ε·E  →  ε = 1 immer
```

Die Formel wird damit trivial und vakuos. Dies ist in RESEARCH_TASKS.md RT-01
als offene Frage dokumentiert — aber noch nicht gelöst.
Kein konsistenter Grenzübergang zu E = ℏω oder E = hf existiert mit dieser Definition.

### ε = cos²(Δφ/2)

Standardformel für Leistungskopplung zweier kohärenter klassischer Oszillatoren
(= (1 + cos Δφ)/2). Keine Ableitung aus den Axiomen.

---

## 3. Zirkelschlüsse — Dokumentierte Muster

### Muster 1 — ε = η (schwerwiegend)
Der Pearson-Estimator η = 0.5·(1 + r) ist für harmonische Signale algebraisch
identisch mit cos²(Δφ/2). Die "Validierung" ε = η ist eine trigonometrische Identität,
keine Messung. Selbst dokumentiert in `coupling_efficiency.md` Z. 256–262 und
RESEARCH_TASKS.md RT-07.

### Muster 2 — GDR-Resonanzfrequenz
f_GDR = E_GDR/(π·ℏ) wird durch Invertierung von A4 gewonnen.
Der Reaktor "validiert" dann, dass Photonen bei f_GDR koppeln —
die Resonanzbedingung ist per Konstruktion erfüllt.

### Muster 3 — CMB-Fitparameter
Die η-Korrektur zum CMB verwendet Fitparameter (200.0 und 0.3) ohne physikalische
Ableitung. Der Pearson-r = 0.626 zu Planck-Residuen ist kein Vorhersagetest.

### Muster 4 — Fidelity = 1.0
Die statische Schrödinger-Simulation löst identische Differentialgleichungen
auf beiden Pfaden — Ergebnis 1.0 ist eine mathematische Tautologie
(selbst dokumentiert in `schrodinger/README.md` Z. 70–73).

---

## 4. Empirische Validierung — Qualitätsbewertung

| Domäne | Methode | Befund | Peer-Review-Wert |
|--------|---------|--------|-----------------|
| CMS Monte Carlo | KDE + Binomialtest, 1.5M Pseudo-Exp. | Bekannte SM-Resonanzen gefunden | Testet Peakfinder, nicht RFT |
| FLRW-Simulation | Gekoppelte KG-Felder, 1530 Runs | Δχ² = +16 vs. **Spielzeugmodell** | Nicht aussagekräftig |
| Resonanzreaktor | GDR-Literaturwerte + RFT-Formel | λ_eff/λ₀ = 7872 (hypothetisch) | Zirkuläre Frequenzableitung |
| Schrödinger | Split-Operator, dynamisches Feedback | Fidelity = 1.0 (statisch) | Tautologie (statisch) |

**Kein einziger Test validiert eine neue, unabhängig falsifizierbare Vorhersage
gegen ein echtes Null-Modell.**

---

## 5. Falsifizierbare Vorhersagen — Status

### Experiment I — Am-241 bei ELI-NP (RT-13)
- **Vorhersage:** σ_coh/σ_incoh = 2.0 (RFT) vs. 1.0 (Standard)
- **Status:** Nicht durchgeführt. ~30 h Strahlzeit, ~50.000 EUR.
- **Blocker:** Kein Unsicherheitsbudget (RT-09). Phasenkohärenz bei 14 MeV γ
  ist technisches Neuland. Inkonsistenz σ_GDR: 340 mb (Manuskript) vs. 120 mb
  (resonance_reactor.md) — Faktor 2,8.

### Experiment II — ⁸⁷Rb-BEC (RT-12)
- **Vorhersage:** |Δ⟨x⟩| = 4.9·λ·ℓ
- **Status:** Nicht durchgeführt. λ ist freier Parameter.
- **Blocker:** Ohne unabhängige λ-Bestimmung (RT-03) ist jedes Nicht-Null-Resultat
  mit beliebigem λ kompatibel — nicht falsifizierbar.

---

## 6. Kritische Lücken — Rangfolge nach Schwere

| # | Lücke | Schwere | Zugehörige RT |
|---|-------|---------|---------------|
| G1 | Frequenzdefinition macht A4 trivial | **Fatal** | RT-01 |
| G2 | ε = η algebraisch garantiert, kein Messresultat | **Schwerwiegend** | RT-07 |
| G3 | CMB-Δχ² gegen Spielzeugmodell, nicht ΛCDM | **Schwerwiegend** | RT-05 |
| G4 | Keine einzige neue Vorhersage experimentell getestet | **Kritisch** | RT-12, RT-13 |
| G5 | λ (Rb) nicht unabhängig bestimmt | **Kritisch** | RT-03 |
| G6 | Kein Wirkungsprinzip für A4 | Moderat | RT-01 |
| G7 | A7 ohne gruppentheoretischen Beweis | Moderat | RT-02 |
| G8 | σ_GDR inkonsistent zwischen Dokumenten (Faktor 2,8) | Moderat | RT-06 |
| G9 | ResoTrade-Backtest nicht reproduzierbar | Gering | RT-10 |

---

## 7. Was genuinen wissenschaftlichen Wert hat

Trotz der Lücken enthält die RFT substanzielle Elemente:

- **Selbstkritische Dokumentation** — Zirkularitäten, offene Ableitungen und
  Spielzeugmodell-Grenzen sind explizit markiert (ungewöhnlich für unabhängige Forschung)
- **Reproduzierbarer Simulationscode** — Alle vier Pipelines öffentlich mit
  Requirements und Runscripts
- **Konkrete Experimentalvorschläge** — Am-241/ELI-NP ist spezifisch, mit Kosten
  und Protokoll — genuiner diskriminierender Test, wenn Phasenkohärenz erreichbar
- **Störungstheorie-Konsistenz** — 1 − F ~ λ² analytisch bewiesen und numerisch
  auf 0,05% Genauigkeit bestätigt
- **Gisin-Analyse** — Korrekte Behandlung der No-Signaling-Bedingung,
  lokale Kopplung als notwendige Struktur identifiziert
- **Kohn-Theorem-Argument (⁸⁷Rb)** — Physikalisch interessant: zeitabhängige
  ε(Δφ(t))-Modulation bricht die Kohn-Bedingung prinzipiell — glaubwürdigste
  QM-Verbindung im gesamten Framework

---

## 8. Projizierter Stand nach Umsetzung der RT-Aufgaben

| Aufgabe gelöst | Lücke geschlossen | Effekt auf Peer-Review |
|----------------|-------------------|----------------------|
| RT-01 (π-Herleitung) | G1 teilweise, G6 | Formel erhält physikalische Basis |
| RT-03 + RT-07 | G2, G5 | Zentraler Zirkelschluss aufgelöst |
| RT-05 (CAMB/CLASS) | G3 | CMB-Aussage wird belastbar |
| RT-09 (Unsicherheitsbudget) | G4 teilweise | Am-241-Vorhersage wird einreichbar |
| RT-02 (Gruppentheorie) | G7 | A7 erhält mathematischen Status |
| RT-06 (EXFOR-Daten) | G8 | σ_GDR-Konsistenz hergestellt |
| RT-10 (Backtest) | G9 | ResoTrade-Abschnitt peer-review-fähig |

**Nach vollständiger Umsetzung:** Das Manuskript wäre bei einem spezialisierten
Journal (z.B. *Foundations of Physics*, *Physical Review D* als Letter,
*European Physical Journal*) einreichbar — mit realistischer Chance auf
externes Review. Annahme ohne positives Experimentalresultat (RT-12 oder RT-13)
bleibt unwahrscheinlich, aber der wissenschaftliche Diskurs wird möglich.

---

## 9. Empfohlene Prioritätenreihenfolge

```
Sofort (Code, lösbar ohne Experiment):
  RT-07 → Zirkelschluss ε = η aufbrechen
  RT-05 → CAMB/CLASS statt Spielzeugmodell
  RT-09 → Unsicherheitsbudget Am-241
  RT-06 → EXFOR-Querschnittsdaten

Mittelfristig (Theorie):
  RT-01 → π-Herleitung / Frequenzdefinition klären  ← blockiert alles andere
  RT-02 → Gruppentheoretischer A7-Beweis
  RT-11 → κ-Parameter deklarieren

Extern (Kooperation nötig):
  RT-03 → λ unabhängig bestimmen
  RT-12 → ⁸⁷Rb-Experiment (PTB/NIST/SYRTE)
  RT-13 → Am-241 bei ELI-NP
```

---

*Erstellt: Juli 2026*  
*Methode: Automatisierte Tiefenanalyse (GitHub Copilot Deep Research) + manuelle Verifikation*  
*Dieses Dokument ist ein internes Transparenzdokument und keine Peer-Review-Einreichung.*
