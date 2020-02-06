import requests
import os.path
import json


def  read_write(url, path):
    path = "resources/moves/" + path
    print(os.path.isfile(path), end=' ')
    if os.path.isfile(path):
        with open(path) as json_file:
            rdata = json.load(json_file)
    else:
        rdata = requests.get(url).json()
        with open(path, 'w') as outfile:
            json.dump(rdata, outfile)
    return rdata


fields = ["id","names","accuracy", "damage_class", "power", "pp", "priority"]

list_mov = read_write('https://pokeapi.co/api/v2/move?offset=0&limit=746', 'list_mov.json')
data = dict()

for mov in list_mov['results']:
    m = read_write(mov['url'], mov['name'] + '.json')
    print(mov)
    data[mov['name']] = dict(((key, m[key]) for key in fields))

with open("assets/mov_data.json", 'w') as outfile:
    json.dump(data, outfile)