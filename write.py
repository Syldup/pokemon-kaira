import requests
import os.path
import json


def read_write(url, path):
    path = "resources/" + path
    print(os.path.isfile(path), end=' ')
    if os.path.isfile(path):
        with open(path) as json_file:
            rdata = json.load(json_file)
    else:
        rdata = requests.get(url).json()
        with open(path, 'w') as outfile:
            json.dump(rdata, outfile)
    return rdata


fieldes = ["name", "abilities", "base_experience", "forms", "height", "held_items",
           "id", "is_default", "order", "species", "stats", "types", "weight"]

list_pok = read_write('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1000', 'list_pok.json')
data = dict()

for pok in list_pok['results']:

    p = read_write(pok['url'], pok['name']+'.json')
    print(pok)
    data[pok['name']] = dict(((key, p[key]) for key in fieldes))

f = open("pok_data.json", 'w')
f.write(str(data))
f.close()