# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LrgbQZ49Df4omA4Bd60k3IbUjtmopncu
"""

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
filename = 'DTC_model.pkl'
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
        Clump_thickness = request.form.get("Clump_thickness", "0")
        Uniformity_of_cell_size = request.form.get("Uniformity_of_cell_size", "0")
        Uniformity_of_cell_shape = request.form.get("Uniformity_of_cell_shape", "0")
        Marginal_adhesion = request.form.get("Marginal_adhesion", "0")
        Single_epithelial_cell_size = request.form.get("Single_cell_epithelial_size", "0")
        Bare_nuclei = request.form.get("Bare_nuclei", "0")
        Bland_chromatin = request.form.get("Bland_chromatin", "0")
        Normal_nucleoli = request.form.get("Normal_nucleoli", "0")
        features = [
            float(Clump_thickness),
            float(Uniformity_of_cell_size),
            float(Uniformity_of_cell_shape),
            float(Marginal_adhesion),
            float(Single_epithelial_cell_size),
            float(Bare_nuclei),
            float(Bland_chromatin),
            float(Normal_nucleoli)]
        prediction = model.predict([features])[0]
        if prediction == 2:
          prediction = "benign"
        else:
            prediction = "malignant"
        return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

!pip show scikit-learn

!pip install scikit-learn==1.3.2