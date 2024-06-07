# test_model_loading.py

import pickle

try:
    with open('IRIS Flower.csv', 'rb') as model_file:
        model = pickle.load(model_file)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
