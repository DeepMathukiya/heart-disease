from flask import Flask, render_template, request
from joblib import load
import numpy as np
RF = load("HeartDisease-RF.joblib")
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html") 
              
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        feature = []
        feature.append(request.form['Age'])
        feature.append(request.form['Gender'])
        feature.append(request.form['Cp'])
        feature.append(request.form['TestBp'])
        feature.append(request.form['Chol'])
        feature.append(request.form['Fbs'])     
        feature.append(request.form['Restecg'])
        feature.append(request.form['Thalach'])
        feature.append(request.form['Exang'])
        feature.append(request.form['Oldpeak'])
        feature.append(request.form['Slope'])
        feature.append(request.form['Ca'])
        feature.append(request.form['Thal'])
        final = [np.array(feature)]
        predict_val = RF.predict(final)
        return render_template("index.html" , output= "{}" .format(final))
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')        
       