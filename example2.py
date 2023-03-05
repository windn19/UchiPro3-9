from pprint import pprint

import requests


response = requests.get('https://swapi.dev/api/planets/10/')
print(response)
text = response.text
print(type(text), text)
js = response.json()
print(type(js))
pprint(js)
