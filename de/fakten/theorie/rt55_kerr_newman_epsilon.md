# RT-55 — Kerr-Newman-Metrik: Ladung als ε-Verstärker

*Dominic-René Schu, November 2026*
*Status: ✅ Analytisch abgeschlossen (Nov 2026)*
*Vorgänger: RT-54 (Kerr ε-Modulation), RT-53 (Schwarzschild)*

---

## Das Ergebnis

Die Kerr-Newman-Metrik (massereiches, rotierendes, geladenes Schwarzes Loch) liefert:

$$\varepsilon_{\rm KN}(r,\vartheta) = 1 - \frac{r_S \cdot r - r_Q^2}{\Sigma}
= \underbrace{1 - \frac{r_S r}{\Sigma}}_{\varepsilon_{\rm Kerr}} + \underbrace{\frac{r_Q^2}{\Sigma}}_{\Delta\varepsilon_Q > 0}$$

mit:
- $\Sigma = r^2 + a^2\cos^2\vartheta$ (Kerr-Strukturfunktion)
- $r_Q^2 = kQ^2G/c^4$ (Ladungsradius, $k = 1/(4\pi\varepsilon_0)$)

**Ladung erhöht ε** gegenüber dem ungeladenen Kerr-BH. Das bedeutet:
Ladung schiebt das System **weg von der Entkopplung** (ε → 0).

---

## ε-Hierarchie der Schwarzen Löcher

| Metrik | ε-Form | Zusatz |
|--------|--------|--------|
| Minkowski | ε = 1 | kein BH |
| Schwarzschild | 1 − r_S/r | Masse M |
| Reißner-Nordström | 1 − (r_S·r − r_Q²)/r² | Masse + Ladung |
| Kerr | 1 − r_S·r/Σ | Masse + Spin |
| **Kerr-Newman** | **1 − (r_S·r − r_Q²)/Σ** | **Masse + Spin + Ladung** |

---

## Ereignishorizonte und No-Hair-Theorem

Die Horizonte: $\Delta_{\rm KN} = r^2 - r_S r + a^2 + r_Q^2 = 0$

$$r_H = \frac{r_S}{2} \pm \sqrt{\left(\frac{r_S}{2}\right)^2 - a^2 - r_Q^2}$$

**No-Hair-Theorem in der RFT:** Ein Schwarzes Loch ist vollständig durch drei Parameter
beschrieben: M (Masse), J (Spin), Q (Ladung) — entsprechend drei ε-Modifikationen.
Alle anderen Eigenschaften (Haare) verschwinden hinter dem Horizont.

Das ist in der RFT direkt erklärt: Hinter dem Horizont (ε ≤ 0) gibt es keine
Resonanzkopplung mehr — keine Information, keine "Haare" können entweichen.

**Extrem-Bedingung** (nacktes Singularität vermieden):
$$a^2 + r_Q^2 \leq \left(\frac{r_S}{2}\right)^2$$

In der RFT: Das Discriminante muss positiv bleiben, damit ε = 0 eine physikalische
Fläche (Horizont) und nicht ein mathematisches Artefakt ist.

---

## Physikalische Bedeutung der Ladungserhöhung von ε

An der Ergosphäre (ε_KN = 0, Äquator):
$$r_{\rm ergo,KN} = \frac{r_S}{2} + \sqrt{\left(\frac{r_S}{2}\right)^2 - r_Q^2}$$

Für Q > 0: r_ergo,KN < r_S/2 (kleiner als Kerr-Ergosphäre!).
Ladung **verkleinert** die Ergosphäre — weil sie ε erhöht und damit den
ε=0-Bereich nach innen verschiebt.

**Penrose-Prozess im KN:** Weniger effizient als reines Kerr-BH, weil die
Ergosphäre kleiner ist. Ladungsenergie konkurriert mit Rotationsenergie.

---

## Verbindung zu A5 (Energierichtung) und RT-54

Das Kerr-Newman-BH hat drei ausgezeichnete Richtungen in der Energiekugel:
1. ê_J (Rotationsachse, RT-54)
2. ê_Q (elektrisches Feldvektor)
3. ê_B (magnetisches Dipolmoment)

Das **magnetische Dipolmoment** des KN-BH:
$$\mu = Q \cdot a = Q \cdot \frac{J}{Mc}$$

Dieser Ausdruck ist identisch mit dem Dipolmoment eines geladenen Spinors mit g=2!

**RFT-Deutung:** Das KN-BH ist makroskopisch ein geladener Spinor — realisiert durch
die Kombination von Drehimpuls (RT-54: Kerr-ê_J) und Ladungsfeld (ê_Q).

---

## Falsifikationskriterien

| Kriterium | Bedingung | Test |
|-----------|-----------|------|
| **F-RT55-1** | ε_KN ≠ 1 − (r_Sr−r_Q²)/Σ bei Präzisionsmessungen | LIGO/LISA: extreme mass-ratio inspirals |
| **F-RT55-2** | Magnetisches Moment ≠ Qa bei KN-BH | Theoretische Konsistenz mit No-Hair |
| **F-RT55-3** | Extrem-KN verletzt Penrose-Schranke | Thermodynamik BH |

---

## Ausblick: RT-56

Das KN-BH ist das allgemeinste Schwarze Loch in der GR. RT-56 erweitert das
auf beliebige Raumzeiten: ε(x^μ) als allgemeines Gravitationsfeld.

---

*RT-55 — DominicReneSchu/RFT — November 2026*
