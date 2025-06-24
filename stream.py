import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load(open(r"C:\Users\Public\Documents\model.pkl", "rb"))

# Streamlit UI
st.title('House Price Prediction')

# Input fields
gr_liv_area = st.number_input('Enter Square Feet of House:', min_value=1, step=1)
bedrooms = st.number_input('Enter No of Bedrooms:', min_value=1, step=1)
full_bath = st.number_input('Enter No of Bathrooms:', min_value=1, step=1)

# Button to make prediction
if st.button('Predict Price'):
    # Prepare the input data
    input_data = np.array([[gr_liv_area, bedrooms, full_bath]])

    # Make prediction using the loaded model
    prediction = model.predict(input_data)

    # Display result
    st.subheader(f'Predicted House Price: ${prediction[0]:,.2f}')
