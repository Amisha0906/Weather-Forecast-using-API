from flask import Flask, render_template, request, jsonify
import datetime
import requests

app = Flask(__name__)
API_KEY = 'YOUR_API_KEY'
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/weather', methods=['POST'])
# def get_weather():
#     city = request.json['city']
#     url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3'
#     response = requests.get(url)
#     data = response.json()
#     return jsonify(data)

def get_forecast(city):
    url = f"{BASE_URL}?key={API_KEY}&q={city}&days=14&aqi=no&alerts=no"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    forecast = None
    city = ''
    if request.method == 'POST':
        city = request.form['city']
        forecast = get_forecast(city)
    return render_template('home.html', forecast=forecast, city=city)


if __name__ == '__main__':
    app.run(debug=True)
