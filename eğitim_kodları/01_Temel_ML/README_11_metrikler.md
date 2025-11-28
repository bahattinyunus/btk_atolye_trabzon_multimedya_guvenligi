# 11_metrikler.py - Sınıflandırma Metrikleri

Bu kod, **Meme Kanseri (Breast Cancer)** veri seti üzerinde **Lojistik Regresyon** algoritmasını kullanarak bir sınıflandırma modeli eğitir ve modelin başarısını çeşitli metriklerle ölçer.

## Kullanılan Metrikler

Sınıflandırma problemlerinde sadece "Doğruluk (Accuracy)" değerine bakmak yanıltıcı olabilir. Bu yüzden aşağıdaki metrikler de hesaplanmıştır:

1.  **Accuracy (Doğruluk)**: Toplam doğru tahminlerin tüm tahminlere oranı.
2.  **Precision (Kesinlik)**: Pozitif olarak tahmin edilenlerin ne kadarının gerçekten pozitif olduğu.
3.  **Recall (Duyarlılık)**: Gerçek pozitiflerin ne kadarının doğru tahmin edildiği.
4.  **F1-Score**: Precision ve Recall değerlerinin harmonik ortalaması (dengesiz veri setleri için önemlidir).
5.  **Confusion Matrix (Karışıklık Matrisi)**: Doğru ve yanlış tahminlerin (TP, TN, FP, FN) detaylı tablosu.

## Çalıştırma Sonuçları

Kod çalıştırıldığında elde edilen sonuçlar:

```text
=== Değerlendirme Metrikleri ===
Accuracy  : 0.9561
Precision : 0.9459
Recall    : 0.9859
F1-Score  : 0.9655

=== Sınıf Bazlı Rapor ===
              precision    recall  f1-score   support

   malignant       0.97      0.91      0.94        43
      benign       0.95      0.99      0.97        71

    accuracy                           0.96       114
   macro avg       0.96      0.95      0.95       114
weighted avg       0.96      0.96      0.96       114
```

*Not: Kod ayrıca bir Karışıklık Matrisi grafiği oluşturur.*
