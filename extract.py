import requests
import json

base_url = 'https://api.rawg.io/api/games?'

api_key = 'key=xxx'

ordering = '&ordering=released'

page_size = '&page_size=20'

request_url_0 = base_url + api_key + ordering + page_size

# x = requests.get(request_url_0, params={'key': api_key})

r = requests.get(request_url_0)

print(r.status_code)

data = r.json()

print(data['count'])
print(data['count']/20)
print(data['next'])

for x in range(20):
    print(data['results'][x]['name'])
    print(data['results'][x]['released'])
    print(data['results'][x]['metacritic'])

#json_data = json.dumps(json.loads(x.text), indent=1)

#print(json_data)
