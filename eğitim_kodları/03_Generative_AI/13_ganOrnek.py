# TensorFlow kütüphanesini içe aktarıyoruz (derin öğrenme için kullanacağız).
import tensorflow as tf

# TensorFlow Hub kütüphanesini içe aktarıyoruz (hazır eğitilmiş modeli buradan alacağız).
import tensorflow_hub as hub

# Görüntü dosyalarını açıp işlemek için Pillow kütüphanesinden Image sınıfını alıyoruz.
from PIL import Image

# Sayısal işlemler ve dizi (array) yönetimi için NumPy kütüphanesini içe aktarıyoruz.
import numpy as np

# Çıktı görüntüsünü ekranda gösterebilmek için matplotlib’in pyplot modülünü içe aktarıyoruz.
import matplotlib.pyplot as plt

# ----------------------- AYARLAR ----------------------- #
import os

# Veri klasörünü oluştur (Çıktı için) - Bir üst dizindeki veriler klasörünü kullan
output_dir = "../veriler"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Görüntüleri indir (eğer yoksa) ve yollarını al
# AI Temalı Görseller (Yerel olarak oluşturuldu ve veriler klasörüne kopyalandı)
# Content: AI Robot Face
CONTENT_IMAGE_PATH = os.path.join(output_dir, "ai_content.png")
print(f"Content path: {CONTENT_IMAGE_PATH}")

# Style: Matrix/Cyberpunk Code
STYLE_IMAGE_PATH = os.path.join(output_dir, "ai_style.png")
print(f"Style path: {STYLE_IMAGE_PATH}")

# Stil uygulanmış sonucu kaydedeceğimiz çıktı dosyasının adı.
OUTPUT_IMAGE_PATH = os.path.join(output_dir, "output_ai_theme.jpg")


# ------------------------------------------------------ #


# Bir görüntüyü dosyadan okuyup modele uygun formata getiren yardımcı fonksiyon.
def load_image(path, max_dim=512):
    # Verilen dosya yolundan görüntüyü açıyoruz ve RGB formatına çeviriyoruz (3 kanal: R, G, B).
    img = Image.open(path).convert("RGB")

    # Görüntünün uzun kenarını max_dim’e göre küçültüyoruz (orantılı şekilde ölçekler).
    img.thumbnail((max_dim, max_dim))

    # Pillow Image nesnesini NumPy dizisine çeviriyoruz (piksel değerleri 0–255 arası olur).
    img = np.array(img)

    # Piksel değerlerini 0–255 aralığından 0–1 aralığına ölçekliyoruz (float’a çevirme).
    img = img / 255.0

    # Tipini açıkça float32 yapıyoruz, çünkü TensorFlow genelde float32 ile çalışır.
    img = img.astype(np.float32)

    # Modele vermek için başa bir boyut ekliyoruz (batch size = 1 olacak).
    # Örneğin (H, W, 3) → (1, H, W, 3).
    img = img[None, ...]

    # Hazırladığımız tensörü geri döndürüyoruz.
    return img


# TensorFlow çıktısını tekrar görüntü (Pillow Image) haline getiren yardımcı fonksiyon.
def tensor_to_image(tensor):
    # Gelen tensörün ilk (ve tek) batch boyutunu kaldırıyoruz: (1, H, W, 3) → (H, W, 3).
    tensor = tensor[0].numpy()

    # Değerler 0–1 aralığında olduğu için tekrar 0–255 aralığına çarpıyoruz.
    tensor = tensor * 255.0

    # Değerlerin 0 ile 255 arasında kalmasını garanti altına almak için kırpıyoruz (clip).
    tensor = np.clip(tensor, 0, 255)

    # Tipini uint8 yapıyoruz (görüntü formatları genelde 8 bit tamsayı kullanır).
    tensor = tensor.astype("uint8")

    # NumPy dizisini Pillow Image nesnesine çevirip geri döndürüyoruz.
    return Image.fromarray(tensor)


# -------------------- 1) GÖRÜNTÜLERİ YÜKLE -------------------- #
# İçerik (content) görüntüsünü, modele uygun tensör formatında yüklüyoruz.
content_image = load_image(CONTENT_IMAGE_PATH)

# Stil (style) görüntüsünü de aynı şekilde yüklüyoruz.
style_image = load_image(STYLE_IMAGE_PATH)
# -------------------------------------------------------------- #


# ---------------- 2) HAZIR STİL AKTARIM MODELİNİ YÜKLE ---------------- #
# TensorFlow Hub üzerinden Google'ın yayınladığı hazır stil aktarım modelini yüklüyoruz.
# Bu model, keyfi (arbitrary) bir stil görüntüsünü, içerik görüntüsüne uygulayabiliyor.
hub_model = hub.load(
    "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
)
# ---------------------------------------------------------------------- #


# ---------------- 3) STİLİZE EDİLMİŞ GÖRÜNTÜYÜ ÜRET ---------------- #
# hub_model, iki tensör alıyor:
# 1) içerik görüntüsü tensörü,
# 2) stil görüntüsü tensörü,
# ve stilize edilmiş bir çıktı görüntüsü döndürüyor.
stylized_image = hub_model(
    tf.constant(content_image),  # içerik görüntüsünü TF tensörüne çevirip veriyoruz
    tf.constant(style_image)  # stil görüntüsünü TF tensörüne çevirip veriyoruz
)[0]  # model birden fazla çıktı döndürüyor, ilkini (stilize görüntü) alıyoruz
# ----------------------------------------------------------------- #


# ---------------- 4) ÇIKTIYI KAYDET VE GÖRÜNTÜLE ---------------- #
# TensorFlow çıktısını Pillow Image nesnesine çeviriyoruz.
output_img = tensor_to_image(stylized_image)

# Çıktıyı disk üzerine OUTPUT_IMAGE_PATH adıyla kaydediyoruz.
output_img.save(OUTPUT_IMAGE_PATH)

# Kullanıcıya, işlemin tamamlandığını ve nereye kaydedildiğini konsolda bildiriyoruz.
print(f"İşlem bitti. Çıktı dosyası: {OUTPUT_IMAGE_PATH}")

# Şimdi çıktı görüntüsünü ekranda göstereceğiz.
# matplotlib, Jupyter defterinde veya uygun bir ortamda resmi inline (satır içi) gösterebilir.
plt.imshow(output_img)  # Görüntüyü eksenlere (plot) yerleştiriyoruz.
plt.axis("off")  # X ve Y eksen çizgilerini gizliyoruz (sadece görüntü kalsın).
plt.title("Stilize Edilmiş Görüntü")  # Grafiğin üstüne bir başlık ekliyoruz.
plt.show()  # Grafiği (ve dolayısıyla görüntüyü) ekranda gösteriyoruz.
# ---------------------------------------------------------------- #
