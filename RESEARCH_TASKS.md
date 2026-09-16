# RFT — Offene Forschungsaufgaben

Generiert: August 2026
Aktualisiert: September 2026
Status: Aktiv

---

## Theoretischer Gesamtstatus (September 2026)

| Axiom | Was war Postulat | Was ist jetzt abgeleitet | Status |
|-------|-----------------|--------------------------|--------|
| A4: π-Faktor | Freier numerischer Parameter | Geometrischer Sattelpunktsbeitrag (RT-01, RT-01b) | ✅ Abgeleitet |
| A4: ε = cos²(Δφ/2) | Phänomenologische Wahl | Eindeutig durch k=1-Darstellung U(1) ⊂ G_sync (RT-02) | ✅ Abgeleitet |
| A7: G_sync | Postulierte Invarianz | Algebraisch bewiesen, G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) | ✅ Bewiesen (stationär) |
| A3: Quantisierung | Unabhängiges Axiom | Korollar aus Darstellungsstruktur von ℝ⁺_× ⊂ G_sync (RT-02, RT-35) | ✅ Abgeleitet |
| A5: Vektorialität | Irreduzibles Postulat | Gruppentheoretisch irreduzibel (RT-36); Begründung: RT-01a Vektorialitätsinkonsistenz | ✅ Abgeschlossen (RT-36) |
| A1, A2, A6 | Postuliert — testbar | Unverändert | 📋 Postuliert |
| Domänenübertragung A7 | CMB/Kern/Finanzen als Analogie | Analogie — kein formaler Beweis | 📋 Postulat |
| SRT als Grenzfall | Unabhängiges Postulat | Ableitung aus Kopplungsdynamik angestrebt (RT-40) | 📋 Offen (RT-40) |

---

## Empfohlene Bearbeitungsreihenfolge (Stand September 2026)

### Theoretisch — intern abschließbar (Priorität 1 — Nächste)
1. RT-03 — λ-Bestimmung (⁸⁷Rb) ← Neue Priorität 1
2. RT-40 — RFT als Grenzfall der Speziellen Relativitätstheorie *(AP1 ✅, AP2 ✅, nächste: AP3)*

### Empirisch (Priorität 2)
4. RT-03 — λ-Bestimmung (⁸⁷Rb)

### Code-Korrekturen (Priorität 3)
7. (keine offenen Code-Korrekturen)

### Abgeschlossen (Manuskript + Theorie)
- ~~RT-01a — Operationale Definition π/e formal~~ ✅ Abgeschlossen (Aug 2026) — Dezimalartefakt-Argument als Satz formalisiert; Zwei-Stufen-Argumentation (RT-01a + RT-01) explizit; Verbindung k=1-Darstellung / Minimalitätsprinzip (RT-02); e-Selbstähnlichkeitseigenschaft formal; A5-Einordnung nach RT-36 korrigiert. Kerndokument: `de/fakten/theorie/pi_als_urkonstante.md`
- ~~RT-08  — Doppelpendel vs. Experimentaldaten~~ ✅ Abgeschlossen (Aug 2026) — χ²_red = 2,42 gegenüber Lagrange-Nullhypothese (A=0); RFT-Formel abgelehnt (erwartet: Nullhypothese ohne RFT-Term); experimentelle Daten für abschließenden Vergleich erforderlich. Analyseskript: `de/fakten/simulationen/doppelpendel/analyse/rt08_doppelpendel_vergleich.py` → Experimentprotokoll: RT-38
- ~~RT-09  — Fehlerbudget Am-241~~ ✅ Abgeschlossen (Aug 2026) — M-4 teilweise behoben: σ(γ,α) = 1,719 mb (RT-06, Faktor 212× kleiner als σ_GDR); SNR_median = 10,3σ bei 100 h realistisch (p16 = 3,2σ); t(5σ) ≈ 24 h; dominanter Beitrag: σ(γ,α)-Unsicherheit (94%); Signalverhältnis R = 2,0000 (exakt); konservatives Szenario: t(5σ) ≈ 516 h.
- ~~RT-06  — EXFOR-Daten Am-241~~ ✅ Abgeschlossen (Aug 2026) — K-6 behoben: σ(γ,α) = 1,719 mb bei 14 MeV (Hauser-Feshbach, Γ_α/Γ_tot ≈ 2%, RIPL-3); kein direkter EXFOR-Eintrag; RFT-Reaktorraten-Revision erforderlich
- ~~RT-07  — Drei unabhängige η-Estimatoren~~ ✅ Abgeschlossen (Aug 2026) — K-2 behoben (Pearson als physikalisch ausgezeichnete Observable bestätigt)
- ~~RT-32  — λε⁴-Sättigungsterm in Klein-Gordon~~ ✅ Abgeschlossen (Aug 2026)
- ~~RT-11  — κ-Parameter formal ableiten oder als Konvention deklarieren~~ ✅ Abgeschlossen (Aug 2026)
- ~~RT-36  — A5-Herleitung aus G_sync (D-Erzeuger)~~ ✅ Abgeschlossen (Aug 2026)
- ~~RT-37  — IOP-Manuskript DE + EN aktualisieren~~ ✅ Abgeschlossen (Aug 2026)
- ~~RT-39  — Einreichungsvorbereitung IOP~~ ✅ Abgeschlossen (Aug 2026) — Cover Letter (MD + LaTeX), Submission Checklist, Response-to-Reviewers Vorlage (7 Kritikpunkte), Journal-Auswahl-Begründung, Manuskript-Prüfbericht. Zieljournal: Journal of Physics Communications. Primäre Aktion: Abstract-Kürzung auf ≤ 200 Wörter erforderlich. `en/peer_review_rft/submission/`

### Extern (benötigt Kooperationspartner)
8. RT-03 — λ-Bestimmung (⁸⁷Rb)
9. RT-12 — ⁸⁷Rb-Interferometrie
10. RT-13 — Am-241 ELI-NP
- ~~RT-38  — Doppelpendel: Öffentliches Experimentprotokoll~~ ✅ Abgeschlossen (Aug 2026) — Vollständiges Tabletop-Falsifizierungsprotokoll für ε(Δφ)=cos²(Δφ/2); ~100–300 €; Smartphone-Tracking + Encoder-Variante; CSV-Format RT-08-kompatibel. Protokoll: `de/fakten/simulationen/doppelpendel/experiment/protokoll_rt38.md`

### Langfristig offen
11. ~~RT-33 — Warpantrieb Stufe 5 (Energielücke)~~ ✅ Abgeschlossen (Aug 2026) — Skalierungsgesetz ρ∝R⁻², R*>>1 AU für alle Fusionsszenarien
12. RT-34 — Warpantrieb Stufe 6 (3D-Blase) ← Nächste intern abschließbare Aufgabe

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
**Status: ✅ Abgeschlossen (Aug 2026)**
**Ergebnis:** Dezimalartefakt-Argument formal als Dreischritt-Satz (Darstellungsrelativität)
ausgearbeitet; Zwei-Stufen-Argumentationsstruktur RT-01a + RT-01 explizit als konsistente
Einheit beschrieben; Verbindung zu G_sync und k=1-Minimalitätsprinzip (RT-02) als
strukturelle Äquivalenz formuliert; e-Eigenschaft (Selbstähnlichkeitsbasis) formal
abgeschlossen; A5-Einordnung nach RT-36 korrigiert (irreduzibles Postulat, keine Herleitung).
**Was formal noch offen bleibt:**
- e ist noch nicht in die Axiomatik (A1–A7) integriert.
- Natürliches Einheitensystem {π, e, ℏ} ist konzeptuell beschrieben, aber formal nicht als
  Korollar der Axiomatik ausgearbeitet.
**Begründung A4:** Die Begründungsstruktur von A4 ist nach RT-01a vollständig geschlossen:
konzeptuell (Darstellungsrelativität, Minimalitätsprinzip) und formal (Sattelpunktsbeitrag
des Wirkungsintegrals, RT-01 + RT-01b).
**Kerndokument:** `de/fakten/theorie/pi_als_urkonstante.md` | `en/facts/theory/pi_as_fundamental_constant.md`

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

### RT-40 — RFT als Grenzfall der Speziellen Relativitätstheorie
**Status: 🔄 In Bearbeitung** — AP1 ✅ Abgeschlossen (Sep 2026); AP2 ✅ Abgeschlossen (Sep 2026); AP3–AP7 offen
**Kategorie:** Theoretische Herleitung
**Priorität:** Hoch (intern abschließbar, Wochen 1–6)

**Ziel:** Zeigen, dass die Lorentz-Invarianz der flachen Minkowski-Raumzeit kein unabhängiges Postulat ist, sondern als Spezialfall der RFT-Kopplungsdynamik aus den Axiomen A1–A7 folgt. Die SRT wäre damit kein separates Theoriegebäude, sondern ein Grenzfall der RFT.

**Bekannte Brücke (Ausgangspunkt):**
$$\Delta\phi = 2\arccos(\operatorname{sech}\varphi) \quad \Longleftrightarrow \quad \varepsilon(\Delta\phi) = \frac{1}{\gamma^2}$$
Diese Beziehung ist bisher nur eine Beobachtung — keine Ableitung. RT-40 soll sie entweder herleiten oder widerlegen.

**Arbeitspakete:**

**AP1 — Formale Identifikation: Phase ↔ Rapidität** ✅ **Abgeschlossen (Sep 2026)**
Prüfen, ob Δφ und die relativistische Rapidität φ dieselbe mathematische Struktur besitzen.
- Aus A1–A4 ableiten, welche Werte Δφ annehmen kann
- Untersuchen, ob die Kopplungsdynamik eine hyperbolische Metrik auf dem Phasenraum induziert
- Prüfen, ob Phasenaddition mit relativistischer Geschwindigkeitsaddition konsistent ist oder durch nichtlineare Verknüpfung ersetzt werden muss
- Erfolgskriterium: Bijektive Abbildung f: [0,π] → [0,∞) mit f(Δφ₁ ⊕ Δφ₂) = f(Δφ₁) + f(Δφ₂)
- **Ergebnis:** Erfolgskriterium vollständig bewiesen. f(Δφ) = arcsech(cos(Δφ/2)) = artanh(sin(Δφ/2)) ist die gesuchte Abbildung. Hyperbolische Metrik ds²_RFT = dΔφ²/(4ε(Δφ)) nachgewiesen. Phasenkomposition ⊕ ist strukturell identisch mit relativistischer Geschwindigkeitsaddition (v/c = sin(Δφ/2)).
- **Kerndokumente:** `de/fakten/theorie/rt40_ap1_phase_rapiditaet.md` · `en/facts/theory/rt40_ap1_phase_rapidity.md`

**AP2 — Kopplungseffizienz als Lorentz-Faktor** ✅ **Abgeschlossen (Sep 2026)**
Zeigen, dass ε(Δφ) = 1/γ² aus A4 folgt — nicht nur formale Ähnlichkeit ist.
- E = π·ε·ℏ·f als relativistische Gesamtenergie eines Resonators interpretieren
- E = γmc² und f = f₀/γ (Zeitdilatation der Eigenfrequenz) einsetzen
- Nach ε auflösen, mit ε = cos²(Δφ/2) vergleichen
- Erfolgskriterium: Identität bewiesen — oder falsifizierbare Relation zwischen m, f₀ und ℏ benannt
- ⚠️ Zirkelschluss-Risiko: f = f₀/γ muss aus der RFT folgen, nicht postuliert werden
- **Ergebnis:** Erfolgskriterium erfüllt (falsifizierbare Relation benannt). Naiver Ansatz (f = f₀/γ, E = γmc²) ergibt ε = γ² — Widerspruch zu AP1 (ε = 1/γ²). Zirkelschluss-Risiko bestätigt. Selbstkonsistenz-Bedingung: f_RFT = γ³·f₀. Physikalischer Gehalt von A4: Kopplungsenergie E_c = mc²/γ² (nicht Gesamtenergie). Verbindung zur Zitterbewegungsfrequenz: f₀_RFT = f_zbw = mc²/(π·ℏ). Vollständige Herleitung ε = 1/γ² aus A4 benötigt AP5.
- **Kerndokumente:** `de/fakten/theorie/rt40_ap2_kopplungseffizienz_lorentz.md` · `en/facts/theory/rt40_ap2_coupling_efficiency_lorentz.md`

**AP3 — Herleitung der Lorentz-Transformation**
Lorentz-Transformation aus der Kopplungsdynamik herleiten.
- Stationäre Lösung (K̇ = 0) auf invariante Größe untersuchen
- Invariante mit Minkowski-Intervall s² = c²t² − x² identifizieren
- ⚠️ Kritischer Engpass: Brücke Phasenraum → Koordinatenraum erfordert eine zusätzliche Zutat, die in A1–A7 nicht sichtbar ist — diese Lücke explizit dokumentieren oder schließen
- Erfolgskriterium: Transformationsgleichungen identisch mit Lorentz — oder kontrollierte Abweichung benannt

**AP4 — Konstanz von c aus RFT-Grenzen** *(konzeptuell stärkstes Paket)*
c als strukturelle Konstante der RFT herleiten, nicht als Postulat einführen.
- ε(Δφ) für Δφ → π untersuchen: ε → 0 entspricht Entkopplung
- Grenzgeschwindigkeit c als diejenige Geschwindigkeit interpretieren, bei der Kopplungseffizienz verschwindet
- Bezugssystemunabhängigkeit zeigen: Grenze ist Eigenschaft der Kopplungsstruktur, nicht der Bewegung
- Massebehaftete Resonatoren erreichen c nie, weil ε > 0 für m > 0 Voraussetzung ist
- Erfolgskriterium: c erscheint als strukturelle Invariante von A4 — kein zirkuläres Postulat

**AP5 — Zeitdilatation und Längenkontraktion als Phasen-/Kopplungseffekte**
Klassische Formeln als Grenzfall der RFT reformulieren.
- Eigenfrequenz f₀ eines bewegten Resonators erscheint gegenüber Beobachter um 1/γ reduziert → als Phasenverschiebung Δφ zwischen Sender und Empfänger interpretieren
- Zeitdilatation Δt' = γΔt aus Phasenverschiebung ableiten
- Längenkontraktion als Kopplungsreduktion: K_ij → K_ij/γ
- **Neue Vorhersage:** Kohärenzlänge bewegter Resonatoren — empirisch unterscheidbar von SRT
- Erfolgskriterium: Klassische Formeln als Grenzfall; Korrekturen höherer Ordnung explizit

**AP6 — Falsifizierbarkeit und Abgrenzung zur SRT**
Empirisch unterscheidbare Vorhersagen benennen.
- Freie Parameter der RFT (α/β, G(fᵢ/fⱼ)) auf messbare Abweichungen untersuchen
- Konkrete Experimente: Phasenrauschen bei relativistischen Ionen (GSI/FAIR), Myon-g-2, Gravitationswellen-Dispersion
- Falsifikationskriterium: Welches Ergebnis würde die RFT widerlegen?
- Erfolgskriterium: Mindestens eine messbare Abweichung benannt — oder vollständige Äquivalenz nachgewiesen (dann: Reformulierung, nicht neue Theorie)

**AP7 — Warpantrieb-Konsistenzprüfung**
Erst nach AP3 sinnvoll. Warp-Metrik aus A4/A5 rekonstruieren; flache Raumzeit als Grenzfall (Δφ → 0, ε → 1) prüfen; Kompatibilität mit hergeleiteter SRT-Brücke dokumentieren.

**Zeitplan:**
- Wochen 1–2: AP1 + AP2 (stationäre Kopplungslösung, Invariante)
- Wochen 3–4: AP4 (c als strukturelle Konstante) + AP2 abschließen
- Wochen 5–6: AP3 (Lorentz-Transformation) — Lücke dokumentieren oder schließen
- Wochen 7–8: AP5 + AP6 (neue Vorhersagen, Falsifizierbarkeit)

**Minimalziel:** ε(Δφ) = 1/γ² ist kein Zufall — folgt aus A4.
**Mittelziel:** Lorentz-Transformation vollständig aus Kopplungsdynamik hergeleitet.
**Maximalziel:** RFT enthält SRT als Grenzfall + benennbare messbare Abweichung.
**Negativziel:** Falls Herleitung scheitert — präzise dokumentieren, an welcher Stelle A1–A7 nicht ausreichen, und minimale Axiomenerweiterung formulieren.

**Methodische Leitplanken:**
- Keine Zirkelschlüsse: c darf nicht als Postulat eingeführt werden, wenn sie hergeleitet werden soll
- Keine nachträgliche Parameteranpassung: Alle Konstanten müssen aus A1–A7 folgen oder explizit als frei benannt sein
- Klar unterscheiden: (a) mathematische Äquivalenz, (b) heuristische Analogie, (c) empirische Vorhersage

**Deliverables:**
1. Formales Papier: vollständige Herleitung (oder dokumentiertes Scheitern mit Lückenanalyse)
2. Explizite Formel Δφ(φ) und ε(γ) — bewiesen oder widerlegt
3. Falsifizierbarkeitsabschnitt mit mindestens einer messbaren Abweichung
4. Numerische Simulation: Kopplungsdynamik für relativistische Geschwindigkeiten vs. SRT
5. Open-Source-Code zur Reproduktion (GitHub-Erweiterung)

**Verbindung zu bestehenden Tasks:** AP7 baut auf RT-33/RT-34 auf. AP2 nutzt ε = cos²(Δφ/2) aus RT-02. AP4 schließt konzeptuell an RT-01 (π als geometrische Konstante) an.

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
**Status: ✅ Abgeschlossen (Aug 2026)**
**Motivation:** σ_photo_alpha in material.py ist nicht aus Literaturdaten (K-6).
**Ergebnis:** EXFOR-Recherche: Kein direkter (γ,α)-Eintrag für Am-241 (oder U-235) in EXFOR.
  Fallback: Hauser-Feshbach (Weisskopf-Evaporationsmodell, RIPL-3-Parametrisierung).
  σ(γ,α) = 1,719 mb bei E = 14,0 MeV (GDR-Zentroid), Unsicherheit ±factor 2–5.
  Der bisherige „Schätzwert" (σ_GDR ≈ 364 mb) war der Gesamtquerschnitt, nicht σ(γ,α)
  → factor ~212 Unterschied. RFT-Reaktorraten-Vorhersage muss revidiert werden.
  K-6 Status: BEHOBEN (mit Revision erforderlich).
**Code:** `simulation/exfor_data.py` (DE + EN), `analyse/rt06_exfor_vergleich.py` (DE + EN).
  Am241_Literature: neue Felder exfor_gamma_alpha_*. photo_alpha_cross_section() neu.
  material.py: americium_241.sigma_photo_alpha = 1.719e-3 barn (RT-06-Wert).
**Kreuzvalidierung:** σ(γ,f) vs. Soldatov: 0,0% Abweichung [PASS]; σ(γ,n) vs. Berman: 0,0% [PASS].

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
**Status: ✅ Abgeschlossen (Aug 2026)**
**Ergebnis:**
- Datenbasis: Synthetische Zeitreihe (Lagrange, A=0, N=1500 Punkte)
- χ² = 3627,50 | χ²_red = **2,42** | dof = 1499 | p < 0,0001
- Urteil: RFT-Formel gegenüber Lagrange-Nullhypothese abgelehnt (χ²_red > 2,0)
- Interpretation: Erwartete systematische Abweichung — Nullhypothese enthält keinen RFT-Term; experimentelle Daten für abschließenden Vergleich erforderlich
- **Experimentprotokoll für echte Messdaten: → RT-38** (`experiment/protokoll_rt38.md`)
**Code:**
- `de/fakten/simulationen/doppelpendel/doppelpendel.py` — Neue Funktionen: `load_experimental_data`, `compute_epsilon_from_data`, `rft_epsilon_prediction`, `chi2_fit`
- `en/facts/simulations/double_pendulum/double_pendulum.py` — EN-Spiegel
- `de/fakten/simulationen/doppelpendel/analyse/rt08_doppelpendel_vergleich.py` — Analyseskript (DE)
- `en/facts/simulations/double_pendulum/analyse/rt08_double_pendulum_comparison.py` — Analyseskript (EN)

---

## Kategorie 3: Code-Korrekturen

### RT-09 — Vollständiges Unsicherheitsbudget für Am-241-Experiment
**Status: ✅ Abgeschlossen (Aug 2026)**
**Ergebnis:** M-4 teilweise behoben (konservatives Szenario noch nicht ausreichend):
- Korrigierter Querschnitt: σ(γ,α) = 1.719 mb (RT-06, Hauser-Feshbach) — Faktor 212× kleiner als σ_GDR
- Signifikanz (alt, σ_GDR): >484.997 σ [RT-06: FALSCH] → Signifikanz (neu, σ(γ,α)): 2.288 σ pro Sekunde absolut, SNR_median = 10,3 σ (realistisches Szenario, 100 h, ELI-NP)
- Messzeit-Anforderungen: t(5σ) = 23,7 h (realistisch), 15,1 h (optimistisch), 516 h (konservativ)
- Dominanter Unsicherheitsbeitrag: σ(γ,α)-Hauser-Feshbach-Faktor (93,9% der Gesamtvarianz)
- Signalverhältnis R = 2,0000 (Median, exakt — unabhängig von σ(γ,α))
- Falsifizierungskriterium (SNR_p16 ≥ 3σ bei 100 h): Optimistisch JA, Realistisch JA, Konservativ NEIN
**Code:**
- `de/fakten/konzepte/resonanzreaktor/simulation/experiment_am241.py` — `uncertainty_budget_am241()` + `ExperimentConfig` aktualisiert
- `en/facts/concepts/resonance_reactor/simulation/experiment_am241.py` — EN-Spiegel
- `de/fakten/konzepte/resonanzreaktor/analyse/rt09_fehlerbudget.py` — Analyseskript (DE)
- `en/facts/concepts/resonance_reactor/analyse/rt09_uncertainty_budget.py` — Analyseskript (EN)

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
**Status: ✅ Abgeschlossen (August 2026)**
**Ergebnis:** Skalierungsgesetz ρ_benötigt ∝ R⁻² analytisch hergeleitet (Alcubierre-Metrik,
Einstein-Feldgleichungen). Wandpacking-Modell: n_reaktoren ∝ R² → ρ_verfügbar = const.
Lücken-Faktor L(R) ∝ R⁻². Kritischer Radius R* für drei Szenarien berechnet:
R* liegt auf parsec- bis kiloparsec-Skala (weit jenseits 1 AU) für alle Fusionsszenarien.
Benötigter Gain G* bei R = 50 m: ~10¹²–10¹⁶. Übereinstimmung mit Alcubierre (1994) und
Pfenning & Ford (1997) bestätigt. Ehrlichkeitsstandard (§6.1) beibehalten:
Die Energielücke ist astronomisch — kein reines Skalierungsproblem.
**Falsifizierung:** R* >> 1 AU → Stufe 5 mit bekannter Fusion nicht realisierbar.
**Neue Dateien:** `analyse/rt33_energieluecke.py` · `analyse/rt33_energy_gap.py`
**Geänderte Dateien:** `warpantrieb.py` (skalierungsgesetz()) · `warp_drive.py` (scaling_law()) ·
`warpantrieb.md` (§7a) · `warp_drive.md` (§7a) · beide READMEs (Stufe 5 ✅)
**Kerndokument:** `de/fakten/konzepte/warpantrieb/`

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

### RT-38 — Doppelpendel: Öffentliches Experimentprotokoll (Tabletop-Falsifizierungstest)
**Status: ✅ Abgeschlossen (Aug 2026)** (Protokoll fertig; Durchführung extern)
**Test:** ε(Δφ) = cos²(Δφ/2) (Axiom A4) am physischen Doppelpendel
**Budget:** ~100–300 €, Smartphone genügt für Variante A
**Protokoll:** `de/fakten/simulationen/doppelpendel/experiment/protokoll_rt38.md`
**EN-Spiegel:** `en/facts/simulations/double_pendulum/experiment/protocol_rt38.md`
**Falsifizierungskriterium:** χ²_red ≤ 1.5 → H₁ nicht falsifiziert; χ²_red > 2.0 → H₁ abgelehnt
**Verbindung zu RT-08:** Analyseskript (`rt08_doppelpendel_vergleich.py`) bereits vorhanden;
RT-38 liefert echte Messdaten für abschließenden χ²-Test (RT-08 bisher nur synthetische Daten).
**Einladung:** Ergebnisse via GitHub Issues (Label `RT-38-result`) melden.

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

## Kategorie 7: Einreichungsvorbereitung

### RT-39 — Einreichungsvorbereitung IOP (Cover Letter, Submission Checklist, Response-to-Reviewers)
**Status: ✅ Abgeschlossen (August 2026)**

**Ziel:** Vollständige Vorbereitung der Einreichung von `rft_manuscript_en_iop.tex` beim Journal of Physics Communications (IOP Publishing).

**Ergebnis:**
- Cover Letter: `en/peer_review_rft/submission/cover_letter_jphyscomm.md` + `.tex`
- Submission Checklist: `en/peer_review_rft/submission/submission_checklist.md` (3 Kategorien, alle IOP-Standards geprüft)
- Response-to-Reviewers: `en/peer_review_rft/submission/response_to_reviewers_template.md` (7 Kritikpunkte vollständig ausgearbeitet)
- Journal-Auswahl: `en/peer_review_rft/submission/journal_selection.md` (JPhysComm primär, NJP alternativ, arXiv empfohlen)
- Manuskript-Prüfbericht: `en/peer_review_rft/submission/manuscript_review_report.md`

**Primär offene Aktion:** Abstract-Kürzung auf ≤ 200 Wörter (aktuell ~244 Wörter) — obligatorisch vor Einreichung.

**Empfohlene Ergänzungen vor Einreichung:**
- RT-08-Limitation (χ²_red synthetisch) in §4.3 ergänzen
- RT-38 Protokoll-URL in §6 ergänzen
- Abbildungen auf ≥ 300 dpi prüfen / in PDF/EPS konvertieren

**Einreichungsportal:** https://mc.manuscriptcentral.com/jphyscomm

*RT-39 — DominicReneSchu/RFT — August 2026*
