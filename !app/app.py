import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = "./templates"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    if request.method == "POST":
        cycle = float(request.form['cycle'])
        voltage_battery = float(request.form['voltage_battery'])
        temp_battery = float(request.form['temp_battery'])
        time = float(request.form['time'])

        input_data = {'cycle': [cycle], 'voltage_battery': [voltage_battery], 'temp_battery': [temp_battery],
                      'time': [time]}

        Xnew = pd.DataFrame(input_data)
        loaded_model = pickle.load(open('finalmodel.sav', 'rb'))
        ynew = loaded_model.predict(Xnew)

        return render_template('result.html', predicted_value=ynew)

if __name__ == "__main__":
    app.run()
