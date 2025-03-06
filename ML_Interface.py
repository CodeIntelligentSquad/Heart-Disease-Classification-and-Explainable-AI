import os
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
import mysql.connector
from mysql.connector import Error

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Define file paths
MODEL_PATH = 'best_model.pkl'
PREPROCESSING_PATH = 'preprocessing.pkl'

# Load the model if the file exists
if os.path.exists(MODEL_PATH):
    try:
        ml_model = joblib.load(MODEL_PATH)
        st.success("Model loaded successfully.")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
else:
    st.error(f"Model file not found: {MODEL_PATH}")

# Load the preprocessing object if the file exists
if os.path.exists(PREPROCESSING_PATH):
    try:
        preprocessing = joblib.load(PREPROCESSING_PATH)
        st.success("Preprocessing file loaded successfully.")
    except Exception as e:
        st.error(f"Error loading the preprocessing file: {e}")
else:
    st.error(f"Preprocessing file not found: {PREPROCESSING_PATH}")

def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='heartdisease',
            user='root',
            password='ashraf'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error while connecting to MySQL: {e}")
    return None

def login_page():
    st.title("Heart Health Data Collection")
    choice = st.selectbox('Login/Signup', ['Log In', 'Sign Up'])

    if choice == 'Log In':
        st.header("Log In")
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        login_button = st.button('Log In')
        
        if login_button:
            if email and password:
                connection = create_db_connection()
                if connection:
                    cursor = connection.cursor(dictionary=True)
                    cursor.execute("SELECT * FROM Users WHERE Email = %s AND HashedPassword = %s", (email, password))
                    user = cursor.fetchone()
                    cursor.close()
                    connection.close()
                    if user:
                        st.session_state['authenticated'] = True
                        st.experimental_rerun()
                    else:
                        st.error("Email or password is incorrect")
            else:
                st.error("Please enter both email and password")
    else:
        st.header("Sign Up")
        first_name = st.text_input('First Name')
        last_name = st.text_input('Last Name')
        email = st.text_input('Email Address')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        re_password = st.text_input('Re-enter your Password', type='password')
        signup_button = st.button('Create Account')
        
        if signup_button:
            if password == re_password:
                connection = create_db_connection()
                if connection:
                    cursor = connection.cursor()
                    cursor.execute(
                        "INSERT INTO Users (Username, HashedPassword, Email, CreateDate) VALUES (%s, %s, %s, NOW())", 
                        (username, password, email)
                    )
                    connection.commit()
                    cursor.close()
                    connection.close()
                    st.session_state['authenticated'] = True
                    st.experimental_rerun()
                else:
                    st.error("Failed to create an account. Please try again.")
            else:
                st.error("Passwords do not match")

def heart_health_data_page():
    st.title("Heart Health Data Collection")
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0)
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    ca = st.number_input("Number of Major Vessels Colored by Flourosopy", min_value=0, max_value=3, step=1)
    thal = st.selectbox("Thal", ["Normal", "Fixed Defect", "Reversible Defect"])
    
    sex_encoded = 1 if sex == "Male" else 0
    cp_encoded = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
    fbs_encoded = 1 if fbs == "Yes" else 0
    restecg_encoded = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(restecg)
    exang_encoded = 1 if exang == "Yes" else 0
    slope_encoded = ["Upsloping", "Flat", "Downsloping"].index(slope)
    thal_encoded = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

    data = {
        'age': age,
        'sex': sex_encoded,
        'cp': cp_encoded,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs_encoded,
        'restecg': restecg_encoded,
        'thalach': thalach,
        'exang': exang_encoded,
        'oldpeak': oldpeak,
        'slope': slope_encoded,
        'ca': ca,
        'thal': thal_encoded
    }
    
    predict_button = st.button("Predict")

    if predict_button:
        data_df = pd.DataFrame([data])
        data_preprocessed = preprocessing.transform(data_df)
        
        prediction = ml_model.predict(data_preprocessed)
        probability = ml_model.predict_proba(data_preprocessed)  # Use predict instead of predict_proba
        
        print(probability)
        if np.round(prediction[0]) == 1:
            st.write("You have a heart disease.")
            st.write('With Probability:',probability[0][1] *100)
            
        else:
            st.write("You do not have a heart disease.")
            st.write('With Probability:',probability[0][0]*100)
    if st.button("Log Out"):
        st.session_state['authenticated'] = False
        st.experimental_rerun()

if st.session_state.get('authenticated', False):
    heart_health_data_page()
else:
    login_page()
