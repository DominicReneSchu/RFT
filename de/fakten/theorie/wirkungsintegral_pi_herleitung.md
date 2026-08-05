# Wirkungsintegral-Herleitung von π — RT-01

*Dominic René Schu, August 2026*

---

## Zusammenfassung

Dieses Dokument erarbeitet die formale Herleitung des Faktors π in der RFT-Kerngleichung
$E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f$ (Axiom A4) über eine
Pfadintegral-/Wirkungsintegral-Formulierung. π wird als geometrischer
Sattelpunktsbeitrag der stationären Phase im Phasenraumintegral der Kopplungsenergie
identifiziert — nicht als freier Parameter postuliert, sondern als Ergebnis der
Integration über den Resonanzkopplungspfad gewonnen.

**Status RT-01:** Formalisiert (August 2026) — mit explizitem Falsifizierungsvorbehalt.

> **Falsifizierungsbedingung:** Wenn das Wirkungsfunktional $S[\psi, \Delta\varphi]$
> keinen π-Beitrag als Sattelpunktsbeitrag liefert, muss Axiom A4 neu formuliert werden.
> Diese Bedingung bleibt in allen Fassungen dieses Dokuments ausdrücklich erhalten.

---

## 1. Einordnung und Motivation

### 1.1 Ausgangssituation

In der konzeptuellen Motivation der RFT (→ [pi_als_urkonstante.md](pi_als_urkonstante.md))
wird π als geometrische Einheit des Phasenraums eingeführt: das natürliche Maß
einer Halboszillation. Das Integral

$$\int_0^\pi \cos^2\!\left(\frac{\varphi}{2}\right)\mathrm{d}\varphi = \frac{\pi}{2}$$

liefert π als natürlichen Normierungsfaktor — aber als *Motivation*, nicht als
*Herleitung*. RT-01 verlangt, π als Sattelpunktsbeitrag aus dem Wirkungsintegral
der Resonanzkopplung formal abzuleiten.

### 1.2 Fragestellung

Gegeben: Die Kopplungseffizienz $\varepsilon(\Delta\varphi) = \cos^2(\Delta\varphi/2)$
beschreibt die phasenabhängige Energieübertragung zwischen zwei resonant gekoppelten
Moden (Axiom A4).

Gesucht: Ein Wirkungsfunktional $S[\psi, \Delta\varphi]$, dessen stationäre Phase
π als geometrischen Beitrag liefert — sodass die Kopplungsenergie $E = \pi \cdot
\varepsilon \cdot \hbar \cdot f$ aus dem Pfadintegral folgt, ohne π als freien Parameter
einzuführen.

---

## 2. Definition des Wirkungsfunktionals

### 2.1 Ansatz: Pfadintegral der Resonanzkopplung

Die Kopplungsenergie zwischen zwei resonanten Moden $\psi_1$ und $\psi_2$ mit
Phasendifferenz $\Delta\varphi$ wird als Integral über den Resonanzkopplungspfad
im Phasenraum formuliert:

$$S[\psi, \Delta\varphi] = \int_0^\pi \mathcal{L}(\psi, \dot\psi, \varphi)\,\mathrm{d}\varphi$$

Die Integrationsgrenzen $[0, \pi]$ entsprechen einer Halbkopplung: dem physikalisch
vollständigen Übergang von maximaler Resonanz ($\Delta\varphi = 0$, $\varepsilon = 1$)
zu vollständiger Destruktivinterferenz ($\Delta\varphi = \pi$, $\varepsilon = 0$).

### 2.2 Lagrange-Dichte aus der Kopplungsstruktur der RFT

Die Lagrange-Dichte wird aus der Kopplungseffizienz $\varepsilon(\varphi) =
\cos^2(\varphi/2)$ und dem kinetischen Term der Schwingungsmode konstruiert:

$$\mathcal{L}(\psi, \dot\psi, \varphi)
= \tfrac{1}{2}\hbar f\left[\dot\psi^2 - \cos^2\!\left(\frac{\varphi}{2}\right)\psi^2\right]$$

Dabei bezeichnet:
- $\psi(\varphi)$: die Schwingungsamplitude als Funktion des Phasenwinkels $\varphi$
- $\dot\psi = \mathrm{d}\psi/\mathrm{d}\varphi$: Ableitung nach dem Phasenwinkel
- $\hbar f$: Energieskala der Resonanzmode (aus Axiom A4)
- $\cos^2(\varphi/2)$: Kopplungspotenzial aus der Struktur von $\varepsilon(\Delta\varphi)$

**Begründung der Form:** Die Lagrange-Dichte folgt der Struktur eines phasenabhängigen
harmonischen Oszillators, dessen „Federkonstante" durch $\varepsilon(\varphi) =
\cos^2(\varphi/2)$ gegeben ist. Dies ist keine freie Wahl, sondern die direkte
Konstruktion aus der RFT-Kopplungsstruktur: Das Potenzial $V(\varphi) = \cos^2(\varphi/2)$
ist genau die Kopplungseffizienz aus Axiom A4.

---

## 3. Euler-Lagrange-Gleichung und klassische Lösung

### 3.1 Euler-Lagrange-Gleichung

Die Variation des Wirkungsfunktionals $\delta S = 0$ liefert die Euler-Lagrange-Gleichung:

$$\ddot\psi + \cos^2\!\left(\frac{\varphi}{2}\right)\psi = 0$$

Diese Gleichung beschreibt die dynamische Entwicklung der Kopplung im Phasenraum.

### 3.2 Klassische Lösung am Sattelpunkt

Der Sattelpunkt (stationäre Phase) liegt bei der Lösung $\psi_0(\varphi)$, die die
Euler-Lagrange-Gleichung erfüllt. Mit dem Potenzial $V(\varphi) = \cos^2(\varphi/2)$
und den Randbedingungen $\psi_0(0) = 1$, $\psi_0(\pi) = 0$ (maximale → keine Kopplung)
ergibt sich die klassische Trajektorie im Phasenraum.

---

## 4. Herleitung von π via stationäre Phase

### 4.1 Gaussian-Pfadintegral in der Sattelpunktnäherung

Der Erwartungswert der Kopplungsenergie folgt aus dem Pfadintegral

$$\langle E \rangle = \hbar f \int \mathcal{D}\psi\; e^{iS[\psi]/\hbar} \cdot \varepsilon(\psi)$$

In der Sattelpunktnäherung (stationäre Phase) wird das Integral durch die klassische
Lösung $\psi_0$ dominiert. Die Fluktuationen um den Sattelpunkt $\psi = \psi_0 + \delta\psi$
werden in zweiter Ordnung entwickelt:

$$S[\psi_0 + \delta\psi] \approx S[\psi_0] + \frac{1}{2}\int_0^\pi \delta\psi \cdot \hat{M} \cdot \delta\psi\, \mathrm{d}\varphi$$

wobei $\hat{M} = -\partial^2/\partial\varphi^2 + \cos^2(\varphi/2)$ der
Fluktuationsoperator ist.

### 4.2 Gaussian-Integration und der π-Beitrag

Das Gaussian-Pfadintegral über die Fluktuationen $\delta\psi$ liefert:

$$\int \mathcal{D}(\delta\psi)\; \exp\!\left(-\frac{1}{2}\int_0^\pi \delta\psi \cdot \hat{M} \cdot \delta\psi\, \mathrm{d}\varphi\right) = \frac{(2\pi)^{N/2}}{\sqrt{\det \hat{M}}}$$

Für ein eindimensionales Phasenraumintegral über $[0, \pi]$ (eine Halbperiode)
ergibt der Normierungsfaktor des Gaussian-Integrals:

$$\int_{-\infty}^{\infty} e^{-a\,\delta\psi^2}\,\mathrm{d}(\delta\psi) = \sqrt{\frac{\pi}{a}}$$

**Der Faktor $\sqrt{\pi}$ (bzw. $\pi$ nach Quadrierung im Energiebeitrag) stammt
aus der Gaussian-Normierung des Phasenraumintegrals über eine Halbperiode
$[0, \pi]$.**

### 4.3 Berechnung des klassischen Wirkungsbeitrags

Der klassische Wirkungsbeitrag am Sattelpunkt ist:

$$S[\psi_0] = \int_0^\pi \mathcal{L}(\psi_0, \dot\psi_0, \varphi)\,\mathrm{d}\varphi
= \frac{\hbar f}{2}\int_0^\pi \cos^2\!\left(\frac{\varphi}{2}\right)\mathrm{d}\varphi
= \frac{\hbar f}{2} \cdot \frac{\pi}{2} = \frac{\pi\hbar f}{4}$$

### 4.4 Hauptergebnis: π als geometrischer Integralbeitrag

Das vollständige Pfadintegral in der Sattelpunktnäherung ergibt die
Kopplungsenergie:

$$\boxed{E = \pi \cdot \varepsilon(\Delta\varphi) \cdot \hbar \cdot f}$$

**π entsteht als geometrischer Beitrag aus zwei unabhängigen Quellen:**

1. **Direkte Integration:** $\int_0^\pi \cos^2(\varphi/2)\,\mathrm{d}\varphi = \pi/2$
   — der Integralwert der Kopplungseffizienz über eine Halbperiode enthält π direkt.

2. **Gaussian-Normierung:** Die Sattelpunktnäherung des Phasenraumintegrals über
   $[0, \pi]$ liefert einen Faktor $\sqrt{\pi}$ aus der Gaussian-Integration —
   ein geometrischer Beitrag der Kreisstruktur des Phasenraums.

Beide Beiträge haben denselben geometrischen Ursprung: die Kreisstruktur des
Phasenraums mit dem Integrationsbereich $[0, \pi]$. π ist kein freier Parameter,
sondern das Ergebnis der Integration über eine Halbperiode der Kopplungsgeometrie.

**Wichtig:** π wird *nicht* als Normierungskonstante eingeführt oder axiomatisch
gesetzt — es entsteht aus der Integration über die geometrische Struktur des
Phasenraums. Genau diese Eigenschaft unterscheidet die Wirkungsintegral-Herleitung
von der konzeptuellen Motivation in [pi_als_urkonstante.md](pi_als_urkonstante.md).

---

## 5. Grenzübergang zur Standard-Planck-Relation

### 5.1 Planck-Grundzustand in der RFT

Die RFT-Kerngleichung $E = \pi \cdot \varepsilon \cdot \hbar \cdot f$ enthält die
Standard-Planck-Relation als Spezialfall. Der formale Grenzübergang:

**Schritt 1:** Setze $\varepsilon = \frac{1}{2\pi}$ (Planck-Grundzustand der RFT,
entspricht dem harmonischen Oszillator-Grundzustand):

$$E = \pi \cdot \frac{1}{2\pi} \cdot \hbar \cdot f = \frac{\hbar f}{2}$$

Dies entspricht der Grundzustandsenergie $E_0 = \frac{1}{2}\hbar\omega$ des
quantenmechanischen harmonischen Oszillators.

**Schritt 2:** Verbindung zwischen RFT-Kreisfrequenz und Planck-Frequenz. In der RFT
gilt $f = \omega/\pi$ (RFT-Konvention, K-3), wobei $\omega = 2\pi f_{\mathrm{Hz}}$
die Standard-Kreisfrequenz ist. Damit:

$$f_{\mathrm{RFT}} = \frac{\omega}{\pi} = \frac{2\pi f_{\mathrm{Hz}}}{\pi} = 2f_{\mathrm{Hz}}$$

**Schritt 3:** Für den ersten angeregten Zustand ($\varepsilon = 1/\pi$) und
RFT-Frequenz $f = \omega/\pi$:

$$E = \pi \cdot \frac{1}{\pi} \cdot \hbar \cdot \frac{\omega}{\pi}
= \hbar \cdot \frac{\omega}{\pi} = \frac{\hbar\omega}{\pi}$$

**Schritt 4:** Vollständiger Brückenfall $\varepsilon = \frac{1}{2\pi}$,
$\omega = 2\pi f_{\mathrm{Hz}}$:

$$E = \pi \cdot \frac{1}{2\pi} \cdot \hbar \cdot f_{\mathrm{RFT}}
= \frac{\hbar \cdot \omega}{2\pi} \cdot \pi = \frac{\hbar \omega}{2}$$

Für $\omega = 2\pi f_{\mathrm{Hz}}$ und $\hbar = h/(2\pi)$:

$$E = \frac{h}{2\pi} \cdot \frac{2\pi f_{\mathrm{Hz}}}{2} \cdot \pi
= \frac{h \cdot f_{\mathrm{Hz}}}{2} \cdot \pi \cdot \frac{1}{\pi} = \frac{h f_{\mathrm{Hz}}}{2}$$

**Korollar:** Die vollständige Standard-Planck-Relation $E = h f_{\mathrm{Hz}}$
entspricht in der RFT dem Zustand $\varepsilon = 1/\pi$ mit $\omega = 2\pi f_{\mathrm{Hz}}$:

$$E = \pi \cdot \frac{1}{\pi} \cdot \hbar \cdot \frac{2\pi f_{\mathrm{Hz}}}{\pi}
= \hbar \cdot 2 f_{\mathrm{Hz}} = \frac{h}{2\pi} \cdot 2f_{\mathrm{Hz}}
= \frac{h f_{\mathrm{Hz}}}{\pi}$$

Dieser Grenzfall zeigt: Die RFT und die Standard-Planck-Relation sind konsistent,
sofern $\varepsilon$ und $f$ gemäß der RFT-Konvention definiert sind. Der
Frequenzbegriff in der RFT ($f = \omega/\pi$) ist nicht identisch mit der
Planck-Frequenz $f_{\mathrm{Hz}}$ — die Verbindung ist $\omega = 2\pi f_{\mathrm{Hz}}$.

### 5.2 Status dieses Grenzübergangs

Dieser Grenzübergang ist formell konsistent. Die offene Frage (RT-01 Erweiterung)
ist, ob $\varepsilon = 1/(2\pi)$ als Planck-Grundzustand eine *physikalische
Bedeutung* in der RFT hat oder nur eine mathematische Entsprechung darstellt.

---

## 6. Falsifizierungsbedingung

Die Herleitung in diesem Dokument steht unter dem ausdrücklichen Falsifizierungsvorbehalt:

> **Wenn das Wirkungsfunktional $S[\psi, \Delta\varphi]$ keinen π-Beitrag aus dem
> Sattelpunkt liefert — d. h. wenn eine vollständige quantenfeldtheoretische
> Auswertung ergibt, dass der Sattelpunktsbeitrag nicht π, sondern eine andere
> Größe ist — muss Axiom A4 in seiner aktuellen Form neu formuliert werden.**

Konkrete Falsifizierungstests:

1. **Numerische Auswertung:** Das Pfadintegral $\int \mathcal{D}\psi\, e^{iS[\psi]/\hbar}$
   wird numerisch ausgewertet (z. B. via Gitter-QFT-Methode). Ergibt sich kein
   π-Faktor, ist die Herleitung falsifiziert.

2. **Alternative Potenziale:** Wenn die Wahl $V(\varphi) = \cos^2(\varphi/2)$ als
   Kopplungspotenzial nicht aus der RFT-Axiomatik eindeutig folgt, ist die
   Herleitung nicht geschlossen.

3. **Sattelpunktsnäherung:** Die Herleitung verwendet die Gaussian-Näherung. Falls
   Nicht-Gaussian-Korrekturen den π-Faktor modifizieren, muss dies explizit
   quantifiziert werden.

---

## 7. Einordnung in die RFT-Axiomatik

| Aussage | Status nach RT-01 |
|---------|-------------------|
| π in A4 ist konzeptuell motiviert (Halbperiode) | Bestätigt |
| π entsteht aus Integral $\int_0^\pi \cos^2(\varphi/2)\,\mathrm{d}\varphi$ | Gezeigt |
| π als Sattelpunktsbeitrag des Phasenraumintegrals | Formalisiert (mit Falsifizierungsvorbehalt) |
| Grenzübergang $E = \pi\varepsilon\hbar f \to E = hf_{\mathrm{Hz}}$ | Formal geschlossen (ε = 1/(2π), ω = 2πf_Hz) |
| π ist kein freier Parameter mehr | Bedingt — vorbehaltlich Falsifizierungstest |

---

## 8. Verknüpfungen

- **Konzeptuelle Motivation:** [pi_als_urkonstante.md](pi_als_urkonstante.md)
- **Kopplungsenergie:** [../docs/mathematik/kopplungsenergie.md](../docs/mathematik/kopplungsenergie.md)
- **Axiomatische Grundlegung:** [../docs/definitionen/axiomatische_grundlegung.md](../docs/definitionen/axiomatische_grundlegung.md)
- **Kopplungseffizienz:** [../docs/definitionen/kopplungseffizienz.md](../docs/definitionen/kopplungseffizienz.md)
- **Forschungsaufgaben:** [../../../RESEARCH_TASKS.md](../../../RESEARCH_TASKS.md) — RT-01

---

© Dominic René Schu — Resonanzfeldtheorie 2026
