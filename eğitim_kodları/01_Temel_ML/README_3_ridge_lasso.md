# 3_ridge_lasso.py - Ridge ve Lasso Regresyon

Bu çalışma, **Ridge (L2)** ve **Lasso (L1)** regresyon tekniklerini karşılaştırmalı olarak incelemek için hazırlanmıştır.

## 📖 Kod Açıklaması

*   **Dosya Adı:** `3_ridge_lasso.py`
*   **Amaç:** Düzenlileştirme (Regularization) tekniklerinin model üzerindeki etkisini göstermek.
*   **Veri Seti:** California Housing Dataset (Scikit-learn içinden).

## 🎯 Temel Kavramlar

### 1. Ridge Regresyon (L2 Regularization)
*   Hata fonksiyonuna katsayıların karelerinin toplamını ekler.
*   Tüm özellikleri modelde tutar, ancak katsayılarını küçültür (sıfıra yaklaştırır).
*   **Kullanım:** Tüm özelliklerin önemli olduğu veya çoklu bağlantı (multicollinearity) sorunu olan durumlarda.

### 2. Lasso Regresyon (L1 Regularization)
*   Hata fonksiyonuna katsayıların mutlak değerlerinin toplamını ekler.
*   Bazı katsayıları tamamen **sıfıra indirir**.
*   **Kullanım:** Özellik seçimi (feature selection) yapmak istendiğinde.

## 📊 Kodun Yaptığı İşlemler

1.  **Veri Hazırlama:** California ev fiyatları verisini yükler ve eğitim/test olarak böler.
2.  **Standartlaştırma:** Veriyi `StandardScaler` ile ölçekler (Ridge ve Lasso için kritiktir).
3.  **Model Eğitimi:**
    *   Linear Regression (Düzenlileştirme yok)
    *   Ridge (Farklı alpha değerleri ile)
    *   Lasso (Farklı alpha değerleri ile)
4.  **Karşılaştırma:**
    *   MSE (Hata) ve R² (Başarı) skorlarını karşılaştırır.
    *   Sıfır olan katsayı sayılarını analiz eder.
5.  **Özellik Seçimi:** Lasso'nun hangi özellikleri elediğini gösterir.

## 🚀 Çalıştırma

```bash
python 3_ridge_lasso.py
```

## 📈 Beklenen Çıktı Özeti

Kod çalıştığında şunları göreceksiniz:
*   Lasso modelinin bazı özellikleri tamamen çıkardığını (katsayı = 0).
*   Ridge modelinin tüm özellikleri tuttuğunu.
*   Alpha değeri arttıkça modellerin nasıl değiştiğini.

## 💡 İpuçları

*   **Alpha Değeri:** Düzenlileştirme şiddetini belirler.
    *   Alpha = 0 -> Normal Linear Regression
    *   Alpha çok büyük -> Underfitting (Model çok basitleşir)
*   Veri setinizde çok fazla gereksiz özellik varsa **Lasso** kullanın.
*   Özellikler arasında yüksek korelasyon varsa **Ridge** kullanın.
