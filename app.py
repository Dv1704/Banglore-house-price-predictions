import streamlit as st
import pickle
import json
import numpy as np

model_path = "C:/Users/OWNER/Desktop/BHP PROJECT/model/BHP_model.pickle"
columns_path = "C:/Users/OWNER/Desktop/BHP PROJECT/model/BHP_columns.json"

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(columns_path, 'r') as f:
    data = json.load(f)
    data_columns = data['data_columns']

def predict_price(location, sqft, bath, bhk):
    loc_index = data_columns.index(location.lower())

    b = np.zeros(len(data_columns))
    b[0] = sqft
    b[1] = bath
    b[2] = bhk
    if loc_index >= 0:
        b[loc_index] = 1

    return model.predict([b])[0]

# Streamlit UI
st.title('House Price Prediction')
st.write('Enter the details below to get an estimated house price.')

location = st.selectbox('Location', data_columns[3:])
total_sqft = st.number_input('Total Square Feet', value=1000)
bath = st.number_input('Number of Bathrooms', value=2)
bhk = st.number_input('Number of Bedrooms', value=2)

if st.button('Predict'):
    estimated_price = predict_price(location, total_sqft, bath, bhk)
    st.success(f'Estimated Price: {estimated_price:.2f} lakhs')
