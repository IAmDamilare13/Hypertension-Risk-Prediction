# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:39:37 2024

@author: DAMILARE-PC
"""

import numpy as np
import pickle
import os
import streamlit as st

# Construct the relative path to the model file
model_path = os.path.join(os.path.dirname(__file__), 'trainedModel.sav')

# Load the model
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)


# Create a Function for Prediction
def hypertensionRiskPrediction(inputData):
    inputDataAsNumpyArray = np.asarray(inputData)
    inputDataReshaped = inputDataAsNumpyArray.reshape(1, -1)
    prediction = loaded_model.predict(inputDataReshaped)
    
    if prediction[0] == 0:
        return 'Good Health'
    elif prediction[0] == 1:
        return 'Mild Risk of Hypertension'
    elif prediction[0] == 2:
        return 'High Risk of Hypertension'
    else:
        return 'Error! Verify Input.'

# Page 1: Home
def home():
    st.image('C:/Users/DAMILARE-PC/Documents/School Materials/UG Project Resources/mlModel/images/heart_icon.png', width=100)
    st.markdown("<h1 style='text-align: center; color: #000;'>Hypertension Risk Prediction</h1>", unsafe_allow_html=True)
    st.write("""
        <div style="text-align: center;">
            <p style="color: #000; text-align: center; font-family: Calibri; font-size: 14px; font-style: normal; font-weight: 400; line-height: normal;">This application predict the risk of hypertension based on patient's medical parameters.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")
    with col2:
        if st.button('PREDICT'):
            st.session_state.current_page = 'Predict Hypertension Risk'
        if st.button('ABOUT'):
            st.session_state.current_page = 'About'
    with col3:
        st.write("")

# Page 2: Predict Hypertension Risk
def predict():
    st.image('C:/Users/DAMILARE-PC/Documents/School Materials/UG Project Resources/mlModel/images/heart_icon.png', width=100)
    st.markdown("<h1 style='text-align: center; color: #000;'>Hypertension Risk Prediction</h1>", unsafe_allow_html=True)

    # Apply custom CSS for labels
    st.markdown(
        """
        <style>
        label {
            color: #000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    gender = st.selectbox('Gender', ['Select', 'Male', 'Female'])
    gender = 1 if gender == 'Male' else 0
    age = st.number_input('Age', min_value=0, max_value=120, step=1)
    systolic_bp = st.number_input('Systolic BP', min_value=0, max_value=300, step=1)
    diastolic_bp = st.number_input('Diastolic BP', min_value=0, max_value=200, step=1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, step=0.1)

    diagnosis = ''

    if st.button('PREDICT'):
        if gender == 'Select' or age == 0 or systolic_bp == 0 or diastolic_bp == 0 or bmi == 0.0:
            st.warning('Please fill in all details.')
        else:
            diagnosis = hypertensionRiskPrediction([gender, age, systolic_bp, diastolic_bp, bmi])
    
    if diagnosis:  # Display diagnosis only if it is not empty
        st.success(diagnosis)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")
    with col2:
        if st.button('HOME'):
            st.session_state.current_page = 'Home'
    with col3:
        st.write("")

# Page 3: About
def about():
    st.image('C:/Users/DAMILARE-PC/Documents/School Materials/UG Project Resources/mlModel/images/heart_icon.png', width=100)
    st.markdown("<h1 style='text-align: center; color: #000;'>About The App</h1>", unsafe_allow_html=True)
    st.write("""
        <div style="text-align: center;">
            <p style="color: #000; text-align: center; font-family: Calibri; font-size: 14px; font-style: normal; font-weight: 400; line-height: normal;">This app is an undergraduate project work that uses a machine learning model to predict patients risk of hypertension. The model was trained on a dataset with various health parameters. </p>
            <p style="color: #000; text-align: center; font-family: Calibri; font-size: 14px; font-style: normal; font-weight: 400; line-height: normal;"> For more information, please contact the developer via daramolacpe186651@futa.edu.ng.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")
    with col2:
        if st.button('HOME'):
            st.session_state.current_page = 'Home'
    with col3:
        st.write("")

# Main function to manage navigation
def main():
    # Apply custom CSS
    st.markdown(
        """
        <style>
        .main {
            background-color: #FFCECE;
            padding: 20px;
        }
        .stButton button {
            border-radius: 30px;
            border: 1px solid #000;
            background: #EE2828;
            width: 145px;
            height: 41px;
            align: center;
            flex-shrink: 0;
        }
        .stButton button:hover {
            background-color: #FFCECE;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize the session state variable for current page if not already initialized
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'

    # Sidebar for navigation
    st.sidebar.title('Navigation')
    page = st.sidebar.selectbox('Select a page:', ['Home', 'Predict Hypertension Risk', 'About'], index=['Home', 'Predict Hypertension Risk', 'About'].index(st.session_state.current_page))

    # Update current page based on sidebar selection
    st.session_state.current_page = page

    # Display the selected page
    if st.session_state.current_page == 'Home':
        home()
    elif st.session_state.current_page == 'Predict Hypertension Risk':
        predict()
    elif st.session_state.current_page == 'About':
        about()

if __name__ == '__main__':
    main()
