# test_model_loading.py
import pickle

def test_loading():
    try:
        with open('IRIS Flower.csv', 'rb') as f:
            model = pickle.load(f)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")

if __name__ == "__main__":
    test_loading()
