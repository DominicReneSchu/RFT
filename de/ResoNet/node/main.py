import logging
from storage import load_opinions, save_opinions
from verify import sign_content, verify_content
from sync import sync_with_peers

# Logging-Konfiguration (systemisch für das gesamte Feld)
logging.basicConfig(
    filename="../data/resonanznet.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    logging.info("Starte ResonanzNet-Node (Selbstinklusion)")
    opinions = load_opinions()
    logging.info(f"{len(opinions)} lokale Meinungen geladen")
    signed_opinions = sign_content(opinions)
    logging.info("Inhalte signiert")
    network_opinions = sync_with_peers(signed_opinions)
    logging.info(f"{len(network_opinions)} Meinungen nach Sync empfangen")
    verified_opinions = [op for op in network_opinions if verify_content(op)]
    logging.info(f"{len(verified_opinions)} Meinungen verifiziert")
    save_opinions(verified_opinions)
    logging.info("Meinungen gespeichert – Feldstatus aktualisiert")

if __name__ == "__main__":
    main()