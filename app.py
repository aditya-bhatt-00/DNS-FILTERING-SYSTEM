from flask import Flask, request, jsonify
import joblib
import numpy as np  # If your model uses NumPy

app = Flask(__name__)

# Load your trained model
try:
    model = joblib.load('dns model.joblib')
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None  # Handle the case where the model fails to load

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.get_json()  # Get data sent from the HTML as JSON

        # **Important:** Extract the input features from the JSON data
        # The keys in the `data` dictionary should match the names of your input features
        features = [data['feature1'], data['feature2']] # Example: Replace with your actual feature names

        # **Important:** Preprocess the input data to match the format your model expects
        # This might involve scaling, encoding, etc.
        processed_features = np.array(features).reshape(1, -1) # Example for numerical features

        # Make the prediction
        prediction = model.predict(processed_features)

        # **Important:** Format the prediction into a readable response
        output = {'prediction': prediction.tolist()} # Convert NumPy array to list for JSON

        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) # Set debug=False for production