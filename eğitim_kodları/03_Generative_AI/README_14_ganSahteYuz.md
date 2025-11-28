# 14. GAN ile Sahte Yüz Üretimi (StyleGAN2)

Bu çalışma, **StyleGAN2** mimarisini kullanarak gerçekçi olmayan (sahte) insan yüzleri üretmeyi amaçlar. HuggingFace Hub üzerindeki önceden eğitilmiş (pretrained) bir modeli kullanır.

## 📝 Dosya Hakkında

*   **Dosya Adı:** `14_ganSahteYuz.py`
*   **Amaç:** Generative Adversarial Networks (GAN) kullanarak sıfırdan yeni insan yüzleri oluşturmak.
*   **Kullanılan Model:** `hajar001/stylegan2-ffhq-128` (FFHQ veri setinde eğitilmiş).

## ⚙️ Nasıl Çalışır?

Kod çalıştırıldığında aşağıdaki adımları izler:

1.  **Gerekli Kütüphaneleri Yükler:** `torch`, `torchvision`, `huggingface_hub`.
2.  **Modeli İndirir ve Yükler:** HuggingFace Hub'dan `style_gan.py` dosyasını ve ağırlıkları indirir.
3.  **Latent Vektör Üretir:** Rastgele gürültüden (noise) oluşan bir vektör (z) oluşturur.
4.  **Görüntü Üretir:** Bu vektörü modele vererek bir yüz görüntüsü oluşturur.
5.  **Sonucu İşler ve Kaydeder:**
    *   Çıktıyı [0, 1] aralığına normalize eder.
    *   İstenilen boyuta (örn. 256x256) ölçekler.
    *   `veriler/gan_face_256.png` olarak kaydeder.

## 🚀 Kurulum ve Çalıştırma

Bu kodu çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

```bash
pip install torch torchvision huggingface_hub safetensors
```

Kodu çalıştırmak için:

```bash
python 14_ganSahteYuz.py
```

## 📂 Çıktılar

Kod başarıyla çalıştığında `veriler` klasörü altında `gan_face_256.png` dosyası oluşturulur.

*   **Çıktı:** Rastgele üretilmiş, var olmayan bir insan yüzü.

## ⚠️ Notlar

*   Model ilk çalıştırıldığında indirme işlemi yapacağı için internet bağlantısı gereklidir.
*   GPU varsa otomatik olarak CUDA kullanır, yoksa CPU üzerinde çalışır.
