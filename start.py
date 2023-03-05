from pprint import pprint

import requests


response = requests.get('https://uchi.ru/')
response.encoding = 'utf-8'
print(response.url)
pprint(response.headers)
print(response.status_code)
print(type(response), response)
print(response.text)
