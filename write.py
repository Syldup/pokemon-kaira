import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=200')


filename = "resources.json"
myfile = open(filename, 'w')
myfile.write(str(r))
myfile.close()
