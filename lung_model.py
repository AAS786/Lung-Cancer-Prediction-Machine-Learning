import streamlit as st
import pickle as pk
import warnings
import numpy as np

warnings.filterwarnings("ignore")

# Loading the saved model
model = pk.load(open('lung_cancer.sav', 'rb'))

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
        background-image: url('https://i.postimg.cc/QN7WrRS8/lung.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: white;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
        text-decoration: underline;
    }
    h3 {
        text-align: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: white; 
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }
    .center-button {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .stTextInput > div {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 5px;
        margin-bottom: 10px;
    }
    .stSelectbox > div {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 5px;
        margin-bottom: 10px;
    }
    .result-box {
        border: 2px solid #4CAF50;
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.5);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Prediction Page Title
st.markdown("<h1> 🫁 Lung Cancer Detection 🫁🎗️</h1>", unsafe_allow_html=True)

# Three-column layout for input fields
col1, col2, col3 = st.columns(3)

# Left Column Inputs
with col1:
    Gender = st.selectbox('**🚻 Gender**', ['Male', 'Female'])
    Yellow_Fingers = st.selectbox('**🟡 Yellow Fingers**', ['Yes', 'No'])
    Chronic_Disease = st.selectbox('**🏥 Chronic Disease**', ['Yes', 'No'])
    Wheezing = st.selectbox('**🌬️ Wheezing**', ['Yes', 'No'])
    Shortness_of_Breath = st.selectbox('**😮‍💨 Shortness of Breath**', ['Yes', 'No'])

# Center Column Inputs
with col2:
    Age = st.text_input('**🎂 Age**')
    Anxiety = st.selectbox('**😟 Anxiety**', ['Yes', 'No'])
    Fatigue = st.selectbox('**😴 Fatigue**', ['Yes', 'No'])
    Alcohol_Consuming = st.selectbox('**🍷 Alcohol Consuming**', ['Yes', 'No'])
    Swallowing_Difficulty = st.selectbox('**🤐 Swallowing Difficulty**', ['Yes', 'No'])

# Right Column Inputs
with col3:
    Smoking = st.selectbox('**🚬 Smoking**', ['Yes', 'No'])
    Peer_Pressure = st.selectbox('**👥 Peer Pressure**', ['Yes', 'No'])
    Allergy = st.selectbox('**🌿 Allergy**', ['Yes', 'No'])
    Coughing = st.selectbox('**🤧 Coughing**', ['Yes', 'No'])
    Chest_Pain = st.selectbox('**❤️ Chest Pain**', ['Yes', 'No'])

# Center the predict button with custom styling
st.markdown("<div class='center-button'>", unsafe_allow_html=True)

if st.button('**🚀 Lung Cancer Predict Result**'):
    # Prepare input data
    input_data = [
        float(Gender == 'Male'),
        float(Age) if Age else 0,  # Handle missing age
        float(Smoking == 'Yes'),
        float(Yellow_Fingers == 'Yes'),
        float(Anxiety == 'Yes'),
        float(Peer_Pressure == 'Yes'),
        float(Chronic_Disease == 'Yes'),
        float(Fatigue == 'Yes'),
        float(Allergy == 'Yes'),
        float(Wheezing == 'Yes'),
        float(Alcohol_Consuming == 'Yes'),
        float(Coughing == 'Yes'),
        float(Shortness_of_Breath == 'Yes'),
        float(Swallowing_Difficulty == 'Yes'),
        float(Chest_Pain == 'Yes')
    ]

    # Reshape input and make prediction
    reshaped_input = np.array(input_data).reshape(1, -1)
    gen_prediction = model.predict(reshaped_input)

    # Generate the result message based on the prediction
    if gen_prediction[0] == 0:
        Predict_diagnosis = 'The person does not have lung cancer'
        result_color = "green"
    else:
        Predict_diagnosis = 'The person has lung cancer'
        result_color = "red"

    # Display the result with color and border
    st.markdown(f"""
        <div class='result-box'>
        <h3 style='color: {result_color};'>{Predict_diagnosis}</h3>
        </div>
    """, unsafe_allow_html=True)
    st.balloons()  # Balloon effect after prediction

st.markdown("</div>", unsafe_allow_html=True)
