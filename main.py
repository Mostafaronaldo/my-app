import streamlit as st
from PIL import Image, ImageDraw
import joblib
import numpy as np
import base64
def resize_image(image_path, size=(300, 300)):
    image = Image.open(image_path)
    return image.resize(size)
def create_circular_image(image_path, size=(100, 100)):
    image = Image.open(image_path).convert("RGBA")
    image = image.resize(size, Image.LANCZOS)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    result = Image.composite(image, Image.new("RGBA", size, (0, 0, 0, 0)), mask)
    return result
def create_rounded_image(image_path, size=(600, 400), radius=30):
    image = Image.open(image_path).convert("RGBA")
    image = image.resize(size, Image.LANCZOS)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    result = Image.composite(image, Image.new("RGBA", size, (0, 0, 0, 0)), mask)
    return result
def set_page_style():
    st.markdown("""
        <style>
            .sidebar {
                background-color: #FF8DA1; 
                padding: 20px;  
                border-radius: 10px;}
            .stApp {
                font-family: 'Segoe UI', sans-serif;
                background-color: rgba(255, 255, 255, 0.8);}
            h1, h2, h3, p {
                color: #0d47a1;
                font-family: 'Arial', sans-serif;}
            .custom-text {
                font-weight: normal;
                color: #333;
                font-size: 18px;}
            .sidebar-title {
                font-size: 24px;
                color: white;}
            .sidebar-button {
                background-color: #0d47a1;
                color: white; 
                border-radius: 5px;  
                padding: 10px;  
                text-align: center; 
                margin-top: 10px;
                display: block;  
                transition: 0.3s ease-in-out;}
            .sidebar-button:hover {
                background-color: #0a3672;
                transform: scale(1.05);}
            .stButton > button {
                border-radius: 5px;
                padding: 10px 20px;
                font-size: 18px;
                transition: 0.3s;}
            .stButton > button:hover {
                background-color: #0a3672;
                transform: scale(1.05); } </style>""", unsafe_allow_html=True)
def navigate_to(page):
    st.session_state.page = page
def Main():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('background.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}  
        </style>""", unsafe_allow_html=True)
    st.markdown("""
        <h1 style='text-align: center; color: #0d47a1;'>Welcome to the Health Assessment Tool</h1>
        <p style='text-align: left; color: black; font-size: 20px;'>
        This tool leverages advanced machine learning models to help users assess health risks such as Breast Cancer, Diabetes, and Anemia. 
        Early diagnosis can significantly improve health outcomes, and this tool aims to guide users towards better preventive measures.
        </p>
        <hr>
        <h2 style='text-align: left; color: #0d47a1;'>What can you do?</h2>
        <ul style='color: black; font-size: 18px;'>
            <li>Assess your risk of Breast Cancer, Diabetes, and Anemia</li>
            <li>Understand the key health indicators and how they affect you</li>
            <li>Get tailored health advice based on your inputs</li>
        </ul>
    """, unsafe_allow_html=True)
    st.markdown("""
        <h2 style='text-align: left; color: #0d47a1;'>Health Tips</h2>
        <p style='text-align: left; color: black; font-size: 18px;'>
        Maintaining a healthy lifestyle is essential for disease prevention. Here are some tips:
        </p>
        <ul style='color: black; font-size: 18px;'>
            <li>Eat a balanced diet rich in fruits, vegetables, and whole grains.</li>
            <li>Stay physically active and maintain a healthy weight.</li>
            <li>Monitor your blood pressure and blood sugar levels regularly.</li>
            <li>Avoid smoking and excessive alcohol consumption.</li>
        </ul>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; color: black; font-size: 20px;'>
        Ready to get started? Choose a health assessment tool from the sidebar to begin your journey to better health.
        </p>
    """, unsafe_allow_html=True)
def Cancer():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('background.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)
    st.title("Breast Cancer")
    st.markdown("""
        <p style='text-align: left; color: black; font-size: 24px;'>
        Breast cancer is one of the most common cancers affecting people globally. Early detection is crucial for better outcomes.
        </p>
    """, unsafe_allow_html=True)
    st.title("Breast Cancer Prediction")
    radius_mean = st.slider('Radius Mean:', min_value=0.0, max_value=30.0, step=0.1)
    texture_mean = st.slider('Texture Mean:', min_value=0.0, max_value=40.0, step=0.1)
    smoothness_mean = st.slider('Smoothness Mean:', min_value=0.0, max_value=0.2, step=0.01)
    compactness_mean = st.slider('Compactness Mean:', min_value=0.0, max_value=0.2, step=0.01)
    symmetry_mean = st.slider('Symmetry Mean:', min_value=0.0, max_value=0.3, step=0.01)
    fractal_dimension_mean = st.slider('Fractal Dimension Mean:', min_value=0.0, max_value=0.1, step=0.001)
    radius_se = st.slider('Radius SE:', min_value=0.0, max_value=5.0, step=0.1)
    texture_se = st.slider('Texture SE:', min_value=0.0, max_value=10.0, step=0.1)
    smoothness_se = st.slider('Smoothness SE:', min_value=0.0, max_value=0.05, step=0.001)
    compactness_se = st.slider('Compactness SE:', min_value=0.0, max_value=0.05, step=0.001)
    symmetry_se = st.slider('Symmetry SE:', min_value=0.0, max_value=0.05, step=0.001)
    fractal_dimension_se = st.slider('Fractal Dimension SE:', min_value=0.0, max_value=0.05, step=0.001)
    if st.button('Predict'):
        user_data = [radius_mean, texture_mean, smoothness_mean, compactness_mean,
                     symmetry_mean, fractal_dimension_mean, radius_se, texture_se, 
                     smoothness_se, compactness_se, symmetry_se, fractal_dimension_se]
        user_data = np.array(user_data).reshape(1, -1)
        model = joblib.load('breast cancer.pkl')
        prediction = model.predict(user_data)
        if prediction[0] == 1:
            st.error('The model predicts the tumor is Malignant.')
        else:
            st.success('The model predicts the tumor is Benign.')
def Anemia():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('background.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>""", unsafe_allow_html=True)
    st.markdown("""
        <h1>Anemia</h1>
        <p style='text-align: left; color: black; font-size: 24px;'>Anemia is a condition in which you lack enough healthy red blood cells to carry adequate oxygen to your body's tissues. 
        Having anemia, also referred to as low hemoglobin, can make you feel tired and weak.</p>
    """, unsafe_allow_html=True)
    st.title("Anemia Prediction")
    gender = st.selectbox('Gender:', ['Male', 'Female'])
    hemoglobin = st.slider('Hemoglobin Level (g/dL):', min_value=6.0, max_value=18.0, step=0.1)
    mch = st.slider('Mean Corpuscular Hemoglobin (pg):', min_value=16.0, max_value=34.0, step=0.1)
    mchc = st.slider('Mean Corpuscular Hemoglobin Concentration (g/dL):', min_value=27.0, max_value=36.0, step=0.1)
    mcv = st.slider('Mean Corpuscular Volume (fL):', min_value=60.0, max_value=120.0, step=0.1)
    if st.button('Predict Anemia'):
        gender = 0 if gender == 'Female' else 1
        user_data = np.array([gender, hemoglobin, mch, mchc, mcv]).reshape(1, -1)
        model = joblib.load('animia.pkl')
        prediction = model.predict(user_data)
        if prediction[0] == 1:
            st.error('The model predicts a risk of anemia.')
        else:
            st.success('The model predicts no risk of anemia.')
def Diabetes():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('background.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }} </style>""", unsafe_allow_html=True)
    st.title("Diabetes")
    st.markdown("""
        <p style='text-align: left; color: black; font-size: 24px;'>
        Diabetes is a chronic condition that affects millions of people worldwide. Early detection and management can significantly improve quality of life.
        </p>""", unsafe_allow_html=True)
    st.title("Diabetes Prediction")
    age = st.slider('Age:', min_value=12, max_value=75, step=1)
    gender = st.selectbox('Gender:', options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
    bmi = st.slider('BMI:', min_value=10, max_value=65, step=1)
    blood_pressure = st.slider('Blood Pressure:', min_value=0, max_value=2, step=1)
    fbs = st.slider('Fasting Blood Sugar (FBS):', min_value=80, max_value=280, step=1)
    hba1c = st.slider('HbA1c:', min_value=5.0, max_value=12.0, step=0.1)
    family_history = st.selectbox('Family History of Diabetes:', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    smoking = st.selectbox('Smoking:', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    diet = st.selectbox('Diet:', options=[0, 1], format_func=lambda x: 'Healthy' if x == 1 else 'Unhealthy')
    exercise = st.selectbox('Exercise:', options=[0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
    if st.button('Predict'):
        user_data = [age, gender, bmi, blood_pressure, fbs, hba1c, family_history, smoking, diet, exercise]
        user_data = np.array(user_data).reshape(1, -1)
        model = joblib.load('Diabetes.pkl')
        prediction = model.predict(user_data)
        if prediction[0] == 1:
            st.error('The model predicts a high risk of Diabetes.')
        else:
            st.success('The model predicts a low risk of Diabetes.')
def Meet_the_Developer():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('background.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>""", unsafe_allow_html=True)
    st.title("About")
    st.markdown("<p class='custom-text'>The Web Application Developer</p>", unsafe_allow_html=True)
    people = [{"image": "me.jpg", "name": "Mostafa Arafat"},]
    for person in people:
        circular_image = create_circular_image(person["image"])
        st.image(circular_image, caption=f"{person['name']}", width=150)
        st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 class='custom-text'>About Me</h3>", unsafe_allow_html=True)
    st.markdown("<p class='custom-text'>I am a preparatory school student aspiring to join the Faculty of Engineering.</p>", unsafe_allow_html=True)
    st.markdown("<p class='custom-text'>Email: moustafaarfat2010@gmail.com</p>", unsafe_allow_html=True)
    st.markdown("<p class='custom-text'>Phone: +20 155 384 8286</p>", unsafe_allow_html=True)
    st.markdown("<p class='custom-text'>&copy; 2024 Mostafa Arafat. All rights reserved.</p>", unsafe_allow_html=True)
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "Welcome"
    set_page_style()
    st.sidebar.title("Navigation :")
    page = st.sidebar.radio("Go to", ["Main", "Breast cancer","Anemia","Diabetes","Meet the Developer"])
    navigate_to(page)
    if st.session_state.page == "Main":
        Main()
    elif st.session_state.page == "Breast cancer":
        Cancer()
    elif st.session_state.page == "Anemia":
        Anemia()
    elif st.session_state.page == "Diabetes":
        Diabetes()
    elif st.session_state.page == "Meet the Developer":
        Meet_the_Developer()
if __name__ == "__main__":
    main()
