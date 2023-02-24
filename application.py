from flask import Flask,request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"


@app.route("/predict")
def predict():
    review = request.args.get('review')
    data = {"review": review}
    url = 'http://20.207.64.67:80/api/v1/service/myservice/score'
    api_key = 's9dWawXU0BaDV0fw6p8x4e6WyqkFmFYa'
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
    req = requests.post(url, headers=headers, json=data)
    result = req.text
    return f"<h1>{result}</h1>"