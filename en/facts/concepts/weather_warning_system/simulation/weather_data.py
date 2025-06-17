import requests
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
def get_weather_data(latitude, longitude, api_key):
    """
    Holt aktuelle Wetterdaten von OpenWeather API anhand von geografischen Koordinaten.
    
    Parameter:
        latitude (float): Breitengrad der Stadt.
        longitude (float): Längengrad der Stadt.
        api_key (str): API-Schlüssel von OpenWeather.
    
    Rückgabe:
        dict: Wetterdaten (Temperatur, Windgeschwindigkeit, Luftfeuchtigkeit) als Dictionary.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPID={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']  # Temperatur in Celsius
        wind_speed = data['wind']['speed']  # Windgeschwindigkeit in m/s
        humidity = data['main']['humidity']  # Luftfeuchtigkeit in %
        
        return {"current_temp": temp, "wind_speed": wind_speed, "humidity": humidity}
    else:
        print(f"Fehler bei der API-Anfrage: {response.status_code}")
        return None
