# -*- coding: utf-8 -*-
"""
K Değeri Seçimi - Kısa ve Öz
Her satır açıklamalı
"""

# Matematiksel işlemler için numpy kütüphanesi
import numpy as np
# Iris veri setini yüklemek için
from sklearn.datasets import load_iris
# K-Means algoritması için
from sklearn.cluster import KMeans
# Veriyi standardize etmek için
from sklearn.preprocessing import StandardScaler
# Kümeleme kalitesini ölçmek için
from sklearn.metrics import silhouette_score

# Başlık yazdır
print("🎯 K DEĞERİ SEÇİMİ - KISA ANALİZ")
print("=" * 40)

# Iris veri setini yükle
iris = load_iris()
# Çiçek özelliklerini al (4 özellik)
X = iris.data
# Standardizasyon için scaler oluştur
scaler = StandardScaler()
# Veriyi standardize et (ortalama=0, standart sapma=1)
X_scaled = scaler.fit_transform(X)

# 1. bölüm başlığı
print("1. DİRSEK YÖNTEMİ İLE ANALİZ")
print("-" * 30)

# Test edilecek K değerleri: 1'den 7'ye kadar
K_degerleri = range(1, 8)
# WCSS değerlerini saklayacak liste
wcss_list = []

# Tablo başlığı
print("K |   WCSS   | Değişim")
print("-" * 25)

# Her K değeri için döngü
for k in K_degerleri:
    # K-Means modelini oluştur
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    # Modeli eğit
    kmeans.fit(X_scaled)
    # WCSS değerini al (küme içi kareler toplamı)
    wcss = kmeans.inertia_
    # WCSS'yi listeye ekle
    wcss_list.append(wcss)

    # Değişimi hesapla (ilk değer hariç)
    if k > 1:
        # Önceki WCSS'den şimdikini çıkar
        degisim = wcss_list[k - 2] - wcss
        # Sonucu yazdır
        print(f"{k} | {wcss:7.1f} | {degisim:6.1f}")
    else:
        # İlk değer için değişim yok
        print(f"{k} | {wcss:7.1f} |   -")

# WCSS değişimlerini hesapla
wcss_degisim = [wcss_list[i - 1] - wcss_list[i] for i in range(1, len(wcss_list))]
# En büyük değişimin olduğu indeksi bul ve +2 ekle (K=2'den başladığı için)
dirsek_k = np.argmax(wcss_degisim) + 2
# Dirsek noktasını yazdır
print(f"\n🎯 Dirsek Noktası: K = {dirsek_k}")

# 2. bölüm başlığı
print("\n2. SİLHUETTE ANALİZİ")
print("-" * 30)

# Tablo başlığı
print("K | Silhouette")
print("-" * 15)

# En iyi silhouette skoru ve K değerini takip et
best_silhouette = 0
best_k = 2

# K=2'den 7'ye kadar döngü
for k in range(2, 8):
    # K-Means modelini oluştur
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    # Modeli eğit
    kmeans.fit(X_scaled)
    # Silhouette skorunu hesapla
    silhouette = silhouette_score(X_scaled, kmeans.labels_)
    # Sonucu yazdır
    print(f"{k} | {silhouette:.3f}")

    # En iyi skoru güncelle
    if silhouette > best_silhouette:
        best_silhouette = silhouette
        best_k = k

# En iyi silhouette sonucunu yazdır
print(f"\n🎯 En İyi Silhouette: K = {best_k} (skor: {best_silhouette:.3f})")

# 3. bölüm başlığı
print("\n3. DOMAİN BİLGİSİ")
print("-" * 30)
# Iris'teki tür sayısını yazdır
print(f"🌼 Iris verisinde {len(iris.target_names)} tür var")
# Domain bilgisine göre önerilen K değeri
print(f"🎯 Domain Bilgisine Göre: K = 3")

# 4. bölüm başlığı
print("\n4. FİNAL KARAR")
print("-" * 30)

# Tüm yöntemlerin önerdiği K değerleri
oylar = [dirsek_k, best_k, 3]  # Dirsek, Silhouette, Domain
# En çok oy alan K değerini bul
final_k = max(set(oylar), key=oylar.count)

# Tüm yöntem sonuçlarını yazdır
print(f"📊 Yöntem Sonuçları:")
print(f"   • Dirsek Yöntemi: K = {dirsek_k}")
print(f"   • Silhouette: K = {best_k}")
print(f"   • Domain Bilgisi: K = 3")
# Seçilen K değerini yazdır
print(f"\n🏆 Seçilen K Değeri: {final_k}")

# Seçilen K ile model oluşturma
print(f"\n5. K = {final_k} İLE MODEL")
print("-" * 30)

# Final K değeri ile model oluştur
kmeans_final = KMeans(n_clusters=final_k, random_state=42, n_init=10)
# Modeli eğit
kmeans_final.fit(X_scaled)

# Sonuçları yazdır
print(f"✅ Model eğitildi")
print(f"📊 WCSS: {kmeans_final.inertia_:.1f}")
print(f"📈 Silhouette: {silhouette_score(X_scaled, kmeans_final.labels_):.3f}")

# Bitirme mesajı
print(f"\n🎉 K DEĞERİ SEÇİMİ TAMAMLANDI!")