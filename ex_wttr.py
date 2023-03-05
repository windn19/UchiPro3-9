from pprint import pprint

import requests


params = {
    'lang': 'ru',
    'format': 'j1'
}
city = 'Moscow'
response = requests.get(f'http://wttr.in/{city}', params=params)
response.encoding = 'utf-8'
print(response.url)
# pprint(response.text)
pprint(response.json())
