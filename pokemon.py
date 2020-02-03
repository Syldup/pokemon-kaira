import json




class Pokemon():
    def __init__(self, name, hp, attack, defense, specialAttack, specialDefense, speed):
        with open('resources.json') as json_file:
            data = json.load(json_file)
            for p in data['results']:
                self.name = p['name']
        self.hp = []
        self.attack = []
        self.defense = []
        self.specialAttack = []
        self.specialDefense = []
        self.speed = []

    def add_trick(self, trick):
        self.tricks.append(trick)






