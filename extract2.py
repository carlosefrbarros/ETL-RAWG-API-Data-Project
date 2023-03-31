import requests

for x in range(1, 11):
    base_url = 'https://api.rawg.io/api/games?'
    api_key = 'key=xxx'
    ordering = '&ordering=-released'
    page_size = '&page_size=20'
    page_number = '&page='+str(x)
    request_url = base_url + api_key + ordering + page_size + page_number
    r = requests.get(request_url)
    print(r.status_code)
    data = r.json()
    for x in range(20):
        print(data['results'][x]['name'])
        print(data['results'][x]['released'])
        print(data['results'][x]['metacritic'])