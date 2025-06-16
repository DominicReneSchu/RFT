# Begleitkapitel: Kompakter numerischer Beweis der Resonanzfeldtheorie

Dieses Kapitel erläutert die numerische Umsetzung und die physikalische Bedeutung der Resonanzfeldtheorie, wie sie im begleitenden Python-Code realisiert ist. Der Ansatz bietet eine kompakte, nachvollziehbare und visuell überprüfbare Bestätigung zentraler Aussagen der Resonanzfeldtheorie.

<p align="center">
  <img src="plot.png" alt="Visualisierung der Resonanzfeldtheorie" width="800"/>
</p>

---

[Link zur Python](resonanzfeld.py)

---

---

## 1. Theoretischer Hintergrund

Die **Resonanzfeldtheorie** beschäftigt sich mit der Beschreibung und Analyse von Resonanzphänomenen in komplexen Systemen. Im Fokus steht hierbei die explizite Abhängigkeit der Resonanzenergie von Systemparametern wie Amplitude (A) und Temperatur (T).
Die hier verwendete Formel für die **Resonanzenergie** lautet:

$$
E_\mathrm{res} = \frac{A}{1 + \left(\frac{\omega_\mathrm{ext} - \omega_0}{\gamma}\right)^2}
$$

mit:

- 𝐴: Amplitude
- 𝜔₀: Eigenfrequenz (Standard: 1.0)
- 𝛾: Dämpfungskonstante (Standard: 0.2)
- 𝜔_ext = 𝜔₀ · (1 + sin(T)): effektive Anregungsfrequenz, abhängig von T

Diese Beziehung beschreibt die Verstärkung der Energieaufnahme in einem Resonanzfeld in Abhängigkeit von den veränderlichen Parametern.

---

## 2. Numerische Umsetzung

### **a) Berechnung der Resonanzenergie**

Die Funktion `berechne_resonanzenergie` erzeugt aus den Wertebereichen für Amplitude (A) und Temperatur (T) ein Gitter und berechnet für jedes Gitterfeld die entsprechende Resonanzenergie (E_res). Werte ohne physikalischen Sinn, wie etwa A ≤ 0 oder T ≤ 0, werden dabei ausgeschlossen.

### **b) Resonanzentropie**

Als weiteres charakteristisches Feld wird die **Resonanzentropie** S berechnet:

$$
S = -E_\mathrm{res} \cdot \ln(E_\mathrm{res})
$$

Hiermit wird die Unordnung oder Diversität des Resonanzfeldes quantifiziert. Auch hier ist numerische Stabilität dadurch sichergestellt, dass E_res > 0 gilt.

---

## 3. Visualisierung

Die Funktion `plot_resonanzfeld` erzeugt zwei gekoppelte 3D-Visualisierungen:

- **Resonanzenergie** E_res über dem A-T-Parameterraum (Farbskala: "inferno")
- **Resonanzentropie** S über demselben Raum (Farbskala: "viridis")

Diese Plots bieten eine unmittelbare, intuitive Übersicht über die Struktur des Resonanzfeldes. Charakteristische Maxima, Plateaus und Bereiche minimaler oder maximaler Entropie werden auf einen Blick sichtbar.

---

## 4. Numerischer Beweis

Durch die Kombination aus analytischer Formel, Gitterberechnung und Visualisierung entsteht ein **kompakter numerischer Beweis** für die Gültigkeit der postulierten Resonanzstruktur. Die resultierenden Energie- und Entropiefelder liefern eine konsistente Bestätigung der theoretischen Vorhersagen für beliebige (physikalisch sinnvolle) Wertebereiche von $A$ und $T$.

---

## 5. Eingabebereiche und physikalische Plausibilität

Die Eingabewerte für A und T sind auf positive Werte normiert und können beliebig fein gewählt werden. Dies gewährleistet sowohl numerische Stabilität als auch physikalische Plausibilität der Ergebnisse.

---

## 6. Bedeutung und Ausblick

Die vorliegende Implementation bietet nicht nur eine konkrete Überprüfung der Resonanzfeldtheorie, sondern auch eine flexible Grundlage für die Erweiterung auf komplexere Systeme (zum Beispiel die Kopplung mehrerer Resonatoren, temperaturabhängige gamma-Werte usw.) oder die Anbindung an experimentelle Daten.

---

*© Dominic Schu, 2025 – Alle Rechte vorbehalten.*

---

⬅️ [zurück zur Übersicht](README.md)