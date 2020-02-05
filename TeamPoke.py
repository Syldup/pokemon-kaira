from pokemon import Pokemon


class TeamPoke:
    def __init__(self, id):
        self.poke = Pokemon.listPokemon[id]
        self.niveau = 50
        modifPV = 0
        modifAttack = 0
        modifDefense = 0
        modifAttackSpe = 0
        modifDefenseSpe = 0
        modifSpeed = 0


    def initStats(self):
        self.hp = (((2 * self.poke.hp + 31 + 7) * 50) / 100) + self.niveau + 10
        self.attack = ((((2*self.poke.attack+31+7)*self.niveau)/100)+5)*1
        self.defense = ((((2*self.poke.defense+31+7)*self.niveau)/100)+5)*1
        self.specialAttack = ((((2*self.poke.specialAttack+31+7)*self.niveau)/100)+5)*1
        self.specialDefense = ((((2*self.poke.specialDefense+31+7)*self.niveau)/100)+5)*1
        self.speed = ((((2*self.poke.speed+31+7)*self.niveau)/100)+5)*1



if __name__ == "__main__":
    Pokemon.initClass()
    lepoke = TeamPoke(150)
    lepoke.initStats()
    print(lepoke.attack)
    print(lepoke.defense)
    print(lepoke.specialAttack)
    print(lepoke.specialDefense)
    print(lepoke.speed)
    print(lepoke.poke.name)