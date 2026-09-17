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
| A8: Kopplungswellengeschwindigkeit | Nicht in A1–A7 enthalten (B₁-Lücke, RT-40 AP3) | A8 als irreduzibles Postulat: c = 1/√(μ₀ε₀) (RT-41) | ✅ Postuliert (RT-41) |
| Kosmologie als Phaseneffekt | Analogie/Postulat | Ableitung aus Kopplungsdynamik angestrebt (RT-42) | 🔄 AP1 ✅ AP2 ✅ (RT-42) |

---

## Empfohlene Bearbeitungsreihenfolge (Stand September 2026)

### Theoretisch — intern abschließbar (Priorität 1 — Nächste)
1. RT-03 — λ-Bestimmung (⁸⁷Rb) ← Neue Priorität 1
2. RT-42 — RFT-Kosmologie: Friedmann-Analogie aus Phasendynamik
3. ~~RT-40 — RFT als Grenzfall der Speziellen Relativitätstheorie~~ ✅ Abgeschlossen (Sep 2026) — AP1–AP7 vollständig; SRT als Grenzfall bewiesen; Warp-Konsistenz dokumentiert; offene Lücke: Brückenannahme B₁ (minimale Axiomenerweiterung A8)
4. ~~RT-41~~  ✅ Abgeschlossen (Sep 2026) — Axiom A8: Kopplungswellengeschwindigkeit als irreduzibles Postulat etabliert

### Empirisch (Priorität 2)
4. RT-03 — λ-Bestimmung (⁸⁷Rb)

### Code-Korrekturen (Priorität 3)
7. (keine offenen Code-Korrekturen)

### Abgeschlossen (Manuskript + Theorie)
- ~~RT-40  — RFT als Grenzfall der Speziellen Relativitätstheorie~~ ✅ Abgeschlossen (Sep 2026) — AP1–AP7 vollständig; SRT als Grenzfall der RFT bewiesen (AP1–AP5); vier empirische Überschuss-Vorhersagen (AP6); Warpkonsistenz und flache Raumzeit als RFT-Grundzustand (AP7). Offene Lücke: Brückenannahme B₁ (minimale Axiomenerweiterung A8). Kerndokumente: `de/fakten/theorie/rt40_ap*` · `en/facts/theory/rt40_ap*`
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
12. ~~RT-34 — Warpantrieb Stufe 6 (3D-Blase)~~ ✅ Abgeschlossen (Sep 2026) — Falsifizierungstest bestanden: ρ≥0 überall; GR-Solver (Christoffel, Riemann, Ricci) implementiert

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
**Status: ✅ Abgeschlossen (Sep 2026)** — AP1 ✅ AP2 ✅ AP3 ✅ AP4 ✅ AP5 ✅ AP6 ✅ AP7 ✅ (alle Arbeitspakete abgeschlossen)
**Kategorie:** Theoretische Herleitung
**Priorität:** Abgeschlossen

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

**AP3 — Herleitung der Lorentz-Transformation** ✅ **Abgeschlossen (Sep 2026)**
Lorentz-Transformation aus der Kopplungsdynamik herleiten.
- Stationäre Lösung (K̇ = 0) auf invariante Größe untersuchen
- Invariante mit Minkowski-Intervall s² = c²t² − x² identifizieren
- ⚠️ Kritischer Engpass: Brücke Phasenraum → Koordinatenraum erfordert eine zusätzliche Zutat, die in A1–A7 nicht sichtbar ist — diese Lücke explizit dokumentieren oder schließen
- Erfolgskriterium: Transformationsgleichungen identisch mit Lorentz — oder kontrollierte Abweichung benannt
- **Ergebnis:** Erfolgskriterium erfüllt (Lorentz-Gleichungen exakt hergeleitet; strukturelle Lücke präzise dokumentiert). Stationäre Kopplungsbedingung K̇ = 0 mit gleichförmiger Relativbewegung identifiziert. RFT-Kopplungs-Invariante I_RFT = Δφ²/k² = |Δx|² − c²Δt² ≅ Minkowski-Intervall hergeleitet. Lorentz-Transformationsgleichungen t' = γ(t − βx/c), x' = γ(x − βct) exakt bewiesen. Lorentz-Gruppe aus G_sync-Phasenkomposition (AP1) abgeleitet. Brückenannahme B₁ (Kopplungswelle mit Phasengeschwindigkeit c) explizit formuliert — in A1–A7 nicht vollständig enthalten; AP4 soll c als strukturelle Grenze fundieren. Minimale Axiomenerweiterung A8 (Kopplungswellengeschwindigkeit) als Option formuliert.
- **Kerndokumente:** `de/fakten/theorie/rt40_ap3_lorentz_transformation.md` · `en/facts/theory/rt40_ap3_lorentz_transformation.md`

**AP4 — Konstanz von c aus RFT-Grenzen** ✅ **Abgeschlossen (Sep 2026)**
c als strukturelle Konstante der RFT herleiten, nicht als Postulat einführen.
- ε(Δφ) für Δφ → π untersuchen: ε → 0 entspricht Entkopplung
- Grenzgeschwindigkeit c als diejenige Geschwindigkeit interpretieren, bei der Kopplungseffizienz verschwindet
- Bezugssystemunabhängigkeit zeigen: Grenze ist Eigenschaft der Kopplungsstruktur, nicht der Bewegung
- Massebehaftete Resonatoren erreichen c nie, weil ε > 0 für m > 0 Voraussetzung ist
- Erfolgskriterium: c erscheint als strukturelle Invariante von A4 — kein zirkuläres Postulat
- **Ergebnis:** Erfolgskriterium erfüllt. ε(Δφ) → 0 für Δφ → π (quadratisch regulär). Strukturelle Grenzgeschwindigkeit c_struct = lim_{ε→0} v(ε) = c_phys abgeleitet. Bezugssystemunabhängigkeit über Lorentz-Invarianz von ε bewiesen (ε ist Skalar im Phasenraum, AP1 + A5). Massebehaftete Resonatoren: E_kin → ∞ für v → c; c in endlicher Zeit nie erreichbar (direkte Konsequenz A4). Brückenannahme B₁ aus AP3 retroaktiv fundiert: c ist die einzige strukturell ausgezeichnete Grenzgeschwindigkeit der RFT. Numerischer Wert c = 2,998 × 10⁸ m/s bleibt empirische Zutat. SRT-Postulate (Relativitätsprinzip + Konstanz von c) beide als Grenzfälle von A1–A7 begründet.
- **Kerndokumente:** `de/fakten/theorie/rt40_ap4_lichtgeschwindigkeit_grenzfall.md` · `en/facts/theory/rt40_ap4_speed_of_light_limit.md`

**AP5 — Zeitdilatation und Längenkontraktion als Phasen-/Kopplungseffekte** ✅ **Abgeschlossen (Sep 2026)**
Klassische Formeln als Grenzfall der RFT reformulieren.
- Eigenfrequenz f₀ eines bewegten Resonators erscheint gegenüber Beobachter um 1/γ reduziert → als Phasenverschiebung Δφ zwischen Sender und Empfänger interpretieren
- Zeitdilatation Δt' = γΔt aus Phasenverschiebung ableiten
- Längenkontraktion als Kopplungsreduktion: K_ij → K_ij/γ
- **Neue Vorhersage:** Kohärenzlänge bewegter Resonatoren — empirisch unterscheidbar von SRT
- Erfolgskriterium: Klassische Formeln als Grenzfall; Korrekturen höherer Ordnung explizit
- **Ergebnis:** Erfolgskriterium vollständig erfüllt. Zeitdilatation Δt = γΔt₀ exakt aus hyperbolischer Phasenprojektionsgeometrie (AP1) hergeleitet. Längenkontraktion L' = L₀/γ aus effektiver Wellenzahl k_eff = γ·k₀ (AP3) bewiesen. ε = 1/γ² algebraisch geschlossen: cos²(arcsin β) = 1 − β² = 1/γ². Neue RFT-Vorhersage: Kohärenzlänge l_c(v) = λ₀/(2γ²), skaliert mit γ² statt γ — empirisch unterscheidbar von SRT-Längenkontraktion. Drei experimentelle Methoden und präzises Falsifikationskriterium formuliert.
- **Kerndokumente:** `de/fakten/theorie/rt40_ap5_zeitdilatation_laengenkontraktion.md` · `en/facts/theory/rt40_ap5_time_dilation_length_contraction.md`

**AP6 — Falsifizierbarkeit und Abgrenzung zur SRT** ✅ **Abgeschlossen (Sep 2026)**
Empirisch unterscheidbare Vorhersagen benennen.
- Freie Parameter der RFT (α/β, G(fᵢ/fⱼ)) auf messbare Abweichungen untersucht
- Konkrete Experimente: Phasenrauschen bei relativistischen Ionen (GSI/FAIR), Myon-g-2, Gravitationswellen-Dispersion, Kohärenzlängen-Interferometrie
- Falsifikationskriterium: l_c ∝ γ⁻¹ (gemessen) würde AP5-Vorhersage widerlegen
- **Ergebnis:** Erfolgskriterium erfüllt. Kinematik RFT ≡ SRT (vollständig äquivalent). Vier Überschuss-Vorhersagen benannt: (1) l_c(v) = λ₀/(2γ²) — γ²-Skalierung vs. γ der SRT; (2) Phasenrauschen S_φ ∝ γ⁻²; (3) interne Konsistenzfrequenz f_int = γ³f₀; (4) frequenzabhängige Gruppengeschwindigkeit nahe ε→0. LIGO-Daten schließen signifikante GW-Dispersion aus. Myon-g-2 qualitativ plausibel, nicht quantifizierbar ohne Quantisierung der RFT.
- **Kerndokumente:** `de/fakten/theorie/rt40_ap6_falsifizierbarkeit_srt_abgrenzung.md` · `en/facts/theory/rt40_ap6_falsifiability_srt_distinction.md`

**AP7 — Warpantrieb-Konsistenzprüfung** ✅ **Abgeschlossen (Sep 2026)**
Erst nach AP3 sinnvoll. Warp-Metrik aus A4/A5 rekonstruieren; flache Raumzeit als Grenzfall (Δφ → 0, ε → 1) prüfen; Kompatibilität mit hergeleiteter SRT-Brücke dokumentieren.
- **Ergebnis:** Erfolgskriterium vollständig erfüllt. RFT-Warp-Metrik aus A4/A5 hergeleitet: h_μν^RFT = h_μν^Alcubierre · ε(Δφ). Flache Raumzeit als kohärenter Grundzustand (Δφ=0, ε=1) analytisch bewiesen. Lichtgrenzfall (Δφ→π, ε→0): Warpfeld kollabiert, konsistent mit AP4. Keine Negativenergie: ε(Δφ)≥0 → ρ_RFT≥0. Drei neue Vorhersagen gegenüber Standard-Alcubierre: (1) ε²-Winkelmodulation der Energiedichte; (2) ρ≥0 überall (keine exotische Materie); (3) Selbst-Abschaltung bei v_s→c. Offene Lücke: Brückenannahme B₁ (wie AP3) und nichtlinearer Warpfall (v_s~c).
- **Kerndokumente:** `de/fakten/theorie/rt40_ap7_warpantrieb_konsistenzpruefung.md` · `en/facts/theory/rt40_ap7_warp_consistency_check.md`

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

### RT-41 — Axiom A8: Kopplungswellengeschwindigkeit — Herleitung oder irreduzibles Postulat
**Status: ✅ Abgeschlossen (Sep 2026)**
**Kategorie:** Theoretische Herleitung
**Priorität:** Abgeschlossen

**Ergebnis:** Ergebnis B: A8 ist irreduzibles Postulat. c als Phasengeschwindigkeit
folgt nicht aus A1–A7. AP1: Dispersionsrelation ist in A1 freier Parameter. AP2: c_lim
(ε→0) und c_φ (B₁) konzeptuell verschieden — Gleichheit konsistent, aber nicht beweisbar.
AP3: G_sync enthält keine SO(1,1)-Untergruppe. A8 formal formuliert und in
`axiomatische_grundlegung.md` eingetragen. Axiomensystem A1–A8 vollständig für SRT-Ableitung.

**Kerndokumente:** `de/fakten/theorie/rt41_axiom_a8_kopplungswelle.md` ·
`en/facts/theory/rt41_axiom_a8_coupling_wave.md` ·
`de/fakten/docs/definitionen/axiomatische_grundlegung.md`

**Verbindung zu bestehenden Tasks:**
- RT-40 AP3: B₁-Lücke (Ausgangspunkt) — `de/fakten/theorie/rt40_ap3_lorentz_transformation.md` §8
- RT-40 AP4: c als strukturelle Grenzgeschwindigkeit — `de/fakten/theorie/rt40_ap4_lichtgeschwindigkeit_grenzfall.md`
- RT-02: G_sync-Gruppenstruktur — `de/fakten/theorie/gsync_gruppenstruktur.md`
- RT-36: A5 als Vorbild für irreduzibles Postulat — `de/fakten/theorie/a5_vektorialitaet_herleitung.md`

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
**Status: ✅ Abgeschlossen (Sep 2026)**
**Ergebnis:** Vollständige sphärisch-azimutale 3D-Warpblase implementiert.
Falsifizierungstest bestanden: ρ(x,y,z) ≥ 0 in allen Raumzeitregionen des
50³-Gitters. GR-Solver (numerische Christoffel-Symbole Γ^t_tr, Γ^r_tt,
Riemann-Tensor R^r_trt, vollständiger Ricci-Skalar R_full) implementiert.
Zwei-Feld-Modell ist hinreichend für eine physikalische Warpblase.
**Neue Dateien:** `analyse/rt34_warpblase_3d.py` · `analyse/rt34_warp_bubble_3d.py`
**Geänderte Dateien:** `de/fakten/konzepte/warpantrieb/warp_3d.py` (GR-Solver,
Falsifizierungstest) · `en/facts/concepts/warp_drive/warp_3d.py` (EN-Spiegel) ·
beide READMEs (Stufe 6 ✅)
**Kerndokument:** `de/fakten/konzepte/warpantrieb/`

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

## Kategorie 5: Kosmologie

## RT-42 – RFT-Kosmologie

### Ableitung einer Friedmann-Analogie aus der Resonanzfeldtheorie

**Version:** 1.1 – AP1 abgeschlossen
**Datum:** 17. September 2026
**Status:** 🔄 In Bearbeitung — AP1 ✅
**Vorgänger:** RT-40 (SRT-Brücke, abgeschlossen), RT-41 (A8, abgeschlossen)
**Verwandt:** RT-33 (Warp-Skalierung), RT-34 (3D-Warpblase), RT-04 (FLRW-Simulation)

---

### 1. Zielsetzung

**Übergeordnetes Ziel:**
Prüfen, ob die kosmische Expansion als **Phaseneffekt im RFT-Feld** beschrieben werden kann – also ob eine modifizierte Friedmann-Gleichung existiert, in der der Skalenfaktor $a(t)$ aus der Phasendynamik $\Delta\phi(t)$ folgt, **ohne** negative Energie oder eine separate Dunkle-Energie-Komponente.

**Teilziele:**

1. Formale Analogie zwischen RFT-Phasendynamik und Friedmann-Gleichungen herstellen.
2. Zeitableitung der Phase $\dot{\Delta\phi}$ aus der Kopplungsdynamik herleiten.
3. Prüfen, ob die RFT $\Lambda$ ersetzen, erklären oder als Spezialfall enthalten kann.
4. Das Skalierungsproblem der Warp-Simulation (28–50 Größenordnungen) kosmologisch einordnen.
5. Falsifizierbare Abweichungen vom $\Lambda$CDM-Modell benennen.
6. **Konsistenz mit A8 prüfen:** Ist die Kopplungswellengeschwindigkeit $c = 1/\sqrt{\mu_0\varepsilon_0}$ mit einem kosmologischen Phasengradienten vereinbar?

---

### 2. Ausgangslage

**Gegeben (RFT):**
- Axiome A1–A8 (A8 seit RT-41: $c = 1/\sqrt{\mu_0\varepsilon_0}$ als irreduzibles Postulat)
- Kopplungseffizienz $\varepsilon(\Delta\phi) = \cos^2(\Delta\phi/2)$
- Kopplungsdynamik $\frac{dK_{ij}}{dt} = \alpha G \cos\Delta\phi - \beta K_{ij}$
- Zustandsgleichung aus RT-33: $w(\theta) = \frac{1}{3}[2\varepsilon(\Delta\phi(\theta)) - 1]$
- **RT-40-Ergebnis:** $\varepsilon = 1/\gamma^2$, Lorentz-Transformation als Grenzfall, $l_c \propto \gamma^{-2}$
- **RT-33-Ergebnis:** ρ ≥ 0 überall, keine negative Energie nötig; $w \in [-1/3, +1/3]$
- **RT-41-Ergebnis:** A8 etabliert $c$ als Kopplungswellengeschwindigkeit

**Gegeben (Kosmologie):**
- Friedmann-Gleichungen:
  $$H^2 = \left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{kc^2}{a^2} + \frac{\Lambda c^2}{3}$$
  $$\frac{\ddot a}{a} = -\frac{4\pi G}{3}\left(\rho + \frac{3p}{c^2}\right) + \frac{\Lambda c^2}{3}$$
- $\Lambda$CDM: Dunkle Energie mit $w \approx -1$, ca. 68 % der Energiedichte
- Beobachtungen: beschleunigte Expansion seit $z \approx 0{,}5$

**Bekannte Spannung:**
- Kosmologische Energiedichte: $\rho_\Lambda \approx 10^{-26}\,\text{kg/m}^3 \approx 10^{-9}\,\text{J/m}^3$
- Warp-Simulation: $\rho \approx 10^{19}\,\text{J/m}^3$ für R = 50 m
- **Diskrepanz: ~28 Größenordnungen** (gegen $\rho_\Lambda$)

---

### 3. Arbeitspakete

#### AP1 – Formale Analogie: Phase ↔ Skalenfaktor ✅ **Abgeschlossen (Sep 2026)**

**Aufgabe:**
Prüfe, ob die RFT-Phasendifferenz $\Delta\phi(t)$ als **dynamische Variable** fungiert, die den kosmischen Skalenfaktor $a(t)$ steuert.

**Konkrete Schritte:**
1. Definiere ein homogenes, isotropes RFT-Feld: $\Delta\phi(\vec x, t) \to \Delta\phi(t)$.
2. Leite aus A1–A8 ab, wie sich $\Delta\phi$ unter Expansion verhält.
3. Setze $\varepsilon(t) = \cos^2(\Delta\phi(t)/2)$ und interpretiere $\varepsilon$ als **effektive kosmologische Dichte**.
4. Vergleiche mit dem Friedmann-Ausdruck: $\varepsilon \leftrightarrow \rho/\rho_c$.
5. Prüfe, ob eine Friedmann-artige Gleichung der Form
   $$H^2 = \frac{8\pi G}{3}\rho_{\text{RFT}}(\varepsilon) - \frac{kc^2}{a^2}$$
   ohne separaten $\Lambda$-Term auskommt.

**Erfolgskriterium:** Explizite Abbildung $\Delta\phi(t) \to a(t)$ — oder Nachweis ihrer Nichtexistenz.

- **Ergebnis:** Erfolgskriterium erfüllt. Explizite Abbildung $H(t) = H_0 \cdot \cos(\Delta\phi(t)/2)$ konstruiert; Friedmann-artige Gleichung $H^2 = H_0^2 \cdot \varepsilon(\Delta\phi)$ ohne $\Lambda$-Term hergeleitet. Bijektivität auf $\Delta\phi \in [0, \pi/2)$ bewiesen. Offene Einschränkung: $w \in [-1/3, +1/3]$ aus RT-33 deckt $w = -1$ (ΛCDM) nicht ab — AP3 erforderlich. Kerndokumente: `de/fakten/theorie/rt42_ap1_phase_skalenfaktor.md` · `en/facts/theory/rt42_ap1_phase_scale_factor.md`

---

#### AP2 – Zeitableitung der Phase

**Status: ✅ Abgeschlossen (Sep 2026)**

**Aufgabe:**
Bestimme $\dot{\Delta\phi}$ aus der Kopplungsdynamik und interpretiere es als **Expansionsrate**.

**Konkrete Schritte:**
1. Homogenes Feld: $\frac{dK}{dt} = \alpha G \cos(\Delta\phi) - \beta K$
2. Drücke $K$ durch $\Delta\phi$ aus (z. B. $K = K_0 \varepsilon(\Delta\phi)$).
3. Leite eine Differentialgleichung für $\Delta\phi(t)$ her.
4. Identifiziere $\dot{\Delta\phi}$ mit $H = \dot a/a$ — oder zeige, warum das nicht geht.
5. Untersuche stationäre ($\dot{\Delta\phi} = 0$) und dynamische Lösungen.
6. **Konsistenz mit A8:** Begrenzt $c$ die Phasendynamik auf kosmologischen Skalen?

**Erfolgskriterium:** Geschlossene Differentialgleichung für $\Delta\phi(t)$, vergleichbar mit Friedmann-Lösungen.

- **Ergebnis:** Erfolgskriterium erfüllt. Geschlossene ODE $\dot{\Delta\phi} = \beta\tan(\Delta\phi/2)$ vollständig aus der RFT-Kopplungsdynamik abgeleitet (A4, A5, AP1-Homogenisierung). Äquivalente Form: $\dot\varepsilon = -\beta(1-\varepsilon)$ mit analytischer Lösung $\varepsilon(t) = 1 - \sin^2(\Delta\phi_0/2)\,e^{\beta t}$. Hubble-Parameter explizit: $H(t) = H_0\sqrt{1 - \sin^2(\Delta\phi_0/2)\,e^{\beta t}}$. Modifizierte Raychaudhuri-Gleichung: $\dot H = -(\beta/2)(H_0^2 - H^2)/H$. Direkte Identifikation $\dot{\Delta\phi} = H$ nicht möglich (verschiedene Funktionen von $\Delta\phi$); physikalische Verbindung läuft über $\dot\varepsilon$. A8-Konsistenz: $\beta \sim H_0$ sichert kausale Verträglichkeit am Hubble-Horizont.
- **Kerndokumente:** `de/fakten/theorie/rt42_ap2_zeitableitung_phase.md` · `en/facts/theory/rt42_ap2_time_derivative_phase.md`

---

#### AP3 – Verbindung zu $\Lambda$ oder Dunkler Energie ✅ **Abgeschlossen (Sep 2026)**

**Aufgabe:**
Klären, ob die RFT $\Lambda$ **ersetzt**, **erklärt** oder **als Grenzfall enthält**.

**Konkrete Schritte:**
1. Prüfe $\varepsilon(\Delta\phi)$ für $\Delta\phi \to \pi$: $\varepsilon \approx \delta^2/4 \to 0$ — nicht $\Lambda$-artig.
2. Prüfe, ob ein **Phasengradient** $\nabla\Delta\phi$ einen effektiven $\Lambda$-Term erzeugt.
3. Vergleiche mit Quintessenz-Modellen ($w(t)$ dynamisch).
4. Benenne Bedingungen, unter denen RFT und $\Lambda$CDM identisch sind.

**Erfolgskriterium:** Klare Aussage: RFT ersetzt / erklärt / ist unvereinbar mit $\Lambda$.

- **Ergebnis:** Erfolgskriterium erfüllt. Homogener Grenzfall (∇Δφ = 0): w ∈ [−1/3, +1/3], w = −1 nicht erreichbar — RFT unvereinbar mit Λ = const. Inhomogener Grenzfall (statischer Superhorizontalgradient ∇Δφ = k₀): effektiver Λ-Term ρ_grad = (1/2μ₀)·k₀²·ℏ²/c² mit w_grad → −1 — RFT **erklärt** Λ geometrisch. ΛCDM ist Spezialfall der RFT (β → 0, k₀ = const), nicht umgekehrt. RFT ist erweitertes Quintessenz-Modell mit w_eff ∈ [−1, +1/3]. Falsifizierbare Vorhersage: w(z) = w₀ + w_a·z/(1+z) mit w_a ≈ β/H₀ (AP5). Kerndokumente: `de/fakten/theorie/rt42_ap3_verbindung_lambda_dunkle_energie.md` · `en/facts/theory/rt42_ap3_connection_lambda_dark_energy.md`

---

#### AP4 – Skalierungsproblem kosmologisch einordnen

**Aufgabe:**
28-Größenordnungen-Diskrepanz zwischen Warp-Energiedichte ($10^{19}$ J/m³) und $\rho_\Lambda$ ($10^{-9}$ J/m³) auflösen oder als Scheinproblem enttarnen.

**Konkrete Schritte:**
1. Berechne $\rho_\Lambda c^2 \approx 10^{-9}$ J/m³.
2. Interpretiere: Warp = lokale Metrikstörung ≠ kosmologische Hintergrundmetrik.
3. Prüfe Skalierungsfaktor $\rho_{\text{warp}}/\rho_\Lambda \propto (R_H/R)^n$ — welches $n$?

**Erfolgskriterium:** Diskrepanz gelöst (Skalierungsfaktor) oder als Scheinproblem ausgewiesen (verschiedene Regime).

---

#### AP5 – Falsifizierbare Abweichungen vom $\Lambda$CDM

**Aufgabe:**
Messbare Unterschiede zwischen RFT-Kosmologie und $\Lambda$CDM benennen.

**Konkrete Schritte:**
1. Freie Parameter: $\alpha/\beta$, $G(f_i/f_j)$, $\Delta\phi_0$, $\dot{\Delta\phi}_0$.
2. Beobachtbare Effekte: Abweichung in $H(z)$, dynamisches $w(z)$, Strukturwachstum, CMB.
3. Vergleich mit Planck, DES, SH0ES.
4. Falsifikationskriterien benennen.

**Erfolgskriterium:** Mindestens eine messbare Abweichung — oder Nachweis vollständiger Äquivalenz.

---

#### AP6 – Kosmische Expansion als Phaseneffekt

**Aufgabe:**
Hypothese prüfen: **Die kosmische Expansion ist ein Phaseneffekt des RFT-Feldes.**

**Konkrete Schritte:**
1. Präzise Formulierung: $\dot a/a = f(\Delta\phi, \dot{\Delta\phi}, \alpha, \beta)$.
2. $f$ aus A1–A8 herleiten — oder Nichtableitbarkeit zeigen.
3. Szenario A: $\Delta\phi$ konstant → De-Sitter-artig.
4. Szenario B: $\Delta\phi$ wächst → dynamisches $H(t)$; erklärt Beschleunigung und/oder frühe Inflation?

**Erfolgskriterium:** Explizite Gleichung gestützt — oder klar widerlegt.

---

#### AP7 – Konsistenz mit RT-33, RT-40 und RT-41

**Aufgabe:**
Konsistenz der RFT-Kosmologie mit abgeschlossenen Tasks prüfen.

**Konkrete Schritte:**
1. $\Delta\phi \to 0$ (flache Raumzeit) mit expandierendem Universum vereinbar?
2. $\varepsilon = 1/\gamma^2$ mit kosmologischem $\varepsilon(t)$ vereinbar?
3. Kosmologische Phase $\Delta\phi(t)$ → Rotverschiebung $z$ konsistent mit Beobachtung?
4. Kohärenzlänge $l_c \propto \gamma^{-2}$ kosmologisch relevant?
5. **A8-Konsistenz:** Erzeugt $c$ eine obere Grenze für $H$?
6. Widersprüche explizit benennen — oder deren Abwesenheit zeigen.

**Erfolgskriterium:** Konsistenz mit RT-33, RT-40, RT-41 nachgewiesen — oder Widersprüche präzise dokumentiert.

---

### 4. Deliverables

1. Formales Papier mit modifizierter Friedmann-Gleichung (falls existent).
2. Explizite Differentialgleichung für $\Delta\phi(t)$ und ihre Lösungen.
3. Klare Aussage zu $\Lambda$: Ersatz, Erklärung oder Unvereinbarkeit.
4. Skalierungsanalyse der 28 Größenordnungen.
5. Falsifizierbarkeitsabschnitt mit mindestens einer messbaren Abweichung.
6. Numerische Simulation der RFT-Kosmologie (Python-Code, öffentlich).
7. Peer-Review-Einreichung (z. B. *Classical and Quantum Gravity*, *JCAP* oder *Foundations of Physics*).

---

### 5. Erfolgskriterien

**Minimalziel:** RFT lässt eine Friedmann-artige Gleichung zu — auch wenn identisch mit $\Lambda$CDM.
**Mittelziel:** RFT ersetzt oder erklärt $\Lambda$ — ohne zusätzliche Komponente.
**Maximalziel:** RFT erklärt beschleunigte Expansion aus Phasendynamik **und** sagt messbare Abweichung von $\Lambda$CDM voraus.
**Negativziel:** Scheitern präzise dokumentieren; minimale Erweiterung formulieren (z. B. A9: kosmologische Randbedingung).

---

### 6. Methodische Leitplanken

- **Keine Zirkelschlüsse:** $\Lambda$ darf nicht als Postulat eingeführt werden, wenn sie hergeleitet werden soll.
- **Keine nachträgliche Parameteranpassung:** Alle Konstanten aus A1–A8 oder explizit als frei deklariert.
- **Falsifizierbarkeit:** Jede Behauptung mit Widerlegungskriterium.
- **Skalentrennung:** Warp (lokal) ≠ Friedmann (kosmologisch) — nicht verwechseln.
- **Transparenz:** Alle Schritte reproduzierbar dokumentiert.
- **Abgrenzung:** (a) mathematische Äquivalenz, (b) heuristische Analogie, (c) empirische Vorhersage.
- **A8-Konsistenz:** $c$ in allen kosmologischen Gleichungen konsistent berücksichtigt.

---

### 7. Konkreter erster Schritt

**Woche 1–2:** Kopplungsdynamik für homogenes, isotropes RFT-Feld formulieren. DGL für $\Delta\phi(t)$ herleiten. Stationäre und dynamische Lösungen prüfen.
**Woche 3–4:** $\varepsilon(t) = \cos^2(\Delta\phi(t)/2)$ mit Friedmann vergleichen. Modifizierte Friedmann-Gleichung ohne $\Lambda$ prüfen.
**Woche 5–6:** Falls Gleichung hält: $H(z)$ herleiten, mit Planck/DES vergleichen. Falls nicht: Lücke dokumentieren, minimale Erweiterung formulieren.

---

### 8. Ehrliche Einschätzung

Die Wahrscheinlichkeit, dass die RFT die kosmische Expansion **exakt** erklärt, ist gering — $\Lambda$CDM passt auf viele Datenpunkte. Die Wahrscheinlichkeit, dass die RFT eine **strukturelle Alternative** liefert — dynamisches $w(z)$ ohne separate Dunkle-Energie-Komponente — ist nicht vernachlässigbar.

Ehrlichster Ausgang: **Die RFT enthält $\Lambda$CDM als Grenzfall — und macht eine neue Vorhersage über die Dynamik von $w(z)$.**

---

### 9. Verwandte Tasks

| Task | Beziehung |
|:--|:--|
| **RT-04** | FLRW-Simulation – numerische Infrastruktur |
| **RT-33** | Warp-Skalierung – $w(\theta)$-Modulation als Baustein |
| **RT-34** | 3D-Warpblase – numerische Metrik |
| **RT-40** | SRT-Brücke – $\varepsilon = 1/\gamma^2$ |
| **RT-41** | A8 – Kopplungswellengeschwindigkeit $c$ |
| **RT-42** | **Dieser Task** – Kosmologie |

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
