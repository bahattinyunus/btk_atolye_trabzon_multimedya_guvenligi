# ----- Gerekli kütüphaneleri içe aktarıyoruz ----- #
import transformers  # transformers kütüphanesinin yüklü olduğundan emin olmak için
import os                           # Dosya ve klasör yolları için
import torch                        # PyTorch (tensörler ve cihaz yönetimi)
from diffusers import StableDiffusionPipeline  # Difüzyon pipeline'ı
from PIL import Image               # PIL, görüntü işlemleri ve yeniden boyutlandırma için


# -----------------------------------------
# 0) Çıktı boyutunu dinamik olarak belirle
# -----------------------------------------

# Burayı değiştirerek çıktı çözünürlüğünü kontrol edebilirsin.
# Model 512x512 üretir, biz istersen bunu OUTPUT_SIZE x OUTPUT_SIZE'e büyütürüz.
OUTPUT_SIZE = 1024  # Örn: 512, 1024, 2048 ...


# -----------------------------------------
# 1) Cihazı belirle (GPU varsa CUDA, yoksa CPU)
# -----------------------------------------

# Eğer GPU (CUDA) varsa 'cuda', yoksa 'cpu' kullan.
device = "cuda" if torch.cuda.is_available() else "cpu"

# Hangi cihazı kullandığımızı ekrana yazıyoruz.
print("Cihaz:", device)


# -----------------------------------------
# 2) Hazır Stable Diffusion Turbo modelini yükle
#    Model: stabilityai/sd-turbo  (hızlı bir difüzyon modeli)
# -----------------------------------------

# Kullanacağımız modelin Hugging Face üzerindeki kimliği.
model_id = "stabilityai/sd-turbo"

# GPU varsa: 16-bit (float16) ile, yoksa: varsayılan (float32) ile yükleyelim.
if device == "cuda":
    # GPU üzerinde daha az bellek için float16 kullanıyoruz.
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16  # 16-bit hassasiyet
    )
else:
    # CPU'da çalışıyorsan float32 daha güvenli (daha yavaş ama daha sorunsuz).
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32  # 32-bit hassasiyet
    )

# Pipeline'ı seçtiğimiz cihaza gönderiyoruz (GPU veya CPU).
pipe = pipe.to(device)

# Bellek kullanımını azaltmak için attention slicing açabiliriz (özellikle GPU/Vram küçükse).
pipe.enable_attention_slicing()


# -----------------------------------------
# 3) Metin betiğini (prompt) tanımla
# -----------------------------------------

# Üretmek istediğimiz sahte yüzü tarif eden metin.
# İstediğin gibi değiştirebilirsin.
prompt = (
    "ultra realistic portrait photo of a young adult, studio lighting, "
    "sharp focus, 4k, highly detailed, symmetrical face"
)

print("Kullanılan prompt:")
print(prompt)


# -----------------------------------------
# 4) Difüzyon ile görüntü üret
# -----------------------------------------

# Difüzyon adım sayısı (SD-turbo için 1 adım bile çoğu zaman yeterli).
num_steps = 4  # 1–4 arası hızlı, 10+ dersen daha yavaş ama daha rafine olabilir.

# Modelin önerilen temel çözünürlüğü 512x512, biz de orada üreteceğiz.
BASE_SIZE = 512
height = BASE_SIZE
width = BASE_SIZE

# Gradyan hesabına gerek olmadığı için no_grad bağlamı kullanıyoruz.
with torch.no_grad():
    if device == "cuda":
        # GPU kullanıyorsak, otomatik karışık duyarlık (autocast) ile biraz hız kazanırız.
        with torch.autocast("cuda"):
            result = pipe(
                prompt=prompt,            # Metin girdisi
                height=height,            # Yükseklik (piksel)
                width=width,              # Genişlik (piksel)
                num_inference_steps=num_steps,  # Difüzyon adımı
                guidance_scale=0.0        # sd-turbo için önerilen: 0.0 (CFG kullanılmıyor)
            )
    else:
        # CPU kullanıyorsak autocast yok, direkt çağırıyoruz.
        result = pipe(
            prompt=prompt,
            height=height,
            width=width,
            num_inference_steps=num_steps,
            guidance_scale=0.0
        )

# pipe(...) çağrısı bir sonuç objesi döndürür; .images listesi içinde PIL Image'lar vardır.
generated_image = result.images[0]  # İlk (ve tek) görüntüyü alıyoruz.


# -----------------------------------------
# 5) Gerekirse görüntüyü OUTPUT_SIZE x OUTPUT_SIZE boyutuna ölçekle
# -----------------------------------------

# Eğer OUTPUT_SIZE, BASE_SIZE'dan farklıysa, yeniden boyutlandırma yapacağız.
if OUTPUT_SIZE != BASE_SIZE:
    # LANCZOS filtreyle yüksek kaliteli upscaling yapıyoruz.
    generated_image = generated_image.resize((OUTPUT_SIZE, OUTPUT_SIZE), Image.LANCZOS)


# -----------------------------------------
# 6) Sonucu "veriler" klasörüne kaydet
# -----------------------------------------

# Çıktı klasörü: 'veriler'
# Çıktı klasörü: 'veriler'
output_dir = "../veriler"

# Klasör yoksa oluştur (exist_ok=True: varsa hata verme).
os.makedirs(output_dir, exist_ok=True)

# Dosya adını dinamik oluştur: örn. diffusion_face_1024.png
output_filename = f"diffusion_face_{OUTPUT_SIZE}.png"

# Tam dosya yolunu elde et: veriler/diffusion_face_1024.png
output_path = os.path.join(output_dir, output_filename)

# PIL Image nesnesini PNG formatında kaydediyoruz.
generated_image.save(output_path)

# Konsola bilgi yazdırıyoruz.
print(f"Difüzyon ile üretilen sahte yüz kaydedildi: {output_path}")
