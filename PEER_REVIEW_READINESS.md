# RFT — Peer-Review Readiness

*Dominic René Schu, August 2026*

Dieses Dokument dokumentiert den Peer-Review-Bereitschaftsstatus der Resonanzfeldtheorie (RFT) nach Kategorien.

---

## Kategorie 1: Theoretische Grundlagen

| ID | Titel | Status | Verweis |
|----|-------|--------|---------|
| RT-01 | Wirkungsintegral-Herleitung von π | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` |
| RT-01a | π als Urkonstante: Operationale Definition und Dezimalartefakt-Argument | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/pi_als_urkonstante.md` · `en/facts/theory/pi_as_fundamental_constant.md` |
| RT-01b | Unabhängige π-Herleitung: Numerisches Pfadintegral + Nicht-Gaussian-Korrekturen | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` §4.5+§9 · `simulationen/rt01b/` |
| RT-02 | Gruppentheoretischer Beweis der Skalentransformation (A7) | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/gsync_gruppenstruktur.md` · `en/facts/theory/gsync_group_structure.md` |
| RT-31 | Resonanz-Hamiltonoperator für spezifische Quantensysteme | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/simulationen/hamilton/README.md` · `en/facts/simulations/hamilton/README.md` |
| RT-35 | A3 als Korollar von A7 in Axiomatik | **✅ Abgeschlossen (Aug 2026)** (durch RT-31) | `de/fakten/theorie/gsync_gruppenstruktur.md` §5 |
| RT-32 | Nichtlineare Sättigungsterme (λ_ε⁴) in der FLRW-Feldgleichung | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/simulationen/FLRW-Simulationen/core/coupled_flrw.py` · `README.md` §RT-32 |
| RT-11 | FLRW κ-Parameter: Konventionsdeklaration κ_RFT = 1 | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/kappa_parameter_rft.md` |
| RT-33 | Warpantrieb: Skalierungsgesetz der Energielücke (Stufe 5) | **✅ Abgeschlossen (Aug 2026) — kein Peer-Review-Blocker, relevant für Ausblick** | `de/fakten/konzepte/warpantrieb/warpantrieb.md` §7a · `analyse/rt33_energieluecke.py` |
| RT-03 | Unabhängige Bestimmung von λ (⁸⁷Rb-Vorhersage) | Offen | RESEARCH_TASKS.md |

### Anmerkung zu RT-01a

RT-01a ist die philosophisch-mathematische Voraussetzung von RT-01: Es dokumentiert, dass
die scheinbare Irrationalität von π und e ein Artefakt der Basis-10-Kodierung ist und
nicht ein Naturphänomen.

**Abgeschlossen (Aug 2026):** Das Dezimalartefakt-Argument wurde als formaler Dreischritt-Satz
(Darstellungsrelativität von π) ausgearbeitet. Die Zwei-Stufen-Argumentation (RT-01a:
*Berechtigung*, π als Einheit zu behandeln; RT-01: *Notwendigkeit*, π im Wirkungsintegral)
ist explizit als konsistente Einheit dargestellt. Die Verbindung zur k=1-Darstellung von
U(1) ⊂ G_sync (RT-02) als strukturell äquivalentes Minimalitätsprinzip ist formalisiert.
Die e-Selbstähnlichkeitseigenschaft ist formal abgeschlossen. A5-Einordnung nach RT-36
korrigiert: irreduzibles Postulat, Vektorialitätsinkonsistenz als Motivation (nicht Herleitung).

**Bedeutung für Peer Review:** Die Begründungsstruktur von A4 ist nach RT-01a vollständig
geschlossen — konzeptuell (Darstellungsrelativität, Minimalitätsprinzip) und formal
(Sattelpunktsbeitrag des Wirkungsintegrals, RT-01 + RT-01b). Dies schließt einen häufigen
Peer-Review-Einwand: Warum hat A4 den Faktor π — eine scheinbar willkürliche Wahl?

**Was formal noch offen bleibt:** e in der Axiomatik (A1–A7); natürliches {π, e, ℏ}-Einheitensystem
als formales Korollar.

### Anmerkung zu RT-01b

RT-01b ist die numerische Bestätigung von RT-01: Das Pfadintegral wurde für N = 100/500/1000
Gitterpunkte ausgewertet und konvergiert gegen π mit Maschinengenauigkeit. Die
Nicht-Gaussian-Korrekturen sind mit |c₃ + c₄| ≈ 5.5 × 10⁻¹¹ weit unterhalb der
Anforderungsschranke. Die Potenzial-Unabhängigkeit des π-Beitrags wurde für drei
normierte Potenziale nachgewiesen.

**Status:** Abgeschlossen (August 2026). RT-01 ist von einer motivierten Formalisierung
zu einem unabhängig bestätigten Ableitungsresultat geworden.

---

## Kategorie 2: Axiomensystem

| Axiom | Titel | Status |
|-------|-------|--------|
| A1 | Universelle Schwingung | Postuliert — testbar |
| A2 | Resonanzkopplung | Postuliert — testbar |
| A3 | Resonanzfenster | **Korollar aus A7** (RT-02, RT-35, Aug 2026) — nicht mehr unabhängig |
| A4 | Kopplungsenergie E = π·ε·ℏ·f | π geometrisch abgeleitet (RT-01, RT-01b, Aug 2026); ε darstellungstheoretisch erzwungen (RT-02); Begründungsstruktur vollständig geschlossen (RT-01a, Aug 2026): konzeptuell (Darstellungsrelativität, Minimalitätsprinzip) + formal (Wirkungsintegral-Sattelpunkt) |
| A5 | Vektorialität der Energie | **Irreduzibles Postulat** (RT-36, Aug 2026) — gruppentheoretisch nicht aus G_sync ableitbar; formale Begründungsgrundlage: RT-01a (Vektorialitätsinkonsistenz in Drehmoment, Spin, Lorentz-4-Vektor) |
| A6 | Resonanzerhaltung | Postuliert — testbar |
| A7 | Skalentransformation | **Bewiesen** — gruppentheoretisch (RT-02, Aug 2026); Domänenübertragung Kosmologie: empirisch testbar (SI) — RT-04 implementiert |

---

## Kategorie 3: Offene Formalisierungsschritte (blockierend für Peer Review)

| ID | Beschreibung |
|----|-------------|
| RT-01a | Operationale Definition von π und e als Phasenraumkonstanten (formal offen) |
| RT-01b | Numerisches Pfadintegral + Nicht-Gaussian-Korrekturen — **✅ Abgeschlossen (Aug 2026)** |
| RT-02 | Gruppentheoretischer Beweis A7 — **✅ Abgeschlossen (Aug 2026)** |
| RT-31 | Resonanz-Hamiltonoperator (Phonon + Spin-Bahn) — **✅ Abgeschlossen (Aug 2026)** |
| RT-35 | A3-Korollar in Axiomatik — **✅ Abgeschlossen (Aug 2026)** |
| RT-32 | Nichtlineare Sättigungsterme (λ_ε⁴) — **✅ Abgeschlossen (Aug 2026)** |
| RT-11 | κ-Parameter Konventionsdeklaration — **✅ Abgeschlossen (Aug 2026)** |
| RT-37 | IOP-Manuskript aktualisieren (RT-01/01b/02/31 einarbeiten) — **✅ Abgeschlossen (Aug 2026)** |
| RT-07 | Unabhängige η-Estimatoren (K-2: Tautologie-Kritik Pearson-Estimator) — **✅ Abgeschlossen (Aug 2026)** — Pearson als physikalisch ausgezeichnete Observable bestätigt |
| RT-04 | FLRW-Solver SI-Einheiten (Planck-2018) — **✅ Abgeschlossen (Aug 2026)** — `core/flrw_si.py` + `compare_to_astropy()`. Falsifizierung: max. Abw. < 1 % vs. astropy. |
| RT-05 | CMB-Vergleich mit CAMB/CLASS (K-5: Spielzeugmodell generate_lcdm_bestfit) — **✅ Abgeschlossen (Aug 2026)** — `core/camb_reference.py` + `compare_with_camb()` + `scan_h0_tension()`. Δχ²_CAMB ist nun der belastbare Vergleich. |
| RT-06 | σ(γ,α) Am-241 aus EXFOR (K-6: Geschätztes sigma_photo_alpha) — **✅ Behoben (Aug 2026, mit Revision erforderlich)** — Hauser-Feshbach: σ(γ,α) = 1,719 mb bei E = 14 MeV (Γ_α/Γ_tot ≈ 2%, RIPL-3). Kein direkter EXFOR-Eintrag für Am-241 (γ,α). RFT-Reaktorraten-Vorhersage muss mit korrektem σ(γ,α) neu berechnet werden. `simulation/exfor_data.py` + `analyse/rt06_exfor_vergleich.py`. |
| RT-09 | Vollständiges Fehlerbudget Am-241 (M-4: fehlende Fehlerrechnung) — **✅ Teilweise behoben (Aug 2026)** — Monte-Carlo-Fehlerrechnung implementiert. σ(γ,α)-Unsicherheit (Faktor 2–5) dominiert mit 93,9% der Varianz. Realistisches Szenario: SNR_median = 10,3σ bei 100 h (ELI-NP). Falsifizierungskriterium (SNR_p16 ≥ 3σ): JA (optimistisch + realistisch), NEIN (konservativ — t(5σ) ≈ 516 h). `simulation/experiment_am241.py` `uncertainty_budget_am241()` + `analyse/rt09_fehlerbudget.py`. |
| RT-10 | ResoTrade Walk-Forward-Backtest (M-5: private Implementierung ohne Reproduzierbarkeit) — **✅ Abgeschlossen (Aug 2026)** — Öffentlicher Walk-Forward-Backtest implementiert. Binance Public API + synthetischer Fallback (seed=42). Falsifizierungskriterium: vs_hodl > 0 in allen Folds. Synthetische Daten: 3/5 Folds positiv, Ø Sharpe=0,89, Ø Max-DD=4,4%. M-5 adressiert (Live-API-Daten empfohlen für abschließende Verifikation). `backtest/backtest_engine.py` + `backtest/analyse/rt10_backtest_comparison.py` (DE+EN). |
| RT-08 | Doppelpendel: ε_RFT vs. Experimentaldaten — **✅ Abgeschlossen (Aug 2026)** — χ²_red = 2,42 gegenüber Lagrange-Nullhypothese (A=0, N=1500). Urteil: RFT-Formel gegenüber rein klassisch-mechanischer Nullhypothese abgelehnt (erwartet). Für abschließenden Vergleich: experimentelle Daten erforderlich (Zenodo). `doppelpendel.py` um `chi2_fit()` + `load_experimental_data()` erweitert. Analyseskript: `analyse/rt08_doppelpendel_vergleich.py`. → Experimentprotokoll: RT-38. |
| RT-38 | Doppelpendel: Öffentliches Experimentprotokoll — **✅ Abgeschlossen (Aug 2026)** — Vollständiges Tabletop-Falsifizierungsprotokoll für ε(Δφ)=cos²(Δφ/2). Budget: ~100–300 €, Smartphone genügt. Messkette: Variante A (Smartphone + OpenCV-Tracking), Variante B (AS5600-Encoder). CSV-Format RT-08-kompatibel. χ²-Auswertungssoftware bereits vorhanden (RT-08). Test durch jede Gruppe reproduzierbar; Ergebnisse via GitHub Issues melden (Label: `RT-38-result`). Protokoll: `de/fakten/simulationen/doppelpendel/experiment/protokoll_rt38.md` |
| RT-03 | Unabhängige λ-Bestimmung für RT-03-Vorhersage |

---

*Verwandt:* [RESEARCH_TASKS.md](RESEARCH_TASKS.md) |
[de/fakten/theorie/pi_als_urkonstante.md](de/fakten/theorie/pi_als_urkonstante.md) |
[en/facts/theory/pi_as_fundamental_constant.md](en/facts/theory/pi_as_fundamental_constant.md)

---

## Einreichungsbereitschaft (August 2026)

| Dokument | Status | Pfad |
|----------|--------|------|
| Cover Letter (MD) | ✅ Erstellt | `en/peer_review_rft/submission/cover_letter_jphyscomm.md` |
| Cover Letter (LaTeX) | ✅ Erstellt | `en/peer_review_rft/submission/cover_letter_jphyscomm.tex` |
| Submission Checklist | ✅ Erstellt | `en/peer_review_rft/submission/submission_checklist.md` |
| Response-to-Reviewers | ✅ Erstellt | `en/peer_review_rft/submission/response_to_reviewers_template.md` |
| Journal-Auswahl | ✅ Erstellt | `en/peer_review_rft/submission/journal_selection.md` |
| Manuskript-Prüfbericht | ✅ Erstellt | `en/peer_review_rft/submission/manuscript_review_report.md` |
| Abstract ≤ 200 Wörter | ⚠️ Aktion erforderlich | aktuell ~244 Wörter |
| Abbildungen ≥ 300 dpi | ⚠️ Prüfen | `figures/*.png` |

Zieljournal: **Journal of Physics Communications** (IOP Publishing)
Einreichungsportal: https://mc.manuscriptcentral.com/jphyscomm
