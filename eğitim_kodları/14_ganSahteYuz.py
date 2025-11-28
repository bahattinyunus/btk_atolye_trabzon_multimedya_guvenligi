# ----- Gerekli kütüphaneleri içe aktarıyoruz ----- #

import os                  # Dosya ve klasör işlemleri için
import sys                 # Python modül arama yolunu (sys.path) değiştirmek için

import torch               # PyTorch, derin öğrenme kütüphanesi
import torch.nn.functional as F  # interpolate gibi fonksiyonlar için
from torchvision.utils import save_image  # Tensor'dan resim dosyası kaydetmek için
from huggingface_hub import hf_hub_download  # HuggingFace'ten dosya indirmek için
import safetensors         # HuggingFace tarafındaki safetensors hatasını engellemek için (sadece varlığı yeterli)


# -----------------------------------------
# 0) Çıktı boyutunu dinamik olarak belirle
# -----------------------------------------

# Burayı değiştirerek çıktı çözünürlüğünü kontrol edebilirsin.
# Örneğin: 512, 1024, 2048, vb.
OUTPUT_SIZE = 256  # tek sayılık hedef boyut (kare görüntü: OUTPUT_SIZE x OUTPUT_SIZE)


# -----------------------------------------
# 1) Cihazı belirle (GPU varsa CUDA, yoksa CPU)
# -----------------------------------------

device = "cuda" if torch.cuda.is_available() else "cpu"  # Uygun cihazı seç
print("Cihaz:", device)  # Hangi cihazı kullandığımızı ekrana yazdır


# -----------------------------------------
# 2) Hazır StyleGAN yüz modelini indir ve yükle
#    Kaynak: hajar001/stylegan2-ffhq-128 (HuggingFace)
# -----------------------------------------

# HuggingFace Hub üzerinden, model tanımını içeren style_gan.py dosyasını indiriyoruz.
model_file = hf_hub_download(
    repo_id="hajar001/stylegan2-ffhq-128",  # Modelin depo adı
    filename="style_gan.py"                 # Bu depodan indirilecek dosya
)

# İndirilen style_gan.py dosyasının bulunduğu klasörü buluyoruz.
model_dir = os.path.dirname(model_file)

# Bu klasörü Python'un modül arama yoluna ekliyoruz.
# Böylece "from style_gan import StyleGAN" satırı bu dosyayı görebilecek.
sys.path.insert(0, model_dir)

# style_gan.py dosyasının içindeki StyleGAN sınıfını içe aktarıyoruz.
from style_gan import StyleGAN  # noqa: E402  # (lint uyarılarını susturmak için)


# Önceden eğitilmiş (pretrained) StyleGAN2 yüz modelini yüklüyoruz.
# "hajar001/stylegan2-ffhq-128" HuggingFace üzerindeki model kimliği.
model = StyleGAN.from_pretrained("hajar001/stylegan2-ffhq-128")

# Modeli seçtiğimiz cihaza (CPU veya GPU) taşıyoruz.
model = model.to(device)

# Modeli "evaluation" moduna alıyoruz (eğitim yok, sadece üretim).
model.eval()


# -----------------------------------------
# 3) Rastgele latent vektörden sahte yüz üret
# -----------------------------------------

# Artık gradyan hesabına ihtiyaç olmadığı için no_grad bağlamı kullanıyoruz (hesaplama daha ucuz olur).
with torch.no_grad():
    # StyleGAN için latent uzay boyutu 512.
    # 1 adet latent vektör üretiyoruz: boyut (1, 512).
    z = torch.randn(1, 512, device=device)

    # Modelin generate fonksiyonunu çağırarak sahte yüz üretiyoruz.
    # truncation_psi: çeşitlilik/kalite dengesi (0.5–1.0 arası tipik).
    # Çıktı tensörü genelde [-1, 1] aralığında piksel değerleri içerir.
    images = model.generate(z, truncation_psi=0.9)

    # Piksel değerlerini [-1, 1] aralığından [0, 1] aralığına dönüştürüyoruz.
    images = (images + 1) / 2.0

    # Güvenlik için değerleri 0.0 ile 1.0 arasında sıkıştırıyoruz (clamp).
    images = torch.clamp(images, 0.0, 1.0)

    # -----------------------------------------
    # 4) Yüzü büyüt: orijinal çözünürlük → OUTPUT_SIZE x OUTPUT_SIZE
    #    Not: Bu sadece upscale; daha yüksek çözünürlükte görünecek ama yeni detay eklemez.
    # -----------------------------------------

    # OUTPUT_SIZE değişkenini kullanarak kare bir hedef boyut tanımlıyoruz.
    target_size = (OUTPUT_SIZE, OUTPUT_SIZE)

    # interpolate ile görüntüyü hedef boyuta ölçekliyoruz.
    images_big = F.interpolate(
        images,                    # Orijinal çıktı tensörü (muhtemelen 128x128)
        size=target_size,          # Hedef boyut (yükseklik, genişlik) → (OUTPUT_SIZE, OUTPUT_SIZE)
        mode="bilinear",           # Görüntü için uygun interpolasyon yöntemi
        align_corners=False        # Köşeleri hizalama ayarı (genelde False tercih edilir)
    )


# -----------------------------------------
# 5) Sonucu "veriler" klasörüne kaydet
# -----------------------------------------

# Çıktıların saklanacağı klasörü belirliyoruz.
output_dir = "veriler"

# Eğer 'veriler' klasörü yoksa oluşturuyoruz (exist_ok=True: varsa hata vermez).
os.makedirs(output_dir, exist_ok=True)

# Çıktı dosyasının adını dinamik oluşturuyoruz: gan_face_512.png, gan_face_2048.png, vb.
output_filename = f"gan_face_{OUTPUT_SIZE}.png"

# Klasör ve dosya adını birleştirip tam yolu elde ediyoruz.
output_path = os.path.join(output_dir, output_filename)

# Tensor halindeki görüntüyü PNG dosyası olarak kaydediyoruz.
# nrow=1: tek görüntü olduğu için bir satırda 1 görüntü.
save_image(images_big, output_path, nrow=1)

# Konsola bilgi veriyoruz: işlem tamamlandı ve dosya şurada:
print(f"GAN ile üretilen {OUTPUT_SIZE}x{OUTPUT_SIZE} sahte yüz kaydedildi: {output_path}")
