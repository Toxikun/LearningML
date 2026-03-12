# İstanbul Apartment Rent Prediction (Learning ML)

[English](#english) | [Türkçe](#türkçe)

---

<a name="english"></a>
## 🇬🇧 English

This project is a comprehensive Machine Learning study aimed at predicting apartment rental prices in Istanbul. It was developed to explore and compare different ML algorithms, from basic regression to advanced ensemble methods.

### 🚀 Key Features

*   **Two-Stage Learning Path:**
    *   **First Model:** A fundamental approach using Linear Regression and Random Forest. Focuses on core data handling and basic scatter plot visualizations.
    *   **Second Model:** An advanced implementation utilizing **XGBoost Regressor**, **K-Means Clustering** for segmentation, and sophisticated Feature Engineering (interaction terms, ratios).
*   **Deployment:** A web application built with **Streamlit** for real-time price predictions.
*   **Success Metrics:** The advanced model achieves approximately **63% R² score** on test data.

### 📈 Model Progression & Learning Journey

The development followed an iterative path, focusing on performance gains and avoiding common pitfalls like data leakage.

**First Model (Initial Learning):**
*   Started with a baseline R² of **0.22** (Linear Regression).
*   Improved to **0.43** through data cleaning.
*   Reached **0.54** by switching to Random Forest Regressor.

**Second Model (Advanced Optimization):**
*   Baseline: **0.59** -> **0.60** (XGBoost introduction).
*   ⚠️ **Data Leakage Check:** Hit **0.99** at one point. Identified as data leakage (using future information/target-related features). **Reverted** to maintain integrity.
*   Stable gain: reached **0.62**.
*   ⚠️ **Anomaly Check:** Hit **0.94** again. Re-evaluated and **reverted** due to overfitting/leakage suspicions.
*   **Final Stable Path:** **63.16** -> **63.26** (Current Version).


### 🛠 Tech Stack

*   **Logic:** Python (Pandas, NumPy, Scikit-learn, XGBoost)
*   **Visualization:** Matplotlib, Seaborn
*   **Deployment:** Streamlit
*   **Storage:** Pickle (for model serialization)

### 📂 File Structure

*   `first_model.ipynb`: Introductory regression analysis.
*   `second_model.ipynb`: Advanced feature engineering and XGBoost model.
*   `app.py`: Streamlit web application.
*   `istanbulApartmentForRent.csv`: Historical rental price dataset.

### 💻 How to Run

1.  **Install dependencies:**
    ```bash
    pip install pandas numpy scikit-learn xgboost matplotlib seaborn streamlit
    ```
2.  **Run the web app:**
    ```bash
    streamlit run app.py
    ```

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

Bu proje, İstanbul'daki daire kira fiyatlarını tahmin etmeyi amaçlayan kapsamlı bir Makine Öğrenmesi çalışmasıdır. Temel regresyondan ileri seviye topluluk yöntemlerine kadar farklı algoritmaları deneyimlemek amacıyla geliştirilmiştir.

### 🚀 Öne Çıkan Özellikler

*   **İki Aşamalı Öğrenme Süreci:**
    *   **First Model (Birinci Model):** Doğrusal Regresyon ve Random Forest kullanan temel yaklaşım. Veri işleme ve temel görselleştirme odaklıdır.
    *   **Second Model (İkinci Model):** **XGBoost Regressor**, **K-Means Kümeleme** (segmentasyon için) ve gelişmiş **Özellik Mühendisliği** (etkileşim terimleri, oranlar) içeren profesyonel yaklaşım.
*   **Canlı Uygulama:** Gerçek zamanlı tahminler için **Streamlit** ile geliştirilmiş kullanıcı arayüzü.
*   **Başarı Oranı:** Gelişmiş model, test verileri üzerinde yaklaşık **%63 R² skoru** elde etmiştir.

### 📈 Model Gelişim Süreci ve Öğrenimler

Geliştirme süreci, performans artışı sağlamak ve "data leakage" (veri sızıntısı) gibi hatalardan kaçınmak için iteratif bir yol izlemiştir.

**First Model (İlk Denemeler):**
*   **0.22** R² skoru ile başlandı (Doğrusal Regresyon).
*   Veri temizliği ile **0.43**'e yükseltildi.
*   Random Forest Regressor'a geçilerek **0.54** başarıya ulaşıldı.

**Second Model (İleri Seviye):**
*   XGBoost girişiyle **0.59** -> **0.60** seviyelerine gelindi.
*   ⚠️ **Veri Sızıntısı Deneyimi:** Bir noktada **0.99** skoru görüldü. Bunun veri sızıntısından (hedef değişkenle doğrudan ilişkili hatalı özellik kullanımı) kaynaklandığı tespit edildi ve **geri alındı**.
*   Kararlı artış: **0.62**'ye ulaşıldı.
*   ⚠️ **Hatalı Artış:** Tekrar **0.94** skoru görüldü, aşırı öğrenme (overfitting) veya sızıntı şüphesiyle tekrar **geri alındı**.
*   **Final Kararlı Sürüm:** **63.16** -> **63.26** (Mevcut en iyi versiyon).


### 🛠 Teknolojiler

*   **Mantık:** Python (Pandas, NumPy, Scikit-learn, XGBoost)
*   **Görselleştirme:** Matplotlib, Seaborn
*   **Dağıtım:** Streamlit
*   **Depolama:** Pickle

### 📂 Dosya Yapısı

*   `first_model.ipynb`: Temel regresyon analizi.
*   `second_model.ipynb`: İleri özellik mühendisliği ve XGBoost modeli.
*   `app.py`: Streamlit web uygulaması arayüzü.
*   `istanbulApartmentForRent.csv`: Tarihsel kira verisi seti.

### 💻 Çalıştırma

1.  **Gereksinimleri yükleyin:**
    ```bash
    pip install pandas numpy scikit-learn xgboost matplotlib seaborn streamlit
    ```
2.  **Uygulamayı başlatın:**
    ```bash
    streamlit run app.py
    ```
