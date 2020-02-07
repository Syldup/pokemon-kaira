import json


class Pokemon:
    listPokemon = []

    def __init__(self, p):
        self.id = p["id"]
        self.name = p["name"]
        self.abilities = p["abilities"]
        self.base_experience = p["base_experience"]
        self.height = p["height"]
        self.hp = p["stats"][5]["base_stat"]
        self.attack = p["stats"][4]["base_stat"]
        self.defense = p["stats"][3]["base_stat"]
        self.specialAttack = p["stats"][2]["base_stat"]
        self.specialDefense = p["stats"][1]["base_stat"]
        self.speed = p["stats"][0]["base_stat"]

    @classmethod
    def init_class(cls):
        cls.listPokemon = []
        with open('assets/pok_data.json') as json_file:
            json_pokemon = json.load(json_file)
            for key, value in json_pokemon.items():
                cls.listPokemon.append(Pokemon(value))

    def __str__(self):
        return self.name


Pokemon.init_class()
