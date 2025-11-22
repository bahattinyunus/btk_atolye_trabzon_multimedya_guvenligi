# -*- coding: utf-8 -*-
"""
K-Means Kümeleme Algoritması - Iris Veri Seti
Basit ve Anlaşılır Versiyon
"""

# 1. GEREKLİ KÜTÜPHANELERİ YÜKLEME
import numpy as np  # Matematiksel işlemler için
import pandas as pd  # Veri işleme için
from sklearn.datasets import load_iris  # Iris veri seti
from sklearn.cluster import KMeans  # K-Means algoritması
from sklearn.preprocessing import StandardScaler  # Veri standardizasyonu
from sklearn.metrics import confusion_matrix  # Performans metriği

# 3. VERİ SETİNİ YÜKLEME
print("\n1. VERİ SETİNİ YÜKLÜYORUM...")
iris = load_iris()
X = iris.data  # Çiçek özellikleri (4 özellik)
y = iris.target  # Gerçek çiçek türleri (kümelemede KULLANMIYORUZ)

print(f"✅ Veri seti yüklendi")
print(f"📊 Toplam {X.shape[0]} çiçek, {X.shape[1]} özellik")
print(f"🌸 Özellikler: {iris.feature_names}")
print(f"🎯 Gerçek türler: {iris.target_names}")

# 4. VERİYİ İNCELEME
print("\n2. VERİYİ İNCELİYORUM...")
# İlk 5 çiçeğin özelliklerini göster
print("🔍 İLK 5 ÇİÇEĞİN ÖZELLİKLERİ:")
for i in range(5):
    print(f"  Çiçek {i + 1}: {X[i]}")

# 5. VERİ ÖN İŞLEME
print("\n3. VERİYİ HAZIRLIYORUM...")
# K-Means ölçeklendirmeye duyarlıdır, bu yüzden standardize ediyoruz
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("✅ Veri standardizasyonu tamamlandı")

# 6. K-MEANS MODELİNİ OLUŞTURMA
print("\n4. K-MEANS MODELİNİ KURUYORUM...")

# Iris'te 3 tür olduğu için doğrudan K=3 kullanıyoruz
K = 3

# K-Means modelini oluştur
kmeans_model = KMeans(
    n_clusters=K,  # Küme sayısı = 3
    random_state=42,  # Aynı sonuçları almak için
    n_init=10,  # 10 farklı başlangıç noktası dene
    max_iter=300  # Maksimum 300 iterasyon
)

print(f"🔧 Model parametreleri:")
print(f"  • Küme sayısı (K): {K}")
print(f"  • Random state: 42")
print(f"  • Başlangıç denemesi: 10")
print(f"  • Maksimum iterasyon: 300")

# 7. MODELİ EĞİTME
print("\n5. MODELİ EĞİTİYORUM...")
kmeans_model.fit(X_scaled)
print("✅ Model eğitimi tamamlandı!")
print(f"🔄 Gerçekleşen iterasyon sayısı: {kmeans_model.n_iter_}")

# 8. MODEL SONUÇLARINI ALMA
print("\n6. KÜMELEME SONUÇLARINI ALIYORUM...")

# Tahmin edilen küme etiketlerini al
tahmin_edilen_kumeler = kmeans_model.labels_

# Küme merkezlerini al
kume_merkezleri = kmeans_model.cluster_centers_

print(f"🎯 İlk 10 çiçeğin atandığı kümeler: {tahmin_edilen_kumeler[:10]}")
print(f"📌 {len(kume_merkezleri)} küme merkezi bulundu")

# 9. KÜMELEME SONUÇLARINI İNCELEME
print("\n7. KÜMELEME SONUÇLARINI İNCELİYORUM...")

# DataFrame oluşturarak sonuçları inceleyelim
sonuc_df = pd.DataFrame({
    'Gerçek_Tür': y,
    'Gerçek_Tür_İsmi': [iris.target_names[t] for t in y],
    'Tahmin_Edilen_Küme': tahmin_edilen_kumeler
})

print("📋 İLK 10 ÇİÇEĞİN KARŞILAŞTIRMASI:")
print(sonuc_df.head(10))

# 10. KÜME DAĞILIMINI GÖRME
print("\n8. KÜME DAĞILIMINI ANALİZ EDİYORUM...")

# Her kümede kaç çiçek var?
kume_dagilimi = sonuc_df['Tahmin_Edilen_Küme'].value_counts().sort_index()
print("📊 KÜMELERDEKİ ÇİÇEK SAYILARI:")
for kume, sayi in kume_dagilimi.items():
    print(f"  Küme {kume}: {sayi} çiçek")

# 11. GERÇEK TÜRLER İLE KARŞILAŞTIRMA
print("\n9. GERÇEK TÜRLER İLE KARŞILAŞTIRIYORUM...")

karsilastirma_tablosu = pd.crosstab(
    sonuc_df['Gerçek_Tür_İsmi'],
    sonuc_df['Tahmin_Edilen_Küme'],
    rownames=['Gerçek Tür'],
    colnames=['Tahmin Küme']
)

print("📈 GERÇEK TÜRLER vs TAHMİN EDİLEN KÜMELER:")
print(karsilastirma_tablosu)

# 12. BASİT DOĞRULUK HESAPLAMA
print("\n10. BASİT DOĞRULUK ANALİZİ...")


# Kümeleri en çok hangi türe denk geldiğine göre eşleştirelim
def basit_kume_eslestirme(tahmin_kumeleri, gercek_etiketler, kume_sayisi):
    """Kümeleri en çok hangi gerçek etikete denk geldiğine göre eşleştirir"""
    eslesme = {}

    for kume in range(kume_sayisi):
        # Bu kümedeki örneklerin gerçek etiketlerini al
        kume_etiketleri = gercek_etiketler[tahmin_kumeleri == kume]

        if len(kume_etiketleri) > 0:
            # En sık görülen etiketi bul
            benzersiz, sayilar = np.unique(kume_etiketleri, return_counts=True)
            en_cok_etiket = benzersiz[np.argmax(sayilar)]
            eslesme[kume] = en_cok_etiket
        else:
            eslesme[kume] = -1  # Küme boşsa

    return eslesme


# Eşleştirmeyi yap
etiket_eslestirme = basit_kume_eslestirme(tahmin_edilen_kumeler, y, K)

print("🔀 KÜME-GERÇEK TÜR EŞLEŞTİRMESİ:")
for kume, gercek_tur in etiket_eslestirme.items():
    if gercek_tur != -1:
        print(f"  Küme {kume} → {iris.target_names[gercek_tur]}")

# Eşleştirilmiş tahminleri oluştur
eslestirilmis_tahminler = np.zeros_like(tahmin_edilen_kumeler)
for kume in range(K):
    mask = (tahmin_edilen_kumeler == kume)
    eslestirilmis_tahminler[mask] = etiket_eslestirme[kume]

# Doğruluk hesapla
dogru_tahmin = np.sum(eslestirilmis_tahminler == y)
toplam = len(y)
gercek_dogruluk = dogru_tahmin / toplam

print(f"\n📊 GERÇEK DOĞRULUK: {gercek_dogruluk:.1%}")
print(f"✅ Doğru tahmin edilen: {dogru_tahmin}/{toplam}")

# Karışıklık matrisi
print(f"\n🎯 KARIŞIKLIK MATRİSİ:")
cm = confusion_matrix(y, eslestirilmis_tahminler)
print(cm)

# 13. KÜME MERKEZLERİNİ İNCELEME
print("\n11. KÜME MERKEZLERİNİ İNCELİYORUM...")

# Küme merkezlerini orijinal ölçeğe çevir
kume_merkezleri_original = scaler.inverse_transform(kume_merkezleri)

# DataFrame oluştur
merkezler_df = pd.DataFrame(
    kume_merkezleri_original,
    columns=iris.feature_names
)

print("🎯 KÜME MERKEZLERİ (ORJİNAL ÖLÇEKTE):")
print(merkezler_df.round(2))

# 14. KÜMELERİ YORUMLAMA
print("\n12. KÜMELERİ YORUMLUYORUM...")

for i, merkez in merkezler_df.iterrows():
    gercek_tur_ismi = iris.target_names[etiket_eslestirme[i]]

    print(f"\n🔍 KÜME {i} ({gercek_tur_ismi}):")
    print(f"  Çanak yaprak: {merkez['sepal length (cm)']:.1f}cm x {merkez['sepal width (cm)']:.1f}cm")
    print(f"  Taç yaprak: {merkez['petal length (cm)']:.1f}cm x {merkez['petal width (cm)']:.1f}cm")

# 15. YENİ BİR ÇİÇEK İÇİN TAHMİN
print("\n13. YENİ BİR ÇİÇEK İÇİN TAHMİN YAPIYORUM...")

# Örnek çiçek özellikleri
yeni_cicek_1 = np.array([[5.1, 3.5, 1.4, 0.2]])  # setosa benzeri
yeni_cicek_2 = np.array([[6.0, 2.7, 5.1, 1.6]])  # virginica benzeri

# Aynı standardizasyonu uygula
yeni_cicek_1_scaled = scaler.transform(yeni_cicek_1)
yeni_cicek_2_scaled = scaler.transform(yeni_cicek_2)

# Küme tahmini yap
tahmin_kume_1 = kmeans_model.predict(yeni_cicek_1_scaled)[0]
tahmin_kume_2 = kmeans_model.predict(yeni_cicek_2_scaled)[0]

# Eşleştirilmiş tahmin
tahmin_tur_1 = etiket_eslestirme[tahmin_kume_1]
tahmin_tur_2 = etiket_eslestirme[tahmin_kume_2]

print("🌱 YENİ ÇİÇEK 1 (Setosa benzeri):")
print(f"  Özellikler: {yeni_cicek_1[0]}")
print(f"  Tahmin edilen küme: {tahmin_kume_1}")
print(f"  Tahmin edilen tür: {iris.target_names[tahmin_tur_1]}")

print("\n🌺 YENİ ÇİÇEK 2 (Virginica benzeri):")
print(f"  Özellikler: {yeni_cicek_2[0]}")
print(f"  Tahmin edilen küme: {tahmin_kume_2}")
print(f"  Tahmin edilen tür: {iris.target_names[tahmin_tur_2]}")

# 16. NİHAİ DEĞERLENDİRME
print("\n14. NİHAİ DEĞERLENDİRME...")

if gercek_dogruluk > 0.85:
    durum = "✅ MÜKEMMEL - K-Means türleri çok iyi ayırt edebildi"
elif gercek_dogruluk > 0.75:
    durum = "👍 İYİ - K-Means türleri iyi ayırt edebildi"
elif gercek_dogruluk > 0.65:
    durum = "⚠️  ORTA - K-Means türleri kısmen ayırt edebildi"
else:
    durum = "❌ ZAYIF - K-Means türleri ayırt etmekte zorlandı"

print(f"📈 DURUM: {durum}")

print(f"\n💡 ANALİZ:")
print(f"• K-Means, iris çiçeklerini %{gercek_dogruluk * 100:.1f} doğrulukla gruplayabildi")
print(f"• Bu, denetimsiz öğrenme için oldukça iyi bir sonuç")
print(f"• Taç yaprak özellikleri en belirleyici faktör")

# 17. SONUÇ ÖZETİ
print("\n" + "=" * 50)
print("🎉 K-MEANS KÜMELEME SONUÇ ÖZETİ")
print("=" * 50)

print(f"✅ Kullanılan küme sayısı: {K}")
print(f"✅ Toplam çiçek sayısı: {X.shape[0]}")
print(f"✅ Gerçek Doğruluk: {gercek_dogruluk:.1%}")
print(f"✅ Model başarıyla eğitildi")

print(f"\n🏁 UYGULAMA TAMAMLANDI!")