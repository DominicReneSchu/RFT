# RFT — Peer-Review Readiness

*Dominic René Schu, August 2026*

Dieses Dokument dokumentiert den Peer-Review-Bereitschaftsstatus der Resonanzfeldtheorie (RFT) nach Kategorien.

---

## Kategorie 1: Theoretische Grundlagen

| ID | Titel | Status | Verweis |
|----|-------|--------|---------|
| RT-01 | Wirkungsintegral-Herleitung von π | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` |
| RT-01a | π als Urkonstante: Operationale Definition und Dezimalartefakt-Argument | **Konzeptuell — formal offen** | `de/fakten/theorie/pi_als_urkonstante.md` · `en/facts/theory/pi_as_fundamental_constant.md` |
| RT-01b | Unabhängige π-Herleitung: Numerisches Pfadintegral + Nicht-Gaussian-Korrekturen | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` §4.5+§9 · `simulationen/rt01b/` |
| RT-02 | Gruppentheoretischer Beweis der Skalentransformation (A7) | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/gsync_gruppenstruktur.md` · `en/facts/theory/gsync_group_structure.md` |
| RT-31 | Resonanz-Hamiltonoperator für spezifische Quantensysteme | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/simulationen/hamilton/README.md` · `en/facts/simulations/hamilton/README.md` |
| RT-35 | A3 als Korollar von A7 in Axiomatik | **✅ Abgeschlossen (Aug 2026)** (durch RT-31) | `de/fakten/theorie/gsync_gruppenstruktur.md` §5 |
| RT-32 | Nichtlineare Sättigungsterme (λ_ε⁴) in der FLRW-Feldgleichung | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/simulationen/FLRW-Simulationen/core/coupled_flrw.py` · `README.md` §RT-32 |
| RT-11 | FLRW κ-Parameter: Konventionsdeklaration κ_RFT = 1 | **✅ Abgeschlossen (Aug 2026)** | `de/fakten/theorie/kappa_parameter_rft.md` |
| RT-03 | Unabhängige Bestimmung von λ (⁸⁷Rb-Vorhersage) | Offen | RESEARCH_TASKS.md |

### Anmerkung zu RT-01a

RT-01a ist die philosophisch-mathematische Voraussetzung von RT-01: Es dokumentiert, dass
die scheinbare Irrationalität von π und e ein Artefakt der Basis-10-Kodierung ist und
nicht ein Naturphänomen. Der Kreisumfang bei r = 1 ist physikalisch exakt messbar; die
unendliche Dezimaldarstellung 3,14159… ist eine Darstellungseigenschaft, keine
Natureigenschaft. Dieses Argument motiviert die Behandlung von π als geometrische
Fundamentalkonstante (Phasenraumkonstante) und damit den Faktor π in A4.

**Status:** Konzeptuell vollständig formuliert (Juli 2026) — formale Ableitung (operationale
Definition von π und e in einem natürlichen Einheitensystem) bleibt offen.

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
| A4 | Kopplungsenergie E = π·ε·ℏ·f | π geometrisch abgeleitet (RT-01, RT-01b, Aug 2026); ε darstellungstheoretisch erzwungen (RT-02) |
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
| RT-03 | Unabhängige λ-Bestimmung für RT-03-Vorhersage |

---

*Verwandt:* [RESEARCH_TASKS.md](RESEARCH_TASKS.md) |
[de/fakten/theorie/pi_als_urkonstante.md](de/fakten/theorie/pi_als_urkonstante.md) |
[en/facts/theory/pi_as_fundamental_constant.md](en/facts/theory/pi_as_fundamental_constant.md)
