# 16. SIFT ile Özellik Çıkarımı (Feature Extraction)

Bu çalışma, **SIFT (Scale-Invariant Feature Transform)** algoritmasını kullanarak bir görüntü üzerindeki önemli anahtar noktaları (keypoints) bulmayı amaçlar.

## 📝 Dosya Hakkında

*   **Dosya Adı:** `16_siftOrnek.py`
*   **Amaç:** Görüntü işleme ve bilgisayarlı görüde kullanılan SIFT algoritmasının temel kullanımını göstermek.
*   **Kullanılan Kütüphane:** OpenCV (`cv2`).

## ⚙️ Nasıl Çalışır?

Kod çalıştırıldığında aşağıdaki adımları izler:

1.  **Görüntüyü Okur:** `veriler/ai_content.png` dosyasını okur.
2.  **Gri Seviyeye Çevirir:** SIFT algoritması renk bilgisine ihtiyaç duymaz, bu yüzden gri tona dönüştürülür.
3.  **SIFT Nesnesi Oluşturur:** `cv2.SIFT_create()` ile algoritma başlatılır.
4.  **Özellikleri Bulur:** `detectAndCompute` fonksiyonu ile anahtar noktalar ve tanımlayıcılar (descriptors) hesaplanır.
5.  **Noktaları Çizer:** Bulunan noktalar orijinal görüntü üzerine çizilir.
6.  **Kaydeder ve Gösterir:**
    *   Sonuç `veriler/output_sift_keypoints.jpg` olarak kaydedilir.
    *   Ekranda bir pencere açılarak sonuç gösterilir.

## 🚀 Kurulum ve Çalıştırma

Bu kodu çalıştırmak için OpenCV kütüphanesinin yüklü olması gerekir:

```bash
pip install opencv-python matplotlib
```

Kodu çalıştırmak için:

```bash
python 16_siftOrnek.py
```

## 📂 Çıktılar

Kod başarıyla çalıştığında `veriler` klasörü altında bir JPG dosyası oluşturulur.

*   **Çıktı:** Üzerinde renkli daireler ve çizgilerle işaretlenmiş özellik noktalarını içeren görüntü.

## 💡 SIFT Nedir?

SIFT, görüntüdeki nesneleri tanımak, görüntüleri eşleştirmek veya 3D modelleme yapmak için kullanılan güçlü bir algoritmadır. Görüntü büyütülse, küçültülse veya döndürülse bile aynı noktaları bulabilir (Scale & Rotation Invariant).
