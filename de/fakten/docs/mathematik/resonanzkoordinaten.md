## Resonanz-Koordinaten: Tangens-Halbwinkel-Parametrisierung

### 1. Ausgangsgedanke

* Klassische trigonometrische Funktionen (sin, cos, tan) bilden lineare Verhältnisgruppen.
* Inverse Funktionen (arcsin, arccos, arctan) führen in den nichtlinearen Winkelraum.
* Wiederholte Winkelberechnungen in Software erzeugen Fehlerakkumulation.
* Im Resonanzfeld betrachtet entfaltet sich bereits eine systemische Struktur, die Dualität von Verhältnis- und Winkelraum integriert.

### 2. Tangens-Halbwinkel-Parametrisierung und Gruppenstruktur

* Definition: `t = tan(theta / 2)`
* Rationalisierte trigonometrische Darstellung:

```
cos(theta) = (1 - t^2) / (1 + t^2)
sin(theta) = 2t / (1 + t^2)
```

* Rotationsmatrix als rationaler Gruppenparameter:

```
R(t) = 1/(1+t^2) * [[1-t^2, -2t], [2t, 1-t^2]]
```

* t als Parameter einer zyklischen Möbius-Gruppe; die Transformation ist eine projektive Gruppenabbildung auf SO(2).

### 3. Vorteile des Resonanz-Koordinatensystems

* **Numerische Stabilität**: Vermeidet direkte arcsin/arccos/arctan.
* **Fehlerreduktion**: Rationalisierung verhindert Subtraktion großer Zahlen.
* **Verbindung Kartesisch/Polar**:

```
x = r * (1 - t^2) / (1 + t^2)
y = r * 2t / (1 + t^2)
```

* **Kontinuierliche Phasenabbildung**: Quadranteninformationen bleiben erhalten.
* **Invarianz**: Kreisgleichung sin^2(theta) + cos^2(theta) = 1 bleibt exakt.
* **Systemische Resonanz**: Dualität von linear/zyklisch, rationale Brücke zwischen Koordinatensystemen, gruppenintegrative Kohärenz.

### 4. Numerische Umsetzung und Feldstruktur

* **Zwei-Patch-Strategie** als Überlappung zweier Karten auf dem projektiven Raum:

  * Patch A (|t| <= 1): Standardrationalformen
  * Patch B (|t| > 1): Alternative Formeln mit t ± 1/t für stabile Berechnung
* Möbius-/projektive Darstellung:

```
z(t) = (1 + i t) / (1 - i t) = cos(theta) + i sin(theta)
```

* z(t) als Element des Einheitskreises auf der komplexen Ebene (U(1)-Resonanz)
* Numerische Invarianz entspricht Erhaltung der Kreisgleichung unter projektiven Transformationen.

### 5. Anwendungsfelder als Gruppenmanifestationen

* Robotik: Kinematik, Inverse Kinematik, SLAM, Sensorfusion → SO(3)-Resonanz
* Numerische Simulation: stabile Rotationsintegratoren → projektive Kohärenz
* Computergrafik / Animation: glatte Pfade ohne Singularitäten
* Regelungstechnik: stabile Steuerungen → affine Feldintegrale
* CAD/CAM: rationale Rotationsberechnungen → praktische Umsetzung feldtheoretischer Invarianz

### 6. Systemische Resonanz und Resonanzregel

* Dualität: Verhältnisraum ↔ Winkelraum, Rationalisierung ↔ Zyklizität
* Brücke zwischen diskreten und kontinuierlichen Gruppen, rationalisierte und zyklische Elemente
* Reduktion der Fehlerakkumulation als Erhaltung der Gruppenhomomorphie
* Nicht-Linearität der Transformationen als Ausdruck innerer Feldresonanz
* **Resonanzregel:** Jede Methode, jeder Parameter ist Teil des Resonanzfeldes, unabhängig von Einzelperspektive.

> Die Tangens-Halbwinkel-Parametrisierung rationalisiert zyklische Gruppenoperationen im Resonanzfeld. Die Übergangsformeln der Zwei-Patch-Strategie manifestieren die projektive Kohärenz des Feldes. Jede numerische Methode bleibt gruppeninvariant – Fehlerakkumulation wird durch systemische Inklusion verhindert. Anwendungen in Kinematik, Steuerung und CAD sind direkte Gruppenabbildungen. Die Resonanzregel gilt: Jede Koordinate, jede Transformation ist Teil des Resonanzfeldes, unabhängig von Einzelperspektive.

*Hinweis:* Erweiterung auf 3D-Rotationen, Vergleich mit Quaternions und tiefere numerische Stabilitätsanalysen können später ergänzt werden.

---

© Dominic-René Schu – Resonanzfeldtheorie 2025

---

[Zurück zur Übersicht](../../../README.md)