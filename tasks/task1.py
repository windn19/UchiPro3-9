import requests

response = requests.get('https://swapi.dev/api/people/').json()
print(response)
characters = response.get('results')
for character in characters:
    print(character['name'])
