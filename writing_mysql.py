import requests
import pymysql

'''
base_url = 'https://rickandmortyapi.com/api/character'
page = '/?page='
r = requests.get('https://rickandmortyapi.com/api/character')

data = r.json()

total_pages = data['info']['pages']

id = data['results'][0]['id']

name = data['results'][0]['name']

episodes = len(data['results'][0]['episode'])

print(total_pages, id, name, episodes)

for item in data['results']:
    id = item['id']
    name = item['name']
    episodes = len(item['episode'])
    print(id, name, episodes)
'''

base_url = 'https://rickandmortyapi.com/api/character'


def main_request(base_url, x):
    r = requests.get(base_url + f'?page={x}')
    return r.json()


def get_pages(response):
    return response['info']['pages']


def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'id': item['id'],
            'name': item['name'],
            'episodes': len(item['episode'])
        }
        charlist.append(char)
    return charlist


data = main_request(base_url, 1)
for x in range(1, get_pages(data)+1):
    print(x)
    #print(parse_json(data))
