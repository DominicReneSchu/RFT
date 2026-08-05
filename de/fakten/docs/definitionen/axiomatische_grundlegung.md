# Axiomatische Grundlegung der Resonanzfeldtheorie

*Dominic-René Schu, 2025/2026*

---

## 1. Einleitung

Die Resonanzfeldtheorie (RFT) beschreibt fundamentale Prozesse in Natur, Technik
und Informationssystemen als Kopplungs- und Resonanzphänomene in Schwingungsfeldern.

Dieses Dokument legt das axiomatische Fundament der Theorie dar. Die Axiome sind
so gewählt, dass sie:

- **minimal** sind (kein Axiom folgt aus den übrigen),
- **formal präzise** formuliert sind (jedes Axiom enthält eine mathematische Aussage),
- **empirisch testbar** sind (jedes Axiom macht eine überprüfbare Vorhersage).

---

## 2. Symboltabelle

### 2.1 Energie und Schwingung

| Symbol | Bedeutung |
|:------:|:----------|
| h | Plancksches Wirkungsquantum |
| f | Frequenz — in der RFT-Grundformel definiert als RFT-Resonanzfrequenz f = E/(π·ℏ) (rad/s); entspricht f = ω/π mit ω = E/ℏ (Standard-Kreisfrequenz). Nicht identisch mit Standard-Hz-Frequenz f_Hz = E/h. Offene Frage: → RESEARCH_TASKS.md RT-01 (K-3); konzeptuelle Grundlage: RT-01a (→ [theorie/pi_als_urkonstante.md](../../theorie/pi_als_urkonstante.md)) |
| ω | Standard-Kreisfrequenz (rad/s); in der RFT-Grundformel gilt f = ω/π (nicht f := ω). Für RFT-Rechnungen wird f verwendet |
| k | Wellenzahl |
| A | Amplitude |
| φ | Phase |
| ψ(x,t) | Schwingungsfunktion (Mode) |
| Φ(x,t) | Gesamtfeldfunktion (Superposition aller Moden) |
| E | Energie (Vektor im Resonanzfeld) |
| E₀ | Charakteristische Energie (Normierung) |

### 2.2 Kopplung und Struktur

| Symbol | Bedeutung |
|:------:|:----------|
| ε(Δφ) | Kopplungseffizienz, Funktion der Phasendifferenz |
| K_ij | Kopplungsstärke zwischen Moden i und j |
| δ | Breite des Resonanzfensters |
| m, n | Resonanzquantenzahlen (m, n ∈ ℤ⁺) |
| Δφ | Phasendifferenz zwischen gekoppelten Moden |
| G(f₁/f₂) | Gewichtungsfunktion des Resonanzfensters |

### 2.3 Information und Ordnung

| Symbol | Bedeutung |
|:------:|:----------|
| S | Entropie einer Resonanzkonfiguration |
| MI(X,Y) | Mutual Information: H(X) + H(Y) − H(X,Y) |
| PCI | Phase Coherence Index: |⟨exp(i(φ₁−φ₂))⟩| ∈ [0,1] |

### 2.4 Symmetrie

| Symbol | Bedeutung |
|:------:|:----------|
| G_sync | Gruppe synchroner Transformationen |
| T | Element von G_sync: T(f_i, φ_i, t) = (λf_i, φ_i + φ₀, at + b) |
| Λ | Frequenzskalierungsoperator |

---

## 3. Axiomensystem

### Axiom 1 — Universelle Schwingung

**Aussage:** Jede physikalische Entität besitzt mindestens eine periodische
Schwingungsmode.

**Formalisierung:**

```
(A1)    ψ(x, t) = A · cos(kx − ωt + φ)
```

**Testbare Vorhersage:** Jedes System lässt sich in periodische Komponenten
zerlegen (Fourier-Zerlegung). In Finanzmärkten: Der Preis lässt sich in
DC-Komponente (Trend) und AC-Komponente (handelbare Schwingung) zerlegen.

**Physikalisches Beispiel:** Eigenschwingungen eines Mikrowellenresonators.

**Empirischer Nachweis (RFT-intern):** FLRW-Simulation: η ≈ cos²(Δφ/2),
Δd_η > 6σ (1.530 Läufe). Die Eigenfrequenz jedes physikalischen Systems
ist messbar (Fourier-Zerlegung).

**Hinweis zum Geltungsbereich:** A1 setzt die Existenz mindestens einer periodischen
Mode voraus — dies ist äquivalent zur Existenz einer Fourier-Zerlegung (Satz der
Funktionalanalysis). Die physikalische Aussage ist die Anwendbarkeit dieser Zerlegung
auf reale Systeme inklusive Finanzmärkte. Die operationale Abgrenzung für
nicht-physikalische Systeme ist eine offene Forschungsfrage (siehe RESEARCH_TASKS.md).

---

### Axiom 2 — Superposition

**Aussage:** Schwingungsmoden überlagern sich linear in Feldern.

**Formalisierung:**

```
(A2)    Φ(x, t) = Σᵢ ψᵢ(x, t) = Σᵢ Aᵢ · cos(kᵢx − ωᵢt + φᵢ)
```

**Testbare Vorhersage:** Die Überlagerung mehrerer Moden erzeugt
Interferenzmuster. In Finanzmärkten: Kurzfristige und langfristige
Schwingungen überlagern sich im Preissignal.

**Physikalisches Beispiel:** Interferenz zweier kohärenter Laserstrahlen.

---

### Axiom 3 — Resonanzbedingung

**Aussage:** Resonanz zwischen zwei Systemen tritt auf, wenn ihre Frequenzen
in einem rationalen Verhältnis stehen, innerhalb eines Toleranzfensters δ.

**Formalisierung:**

```
(A3)    |f₁/f₂ − m/n| < δ,    m, n ∈ ℤ⁺

        G(f₁/f₂) = exp(−(|f₁/f₂ − m/n| / δ)²)
```

G ist die Gewichtungsfunktion: maximal bei exakter Resonanz, abfallend
mit der Verstimmung.

**Hinweis zur Toleranz δ:** A3 erfordert keine exakt rationalen Frequenzverhältnisse,
sondern nur Verhältnisse innerhalb des Toleranzfensters δ: |f₁/f₂ − m/n| < δ.
Die GDR-Frequenz f_GDR = E_GDR/(π·ℏ) ist irrational, liegt aber innerhalb δ eines
rationalen Verhältnisses. Das Toleranzfenster δ ist ein Modellparameter der RFT —
kein freier Parameter, da es physikalisch durch die Resonanzbreite Γ_GDR ≈ 4–5 MeV
bestimmt wird (siehe material.py).

**Korollar-Verweis (RT-02, RT-35):** A3 ist durch RT-02 als **Konsequenz von A7**
identifiziert worden: Die Quantisierungsbedingung fᵢ/fⱼ ∈ ℚ folgt aus der
Darstellungsstruktur der Untergruppe ℝ⁺_× ⊂ G_sync (Korollar in
`de/fakten/theorie/gsync_gruppenstruktur.md` §5, abgeschlossen durch RT-31/RT-35).
A3 ist damit kein unabhängiges Axiom mehr, sondern ein abgeleiteter Satz.

**Testbare Vorhersage:** Systeme mit verschiedenen Eigenfrequenzen können
resonant koppeln. Systeme mit identischen Eigenfrequenzen schwingen synchron —
keine Obertöne, kein Informationsaustausch.

**Empirischer Nachweis (RFT-intern):** Monte-Carlo-Test auf CMS-Dielektron-Daten:
5 Resonanzen bei Teilchenmassen, emp. p = 0 (1.500.000 Simulationen, 3 KDE,
30 Seeds). CERN-Resonanzanalyse: signifikante Resonanzüberschüsse in Massendaten.

---

### Axiom 4 — Kopplungsenergie

**Aussage:** Die effektive Energie einer resonanten Kopplung ist bestimmt
durch Frequenz, Kopplungseffizienz und die zyklische Geometrie des
Resonanzpfads.

**Formalisierung:**

```
(A4)    E_eff = π · ε(Δφ) · ℏ · f

        Bei Mehrmodenkopplung:
        E_eff = π · ε(Δφ_ij) · ℏ · ⟨f_ij⟩
```

Dabei ist (f = RFT-Resonanzfrequenz = E/(π·ℏ), rad/s; vgl. K-3):
- ε(Δφ) die Kopplungseffizienz als Funktion der Phasendifferenz,
  z.B. ε(Δφ) = cos²(Δφ/2)
- π der geometrische Faktor aus der Integration über einen Halbzyklus
  des Resonanzpfads (geometrische Motivation: siehe §4.1;
  formale Herleitung via Wirkungsintegral: → [theorie/wirkungsintegral_pi_herleitung.md](../../theorie/wirkungsintegral_pi_herleitung.md),
  RT-01 August 2026 — mit Falsifizierungsvorbehalt;
  konzeptuelle Grundlage: RT-01a → [theorie/pi_als_urkonstante.md](../../theorie/pi_als_urkonstante.md))
- ℏ das reduzierte Plancksche Wirkungsquantum
- f die RFT-Resonanzfrequenz der gekoppelten Mode, f = E/(π·ℏ) = ω/π (K-3)

> **E = π·ε·ℏ·f ist ein definierendes Postulat der RFT. Sie wird nicht aus
> den vorangehenden Integralen abgeleitet, sondern axiomatisch gesetzt.**

**Herleitung von π:** Die Kopplung zwischen zwei Resonatoren erfolgt
nicht instantan, sondern über einen Pfad im Phasenraum. Die Integration
der Kopplungseffizienz über einen vollständigen Halbzyklus ergibt:

```
        ∫₀^π cos²(φ/2) dφ = π/2

        Normiert auf die maximale Kopplung (Δφ = 0):
        E_eff / E_max = π · ε · ℏ · f / (ℏ · f) = π · ε
```

Der Faktor π entsteht somit aus der zyklischen Geometrie der Kopplung,
nicht als freier Parameter.

**Testbare Vorhersage:** Die Energieübertragung ist maximal bei
Phasengleichheit (ε = 1) und null bei Phasenorthogonalität (ε = 0).

**Physikalisches Beispiel:** Josephson-Kontakt — Energieübertragung
zwischen Supraleitern über phasenkohärente Kopplung.

**Empirischer Nachweis (RFT-intern):**
- **Schrödinger-Simulation** (→ [simulationen/schrödinger/README.md](../../simulationen/schrödinger/README.md)):
  5-stufige Ableitung der Schrödinger-Gleichung aus Axiom 4;
  Korrespondenzprinzip numerisch bewiesen — Fidelity = 1.000000000000
  für alle 4 Kopplungsszenarien (Δφ = π, 2π/3, π/2, 0);
  Störungstheorie bestätigt 1−F ~ λ² (Exponent 2.001, Abweichung 0,05%)
  und |Δ⟨x⟩| ~ λ¹ (Exponent 1.001); Standard-QM ist der exakte Grenzfall der RFT (λ → 0);
  Wirkungsprinzip S[ψ,Δφ] über Euler-Lagrange abgeleitet (Dichtemodell als effektiver Grenzfall);
  Gisin-Theorem: lokale Kopplungsstruktur bewahrt No-Signaling (konsistent mit ART);
  **falsifizierbare Vorhersage:** |Δ⟨x⟩| = 4,9·λ·ℓ ≈ 2,0·λ µm für ⁸⁷Rb-Atome.
- **Warpantrieb** (→ [konzepte/warpantrieb/warpantrieb.md](../../konzepte/warpantrieb/warpantrieb.md)):
  Phasensteuerung ε(Δφ) = cos²(Δφ/2) erzeugt Vorzeichenwechsel in der Zustandsgleichung —
  w(Δφ=0) = +0,034 (Kontraktion) → w(Δφ=π/2) = −0,024 (Expansion);
  **erste Warpblasensimulation mit rein positiver Energiedichte** (E⁻ = 0,
  bestätigt durch 3D-Integration); RFT-Signatur: ρ(Δφ) ∝ cos⁴(Δφ/2),
  ρ(0)/⟨ρ⟩ = 2,5806, κ = 1.
- **Resonanzreaktor** (→ [konzepte/resonanzreaktor/README.md](../../konzepte/resonanzreaktor/README.md)):
  λ_eff/λ₀ = 7.872 für U-235 bei perfekter Resonanz (Δφ=0, κ=1);
  **falsifizierbare Vorhersage:** σ_coh > σ_incoh.
- FLRW-Simulationen: ε = η Identität (κ = 1), 1.530 Läufe.

---

### Axiom 5 — Energierichtung

**Aussage:** Energie in einem Resonanzfeld ist keine skalare Größe,
sondern ein Vektor: Sie hat Betrag und Richtung im Feld.

**Formalisierung:**

```
(A5)    E⃗ = E_eff · ê(Δφ, ∇Φ)

        Die Richtung ê wird bestimmt durch:
        - den Phasengradienten ∇Φ des Resonanzfelds
        - die Phasendifferenz Δφ zwischen gekoppelten Moden
```

In einem diskreten Mehrskalensystem (z.B. Finanzmärkte) ergibt sich
der Energierichtungsvektor als Differenz der relativen Energien auf
verschiedenen Zeitskalen:

```
        energy_dir = e_short − e_long

        e_short = (Preis − MA_SHORT) / MA_SHORT
        e_long  = (Preis − MA_LONG)  / MA_LONG
```

**Testbare Vorhersage:** Die Richtung des Energieflusses ist eine
verwertbare Observable, die über skalare Indikatoren hinausgeht.

**Empirischer Nachweis (RFT-intern):** Resonanzfeld-Simulation: Energierichtungsvektor
(A5) bestätigt — PCI → MI zeigt direktionale Energieflusskontrolle.
FLRW-Simulation: Energiefluss-Direktion bestätigt in kosmologischem Kontext.
Warpantrieb (→ [konzepte/warpantrieb/warpantrieb.md](../../konzepte/warpantrieb/warpantrieb.md)):
Energierichtung bestimmt Kontraktion (vorn, w > 0) vs. Expansion (hinten, w < 0) —
Vorn-/Hinten-Asymmetrie als direkte Folge von A5.
Doppelpendel: ε(θ₂−θ₁) bestätigt direktionale Kopplung.

---

### Axiom 6 — Informationsfluss durch Resonanzkopplung

**Aussage:** Information wird ausschließlich durch kohärente Phasen- und
Frequenzrelationen übertragen. Die Qualität des Informationsflusses ist
messbar durch Mutual Information und Phase Coherence Index.

**Formalisierung:**

```
(A6)    MI(X, Y) = H(X) + H(Y) − H(X, Y)

        PCI = |⟨exp(i(φ₁ − φ₂))⟩| ∈ [0, 1]

        Informationsfluss I(X → Y) > 0  ⟺  PCI > 0 ∧ MI > 0
```

**Testbare Vorhersage:** Systeme ohne Phasenkohärenz (PCI ≈ 0) können
keine Information austauschen — unabhängig von der Amplitude der
Einzelschwingungen.

**Empirischer Nachweis (RFT-intern):** Resonanzfeld-Simulation: Informationsfluss
durch Kopplungseffizienz und PCI bestätigt. Monte-Carlo-Test: emp. p = 0
(Resonanz nur bei Resonanzbedingung, A3).

---

### Axiom 7 — Invarianz unter synchronen Transformationen

**Aussage:** Die Kopplungsstruktur des Resonanzfelds bleibt invariant
unter synchronen Transformationen der Gruppe G_sync.

**Formalisierung:**

```
(A7)    T ∈ G_sync:  T(fᵢ, φᵢ, t) = (λfᵢ, φᵢ + φ₀, at + b)

        Invarianzbedingungen:
        G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ))
        ε(Δφ_ij) = ε(T(φᵢ) − T(φⱼ))
```

**Gruppentheoretischer Beweis (RT-02, Aug 2026):** Die vier Gruppenaxiome für
G_sync ≅ ℝ⁺_× × U(1) × Aff⁺(ℝ) wurden algebraisch bewiesen. Die Invarianz
von G(fᵢ/fⱼ) unter der Frequenzskalierung und von ε(Δφ) unter Phasenverschiebungen
ist formal nachgewiesen. Die Domänenübertragung (CMB, Kernphysik, Finanzmärkte)
bleibt ein motiviertes Postulat. Die Funktion ε(Δφ) = cos²(Δφ/2) ist als
eindeutig ausgezeichnete Funktion der k=1-Darstellung von U(1) ⊂ G_sync
gruppentheoretisch erzwungen.

**Korollar A3 (RT-35, Aug 2026):** Die Darstellungsstruktur von A7 impliziert
A3: fᵢ/fⱼ ∈ ℚ ist eine Konsequenz von A7, kein unabhängiges Axiom.
Vollständiges Korollar: `de/fakten/theorie/gsync_gruppenstruktur.md` §5

Vollständiger Beweis: `de/fakten/theorie/gsync_gruppenstruktur.md` |
Symbolische Verifikation: `de/fakten/theorie/simulationen/rt02/rt02_gsync_verification.py`

**Testbare Vorhersage:** Die Resonanzstruktur ist skalierungsinvariant —
sie gilt auf allen Zeitskalen und Energieskalen.

**Empirischer Nachweis (RFT-intern):** Monte-Carlo-Test stabil über 3 KDE-Bandbreiten
und 30 Seeds (A7 bestätigt). FLRW-Simulation: Kopplungsstruktur invariant über
verschiedene H₀-Werte (4 Regime). CERN-Daten: stabiles Resonanzmuster.

---

## 4. Mathematische Konsequenzen

### 4.1 Geometrische Motivation des Faktors π in der Energieformel

Aus Axiom 1 (Schwingung) und Axiom 4 (Kopplungsenergie) folgt:

> *Die folgende Integration motiviert den Faktor π geometrisch, leitet ihn jedoch
> nicht zwingend ab. Eine vollständige Herleitung über ein Wirkungsintegral S[ψ, Δφ]
> ist eine offene Forschungsfrage (siehe RESEARCH_TASKS.md).*

Die Energieübertragung zwischen zwei resonant gekoppelten Moden
mit Kopplungseffizienz ε(Δφ) = cos²(Δφ/2) über einen vollständigen
Kopplungszyklus ist:

```
    E_zyklus = ℏ · f · ∫₀^(2π) cos²(φ/2) dφ / (2π)
             = ℏ · f · π / (2π)
             = ℏ · f / 2
```

Die effektive Kopplungsenergie für einen Halbzyklus (die minimale
Einheit kohärenter Übertragung) beträgt:

```
    E_eff = ℏ · f · ∫₀^π cos²(φ/2) dφ / π
          = ℏ · f · (π/2) / π
          = ℏ · f / 2
```

Normiert auf die Kopplungseinheit ergibt sich:

```
    E_eff = π · ε(Δφ) · ℏ · f
```

wobei der Faktor π die zyklische Geometrie des Kopplungspfads
kodiert und ε ∈ [0, 1] die effektive Kopplungsstärke.

### 4.2 Stabilität als Konsequenz (kein eigenes Axiom)

Aus A1 (Schwingung), A2 (Superposition) und A3 (Resonanzbedingung) folgt:

**Satz (Stabile Resonanzfelder):** Ein Feld Φ(x,t) ist genau dann stabil,
wenn seine Fourier-Komponenten ωₙ in rationalen Verhältnissen stehen:

```
    Φ_stabil(x, t) = Σₙ cₙ · exp(i(kₙx − ωₙt))
    mit ωₙ/ω₀ ∈ ℚ  für alle n
```

*Beweis:* Konstruktive Interferenz (stehende Wellen) erfordert periodische
Wiederkehr des Feldmusters. Dies ist nur bei rationalen Frequenzverhältnissen
gegeben (Satz von Weyl über Gleichverteilung).

**Anmerkung:** In der alten Version war dies Axiom 5. Es ist aber eine
Konsequenz der Axiome 1–3 und daher kein unabhängiges Axiom.

### 4.3 Kopplungsdynamik

Aus A3 (Resonanzbedingung) und A4 (Kopplungsenergie) folgt die
zeitliche Entwicklung der Kopplungsstärke:

```
    dK_ij/dt = α · G(fᵢ/fⱼ) · cos(Δφ_ij) − β · K_ij
```

(α: Anregungsrate, β: Dämpfungsrate)

### 4.4 Resonanzlandschaft und Attraktoren

Das effektive Potenzial der Kopplung:

```
    V(f) = −π · ε(Δφ(f)) · h · f
```

Lokale Minima von V entsprechen stabilen Resonanzen (Attraktoren).

### 4.5 Resonanz als Informationsselektion

Aus A6 (Informationsfluss) folgt, dass Resonanz als Bayesscher
Informationsfilter wirkt:

```
    P(ψ | Φ) ∝ P(Φ | ψ) · P(ψ)
```

Kohärente Zustände (hoher PCI) werden selektiv verstärkt.

---

## 5. Interpretative Erweiterungen

Die folgenden Aussagen sind **keine Axiome** der RFT, sondern
interpretative Ergänzungen, die auf dem axiomatischen Fundament aufbauen.

### 5.1 Beobachter als Resonator (E1)

Der Beobachter kann als gekoppelte Mode im Resonanzfeld modelliert werden.
Durch Resonanzkopplung (A6) prägt der Messprozess die Feldstruktur mit.

Dies ist konsistent mit der Quantenmechanik (Messproblem), wird hier aber
nicht als Axiom gesetzt, da es aus A1–A7 folgt: Ein Beobachter ist ein
System mit Eigenfrequenz (A1), das durch Resonanzkopplung (A3, A6)
Information mit dem Feld austauscht.

---

## 6. Übersicht: Axiome und ihre empirischen Tests

| Axiom | Kernaussage | Formale Kernformel | RFT-interner Nachweis |
|-------|-------------|-------------------|----------------------|
| A1 | Universelle Schwingung | ψ = A·cos(kx−ωt+φ) | FLRW-Simulationen: η ≈ cos²(Δφ/2), Δd_η > 6σ |
| A2 | Superposition | Φ = Σ ψᵢ | Gekoppelte Oszillatoren: Mehrfrequenz-Überlagerung simuliert |
| A3 | Resonanzbedingung | \|f₁/f₂ − m/n\| < δ | Monte-Carlo-Test: 5 Resonanzen bei Teilchenmasse, emp. p = 0 |
| A4 | Kopplungsenergie | E = π·ε·h·f | Schrödinger-Simulation: 5-stufige Ableitung aus A4, Fidelity = 1,0, 1−F ~ λ² bestätigt; Warpantrieb: erste Warpblase mit positiver Energiedichte via ε(Δφ)-Phasensteuerung; Resonanzreaktor: λ_eff/λ₀ = 7.872 (U-235); FLRW: ε = η Identität (κ = 1) |
| A5 | Energierichtung | E⃗ = E·ê(Δφ,∇Φ) | Resonanzfeld-Simulation: Energierichtungsvektor, Doppelpendel: ε(θ₂−θ₁); Warpantrieb: Vorn-/Hinten-Asymmetrie (Kontraktion vs. Expansion) |
| A6 | Informationsfluss | MI > 0 ⟺ PCI > 0 | Resonanzfeld-Simulation: Kopplungseffizienz und Energiefluss |
| A7 | Invarianz (G_sync) | G(fᵢ/fⱼ) = G(T(fᵢ)/T(fⱼ)) | Monte-Carlo-Test: bandbrei­tenunabhängig (3 KDE), CERN-Daten: stabiles Resonanzmuster |

---

## 7. Anwendungsfelder

- **Quantenphysik:** Superposition, Quantisierung durch rationale Frequenzverhältnisse
- **Klassische Mechanik:** Synchronisation gekoppelter Oszillatoren
- **Finanzmärkte:** Resonanzbasiertes Trading (ResoTrade — Anwendungskonzept)
- **Biophysik / Schwarmverhalten:** Resonanzbasierte Erklärung von Vogel- und Fischschwärmen — warum Schwarmlebewesen sich synchronisieren und wie sie durch Phasenkopplung im Medium extreme Wendigkeit erreichen. Siehe [Schwarmresonanz](../erklaerungen/schwarmresonanz.md).
- **Disziplinübergreifend:** Resonanz als verbindendes Muster durch alle Disziplinen der Physik — Mechanik, Thermodynamik, Elektrodynamik, Quantenmechanik, Relativität. Siehe [Resonanz in der Physik](../erklaerungen/resonanz_in_der_physik.md).
- **Informationstheorie:** Resonanzbasierte Kanalkapazität
- **Kosmologie:** Harmonische Musterbildung

---

## 8. Fazit

Die Resonanzfeldtheorie besteht aus 7 Kern-Axiomen (A1–A7), die:

1. **Minimal** sind: Das stabile Resonanzfeld (altes A5) ist als Satz ableitbar
2. **Unabhängig** sind: Kein Axiom folgt aus den übrigen
3. **Formal präzise** sind: Jedes Axiom enthält eine mathematische Formel
4. **Empirisch testbar** sind: Jedes Axiom hat einen dokumentierten Test (FLRW-Simulationen, Monte-Carlo, CERN-Daten, Resonanzreaktor)

Die Erweiterung E1 (Beobachter als Resonator) ist eine interpretative
Ergänzung, die auf dem Fundament aufbaut, aber nicht zur physikalischen
Axiomatik gehört.

---

© Dominic-René Schu — Resonanzfeldtheorie 2025/2026

---

[Zurück zur Übersicht](../../../README.md)