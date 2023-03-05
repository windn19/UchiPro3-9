import requests

params = {'search': 'Millennium Falcon'}
response = requests.get('https://swapi.dev/api/starships/', params=params).json()
print(response)
print(response['results'][0]['cost_in_credits'])
