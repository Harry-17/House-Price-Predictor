import pandas as pd
import pickle as pk
import streamlit as st


model = pk.load(open(r'C:\Users\91638\OneDrive\Desktop\house price\House_prediction_model.pkl', 'rb'))

st.header('Bengaluru House Price Predictor')

data = pd.read_csv(r'C:\Users\91638\OneDrive\Desktop\house price\Cleaned_data.csv')

loc = st.selectbox('Choose Location', data['location'].unique())
sqft = st.number_input('Total Square Feet', min_value=0.0, step=1.0)
beds = st.number_input('Number of Bedrooms', min_value=0, step=1)
baths = st.number_input('Number of Bathrooms', min_value=0, step=1)
balc = st.number_input('Number of Balconies', min_value=0, step=1)

input_data = pd.DataFrame(
    [[loc, sqft, baths, balc, beds]],
    columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms']
)

if st.button('Predict Price'):
    try:
        prediction = model.predict(input_data)
        st.success(f'Price of House: ₹{prediction[0] * 100000:,.2f}')
    except Exception as e:
        st.error(f"An error occurred: {e}")
