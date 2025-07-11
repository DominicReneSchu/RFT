# ResoNet – Das dezentrale Resonanzfeld-Netzwerk

> Dein Raspy. Deine Meinung. Unser Resonanzfeld.

**ResoNet** ist ein P2P-Netzwerk, das jedem Menschen die Möglichkeit gibt, seine Sichtweise zu gesellschaftlichen, politischen oder philosophischen Themen **dezentral**, **verifizierbar** und **manipulationssicher** zu hinterlegen – mit einem einzigen Gerät: einem Raspberry Pi.

---

## 🎯 Zielsetzung

ResoNet möchte zentrale Abhängigkeiten überwinden und individuelle Beiträge zu einem kollektiven Resonanzfeld verbinden. Es geht nicht um Likes, Reichweite oder Kontrolle – sondern um Wahrheit, Struktur und Verantwortung im offenen Diskursraum.

- 🌐 *Keine zentrale Plattform*
- 🔐 *Fälschungssichere Inhalte durch Signaturen*
- 🧠 *Konsensabfrage via KI*
- 🌱 *Emergentes Feld statt Meinungsdiktat*

---

## 🧱 Funktionsweise

Jeder Raspy-Knoten:
- enthält die **Meinung seines Besitzers** (lokal speicherbar)
- **synchronisiert sich mit anderen Raspys** im Netzwerk
- **verifiziert** neu empfangene Inhalte durch Signaturprüfung
- speichert eine vollständige, verifizierte Kopie des gesamten Resonanzfelds

---

## ⚙️ Installation (Raspberry Pi)

### Voraussetzungen:
- Raspberry Pi (empfohlen: 4 oder 5)
- Raspberry Pi OS (Lite oder Desktop)
- Internetzugang
- SSH (optional)

### Setup:
```bash
git clone https://github.com/DominicReneSchu/resonet.git
cd resonet/setup
chmod +x install.sh
./install.sh
```

Danach erreichst du das Webinterface lokal über:

http://raspberrypi.local:5000

---

## 🌐 Architekturüberblick

- **main.py**: Einstiegspunkt, orchestriert Laden, Signatur, Sync, Speicherung.
- **storage.py**: Meinungsverwaltung, automatisches Backup & Versionierung.
- **sync.py**: Netzwerk-Synchronisation (P2P-ready, HTTP-Stub).
- **verify.py**: Kryptografische Signaturen für Authentizität.
- **web.py**: Web-UI, Eintragen & Anzeigen von Meinungen, Konsensanzeige.
- **viz_network.py**: Visualisierung der Feldstruktur und Themencluster.
- **consensus_extract.py**: GPT-kompatibler Export des Feldkonsenses.
- **generate_keys.py**: RSA-Keypair-Generator für Identität & Verifikation.
- **install.sh**: Setup-Skript inkl. Keygen, Abhängigkeitsinstallation.
- **config.json**: Knotenkonfiguration (Name, Port, Topics, Peers).

---

## 🚀 Schnellstart

```bash
cd de/ResoNet
bash setup/install.sh
python3 generate_keys.py
python3 node/main.py
python3 ui/web.py
```

Öffne [http://localhost:5000](http://localhost:5000) für das lokale Resonanzfeld.

---

## 🖥️ Web-UI (Feldportal)

- **Meinung eintragen:** Direkt im Browser, Thema auswählen, Text eingeben.
- **Meinungen im Feld:** Tabellarische Übersicht aller Stimmen, sortiert nach Zeit.
- **Konsensanzeige:** Für jedes Thema wird der aktuelle Feld-Konsens als Liste angezeigt.
- **Themenfilter:** Auswahlfeld zur gezielten Ansicht/Eingabe je Topic.
- **Sync-Button:** Synchronisation mit Peers (Platzhalter, P2P-ready).

![Web-UI Screenshot](docs/resonet_webui_screenshot.png)

---

## 📊 Konsens-Export

Nutze `consensus_extract.py`, um den aktuellen Konsens pro Thema als JSON zu exportieren (GPT-kompatibel):

```bash
python3 tools/consensus_extract.py
cat data/consensus_export.json
```

---

## 🔑 Schlüsselverwaltung

Jeder Knoten generiert lokal ein RSA-Schlüsselpaar (private.pem, public.pem) per:

```bash
python3 generate_keys.py
```

Die öffentliche Identität kann optional in `config.json` veröffentlicht werden.

---

## 🛠️ Backup & Logging

- **Backups:** Jede Änderung an opinions.json erzeugt ein zeitgestempeltes Backup unter `data/backups/`.
- **Logging:** Aktionen & Fehler werden in `data/resonanznet.log` protokolliert.

---

## 🤝 Mitwirkende

- Systemischer Hauptentwickler: Dominic-René Schu

---

## 📨 Kontakt & Erweiterung

- Issues & Feedback: [GitHub Issues](https://github.com/DominicReneSchu/public)
- Vorschläge für Feld-Features und Erweiterungen sind ausdrücklich erwünscht.

---

**Resonanzregel:**  
Gruppenzugehörigkeit ist systemisch invariant und umfasst alle Mitglieder unabhängig von Nennung oder Sichtweise.