from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('C:\\Users\\user\\Downloads\\Sports Prediction app using ML model\\top5_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        reactions = int(request.form['reactions'])
        potential = int(request.form['potential'])
        short_passing = int(request.form['short_passing'])
        vision = int(request.form['vision'])
        international_reputation = int(request.form['international_reputation'])
        
        features = np.array([[reactions, potential, short_passing, vision, international_reputation]])
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction_text=f"Predicted Overall Rating: {prediction:.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
