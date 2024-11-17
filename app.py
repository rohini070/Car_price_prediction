import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and data
pipe = pickle.load(open('model.pkl', 'rb'))
df = pickle.load(open('dataframe.pkl', 'rb'))

# Streamlit UI(UserInterface)
st.title("Car Price Predictor")

# Input selection
company = st.selectbox('Car Brand', df['company'].unique())
year = st.selectbox('Year of Manufacture', df['year'].unique())
kms_driven = st.selectbox('Kilometers Driven', df['kms_driven'].unique())
fuel_type = st.selectbox('Fuel Type', df['fuel_type'].unique())

# Prediction button
if st.button('Predict Price'):
    # Create a DataFrame for user input
    user_data = pd.DataFrame(
        [[company, year, kms_driven, fuel_type]],
        columns=['company', 'year', 'kms_driven', 'fuel_type']
    )
    
    # Predict the price
    predicted_price = pipe.predict(user_data)
    
    # Display the result
    st.subheader(f"The predicted price for the car is: {predicted_price[0]:,.2f}")
