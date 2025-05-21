# # import streamlit as st
# # import pandas as pd

# # # Load the dataset from a CSV file or the notebook (you can modify this part)
# # @st.cache_data
# # def load_data():
# #     return pd.read_csv("Electric_Vehicle_Population_Data.csv")  # Replace with your actual data source

# # df = load_data()

# # st.title("Electric Vehicle Range Predictor")

# # # Display dataset
# # if st.checkbox("Show dataset"):
# #     st.write(df)

# # # Fetch a row by index
# # st.subheader("Fetch a row by index")
# # index = st.number_input("Enter index (starting from 0)", min_value=0, max_value=len(df)-1, step=1)
# # if st.button("Get Row"):
# #     st.write(df.iloc[index])

# # # Fetch rows by condition
# # st.subheader("Fetch row by condition")
# # column = st.selectbox("Select column", df.columns)
# # value = st.text_input("Enter value to match")

# # if st.button("Filter Row(s)"):
# #     filtered = df[df[column].astype(str) == value]
# #     st.write(filtered)













# # import streamlit as st
# # import numpy as np
# # import pickle

# # # Load the model
# # with open('electric_vehicle.pkl', 'rb') as f:
# #     model = pickle.load(f)

# # # Title
# # st.title('Electric Vehicle Range Predictor 🔋🚗')
# # st.write('Provide vehicle details to predict the electric driving range.')

# # # Sidebar inputs
# # st.sidebar.header('Input Features')

# # # Collect user input features into variables
# # postal_code = st.sidebar.number_input('Postal Code', min_value=0, value=98001)
# # model_year = st.sidebar.number_input('Model Year', min_value=1990, max_value=2025, value=2020)
# # county = st.sidebar.number_input('County (Encoded)', min_value=0, value=0)
# # city = st.sidebar.number_input('City (Encoded)', min_value=0, value=0)
# # make = st.sidebar.number_input('Make (Encoded)', min_value=0, value=0)
# # model_car = st.sidebar.number_input('Model (Encoded)', min_value=0, value=0)
# # ev_type = st.sidebar.number_input('Electric Vehicle Type (Encoded)', min_value=0, value=0)
# # cafv_eligibility = st.sidebar.number_input('CAFV Eligibility (Encoded)', min_value=0, value=0)
# # electric_utility = st.sidebar.number_input('Electric Utility (Encoded)', min_value=0, value=0)
# # census_tract = st.sidebar.number_input('2020 Census Tract', min_value=0.0, value=0.0)

# # # Predict button
# # if st.sidebar.button('Predict Range'):
# #     input_data = np.array([[postal_code, model_year, county, city, make, model_car, ev_type, cafv_eligibility, electric_utility, census_tract]])
    
# #     # Predict
# #     prediction = model.predict(input_data)
    
# #     # Show result
# #     st.success(f"Predicted Electric Range: **{prediction[0]:.2f} km**")

# # st.sidebar.markdown("---")
# # st.sidebar.write("Note: Some features are encoded numerically as per training data.")







# # # import streamlit as st
# # # import numpy as np
# # # import pickle

# # # # Set page config
# # # st.set_page_config(page_title="Electric Vehicle Range Predictor", layout="centered")

# # # # Background Image via URL
# # # page_bg_img = """
# # # <style>
# # # [data-testid="stAppViewContainer"] {
# # # background-image: url(""C:\Oct_Batch_ml\Project\Tesla.jpg"");
# # # background-size: cover;
# # # background-position: center;
# # # background-repeat: no-repeat;
# # # background-attachment: fixed;
# # # }
# # # [data-testid="stSidebar"] {
# # # background-color: rgba(255, 255, 255, 0.8);
# # # }
# # # </style>
# # # """

# # # st.markdown(page_bg_img, unsafe_allow_html=True)

# # # # Load the model
# # # with open('electric_vehicle.pkl', 'rb') as f:
# # #     model = pickle.load(f)

# # # # Title
# # # st.title('🔋 Electric Vehicle Range Predictor')
# # # st.write('Provide vehicle details to predict the electric driving range.')

# # # # Sidebar inputs
# # # st.sidebar.header('Input Features')

# # # # Collect user input features into variables
# # # postal_code = st.sidebar.number_input('Postal Code', min_value=0, value=98001)
# # # model_year = st.sidebar.number_input('Model Year', min_value=1990, max_value=2025, value=2020)
# # # county = st.sidebar.number_input('County (Encoded)', min_value=0, value=0)
# # # city = st.sidebar.number_input('City (Encoded)', min_value=0, value=0)
# # # make = st.sidebar.number_input('Make (Encoded)', min_value=0, value=0)
# # # model_car = st.sidebar.number_input('Model (Encoded)', min_value=0, value=0)
# # # ev_type = st.sidebar.number_input('Electric Vehicle Type (Encoded)', min_value=0, value=0)
# # # cafv_eligibility = st.sidebar.number_input('CAFV Eligibility (Encoded)', min_value=0, value=0)
# # # electric_utility = st.sidebar.number_input('Electric Utility (Encoded)', min_value=0, value=0)
# # # census_tract = st.sidebar.number_input('2020 Census Tract', min_value=0.0, value=0.0)

# # # # Predict button
# # # if st.sidebar.button('Predict Range'):
# # #     input_data = np.array([[postal_code, model_year, county, city, make, model_car, ev_type, cafv_eligibility, electric_utility, census_tract]])
    
# # #     # Predict
# # #     prediction = model.predict(input_data)
    
# # #     # Show result
# # #     st.success(f"Predicted Electric Range: **{prediction[0]:.2f} km**")

# # # st.sidebar.markdown("---")
# # # st.sidebar.write("Note: Some features are encoded numerically as per training data.")






# # import streamlit as st
# # import numpy as np
# # import pickle
# # import base64

# # # --- Set Streamlit page configuration ---
# # st.set_page_config(page_title="Electric Vehicle Range Predictor", layout="centered")

# # # --- Function to set a background image from a local file ---
# # def set_background_from_local(image_file):
# #     with open(image_file, "rb") as file:
# #         encoded_string = base64.b64encode(file.read()).decode()
# #     st.markdown(
# #          f"""
# #          <style>
# #          .stApp {{
# #              background-image: url("data:image/jpeg;base64,{encoded_string}");
# #              background-attachment: fixed;
# #              background-size: cover;
# #              background-position: center;
# #          }}
# #          </style>
# #          """,
# #          unsafe_allow_html=True
# #      )

# # # --- Load the model ---
# # with open('electric_vehicle.pkl', 'rb') as f:
# #     model = pickle.load(f)

# # # --- Set your local background image ---
# # set_background_from_local("C:\Oct_Batch_ml\Project\Tesla.jpg")  # Make sure background.jpg is in the same folder

# # # --- App title ---
# # st.title('🔋 Electric Vehicle Range Predictor')
# # st.write('Provide vehicle details to predict the electric driving range.')

# # # --- Sidebar for user inputs ---
# # st.sidebar.header('Input Features')

# # postal_code = st.sidebar.number_input('Postal Code', min_value=0, value=98001)
# # model_year = st.sidebar.number_input('Model Year', min_value=1990, max_value=2025, value=2020)
# # county = st.sidebar.number_input('County (Encoded)', min_value=0, value=0)
# # city = st.sidebar.number_input('City (Encoded)', min_value=0, value=0)
# # make = st.sidebar.number_input('Make (Encoded)', min_value=0, value=0)
# # model_car = st.sidebar.number_input('Model (Encoded)', min_value=0, value=0)
# # ev_type = st.sidebar.number_input('Electric Vehicle Type (Encoded)', min_value=0, value=0)
# # cafv_eligibility = st.sidebar.number_input('CAFV Eligibility (Encoded)', min_value=0, value=0)
# # electric_utility = st.sidebar.number_input('Electric Utility (Encoded)', min_value=0, value=0)
# # census_tract = st.sidebar.number_input('2020 Census Tract', min_value=0.0, value=0.0)

# # # --- Prediction button ---
# # if st.sidebar.button('Predict Range'):
# #     input_data = np.array([[postal_code, model_year, county, city, make, model_car, ev_type, cafv_eligibility, electric_utility, census_tract]])
# #     prediction = model.predict(input_data)
# #     st.success(f"Predicted Electric Range: **{prediction[0]:.2f} km**")

# # st.sidebar.markdown("---")
# # st.sidebar.write("Note: Some features are encoded numerically as per training data.")










# # import streamlit as st
# # import numpy as np
# # import pickle
# # import base64

# # # --- Set Streamlit page configuration ---
# # st.set_page_config(page_title="Electric Vehicle Range Predictor", layout="centered")

# # # --- Function to set a background image from a local file ---
# # def set_background_from_local(image_file):
# #     with open(image_file, "rb") as file:
# #         encoded_string = base64.b64encode(file.read()).decode()
# #     st.markdown(
# #          f"""
# #          <style>
# #          .stApp {{
# #              background-image: url("data:image/jpeg;base64,{encoded_string}");
# #              background-attachment: fixed;
# #              background-size: cover;
# #              background-position: center;
# #          }}
# #          h1 {{
# #              color: white;
# #              text-align: center;
# #          }}
# #          </style>
# #          """,
# #          unsafe_allow_html=True
# #      )

# # # --- Load the model ---
# # with open('electric_vehicle.pkl', 'rb') as f:
# #     model = pickle.load(f)

# # # --- Set your local background image and title styling ---
# # set_background_from_local("C:\Oct_Batch_ml\Project\Tesla.jpg")  # Make sure background.jpg is in the same folder

# # # --- App title ---
# # st.title('🔋 Electric Vehicle Range Predictor')
# # st.write('Provide vehicle details to predict the electric driving range.')

# # # --- Sidebar for user inputs ---
# # st.sidebar.header('Input Features')

# # postal_code = st.sidebar.number_input('Postal Code', min_value=0, value=98001)
# # model_year = st.sidebar.number_input('Model Year', min_value=1990, max_value=2025, value=2020)
# # county = st.sidebar.number_input('County (Encoded)', min_value=0, value=0)
# # city = st.sidebar.number_input('City (Encoded)', min_value=0, value=0)
# # make = st.sidebar.number_input('Make (Encoded)', min_value=0, value=0)
# # model_car = st.sidebar.number_input('Model (Encoded)', min_value=0, value=0)
# # ev_type = st.sidebar.number_input('Electric Vehicle Type (Encoded)', min_value=0, value=0)
# # cafv_eligibility = st.sidebar.number_input('CAFV Eligibility (Encoded)', min_value=0, value=0)
# # electric_utility = st.sidebar.number_input('Electric Utility (Encoded)', min_value=0, value=0)
# # census_tract = st.sidebar.number_input('2020 Census Tract', min_value=0.0, value=0.0)

# # # --- Prediction button ---
# # if st.sidebar.button('Predict Range'):
# #     input_data = np.array([[postal_code, model_year, county, city, make, model_car, ev_type, cafv_eligibility, electric_utility, census_tract]])
# #     prediction = model.predict(input_data)
# #     st.success(f"Predicted Electric Range: **{prediction[0]:.2f} km**")

# # st.sidebar.markdown("---")
# # st.sidebar.write("Note: Some features are encoded numerically as per training data.")


# import streamlit as st
# import numpy as np
# import pickle
# import base64

# # --- Set Streamlit page configuration ---
# st.set_page_config(page_title="Electric Vehicle Range Predictor", layout="centered")

# # --- Function to set a background image from a local file ---
# def set_background_from_local(image_file):
#     with open(image_file, "rb") as file:
#         encoded_string = base64.b64encode(file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/jpeg;base64,{encoded_string}");
#             background-attachment: fixed;
#             background-size: cover;
#             background-position: center;
#         }}
#         /* Title text styling */
#         .stMarkdown h1 {{
#             color: white !important;
#             text-align: center;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # --- Load the model ---
# with open('electric_vehicle.pkl', 'rb') as f:
#     model = pickle.load(f)

# # --- Set background and style ---
# set_background_from_local("Tesla.jpg")  # Your local image file

# # --- App title ---
# st.title('🔋 Electric Vehicle Range Predictor')
# st.write('Provide vehicle details to predict the electric driving range.')

# # --- Sidebar Inputs ---
# st.sidebar.header('Input Features')

# postal_code = st.sidebar.number_input('Postal Code', min_value=0, value=98001)
# model_year = st.sidebar.number_input('Model Year', min_value=1990, max_value=2025, value=2020)
# county = st.sidebar.number_input('County (Encoded)', min_value=0, value=0)
# city = st.sidebar.number_input('City (Encoded)', min_value=0, value=0)
# make = st.sidebar.number_input('Make (Encoded)', min_value=0, value=0)
# model_car = st.sidebar.number_input('Model (Encoded)', min_value=0, value=0)
# ev_type = st.sidebar.number_input('Electric Vehicle Type (Encoded)', min_value=0, value=0)
# cafv_eligibility = st.sidebar.number_input('CAFV Eligibility (Encoded)', min_value=0, value=0)
# electric_utility = st.sidebar.number_input('Electric Utility (Encoded)', min_value=0, value=0)
# census_tract = st.sidebar.number_input('2020 Census Tract', min_value=0.0, value=0.0)

# # --- Prediction button ---
# if st.sidebar.button('Predict Range'):
#     input_data = np.array([[postal_code, model_year, county, city, make, model_car, ev_type, cafv_eligibility, electric_utility, census_tract]])
#     prediction = model.predict(input_data)
#     st.success(f"Predicted Electric Range: **{prediction[0]:.2f} km**")

# st.sidebar.markdown("---")
# st.sidebar.write("Note: Some features are encoded numerically as per training data.")




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
    model = pickle.load(f)

# --- Set background with dark overlay ---
set_background_from_local("Tesla.jpg")  # Make sure this image exists in your working dir

# --- Custom white title with overlay readability ---
st.markdown('<div class="title-style">🔋 Electric Vehicle Range Predictor</div>', unsafe_allow_html=True)

# --- App instructions ---
st.write('Provide vehicle details to predict the electric driving range.')

# --- Sidebar Inputs ---
st.sidebar.header('Input Features')

postal_code = st.sidebar.number_input('Postal Code', min_value=0, value=98001)
model_year = st.sidebar.number_input('Model Year', min_value=1990, max_value=2025, value=2020)
county = st.sidebar.number_input('County (Encoded)', min_value=0, value=0)
city = st.sidebar.number_input('City (Encoded)', min_value=0, value=0)
make = st.sidebar.number_input('Make (Encoded)', min_value=0, value=0)
model_car = st.sidebar.number_input('Model (Encoded)', min_value=0, value=0)
ev_type = st.sidebar.number_input('Electric Vehicle Type (Encoded)', min_value=0, value=0)
cafv_eligibility = st.sidebar.number_input('CAFV Eligibility (Encoded)', min_value=0, value=0)
electric_utility = st.sidebar.number_input('Electric Utility (Encoded)', min_value=0, value=0)
census_tract = st.sidebar.number_input('2020 Census Tract', min_value=0.0, value=0.0)

# --- Prediction button ---
if st.sidebar.button('Predict Range'):
    input_data = np.array([[postal_code, model_year, county, city, make, model_car, ev_type, cafv_eligibility, electric_utility, census_tract]])
    prediction = model.predict(input_data)
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
st.sidebar.write("Note: Some features are encoded numerically as per training data.")


