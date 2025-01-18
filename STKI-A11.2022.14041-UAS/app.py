import streamlit as st
import pandas
import pickle
import numpy as np

import os

# Load the dataset
data_file = 'https://raw.githubusercontent.com/Dotbima6/Data-Mining/edit/main/STKI-A11.2022.14041-UAS/heart.csv'
data = pd.read_csv(data_file)

# Judul Aplikasi
st.title("Aplikasi Prediksi Kemungkinan Penyakit Jantung")

# Penjelasan Singkat
st.markdown("""
Aplikasi ini menggunakan model **Random Forest** untuk memprediksi risiko penyakit jantung berdasarkan data medis pasien. 
Masukkan data Anda di bawah ini, dan klik **Predict** untuk melihat hasil prediksi.
""")

# Input User
st.sidebar.header("Masukan Fitur")
def user_input_features():
    age = st.sidebar.slider("Usia", 20, 80, 50)
    sex = st.sidebar.selectbox("Jenis Kelamin (0 = Female, 1 = Male)", [0, 1])
    cp = st.sidebar.selectbox("Jenis/Tingkat Nyeri Dada (1-4)", [1, 2, 3, 4])
    trestbps = st.sidebar.slider("Tekanan Darah Saat Istirahat (mm Hg)", 90, 200, 120)
    chol = st.sidebar.slider("Kolesterol (mg/dL)", 100, 400, 200)
    fbs = st.sidebar.selectbox("Gula Darah Puasa > 120 mg/dL (1 = Yes, 0 = No)", [0, 1])
    restecg = st.sidebar.selectbox("Hasil electrocardiogram (ECG) saat istirahat (0-2)", [0, 1, 2])
    thalach = st.sidebar.slider("Denyut Jantung Maksimum Tercapai", 70, 220, 150)
    exang = st.sidebar.selectbox("Nyeri Dada Setelah Olahraga (1 = Yes, 0 = No)", [0, 1])
    oldpeak = st.sidebar.slider("Depresi ST yang Diakibatkan Karena Olahraga", 0.0, 6.0, 1.0, step=0.1)
    slope = st.sidebar.selectbox("Elevasi Puncak Latihan segmen-ST (0-2)", [0, 1, 2])
    ca = st.sidebar.selectbox("Jenis Pembuluh Darah Besar (0-4)", [0, 1, 2, 3, 4])
    thal = st.sidebar.selectbox("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", [1, 2, 3])

    data = {
        "age": age, "sex": sex, "cp": cp, "trestbps": trestbps,
        "chol": chol, "fbs": fbs, "restecg": restecg, "thalach": thalach,
        "exang": exang, "oldpeak": oldpeak, "slope": slope, "ca": ca, "thal": thal
    }
    features = np.array(list(data.values())).reshape(1, -1)
    return features

input_features = user_input_features()

# Prediksi
if st.button("Predict"):
    prediction = model.predict(input_features)
    prediction_prob = model.predict_proba(input_features)
    if prediction[0] == 1:
        st.success("The model predicts that the patient is at **high risk** of heart disease.")
    else:
        st.success("The model predicts that the patient is at **low risk** of heart disease.")
    
    st.subheader("Prediction Probability")
    st.write(f"Low Risk: {prediction_prob[0][0]*100:.2f}%")
    st.write(f"High Risk: {prediction_prob[0][1]*100:.2f}%")
