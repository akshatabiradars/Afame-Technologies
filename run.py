# run.py

import pickle

# Load the model
def load_model():
    with open('IRIS Flower.csv', 'rb') as f:
        return pickle.load(f)

model = load_model()

# Function to make predictions
def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    return model.predict(features)

# Test prediction
if __name__ == "__main__":
    sample_input = {
        "sepal_length": 5.4,
        "sepal_width": 3.4,
        "petal_length": 1.3,
        "petal_width": 0.2
    }
    prediction = predict_iris(**sample_input)
    print(f"Predicted class: {prediction[0]}")
