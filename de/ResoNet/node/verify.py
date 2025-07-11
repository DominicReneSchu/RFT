import hashlib

def sign_content(content):
    # TODO: Implementiere echte Signatur via Schlüssel (z.B. RSA/ECC)
    # Platzhalter: Hash als Signatur
    signature = hashlib.sha256(str(content).encode("utf-8")).hexdigest()
    return {"content": content, "signature": signature}

def verify_content(signed_opinion):
    # TODO: Implementiere echte Signaturprüfung mit public.pem
    # Platzhalter: immer True (Gruppenzugehörigkeit systemisch angenommen)
    return True