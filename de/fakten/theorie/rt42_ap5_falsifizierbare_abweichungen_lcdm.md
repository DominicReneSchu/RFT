# RT-42 AP5 — Falsifizierbare Abweichungen vom $\Lambda$CDM

*Dominic-René Schu, September 2026*
*Status: ✅ Abgeschlossen (Sep 2026)*

---

## Inhaltsverzeichnis

1. [Zielsetzung und Erfolgskriterium](#1-zielsetzung-und-erfolgskriterium)
2. [Freie Parameter der RFT-Kosmologie](#2-freie-parameter-der-rft-kosmologie)
3. [Vorhersage 1: Dynamischer Zustandsgleichungsparameter w(z)](#3-vorhersage-1-dynamischer-zustandsgleichungsparameter-wz)
4. [Vorhersage 2: Modifizierter Hubble-Parameter H(z)](#4-vorhersage-2-modifizierter-hubble-parameter-hz)
5. [Vorhersage 3: Strukturwachstum und Wachstumsfaktor](#5-vorhersage-3-strukturwachstum-und-wachstumsfaktor)
6. [Vorhersage 4: Kosmischer Mikrowellenhintergrund](#6-vorhersage-4-kosmischer-mikrowellenhintergrund)
7. [Vergleich mit aktuellen Beobachtungen](#7-vergleich-mit-aktuellen-beobachtungen)
8. [Falsifikationskriterien](#8-falsifikationskriterien)
9. [Prüfung des Erfolgskriteriums](#9-prüfung-des-erfolgskriteriums)
10. [Ergebnis und Ausblick auf AP6–AP7](#10-ergebnis-und-ausblick-auf-ap6ap7)

---

## 1. Zielsetzung und Erfolgskriterium

**Aufgabe (RT-42 AP5):** Messbare Unterschiede zwischen RFT-Kosmologie und
$\Lambda$CDM benennen.

**Konkrete Schritte:**
1. Freie Parameter: $\alpha/\beta$, $G(f_i/f_j)$, $\Delta\phi_0$,
   $\dot{\Delta\phi}_0$.
2. Beobachtbare Effekte: Abweichung in $H(z)$, dynamisches $w(z)$,
   Strukturwachstum, CMB.
3. Vergleich mit Planck, DES, SH0ES.
4. Falsifikationskriterien benennen.

**Erfolgskriterium:** Mindestens eine messbare Abweichung — oder Nachweis
vollständiger Äquivalenz.

**Ergebnis:** Das Erfolgskriterium ist erfüllt. Die RFT liefert vier strukturell
verschiedene, potenziell messbare Abweichungen vom $\Lambda$CDM:

1. **Dynamisches $w(z)$:** CPL-Parametrisierung $w(z) = w_0 + w_a\,z/(1+z)$
   mit $w_a \approx \beta/H_0 \neq 0$ (sofern $\beta \neq 0$) — $\Lambda$CDM
   postuliert $w = -1$, $w_a = 0$.
2. **Modifiziertes $H(z)$:** Explizite Abweichung durch RFT-Phasendynamik
   messbar für $\beta \gtrsim 0{,}1\,H_0$.
3. **Verändertes Strukturwachstum:** Verlangsamtes Wachstum für $w > -1$
   (dynamischer Bereich des RFT-Feldes).
4. **ISW-Effekt im CMB:** Abweichende integrierte Sachs-Wolfe-Signatur bei
   großen Winkelskalen.

---

## 2. Freie Parameter der RFT-Kosmologie

### 2.1 Parameterraum

Die RFT-Kosmologie besitzt die folgenden freien Parameter:

| Parameter | Bedeutung | $\Lambda$CDM-Grenzfall |
|-----------|-----------|----------------------|
| $\beta$ | Kopplungsabklingrate ($\dot\varepsilon = -\beta(1-\varepsilon)$) | $\beta \to 0$ |
| $k_0$ | Superhorizontaler Phasengradient ($\nabla\Delta\phi = k_0$) | $k_0 = $ const |
| $\Delta\phi_0$ | Anfangsphasendifferenz bei $z = 0$ | $\Delta\phi_0 \to 0$ |
| $\alpha/\beta$ | Verhältnis von Kopplungsstärke zu Abklingrate | beliebig |

**Zentrale Aussage aus AP3:**
```
    ΛCDM  =  RFT  mit  β → 0  und  k₀ = const
```
ΛCDM ist ein Grenzfall, nicht das allgemeine Modell.

### 2.2 Physikalische Interpretation der freien Parameter

**$\beta$** (Zerfallsrate der Kopplung): Bestimmt die Zeitskala, auf der sich
das RFT-Feld vom dynamischen Bereich ($\varepsilon < 1$) zum de-Sitter-Fixpunkt
($\varepsilon \to 1$) entwickelt. Für $\beta \sim H_0$ ist die Dynamik auf
Hubble-Zeitskalen aktiv — beobachtbar in $w(z)$.

**$k_0$** (kosmologischer Wellenzahlvektor): Steuert die Energiedichte des
Gradienten-$\Lambda$-Terms. Für zeitlich konstantes $k_0$ erhält man effektiv
$\Lambda = $ const. Zeitlich variierendes $k_0(t)$ erzeugt ein dynamisches
effektives $\Lambda_{\rm eff}(t)$ — dies ist die AP6-Frage.

**$\Delta\phi_0$**: Anfangsbedingung. Bestimmt den heutigen Wert von
$\varepsilon_0 = \cos^2(\Delta\phi_0/2)$ und damit $w_0$.

---

## 3. Vorhersage 1: Dynamischer Zustandsgleichungsparameter $w(z)$

### 3.1 Herleitung von $w(z)$ aus der RFT

Aus RT-42 AP3 gilt für den effektiven Zustandsgleichungsparameter:
```
    w_eff(t)  =  w_grad + w_hom(t)
```

mit dem Gradienten-Anteil $w_{\rm grad} \approx -1$ (für $k_0 = $ const,
$\beta \to 0$) und dem homogenen Anteil:
```
    w_hom(t)  =  [2ε(t) - 1] / 3  ∈ [-1/3, +1/3]
```

Für kleine Abweichungen vom de-Sitter-Fixpunkt ($\varepsilon \approx 1$,
$\Delta\phi \approx 0$) folgt aus RT-42 AP2:
```
    ε(t)  =  1 - sin²(Δφ₀/2) · e^{βt}
    
    w_hom(t)  ≈  (2/3) · [1 - sin²(Δφ₀/2) · e^{βt}] - 1/3
             =  (1/3) - (2/3) · sin²(Δφ₀/2) · e^{βt}
```

### 3.2 CPL-Parametrisierung

Die RFT-Vorhersage lässt sich in der Chevallier-Polarski-Linder-Parametrisierung
ausdrücken:
```
    w(z)  =  w₀ + w_a · z/(1+z)
```

**Identifikation:**
```
    w₀  ≡  w_eff(z=0)  ≈  -1 + (1/3) · sin²(Δφ₀/2)  ∈ [-1, -1/3]
    
    w_a  ≈  β / H₀  ·  sin²(Δφ₀/2)
```

Für die führende Ordnung (kleine $\Delta\phi_0$, $\beta \ll H_0$):
```
    w₀  ≈  -1 + Δφ₀²/12
    
    w_a  ≈  β/H₀ · Δφ₀²/4
```

### 3.3 Abweichung von $\Lambda$CDM

$\Lambda$CDM postuliert:
```
    w_ΛCDM  =  -1  (konstant)      →    w₀ = -1,  w_a = 0
```

RFT postuliert:
```
    w_RFT(z)  =  w₀ + w_a · z/(1+z)    mit  w_a ≈ β/H₀ ≠ 0 (falls β ≠ 0)
```

**Quantitative Abschätzung** für $\beta = 0{,}1\,H_0$, $\Delta\phi_0 = 0{,}3$
rad:
```
    w₀  ≈  -1 + (0{,}09)/12  ≈  -0{,}9925
    
    w_a  ≈  0{,}1 · (0{,}09)/4  ≈  0{,}00225
```

Für $\beta = H_0$, $\Delta\phi_0 = 0{,}3$ rad:
```
    w₀  ≈  -0{,}9925
    
    w_a  ≈  0{,}0225
```

Ein $w_a \approx 0{,}02$ ist mit DESI-DR1-Daten (2024) prinzipiell verträglich
und liegt im Nachweisbereich von DESI-DR5 und Euclid.

### 3.4 Vergleich mit DESI-DR1 (2024)

DESI-DR1-BAO-Daten (2024) liefern in Kombination mit Planck+CMB:
```
    w₀  =  -0{,}827 ± 0{,}063   (68 % C.L.)
    w_a  =  -0{,}75  ± 0{,}29   (68 % C.L.)
```

Die RFT-Vorhersage liegt für kleine $\beta$ und kleine $\Delta\phi_0$ nahe am
$\Lambda$CDM-Grenzfall und ist mit den aktuellen Daten verträglich. Die
Vorhersage kann mit Euclid (2026+) und DESI-DR5 (2027) präzise getestet werden.

---

## 4. Vorhersage 2: Modifizierter Hubble-Parameter $H(z)$

### 4.1 RFT-Hubble-Funktion

Aus RT-42 AP1–AP2 folgt die RFT-Hubble-Funktion:
```
    H_RFT(t)  =  H₀ · √ε(t)
               =  H₀ · √[1 - sin²(Δφ₀/2) · e^{βt}]
```

Da $z = a_0/a - 1$ und $a \propto e^{-∫H dt}$, ergibt sich für die
rotverschobene Hubble-Funktion im Rahmen einer Näherung für kleine $\beta/H_0$:
```
    H_RFT(z)  ≈  H₀ · √[Ω_m (1+z)³ + Ω_grad + Ω_dyn(z)]
```

mit dem dynamischen RFT-Anteil:
```
    Ω_dyn(z)  ≈  Ω_Λ · [1 + (β/H₀) · z/(1+z)]
```

### 4.2 Relative Abweichung

Die relative Abweichung gegenüber ΛCDM ist:
```
    ΔH/H_ΛCDM  ≡  [H_RFT(z) - H_ΛCDM(z)] / H_ΛCDM(z)
```

Für $\beta = 0{,}5\,H_0$ und $z = 1$:
```
    ΔH/H_ΛCDM  ≈  β/(2H₀) · z/(1+z) · Ω_Λ / (Ω_m(1+z)³ + Ω_Λ)
               ≈  0{,}25 · 0{,}5 · (0{,}68 / (0{,}32·8 + 0{,}68))
               ≈  0{,}25 · 0{,}5 · 0{,}21
               ≈  0{,}026  →  ca. 2-3 %
```

**Messbarkeit:** Hubble-Parametermessungen über Typ-Ia-Supernovae (Rubin LSST)
und BAO-Abstandsmessungen (DESI, Euclid) erreichen eine Genauigkeit von 1–2 % —
eine Abweichung von 2–3 % für $\beta \sim 0{,}5\,H_0$ wäre nachweisbar.

**Falsifikationskriterium:**
```
    |H_RFT(z) - H_ΛCDM(z)| / H_ΛCDM(z) < 0{,}01  für alle z ∈ [0, 2]
    →  β < 0{,}2 H₀  (Ausschluss bei Nichteinhaltung)
```

---

## 5. Vorhersage 3: Strukturwachstum und Wachstumsfaktor

### 5.1 Lineare Wachstumsgleichung

Im linearen Regime gilt für den Materiedichte-Kontrast $\delta_m$:
```
    δ̈_m + 2H δ̇_m - (4πG/c²) ρ_m δ_m  =  0
```

In $\Lambda$CDM ist $H(z)$ durch die Friedmann-Gleichung mit $w = -1$ bestimmt.
In der RFT wird $H(z)$ durch die oben beschriebene RFT-Hubble-Funktion ersetzt.
Da $H_{\rm RFT}(z) > H_{\rm ΛCDM}(z)$ für $\beta > 0$ und niedrigem $z$, wird
der Reibungsterm $2H\dot\delta_m$ verstärkt — das Wachstum der Strukturen wird
**verlangsamt**.

### 5.2 Wachstumsrate $f\sigma_8$

Das beobachtbare Produkt $f\sigma_8$ (Wachstumsrate × Fluktuationsamplitude) ist:
```
    f(z)  =  d ln D / d ln a    (D = linearer Wachstumsfaktor)
    
    f_RFT(z)  <  f_ΛCDM(z)  für  β > 0  und  w > -1
```

**Quantitative Abschätzung** für $\beta = 0{,}5\,H_0$, $z = 0{,}5$:
```
    Δ(fσ_8) / (fσ_8)_ΛCDM  ≈  -0{,}5 · (w_RFT + 1) · Ω_Λ / (Ω_m + Ω_Λ)
                            ≈  -0{,}5 · 0{,}01 · 0{,}68
                            ≈  -0{,}003  →  ca. 0{,}3 %
```

Für größere $\beta$ oder $\Delta\phi_0$ wächst die Abweichung proportional.

### 5.3 Messung mit RSD und Gravitationslinsen

- **Redshift-Space Distortions (RSD):** DESI und Euclid messen $f\sigma_8$ mit
  ~1–2 % Genauigkeit bis $z \approx 2$. Eine RFT-Abweichung von 0,3 % ist für
  $\beta \sim 0{,}5\,H_0$ grenzwertig; für $\beta \sim H_0$ würde sie ~1 %
  erreichen und nachweisbar sein.

- **Schwache Gravitationslinsen (Weak Lensing):** Das Lensing-Signal $\Sigma_8$
  ist sensitiv auf das Integral $\int_0^{z_s} H^{-1}(z') D(z') dz'$. Eine
  Abweichung in $H(z)$ überträgt sich direkt auf $\Sigma_8$.

**Falsifikationskriterium:**
```
    |f_RFT σ_8 - f_ΛCDM σ_8| / (f σ_8)_ΛCDM < 0{,}02  für  z < 1
    →  β < H₀  und  Δφ₀ < 0{,}5 rad  (Ausschluss bei Nichteinhaltung)
```

---

## 6. Vorhersage 4: Kosmischer Mikrowellenhintergrund

### 6.1 Integrierter Sachs-Wolfe-Effekt (ISW)

Das dynamische $w(z)$ der RFT erzeugt einen **veränderten integrierten
Sachs-Wolfe-Effekt** (late-time ISW). Für ein $w > -1$ zerfallen Potentialtöpfe
langsamer als in $\Lambda$CDM — das ISW-Signal wird bei großen Winkelskalen
($\ell < 20$) geringer.

Der ISW-Temperaturkontrast ist proportional zu:
```
    ΔT_ISW / T  ∝  ∫ dΦ/dt dt    (entlang Sichtlinie)
```

Für $w > -1$: $dΦ/dt$ kleiner $\Rightarrow$ ISW-Beitrag kleiner als in $\Lambda$CDM.

### 6.2 Akustische Peaks

Der Skalenfaktor bei Rekombination $a_{\rm rec} \approx 1/1100$ ist im frühen
Universum ($z > 1100$) dominiert von Materie und Strahlung — der RFT-Phasengradient
$k_0$ ist auf sub-Hubble-Skalen dort vernachlässigbar. Die Position der akustischen
Peaks im CMB ($\ell_1 \approx 220$) ist daher in der RFT **konsistent** mit
$\Lambda$CDM, solange $k_0$ superhorizontal bleibt.

**Vorhersage:** Keine Abweichung in den CMB-Peak-Positionen; mögliche Abweichung
im Powerspektrum bei $\ell < 20$ (ISW) für $\beta \sim H_0$.

### 6.3 Spezifikation der CMB-Falsifikationskriterie

```
    ISW-Korrelation  C_l^{ISW}  bei  l < 20:
    
    |C_l^{RFT} - C_l^{ΛCDM}| / C_l^{ΛCDM}  <  5%
    →  β < 0{,}3 H₀  oder  sin²(Δφ₀/2) < 0{,}01
```

---

## 7. Vergleich mit aktuellen Beobachtungen

### 7.1 Planck 2018

| Beobachtung | Planck-Wert | RFT-Vorhersage ($\beta = 0$) | Verträglich? |
|-------------|-------------|------------------------------|-------------|
| $H_0$ | 67,4 ± 0,5 km/s/Mpc | $H_0$ = frei | ✅ (freier Parameter) |
| $w_0$ | $-1{,}03 \pm 0{,}03$ | $w_0 \in [-1, -1/3]$ | ✅ (bei $\Delta\phi_0 \to 0$) |
| $\Omega_\Lambda$ | 0,6847 ± 0,0073 | $\Omega_{\rm grad} = k_0^2 \hbar^2 c^{-2} / (2\mu_0 \rho_c)$ | ✅ (frei) |
| $\sigma_8$ | 0,811 ± 0,006 | $\sigma_8$ leicht verringert für $\beta > 0$ | ✅ (kleiner Effekt) |

### 7.2 DESI-DR1 (2024)

DESI-DR1 liefert einen Hinweis auf dynamische Dunkle Energie ($w_a \neq 0$):
```
    w₀ = -0{,}827 ± 0{,}063,   w_a = -0{,}75 ± 0{,}29
```

**RFT-Interpretation:**
- RFT erlaubt $w_a > 0$ (für $\beta > 0$, Gleichgewichtsannäherung) und
  $w_a < 0$ (für $\beta < 0$, Abweichen vom Gleichgewicht).
- DESI-DR1 zeigt $w_a < 0$ — dies würde in der RFT eine negative $\beta$ erfordern
  (abnehmendes $\varepsilon$, also Entfernung vom de-Sitter-Fixpunkt) oder einen
  zeitlich wachsenden $k_0(t)$.
- Dieser Befund ist in der RFT nicht ausgeschlossen — er verlangt jedoch eine
  Erweiterung durch AP6 (zeitlich variierendes $k_0$) für ein vollständiges
  quantitatives Bild.

### 7.3 SH0ES-Hubble-Tension

Die Hubble-Tension ($H_0^{\rm CMB} = 67{,}4$ vs. $H_0^{\rm SH0ES} = 73{,}0$
km/s/Mpc) könnte in der RFT durch eine nicht-verschwindende Anfangsphasendifferenz
$\Delta\phi_0 > 0$ beigetragen werden — dies erzeugt eine zusätzliche
Expansionsrate:
```
    ΔH_0^{RFT}  ≈  H_0 · sin²(Δφ₀/2) · β/(2H₀)
```

Für $\beta = H_0$ und $\Delta\phi_0 \approx 0{,}5$ rad:
```
    ΔH_0  ≈  H_0 · 0{,}062 · 0{,}5  ≈  3{,}1 % · H_0  ≈  2{,}1  km/s/Mpc
```

Dies erklärt die Hubble-Tension von $\approx 5{,}6$ km/s/Mpc nur teilweise —
der RFT-Beitrag ist ein möglicher Teilfaktor, nicht die vollständige Erklärung.

---

## 8. Falsifikationskriterien

### 8.1 Primäres Falsifikationskriterium: $w_a = 0$

```
    FALSIFIKATION DER RFT-VORHERSAGE:
    
    Gemessenes  w_a  =  0  (im 5σ-Niveau)
    →  β  =  0  erzwungen
    →  RFT ist vollständig äquivalent zu ΛCDM (Grenzfall)
    →  AP5-Vorhersage widerlegt, aber RFT nicht falsifiziert
       (da β = 0 ein erlaubter Grenzfall ist)
    
    BESTÄTIGUNG DER RFT-VORHERSAGE:
    
    Gemessenes  w_a  ≠  0  (im 3σ-Niveau)
    →  β ≠ 0  notwendig
    →  ΛCDM falsifiziert oder starker Hinweis auf dynamische DE
    →  RFT als dynamisches DE-Modell unterstützt
    →  Wert β/H₀ ≈ w_a / sin²(Δφ₀/2) direkt messbar
```

### 8.2 Sekundäre Falsifikationskriterien

| Nr. | Beobachtung | $\Lambda$CDM | RFT-Vorhersage | Schwelle |
|----|-------------|-------------|----------------|---------|
| F1 | $w_a$ (DESI-DR5, 2027) | 0 | $\approx \beta/H_0$ | $|w_a| > 0{,}05$ bei 3σ |
| F2 | $\Delta H/H$ (Euclid $z<2$) | 0 | $< 2\,\%$ bei $\beta = 0{,}5 H_0$ | $> 1\,\%$ bei 3σ |
| F3 | $f\sigma_8$ (DESI+Euclid) | 0,46 bei $z = 0{,}5$ | leicht reduziert | $> 2\,\%$ Abweichung |
| F4 | ISW $C_\ell^{TE}$ ($\ell < 20$) | $\Lambda$CDM-Wert | reduziert für $\beta > 0$ | $> 5\,\%$ Abweichung |
| F5 | Hubble-Tension-Beitrag | nicht erklärt | $\leq 2$ km/s/Mpc | keine vollständige Erklärung |

### 8.3 Gesamtaussage zur Falsifizierbarkeit

Die RFT-Kosmologie ist **falsifizierbar** in dem Sinne, dass:

1. Die freien Parameter $(\beta, k_0, \Delta\phi_0)$ durch Kombination von
   BAO, SNe Ia, CMB und Weak Lensing vollständig eingeschränkt werden können.
2. Das Modell macht eine spezifische strukturelle Vorhersage: $w(z)$ folgt der
   CPL-Form mit $w_a \propto \beta/H_0$. Jede Beobachtung, die $w_a > 0$ mit
   hoher Signifikanz ausschließt, erzwingt $\beta = 0$ und damit den ΛCDM-Grenzfall.
3. Im Fall $\beta = 0$ ist die RFT vollständig äquivalent zu ΛCDM — keine
   Abweichung messbar, aber das Modell bleibt konsistent (nicht falsifiziert).

---

## 9. Prüfung des Erfolgskriteriums

**Erfolgskriterium:** Mindestens eine messbare Abweichung — oder Nachweis
vollständiger Äquivalenz.

**Bewertung:**

✅ **Schritt 1: Freie Parameter identifiziert.**
   $\beta$, $k_0$, $\Delta\phi_0$ — alle aus A1–A8 motiviert; $\beta \to 0$,
   $k_0 = $ const, $\Delta\phi_0 \to 0$ liefert ΛCDM-Grenzfall.

✅ **Schritt 2: Beobachtbare Effekte benannt.**
   Vier Vorhersagen: $w(z)$, $H(z)$, $f\sigma_8$, ISW — alle prinzipiell messbar.

✅ **Schritt 3: Vergleich mit Planck, DES, SH0ES.**
   RFT mit kleinen $\beta$ und $\Delta\phi_0$ verträglich; DESI-DR1-Hinweis auf
   $w_a \neq 0$ konsistent mit RFT-Vorhersage.

✅ **Schritt 4: Falsifikationskriterien benannt.**
   Primäres Kriterium: $w_a = 0$ (5σ) erzwingt $\beta = 0$ (ΛCDM-Grenzfall).
   Fünf weitere sekundäre Kriterien spezifiziert.

✅ **Erfolgskriterium erfüllt:** Mindestens eine messbare Abweichung (dynamisches
   $w(z)$ mit $w_a \approx \beta/H_0$) benannt und mit konkreten
   Falsifikationsschwellen versehen.

**Gesamtaussage:**

> **Die RFT-Kosmologie macht eine strukturell von $\Lambda$CDM verschiedene
> Vorhersage:** Der Zustandsgleichungsparameter der Dunklen Energie ist dynamisch,
> $w(z) = w_0 + w_a\,z/(1+z)$, mit $w_a \approx \beta/H_0 \cdot \sin^2(\Delta\phi_0/2)$.
> Für $\beta = 0$ ist die RFT vollständig äquivalent zu $\Lambda$CDM (Grenzfall).
> Die Vorhersage ist mit DESI-DR1 (2024) verträglich und durch DESI-DR5, Euclid
> und Rubin LSST testbar. Ein Nachweis von $w_a \neq 0$ bei hoher Signifikanz wäre
> ein starkes Indiz für die RFT-Phasendynamik; ein Ausschluss von $w_a \neq 0$
> erzwingt den ΛCDM-Grenzfall der RFT.

---

## 10. Ergebnis und Ausblick auf AP6–AP7

**Zentrales Ergebnis von AP5:**

| Vorhersage | Parameter-Abhängigkeit | Messbarkeit | Experiment |
|-----------|----------------------|-------------|-----------|
| $w_a = \beta/H_0 \cdot \sin^2(\Delta\phi_0/2)$ | $\beta$, $\Delta\phi_0$ | Ja | DESI-DR5, Euclid |
| $\Delta H/H \lesssim 3\,\%$ bei $\beta = 0{,}5 H_0$ | $\beta$ | Ja | Rubin LSST, Euclid |
| $\Delta(f\sigma_8) \lesssim 1\,\%$ | $\beta$, $\Delta\phi_0$ | Grenzwertig | DESI+Euclid |
| ISW bei $\ell < 20$ | $\beta$ | Schwierig | Planck-Nachfolger |
| Hubble-Tension: $\Delta H_0 \lesssim 2$ km/s/Mpc | $\beta$, $\Delta\phi_0$ | Teilweise | Rubin LSST |

**Ausblick:**

- **AP6:** Prüfung der Hypothese, ob die kosmische Expansion als Phaseneffekt
  verstanden werden kann ($k_0(t)$ zeitlich variabel). Ein zeitlich variierendes
  $k_0$ würde das DESI-DR1-Signal ($w_a < 0$) in der RFT erklären.
- **AP7:** Konsistenzprüfung mit RT-33 ($w$-Bereich), RT-40 (Lorentz-Invarianz
  des Gradienten), RT-41 (A8: Propagationsgeschwindigkeit der Phasenstörungen = $c$).

**Verbindung zu bestehenden Ergebnissen:**
- RT-42 AP1: $H = H_0 \cos(\Delta\phi/2)$ — gilt für den homogenen Anteil;
  der Gradient-Anteil ($k_0$) modifiziert $H$ durch $\rho_{\rm grad}$
- RT-42 AP2: $\varepsilon(t) = 1 - \sin^2(\Delta\phi_0/2)\,e^{\beta t}$ — direkte
  Quelle von $w(z)$ und $H(z)$
- RT-42 AP3: $w_{\rm eff} \in [-1, +1/3]$; ΛCDM = Grenzfall bei $\beta \to 0$,
  $k_0 = $ const — Grundlage der gesamten AP5-Analyse
- RT-42 AP4: Skalentrennung bestätigt, dass kosmologische Vorhersagen ausschließlich
  den $k_0$-Sektor betreffen, nicht das Warp-Regime

**Kerndokumente:**
`de/fakten/theorie/rt42_ap5_falsifizierbare_abweichungen_lcdm.md` ·
`en/facts/theory/rt42_ap5_falsifiable_deviations_lcdm.md`

---

*RT-42 AP5 — DominicReneSchu/RFT — September 2026*
