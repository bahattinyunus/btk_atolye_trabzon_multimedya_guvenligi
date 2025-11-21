import streamlit as st
import sys
import os
import torch

# Proje kök dizinini path'e ekle
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, "multimedya-guvenligi-ai")
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.inference.predict_deepfake import predict_video
from src.training.train_deepfake import train

st.set_page_config(page_title="Multimedya Güvenliği AI", layout="wide")

st.title("🛡️ Multimedya Güvenliği AI Platformu")

tabs = st.tabs(["🕵️ Deepfake Analizi", "🎓 Model Eğitimi"])

# --- Tab 1: Deepfake Analizi ---
with tabs[0]:
    st.header("Deepfake Video/Görüntü Analizi")
    st.markdown("Bu modül, yüklenen medyanın **Deepfake** olup olmadığını analiz eder.")

    uploaded_file = st.file_uploader("Analiz edilecek dosyayı yükleyin (Video veya Resim)", type=["mp4", "avi", "jpg", "png"])

    if st.button("Analizi Başlat"):
        with st.spinner("Analiz yapılıyor..."):
            # Şu anki dummy implementasyon dosya içeriğini kullanmıyor ama
            # gerçek senaryoda dosya path'i fonksiyona verilir.
            score = predict_video()
            
            st.success("Analiz Tamamlandı!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Deepfake Skoru", value=f"{score:.4f}")
            
            with col2:
                if score > 0.5:
                    st.error("⚠️ TESPİT: Bu medyanın SAHTE (Deepfake) olma ihtimali yüksek!")
                else:
                    st.success("✅ TESPİT: Bu medya GERÇEK görünüyor.")

# --- Tab 2: Model Eğitimi ---
with tabs[1]:
    st.header("Model Eğitimi Simülasyonu")
    st.markdown("Mevcut veri seti üzerinde modeli yeniden eğitin.")

    col1, col2 = st.columns(2)
    with col1:
        epochs = st.slider("Epoch Sayısı", min_value=1, max_value=10, value=1)
    with col2:
        lr = st.number_input("Learning Rate", value=0.001, format="%.4f")

    if st.button("Eğitimi Başlat"):
        st.info(f"Eğitim başlatılıyor... (Epochs: {epochs}, LR: {lr})")
        
        # Konsol çıktısını yakalamak için basit bir yöntem kullanılabilir ama
        # şimdilik sadece fonksiyonu çağırıp sonucu ekrana basacağız.
        # train fonksiyonu şu an print yapıyor, bunu UI'da göstermek için
        # stdout'u redirect edebiliriz veya fonksiyonu değiştirebiliriz.
        # Basitlik adına şimdilik sadece çalıştırıyoruz.
        
        with st.spinner("Model eğitiliyor..."):
            try:
                train(num_epochs=epochs, lr=lr)
                st.success("Eğitim başarıyla tamamlandı!")
            except Exception as e:
                st.error(f"Eğitim sırasında hata oluştu: {e}")
