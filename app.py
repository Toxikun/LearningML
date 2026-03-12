import streamlit as st
import pandas as pd
import pickle

try:
    with open("63_percent_final_model.pkl", "rb") as f:
        pack = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please ensure '63_percent_final_model.pkl' is in the same directory.")
    st.stop()

st.set_page_config(page_title="AI Real Estate Predictor", page_icon="🏢", layout="centered")

st.title("🏢 Istanbul Apartment Rent Predictor")
st.markdown("""
This AI tool predicts monthly apartment rents in Istanbul based on physical characteristics. 
*Powered by **XGBoost** with a **63.26% R² Score**.*
""")
st.divider()

st.subheader("Apartment Features")
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Living Area (m²)", min_value=10, max_value=500, value=100, step=5)
    age = st.number_input("Building Age", min_value=0, max_value=100, value=5, step=1)

with col2:
    room = st.slider("Number of Rooms", min_value=1, max_value=6, value=3)

if st.button("Predict Rental Price", use_container_width=True):

    input_data = pd.DataFrame([[
        area, 
        age, 
        room, 
        area / room, 
        area / (age + 1), 
        age * area, 
        room / area
    ]], columns=pack["features"])
    
  
    segment = pack["kmeans"].predict(input_data[['area (m2)', 'age', 'room']])[0]
    input_data['segment'] = segment
    
    prediction = pack["model"].predict(input_data)[0]
    
    
    st.divider()
    st.metric(label="Estimated Monthly Rent", value=f"{prediction:,.0f} TRY")
    
    with st.expander("View Model Analysis"):
        st.write(f"**Calculated Segment:** {segment}")
        st.write(f"**Model Confidence:** 63.26%")
        st.info("Note: Predictions are based on physical features and do not include specific neighborhood premium or luxury finishes.")

st.markdown("---")
st.caption("Developed by Ahmet Orkun Yılmaz | 2026 AI Project")