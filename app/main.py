import requests
from fastapi import FastAPI

app = FastAPI()

# Replace with your WeatherAPI key
API_KEY = "f128d656ad404b27a17121251250605"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

@app.get("/")
def read_root():
    return {"message": "Welcome to Dublin Ireland!"}

@app.get("/weather")
def get_weather():
    city = "London"  # You can change this to any city or make it dynamic
    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no"

    # Fetch the weather data from WeatherAPI
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return {
            "city": city,
            "temperature": data['current']['temp_c'],
            "condition": data['current']['condition']['text'],
            "icon": data['current']['condition']['icon']
        }
    else:
        return {"error": "Could not fetch weather data."}


