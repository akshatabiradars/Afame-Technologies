# app.py

import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('IRIS Flower.csv', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to make predictions
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_features)
    prediction_proba = model.predict_proba(input_features)
    return prediction, prediction_proba

# Streamlit app
st.title('IRIS Flower Species Prediction')

st.sidebar.header('User Input Parameters')
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    return data

input_data = user_input_features()

# Display user input parameters
st.subheader('User Input parameters')
st.write(input_data)

# Make prediction
prediction, prediction_proba = predict_species(
    input_data['sepal_length'], 
    input_data['sepal_width'], 
    input_data['petal_length'], 
    input_data['petal_width']
)

# Display prediction
st.subheader('Prediction')
iris_species = np.array(['Setosa', 'Versicolor', 'Virginica'])
st.write(iris_species[prediction][0])

# Display prediction probability
st.subheader('Prediction Probability')
st.write(prediction_proba)
