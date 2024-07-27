import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def main():
        return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    if request.method == "POST":
        cycles = float(request.form['cycles'])
        voltage_battery = float(request.form['voltage_battery'])
        temp_battery = float(request.form['temp_battery'])
        time = float(request.form['time'])

        input_data = {'cycles': [cycles], 'voltage_battery': [voltage_battery], 'temp_battery': [temp_battery],
                      'time': [time]}
        
        Xnew = pd.DataFrame(input_data)
        loaded_model = pickle.load(open('best_model.pkl', 'rb'))
        ynew = loaded_model.predict(Xnew)
    return render_template('result.html', predicted_value=ynew)
    
if __name__ == "__main__":
    app.run()

