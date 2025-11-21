

# 🕵️‍♂️ **Sosyal Mühendislik (Social Engineering) – README**

## 📌 **Giriş**

Sosyal mühendislik, teknik açıklar yerine **insan zaaflarını** hedef alarak yapılan saldırıların genel adıdır. Yani olay şu: “Firewall duvar gibi, IDS canavar gibi… ama insan? ‘Hmm bu link neymiş?’”
Sosyal mühendislik siber güvenliğin en kritik alanlarından biridir çünkü **teknolojiyi değil, insanı hackler.**

---

## 🎯 **Amaç**

Bu README, sosyal mühendisliğin temel prensiplerini, saldırı türlerini, kullanılan teknikleri, önleme yöntemlerini ve gerçek hayattan örnekleri anlatır. Eğitim materyali olarak kullanılabilir.

---

# 🧠 **1. Sosyal Mühendislik Nedir?**

Sosyal mühendislik; manipülasyon, ikna, psikoloji ve insan davranışlarını kullanarak **bilgi, erişim veya yetki elde etme sanatıdır.**
Saldırganlar genellikle:

* Merak
* Aciliyet
* Güven duygusu
* Otoriteye itaat
* Yardımseverlik
* Ödül beklentisi

gibi insani zafiyetleri hedef alır.

---

# 🧩 **2. Sosyal Mühendislik Aşamaları**

Klasik “4 Adım Kuralı”:

### **1️⃣ Bilgi Toplama (Reconnaissance)**

* OSINT
* Profil analizleri
* Sosyal medya taraması
* Whois, Shodan, LinkedIn incelemesi

### **2️⃣ Yaklaşım (Engagement)**

* Mail, telefon, fiziki temas
* Hedefin davranış analizi

### **3️⃣ Manipülasyon (Exploitation)**

* Güven ilişkisi kurma
* Acele ettirme (urgency)
* Sahte kimlik kullanma

### **4️⃣ Sızma / Erişim (Execution)**

* Zararlı link
* Kimlik bilgisi alma
* Cihaz erişimi
* Fiziksel giriş

---

# 🎭 **3. Sosyal Mühendislik Saldırı Türleri**

## 🔹 **Phishing (Oltalama)**

Sahte mail/site ile kullanıcıyı kanmasına zorlama.
Örn: “Hesabınız askıya alındı, hemen giriş yapın!”

## 🔹 **Spear Phishing**

Hedefe özel hazırlanmış profesyonel saldırı.

## 🔹 **Whaling**

CEO / Müdür gibi üst düzey kişilere yapılan saldırı.

## 🔹 **Vishing**

Telefon üzerinden sosyal mühendislik.

## 🔹 **Smishing**

SMS ile oltalama.

## 🔹 **Pretexting (Kurgulama)**

Kendini farklı biri gibi tanıtma (IT çalışanı, polis, kargo vs).

## 🔹 **Baiting**

“Bedava USB” tuzağı gibi yemleme teknikleri.

## 🔹 **Tailgating**

Kartı olmayan birinin kartlı kapıdan biriyle birlikte geçmesi.

## 🔹 **Watering Hole**

Hedefin sıklıkla ziyaret ettiği sitenin hacklenmesi.

---

# 🛠️ **4. Kullanılan Teknikler**

### 🧲 **Psychological Triggers (Psikolojik Tetikler)**

* Otorite: “BT'den geliyorum.”
* Kıtlık: “Son 2 dakika, hesabın kapanıyor.”
* Merak: “Bu fotoğrafta sen varsın!”
* Korku: “Polisten geliyorum, hakkınızda işlem var.”
* Ödül: “iPhone 16 kazandınız!”

### 🧰 **Teknik Araçlar**

* OSINT Framework
* Maltego
* Social-Engineer Toolkit (SET)
* King Phisher
* Evilginx2 (MITM phishing)

---

# 🧿 **5. Korunma Yöntemleri**

## 🔐 **Bireysel Önlemler**

* Bilinmeyen linklere tıklamama
* Mail adresini doğrulama
* Çok faktörlü doğrulama (MFA)
* USB cihaz kabul etmeme
* “Bu kişi gerçekten bu kişi mi?” sorgulaması

## 🏢 **Kurumsal Önlemler**

* Sosyal mühendislik farkındalık eğitimleri
* Güvenli parola politikası
* Güvenlik denetimleri
* Phishing simülasyonları
* Zero-Trust yaklaşımı
* Erişim kontrolü ve loglama

---

# 📚 **6. Örnek Senaryo**

**Senaryo:**
Bir şirket çalışanına BT ekibi olduğun söylenir, cihazda güvenlik güncellemesi yapılması gerektiği belirtilir. Çalışana bir “uzaktan bağlantı linki” gönderilir.
Çalışan bağlanır → saldırgan cihazı ele geçirir.

**Analiz:**

* Otorite
* Aciliyet
* Teknik bilgi eksikliği
  üzerinden saldırı yapılmıştır.

---

# 🧪 **7. Siber Güvenlik Eğitimlerinde Kullanım**

Bu README şu amaçlarla kullanılabilir:

* Sunum & ders materyali
* Siber güvenlik atölyesi
* Red team / blue team çalışmaları
* Phishing kampanyaları hazırlığı
* CTF eğitimleri

---

# 🛡️ **8. Sonuç**

Sosyal mühendislikte en zayıf halka hâlâ *insan.*
Sistemin ne kadar güçlü olduğu önemli değil; **en zeki hacker bile bazen bir çay molasıyla sistemi çökertebilir.**
Bu yüzden teknik savunma kadar **farkındalık** da kritik önemdedir.

