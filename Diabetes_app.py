import pickle
import streamlit as st
import pandas as pd
from holoviews.examples.gallery.apps.flask.flask_app import index

# upload data

data= pickle.load(open(r"C:\Users\DELL\OneDrive\Desktop\Pro\Forecasting Diabetes Risk\Diabetes_prediction.sav",'rb'))

st.title("Diabetes Prediction Application")
st.info("Easy Application For Diabetes Prediction Disease")

st.sidebar.image(r"C:\Users\DELL\OneDrive\Desktop\Pro\Forecasting Diabetes Risk\logo.png",width=200)

st.sidebar.header("Click here to find out whether the patient is diagnosed with diabetes or not.")


Pregnancies= st.text_input('Pregnancies')
Glucose= st.text_input('Glucose')
BloodPressure= st.text_input('BloodPressure')
SkinThickness= st.text_input('SkinThickness')
BMI= st.text_input('BMI')
DiabetesPedigreeFunction= st.text_input('DiabetesPedigreeFunction')
Age= st.text_input('Age')

df= pd.DataFrame({'Pregnancies':[Pregnancies], 'Glucose':[Glucose], 'BloodPressure': [BloodPressure] , 'SkinThickness':[SkinThickness], 'BMI':[BMI], 'DiabetesPedigreeFunction':[DiabetesPedigreeFunction] , 'Age':[Age]} ,index=[0])


con= st.sidebar.button('Confirm')
if con:
    res= data.predict(df)
    if res == 0:
       st.sidebar.write('The Patiant Dose Not Have Diabetes')
    else:
        st.sidebar.write('The Patiant has Diabetes')
