"""Basit asimetrik (RSA) şifreleme ve dijital imza demosu.

cryptography kütüphanesinin high-level RSA arabirimleri kullanılır.
Bu kod eğitim amaçlıdır.
"""

from __future__ import annotations

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def generate_rsa_keypair(key_size: int = 2048):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_with_public_key(public_key, message: str) -> bytes:
    return public_key.encrypt(
        message.encode("utf-8"),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )


def decrypt_with_private_key(private_key, ciphertext: bytes) -> str:
    data = private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
    )
    return data.decode("utf-8")


def sign_message(private_key, message: str) -> bytes:
    return private_key.sign(
        message.encode("utf-8"),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )


def verify_signature(public_key, message: str, signature: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            message.encode("utf-8"),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
        return True
    except Exception:
        return False


def demo() -> None:
    """Uçtan uca RSA şifreleme + imza demosu.

    Çalıştırmak için:
        python -m src.crypto.rsa_demo
    """

    private_key, public_key = generate_rsa_keypair()

    message = "Bu mesaj RSA ile şifrelenecek ve imzalanacak."
    print("Orijinal mesaj:", message)

    ciphertext = encrypt_with_public_key(public_key, message)
    print("Şifreli veri (ilk 80 byte):", ciphertext[:80], b"...")

    recovered = decrypt_with_private_key(private_key, ciphertext)
    print("Çözülen mesaj:", recovered)

    signature = sign_message(private_key, message)
    print("İmza (ilk 80 byte):", signature[:80], b"...")

    ok = verify_signature(public_key, message, signature)
    print("İmza doğrulama sonucu:", ok)


if __name__ == "__main__":
    demo()
