# OpenCV kütüphanesini içe aktarıyoruz (görüntü okuma, işleme, SIFT vb. için kullanacağız).
import cv2

# NumPy, matris / dizi işlemleri için (OpenCV ile sık birlikte kullanılır, burada zorunlu değil ama hazır dursun).
import numpy as np

# matplotlib, sonucu ekranda gösterebilmek için kullanacağız.
import matplotlib.pyplot as plt

# ----------------------- AYARLAR ----------------------- #
import os

# Veri klasörü (bir üst dizinde)
DATA_DIR = "../veriler"

# Üzerinde SIFT özellik noktaları bulmak istediğimiz girdi görüntüsünün dosya yolu.
INPUT_IMAGE_PATH = os.path.join(DATA_DIR, "ai_content.png")

# Özellik noktaları çizilmiş çıktıyı kaydedeceğimiz dosya yolu.
OUTPUT_IMAGE_PATH = os.path.join(DATA_DIR, "output_sift_keypoints.jpg")
# ------------------------------------------------------- #


# 1) Girdiyi oku (renkli olarak)
# cv2.imread, resmi BGR (Blue-Green-Red) kanal sırasıyla okur.
image_bgr = cv2.imread(INPUT_IMAGE_PATH)

# Eğer görüntü okunamadıysa (dosya yok, yol yanlış vs.), hata fırlatıyoruz.
if image_bgr is None:
    raise FileNotFoundError(f"Girdi görüntüsü okunamadı: {INPUT_IMAGE_PATH}")


# 2) SIFT genellikle gri seviyeli (tek kanal) görüntü üzerinde çalışır.
# Bu yüzden önce BGR formatındaki görüntüyü gri seviyeye dönüştürüyoruz.
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)


# 3) SIFT nesnesini oluşturuyoruz.
# cv2.SIFT_create() sadece opencv-contrib-python paketinde bulunur.
sift = cv2.SIFT_create(
    nfeatures=5000,          # En fazla kaç anahtar nokta bulsun?
    contrastThreshold=0.09, # Kontrast eşiği (daha yüksek -> daha az nokta)
    edgeThreshold=10,       # Kenar duyarlılığı
    sigma=1.6               # Gauss bulanıklığı (ölçek uzayı için)
)


# 4) SIFT ile özellik noktası (keypoint) ve descriptor hesaplama
# detectAndCompute:
#   - Birinci parametre: giriş görüntüsü (gri seviye)
#   - İkinci parametre: maske (None -> tüm görüntüyü kullan)
#   - Çıktı: keypoints (konum, ölçek vb. bilgiler) ve descriptors (her noktanın öznitelik vektörü)
keypoints, descriptors = sift.detectAndCompute(image_gray, None)

# Bulunan özellik noktası sayısını konsola yazdırıyoruz.
print(f"Bulunan SIFT özellik noktası sayısı: {len(keypoints)}")


# 5) Özellik noktalarını orijinal görüntü üzerinde çizdirme
# cv2.drawKeypoints:
#   - İlk parametre: arka plan olarak kullanılacak görüntü (biz BGR renkli görüntüyü kullanıyoruz).
#   - İkinci parametre: çizmek istediğimiz keypoint listesi.
#   - Üçüncü parametre: çıktı görüntüsü (None verirsek yeni bir görüntü döner).
#   - flags: DRAW_RICH_KEYPOINTS -> sadece noktayı değil, ölçeği ve yönü de gösterir (daha bilgi verici).
image_with_keypoints_bgr = cv2.drawKeypoints(
    image_bgr,                                      # Arka plan görüntü (renkli)
    keypoints,                                      # Çizilecek SIFT noktaları
    None,                                           # Yeni bir çıktı görüntüsü oluştur
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)


# 6) OpenCV BGR formatını kullanırken, matplotlib RGB formatını bekler.
# Bu yüzden gösterim için BGR'yi RGB'ye dönüştürüyoruz.
image_with_keypoints_rgb = cv2.cvtColor(
    image_with_keypoints_bgr,                       # BGR formatındaki görüntü
    cv2.COLOR_BGR2RGB                               # BGR -> RGB dönüşüm kodu
)


# 7) Çıktı görüntüsünü dosyaya kaydediyoruz.
# Burada BGR formatında kaydetmemiz sorun değil, çünkü dosyayı normal bir görüntü izleyici açarken BGR/RGB farkı yok.
cv2.imwrite(OUTPUT_IMAGE_PATH, image_with_keypoints_bgr)

# Kullanıcıya konsolda bilgi veriyoruz: çıktı nereye kaydedildi.
print(f"SIFT özellik noktaları çizilmiş görüntü kaydedildi: {OUTPUT_IMAGE_PATH}")


# 8) Görüntüyü matplotlib ile ekranda gösteriyoruz.
# Yeni bir şekil (figure) penceresi oluşturuyoruz, boyutunu ayarlıyoruz.
plt.figure(figsize=(10, 8))

# RGB formatındaki görüntüyü çizdiriyoruz.
plt.imshow(image_with_keypoints_rgb)

# X ve Y eksen çizgilerini ve değerlerini gizliyoruz (sadece görüntü kalsın).
plt.axis("off")

# Üst tarafa bir başlık ekliyoruz.
plt.title("SIFT Özellik Noktaları")

# Grafiği (ve dolayısıyla görüntüyü) ekranda gösteriyoruz.
plt.show()
