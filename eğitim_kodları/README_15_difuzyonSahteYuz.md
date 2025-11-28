# 15. Difüzyon Modeli ile Sahte Yüz Üretimi (Stable Diffusion Turbo)

Bu çalışma, **Stable Diffusion Turbo** (SD-Turbo) modelini kullanarak metin tabanlı (text-to-image) sahte yüz üretimi yapar.

## 📝 Dosya Hakkında

*   **Dosya Adı:** `15_difuzyonSahteYuz.py`
*   **Amaç:** Metin komutları (prompt) kullanarak yüksek kaliteli ve gerçekçi yapay yüzler oluşturmak.
*   **Kullanılan Model:** `stabilityai/sd-turbo` (Hızlı ve tek adımda sonuç verebilen bir difüzyon modeli).

## ⚙️ Nasıl Çalışır?

Kod çalıştırıldığında aşağıdaki adımları izler:

1.  **Gerekli Kütüphaneleri Yükler:** `diffusers`, `transformers`, `torch`, `PIL`.
2.  **Modeli Yükler:** HuggingFace üzerinden `sd-turbo` modelini indirir (İlk çalıştırmada birkaç GB indirme yapar).
3.  **Prompt İşler:** Kod içindeki İngilizce metin tanımını (prompt) alır.
    *   *Örnek Prompt:* "ultra realistic portrait photo of a young adult..."
4.  **Görüntü Üretir:** Difüzyon modeli, gürültüden başlayarak metne uygun görüntüyü oluşturur.
5.  **Sonucu Kaydeder:**
    *   Çıktıyı `veriler/diffusion_face_1024.png` (veya ayarlanan boyutta) olarak kaydeder.

## 🚀 Kurulum ve Çalıştırma

Bu kodu çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

```bash
pip install torch torchvision diffusers transformers accelerate
```

Kodu çalıştırmak için:

```bash
python 15_difuzyonSahteYuz.py
```

## 📂 Çıktılar

Kod başarıyla çalıştığında `veriler` klasörü altında bir PNG dosyası oluşturulur.

*   **Çıktı:** Prompt'a uygun olarak üretilmiş yapay zeka tabanlı yüz.

## ⚠️ Önemli Notlar

*   **İlk Çalıştırma:** Model dosyaları büyük olduğu için (yaklaşık 2-4 GB), ilk çalıştırmada indirme işlemi internet hızınıza bağlı olarak **uzun sürebilir**.
*   **Donanım:** GPU (NVIDIA CUDA) varsa çok hızlı sonuç alırsınız (saniyeler içinde). CPU üzerinde çalıştırırsanız işlem birkaç dakika sürebilir.
*   **Bellek:** 8GB+ RAM önerilir.
