from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual API key from OpenWeatherMap
API_KEY = "5a945612ae9abfaa000d54d3c0ed0940"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = None
    error = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }
            try:
                response = requests.get(BASE_URL, params=params)
                response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
                data = response.json()

                if data.get("cod") == 200:
                    weather_data = {
                        "city": city.title(), # Capitalize first letter of each word
                        "temperature": data['main']['temp'],
                        "humidity": data['main']['humidity'],
                        "description": data['weather'][0]['description'].title(), # Capitalize description
                        "icon": data['weather'][0]['icon'], # Get weather icon code 
                        "wind_speed": data['wind']['speed'],
                        "pressure": data['main']['pressure']
                    }
                else:
                    error = "City not found or invalid request. Please check the city name."
            except requests.exceptions.RequestException as e:
                error = f"Error fetching weather data: {e}. Please check your internet connection or try again later."
        else:
            error = "Please enter a city name."

    return render_template('index.html', weather=weather_data, city_name=city, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5001) # debug=True allows for automatic reloading on code changes