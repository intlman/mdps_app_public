# -*- coding: utf-8 -*-
"""PredictMain_MDPS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D1VB2Sl_NvFte8OAZPTewdco42uj74ZZ
"""

import pickle
import pickle
import streamlit as st                                                                                                                                                                                                                                                             
from streamlit_option_menu import option_menu


# loading the saved models

cardiovascular_disease_model = pickle.load(open('C:/Users/regin/Desktop/HUD_Final/cardiovascular_disease_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/regin/Desktop/HUD_Final/heart_disease_model.sav', 'rb'))

hypertension_disease_model = pickle.load(open('C:/Users/regin/Desktop/HUD_Final/hypertension_disease_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Cardiovascular Disease Prediction',
                           'Heart Disease Prediction',
                           'Hypertension Prediction'],
                          icons=['activity','heart', 'person'],
                          default_index=0)
    
    
# Cardiovascular Disease Prediction Page
if (selected == 'Cardiovascular Disease Prediction'):
    
    # page title
    st.title('Cardiovascular Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        gender = st.text_input('Gender: 1 = female, 2 = male')
        
    with col3:
        height = st.text_input('Height (cm)')
        
    with col1:
        weight = st.text_input('Weight (kg)')
        
    with col2:
        ap_hi = st.text_input('Systolic Blood Pressure')
        
    with col3:
        ap_lo = st.text_input('Diastolic Blood Pressure')
        
    with col1:
        cholesterol = st.text_input('Cholesterol: 1 = normal, 2 = above normal, 3 = well above normal')
        
    with col2:
        gluc = st.text_input('Glucose: 1 = normal, 2 = above normal, 3 = well above normal')
        
    with col3:
        smoke = st.text_input('Smoke: 0 = no, 1: yes')
        
    with col1:
        alco = st.text_input('Alcohol: 0 = no, 1: yes')
        
    with col2:
        active = st.text_input('Physical Activity: 0 = no, 1: yes')
        
               
    # code for Prediction
    cardiovascular_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Cardiovascular Disease Test Result'):
        cardiovascular_prediction = cardiovascular_disease_model.predict([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])                          
        
        if (cardiovascular_prediction[0] == 1):
          cardiovascular_diagnosis = 'You are at risk for cardiovascular disease'
        else:
          cardiovascular_diagnosis = 'You are not at risk for cardiovascular disease'
        
    st.success(cardiovascular_diagnosis)   


# Heart Disease Prediction Page - CHECK LEGEND!!
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
               
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'You are at risk for heart disease'
        else:
          heart_diagnosis = 'You are not at risk for heart disease'
        
    st.success(heart_diagnosis)
        

# Hypertension Prediction Page
if (selected == 'Hypertension Prediction'):
    
    # page title
    st.title('Hypertension Prediction')
    
    col1, col2, col3 = st.columns(3)
            
    with col1:
        age = st.text_input('Age')
      
    with col2:
        bmi = st.text_input('BMI')
        
    with col3:
        heartRate = st.text_input('Heart Rate')
       
     
    # code for Prediction
    hypertension_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Hypertension Test Result'):
        hypertension_prediction = hypertension_model.predict([[age, BMI, heartRate]])                          
        
        if (hypertension_prediction[0] == 1):
          hypertension_diagnosis = 'The person is at risk of hypertension'
        else:
          hypertension_diagnosis = 'The person is not at risk of hypertension'
        
    st.success(hypertension_diagnosis)