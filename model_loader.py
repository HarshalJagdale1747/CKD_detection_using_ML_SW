"""import joblib
import numpy as np

def load_model():
    return joblib.load("ckd_model.pkl")

def model_predict(model, vals):
    vals = np.array(vals).reshape(1, -1)
    return int(model.predict(vals)[0])
"""
import joblib
import numpy as np

def load_model():
    return joblib.load("ckd_model.pkl")

def model_predict(model, vals):
    vals = np.array(vals).reshape(1, -1)
    return int(model.predict(vals)[0])
