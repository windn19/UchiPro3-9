import requests

from settings import token


weather_url = 'https://api.openweathermap.org/data/2.5/weather'
weather_params = {
    'appid': token,
    # 'lat': '55.755811',
    # 'lon': '37.617617',
    'q': 'Moscow',
    'units': 'metric',
    'lang': 'ru'
}

city = input()
weather_params['q'] = city
response = requests.get(weather_url, params=weather_params)
print(response.status_code)
# print(response.text)
js = response.json()
city = js['name']
weather = js['weather'][0]['description']
temp = js['main']['temp']
print(f'Погода в городе: {city}. {weather.capitalize()}, температура: {temp} С')