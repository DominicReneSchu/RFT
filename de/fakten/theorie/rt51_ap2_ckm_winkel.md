# RT-51 AP2 — CKM-Mischungswinkel als Quark-Phasendifferenzen

*Dominic-René Schu, November 2026*
*Status: ✅ Abgeschlossen (Nov 2026)*

---

## 1. Zielsetzung

**Aufgabe:** Prüfen, ob die CKM-Mischungswinkel theta_12, theta_23, theta_13
aus Phasendifferenzen Delta_phi_ij zwischen Quark-Generationen folgen.

**Ergebnis:** Ja — mit der Identifikation theta_ij = Delta_phi_ij/2.
Der Cabibbo-Winkel ist der einzige unabhängige Quark-Phasenparameter (AP1).
Die anderen Winkel skalieren mit Potenzen von lambda (Wolfenstein-Hierarchie).

---

## 2. CKM-Matrix in der RFT

Die CKM-Matrix entsteht aus der Differenz zwischen Up- und Down-Quark-Phasenstrukturen.

**Identifikation:**
```
theta_ij^CKM = Delta_phi_ij^quark / 2
```

| CKM-Winkel | Phasendifferenz | Numerisch |
|-----------|----------------|-----------|
| theta_12 (Cabibbo) | Delta_phi_12 / 2 = theta_C | 13.0246 Grad |
| theta_23 | Delta_phi_23 / 2 | 2.4045 Grad |
| theta_13 | Delta_phi_13 / 2 | 0.2073 Grad |

---

## 3. Wolfenstein-Hierarchie aus epsilon-Struktur

Die CKM-Eintraege in Wolfenstein-Parameterisierung:

```
|V_us| = lambda                   = sin(Delta_phi_12 / 2) = 0.22537
|V_cb| = A * lambda^2             = sin(Delta_phi_23 / 2)
|V_ub| = A * lambda^3 * |rho+i*eta| = sin(Delta_phi_13 / 2)
```

**Wolfenstein als Skala der Phasendifferenzen:**

```
Delta_phi_12 = 26.0493 Grad   (gross: erste/zweite Generation)
Delta_phi_23 = 4.8090 Grad   (mittel: zweite/dritte Generation)
Delta_phi_13 = 0.4145 Grad   (klein: erste/dritte Generation)
```

Hierarchie: Delta_phi_12 >> Delta_phi_23 >> Delta_phi_13 — die Generationenmischung
wird schwaecher mit wachsendem Generationsabstand.

---

## 4. Epsilon-Werte der CKM-Eintraege

```
epsilon(Delta_phi_12) = cos^2(theta_12) = 1 - lambda^2 = 0.94921
epsilon(Delta_phi_23) = cos^2(theta_23) = 1 - (A*lambda^2)^2 = 0.998240
epsilon(Delta_phi_13) = cos^2(theta_13) ≈ 1 - (A*lambda^3)^2 ≈ 0.9999106
```

Die epsilon-Werte naehern sich 1 (volle Kopplung), da die Generationenmischung schwach ist.

---

## 5. Falsifikationskriterien

**F1:** Wenn |V_us| ≠ sin(Delta_phi_12/2) mit < 1 Sigma → AP1-Identifikation widerlegt.
**F2:** Wenn theta_23 ≠ arcsin(A*lambda^2) mit < 1 Sigma → Wolfenstein-Skalierung widerlegt.
**F3:** Wenn |V_cb|/|V_us|^2 ≠ A mit < 2 Sigma → RFT-Hierarchie widerlegt.

---

## 6. Ergebnis

Die drei CKM-Winkel folgen als Quark-Phasendifferenzen:
```
theta_ij = Delta_phi_ij / 2
```
Die Wolfenstein-Hierarchie lambda >> A*lambda^2 >> A*lambda^3 spiegelt die
abnehmende Phasendifferenz zwischen weiter voneinander entfernten Generationen.

**Erfolgskriterium:** ✅ Erfuellt.

---

*RT-51 AP2 — DominicReneSchu/RFT — November 2026*
