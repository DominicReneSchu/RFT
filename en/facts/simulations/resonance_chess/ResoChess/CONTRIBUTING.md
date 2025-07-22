### 🧠 GitHub Copilot Instruction: Snapshot-Mechanismus zur Erfahrungssicherung

**Ziel:**  
Implementiere eine automatische Snapshot-Sicherung des Erfahrungsspeichers `experience_weighted.csv` nach jeweils `SNAPSHOT_INTERVAL` abgeschlossenen Spielen (Standard: 100). Die Snapshots sollen fortlaufend durchnummeriert im Verzeichnis `./snapshots/` gespeichert werden.

---

#### ✴️ Bestandteile (bereits im Code enthalten, ggf. optimierbar):

1. **Konstanten & Zähler:**

   ```python
   SNAPSHOT_INTERVAL = 100
   games_played = 0
   ```

2. **Snapshot-Erstellung:**

   ```python
   def create_experience_snapshot():
       ...
       shutil.copy2(src, dst)
   ```

3. **Nummerierungslogik & Verzeichnis:**

   ```python
   def get_next_snapshot_number():
       ...
   ```

4. **Trigger-Logik nach jedem Spiel:**

   ```python
   if games_played % SNAPSHOT_INTERVAL == 0:
       create_experience_snapshot()
   ```

---

#### ✅ Copilot TODO (optional zur Erweiterung oder Optimierung):

* [ ] Parameter `snapshot_interval` optional über UI wählbar machen
* [ ] Snapshots mit Zeitstempel ergänzen (z. B. `..._0001_20250721.csv`)
* [ ] Snapshots als `gzip` komprimieren (für große Datenmengen)
* [ ] Snapshot-Wiederherstellung als Menüfunktion implementieren

---