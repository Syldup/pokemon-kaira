import json

class Move:
    listMove = []

    def __init__(self, m):
        self.id = m["id"]
        self.name = m["names"][1]["language"]
        self.accuracy = m["accuracy"]
        self.power = m["power"]
        self.pp = m["pp"]
        self.priority = m["priority"]
        self.damageClass = m["damage_class"]["name"]

    @classmethod
    def initClass(cls):
        with open('assets/mov_data.json') as json_file:
            jsonMove = json.load(json_file)
            for key, value in jsonMove.items():
                cls.listMove.append(Move(value))

    def __str__(self):
        return self.name


if __name__ == "__main__":
    Move.initClass()
    print((Move.listMove[202]))

