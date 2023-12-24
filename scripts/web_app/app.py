```python
# Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
from scripts.data_preprocessing import load_data, clean_data, transform_data
from scripts.environmental_impact_assessment import predict_impact
from scripts.recommendation_engine import generate_recommendations

# File paths for the processed data
cleaned_data_path = '../data/processed/cleaned_data.csv'
transformed_data_path = '../data/processed/transformed_data.csv'

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load, clean, and transform the data
    data = load_data(cleaned_data_path)
    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)

    # Predict the environmental impact
    impact = predict_impact(transformed_data)

    return render_template('predict.html', impact=impact)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Load, clean, and transform the data
    data = load_data(cleaned_data_path)
    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)

    # Generate recommendations
    recommendations = generate_recommendations(transformed_data)

    return render_template('recommend.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
```
