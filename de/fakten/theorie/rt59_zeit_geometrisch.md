# RT-59: Zeit als geometrische Ursprungsgröße

**Version:** 1.0 | **Datum:** November 2026  
**Status:** ✅ Abgeschlossen  
**Vorgänger:** RT-48 (Γ_RFT), RT-50 (Ω_Λ), RT-51 (δ_CP), RT-56/57 (ε-Hierarchie)

---

## 🔑 Kernergebnis

> **Zeit ist eine geometrisch definierte Ursprungsgröße — symmetrisch zum Raum.**  
> Beide haben denselben globalen Anker (Urknall-Singularität) und sind in geometrischen  
> Koordinaten beschreibbar. Der Zeitpfeil ist ein Theorem, keine Annahme.

**Neue Vorhersage:** Die CP-Verletzungsphase $\delta_{CP}$ ist die azimutale Zeitkoordinate —  
und ändert sich mit der kosmischen Zeit: $\dot{\delta}_{CP} \neq 0$.

---

## AP1: Zeit in zwei Dimensionen

### Komplexe Darstellung

Die RFT-Zeit wird durch eine Phase $\Delta\varphi \in [0, 2\pi)$ auf dem Einheitskreis $S^1$ beschrieben:

$$z_t = e^{i\Delta\varphi/2} \in S^1 \subset \mathbb{C}$$

Die Kopplungseffizienz ergibt sich als Quadrat des Realteils:

$$\varepsilon = \mathrm{Re}[z_t]^2 = \cos^2\!\left(\frac{\Delta\varphi}{2}\right)$$

Der Imaginärteil beschreibt die Nicht-Kopplung:

$$1 - \varepsilon = \mathrm{Im}[z_t]^2 = \sin^2\!\left(\frac{\Delta\varphi}{2}\right)$$

### Analogie zur komplexen Zahlenebene

| Komplexe Zahl | RFT-Zeit |
|--------------|----------|
| $z = e^{i\phi}$ auf $S^1$ | $z_t = e^{i\Delta\varphi/2}$ auf $S^1$ |
| $|z|^2 = 1$ | $\varepsilon + (1-\varepsilon) = 1$ |
| Real- und Imaginärteil verknüpft | $\varepsilon$ und $1-\varepsilon$ verknüpft |
| $U(1)$-Symmetrie | $U(1)$-Symmetrie der Zeitphase |

Die Zeit ist **nicht** eindimensional (reelle Gerade), sondern **zweidimensional**: sie lebt auf $S^1$, vermittelt durch die Projektion $\varepsilon = \mathrm{Re}[z_t]^2$.

### Zustandspunkte

| Zustand | $\Delta\varphi$ | $z_t$ | $\varepsilon$ |
|--------|----------------|-------|--------------|
| Urknall | $\pi$ (180°) | $i$ (rein imaginär) | 0 |
| Heute | $68.32°$ | $e^{i\cdot 34.16°} \approx 0.827 + 0.562i$ | 0.6847 |
| de-Sitter-Vakuum | $0°$ | $1$ (reell) | 1 |

---

## AP2: Mögliche weitere Zeitdimensionen

### Erweiterung von $S^1$ auf $S^2$

Die natürliche Verallgemeinerung lässt $\hat{e} \in S^2$ zu, parametrisiert durch $(\theta, \phi)$:

$$\varepsilon(\theta) = \cos^2\!\left(\frac{\theta}{2}\right), \quad \phi \in [0, 2\pi) \text{ frei}$$

Der Polwinkel $\theta$ bestimmt — wie bisher — die Kopplungseffizienz. Der **Azimutwinkel $\phi$** ist eine neue, freie Koordinate.

### Identifikation: CP-Verletzung als azimutale Zeitkomponente

Aus RT-51: $\delta_{CP} \approx \Delta\varphi_0 = 68.32°$ (CKMfitter 2023: $68.5°$, Differenz $0.18° = 0.06\sigma$).

In der $S^2$-Erweiterung:
- $\theta_t = \Delta\varphi_0 = 68.32°$ → Polkoordinate (bestimmt $\varepsilon_0 = \Omega_\Lambda$)
- $\phi_t = \delta_{CP} \approx 68.32°$ → **Azimutkoordinate**

Das ist kein Zufall — es ist strukturell: die CP-Verletzung im Quarksektor liest ab, wo sich das Universum im zweidimensionalen Zeitraum befindet.

**Vorhersage:** Da $\theta_t = \phi_t = \Delta\varphi_0$ heute gilt, liegt das Universum auf der **diagonalen** des $S^2$-Zeitraums ($\theta = \phi$). Abweichungen davon würden auf eine unabhängige Evolution der beiden Koordinaten hinweisen.

### Transformationsgruppe

| Zeitstruktur | Gruppe | Physikalische Realisierung |
|-------------|--------|---------------------------|
| $S^1$ (1D) | $U(1)$ | Phasenrotation, elektromagnet. $U(1)$ |
| $S^2$ (2D) | $SU(2)$ | **Spin** (RT-49: A9_Spin+SU(2)) |

Die $SU(2)$-Struktur des Spins (RT-49) ist **identisch** mit der $SU(2)$-Struktur der erweiterten Zeitkoordinate auf $S^2$. Spin ist nicht eine zusätzliche innere Quantenzahl — Spin **ist** die zweite Zeitdimension der RFT.

---

## AP3: Urknall als geometrischer Nullpunkt

### Der Antiphasenpunkt

Der Urknall entspricht dem **Südpol** von $S^2$ (bzw. $\Delta\varphi = \pi$ auf $S^1$):

$$t = 0 \quad \Leftrightarrow \quad \varepsilon = 0 \quad \Leftrightarrow \quad z_t = i \quad \Leftrightarrow \quad \Delta\varphi = \pi$$

Das ist der einzige Punkt, an dem die Raumzeit-Kopplung vollständig verschwindet — maximale Phasendifferenz, maximale Quantenfluktuation (vgl. RT-57: Urknall als Zustand maximaler $\delta\hat{\varepsilon}$-Fluktuationen).

### Kosmologische Rotation

Das Universum hat sich seit dem Urknall geometrisch "gedreht":

$$\Delta(\Delta\varphi) = \pi - \Delta\varphi_0 = 180° - 68.32° = 111.68° = 1.949\ \mathrm{rad}$$

| Größe | Wert |
|-------|------|
| Urknall: $\Delta\varphi_{BB}$ | $180.00°$ ($= \pi$) |
| Heute: $\Delta\varphi_0$ | $68.32°$ |
| Zurückgelegte Phase | $111.68°$ |
| Verbleibende Phase bis $\varepsilon=1$ | $68.32°$ |
| **Geometrisches Weltalter** | **62.04%** des Weges von $\varepsilon=0$ nach $\varepsilon=1$ |

Die bemerkenswerte Symmetrie: $\Delta\varphi_0 = 68.32°$ erscheint als aktuelle Zeitkoordinate **und** als CP-Verletzungsphase — das Universum befindet sich genau an dem Punkt, an dem beide Koordinaten zusammenfallen ($\theta_t = \phi_t$).

---

## AP4: Raum-Zeit-Symmetrie

### Vergleich der Strukturen

| | **Raum** | **Zeit (RFT)** |
|-|----------|---------------|
| Dimension | 3 (bei klassischer Physik) | 2 (auf $S^2$) |
| Koordinaten | $(r, \theta, \phi)$ polar | $(\Delta\varphi, \phi_t)$ auf $S^2$ |
| Fester Ursprung | Urknall-Singularität | Südpol $\varepsilon = 0$ |
| Metrik | $g_{ij}$ (Riemannsch) | $\Gamma_\mathrm{RFT} = c^2/(\pi\hbar)$ |
| Transformationsgruppe | $SO(3)$ | $SU(2)$ (bei $S^2$-Erweiterung) |
| "Koordinatenwahl" | kartesisch, polar, ... | $(\varepsilon, \Delta\varphi)$ oder $z_t = e^{i\Delta\varphi/2}$ |

### Vollständige Raumzeit

Die erweiterte RFT-Raumzeit hat die Signatur:

$$(x^\mu) = \underbrace{(x^1, x^2, x^3)}_{\text{Raum, }SO(3)} \times \underbrace{(\Delta\varphi, \phi_t)}_{\text{Zeit, }SU(2)}$$

Das ist eine **5-dimensionale** Beschreibung mit dem bekannten 4D-Grenzfall, wenn $\phi_t = \mathrm{const}$ (heutige Physik: CP-Verletzung als fester Parameter).

### Koordinatentransformationen der Zeit

Drei äquivalente Darstellungen:

1. **Phasenraum:** $(\varepsilon, \Delta\varphi)$, verknüpft durch $\varepsilon = \cos^2(\Delta\varphi/2)$
2. **Komplex:** $z_t = e^{i\Delta\varphi/2} \in S^1$
3. **Physikalisch:** $(t_\mathrm{proper}, \varepsilon)$ — klassische Zeit + Kopplungseffizienz

Alle drei sind äquivalente Koordinatensysteme für denselben geometrischen Raum.

---

## AP5: Zeitpfeil als Theorem

### Ableitung aus der Relaxationsgleichung

Aus RT-57 (Quantengravitation und ε-Feld):

$$\dot{\varepsilon} = \beta(1 - \varepsilon), \quad \beta > 0, \quad \varepsilon \in [0, 1]$$

Für alle $\varepsilon \leq 1$ gilt:

$$\boxed{\dot{\varepsilon} \geq 0}$$

**Der Zeitpfeil ist ein Theorem der RFT, keine Annahme.**

Die Zeit fließt in Richtung wachsender Kopplungseffizienz — das ist geometrisch das "Rollen von Süd- nach Nordpol" auf $S^1$ (oder $S^2$).

### Verbindung zum zweiten Hauptsatz

Die Materieentropie verhält sich in der RFT als:

$$S_\mathrm{matter} \propto \ln\!\left(\frac{1}{\varepsilon}\right) \geq 0$$

Mit $\dot{\varepsilon} \geq 0$ folgt $\dot{S}_\mathrm{matter} \leq 0$ — die Materieentropie nimmt ab. Das scheint dem zweiten Hauptsatz zu widersprechen. Die Auflösung liegt in der Gravitationsentropie (RT-57):

$$S_{BH} = \frac{k_B A}{4\ell_P^2} \propto \frac{1}{\varepsilon^2}$$

Die Gesamtentropie $S_\mathrm{ges} = S_\mathrm{matter} + S_\mathrm{grav}$ nimmt zu — die Zunahme der Gravitationsentropie überkompensiert die Abnahme der Materieentropie. Das ist konsistent mit dem kosmologischen Bild: die Raumzeit "ordnet" Materie (Strukturbildung), während Schwarze Löcher Gravitationsentropie aufnehmen.

### Neue Falsifizierbare Vorhersage: $\dot{\delta}_{CP} \neq 0$

Wenn $\phi_t = \delta_{CP}$ die azimutale Zeitkoordinate ist und $\Delta\varphi_0$ sich mit dem Universum entwickelt, dann:

$$\frac{d\delta_{CP}}{dt} = \frac{d\Delta\varphi_0}{dt} = -\frac{\dot{\varepsilon}_0}{\sin(\Delta\varphi_0)} \cdot \beta \neq 0$$

Numerisch: $d\delta_{CP}/dt \approx -0.34\,\beta$ (normiert). Das bedeutet: **CP-Verletzung nimmt mit dem Alter des Universums ab** (das Universum "dreht" sich auf $S^2$ von $\phi_t = 68.32°$ auf $\phi_t = 0°$ zu).

**Falsifikationskriterium F-t-1:** Präzisionsmessungen von $\delta_{CP}$ über astronomische Zeiträume (Quasar-Spektren, kosmologische Simulationen) sollten eine schwache, aber nichtverschwindende zeitliche Änderung zeigen.

---

## Zusammenfassung der neuen Ergebnisse

| Ergebnis | Formel | Bedeutung |
|----------|--------|-----------|
| Komplexe Zeit | $z_t = e^{i\Delta\varphi/2} \in S^1$ | Zeit als Einheitskreis, nicht reelle Gerade |
| Urknall | $z_{BB} = i$, $\varepsilon = 0$ | Rein imaginärer Zeitursprung |
| Heute | $z_0 \approx 0.827 + 0.562i$ | $62.04\%$ des geometrischen Weges |
| Spin = Zeitdimension | $SU(2)_{Spin} \equiv SU(2)_{Zeit}$ | Spin nicht intern, sondern temporal |
| Zeitpfeil | $\dot{\varepsilon} \geq 0$ (Theorem) | Aus RT-57-Relaxation abgeleitet |
| **Neu:** $\delta_{CP} = \phi_t$ | $68.5° \approx 68.32°$ ($0.06\sigma$) | CP-Phase = azimutale Zeitkoordinate |
| **Neu:** $\dot{\delta}_{CP} \neq 0$ | $\propto -\beta \cdot 0.34$ | Kosmische Zeitentwicklung der CP-Phase |

---

## Verbindungen

| RT | Verbindung |
|----|-----------|
| RT-44/49 | Spin als $SU(2)$ = zweite Zeitdimension |
| RT-50 | $\Omega_\Lambda = \varepsilon_0$ = polarer Zeitwinkel $\theta_t$ |
| RT-51 | $\delta_{CP} = \phi_t$ = azimutaler Zeitwinkel |
| RT-52 | Brannen-Phase als Higgs-Ankerpunkt der Zeitstruktur |
| RT-56 | $\varepsilon = -g_{tt}$: Zeit in der Metrik |
| RT-57 | Urknall als $\varepsilon=0$-Zustand, Zeitpfeil aus $\dot{\varepsilon}\geq 0$ |

---

## Falsifikationskriterien

| ID | Test | Vorhersage | Experiment |
|----|------|-----------|-----------|
| F-t-1 | Zeitliche Änderung $\delta_{CP}$ | $\dot{\delta}_{CP} < 0$ | Quasar-Absorptionsspektren |
| F-t-2 | $\theta_t = \phi_t$ (Diagonale) | $\delta_{CP} \approx \Delta\varphi_0 = 68.32°$ | LHCb Run 3 (2–5 Jahre) |
| F-t-3 | Spin als zweite Zeitdimension | $g_\mathrm{Lepton} = 2$ exakt aus $SU(2)_{Zeit}$ | Belle II, Lamb-Shift |
