# streamlit_app.py
import streamlit as st
import pickle

# Function to load the model
def load_model():
    try:
        with open('IRIS Flower.csv', 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# Streamlit user interface
st.title("IRIS Flower Species Prediction")

sepal_length = st.number_input("Sepal Length", min_value=0.0, max_value=10.0, value=5.4)
sepal_width = st.number_input("Sepal Width", min_value=0.0, max_value=10.0, value=3.4)
petal_length = st.number_input("Petal Length", min_value=0.0, max_value=10.0, value=1.3)
petal_width = st.number_input("Petal Width", min_value=0.0, max_value=10.0, value=0.2)

if st.button("Predict"):
    if model is not None:
        try:
            features = [[sepal_length, sepal_width, petal_length, petal_width]]
            prediction = model.predict(features)
            st.write(f"Predicted class: {prediction[0]}")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.error("Model is not loaded correctly.")

# Run the Streamlit app
if __name__ == "__main__":
   
