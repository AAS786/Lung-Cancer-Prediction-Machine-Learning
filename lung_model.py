import streamlit as st
import pickle as pk
import warnings
import numpy as np

warnings.filterwarnings("ignore")

# Loading the saved model
model = pk.load(open('lung_cancer.sav', 'rb'))

# Custom CSS for enhanced styling and animations, including column header colors
st.markdown("""
    <style>
    /* Apply background to the entire container */
    .main {
        background-image: url('https://i.postimg.cc/ZYB9Z1b7/lung7.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        animation: fadeIn 2s ease-in-out;
    }

    h1 {
        color: Purple;
        text-align: center;
        text-decoration: underline;
        animation: slideIn 1s ease-out;
    }
    h3 {
        text-align: center;
    }

    /* Style for changing column header colors */
    .stSelectbox label, .stTextInput label {
        color: blue; /* Change to desired color */
        font-size: 16px;
        font-weight: bold;
        animation: colorChange 3s infinite alternate;
    }

    /* Different colors for different columns */
    .stSelectbox label:nth-of-type(1), .stTextInput label:nth-of-type(1) { color: purple; } /* Column 1 */
    .stSelectbox label:nth-of-type(2), .stTextInput label:nth-of-type(2) { color: purple; } /* Column 2 */
    .stSelectbox label:nth-of-type(3), .stTextInput label:nth-of-type(3) { color: purple; } /* Column 3 */
    .stSelectbox label:nth-of-type(4), .stTextInput label:nth-of-type(4) { color: purple; } /* Column 4 */

    /* Style for input boxes and hover effects */
    .stTextInput > div, .stSelectbox > div {
        border: 2px solid #4CAF50;
        border-radius: 8px;
        padding: 5px;
        margin-bottom: 10px;
        transition: background-color 0.3s ease;
    }
    .stTextInput > div:hover, .stSelectbox > div:hover {
        background-color: rgba(255, 255, 255, 0.2);
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
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background-color: white; 
        color: #4CAF50;
        border: 2px solid #4CAF50;
        transform: scale(1.05);
    }
    .center-button {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }

    .result-box {
        border: 2px solid #4CAF50;
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.5);
        text-align: center;
        animation: resultReveal 1.5s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(-100px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes resultReveal {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }

    @keyframes colorChange {
        from { color: yellow; }
        to { color: yellow; }
    }
    </style>
""", unsafe_allow_html=True)

# Wrap the whole app content inside a main div for background image
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Prediction Page Title
st.markdown("<h1> 🫁 Lung Cancer Detection 🫁🎗️</h1>", unsafe_allow_html=True)

# Three-column layout for input fields
col1, col2, col3 = st.columns(3)

# Left Column Inputs
with col1:
    Gender = st.selectbox('**🚻 Gender**', ['Male', 'Female'], help="Select your gender.")
    Yellow_Fingers = st.selectbox('**🟡 Yellow Fingers**', ['Yes', 'No'], help="Do you have yellowed fingers?")
    Chronic_Disease = st.selectbox('**🏥 Chronic Disease**', ['Yes', 'No'], help="Do you have any chronic disease?")
    Wheezing = st.selectbox('**🌬️ Wheezing**', ['Yes', 'No'], help="Do you experience wheezing?")
    Shortness_of_Breath = st.selectbox('**😮‍💨 Shortness of Breath**', ['Yes', 'No'], help="Do you experience shortness of breath?")

# Center Column Inputs
with col2:
    Age = st.text_input('**🎂 Age**', help="Enter your age.")
    Anxiety = st.selectbox('**😟 Anxiety**', ['Yes', 'No'], help="Do you suffer from anxiety?")
    Fatigue = st.selectbox('**😴 Fatigue**', ['Yes', 'No'], help="Do you often feel fatigued?")
    Alcohol_Consuming = st.selectbox('**🍷 Alcohol Consuming**', ['Yes', 'No'], help="Do you consume alcohol regularly?")
    Swallowing_Difficulty = st.selectbox('**🤐 Swallowing Difficulty**', ['Yes', 'No'], help="Do you have trouble swallowing?")

# Right Column Inputs
with col3:
    Smoking = st.selectbox('**🚬 Smoking**', ['Yes', 'No'], help="Are you a smoker?")
    Peer_Pressure = st.selectbox('**👥 Peer Pressure**', ['Yes', 'No'], help="Are you under peer pressure to smoke?")
    Allergy = st.selectbox('**🌿 Allergy**', ['Yes', 'No'], help="Do you have any allergies?")
    Coughing = st.selectbox('**🤧 Coughing**', ['Yes', 'No'], help="Do you cough frequently?")
    Chest_Pain = st.selectbox('**❤️ Chest Pain**', ['Yes', 'No'], help="Do you experience chest pain?")

# Center the predict button with custom styling
st.markdown("<div class='center-button'>", unsafe_allow_html=True)

if st.button('**🚀 Lung Cancer Predict Result**'):
    # Prepare input data
    input_data = [
        float(Gender == 'Male'),
        float(Age) if Age else 0,  # Handle missing age
        float(Smoking == 'Yes'),
        float(Yellow_Fingers == 'No'),
        float(Anxiety == 'Yes'),
        float(Peer_Pressure == 'No'),
        float(Chronic_Disease == 'Yes'),
        float(Fatigue == 'No'),
        float(Allergy == 'Yes'),
        float(Wheezing == 'No'),
        float(Alcohol_Consuming == 'Yes'),
        float(Coughing == 'No'),
        float(Shortness_of_Breath == 'Yes'),
        float(Swallowing_Difficulty == 'No'),
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

# Close the main div
st.markdown("</div>", unsafe_allow_html=True)
