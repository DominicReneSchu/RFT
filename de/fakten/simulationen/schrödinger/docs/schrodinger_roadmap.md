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

## E′. Kritikpunkt: Was der Gutachter als nächstes fragen wird

### Das Tautologie-Problem

Die bisherige Ableitung zeigt:

$$
\hat{H}_{\mathrm{res}} = \hat{H}_0 + \varepsilon(\Delta\varphi)\,\hat{V}_{\mathrm{Kopplung}}
$$

reproduziert die Standard-QM mit $V_{\mathrm{eff}} = \varepsilon \cdot V_{\mathrm{Kopplung}}$.

Das ist mathematisch eine **Tautologie**: Der Split-Operator sieht nur $V_{\mathrm{eff}}$, egal ob dieses als $\varepsilon(\Delta\varphi) \cdot V$ über eine Kopplung oder direkt als Potential hereingegeben wird. Ein kritischer Gutachter wird das sofort bemerken.

### Die entscheidende offene Frage: Woher kommt $\Delta\varphi$?

| Frage | Warum entscheidend |
|-------|-------------------|
| Ist $\Delta\varphi$ ein externer Parameter oder ein dynamisches Feld? | Wenn extern → RFT ist nur Umparametrisierung der Standard-QM |
| Hat $\Delta\varphi$ eine eigene Bewegungsgleichung? | Wenn ja → neue Physik möglich (und testbar) |
| Wie koppelt $\Delta\varphi$ an den Zustand $\psi$? | Rückkopplung $\psi \to \Delta\varphi \to V_{\mathrm{eff}} \to \psi$ wäre nicht-trivial |

### Konkrete Empfehlung

Ein `schrodinger_1d_rft_dynamic.py`, in dem $\Delta\varphi(t)$ **selbst dynamisch** ist – z. B. gekoppelt an $|\psi|^2$ oder an $\langle x \rangle$ – würde die RFT erstmals von Standard-QM **unterscheidbar** machen. Erst dann kann man sagen: *"RFT ist nicht nur eine Umschreibung, sondern eine Erweiterung."*

Das ist auch der Punkt, an dem Kritikpunkt 2.1 (ART-Grenzwert) und 2.2 (Eichinvarianz) erstmals angreifbar werden – sobald die Dynamik von $\Delta\varphi$ feststeht, lassen sich Vorhersagen ableiten, die experimentell testbar sind.

**Status:** Implementiert in [`python/schrodinger_1d_rft_dynamic.py`](../python/schrodinger_1d_rft_dynamic.py).

---

## G. Störungstheorie der RFT — Konvergenz gegen Standard-QM

### Gutachter-Empfehlung (adressiert)

> Im Limit λ → 0 (schwache Rückkopplung) muss die dynamische RFT gegen
> Standard-QM konvergieren, und die führenden Korrekturen müssen von
> Ordnung O(λ) sein. Das wäre die Störungstheorie der RFT.

### Störungsentwicklung

Schreibe $\psi_{\mathrm{RFT}} = \psi_0 + \lambda\,\psi_1 + O(\lambda^2)$
und $\Delta\varphi(t) = \Delta\varphi_0 + \lambda\,\varphi_1(t) + O(\lambda^2)$.

**Nullte Ordnung** ($\lambda = 0$):

$$
i\hbar\,\partial_t\psi_0 = [\hat{H}_0 + \varepsilon(\Delta\varphi_0)\,V]\,\psi_0
$$

Das ist exakt die Standard-Schrödinger-Gleichung mit $V_{\mathrm{eff}} = \varepsilon_0 \cdot V$.

**Erste Ordnung**:

$$
i\hbar\,\partial_t\psi_1 = [\hat{H}_0 + \varepsilon_0\,V]\,\psi_1 + \varepsilon'(\Delta\varphi_0)\,\varphi_1(t)\,V\,\psi_0
$$

wobei $\varphi_1(t) = \int_0^t F[\psi_0(t')]\,\mathrm{d}t'$ das integrierte
Rückkopplungsfunktional der ungestörten Lösung ist.

### Numerische Verifikation

Die Simulation [`python/schrodinger_1d_rft_perturbation.py`](../python/schrodinger_1d_rft_perturbation.py)
bestätigt die Störungstheorie über einen systematischen λ-Scan:

| Observable | Skalierung (numerisch) | Erwartet (Theorie) |
|------------|------------------------|--------------------|
| 1 − Fidelity | ~ λ^2.00 | O(λ²) |
| \|Δ⟨x⟩\| | ~ λ^1.00 | O(λ) |
| \|Δ⟨p⟩\| | ~ λ^1.00 | O(λ) |
| max\|Δψ\| | ~ λ^1.00 | O(λ) |

Zusätzlich stimmt die analytische Vorhersage 1. Ordnung für Δε mit der
Numerik bis auf relative Fehler < 0.02% überein.

### Konsequenzen

1. **Standard-QM ist exakter Grenzfall:** Für λ = 0 reproduziert die
   dynamische RFT die Standard-Schrödinger-Gleichung identisch
   (Fidelity = 1.000000000000).

2. **Kontrollierbare Korrekturen:** Abweichungen sind O(λ) in
   Erwartungswerten und O(λ²) in der Zustandstreue — die RFT ist
   eine wohldefinierte Erweiterung mit kontrolliertem Parameterraum.

3. **Normerhaltung:** Für alle λ bleibt die Norm erhalten (< 10⁻¹³),
   da V_eff stets reell ist und der Split-Operator unitär bleibt.

**Status:** Implementiert in [`python/schrodinger_1d_rft_perturbation.py`](../python/schrodinger_1d_rft_perturbation.py).

---

## H. Kritikpunkte — Gisin-Theorem, Axiom-Ableitung, Messdaten

### H.1 Axiomatische Ableitung des Rückkopplungsmodells

**Kritikpunkt:** Die drei Modelle (density, position, energy) in der
dynamischen Simulation sind ad hoc. Welches folgt aus den RFT-Axiomen?

**Antwort (Abschnitt G der Roadmap):**

Das density-Modell $\dot{\Delta\varphi} = \lambda \int |\psi|^4\,\mathrm{d}x$
lässt sich wie folgt aus dem RFT-Formalismus motivieren:

1. Das RFT-Kopplungsfunktional enthält den Term
   $S_{\mathrm{Kopplung}}[\psi, \varphi] = \int \varepsilon(\Delta\varphi) \cdot |\psi(x)|^2\,\mathrm{d}x$.

2. Variation nach $\Delta\varphi$ liefert $\varepsilon'(\Delta\varphi)$
   als Quelle der Phasendynamik.

3. Der Lokalisierungsterm $\int |\psi|^4\,\mathrm{d}x$ entsteht als
   niedrigste nichtlineare Korrektur im effektiven Wirkungsfunktional
   (analog zur Gross-Pitaevskii-Herleitung aus dem Kontaktwechselwirkungsterm).

4. Die Modelle position und energy bleiben als **alternative
   Rückkopplungshypothesen** erhalten — sie sind empirisch testbar,
   sobald Messdaten vorliegen (Kritikpunkt H.3).

**Offener Punkt:** Eine vollständige Ableitung aus einem
RFT-Wirkungsprinzip (Hamilton-/Lagrange-Formalismus) steht aus.
Das erfordert die Spezifikation der kinetischen Energie des φ-Feldes
(z.B. $\frac{1}{2}(\partial_t \Delta\varphi)^2$), was über den
aktuellen 1-Teilchen-Rahmen hinausgeht.

### H.2 Gisin-Theorem und No-Signaling-Bedingung

**Kritikpunkt:** Nichtlineare QM erlaubt prinzipiell superluminale
Signalisierung (Gisin 1990). Verletzt die RFT-Dynamik die
No-Signaling-Bedingung?

**Antwort:**

1. **1-Teilchen-Sektor:** In der vorliegenden 1D-Simulation gibt es
   kein Signaling-Problem. Die Dynamik ist nichtlinear, aber lokal
   (kein zweites Teilchen, an das ein Signal gesendet werden könnte).

2. **Norm ist erhalten:** Da $V_{\mathrm{eff}}$ stets reell ist, bleibt
   der Split-Operator unitär in jedem Einzelschritt. Numerisch bestätigt:
   Normabweichung < 10⁻¹³ für alle λ.

3. **Perturbativer Schutz:** Im Limit λ → 0 ist die Dynamik streng
   linear und unitär → No-Signaling gilt exakt. Für 0 < λ ≪ 1 sind
   Abweichungen von der Linearität O(λ) — das Gisin-Theorem greift
   erst bei endlichem λ im Mehrteilchensektor.

4. **Offener Punkt:** Die Frage der No-Signaling-Bedingung wird
   relevant, sobald die RFT auf den Mehrteilchensektor erweitert
   wird. Mögliche Auswege:
   - φ koppelt nur lokal an ψ (keine instantane Fernwirkung)
   - Dekoherenz unterdrückt nichtlineare Effekte im Vielteilchenlimit
   - λ_eff(N) → 0 für N → ∞ (thermodynamischer Grenzwert)

### H.3 Kontakt zu Messdaten (adressiert)

**Kritikpunkt 3.1 (SI-Einheiten, Kalibrierung) ist adressiert.**
Kritikpunkt 2.1 (ART-Grenzwert) bleibt offen.

Die Störungstheorie-Ergebnisse wurden auf ein konkretes physikalisches
System abgebildet: **ultrakalte ⁸⁷Rb-Atome in einer harmonischen Falle**.

**Falsifizierbare Vorhersage:**

$$
|\Delta\langle x\rangle|_\mathrm{SI} = 4.9 \cdot \lambda \cdot \ell
\approx 2.0 \cdot \lambda\;\mu\mathrm{m}
$$

wobei $\ell = V_\mathrm{strength}^{1/4} \cdot a_\mathrm{ho}$ die
Längeneinheit der Simulation ist. Für $\omega = 2\pi \times 100\;\mathrm{Hz}$
ergibt sich $a_\mathrm{ho} \approx 1.08\;\mu\mathrm{m}$ und
$\ell \approx 0.41\;\mu\mathrm{m}$.

Die Vorhersage ist messbar über Absorptionsbildgebung (Time-of-Flight)
mit räumlicher Auflösung ~ 1 µm. Detektierbarkeitsgrenze:
$\lambda \gtrsim 0.05$ nach 100 Wiederholungen.

| Schritt | Beschreibung | Status |
|---------|-------------|--------|
| Kalibrierung | Dimensionslose Parameter auf SI-Einheiten abbilden | ✅ [`schrodinger_1d_rft_experiment.py`](../python/schrodinger_1d_rft_experiment.py) |
| Experimenteller Vorschlag | Falsifizierbare Vorhersage für ⁸⁷Rb | ✅ [`experimental_proposal.md`](experimental_proposal.md) |
| Kritische Einordnung | GP-Problem (Kohn), Systematik, Gutachterfragen | ✅ `--critical` Flag + [Abschnitt 6](experimental_proposal.md#6-kritische-einordnung) |
| ART-Grenzwert | Kopplung von φ an die Metrik | ❌ Offen (bewusst abgegrenzt) |

---

## I. Nächste Schritte (aktualisiert)
- ~~Implementiere `schrodinger_1d_free_particle.py` als Referenz.~~ ✓ (`schrodinger_1d_reference.py`)
- ~~Ergänze Smoke-Test: Normabweichung nach N Schritten < Toleranz.~~ ✓
- ~~Baue ein minimales Phasen-Kopplungsmodell und vergleiche numerisch gegen die Referenz.~~ ✓ (`schrodinger_1d_rft.py`)
- ~~Dynamische Phasenkopplung $\Delta\varphi(t)$ mit Rückkopplung an $|\psi|^2$ implementieren.~~ ✓ (`schrodinger_1d_rft_dynamic.py`)
- ~~Störungstheorie: λ-Scan, Skalierungsanalyse, analytische Vorhersage.~~ ✓ (`schrodinger_1d_rft_perturbation.py`)
- ~~SI-Kalibrierung und experimenteller Vorschlag.~~ ✓ (`schrodinger_1d_rft_experiment.py`)
- ~~Kritische Einordnung: GP-Problem, Systematik, Peer-Review-Bilanz.~~ ✓ (`--critical`)
- **Offen:** 2-Teilchen-Erweiterung für Gisin-Theorem / No-Signaling
- **Offen:** Wirkungsprinzip (Lagrange-Dichte) für die Rückkopplung
