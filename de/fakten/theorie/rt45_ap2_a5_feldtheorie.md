# RT-45 AP2 — A5 als Erweiterung der Standard-Feldtheorie

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Prüfen, ob A5 (Energierichtung) mit der Standard-Feldtheorie kompatibel
ist oder sie erweitert — mit explizitem Grenzfall.

**Ergebnis:** A5 ist eine **strukturelle Erweiterung** der Standard-Feldtheorie.
Im lokalen, nicht-relativistischen Grenzfall reduziert A5 auf die skalare
Energiebehandlung. Im kosmologischen und Warp-Regime liefert A5 qualitativ
neue physikalische Konsequenzen.

---

## 2. Präzise Formulierung von A5

**Axiom A5 (RT-36):** Energie hat Richtung im Resonanzfeld:

```
E⃗ = E_eff · ê(Δφ, ∇Φ)
```

mit:
- E_eff = π · ε(Δφ) · ħ · f (skalarer Betrag, aus A4)
- ê = Einheitsvektor in Richtung des Energieflusses
- ê hängt von Phasendifferenz Δφ und Feldgradient ∇Φ ab

**Status (RT-36):** A5 ist irreduzibel — ê kann nicht aus A1–A4 abgeleitet werden.

---

## 3. Vergleich mit Poynting-Vektor

```
S⃗ = (1/μ₀) · E⃗_EM × B⃗   [Energiefluss in der Elektrodynamik]
```

**Ist S⃗ ein Spezialfall von A5?**

Ja: S⃗ ist der elektromagnetische Energiefluss, und ê_EM = S⃗/|S⃗| ist die
Richtung des EM-Energieflusses. A5 verallgemeinert dieses Konzept:
- Poynting: ê nur für EM-Felder definiert
- A5: ê für beliebige Resonanzfelder definiert (EM, Gravitation, Quantenfelder)

**Unterschied:** A5 erlaubt auch nicht-EM-Energieflüsse (Gravitation, Phasengradienten)
als gerichtete Größen. Das ist eine echte Erweiterung.

---

## 4. Vergleich mit Energie-Impuls-Tensor T^μν

```
T^μν = (Energiedichte, Energiefluss; Impulsdichte, Spannungstensor)
T^00 = ρ (Energiedichte)
T^0i = S^i/c (Energiefluss in i-Richtung)
```

**Ist A5 eine Zerlegung von T^0i?**

Teilweise: T^0i beschreibt den Energiefluss in der Standardphysik. A5 fügt hinzu:
- T^00 ist selbst eine **gerichtete** Größe (nicht nur skalar)
- Die Richtung von E⃗ ist durch ê(Δφ, ∇Φ) gegeben, nicht durch Koordinatenwahl
- A5 macht den Energiebetrag von T^00 richtungsabhängig:

```
T^00_A5(x) = ρ(x) · ε²(Δφ(x))   [aus RT-43 AP1]
```

**Das ist eine strukturelle Erweiterung:** T^00 ist in der Standard-ART
rahmenabhängig, aber bei festem Rahmen skalar. A5 macht T^00 zusätzlich von
der lokalen Phasendifferenz Δφ(x) abhängig.

---

## 5. Lorentz-Kovarianz von A5

**Frage:** Transformiert sich E⃗ wie ein Vierervektor?

**Antwort:** E⃗ transformiert sich **nicht** wie ein Vierervektor — es ist ein
3-Vektor im Resonanzfeld. Die Lorentz-kovarianante Erweiterung wäre ein
Viererstrom J^μ_E = (ρ_E, E⃗/c) mit entsprechendem Transformationsverhalten.

**Status:** Die relativistische Formulierung von A5 als Vierervektor ist offen
(Richtung RT-40-Erweiterung). Im nicht-relativistischen Grenzfall ist A5
konsistent mit der Newton'schen Mechanik (P = F⃗·v⃗).

---

## 6. Grenzfall: Wann reduziert A5 auf Standard-Feldtheorie?

A5 reduziert auf die skalare Standard-Behandlung unter folgenden Bedingungen:

| Bedingung | Auswirkung |
|-----------|-----------|
| ê · ∇ε ≈ 0 (homogenes ε) | E⃗ ≈ skalares E |
| Δφ → 0 überall (volle Kopplung) | ê fixiert durch Hintergrundfeld |
| v ≪ c (nicht-relativistisch) | Vierervektor-Struktur vernachlässigbar |
| ∇Φ ≈ 0 (schwacher Gradient) | Richtungseffekte klein |

**Ergebnis:** Standardphysik ist der Grenzfall ε = 1, ∇Δφ = 0 von A5.

---

## 7. Ergebnis

**A5 ist eine strukturelle Erweiterung der Standard-Feldtheorie:**
- Kompatibel im lokalen, homogenen Grenzfall (Standard-Feldtheorie als Grenzfall)
- Erweitert im gradientenreichen Regime (Warp, Kosmologie)
- Nicht-relativistische Formulierung: konsistent
- Relativistische Formulierung (Vierervektor): offen

**Erfolgskriterium:** ✅ Erfüllt — klare Aussage mit explizitem Grenzfall.

---

*RT-45 AP2 — DominicReneSchu/RFT — November 2026*
