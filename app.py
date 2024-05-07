import streamlit as st
import numpy as np
import pickle

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

main_bg = "linear-gradient(to bottom, #ff7e5f, #feb47b)"  # Gradient background color
sidebar_bg = "#feb47b"  # Sidebar background color
st.markdown(
    f"""
    <style>
        body {{
            background: {main_bg};
            color: white;
        }}
        .sidebar .sidebar-content {{
            background: {sidebar_bg};
            color: white;
        }}
        h1 {{
            color: #ff5733; /* Change color of h1 heading */
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# Title and disclaimer
st.markdown("<h1 style='text-align: center; color: #ff5733;'>PCOS Disease Predictor</h1>", unsafe_allow_html=True)


# Input features
st.header('Questionnaire')
age = st.number_input('Enter your Age (years)', min_value=0, max_value=120)
weight = st.number_input('Enter your Weight (Kg)', min_value=0.0)
bmi = st.number_input('Enter your BMI', min_value=0.0)
cycle = st.radio('Is your Cycle Regular or Irregular?', ['Regular', 'Irregular'])
cycle_length = st.number_input('Enter your Cycle length (days)', min_value=0)
marriage_status = st.number_input('Enter your Marriage Status (years)', min_value=0)
beta_HCG = st.number_input('Enter your I beta-HCG (mIU/mL)', min_value=0.0)
FSH = st.number_input('Enter your FSH (mIU/mL)', min_value=0.0)
LH = st.number_input('Enter your LH (mIU/mL)', min_value=0.0)
FSH_LH = st.number_input('Enter your FSH/LH', min_value=0.0)
vit_d3 = st.number_input('Enter your Vit D3 (ng/mL)', min_value=0.0)
PRG = st.number_input('Enter your PRG (ng/mL)', min_value=0.0)
weight_gain = st.radio('Have you experienced Weight gain? (Yes/No)', ['Yes', 'No'])
hair_growth = st.radio('Have you experienced Hair growth? (Yes/No)', ['Yes', 'No'])
skin_darkening = st.radio('Have you experienced Skin darkening? (Yes/No)', ['Yes', 'No'])
hair_loss = st.radio('Have you experienced Hair loss? (Yes/No)', ['Yes', 'No'])
pimples = st.radio('Have you experienced Pimples? (Yes/No)', ['Yes', 'No'])
fast_food = st.radio('Do you consume Fast food? (Yes/No)', ['Yes', 'No'])
follicle_L = st.number_input('Enter your Follicle No. (L)', min_value=0)
follicle_R = st.number_input('Enter your Follicle No. (R)', min_value=0)

# Convert categorical inputs to numerical
cycle = 1 if cycle == 'Regular' else 0
weight_gain = 1 if weight_gain == 'Yes' else 0
hair_growth = 1 if hair_growth == 'Yes' else 0
skin_darkening = 1 if skin_darkening == 'Yes' else 0
hair_loss = 1 if hair_loss == 'Yes' else 0
pimples = 1 if pimples == 'Yes' else 0
fast_food = 1 if fast_food == 'Yes' else 0

# Prediction button
if st.button('Predict', key='predict_button'):
    # Make prediction
    input_data = np.array([[age, weight, bmi, cycle, cycle_length, marriage_status, beta_HCG, FSH, LH, FSH_LH, vit_d3, PRG, weight_gain, hair_growth, skin_darkening, hair_loss, pimples, fast_food, follicle_L, follicle_R]])
    prediction = model.predict(input_data)

    # Display prediction
    st.subheader('Prediction')
    if prediction[0] == 1:
        st.markdown("<h2 style='color: red;'>The model predicts that you may have PCOS.</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color: green;'>The model predicts that you may not have PCOS.</h2>", unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #f9f9f9; padding: 10px; border-radius: 10px;'>
        <p style='color: #333333; font-size: 16px;'><b>Disclaimer:</b> This app provides a prediction of the likelihood of a person having PCOS based on their inputs. It is not a substitute for professional medical advice. Please consult a doctor or healthcare professional for medical advice and diagnosis.</p>
    </div>
""", unsafe_allow_html=True)
