import requests
import pandas as pd

def extract_weather_data(city_name="Ranchi", latitude=23.3441, longitude=85.3096):
    """Fetch current weather data from Open-Meteo API and return it as a DataFrame."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    data = response.json()
    
    weather = data['current']
    weather['city'] = city_name
    
    df = pd.DataFrame([weather])
    return df

# Quick test when running this file directly
if __name__ == "__main__":
    df = extract_weather_data()
    print(df)