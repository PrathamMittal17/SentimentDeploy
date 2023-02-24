import json
import os
import joblib


def init():
    global model

    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'sentiment_analysis_model.pkl')
    model = joblib.load(model_path)


def run(data):
    r = json.loads(data)["review"]
    prediction = int(model.predict([r])[0])
    return prediction

