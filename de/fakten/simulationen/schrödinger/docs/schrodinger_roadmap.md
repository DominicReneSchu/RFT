# Schrödinger-Startstrecke (Forschungsprogramm, Minimalnachweis)

Ziel: Einen sauberen, reproduzierbaren Weg formulieren, wie aus einem resonanz-/phasenbasierten Modenmodell im geeigneten Grenzfall die nichtrelativistische Schrödinger-Gleichung entsteht, und parallel eine numerische Referenz implementieren, gegen die ein späteres Resonanz-Diskretmodell geprüft werden kann.

Kein Publikationsanspruch. Keine Aussagen zu ART/Eichtheorien. Fokus: QM eines einzelnen Teilchens.

---

## A. Minimalziel (Referenzgleichung)

Wir wollen als Zielgleichung reproduzieren:

$$
 i\hbar\,\partial_t\psi(x,t)= -\frac{\hbar^2}{2m}\,\nabla^2\psi(x,t)+V(x)\psi(x,t)
$$

mit:
- $\psi$: komplexe Wellenfunktion (Amplitude + Phase)
- $m$: effektive Masse (Parameter/Skala)
- $V(x)$: externes Potential (Parameterfeld)
- $\hbar$: Skalenfaktor zur Kopplung zwischen Phase und Energie

---

## B. Minimalannahmen (Resonanz-/Modenmodell → QM)

Wir nehmen ein diskretes Feld (Gitter) von Freiheitsgraden an, das lokal schwingt und über Nachbarschaft koppelt:

- Gitterpunkte $x_n = n\,a$ mit Gitterabstand $a$
- Feldvariable: Phase $\varphi_n(t)$ und (optional) Amplitude $A_n(t)$
- Komplexe Feldrepräsentation:
  $$
  \psi_n(t) := A_n(t)\,e^{i\varphi_n(t)}
  $$
- Lokale Frequenz / Energiebezug (als Arbeitsdefinition):
  $$
  E_n = \hbar\,\omega_n \quad,\quad \omega_n:=\partial_t\varphi_n
  $$
- Kopplung: eine Funktion der Phasendifferenz $\Delta\varphi_{n,n+1}$, z. B. über einen Kopplungsterm, der im Kontinuumsgrenzwert zu einem Laplace-Operator führt.

Wichtig: Die konkrete Form $\varepsilon(\Delta\varphi)$ bleibt hier offen. Entscheidend ist nur: Im kleinen-Gradienten-Grenzfall muss der Kopplungsterm auf etwas wie $\partial_x^2 \psi$ hinauslaufen.

---

## C. Konkreter Weg (diskret → kontinuierlich → Schrödinger-Form)

### Schritt C1: Diskretes komplexes Feld und lineare Näherung
Startpunkt ist nicht „Energie-Bilanz", sondern eine dynamische Gleichung für $\psi_n(t)$. Für kleine Phasengradienten und schwache Kopplung ist eine lineare Näherung plausibel:

$$
 i\,\partial_t \psi_n \approx -\kappa\,(\psi_{n+1}-2\psi_n+\psi_{n-1}) + U_n\,\psi_n
$$

- $\kappa$ ist eine Kopplungsstärke mit Dimension $1/\text{Zeit}$
- $U_n$ ist ein lokaler Term (entspricht später $V/\hbar$)

Diese Form ist bewusst gewählt, weil der diskrete Laplace-Operator bereits sichtbar ist.

### Schritt C2: Kontinuumsgrenzwert
Setze $x = n a$, $\psi_n(t)\to \psi(x,t)$ und benutze:

$$
\psi_{n\pm1} = \psi(x\pm a,t) \approx \psi \pm a\partial_x\psi + \frac{a^2}{2}\partial_x^2\psi
$$

Dann gilt:

$$
\psi_{n+1}-2\psi_n+\psi_{n-1} \approx a^2 \partial_x^2\psi
$$

Damit wird:

$$
 i\,\partial_t\psi = -\kappa\,a^2\,\partial_x^2\psi + U(x)\psi
$$

### Schritt C3: Identifikation von $\hbar$, $m$, $V$
Vergleiche mit:

$$
 i\hbar\,\partial_t\psi = -\frac{\hbar^2}{2m}\partial_x^2\psi + V\psi
$$

und identifiziere:

$$
 \kappa a^2 \equiv \frac{\hbar}{2m}
 \quad,\quad
 U(x) \equiv \frac{V(x)}{\hbar}
$$

Damit ist klar, was im Resonanzmodell „Masse" bedeutet: eine effektive Trägheitsskala, die aus Kopplungsstärke und Diskretisierung entsteht.

### Schritt C4: Wo „Resonanz" in die Gleichung kommt
Im Resonanzbild steckt die Physik in der Wahl des Kopplungsmechanismus, der im kleinen-Gradienten-Grenzfall genau diesen Laplace-Term erzeugt.

Offene Designfrage:
- Welche $\varepsilon(\Delta\varphi)$ führt zu einer linearen Kopplung in $\psi$?
- Welche nichtlinearen Korrekturen treten auf (führen z. B. zu nichtlinearer Schrödinger-Gleichung)?
- Welche Stabilitätsbedingungen gelten (Normerhaltung, Unitariät)?

---

## D. Numerische Referenz (wichtig für spätere Falsifikation/Abgleich)

Bevor ein Resonanz-Diskretmodell „Schrödinger emergent" behauptet, wird eine Referenz implementiert:

- 1D, freies Teilchen $V=0$ (Pflichttest)
- optional: harmonischer Oszillator oder Potentialtopf
- Initialzustand: Gauß-Wellenpaket
- Checks:
  - Normerhaltung $\int |\psi|^2 dx$
  - Erwartungswerte $\langle x\rangle, \langle p\rangle$
  - qualitative Ausbreitung (Dispersion)

Diese Referenz dient als Regressionstest: Resonanzmodell muss (im passenden Parameterregime) diese Kurven reproduzieren.

---

## E. Offene Punkte / TODOs (explizit)

1. **$\varepsilon(\Delta\varphi)$**: analytische Spezifikation + Begründung, warum im Grenzfall der Laplace-Term entsteht.
2. **Einheiten/Kalibrierung**: Dimensionlose vs. SI-Skalen. Mindestens: eindeutige Dokumentation, welche Größen dimensionslos sind.
3. **Herleitung statt Postulat**: Langfristig braucht es ein Wirkungsprinzip (Lagrange/Hamilton), aus dem die diskrete Dynamik folgt.
4. **Abgrenzung**: Keine kosmologischen/thermodynamischen Claims, solange der QM-Minimalfall nicht steht.

---

## F. Nächster Schritt (konkret)
- Implementiere `schrodinger_1d_free_particle.py` als Referenz.
- Ergänze Smoke-Test: Normabweichung nach N Schritten < Toleranz.
- Danach: Baue ein minimales Phasen-Kopplungsmodell und vergleiche numerisch gegen die Referenz.
