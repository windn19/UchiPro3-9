import requests

from settings import token

API_KEY = token
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
WEATHER_PARAMS = {
   'appid': API_KEY,
   'lat': '55.755811',
   'lon': '37.617617',
   'units': 'metric',
   'lang': 'ru'
}

response = requests.get(WEATHER_URL, WEATHER_PARAMS)
json = response.json()
city = json['name']
weather = json['weather'][0]['description']
temp = json['main']['temp']
print(f'Погода в городе: {city}. {weather.capitalize()}, температура: {temp} °C.')