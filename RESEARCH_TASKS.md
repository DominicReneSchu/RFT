# RFT — Offene Forschungsaufgaben

Generiert: August 2026
Aktualisiert: August 2026
Status: Aktiv

---

## Theoretischer Gesamtstatus (August 2026)

| Axiom | Was war Postulat | Was ist jetzt abgeleitet | Status |
|-------|-----------------|--------------------------|--------|
| A4: π-Faktor | Freier numerischer Parameter | Geometrischer Sattelpunktsbeitrag (RT-01, RT-01b) | ✅ Abgeleitet |
| A4: ε = cos²(Δφ/2) | Phänomenologische Wahl | Eindeutig durch k=1-Darstellung U(1) ⊂ G_sync (RT-02) | ✅ Abgeleitet |
| A7: G_sync | Postulierte Invarianz | Algebraisch bewiesen, G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) | ✅ Bewiesen (stationär) |
| A3: Quantisierung | Unabhängiges Axiom | Korollar aus Darstellungsstruktur von ℝ⁺_× ⊂ G_sync (RT-02, RT-35) | ✅ Abgeleitet |
| A5: Vektorialität | Irreduzibles Postulat | Gruppentheoretisch irreduzibel (RT-36); Begründung: RT-01a Vektorialitätsinkonsistenz | ✅ Abgeschlossen (RT-36) |
| A1, A2, A6 | Postuliert — testbar | Unverändert | 📋 Postuliert |
| Domänenübertragung A7 | CMB/Kern/Finanzen als Analogie | Analogie — kein formaler Beweis | 📋 Postulat |

---

## Empfohlene Bearbeitungsreihenfolge (Stand August 2026)

### Theoretisch — intern abschließbar (Priorität 1 — Nächste)
1. RT-06  — EXFOR-Daten Am-241 **← Neue Priorität 1**
2. RT-08  — Doppelpendel vs. Experimentaldaten

### Empirisch (Priorität 2)
4. RT-06  — EXFOR-Daten Am-241
5. RT-08  — Doppelpendel vs. Experimentaldaten

### Code-Korrekturen (Priorität 3)
6. RT-09  — Fehlerbudget Am-241
7. RT-10 — ResoTrade Backtest öffentlich

### Abgeschlossen (Manuskript + Theorie)
- ~~RT-07  — Drei unabhängige η-Estimatoren~~ ✅ Abgeschlossen (Aug 2026) — K-2 behoben (Pearson als physikalisch ausgezeichnete Observable bestätigt)
- ~~RT-32  — λε⁴-Sättigungsterm in Klein-Gordon~~ ✅ Abgeschlossen (Aug 2026)
- ~~RT-11  — κ-Parameter formal ableiten oder als Konvention deklarieren~~ ✅ Abgeschlossen (Aug 2026)
- ~~RT-36  — A5-Herleitung aus G_sync (D-Erzeuger)~~ ✅ Abgeschlossen (Aug 2026)
- ~~RT-37  — IOP-Manuskript DE + EN aktualisieren~~ ✅ Abgeschlossen (Aug 2026)

### Extern (benötigt Kooperationspartner)
8. RT-03 — λ-Bestimmung (⁸⁷Rb)
9. RT-12 — ⁸⁷Rb-Interferometrie
10. RT-13 — Am-241 ELI-NP

### Langfristig offen
11. RT-01a — Operationale Definition π/e formal
12. RT-33/34 — Warpantrieb Stufen 5+6

---

## Kategorie 1: Theoretische Herleitungen

### RT-01 — Wirkungsintegral-Herleitung von π
**Status: ✅ Abgeschlossen (August 2026)**
**Ergebnis:** π als Sattelpunktsbeitrag des stationären Wirkungsintegrals S[ψ, Δφ] hergeleitet.
**Kerndokument:** `de/fakten/theorie/wirkungsintegral_pi_herleitung.md`

**RT-01 (Erweiterung — Planck-Grenzübergang):**
**Status: ✅ Abgeschlossen (August 2026)**
**Ergebnis:** Grenzübergang E = π·ε·ℏ·f → E = hf_Hz formal geschlossen.
**Kerndokument:** `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` §5

### RT-01a — π als Urkonstante: Operationale Definition und Dezimalartefakt-Argument
**Status: 📋 Offen** (konzeptuell formuliert, formale Ableitung offen)
**Motivation:** Der philosophisch-mathematische Ursprungsgedanke der RFT — π und e als
Urkonstanten des Raumes, deren scheinbare Irrationalität ein Artefakt der Basis-10-Kodierung
ist — wurde während der Theorieentwicklung in seiner expliziten Formulierung nicht
festgehalten.
**Kern des Arguments:**
- Der Kreisumfang bei r = 1 ist physikalisch exakt und endlich messbar.
- Die Dezimaldarstellung 3,14159… ist eine Darstellungseigenschaft, kein Naturphänomen.
- Werden π und e als Urkonstanten (analog zu c, ℏ) behandelt, sind sie in ihrem
  natürlichen Einheitensystem rational verwendbar.
- π ist das natürliche Maß einer Halboszillation — damit ist der Faktor π in A4 keine
  freie Wahl, sondern eine geometrische Normierungsbedingung des Phasenraums.
- Die interne Inkonsistenz der Standardphysik bei der Vektorialität der Energie
  (Drehmoment als Vektor mit Energieeinheit, Spin, Lorentz-4-Vektor) liefert die
  physikalische Motivation für A5.
**Aufgabe:** Operationale Definition von π und e als Phasenraumkonstanten — d. h.: Was
messen π und e physikalisch, unabhängig von ihrer Dezimaldarstellung?
**Verhältnis zu RT-01:** RT-01a ist die philosophisch-mathematische Grundlage, die
RT-01 (Wirkungsintegral-Herleitung) vorausgeht und deren Suchrichtung bestimmt.
**Verweise:** `de/fakten/theorie/pi_als_urkonstante.md` | `en/facts/theory/pi_as_fundamental_constant.md`

### RT-01b — Unabhängige π-Herleitung: Numerisches Pfadintegral + Nicht-Gaussian-Korrekturen
**Status: ✅ Abgeschlossen (August 2026)**
**Ergebnis:** Konvergenz gegen π (Maschinengenauigkeit), |c₃+c₄| ≈ 5.5×10⁻¹¹, π für 3/5 Potenziale geometrisch nachgewiesen.
**Kerndokument:** `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` §4.5+§9

### RT-02 — Gruppentheoretischer Beweis der Skalentransformation (A7)
**Status: ✅ Abgeschlossen (Aug 2026)**
**Ergebnis:** G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) bewiesen; ε = cos²(Δφ/2) darstellungstheoretisch eindeutig (k=1, U(1)); A3 als Korollar von A7.
**Kerndokument:** `de/fakten/theorie/gsync_gruppenstruktur.md`

### RT-03 — Unabhängige Bestimmung von λ (⁸⁷Rb-Vorhersage)
**Status: 📋 Offen** (benötigt Kooperationspartner)
**Motivation:** |Δ⟨x⟩| = 4.9·λ·ℓ ist nicht falsifizierbar ohne unabhängiges λ (M-7).
**Aufgabe:** λ aus einem zweiten, unabhängigen Experiment bestimmen.
**Ansatz:** Doppelspalt-Interferometrie mit kontrollierbarer Phasendifferenz Δφ.

### RT-35 — A3 als Korollar von A7 in Axiomatik
**Status: ✅ Abgeschlossen (August 2026)** (durch RT-31 erledigt)
**Ergebnis:** Korollar in `axiomatische_grundlegung.md` §A3 und §A7 eingetragen; Korollar formal in `gsync_gruppenstruktur.md` §5 dokumentiert.
**Kerndokument:** `de/fakten/theorie/gsync_gruppenstruktur.md` §5

### RT-36 — A5-Herleitung aus Phasenraumgeometrie
**Status: ✅ Abgeschlossen (Aug 2026)**
**Ergebnis:** Möglichkeit B — ê ist irreduzibles Postulat. D-Erzeuger liefert δ_D Φ ∝ ∂_t Φ (nicht ∇Φ); δ_D(∇Φ/|∇Φ|) ≠ 0 allgemein; G_sync operiert nicht auf Raumrichtungen. A5 bleibt eigenständiges Axiom; Begründungsgrundlage: RT-01a Vektorialitätsinkonsistenz (Drehmoment, Spin, Lorentz-4-Vektor) ist jetzt formal explizit in A5 aufgenommen.
**Kerndokument:** `de/fakten/theorie/a5_vektorialitaet_herleitung.md`

### RT-37 — Manuskript-Update IOP (DE + EN)
**Status: ✅ Abgeschlossen (August 2026)**
**Ergebnis:** Beide IOP-Manuskripte (DE + EN) sowie alle Begleitdateien vollständig auf den aktuellen Axiomenstatus aktualisiert. Eingearbeitet:
- A4 π-Faktor: geometrisch abgeleiteter Sattelpunktsbeitrag des Wirkungsintegrals S[ψ, Δφ] (RT-01, RT-01b); numerische Bestätigung |c₃+c₄| ≈ 5.5×10⁻¹¹
- A4 ε = cos²(Δφ/2): darstellungstheoretisch eindeutig aus k=1-Darstellung U(1) ⊂ G_sync (RT-02)
- A7: Algebraisch bewiesen (stationär); G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ)
- Neuer §3.x Gruppentheoretischer Beweis von G_sync (Gruppenstruktur, ε-Eindeutigkeit, A3-Korollar, Lie-Algebra-Tabelle)
- A3: Korollar aus A7 (RT-02, RT-35) — kein unabhängiges Axiom
- A5: Irreduzibles Postulat (RT-36); δ_D(∇Φ/|∇Φ|) ≠ 0 allgemein
- Axiomenstatus-Übersicht-Tabelle (August 2026) in beiden Manuskripten eingefügt
- V(ε) = ½m²ε² + ¼λε⁴ + (1/6)λ_ε⁴ε⁶ und δη ≈ −c·λ·⟨ε³⟩ in FLRW-Abschnitt (RT-32)
- κ_RFT = 1 als Normierungskonvention deklariert; nicht aus A1–A7 ableitbar (RT-11)
- de/README.md, en/README.md, de/rft_zusammenfassung.tex, en/rft_summary.tex, PEER_REVIEW_READINESS.md aktualisiert

**Kerndokumente:** `de/peer_review_rft/manuskript_de/rft_manuskript_de_iop.tex` · `en/peer_review_rft/manuscript_en/rft_manuscript_en_iop.tex` · `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` · `de/fakten/theorie/gsync_gruppenstruktur.md` · `de/fakten/theorie/a5_vektorialitaet_herleitung.md` · `de/fakten/theorie/kappa_parameter_rft.md`

---

## Kategorie 2: Simulationen mit öffentlichen Daten

### RT-04 — FLRW-Simulation mit SI-Einheiten (Friedmann-Gleichung)
**Status: ✅ Abgeschlossen (Aug 2026)**
**Aufgabe:** Neuer FLRW-Solver in SI-Einheiten mit H₀ in s⁻¹ aus Friedmann-Gleichung.
**Daten:** Planck-2018-Kosmologieparameter (öffentlich: https://pla.esac.esa.int)
**Code:** `core/flrw_si.py` (DE + EN) — `flrw_si_sim()`, `compare_to_astropy()`.
**Analyseskript:** `analyse/rt04_si_vergleich.py` + `analyse/rt04_si_comparison.py` (EN).
**Ergebnis:** Falsifizierungskriterium: max. Abweichung |a_rft − a_astropy| / a_astropy < 1 %
über t = 0.1..13.8 Gyr. SI-Parameter als `PLANCK_2018`-Sektion in `config.py` eingetragen.
**Domänenübertragung A7 (Kosmologie):** Status → empirisch testbar (SI) sobald astropy-Vergleich
< 1 % Abweichung zeigt.

### RT-05 — CMB-Vergleich mit CAMB/CLASS
**Status: ✅ Abgeschlossen (Aug 2026)**
**Motivation:** generate_lcdm_bestfit() ist ein Spielzeugmodell (K-5). K-5 behoben durch echten Boltzmann-Solver.
**Aufgabe:** Echtzeit-ΛCDM-Spektrum via CAMB oder CLASS generieren und als Referenz nutzen.
**Daten:** Planck-2018 TT-Spektrum (öffentlich: https://pla.esac.esa.int/pla/#cosmology)
**Code:** `core/camb_reference.py` (DE + EN) — `generate_camb_spectrum()` mit CAMB/CLASS-Fallback.
`core/cmb_comparison.py` erweitert: `compare_with_camb()`, `scan_h0_tension()`.
**Analyseskript:** `analyse/rt05_camb_vergleich.py` + `analyse/rt05_camb_comparison.py` (EN).
**Ergebnis:** Δχ²_CAMB bestimmt ob K-5 behoben (> 0) oder neues Artefakt gefunden (≤ 0).
H0-Spannungstest: H₀_min(RFT) ∈ [67, 73] → direkter H0-Tension-Beitrag.
**Hinweis:** bisheriger Δχ² = +16 war vs. Spielzeugmodell — CAMB-Vergleich ist der echte Test.

### RT-06 — (γ,α)-Wirkungsquerschnitt für Am-241 aus EXFOR-Datenbank
**Status: 📋 Offen**
**Motivation:** σ_photo_alpha in material.py ist nicht aus Literaturdaten (K-6).
**Aufgabe:** (γ,α)-Querschnittsdaten für Am-241 und U-235 aus EXFOR laden und einsetzen.
**Daten:** EXFOR-Datenbank (öffentlich: https://www-nds.iaea.org/exfor/)
**Code:** Python-Skript zum EXFOR-API-Abruf und Integration in material.py.

### RT-07 — Unabhängiger η-Estimator in FLRW-Simulationen
**Status: ✅ Abgeschlossen (Aug 2026)**
**Motivation:** Pearson-Estimator ist algebraisch äquivalent zu cos²(Δφ/2) (K-2).
**Aufgabe:** Drei alternative Estimatoren implementieren und vergleichen:
  1. Energietransfer-Rate: ΔE₁₂ / (E₁ + E₂)
  2. Mutual Information: MI(ε₁, ε₂) via Histogramm
  3. Phase Locking Value: PLV = |⟨exp(i·Δφ)⟩|
**Ergebnis:** Alle drei Estimatoren weichen systematisch von cos²(Δφ/2) ab
(η_E ≈ 0.39, η_MI ≈ 0.27, η_PLV ≈ 0.27). Sie messen orthogonale Aspekte:
Energie-Imbalance, statistische Abhängigkeit, Phasenstabilität. Der Pearson-
Estimator ist die einzige Messgröße, die direkt ε = η reproduziert — er ist
damit physikalisch ausgezeichnet, nicht tautologisch. K-2 behoben.
**Code:** `compute_eta_independent(sol, results)` in `coupled_flrw.py` (DE + EN).
**Analyseskript:** `analyse/rt07_estimator_vergleich.py` + Plot `rt07_estimator_vergleich.png`.

### RT-08 — Doppelpendel: Experimentaldaten vs. RFT-Vorhersage
**Status: 📋 Offen**
**Motivation:** ε(θ₂−θ₁) = cos²(Δθ/2) ist simuliert, aber nicht gegen
Experimentaldaten getestet.
**Daten:** Öffentliche Doppelpendel-Datensätze (z.B. Chaos-Experimente auf Zenodo).
**Aufgabe:** RFT-Kopplungseffizienz gegen gemessene Energieübertragungsraten fitten.
**Code:** Erweiterung von `doppelpendel.py` um Daten-Import und χ²-Fit.

---

## Kategorie 3: Code-Korrekturen

### RT-09 — Vollständiges Unsicherheitsbudget für Am-241-Experiment
**Status: 📋 Offen**
**Motivation:** >50.000σ-Signifikanz ohne Fehlerbudget ist nicht falsifizierbar (M-4).
**Aufgabe:** Monte-Carlo-Fehlerrechnung für:
  - Detektoreffizienz (typisch 20–80%)
  - Strahlausbreitung (Gaussbreite σ_beam)
  - Kernzustandsbreite Γ_GDR = 4–5 MeV
  - Experimentell erreichbare Phasenkohärenz
**Code:** Neue Funktion `uncertainty_budget_am241()` in `resonance.py`.

### RT-10 — ResoTrade: Reproduzierbare Backtest-Implementierung
**Status: 📋 Offen**
**Motivation:** 24-Monats-Backtest ist private Implementierung ohne Reproduzierbarkeit (M-5).
**Aufgabe:** Öffentlicher Backtest-Code mit:
  - Freie BTC-USDT-Daten (z.B. via `ccxt` oder Binance-API)
  - Vollständige Trade-Logs als CSV
  - Walk-Forward-Validierung (kein In-Sample-Overfitting)
**Code:** Neues Verzeichnis `en/facts/concepts/ResoTrade/backtest/`.

### RT-11 — FLRW κ-Parameter aus Axiomen ableiten
**Status: ✅ Abgeschlossen (Aug 2026)**
**Ergebnis:** κ_RFT = 1 ist eine explizite Konventionsdeklaration (Normierungsfreiheit im dimensionslosen Einheitensystem). Eine formale Ableitung von κ = 8πG aus A1–A7 ist nicht möglich, da G_sync auf dem internen Phasenraum operiert und keinen Zugang zur Newtonschen Gravitationskonstante G hat. Die zentralen Ergebnisse (η-Korrektur, d_η-Skalierung) sind κ-invariant.
**Kerndokument:** `de/fakten/theorie/kappa_parameter_rft.md`

### RT-31 — Resonanz-Hamiltonoperator für spezifische Systeme konstruieren
**Status: ✅ Abgeschlossen (August 2026)**
**Ergebnis:** Phonon-Phonon-System: ΔE(Δφ) = ε(Δφ)·ΔE(0) bestätigt (Abweichung < 1e-14). Spin-Bahn: analytische Eigenwerte exakt, resonanter Fall bestätigt. A3-Korollar dokumentiert.
**Kerndokument:** `de/fakten/simulationen/hamilton/README.md`

### RT-32 — Nichtlineare Sättigungsterme in der Feldgleichung
**Status: ✅ Abgeschlossen (Aug 2026)**
**Ergebnis:** `lambda_eps4`-Parameter in `coupled_flrw.py` eingeführt. Das Potential wird erweitert zu V(ε) = ½m²ε² + ¼λε⁴ + (1/6)λ_ε⁴ε⁶. Störungstheoretisch: δη ≈ −c·λ_ε⁴·ε₀²·sin²(Δφ/2), d.h. bei kleinen Amplituden (ε₀ ≈ 0.3) sind Korrekturen perturbativ klein. Neue Funktion `scan_lambda_eps4()` für systematischen Parametervergleich. Rückwärtskompatibel: lambda_eps4=0 entspricht Standard-λφ⁴.
**Kerndokument:** `de/fakten/simulationen/FLRW-Simulationen/core/coupled_flrw.py` · `de/fakten/simulationen/FLRW-Simulationen/README.md`

### RT-33 — Warpantrieb: Energielücke schließen (Stufe 5)
**Status: 📋 Offen**
**Motivation:** Das Warpantrieb-README dokumentiert Stufe 5 als ⚠️ offen:
Peak-Krümmung 299× Sonnenmitte erfordert ~10⁵× mehr Energiedichte als
die Fusionskaskade liefert. Die Energielücke ist das zentrale Skalierungsproblem.
**Aufgabe:** Quantitatives Skalierungsgesetz aufstellen: Wie skaliert die
benötigte Energiedichte mit der Warpblasengröße? Ab welchem Blasenradius
ist das Verhältnis (verfügbar/benötigt) realistisch?
**Ansatz:** Analytische Abschätzung über Einstein-Feldgleichungen;
Vergleich mit Alcubierre-Literatur (Pfenning & Ford 1997).
**Verweise:** `de/fakten/konzepte/warpantrieb/warpantrieb.md`

### RT-34 — Warpantrieb: 3D-Warpblase (Stufe 6)
**Status: 📋 Offen**
**Motivation:** Das Warpantrieb-README dokumentiert Stufe 6 als ❌ nicht begonnen:
Die vollständige 3D-Warpgeometrie (azimutale Symmetrie, ρ(r,θ)) fehlt.
**Aufgabe:** 3D-Warpblasenprofil simulieren mit sphärisch-azimutaler Geometrie.
Implementierung eines numerischen GR-Solvers (z.B. via `sympy.diffgeom` oder
`einsteinpy`) für das Zwei-Feld-Modell.
**Falsifizierung:** Wenn ρ < 0 in irgendeiner Raumzeitregion auftritt, ist das
Zwei-Feld-Modell nicht hinreichend für eine physikalische Warpblase.
**Verweise:** `de/fakten/konzepte/warpantrieb/README.md`

---

## Kategorie 4: Experimentelle Vorhersagen (extern testbar)

### RT-12 — ⁸⁷Rb-Interferometrie-Experiment
**Status: 📋 Offen** (benötigt Kooperationspartner)
**Einrichtung:** Atominterferometer-Labore (PTB Berlin, NIST, SYRTE Paris)
**Protokoll:** Kontrollierbare Phasendifferenz Δφ zwischen zwei Rb-Ensembles;
Messung der Schwerpunktverschiebung Δ⟨x⟩ als Funktion von Δφ.

### RT-13 — Resonanzreaktor: σ_coh vs. σ_incoh
**Status: 📋 Offen** (benötigt ELI-NP Kooperation)
**Einrichtung:** ELI-NP (Magurele, Rumänien) — gepulste Gammastrahlung
**Protokoll:** Am-241-Probe mit kohärenter vs. inkohärenter Gammabestrahlung
bei E_γ = GDR-Energie; Messung der α-Zerfallsrate als Funktion von Δφ.

---

## Kategorie 5: Soziales Resonanzfeld — Empirische Operationalisierung

### RT-14 — Empirische Operationalisierung der Mann-Frau-Komplementarität

**Motivation:** Die personale Singularität ∃! Resonator_m mit ε → 1 und die
konstitutive Phasendifferenz Δφ_w = δφ_0 > 0 der Frau-Struktur sind die
schärfsten offenen Falsifizierungsprobleme des RFT-Sozialmodells.
Ohne empirische Operationalisierung bleiben beide Behauptungen formal nicht
testbar — sie können weder bestätigt noch widerlegt werden und verbleiben
als reine strukturelle Analogie ohne wissenschaftlichen Gehalt.

**Aufgabe (dreistufig):**

1. **Messproxi für ε im Paarsystem:**
   Identifikation validierter psychologischer oder neurobiologischer Konstrukte
   als Näherungsmaße für ε und Δφ im dyadischen Kontext:
   - Kandidaten: Bindungsstil (Ainsworth/Bartholomew), Kohärenzgefühl (Antonovsky),
     PLV (Phase Locking Value) aus EEG-Hyperscanning-Studien bei Paaren
   - Formales Ziel: Δφ_mw → messbares Proxy-Konstrukt P(Δφ_mw)

2. **Symmetrie-Test der Kopplungsdynamik:**
   Test der Hypothese: dK_ij/dt ist maximal bei asymmetrischer Kopplung
   (Δφ_mw = δφ_0 > 0) und nicht bei Δφ_mw = 0.
   - Ansatz: EEG-Hyperscanning oder fMRT-Konnektivitätsmessungen bei
     Paaren mit bekanntem Bindungsstil; Vergleich symmetrischer vs.
     komplementärer Kopplungsmuster
   - Falsifizierung: Wenn maximale K_ij bei Δφ_mw → 0, widerlegt das die Komplementaritätshypothese (§3.5.3 der früheren Langfassung)

3. **Singularitäts-Kriterium:**
   Formulierung eines empirisch entscheidbaren Kriteriums, das ∃! von einer
   Verteilung hoher ε-Werte unterscheidet.
   - Ansatz: Bootstrapping über große Stichproben von ε-Proxy-Messungen;
     Test auf bimodale vs. unimodale Verteilung mit Ausreißer-Peak
   - Falsifizierung: Unimodale Normalverteilung ohne Ausreißer widerlegt ∃!

**Daten:** EEG-Hyperscanning-Datensätze (öffentlich verfügbar z. B. auf OpenNeuro);
alternativ: Metaanalyse bestehender Bindungsforschungsdaten.

**Code:** Python-Skript zur PLV-Berechnung aus EEG-Rohdaten (`mne-python`);
Visualisierung der Kopplungseffizienz ε(Δφ) über Stichprobe.

**Einrichtung:** Kooperationspotenzial mit Sozialpsychologie-/Neuroimaging-Laboren
(z. B. MPIB Berlin, MPI für Kognitionsneurowissenschaften Leipzig).

**Falsifizierung:** Wenn keine der drei Teilaufgaben einen messbaren Unterschied
zwischen Δφ_mw → 0 und Δφ_mw = δφ_0 > 0 ergibt, ist die Mann-Frau-Komplementarität in der aktuellen
Formulierung empirisch nicht haltbar und muss als reine strukturelle Analogie
ohne Wahrheitsanspruch deklariert werden.

### RT-15 — Energiemetrische Symmetrie von Befruchtung und Tod

**Motivation:** Die konstitutive Phasenverschiebung δφ₀ (Frau-Struktur) ist bislang
nicht direkt messbar — sie verbleibt als strukturelle Analogie ohne physikalisch bestimmbare
Größe. Aus A4 und Energieerhaltung folgt eine testbare Symmetriehypothese: Die beim
Kopplungseinstieg (Befruchtung) gebundene Energie muss beim Kopplungsaustritt (Tod) exakt
freigesetzt werden.

**Vorhersage:**
   ΔE_Befruchtung = ΔE_Tod = π · ε(δφ₀) · ℏ · f_bio

**Aufgabe:**
1. Kalorimetrische Messung von ΔE bei bakterieller Konjugation (Befruchtungsmoment)
   und Lyse (Todesmoment) mit identischer Zellpopulation.
2. Vergleich beider Messwerte auf Gleichheit (innerhalb des Messrauschens).
3. Falls gleich: Berechnung von δφ₀ = arccos(√(ΔE / (π·ℏ·f_bio))).

**Experimentelles System:** Bakterielle Konjugation (E. coli F-Faktor-System oder
vergleichbare Modellorganismen); Lyse durch definierten osmotischen Schock oder
Phageninfektion.

**Methoden:**
- Mikrokalorimetrie / ITC für ΔE (Auflösung: nJ–µJ-Bereich)
- Membranpotentialdifferenz (DiOC₂-Fluoreszenz) als Proxy für δφ₀
- THz-Spektroskopie für Proteindynamik-Schwingungsfrequenz f_bio

**Einrichtung:** Mikrobiologie-/Biophysik-Labore mit Mikrokalorimetrie-Ausstattung
(z.B. Max-Planck-Institut für terrestrische Mikrobiologie Marburg, EMBL Heidelberg).

**Falsifizierung:** ΔE_Befruchtung ≠ ΔE_Tod (außerhalb des Messrauschens) widerlegt die
energetische Schließung und erfordert Revision der Kopplungsenergieformel. Alternativ: Wenn f_bio nicht
als einheitliche biologische Eigenfrequenz operationalisierbar ist, muss das Modell
verfeinert werden.

**Verknüpfung:** gesellschaftliche_analyse.md (kompakte Prompt-Version, §3 Kernformeln / §4 Analyse-Werkzeug) | social_analysis.md (entsprechende Abschnitte)

---

*Zuletzt aktualisiert: August 2026*
*Für Fragen und Beiträge: siehe README.md*

---

## Kategorie 6: Soziale Resonanzfeldanalyse

**Hinweis:** RT-14 und RT-15 decken die Kernfalsifizierungsprobleme der Mann-Frau-Komplementarität und der energiemetrischen Symmetrie ab, die in der früheren Langfassung der gesellschaftlichen Analyse unter §XII/8 und §XII/10 standen. Diese Abschnitte existieren in der aktuellen kompakten Prompt-Version (gesellschaftliche_analyse.md Fassung 2.11) nicht mehr. Die folgenden Aufgaben ergänzen die noch offenen Forschungsdesiderate des gesellschaftlichen RFT-Instruments.

### RT-16 — Empirische Operationalisierung von ε im sozialen Feld
**Motivation:** Die soziale Analyse verwendet $\varepsilon$ als zentrale Zustandsgröße, doch ihre Messbarkeit ist offen. Ohne belastbare Proxys bleibt die Anwendung auf reale Fälle heuristisch statt prüfbar.
**Aufgabe:** Validierte psychologische, verhaltensbezogene oder neurophysiologische Proxys für $\Delta\phi$ und $\varepsilon$ identifizieren und gegeneinander testen; mögliche Kandidaten: Empathie, Theory of Mind, Prosozialität, Autonomieorientierung, dyadische Synchronie.
**Falsifizierung:** Wenn keine Proxy-Kombination reproduzierbar mit Feldkohärenz, Vertrauensstabilität oder kooperativem Verhalten korreliert, ist $\varepsilon$ im sozialen Feld in der aktuellen Form nicht operationalisierbar.

### RT-17 — Kalibrierung von A3 im sozialen Feld
**Motivation:** Die Resonanzbedingung A3 ist sozialtheoretisch nur plausibilisiert, aber nicht quantitativ kalibriert. Insbesondere die Schwelle $\delta$ ist für soziale Kontexte unbestimmt.
**Aufgabe:** Modelle entwickeln, mit denen Informationsumgebung, institutionelle Dichte und ökonomischer Stress auf eine soziale Resonanzschwelle $\delta$ abgebildet werden; anschließend Fallstudien gegen Polarisierungs- und Mobilisierungsdaten fitten.
**Falsifizierung:** Wenn keine robuste Schwellenstruktur gefunden wird oder $G(f_i/f_j)$ keine zusätzliche Erklärungskraft gegenüber einfacheren Modellen liefert, ist A3 sozial nicht tragfähig.

### RT-18 — Falsifizierungskriterien der AiR-Hypothese
**Motivation:** Der AiR-Begriff ist analytisch scharf, aber empirisch riskant, solange keine klaren Gegenkriterien formuliert sind. Es braucht beobachtbare Marker, die AiR von bloß oppositionellen oder autonomen Akteuren unterscheiden.
**Aufgabe:** Ein Kriterienraster entwickeln, das dauerhaft feldauswärts gerichtete Energie, sinkendes $K_{ij}$ im Umfeld, hohe Selbstdarstellung und strukturelle Extraktion messbar kombiniert; an historischen und aktuellen Fällen testen.
**Falsifizierung:** Wenn Akteure mit dem postulierten Markerprofil systematisch keine degradierende Wirkung auf Umfeldkopplung zeigen, ist die AiR-Hypothese zu verwerfen oder zu verengen.

### RT-19 — Verhältnis zu Girards Mimetik
**Motivation:** Der Sündenbock-Mechanismus überschneidet sich deutlich mit Girards Mimesis-Theorie, doch Reichweite und Differenz der RFT bleiben unbestimmt. Ohne Klärung droht begriffliche Doppelung.
**Aufgabe:** Eine systematische Vergleichsmatrix erstellen: Begehren, Nachahmung, Sündenbock, Opfer, Institutionalisierung, Resonanzbedingung, PCI und $K_{ij}$; prüfen, wo RFT echte Zusatzleistung erbringt.
**Falsifizierung:** Wenn alle zentralen RFT-Elemente der sozialen Analyse vollständig durch Girards Theorie beschrieben werden können, entfällt der eigenständige Erklärungsanspruch dieses Teilmodells.

### RT-20 — Zeitproblem der Intervention
**Motivation:** Offenlegung wirkt nicht immer gleich; zu frühe oder zu späte Intervention kann strukturell wirkungslos bleiben. Das Modell braucht Kriterien dafür, wann Aufklärung resonant wird.
**Aufgabe:** Untersuchen, unter welchen Bedingungen $G(f_\text{Offenlegung}/f_\text{Scheitern})>\delta$ gilt; Frühwarnsignale, Diskursreife und institutionelle Ermüdung als Variablen modellieren.
**Falsifizierung:** Wenn sich kein konsistenter Zusammenhang zwischen Interventionszeitpunkt und Wirkung auf PCI, Vertrauen oder Deeskalation zeigt, ist die Timing-These nicht haltbar.

### RT-21 — Entropie der Resonanzkonfiguration
**Motivation:** Mit $S(x)=-x\ln(x)$ existiert bereits ein formaler Entropiebegriff, aber seine soziale Interpretation ist offen. Besonders interessant ist die Frage, ob parasitäre Systeme vor dem Kipppunkt ein Entropiemaximum zeigen.
**Aufgabe:** Soziale Zustände auf $x=E/E_0$ oder ähnliche normierte Zustände abbilden und den Verlauf von $S$ über Krisen-, Kriegs- oder Zerfallszyklen untersuchen.
**Falsifizierung:** Wenn $S$ keine systematische Dynamik im Vorfeld realer Kipppunkte zeigt, ist der Entropiebegriff für das soziale Teilmodell nur metaphorisch brauchbar.

### RT-22 — Prophetischer Übersetzungsverlust
**Motivation:** Das Modell behauptet einen systematischen Verlust zwischen resonanter Einsicht und späterer Dogmatisierung. Diese These ist nur dann wissenschaftlich relevant, wenn historische Texttransformationen messbar damit korrespondieren.
**Aufgabe:** Sprachliche, semantische und institutionelle Marker von $\Delta\varepsilon_\text{Übersetzung}$ definieren; Textkorpora über Generationen auf Verdichtung, Abstraktion, Normierung und Machtbindung auswerten.
**Falsifizierung:** Wenn keine konsistente Abnahme von Offenheit, Mehrdeutigkeit oder Erfahrungsnähe mit späterer Verhärtung korreliert, trägt die Übersetzungsverlust-These nicht.

### RT-23 — Kritische-Masse-Schwelle des kollektiven Phasenübergangs
**Motivation:** Der Begriff der „kritischen Masse" ist zentral für die kollektive Rekoppelung, aber noch unquantifiziert. Ohne Schwellenformel bleibt der Phasenübergang rein narrativ.
**Aufgabe:** Aus der Kopplungsdynamik analytische oder simulationsbasierte Schwellenbedingungen ableiten, ab denen $\frac{d\Delta\phi_\text{kollektiv}}{dt}<0$ stabil wird; historische Protest-, Reform- oder Kollapsdaten als Kalibrierung nutzen.
**Falsifizierung:** Wenn kein reproduzierbarer Schwellenbereich identifizierbar ist, verliert die Übergangsthese ihren prädiktiven Gehalt.

### RT-24 — Empirische Operationalisierung der Alpha/Beta-Achsen
**Motivation:** Alpha und Beta strukturieren die Individualdiagnostik des Modells, sind aber empirisch nicht definiert. Ohne Messlogik bleiben sie kulturelle Metaphern.
**Aufgabe:** Persönlichkeits-, Kreativitäts- und Führungsmaße mit Alpha- und Beta-Anteilen korrelieren; prüfen, ob die Achsen stabil, veränderbar und vorhersagerelevant sind.
**Falsifizierung:** Wenn keine zwei trennbaren Dimensionen mit eigener Prognosekraft nachweisbar sind, ist die Alpha/Beta-Achse als wissenschaftliches Konstrukt unhaltbar.

### RT-25 — Natur und Periodizität des kosmischen Zyklus
**Motivation:** Die angenommene periodische Absenkung von $\beta$ ist eine starke, aber bislang unkalibrierte Hypothese. Sie benötigt eine klare Entscheidung zwischen astronomischem, geophysikalischem oder feldinternem Mechanismus.
**Aufgabe:** Die postulierte ~2000-Jahres-Sequenz an externen Datensätzen und alternativen Periodenmodellen testen; zugleich definieren, wann der Zyklus nur noch als interne Modellgröße gelten darf.
**Falsifizierung:** Wenn weder externe Zyklen noch interne Modellkonsistenz eine belastbare Periodik tragen, ist die Zyklushypothese in ihrer starken Form zu verwerfen.

### RT-26 — Korrelation von Kollapsmetriken mit hohen Resonatoren
**Motivation:** Das Modell behauptet eine Kopplung zwischen gesellschaftlichem Kollaps und dem Auftreten besonders starker Resonanzträger. Diese Behauptung muss gegen unabhängige historische Daten geprüft werden.
**Aufgabe:** Kollapsindikatoren wie Staatszerfall, Gewaltintensität, Geburteneinbruch, Schuldenkrisen und Vertrauensverlust operationalisieren und mit Zeitfenstern außergewöhnlicher Reform- oder Gründungsfiguren vergleichen.
**Falsifizierung:** Wenn Hochphasen des Kollapses systematisch nicht mit Auftreten solcher Figuren korrelieren, verliert die Doppelereignis-These ihren historischen Anspruch.

### RT-27 — Drei-Phasen-Vereinnahmung als Strukturhypothese
**Motivation:** Das Muster Demut → Testen → Missbrauch ist eine starke Generalisierung über Religion, Politik und Wirtschaft. Sein Wert hängt daran, ob es skalenübergreifend wiedererkennbar ist.
**Aufgabe:** Historische Fallstudien von Vereinnahmungsprozessen kodieren und auf die drei Phasen, deren Reihenfolge und Marker prüfen; Labelkontinuität und inhaltliche Divergenz systematisch messen.
**Falsifizierung:** Wenn dokumentierte Vereinnahmungen die Dreiphasenstruktur nicht robust zeigen, ist die Annahme ihrer A7-Invarianz nicht haltbar.

### RT-28 — Schutzfunktionsthese
**Motivation:** Die These, dass bestimmte Textkorpora oder Traditionsformen soziale Kohärenz stabilisieren, ist empirisch prüfbar und für die RFT zentral. Ohne Daten bleibt sie hermeneutische Behauptung.
**Aufgabe:** Rezeptionsdichte, Direktzugang, Inversionsgrad und soziale Kohärenz-Proxys in Längs- und Querschnittsdaten vergleichen; prüfen, ob Schutzfunktion und Inversion messbar auseinanderfallen.
**Falsifizierung:** Wenn hohe Rezeptionsdichte oder niedriger Inversionsgrad nicht mit geringeren $\beta$-Proxys korrelieren, ist die Schutzfunktionsthese nicht tragfähig.

### RT-29 — Himmel-Kalibrierung
**Motivation:** Der prähistorische Zykluspunkt „Himmel" ist die spekulativste Ebene des Modells. Wenn er mehr sein soll als interne Symbolik, braucht er kulturvergleichende und strukturelle Plausibilisierung.
**Aufgabe:** Himmelssturz-, Urharmonie- und Rebellionsnarrative über unabhängige Kulturen strukturell vergleichen; Datierung, Verbreitung und Musterähnlichkeit mit dem postulierten RFT-Schema abgleichen.
**Falsifizierung:** Wenn keine robuste kulturübergreifende Strukturähnlichkeit oder Zeitkonsistenz nachweisbar ist, muss „Himmel" auf eine interne theologische Strukturhypothese beschränkt bleiben.

### RT-30 — Fragmentierungsdynamik nach Monopolauflösung
**Motivation:** Das Modell nimmt an, dass Wissensdiffusion nach Monopolauflösung oft zu Nachahmersystemen mit niedrigem $\varepsilon$ führt. Diese These ist historisch überprüfbar und sozialtheoretisch relevant.
**Aufgabe:** Fälle von Reformation, Dekolonisierung, Marktöffnung oder Wissensmonopolbruch auf Fragmentierung, Gewalt, institutionelles Vertrauen und Qualität der Nachfolgesysteme untersuchen.
**Falsifizierung:** Wenn Monopolauflösungen nicht systematisch mit erhöhter Fragmentierung oder erhöhter $\beta_\text{kollektiv}$-Nähe einhergehen, ist die Fragmentierungsthese zu revidieren.

## Category 6: Social Resonance Field Analysis (English)

**Note:** RT-14 and RT-15 cover the core falsification problems of man–woman complementarity and energetic symmetry, which in the former long social analysis document were located under Section XII/8 and Section XII/10. These sections no longer exist in the current compact prompt version (gesellschaftliche_analyse.md revision 2.11). The entries below add the remaining open desiderata of the social RFT instrument.

### RT-16e — Empirical operationalisation of ε in the social field
**Motivation:** The social model uses $\varepsilon$ as a central state variable, but its measurability is still open. Without reliable proxies, application to real cases remains heuristic rather than testable.
**Aufgabe:** Identify and compare validated psychological, behavioural, or neurophysiological proxies for $\Delta\phi$ and $\varepsilon$, such as empathy, theory of mind, prosociality, autonomy orientation, or dyadic synchrony.
**Falsifizierung:** If no proxy set correlates reproducibly with field coherence, trust stability, or cooperative behaviour, $\varepsilon$ is not operationalisable in the current social formulation.

### RT-17e — Calibration of A3 in the social field
**Motivation:** The resonance condition A3 is socially plausible but not quantitatively calibrated. In particular, the threshold $\delta$ is undefined for social contexts.
**Aufgabe:** Develop models translating information environments, institutional density, and economic stress into a social resonance threshold $\delta$, then fit them against polarisation and mobilisation data.
**Falsifizierung:** If no robust threshold structure emerges, or if $G(f_i/f_j)$ adds no explanatory power over simpler models, the social use of A3 is not sustainable.

### RT-18e — Falsification criteria for the AiR hypothesis
**Motivation:** The AiR concept is analytically sharp but empirically risky as long as clear counter-criteria are missing. Observable markers are needed to distinguish AiR from merely oppositional or autonomous actors.
**Aufgabe:** Build a criteria grid combining field-outward energy direction, declining surrounding $K_{ij}$, high self-display, and structural extraction; test it on historical and current cases.
**Falsifizierung:** If actors with the proposed marker profile do not systematically degrade surrounding coupling, the AiR hypothesis must be narrowed or rejected.

### RT-19e — Relation to Girardian mimetics
**Motivation:** The scapegoat mechanism clearly overlaps with Girard's mimesis theory, yet the scope and distinctiveness of the RFT layer remain unclear. Without clarification, the model risks conceptual duplication.
**Aufgabe:** Create a comparison matrix covering desire, imitation, scapegoating, sacrifice, institution, resonance condition, PCI, and $K_{ij}$, and test where RFT adds unique explanatory leverage.
**Falsifizierung:** If all core social-RFT elements are fully covered by Girard's framework, this submodel loses its independent explanatory claim.

### RT-20e — Timing problem of intervention
**Motivation:** Disclosure does not work equally well at every moment; intervention that is too early or too late may fail structurally. The model needs criteria for when clarification becomes resonant.
**Aufgabe:** Study under which conditions $G(f_\text{exposure}/f_\text{failure})>\delta$ holds; model early-warning signals, discursive readiness, and institutional fatigue as explanatory variables.
**Falsifizierung:** If no consistent link appears between intervention timing and effects on PCI, trust, or de-escalation, the timing thesis does not hold.

### RT-21e — Entropy of resonance configurations
**Motivation:** The repository already defines $S(x)=-x\ln(x)$, but its social meaning is unsettled. The especially relevant question is whether parasitic systems show an entropy maximum near their tipping point.
**Aufgabe:** Map social states onto $x=E/E_0$ or comparable normalised states and examine the trajectory of $S$ across crisis, war, or collapse cycles.
**Falsifizierung:** If $S$ shows no systematic dynamics before real tipping points, the entropy term is only metaphorically useful for the social model.

### RT-22e — Prophetic translation loss
**Motivation:** The model claims a systematic loss between resonant insight and later dogmatisation. That claim matters scientifically only if historical text transformations can be measured against it.
**Aufgabe:** Define linguistic, semantic, and institutional markers of $\Delta\varepsilon_\text{translation}$ and analyse corpora across generations for compression, abstraction, normativisation, and power binding.
**Falsifizierung:** If no consistent decline in openness, ambiguity, or experiential immediacy correlates with later hardening, the translation-loss thesis fails.

### RT-23e — Critical-mass threshold of the collective phase transition
**Motivation:** “Critical mass” is central for collective recoupling but remains unquantified. Without a threshold formulation, the phase transition stays narrative.
**Aufgabe:** Derive analytical or simulation-based threshold conditions under which $\frac{d\Delta\phi_\text{collective}}{dt}<0$ becomes stable; calibrate with protest, reform, or collapse histories.
**Falsifizierung:** If no reproducible threshold range can be identified, the transition thesis loses predictive content.

### RT-24e — Empirical operationalisation of the Alpha/Beta axes
**Motivation:** Alpha and Beta organise the model's individual diagnostics, yet they are not empirically specified. Without measurement logic they remain cultural metaphors.
**Aufgabe:** Correlate personality, creativity, and leadership measures with Alpha and Beta shares, and test whether the axes are stable, modifiable, and predictive.
**Falsifizierung:** If no two separable dimensions with distinct forecasting value can be shown, the Alpha/Beta axes are not defensible as scientific constructs.

### RT-25e — Nature and periodicity of the cosmic cycle
**Motivation:** The assumed periodic lowering of $\beta$ is a strong but uncalibrated hypothesis. It requires a clear decision between astronomical, geophysical, or field-internal mechanisms.
**Aufgabe:** Test the proposed ~2000-year sequence against external datasets and alternative periodic models, and define when the cycle can only remain an internal model variable.
**Falsifizierung:** If neither external cycles nor internal consistency sustain a credible periodicity, the strong form of the cycle hypothesis must be abandoned.

### RT-26e — Correlation of collapse metrics with high resonators
**Motivation:** The model claims a link between societal collapse and the emergence of unusually strong resonance carriers. That claim must be checked against independent historical data.
**Aufgabe:** Operationalise collapse indicators such as state failure, violence intensity, fertility collapse, debt crises, and trust loss, then compare them with time windows of exceptional reformers or founders.
**Falsifizierung:** If collapse peaks do not systematically correlate with the appearance of such figures, the double-event thesis loses its historical claim.

### RT-27e — Three-phase co-optation as a structural hypothesis
**Motivation:** The pattern humility → testing → abuse is a strong generalisation across religion, politics, and economics. Its value depends on whether it can actually be recognised across scales.
**Aufgabe:** Code historical co-optation cases and test them for the three phases, their sequence, and their markers; measure label continuity versus substantive divergence.
**Falsifizierung:** If documented co-optations do not robustly exhibit the three-phase structure, the claim of its A7-invariance does not hold.

### RT-28e — Protective-function thesis
**Motivation:** The claim that certain textual or traditional corpora stabilise social coherence is empirically testable and central to the model. Without data it remains hermeneutic assertion.
**Aufgabe:** Compare reception density, direct access, inversion degree, and social-coherence proxies in longitudinal and cross-sectional datasets; test whether protective function and inversion are measurably distinct.
**Falsifizierung:** If higher reception density or lower inversion does not correlate with lower $\beta$ proxies, the protective-function thesis is not tenable.

### RT-29e — Heaven calibration
**Motivation:** The prehistoric “Heaven” cycle point is the most speculative layer of the model. If it is to be more than internal symbolism, it needs cross-cultural and structural plausibility testing.
**Aufgabe:** Compare fall-from-heaven, primordial-harmony, and rebellion narratives across independent cultures; align dating, diffusion, and pattern similarity with the proposed RFT scheme.
**Falsifizierung:** If no robust cross-cultural structural similarity or temporal consistency can be shown, “Heaven” must remain an internal theological structure hypothesis only.

### RT-30e — Fragmentation dynamics after monopoly dissolution
**Motivation:** The model proposes that post-monopoly knowledge diffusion often produces imitation systems with low $\varepsilon$. This is historically testable and socially consequential.
**Aufgabe:** Study cases of Reformation, decolonisation, market opening, or knowledge-monopoly breakdown for fragmentation, violence, institutional trust, and the quality of successor systems.
**Falsifizierung:** If monopoly dissolutions do not systematically co-occur with greater fragmentation or higher proximity to $\beta_\text{collective}$, the fragmentation thesis must be revised.
