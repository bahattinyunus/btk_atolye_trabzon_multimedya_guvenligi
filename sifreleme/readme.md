

# 🔐 **Şifreleme (Encryption) - README**

Bu doküman, şifreleme kavramını temelden ileri seviyeye kadar anlaşılır, akıcı ve pratik bir dille anlatmak için hazırlanmıştır. Multimedya güvenliği, yazılım geliştirme, siber güvenlik ve veri koruma süreçlerinde şifrelemenin temeli bu dosyada ele alınmaktadır.

---

## 📌 **1. Şifreleme Nedir?**

Şifreleme, bir veriyi **anlamsız bir forma dönüştürerek** yetkisiz kişilerin okumasını engelleme işlemidir.
Açık metin (**plaintext**) → Şifrelenmiş metin (**ciphertext**) dönüşümü yapılır.

Amaç:

* Veriyi korumak
* Yetkisiz erişimi engellemek
* Gizlilik, bütünlük ve doğrulama sağlamak

Modern dünyada mesajlaşma uygulamalarından bankacılığa, multimedya içerik korumadan devlet sistemlerine kadar her yerde kullanılır.

---

## 📌 **2. Şifreleme Neden Önemlidir?**

* **Gizlilik** → Mesajları, dosyaları, videoları sadece doğru anahtarı olan kişi açabilir.
* **Bütünlük** → Veri değiştirilse bile tespit edilebilir.
* **Kimlik Doğrulama** → Verinin gerçekten gönderenden geldiğini kanıtlar.
* **Günümüz Dünyasında Zorunluluk** → TLS, WhatsApp E2EE, VPN, SSH gibi tüm kritik sistemler şifreleme tabanlı.

---

# 🔧 **3. Şifreleme Türleri**

Aşağıdaki iki ana başlık tüm siber güvenlik dünyasının temeli sayılır:

---

## **3.1. Simetrik Şifreleme (Symmetric Encryption)**

**Tek bir anahtar** kullanılır:

* Hem şifrelemek
* Hem çözmek için

### Avantajlar

* Çok hızlı
* Büyük dosyalar için ideal
* Multimedya (video, ses) şifrelemede genelde tercih edilir

### Dezavantajlar

* Anahtar paylaşımı sorunlu (en büyük zorluk bu)

### Popüler Algoritmalar

* **AES** (günümüz standardı)
* DES / 3DES (artık zayıf)
* Blowfish
* ChaCha20 (yüksek performans)

---

## **3.2. Asimetrik Şifreleme (Public-Key Encryption)**

**İki farklı anahtar** kullanılır:

* **Public key (genel anahtar)** → Herkes biliyor
* **Private key (özel anahtar)** → Sadece sen biliyorsun

### Avantajlar

* Güvenli anahtar değişimi
* Dijital imza atabilme
* Sunucu–istemci iletişiminde kritik (TLS/HTTPS)

### Dezavantajlar

* Simetriğe göre daha yavaş
* Büyük dosya şifrelemeye uygun değil (genelde sadece *anahtar şifrelemede* kullanılır)

### Popüler Algoritmalar

* **RSA**
* **ECC** (modern & hızlı; WhatsApp, Signal vb. kullanıyor)
* Diffie–Hellman (anahtar değişim protokolü)

---

# 🧩 **4. Hibrit Şifreleme (Hybrid Encryption)**

Günümüzde neredeyse tüm büyük sistemlerin kullandığı yöntem:

> **Simetrik + Asimetrik şifrelemeyi birlikte kullanmak**

Örnek:

* Asimetrik anahtar ile AES anahtarı güvenli şekilde paylaşılır
* Sonra verinin kendisi AES ile şifrelenir (çok hızlı)

HTTPS, WhatsApp, Signal gibi sistemler hibrit model kullanır.

---

# 🔒 **5. Veri Beklerken ve Taşınırken Şifreleme**

## 5.1. **Data at Rest (Bekleyen Veri)**

* Disk şifreleme (BitLocker, FileVault)
* Veritabanı şifreleme
* Cloud depolama güvenliği

Amaç:
Cihazın çalınması durumunda veriyi korumak.

---

## 5.2. **Data in Transit (Taşınan Veri)**

* TLS (HTTPS)
* VPN
* SSH
* E2EE mesajlaşma

Amaç:
Ağ üzerinden geçen veriyi dinlemelere karşı korumak.

---

# 🛡️ **6. Şifreleme Saldırı Modelleri**

## 🧪 **6.1. Brute Force (Kaba Kuvvet)**

Tüm kombinasyonları deneme.
Modern AES için pratik olarak **imkânsız**.

## 🧮 **6.2. Kriptanaliz**

Algoritmalardaki zayıflıkları hedefler.

## 🧻 **6.3. Yan Kanal Saldırıları**

CPU sıcaklığı, zamanlama, güç tüketimi gibi fiziksel ölçümlerden anahtar çıkarmak.

## 📤 **6.4. Key Leakage (Anahtar Sızıntısı)**

En sık görülen: Anahtarın çalınması → sistem direkt düşer.

---

# 🧲 **7. Kriptografide Kullanılan Modlar (Block Cipher Modes)**

AES gibi blok şifrelerin çalışma modlarıdır.

* **ECB** → Güvensiz (pattern leak yapar)
* **CBC** → Güvenli ama yavaş
* **CFB** → Akışa yakın
* **OFB** → Hatalara duyarlı değil
* **CTR** → En hızlı modlardan
* **GCM** → En moderni; hem şifreleme hem doğrulama yapar

---

# 📝 **8. Dijital İmza (Digital Signature)**

Amaçlar:

* Kimlik doğrulama
* İnkâr edilemezlik
* Verinin değişmediğini garanti etme

Kullanılan algoritmalar:

* RSA
* ECDSA
* Ed25519 (modern)

---

# 🔐 **9. Hashing vs Encryption**

| Özellik    | Şifreleme         | Hash            |
| ---------- | ----------------- | --------------- |
| Geri dönüş | Evet, anahtar ile | Hayır           |
| Amaç       | Gizlilik          | Bütünlük        |
| Örnek      | AES, RSA          | SHA-256, BLAKE2 |

Hash, şifreleme değildir!

---

# 📦 **10. Modern Dünyada Şifreleme Kullanım Alanları**

* WhatsApp uçtan uca iletişim
* YouTube DRM içerik koruması
* Cloud depolama
* E-ticaret sitelerinin SSL/TLS sertifikası
* Disk şifreleme
* Blockchain ve kripto paralar
* Parola saklama (hashing + salt)

---

# 🚀 **11. En İyi Uygulamalar (Best Practices)**

* AES-256 veya ChaCha20 tercih et
* RSA yerine ECC kullan
* Anahtarları düz metin olarak saklama
* Salt + hash kullan (parola için)
* GCM gibi doğrulama içeren modlar kullan
* Anahtarları düzenli yenile
* Public Wi-Fi’da mutlaka VPN kullan

---

# 📚 **12. Özet**

Şifreleme, modern güvenlik mimarisinin kalbidir.
Gizlilikten bütünlüğe, kimlik doğrulamadan dijital imzaya kadar her konuda kritiktir. Günümüzde kullanılan tüm güvenli protokollerin temelinde şifreleme vardır.



# 🔐 **Şifreleme – Teknik Derinlik (Part 2)**

Bu bölüm, temel kavramları aşmış geliştiriciler, siber güvenlik öğrencileri ve kriptografi ile ciddi ilgilenenler için hazırlanmış ileri seviye içeriktir. Amaç, şifrelemenin iç mekanizmasını, kırılma yöntemlerini ve modern protokollerde kullanılan güvenlik prensiplerini daha teknik bir dille açıklamaktır.

---

# 🧮 1. Kriptografinin Matematiksel Temelleri

## **1.1. Modüler Aritmetik**

Tüm modern kriptografi **modüler matematik** üzerine kuruludur.
Özellikle:

* RSA → büyük asal çarpanlar
* Diffie-Hellman → modüler üs alma
* ECC → eliptik eğri üzerindeki noktalar

Örnek:
**Mod Exp** → ( c = m^e \mod n )
RSA’nın ana yapısıdır. Bu işlemi hızlı yapmak için **Montgomery Reduction** gibi teknikler kullanılır.

---

## **1.2. Eliptik Eğri Matematiği (ECC)**

Eliptik eğri denklemi:

[
y^2 = x^3 + ax + b
]

Üzerinde toplama işlemi:

* Nokta toplama
* Nokta ikiyleme
* Scalar multiplication (k·P)

ECC’nin gücü:
**256-bit ECC ≈ 3072-bit RSA** güvenliği sağlar.
Bu yüzden Signal, WhatsApp, TLS 1.3 gibi sistemler ECC’yi tercih eder.

---

# 🔑 2. Anahtar Yönetimi (Key Management)

Kriptografide **zayıf algoritordan daha büyük problem**, kötü anahtar yönetimidir.

## **2.1. Key Derivation Functions (KDF)**

Paroladan direkt AES anahtarı üretmek risklidir → brute force için açık kapı.

Bu yüzden:

* PBKDF2
* Argon2 (modern ve memory-hard)
* scrypt

kullanılır.

Amaç:

* Parolayı brute-force'a dayanıklı hale getirmek
* Salt eklemek
* Yüksek hesaplama maliyeti oluşturmak

---

## **2.2. Key Lifecycle**

Bir anahtar şu aşamalardan geçer:

1. Üretim
2. Depolama
3. Dağıtım
4. Rotasyon
5. İmha

Rotasyon yapılmayan anahtarlar → protokol zafiyeti üretir.

---

## **2.3. Anahtar ve Nonce Ayrımı**

* **Key** → kritik
* **Nonce** → tekrar etmeyen sayı
* **IV (Initialization Vector)** → belirli modlarda başlangıç vektörü

AES-GCM gibi modlarda:
**Nonce tekrar ederse bütün şifreleme çöker.**

---

# 🎲 3. Rastgelelik ve PRNG/DRBG Modelleri

Modern kriptografi **güçlü bir rastgeleyiciye** bağlıdır.

* CSPRNG → Cryptographically Secure PRNG
* DRBG → Deterministic Random Bit Generator

Kalitesiz RNG örneği:
2008 Debian OpenSSL hatası → milyonlarca anahtar çöktü.

Kaynaklar:

* /dev/urandom
* NIST SP 800-90A DRBG
* Fortuna generator

---

# 🧱 4. Padding Yapıları ve Saldırılar

## **4.1. Block Cipher Padding**

Blok şifreler (AES-CBC vb.) veriyi bloklara böler.

Popüler padding:

* PKCS#7
* ANSI X.923
* Zero padding

Yanlış padding → **Padding Oracle Attack**
Bu saldırıyla CBC modunda şifre çözme yapılabilir.

---

## **4.2. RSA Padding**

RSA'yı kırmanın en yaygın yolları padding açıklarıdır.

* PKCS#1 v1.5 → zayıf, MitM saldırılarına açık
* OAEP → modern ve güvenli

Bleichenbacher saldırısı (1998) → milyonlarca sistem patladı.

---

# ⚙️ 5. Block Cipher Mode Detayları

## **5.1. Doğrulama Olmayan Modlar**

* ECB → tamamen güvensiz
* CBC → güvenli ama padding oracle zafiyetine açık
* CFB / OFB → akış modları

## **5.2. Doğrulama İçeren Modern Modlar (AEAD)**

AEAD = Authenticated Encryption with Associated Data

* AES-GCM (en yaygın)
* ChaCha20-Poly1305
* OCB mode

AEAD, hem şifreleme hem MAC yapar → veri hem gizli hem bütünlük korumalı olur.

---

# 🔗 6. Mesaj Kimlik Doğrulama Kodları (MAC)

MAC = Message Authentication Code
Bir verinin gerçekten sana ait olduğunu ve değiştirilmediğini kanıtlar.

### Yaygın teknikler:

* HMAC (Hash tabanlı → SHA-256)
* CMAC (AES tabanlı)
* GMAC (GCM’in MAC fonksiyonu)

Şifreleme + MAC = güvenli iletişim
Şifreleme – MAC = **güvensiz**; veri değişse bile fark etmeyebilirsin.

---

# 🔐 7. Diffie-Hellman ve Key Exchange

## **7.1. Klasik Diffie-Hellman**

[
g^a \mod p, \quad g^b \mod p
]

Paylaşılan anahtar:
[
g^{ab} \mod p
]

## **7.2. ECDH – Eliptik Eğri Diffie Hellman**

Daha hızlı ve daha güvenli:

* X25519 (modern standart)
* P-256

TLS 1.3 → yalnızca ECDHE kullanır (forward secrecy için).

---

# ⏱️ 8. Forward Secrecy (FS)

Forward secrecy, gelecekte anahtar sızsa bile **eski oturumların çözülememesini** sağlar.

Bunu sağlayan:
**ECDHE / DHE** gibi geçici anahtar değişimi protokolleri.

TLS 1.3 tamamen forward-secret.

---

# ☠️ 9. Saldırı Modelleri – İleri Seviye

## **9.1. Chosen-Plaintext Attack (CPA)**

Saldırgan bazı verilerin şifreli halini üretebilir.

## **9.2. Chosen-Ciphertext Attack (CCA)**

Saldırgan bazı şifreli blokları çözmeye zorlayabilir.
RSA-CCA → OAEP zorunlu hale geldi.

## **9.3. Side-Channel Attacks**

* Timing
* Power analysis
* Acoustic analysis
* EM leakage

Pratikte en tehlikeli saldırılar bunlardır.

---

# 🧩 10. Post-Quantum Cryptography (PQC)

Kuantum bilgisayarlar:

* RSA
* ECC
* DH

gibi sistemleri kırabilir.

Bu yüzden NIST yeni standartları seçti:

### Onaylanan Algoritmalar:

* **CRYSTALS-Kyber** (anahtar değişimi)
* **CRYSTALS-Dilithium** (dijital imza)
* **Falcon** (dijital imza)

Gelecek → hibrit:
*ECC + PQC birlikte kullanılacak.*

---

# 🎯 11. Özet

Part 2’de gördüklerin:

* Matematiksel temeller
* Anahtar yönetimi
* Nonce/IV kritikliği
* Padding zafiyetleri
* AEAD modlarının önemi
* MAC mekanizmaları
* DH/ECDH çalışma mantığı
* Forward secrecy prensipleri
* Quantum sonrası kripto sistemler

Bunlar, modern siber güvenlikte kripto uygulayan herkesin bilmesi gereken yapısal bilgiler.

---

