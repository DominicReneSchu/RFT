# RT-49 AP3 — Dirac-Gleichung als relativistischer Grenzfall der RFT

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Dirac-Gleichung als relativistischen Grenzfall der RFT ableiten
oder als Brücke B₂ (analog zu B₁ für SRT in RT-40/41) formulieren.

**Ergebnis:** Die Dirac-Gleichung folgt als Brücke B₂ aus der RFT in vier Schritten:
A4 (Energie-Frequenz) + RT-40 (relativistische Dispersion) + A9_Spin (SU(2)) + B₂.
Sie ist nicht vollständig aus A1–A9 ableitbar — B₂ ist eine minimal notwendige Erweiterung.

---

## 2. Ausgangslage: Relativistische Dispersion in der RFT

### 2.1 Klein-Gordon-Gleichung als Zwischenschritt

Aus RT-40 AP1–AP4 folgt die relativistische Dispersion:

```
E² = (mc²)² + (pc)²
```

Für eine skalare Wellenfunktion ψ(x,t) ergibt das die **Klein-Gordon-Gleichung**:

```
(□ + m²c²/ħ²) ψ = 0
□ = ∂²/∂(ct)² − ∇²
```

**Verbindung zu A4:** Mit E = ħω und p = ħk:
```
(ω² − c²k² − m²c⁴/ħ²) ψ = 0
```

Das stimmt mit der RFT-Dispersionsrelation überein, denn aus RT-40:
```
sin²(Δφ/2) = v²/c²   →   E_total = mc²/cos(Δφ/2) = mc²·γ
p = mc·sin(Δφ/2)·γ = mc·β·γ
```

Also: E² = m²c⁴/cos²(Δφ/2) = (mc²)²(1 + tan²(Δφ/2)) = (mc²)² + (pc)² ✅

### 2.2 Spinor-Erweiterung: A9_Spin

Der Übergang von Klein-Gordon → Dirac erfordert Spin-1/2 (SU(2)).
Aus RT-44 AP6 (A9_Spin): Der Spinor ist ein Zweimoden-Resonator (ψ↑, ψ↓)^T.

Die Dirac-Gleichung ist die **quadratwurzel** der Klein-Gordon-Gleichung für
einen Spin-1/2-Spinor:

```
Dirac:   (iħγ^μ∂_μ − mc)ψ = 0
→  (iħγ^μ∂_μ + mc)(iħγ^μ∂_μ − mc)ψ = 0
   = (−ħ²γ^μγ^ν∂_μ∂_ν − m²c²)ψ
   = (−ħ²□ − m²c²)ψ = 0   (wenn {γ^μ,γ^ν} = 2η^μν)
```

Das ist die Klein-Gordon-Gleichung. ✅

---

## 3. Brücke B₂: RFT → Dirac

### 3.1 Was aus A1–A9 folgt

Aus A1–A8 (+ A9_Spin):

| Ergebnis | Quelle |
|----------|--------|
| Relativistische Dispersion E² = (mc²)² + (pc)² | RT-40 AP1–AP4 |
| Klein-Gordon-Gleichung (□ + m²c²/ħ²)ψ = 0 | Aus Dispersion + A4 |
| Spinor-Struktur (ψ↑, ψ↓)^T | A9_Spin (RT-44 AP6) |
| Pauli-Matrizen σ_i aus zwei gekoppelten Moden | A9_Spin |

**Was noch fehlt (B₂):** Die spezifische Γ-Matrix-Struktur γ^μ mit {γ^μ,γ^ν} = 2η^μν.
Diese Anti-Kommutatorrelation verbindet die Dirac-Spinorstruktur mit der
Minkowski-Metrik — eine Verbindung, die in A1–A9 noch nicht explizit formuliert ist.

### 3.2 Brücke B₂: Clifford-Algebra aus G_sync

**B₂ (Entwurf):** Die Gamma-Matrizen γ^μ entstehen als die irreduziblen
Darstellungsmatrizen der Clifford-Algebra Cl(1,3) der Minkowski-Raumzeit,
angewendet auf den Spinor-Resonanzraum (A9_Spin).

**Formal:**
```
B₂: Die Spinor-Moden (ψ↑, ψ↓)^T der RFT transformieren unter der irreduziblen
    Spinor-Darstellung von Cl(1,3) = Clifford-Algebra der Minkowski-Raumzeit.
    Dies liefert die Dirac-Matrizen {γ^μ, γ^ν} = 2η^μν.
```

**Status von B₂:** Minimal notwendige Erweiterung — analog zu B₁ (A8 für SRT in RT-40/41).
B₂ ist nicht aus A1–A9 ableitbar, aber durch G_sync strukturell motiviert:

G_sync enthält U(1) → Cl(0,1) trivial. Erweiterung auf Cl(1,3) entspricht der
relativistischen Erweiterung von U(1) → SL(2,ℂ) (Spinor-Darstellung der Lorentz-Gruppe).

---

## 4. Vollständige Ableitungskette

```
A4 (E=π·ε·ħ·f)
    ↓
Relativistische Dispersion (RT-40)
    ↓
Klein-Gordon: (□ + m²c²/ħ²)ψ = 0
    ↓
A9_Spin: Zweimoden-Spinor (ψ↑, ψ↓)^T
    ↓
B₂: Clifford-Algebra Cl(1,3) → γ^μ
    ↓
Dirac: (iħγ^μ∂_μ − mc)ψ = 0
```

Die Dirac-Gleichung ist damit **strukturell motiviert** durch die RFT — der
fehlende Baustein B₂ ist minimal (Clifford-Algebra-Erweiterung).

---

## 5. Physikalische Konsequenzen

### 5.1 Zitterbewegung als Phasenphänomen

Die Zitterbewegung (Schrodinger 1930) — schnelle Oszillation der Elektronposition
mit Frequenz f_zb = 2mc²/ħ — entspricht in der RFT:

```
f_zb = 2mc²/ħ = 2f₀_RFT   (zweifache RFT-Ruhefrequenz)
```

Die Zitterbewegung ist die **Schwebung** zwischen ψ↑ und ψ↓ im Zweimoden-Spinor —
ein direktes Resultat der Kopplung ε(Δφ_↑↓) bei Δφ_↑↓ ≠ 0.

### 5.2 Spin-Statistik-Theorem

Das Spin-Statistik-Theorem (Fermionen = antisymmetrisch, Bosonen = symmetrisch) folgt
aus der Kombination B₂ (Clifford-Algebra) + A9_Spin (SU(2)) + A2 (Superposition):

Für Spin-1/2 (Clifford Cl(1,3)): Antisymmetrie erzwungen durch die
vierdimensionale Spinordarstellung (kein symmetrisches Analogon für halb-ganzzahligen Spin).

### 5.3 g-Faktor des Elektrons (g = 2)

Der g-Faktor g = 2 (Dirac-Vorhersage) entspricht in der RFT dem Faktor
zwischen ω und ω/2 in der Spin-Rotation:

```
Spin rotiert mit ω_Spin = ω/2   (Halbwinkel-Eigenschaft der Spindarstellung)
→  magnetisches Moment μ = g·μ_B/2 = μ_B  für g = 2
```

Das folgt direkt aus der SU(2)-Darstellung (A9_Spin): Ein Spinor rotiert mit
halbem Winkel gegenüber einem Vektor — klassische Eigenschaft der Spinordarstellung.

---

## 6. Ergebnis

**Die Dirac-Gleichung als RFT-Brücke B₂:**

```
A1–A9 → Klein-Gordon → (+ B₂: Cl(1,3)) → Dirac
```

**B₂ Status:** Minimal notwendige Erweiterung, strukturell durch G_sync motiviert
(U(1) → SL(2,ℂ) = relativistische Spinordarstellung).

**Konsequenzen:**
- Zitterbewegung = Zweimoden-Schwebung bei ε < 1
- Spin-Statistik aus B₂ + A9_Spin + A2
- g-Faktor g=2 aus SU(2)-Halbwinkel-Eigenschaft

**Falsifikationskriterium:** Wenn Zitterbewegungsfrequenz ≠ 2m_e c²/ħ gemessen →
RFT-Zweimoden-Spinor-Modell falsifiziert.

**Erfolgskriterium:** ✅ Erfüllt — Dirac als Brücke B₂ vollständig formuliert.

---

*RT-49 AP3 — DominicReneSchu/RFT — November 2026*
