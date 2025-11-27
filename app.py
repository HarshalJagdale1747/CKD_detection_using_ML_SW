from flask import Flask, render_template, request
from model_loader import load_model, model_predict
from rule_checker import rule_based_check

app = Flask(__name__)

model = load_model()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/advanced')
def advanced():
    return render_template("advanced.html")

@app.route('/predict', methods=['POST'])
def predict():
    
    vals = [
        float(request.form['sc']),
        float(request.form['bu']),
        float(request.form['al']),
        float(request.form['sg']),
        float(request.form['sod']),
        float(request.form['pot']),
        float(request.form['hemo']),
        float(request.form['htn']),
        float(request.form['dm']),
        float(request.form['ane'])
    ]

    ml_result = model_predict(model, vals)
    rule_result = rule_based_check(vals)

    if ml_result == 1 and rule_result == "High Risk":
        final_result = "CKD Confirmed – Immediate medical consultation required."
    elif ml_result == 1:
        final_result = "CKD Likely – Model detected kidney issues."
    elif ml_result == 0 and rule_result == "High Risk":
        final_result = "Warning: High Risk – Several indicators are abnormal."
    else:
        final_result = "No CKD detected – Kidney condition appears normal."

    return render_template("result.html", output=final_result)

if __name__ == "__main__":
    app.run(debug=True)
