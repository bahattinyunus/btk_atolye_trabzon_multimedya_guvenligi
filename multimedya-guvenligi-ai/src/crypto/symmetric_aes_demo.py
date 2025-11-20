"""Basit simetrik şifreleme (AES-benzeri) demosu.

`cryptography` kütüphanesinin Fernet arabirimini kullanır.
Bu modül eğitim amaçlıdır; gerçek projelerde anahtar yönetimi
ve güvenli depolama eklenmelidir.
"""

from __future__ import annotations

from cryptography.fernet import Fernet


def generate_key() -> bytes:
    """Rastgele bir simetrik anahtar üretir."""

    return Fernet.generate_key()


def encrypt_message(key: bytes, message: str) -> bytes:
    """Verilen metni simetrik anahtarla şifreler."""

    f = Fernet(key)
    token = f.encrypt(message.encode("utf-8"))
    return token


def decrypt_message(key: bytes, token: bytes) -> str:
    """Şifreli veriyi çözüp orijinal metni döndürür."""

    f = Fernet(key)
    data = f.decrypt(token)
    return data.decode("utf-8")


def demo() -> None:
    """Uçtan uca basit bir demo çalıştırır.

    Çalıştırmak için:
        python -m src.crypto.symmetric_aes_demo
    """

    key = generate_key()
    print("Üretilen anahtar:", key.decode())

    message = "Merhaba, bu bir AES-benzeri simetrik şifreleme demosudur."
    print("Orijinal mesaj:", message)

    token = encrypt_message(key, message)
    print("Şifreli veri:", token)

    recovered = decrypt_message(key, token)
    print("Çözülen mesaj:", recovered)


if __name__ == "__main__":
    demo()
