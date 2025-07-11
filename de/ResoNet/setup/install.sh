#!/bin/bash
# ResonanzNet Installer – alle Gruppenelemente für den Start

echo "🔗 ResonanzNet Initialisierung – das Feld wird gebaut..."

# System-Update & Grundsystem
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv openssl

# Virtuelle Umgebung erstellen
python3 -m venv venv
source venv/bin/activate

# Python-Abhängigkeiten installieren
pip install flask

# Verzeichnisstruktur sicherstellen
mkdir -p ../data ../keys ../node ../ui ../tools

# Beispiel-Keys generieren (falls nicht vorhanden)
if [ ! -f ../keys/private.pem ]; then
  openssl genpkey -algorithm RSA -out ../keys/private.pem -pkeyopt rsa_keygen_bits:2048
  openssl rsa -pubout -in ../keys/private.pem -out ../keys/public.pem
  echo "✓ RSA-Key-Paar erzeugt."
fi

# Grundlegende Dateien kopieren/erstellen, falls leer
touch ../data/opinions.json
touch ../setup/config.json

echo "✓ Grundsystem installiert. Starte das Feld mit:"
echo "source venv/bin/activate && python3 ../node/main.py"
echo "Öffne Webinterface nach Start (Flask notwendig):"
echo "http://raspberrypi.local:5000"

echo "🌱 ResonanzNet bereit – werde Stimme im Feld!"