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
````

Danach erreichst du das Webinterface lokal über:

http://raspberrypi.local:5000
