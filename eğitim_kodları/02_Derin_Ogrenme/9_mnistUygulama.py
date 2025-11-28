# Gerekli kütüphanelerin yüklenmesi
import torch                             # PyTorch ana kütüphanesi
import torch.nn as nn                    # Sinir ağı katmanları ve yapıları için modül
import torch.nn.functional as F          # Aktivasyon fonksiyonları ve benzeri işlemler
from torchvision import datasets, transforms  # Görsel veri setleri ve dönüşüm işlemleri
import matplotlib.pyplot as plt          # Görselleştirme için matplotlib kütüphanesi

# Görselleri tensöre dönüştüren dönüşüm tanımı (veriyi normalize eder)
transform = transforms.ToTensor()

# MNIST eğitim veri setini indir ve dönüşümü uygula
train_data = datasets.MNIST(root='data', train=True, download=True, transform=transform)

# MNIST test veri setini indir ve dönüşümü uygula
test_data = datasets.MNIST(root='data', train=False, download=True, transform=transform)

# Eğitim verilerini mini-batch'ler halinde yükle (batch_size = 64, karıştırma açık)
train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)

# Test verilerini mini-batch'ler halinde yükle (batch_size = 10, sabit sıra)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=10, shuffle=False)

# Basit bir yapay sinir ağı (ANN) sınıfı tanımı
class SimpleANN(nn.Module):
    def __init__(self):
        super(SimpleANN, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)  # Giriş katmanı: 784 giriş (28x28 piksel), 128 çıkış
        self.fc2 = nn.Linear(128, 10)     # Çıkış katmanı: 128 giriş, 10 çıkış (0-9 sınıfları)

    def forward(self, x):
        x = x.view(-1, 28*28)             # 2D görseli 1D vektöre düzleştir
        x = F.relu(self.fc1(x))           # İlk katmanı geç, ReLU aktivasyonu uygula
        x = self.fc2(x)                   # Çıkış katmanını geç (logit skorları üretir)
        return x

# Model nesnesini oluştur
model = SimpleANN()

# Kayıp fonksiyonu: Çok sınıflı sınıflandırma için uygundur (Cross Entropy Loss)
criterion = nn.CrossEntropyLoss()

# Optimizasyon algoritması: Adam kullanılıyor (öğrenme oranı 0.001)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Eğitim döngüsü (5 epoch boyunca modeli eğit)
for epoch in range(5):
    running_loss = 0.0                              # Epoch başında toplam kayıp sıfırlanır
    for images, labels in train_loader:            # Eğitim verisinde batch'ler üzerinde dön
        outputs = model(images)                    # Modelden tahmin edilen sonuçları al
        loss = criterion(outputs, labels)          # Gerçek etiketlerle tahminleri karşılaştır

        optimizer.zero_grad()                      # Önceki gradyanları temizle
        loss.backward()                            # Geri yayılım ile gradyanları hesapla
        optimizer.step()                           # Ağırlıkları gradyanlara göre güncelle

        running_loss += loss.item()                # Toplam kayba bu batch'in kaybını ekle

    # Her epoch sonunda ortalama kaybı yazdır
    print(f"Epoch {epoch+1}, Loss: {running_loss / len(train_loader):.4f}")

# Test verisinden bir batch al (10 örnek)
dataiter = iter(test_loader)
images, labels = next(dataiter)

# Modeli değerlendirme moduna geçir (dropout vb. devre dışı)
model.eval()

# Tahmin yaparken gradyan hesaplanmasın (hesaplama yükünü azaltır)
with torch.no_grad():
    outputs = model(images)                       # Test görselleri ile model tahmini al

# En yüksek logit skoruna sahip indeks: tahmin edilen sınıf
_, predicted = torch.max(outputs, 1)

# Tahmin edilen sonuçları görsel olarak göster (ilk 10 örnek)
for i in range(10):
    plt.imshow(images[i].squeeze(), cmap='gray') # Görüntüyü 2D hale getir ve gri tonda göster
    plt.title(f"Tahmin: {predicted[i].item()}, Gerçek: {labels[i].item()}") # Başlık: Tahmin vs Gerçek
    plt.axis('off')                              # Eksenleri gizle
    plt.show()                                   # Görseli ekranda göster
