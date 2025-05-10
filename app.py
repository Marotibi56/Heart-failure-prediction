import re
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import math as math

# Initialize Flask app
app = Flask(__name__)

# Load the trained models from the pickle file
all_models=pickle.load(open('models.pkl', 'rb'))
all_models2=pickle.load(open('models.pkl', 'rb'))

@app.route('/', methods=['GET' , 'POST'])
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle predictions."""
    try:
        # Collect data from the form
        data=request.form['data']
        features = np.array([data])

        # Use the default model (Random Forest) for prediction
      
        prediction = model.predict(features)

        # Map the prediction result
        result = "High Risk" if prediction[0] == 1 else "Low Risk"
        return render_template('index.html', prediction=result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
