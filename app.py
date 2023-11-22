
import numpy as np
import pickle
import math
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder= "template", static_folder= "staticFiles") ## assign Flask = app
model = pickle.load(open('build.pkl','rb'))   ### import model

@app.route('/')
def home():
    return render_template('index.html')  # read index.html file

@app.route('/predict', methods=['POST'])   ###transfer data from html to python / server

def predict():
    float_features= [float(x)  for x in request.form.values()]   # request for data values
    final_features= [np.array(float_features)]  # convert into array
    prediction = model.predict(final_features)  # Predict
    if prediction == 0:
        return render_template('index.html', prediction_text="Move-Forward Navigation").format(prediction)
    elif prediction == 1:
        return render_template('index.html', prediction_text="Sharp=Right-Turn Navigation").format(prediction)
    elif prediction == 2:
        return render_template('index.html', prediction_text="Slight-Left-Turn Navigation").format(prediction)
    else:
        return render_template('index.html', prediction_text="Slight-Right-Turn Navigation").format(prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    app.debug = True
   
   