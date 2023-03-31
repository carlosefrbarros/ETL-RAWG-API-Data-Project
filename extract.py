import requests
import json

api_key = 'xxx'

x = requests.get('https://api.rawg.io/api/games?ordering=released', params={'key': api_key})

print(x.status_code)

json_data = json.dumps(json.loads(x.text), indent=1)

print(json_data)