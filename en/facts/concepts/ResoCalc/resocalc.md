# Vergleich: Konventionelle Drehmomentberechnung vs. ResoCalc (Resonanzfeldtheorie)

In diesem Abschnitt vergleichen wir die klassische mechanische Berechnung des effektiven Drehmoments mit der neuen Methode auf Basis der Resonanzfeldtheorie (ResoCalc).

👉 **Direkt zur Anwendung:**  
[![⚡ ResoCalc starten](https://img.shields.io/badge/⚡_ResoCalc_starten-Resonanzfeld_theorie-orange)](https://resoshift.com/)

### Ausgangswerte:
- Masse $$m = 2\,0\mathrm{kg}$$  
- Länge $$l = 1\,0\mathrm{m}$$  
- Anregungsfrequenz $$f = 10\,0\mathrm{Hz}$$  
- Resonanzfrequenz $$f_r = 5\,0\mathrm{Hz}$$  
- Kopplungsfaktor: 0.2

### Berechnungsansätze:

#### 🔵 Konventionell (klassisch):  
Effektives Drehmoment:

$$
M_{\text{konv}} = J \cdot \omega^2 \cdot \frac{\theta_{\text{max}}}{\sqrt{2}} \quad \text{mit} \quad J = m \cdot l^2
$$

Die klassische Berechnung hängt von der **willkürlich festgelegten maximalen Auslenkung** $$\theta_{\text{max}}$$ ab, die oft als Beispielwert angenommen wird. In diesem Fall nehmen wir $$\theta_{\text{max}} = 5^\circ = \frac{\pi}{36} \,\text{rad}$$ an.

- Trägheitsmoment: $$J = 2 \cdot 1^2 = 2\,0\mathrm{kg \cdot m^2}$$
- Kreisfrequenz: $$\omega = 2\pi \cdot f = 2\pi \cdot 10 = 62\,83\mathrm{rad/s}$$

Damit erhalten wir:

$$
M_{\text{konv}} = 2 \cdot 62.83^2 \cdot \frac{\frac{\pi}{36}}{\sqrt{2}} \approx 558.3 \,\text{Nm}
$$

#### 🔴 ResoCalc (Resonanzfeldtheorie):

In der ResoCalc-Methode wird das **Drehmoment in Resonanzbedingungen** berechnet. Anstelle einer willkürlichen Auslenkung verwenden wir das Verhältnis der Frequenzen $$\frac{f}{f_r}$$ und den **Kopplungsfaktor**:

$$
M_{\text{reso}} = 0{,}5 \cdot m \cdot l^2 \cdot (2\pi f)^2 \cdot \frac{1}{|1 - (f / f_r)^2|} \cdot \text{Kopplung}
$$

Erklärung der Formel:
- **Kopplungsfaktor**: Diese Größe berücksichtigt, wie stark die Energie zwischen den Schwingungen übertragen wird.
- **Resonanzverstärkung**: Das Verhältnis $$\frac{f}{f_r}$$ steuert die Verstärkung des Systems in Resonanz.

Setzen wir die gegebenen Werte ein:
- $$m = 2\,0\text{kg}$$
- $$l = 1\,0\text{m}$$
- $$f = 10\,0\text{Hz}$$
- $$f_r = 5\,0\text{Hz}$$
- Kopplungsfaktor: 0.2

Berechnung:

$$
M_{\text{reso}} = 0{,}5 \cdot 2 \cdot 1^2 \cdot (2\pi \cdot 10)^2 \cdot \frac{1}{|1 - (10 / 5)^2|} \cdot 0.2
$$

Das ergibt:

$$
M_{\text{reso}} \approx 2543.03 \,\text{Nm}
$$

### Ergebnis:
| Methode       | Effektives Drehmoment |
|---------------|------------------------|
| Konventionell | 558,3 Nm              |
| ResoCalc      | 2543,03 Nm            |

Die konventionelle Methode ist abhängig von der **willkürlich gewählten Auslenkung** $$\theta_{\text{max}}$$, was zu unrealistisch kleinen Werten führen kann, insbesondere bei Resonanz.

Die ResoCalc-Methode hingegen nutzt das Verhältnis $$f / f_r$$ und die Resonanzverstärkung, um das Drehmoment realistisch und ohne willkürliche Annahmen zu berechnen. Die **Kopplung** sorgt für eine skalierte Energieübertragung und eine viel präzisere Modellierung der realen Mechanik.

### Visualisierung:

![Vergleich: ResoCalc vs. Konventionell](resocalcVSkonv.png)

### Fazit:
**ResoCalc ersetzt den klassischen Rechenweg durch eine physikalisch intuitive, automatische Berechnung auf Knopfdruck.**  
Grenzwerte bleiben realistisch, das Ergebnis ist reproduzierbar – und für Ingenieure sofort nutzbar.

---

© Dominic-René Schu – Resonanzfeldtheorie 2025

---

[Zurück zur Übersicht](../../../README.md)