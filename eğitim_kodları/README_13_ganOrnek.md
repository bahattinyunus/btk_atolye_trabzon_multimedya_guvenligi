# 13. Stil Aktarımı (Style Transfer) Örneği

Bu çalışma, **TensorFlow Hub** üzerinde bulunan hazır bir **Stil Aktarımı (Style Transfer)** modelini kullanarak, bir içerik görüntüsüne (content image) başka bir görüntünün stilini (style image) uygulama işlemini gerçekleştirir.

## 📝 Dosya Hakkında

*   **Dosya Adı:** `13_ganOrnek.py`
*   **Amaç:** Derin öğrenme tabanlı stil aktarımı (Neural Style Transfer) yapmak.
*   **Kullanılan Model:** Google Magenta tarafından geliştirilen `arbitrary-image-stylization-v1-256` modeli.

## ⚙️ Nasıl Çalışır?

Kod çalıştırıldığında aşağıdaki adımları izler:

1.  **Gerekli Kütüphaneleri Yükler:** `tensorflow`, `tensorflow_hub`, `PIL`, `numpy`, `matplotlib`.
2.  **Görüntüleri Hazırlar:**
    *   İnternet üzerinden örnek bir **İçerik Görüntüsü** (Labrador köpeği) ve **Stil Görüntüsü** (Kandinsky tablosu) indirir.
    *   Bu görüntüleri TensorFlow'un işleyebileceği tensör formatına dönüştürür ve 0-1 aralığına normalize eder.
3.  **Modeli Yükler:** TensorFlow Hub üzerinden hazır eğitilmiş stil aktarım modelini indirir.
4.  **Stil Aktarımı Yapar:** Model, içerik ve stil görüntülerini alarak yeni bir görüntü üretir.
5.  **Sonucu Kaydeder ve Gösterir:**
    *   Üretilen görüntüyü `veriler/output.jpg` olarak kaydeder.
    *   Sonucu ekranda gösterir.

## 🚀 Kurulum ve Çalıştırma

Bu kodu çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

```bash
pip install tensorflow tensorflow-hub pillow matplotlib
```

Kodu çalıştırmak için:

```bash
python 13_ganOrnek.py
```

## 📂 Çıktılar

Kod başarıyla çalıştığında `veriler` klasörü altında `output.jpg` dosyası oluşturulur.

*   **Girdi (Content):** Sarı Labrador
*   **Stil (Style):** Vassily Kandinsky - Composition 7
*   **Çıktı:** Kandinsky stilinde Labrador

## ⚠️ Notlar

*   İlk çalıştırmada modelin ve görüntülerin indirilmesi internet hızınıza bağlı olarak biraz zaman alabilir.
*   TensorFlow kurulumu sisteminize göre değişiklik gösterebilir (CPU/GPU desteği vb.).
