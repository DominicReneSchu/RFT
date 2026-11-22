# RT-45 AP1 — Skalarität der Energie: Zulässigkeit und Grenzen

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Systematisch prüfen, wo die Standardphysik Energie als Skalar behandelt
und wo diese Behandlung unzulässig ist.

**Ergebnis:** Die skalare Behandlung von E ist in homogenen, nicht-gradienten-reichen
Systemen eine exzellente Näherung. Sie versagt strukturell in der Kosmologie
(kosmologische Konstante), in der ART (rahmenabhängiges T^00) und in Warp-Metriken.

---

## 2. Katalog: Energie als Skalar in der Standardphysik

| Kontext | Behandlung | Exakt oder Näherung? |
|---------|-----------|----------------------|
| Newtonsche Mechanik E = ½mv² + V | Skalar | Näherung (nicht-relativistisch, keine Rotation) |
| Thermodynamik dU = δQ − δW | Skalar | Exakt im thermodynamischen Gleichgewicht |
| Elektrostatik U = qΦ | Skalar | Näherung (statisches Feld, keine Strahlung) |
| QM: H|ψ⟩ = E|ψ⟩ | Skalar (Eigenwert) | Exakt in nicht-relativistischer QM |
| Kosmologie: ρ_Λ = const | Skalar (homogen) | ⚠️ Fraglich (s. Abschnitt 4) |
| ART: T^μν | Tensor (nicht Skalar) | Exakt — E = T^00 ist rahmenabhängig |

---

## 3. Kontexte, in denen Energie notwendig gerichtet ist

### 3.1 Poynting-Vektor

```
S⃗ = E⃗ × B⃗  [W/m²]
```

Der elektromagnetische Energiefluss ist ein Vektor — Energie fließt in eine Richtung.
Skalarität würde keine Richtungsinformation liefern.

### 3.2 Leistung als Skalarprodukt

```
P = F⃗ · v⃗ = |F||v|cos(θ)
```

Energie pro Zeit = Skalarprodukt zweier Vektoren. Die Richtungsinformation wird
durch die Projektion (cos θ) komprimiert — aber sie ist physikalisch vorhanden.

### 3.3 Lorentz-Vierervektoren

```
p^μ = (E/c, p⃗)
```

E ist die 0-Komponente eines Vierervektors — keine eigenständige skalare Größe.
Unter Lorentz-Transformationen mischen sich E und p⃗.

### 3.4 Energie-Impuls-Tensor T^μν

```
T^00 = ρ (Energiedichte)
T^0i = S^i/c (Energiefluss = Poynting)
T^ij = Maxwell-Spannungstensor
```

T^00 ist **rahmenabhängig** — in einem anderen Inertialsystem ist T'^00 ≠ T^00.
Energie ist in der ART **kein Lorentz-Skalar**.

---

## 4. Das Skalaritätspostulat

**Formulierung:** Energie E ist unter den folgenden Bedingungen (näherungsweise) skalar:

1. Kein dominanter Energiefluss (S⃗ ≈ 0 im Mittel)
2. Homogene Energieverteilung (∇ρ ≈ 0)
3. Nicht-relativistisches System (v ≪ c)
4. Kein ausgeprägter Gradienten-Term (∇Φ ≈ 0)

**Konsequenz:** In der Kosmologie sind Bedingungen 1 und 2 nur auf sehr großen Skalen
(Homogenitätsskala > 100 Mpc) näherungsweise erfüllt — und für die kosmologische
Konstante ρ_Λ werden sie unreflektiert auf Quantenskalen extrapoliert.

---

## 5. Strukturelle Lücke der skalaren Behandlung

**Kosmologisches Konstantenproblem (Vorschau auf AP3):**

Die Quantenfeldtheorie sagt ρ_Λ^QFT ~ 10⁹⁶ kg/m³ vorher.
Beobachtet: ρ_Λ^obs ~ 10⁻²⁶ kg/m³.
Differenz: ~122 Größenordnungen.

**RFT-Deutung:** Eine homogene Energiedichte (∇ρ = 0) hat in der RFT keine
physikalische Wirkung — weil A5 besagt, dass Energie nur durch Gradienten
(∇Δφ) physikalisch wirksam wird. Die 122-Größenordnungen-Diskrepanz ist
kein Feinabstimmungsproblem, sondern ein Artefakt der skalaren Behandlung.

---

## 6. Ergebnis

**Skalarität ist zulässig:** Homogene, nicht-relativistische, gradientenfreie Systeme.

**Skalarität versagt strukturell:** Lorentz-Transformationen (p^μ), ART (T^μν
rahmenabhängig), Kosmologie (ρ_Λ-Problem), Warp-Metriken (ρ < 0 in Alcubierre).

**Erfolgskriterium:** ✅ Erfüllt — systematische Übersicht erstellt.

---

*RT-45 AP1 — DominicReneSchu/RFT — November 2026*
