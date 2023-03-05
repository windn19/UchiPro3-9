import requests

from settings import token


weather_url = 'https://api.openweathermap.org/data/2.5/weather'
geocoder_url = 'http://api.openweathermap.org/geo/1.0/direct'

weather_params = {
    'appid': token,
    'units': 'metric',
    'lang': 'ru'
}

geocoder_params = {'appid': token}


def get_city_coords(city):
    geocoder_params['q'] = city
    res = requests.get(geocoder_url, params=geocoder_params).json()
    lan, lon = res[0]['lat'], res[0]['lon']
    return lan, lon


def get_weather(lat, lon):
    weather_params.update({
        'lat': lat,
        'lon': lon
    })
    res = requests.get(url=weather_url, params=weather_params).json()
    city = res['name']
    description = res['weather'][0]['description']
    temp = res['main']['temp']
    return f'Погода в городе: {city}. {description.capitalize()}, температура: {temp} С'


city = input()
lat, lon = get_city_coords(city)
result = get_weather(lat, lon)
print(result)