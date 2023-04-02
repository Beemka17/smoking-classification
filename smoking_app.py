import pickle
import streamlit as st

smoking_model = pickle.load(open('smoking_model.sav','rb'))

st.title('Prediksi Perilaku Merokok Berdasarkan Kondisi Kesehatan')

col1, col2=st.columns(2)
with col1:
    gender = st.number_input ('Input Gender pasien (M = 1 / F = 0)')
with col2 :
    age = st.number_input('Input Umur Pasien')
with col1 :
    height = st.number_input('Input Tinggi Pasien :')
with col2 :
    weight = st.number_input('Input Berat Pasien :')
with col1 :
    waist = st.number_input('Input Ukuran Pinggang Pasien :')
with col2 :
    eyesight_left = st.number_input('Input Penglihatan Mata Kiri :')
with col1 :
    eyesight_right = st.number_input('Input Penglihatan Mata Kanan :')
with col2 :
    hearing_left = st.number_input('Input Pendengaran Telinga Kiri :')
with col1 :
    hearing_right = st.number_input('Input Pendengaran Telinga Kanan :')
with col2 :
    systolic = st.number_input('Input Nilai Systolic :')
with col1 :
    relaxation = st.number_input('Input Nilai Relaxation :')
with col2 :
    fasting_blood_sugar = st.number_input('Input Hasil Cek Glukosa Puasa :')
with col1 :
    cholesterol = st.number_input('Input Hasil Cek Kolesterol :')
with col2 :
    triglyceride = st.number_input('Input Nilai triglyceride :')
with col1 :
    hdl = st.number_input('Input Nilai HDL :')
with col2 :
    ldl = st.number_input('Input Nilai LDL :')
with col1 :
    hemoglobin = st.number_input('Input Nilai Hemogoblin :')
with col2 :
    urine_protein = st.number_input('Input Nilai Protein Urine :')
with col1 :
    serum_creatinine = st.number_input('Input Nilai Erum Creatinine :')
with col2 :
    ast = st.number_input('Input Nilai AST :')
with col1 :
    alt = st.number_input('Input Nilai ALT :')
with col2 :
    gtp = st.number_input('Input Nilai GTP :')
with col1 :
    oral = st.number_input('Input Status Oral : (Jika Ya = 1 / Jika Tidak = 0)')
with col2 :
    dental_caries = st.number_input('Apakah Gigi Berlubang? Jika Ya = 1 / Jika Tidak = 0')
with col1 :
    tartar = st.number_input('Apakah Meng-Konsumsi Tartar? Jika Ya = 1 / Jika Tidak = 0')

smoking_diagnosis = ''

if st.button('Test Perilaku Merokok Pasien') :
    smoking_prediction = smoking_model.predict([[gender,age,height,weight,waist,eyesight_left,eyesight_right,hearing_left,hearing_right,systolic,relaxation,fasting_blood_sugar,cholesterol,triglyceride,hdl,ldl,hemoglobin,urine_protein,serum_creatinine,ast,alt,gtp,oral,dental_caries,tartar]])

    if(smoking_prediction[0] == 0):
        smoking_diagnosis = 'Pasien Bukan Perokok'
    else :
        smoking_diagnosis = 'Pasien Perokok'

    st.success(smoking_diagnosis)