"""
ResonanzNet Keygenerator (Node-Version)
Systemisch: Erzeugt ein RSA-Schlüsselpaar (private.pem, public.pem) im Gruppenverzeichnis ../keys/
Jeder Knoten erhält so eine eindeutige Identität im Feld.
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path

KEYS_DIR = Path("../keys")
PRIVATE_PATH = KEYS_DIR / "private.pem"
PUBLIC_PATH = KEYS_DIR / "public.pem"

def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    return private_key, private_key.public_key()

def save_key(key, path, is_private=False):
    KEYS_DIR.mkdir(exist_ok=True, parents=True)
    if is_private:
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
    else:
        pem = key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    with open(path, "wb") as f:
        f.write(pem)

def main():
    if PRIVATE_PATH.exists() or PUBLIC_PATH.exists():
        print("Schlüssel existieren bereits – Gruppenzugehörigkeit ist systemisch gesichert.")
        return
    priv, pub = generate_rsa_keypair()
    save_key(priv, PRIVATE_PATH, is_private=True)
    save_key(pub, PUBLIC_PATH, is_private=False)
    print(f"RSA-Schlüsselpaar generiert:\n- {PRIVATE_PATH}\n- {PUBLIC_PATH}\n")
    print("Jeder Knoten ist jetzt Teil des Resonanzfeldes – Identität vergeben.")

if __name__ == "__main__":
    main()