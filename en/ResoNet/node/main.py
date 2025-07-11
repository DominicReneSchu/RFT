from storage import load_opinions, save_opinions
from verify import sign_content, verify_content
from sync import sync_with_peers

def main():
    # Eigene Meinungen laden
    opinions = load_opinions()
    # Inhalte signieren
    signed_opinions = sign_content(opinions)
    # Synchronisation mit anderen Nodes
    network_opinions = sync_with_peers(signed_opinions)
    # Eingehende Meinungen verifizieren (optional, Platzhalter)
    verified_opinions = [op for op in network_opinions if verify_content(op)]
    # Aktuellen Stand speichern
    save_opinions(verified_opinions)

if __name__ == "__main__":
    main()