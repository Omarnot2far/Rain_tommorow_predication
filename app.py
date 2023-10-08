import pickle
import json
import numpy as np
from flask import Flask, request, jsonify, url_for, render_template

app = Flask(__name__)

# Load the model and scaling pickle
model = pickle.load(open('clfmodel.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    # Convert data to numpy array and reshape
    new_data = np.array(list(data.values())).reshape(1, -1)
    # Transform using the loaded scaler
    new_data_scaled = scaler.transform(new_data)
    # Predict using the loaded model
    output = model.predict(new_data_scaled)
    return jsonify({'prediction': str(output[0])})

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template("home.html",prediction_text="The prediction is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)
