# RFT — Peer-Review Readiness

*Dominic René Schu, August 2026*

Dieses Dokument dokumentiert den Peer-Review-Bereitschaftsstatus der Resonanzfeldtheorie (RFT) nach Kategorien.

---

## Kategorie 1: Theoretische Grundlagen

| ID | Titel | Status | Verweis |
|----|-------|--------|---------|
| RT-01 | Wirkungsintegral-Herleitung von π | **Formalisiert (Aug 2026)** | `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` |
| RT-01a | π als Urkonstante: Operationale Definition und Dezimalartefakt-Argument | **Konzeptuell — formal offen** | `de/fakten/theorie/pi_als_urkonstante.md` · `en/facts/theory/pi_as_fundamental_constant.md` |
| RT-01b | Unabhängige π-Herleitung: Numerisches Pfadintegral + Nicht-Gaussian-Korrekturen | **Abgeschlossen (Aug 2026)** | `de/fakten/theorie/wirkungsintegral_pi_herleitung.md` §4.5+§9 · `simulationen/rt01b/` |
| RT-02 | Gruppentheoretischer Beweis der Skalentransformation (A7) | **Abgeschlossen (Aug 2026)** | `de/fakten/theorie/gsync_gruppenstruktur.md` · `en/facts/theory/gsync_group_structure.md` |
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
| A3 | Resonanzfenster | Postuliert — testbar |
| A4 | Kopplungsenergie E = π·ε·ℏ·f | Postuliert; π geometrisch motiviert (RT-01, RT-01a); numerisch bestätigt (RT-01b) |
| A5 | Vektorialität der Energie | Postuliert — konzeptuelle Motivation: RT-01a |
| A6 | Resonanzerhaltung | Postuliert — testbar |
| A7 | Skalentransformation | Bewiesen — gruppentheoretisch (RT-02, Aug 2026); Domänenübertragung postuliert |

---

## Kategorie 3: Offene Formalisierungsschritte (blockierend für Peer Review)

| ID | Beschreibung |
|----|-------------|
| RT-01a | Operationale Definition von π und e als Phasenraumkonstanten (formal offen) |
| RT-01b | Numerisches Pfadintegral + Nicht-Gaussian-Korrekturen — **Abgeschlossen (Aug 2026)** |
| RT-02 | Gruppentheoretischer Beweis A7 — **Abgeschlossen (Aug 2026)** |
| RT-03 | Unabhängige λ-Bestimmung für RT-03-Vorhersage |

---

*Verwandt:* [RESEARCH_TASKS.md](RESEARCH_TASKS.md) |
[de/fakten/theorie/pi_als_urkonstante.md](de/fakten/theorie/pi_als_urkonstante.md) |
[en/facts/theory/pi_as_fundamental_constant.md](en/facts/theory/pi_as_fundamental_constant.md)
