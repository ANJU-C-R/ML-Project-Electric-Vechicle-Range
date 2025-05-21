import streamlit as st
import numpy as np
import pickle
import base64

# --- Set Streamlit page configuration ---
st.set_page_config(page_title="Electric Vehicle Range Predictor", layout="centered")

# --- Function to set a background image with dark overlay ---
def set_background_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(0, 0, 0, 0.6), 
                rgba(0, 0, 0, 0.6)
            ), url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        .title-style {{
            font-size: 40px;
            font-weight: bold;
            color: white;
            text-align: center;
            padding: 20px 0;
        }}
        .stMarkdown > div {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Load the model ---
with open('electric_vehicle.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# --- Load the encoders ---
encoders = {}
object_columns = [
    'VIN (1-10)', 'County', 'City', 'Make', 'Model',
    'Electric Vehicle Type', 'CAFV Eligibility', 'Vehicle Location', 'Electric Utility'
]
for col in object_columns:
    with open(f'{col}_encoder.pkl', 'rb') as f:
        encoders[col] = pickle.load(f)

# --- Set background ---
set_background_from_local("Tesla.jpg")

# --- Title ---
st.markdown('<div class="title-style">🔋 Electric Vehicle Range Predictor</div>', unsafe_allow_html=True)
st.write('Provide vehicle details to predict the electric driving range.')

# --- Sidebar Inputs ---
st.sidebar.header('Input Features')

vin = st.sidebar.text_input('VIN (1-10)')
county = st.sidebar.text_input('County')
city = st.sidebar.text_input('City')
make = st.sidebar.text_input('Make')
model_name = st.sidebar.text_input('Model')  # Avoid 'model' name conflict
ev_type = st.sidebar.text_input('Electric Vehicle Type')
cafv_eligibility = st.sidebar.text_input('CAFV Eligibility')
legislative_district = st.sidebar.number_input('Legislative District', min_value=1.0, value=1.0)
vehicle_location = st.sidebar.text_input('Vehicle Location')
electric_utility = st.sidebar.text_input('Electric Utility')

# --- Transform function ---
def transform_input(data_dict):
    transformed_data = []
    for col, value in data_dict.items():
        if col in encoders:
            try:
                encoded_value = encoders[col].transform([value])[0]
            except:
                encoded_value = 0  # or a default/fallback if unseen
            transformed_data.append(encoded_value)
        else:
            transformed_data.append(value)
    return np.array(transformed_data).reshape(1, -1)  # 2D input for prediction

# --- Prediction ---
if st.sidebar.button('Predict Range'):
    input_data = {
        'VIN (1-10)': vin,
        'County': county,
        'City': city,
        'Make': make,
        'Model': model_name,
        'Electric Vehicle Type': ev_type,
        'CAFV Eligibility': cafv_eligibility,
        'Legislative District': legislative_district,
        'Vehicle Location': vehicle_location,
        'Electric Utility': electric_utility
    }

    transformed_data = transform_input(input_data)

    prediction = loaded_model.predict(transformed_data)

    st.markdown(
        f"""
        <div style="background-color: rgba(255, 255, 255, 0.15);
                    padding: 15px;
                    border-radius: 10px;
                    text-align: center;
                    color: white;
                    font-size: 20px;
                    font-weight: bold;
                    margin-top: 20px;">
            Predicted Electric Range: {prediction[0]:.2f} km
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Sidebar note ---
st.sidebar.markdown("---")
st.sidebar.write("Note: Categorical inputs are automatically encoded using training data.")

