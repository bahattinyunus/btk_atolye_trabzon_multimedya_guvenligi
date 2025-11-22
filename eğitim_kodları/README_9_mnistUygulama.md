# 🧠 MNIST Rakam Tanıma ile Yapay Sinir Ağı (ANN) Projesi

Bu proje, **Artificial Neural Network (ANN)** kullanarak **MNIST rakam veri seti** üzerinde rakam tanıma işlemi gerçekleştiren kapsamlı bir deep learning uygulamasıdır.

## 📋 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Model Mimarisi](#model-mimarisi)
- [Kod Yapısı](#kod-yapısı)
- [Sonuçlar](#sonuçlar)
- [Teknik Detaylar](#teknik-detaylar)
- [Öğrenme Çıktıları](#öğrenme-çıktıları)

## 🎯 Proje Hakkında

### Amaç
Bu proje, **Deep Learning**'in temellerini öğretmek ve **PyTorch** framework'ü ile basit bir yapay sinir ağı oluşturmayı amaçlar. El yazısı rakamları tanıyabilen bir model geliştirilir.

### Veri Seti: MNIST
- **60,000** eğitim görüntüsü
- **10,000** test görüntüsü  
- **28x28 piksel** gri tonlama görüntüler
- **10 sınıf**: 0-9 rakamları
- **Klasik benchmark** veri seti

### Temel Özellikler
- ✅ **PyTorch** tabanlı implementasyon
- ✅ **Basit ANN mimarisi** (2 katman)
- ✅ **Otomatik veri indirme**
- ✅ **Görsel sonuç analizi**
- ✅ **Batch processing** optimizasyonu
- ✅ **Eğitim süreci takibi**

## 🔧 Kurulum

### Gerekli Kütüphaneler
```bash
pip install torch torchvision matplotlib
```

### Sistem Gereksinimleri
- **Python**: 3.7+
- **RAM**: Minimum 4GB
- **Disk**: ~100MB (veri seti için)
- **GPU**: Opsiyonel (CPU'da çalışır)

### Dosya Yapısı
```
├── 9_mnistUygulama.py           # Ana uygulama dosyası
├── README_9_mnistUygulama.md    # Bu döküman
└── data/                        # Otomatik oluşturulur (MNIST verileri)
```

## 🚀 Kullanım

### Basit Çalıştırma
```bash
python 9_mnistUygulama.py
```

### Beklenen Çıktı
1. **MNIST veri seti indirme** (ilk çalıştırmada)
2. **5 epoch eğitim süreci** ve kayıp değerleri
3. **10 adet test görseli** ve tahmin sonuçları
4. **Görsel analiz** ekranları

### Program Akışı
1. **Veri yükleme** ve dönüşüm
2. **Model tanımlama** (ANN mimarisi)
3. **Eğitim döngüsü** (5 epoch)
4. **Test ve görselleştirme**

## 🏗️ Model Mimarisi

### Artificial Neural Network (ANN)
```
Input Layer:    784 neurons (28×28 pixels)
                    ↓
Hidden Layer:   128 neurons + ReLU
                    ↓
Output Layer:   10 neurons (0-9 digits)
```

### Katman Detayları

#### 1. Input Layer (Giriş Katmanı)
- **Boyut**: 784 (28×28 piksel düzleştirilmiş)
- **Tür**: Tam bağlantılı (Fully Connected)
- **Fonksiyon**: Görüntüyü vektöre dönüştürme

#### 2. Hidden Layer (Gizli Katman)
- **Boyut**: 128 nöron
- **Aktivasyon**: ReLU (Rectified Linear Unit)
- **Rol**: Özellik öğrenme ve dönüşüm

#### 3. Output Layer (Çıkış Katmanı)
- **Boyut**: 10 nöron (her rakam için 1)
- **Aktivasyon**: Yok (raw logits)
- **Çıkış**: Sınıf skorları

### Model Parametreleri
```python
# Toplam parametre sayısı hesaplama
input_to_hidden = 784 × 128 = 100,352
hidden_bias = 128
hidden_to_output = 128 × 10 = 1,280
output_bias = 10

Toplam = 100,352 + 128 + 1,280 + 10 = 101,770 parametre
```

## 📁 Kod Yapısı

### 1. Kütüphane İmportları
```python
import torch                    # Ana PyTorch
import torch.nn as nn          # Sinir ağı katmanları  
import torch.nn.functional as F # Aktivasyon fonksiyonları
from torchvision import datasets, transforms # Veri seti
import matplotlib.pyplot as plt # Görselleştirme
```

### 2. Veri Hazırlama
```python
# Veri dönüşümü (normalizasyon)
transform = transforms.ToTensor()

# Veri setlerini yükle
train_data = datasets.MNIST(root='data', train=True, download=True, transform=transform)
test_data = datasets.MNIST(root='data', train=False, download=True, transform=transform)
```

### 3. Veri Yükleyiciler
```python
# Batch halinde veri yükleme
train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=10, shuffle=False)
```

### 4. Model Sınıfı
```python
class SimpleANN(nn.Module):
    def __init__(self):
        super(SimpleANN, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)  # İlk katman
        self.fc2 = nn.Linear(128, 10)     # Çıkış katmanı

    def forward(self, x):
        x = x.view(-1, 28*28)             # Flatten
        x = F.relu(self.fc1(x))           # ReLU aktivasyon
        x = self.fc2(x)                   # Çıkış
        return x
```

### 5. Eğitim Döngüsü
```python
for epoch in range(5):
    running_loss = 0.0
    for images, labels in train_loader:
        outputs = model(images)           # Forward pass
        loss = criterion(outputs, labels) # Kayıp hesaplama
        
        optimizer.zero_grad()             # Gradyan temizleme
        loss.backward()                   # Backward pass
        optimizer.step()                  # Parametre güncelleme
        
        running_loss += loss.item()
```

## 📊 Sonuçlar

### Beklenen Performans

| Metrik | Değer |
|--------|--------|
| **Eğitim Süresi** | ~2-5 dakika |
| **Final Loss** | ~0.2-0.4 |
| **Tahmini Doğruluk** | ~95-97% |
| **Epoch Sayısı** | 5 |

### Tipik Eğitim Çıktısı
```
Epoch 1, Loss: 0.4523
Epoch 2, Loss: 0.2156  
Epoch 3, Loss: 0.1598
Epoch 4, Loss: 0.1234
Epoch 5, Loss: 0.0987
```

### Görsel Sonuçlar
Program 10 adet test görseli gösterir:
- ✅ **Doğru tahminler**: Yeşil başlık
- ❌ **Yanlış tahminler**: Kırmızı başlık (nadir)
- 📊 **Karışıklık**: Benzer rakamlar (6-8, 4-9)

## ⚙️ Teknik Detaylar

### PyTorch Özellikleri

#### Tensor İşlemleri
- **view(-1, 28*28)**: 2D görüntüyü 1D vektöre düzleştirme
- **ToTensor()**: PIL/numpy array'i PyTorch tensor'e çevirme
- **Normalizasyon**: [0,1] aralığına ölçekleme

#### Optimizasyon
- **Adam Optimizer**: Adaptif öğrenme oranı
- **Learning Rate**: 0.001 (varsayılan)
- **CrossEntropyLoss**: Çok sınıflı sınıflandırma loss'u

#### Memory Management
- **Batch Size**: 64 (eğitim), 10 (test)
- **torch.no_grad()**: Test sırasında gradyan hesaplamayı kapatma
- **model.eval()**: Dropout vb. katmanları devre dışı bırakma

### Veri İşleme Pipeline
```
Raw Image (PIL) → ToTensor() → Normalize → Flatten → Model → Logits → Prediction
```

## 🎓 Öğrenme Çıktıları

### Teorik Bilgiler
- ✅ **Artificial Neural Network** temelleri
- ✅ **PyTorch framework** kullanımı
- ✅ **Backpropagation** algoritması
- ✅ **Loss fonksiyonları** ve optimizasyon
- ✅ **Batch processing** konsepti
- ✅ **Overfitting/Underfitting** kavramları

### Pratik Beceriler
- ✅ **PyTorch model** tanımlama
- ✅ **MNIST veri seti** kullanımı
- ✅ **Eğitim döngüsü** implementasyonu
- ✅ **Görselleştirme** teknikleri
- ✅ **Model değerlendirmesi**

## 🔍 Program Çıktısı Analizi

### Başarı Kriterleri

**Mükemmel Performans (>%96)**:
- Loss değeri < 0.1
- Çoğu rakam doğru tahmin edilir
- Eğitim süreci stabil

**İyi Performans (%90-96)**:
- Loss değeri 0.1-0.3 arası
- Bazı karmaşık rakamlar karışabilir
- Genel trend azalan

**Geliştirilmesi Gereken (<90%)**:
- Loss değeri > 0.3
- Çok sayıda yanlış tahmin
- Model parametreleri gözden geçirilmeli

### Yaygın Hatalar ve Çözümleri

#### 1. Düşük Doğruluk
**Sebepler**:
- Yetersiz eğitim süresi
- Yanlış öğrenme oranı
- Aşırı basit model mimarisi

**Çözümler**:
- Epoch sayısını artırın
- Learning rate'i ayarlayın (0.01, 0.0001)
- Daha fazla hidden layer ekleyin

#### 2. Overfitting
**Belirtiler**:
- Eğitim loss'u düşer, test loss'u artar
- Eğitim doğruluğu yüksek, test doğruluğu düşük

**Çözümler**:
- Dropout katmanları ekleyin
- L2 regularization kullanın
- Daha fazla eğitim verisi

#### 3. Slow Training
**Sebepler**:
- CPU kullanımı
- Büyük batch size
- Veri yükleme darboğazı

**Çözümler**:
- GPU kullanımını etkinleştirin
- Batch size'ı optimize edin
- num_workers parametresi ayarlayın

## 🛠️ Gelişmiş Özellikler

### GPU Desteği Ekleme
```python
# GPU kontrolü ve model aktarımı
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Veriyi GPU'ya taşıma
for images, labels in train_loader:
    images, labels = images.to(device), labels.to(device)
```

### Validation Set Ekleme
```python
# Eğitim verisini böl
from torch.utils.data import random_split

train_size = int(0.8 * len(train_data))
val_size = len(train_data) - train_size
train_data, val_data = random_split(train_data, [train_size, val_size])
```

### Model Kaydetme
```python
# Eğitimli modeli kaydet
torch.save(model.state_dict(), 'mnist_model.pth')

# Modeli yükle
model = SimpleANN()
model.load_state_dict(torch.load('mnist_model.pth'))
```

### Confusion Matrix
```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Tüm test verisi üzerinde tahmin
all_predicted = []
all_actual = []

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        all_predicted.extend(predicted.numpy())
        all_actual.extend(labels.numpy())

# Confusion matrix çiz
cm = confusion_matrix(all_actual, all_predicted)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('MNIST Confusion Matrix')
plt.show()
```

## 📚 İleri Seviye Konular

### Model İyileştirmeleri

#### 1. Daha Derin Ağ
```python
class DeepANN(nn.Module):
    def __init__(self):
        super(DeepANN, self).__init__()
        self.fc1 = nn.Linear(28*28, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 10)
        self.dropout = nn.Dropout(0.2)
        
    def forward(self, x):
        x = x.view(-1, 28*28)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x
```

#### 2. Learning Rate Scheduling
```python
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

for epoch in range(epochs):
    # ... eğitim kodu
    scheduler.step()  # Her epoch sonunda learning rate güncelle
```

#### 3. Early Stopping
```python
best_val_loss = float('inf')
patience = 5
counter = 0

for epoch in range(epochs):
    # ... eğitim ve validasyon
    
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        counter = 0
        torch.save(model.state_dict(), 'best_model.pth')
    else:
        counter += 1
        
    if counter >= patience:
        print("Early stopping!")
        break
```

## 📈 Alternatif Yaklaşımlar

### Convolutional Neural Network (CNN)
```python
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)
```

### Transfer Learning
```python
import torchvision.models as models

# Önceden eğitilmiş model kullanımı
model = models.resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, 10)
```

## 🎯 Proje Genişletme Fikirleri

### Başlangıç Seviyesi
1. **Batch size optimizasyonu**: Farklı değerler deneyin
2. **Epoch sayısı**: Daha uzun eğitim süreleri
3. **Hyperparameter tuning**: Learning rate, hidden size

### Orta Seviye
1. **Validation set**: Model performansını daha iyi değerlendirin
2. **Data augmentation**: Görüntü döndürme, kaydırma
3. **Regularization**: L1, L2, Dropout teknikleri

### İleri Seviye
1. **CNN implementasyonu**: Konvolüsyonel katmanlar
2. **Ensemble methods**: Birden fazla model kombinasyonu
3. **Adversarial examples**: Modelin güçlü yanlarını test etme

## 🔗 İlgili Kaynaklar

### Resmi Dokümantasyon
- [PyTorch Documentation](https://pytorch.org/docs/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- [torchvision.datasets](https://pytorch.org/vision/stable/datasets.html)

### Eğitim Materyalleri
- [Deep Learning with PyTorch](https://pytorch.org/tutorials/)
- [Neural Networks Explained](https://www.3blue1brown.com/topics/neural-networks)
- [CS231n Stanford Course](http://cs231n.stanford.edu/)

### Pratik Kaynaklar
- [PyTorch Examples](https://github.com/pytorch/examples)
- [MNIST Benchmarks](https://paperswithcode.com/sota/image-classification-on-mnist)

## 🏆 Başarı Metrikleri ve Benchmarklar

### MNIST State-of-the-Art
| Model | Doğruluk | Yıl |
|-------|----------|-----|
| **Bu Proje (ANN)** | ~97% | 2024 |
| **LeNet-5** | 99.05% | 1998 |
| **Modern CNN** | >99.5% | 2010+ |
| **Ensemble Methods** | >99.8% | 2015+ |

### Performance Karşılaştırması
```
Basit ANN:     ~97%    (Bu proje)
CNN:           ~99%    (Önerilen upgrade)
ResNet:        ~99.5%  (Transfer learning)
Ensemble:      ~99.8%  (Çoklu model)
```

---

**🔗 İlgili Projeler**: 
- `6_destekvektor_iris.py` - SVM Sınıflandırma
- `7_kMeans_iris.py` - Unsupervised Learning
- `8_kMeans_kDegerSecimi.py` - Hyperparameter Tuning

**📧 İletişim**: BTK Atölye Multimedya Güvenliği Projesi kapsamında hazırlanmıştır.

**🏷️ Etiketler**: #DeepLearning #ANN #PyTorch #MNIST #ImageClassification #NeuralNetworks #MachineLearning #Python

**⭐ Zorluk Seviyesi**: Orta | **⏱️ Tahmini Süre**: 45-60 dakika | **👥 Hedef Kitle**: ML öğrencileri, deep learning başlangıç