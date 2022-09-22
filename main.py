import requests


if __name__ == '__main__':
    base_url = 'https://akabab.github.io/superhero-api/api'
    url = base_url + '/all.json'
    response = requests.get(url=url).json()
    response_selected = filter(lambda x: x['name'] in ['Hulk', 'Captain America', 'Thanos'], response)
    who_is_smartest = max(response_selected, key=lambda x: x['powerstats']['intelligence'])
    print(who_is_smartest['name'])
