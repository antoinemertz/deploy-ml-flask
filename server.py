# import Flask class from the flask module
from flask import Flask, request, jsonify

import numpy as np
import pickle

# Create Flask object to run
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return "Hi, Welcome to my app to show how to deploy a ML model with flask and docker"

# Prediction page
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predict_data = np.array([data['sl'], data['sw'], data['pl'], data['pw']]).reshape((-1,4))
    y_hat = svm_model.predict(predict_data).reshape((1, -1))
    output = y_hat.astype(int)
    output = output.tolist()
    return(jsonify(results=output))

# Load the pre-trained and persisted SVM model
# Note: The model will be loaded only once at the start of the server
def load_model():
	global svm_model

	with open('models/svm.pckl', 'rb') as svm_file:
	       svm_model = pickle.load(svm_file)

if __name__ == "__main__":
    print("**Starting Server...")
    # Call function that loads Model
    load_model()
    print("**Model loaded...")
    # Run Server
    app.run(host="0.0.0.0", port=5000)
