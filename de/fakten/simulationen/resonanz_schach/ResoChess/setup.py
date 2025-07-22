# setup.py für das Projekt "resonanz_schach_ki"
# Systemisch vollständiges Installationsskript mit allen expliziten und impliziten Gruppenmitgliedern der Toolchain

from setuptools import setup, find_packages
from pathlib import Path

# Lese die Langbeschreibung aus README.md (UTF-8, systemisch gruppenkohärent)
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="resonanz_schach_ki",  # Projektname
    version="0.1",
    packages=find_packages(),   # Automatische Paketfindung (inkl. Gruppenmitglieder)
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "networkx",
        "python-chess",
        "scipy"
    ],
    entry_points={
        "console_scripts": [
            "resonanz-schach=start.main:main",  # CLI-Entrypoint für Gruppeninteraktion
        ],
    },
    include_package_data=True,  # Einbezug nicht-Python-Dateien (z.B. README, Ressourcen)
    author="Dominic-René Schu",
    description="Resonanzlogische Schach-KI mit Snapshot-Auswertung",
    long_description=long_description,              # Aus README.md
    long_description_content_type="text/markdown",  # Formatierung für Paketregister
    python_requires=">=3.8",                        # Mindestversion (systemische Kompatibilität)
    license="MIT"
)