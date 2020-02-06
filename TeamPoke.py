from __future__ import annotations

from pokemon import Pokemon
from move import Move
from random import random

class TeamPoke:
    def __init__(self, id):
        self.poke = Pokemon.listPokemon[id]
        #self.move = Move.listMove[id]
        self.niveau = 50
        self.initStats()

    def initStats(self):
        self.hp = (((2 * self.poke.hp + 31 + 7) * 50) / 100) + self.niveau + 10
        self.attack = ((((2 * self.poke.attack + 31 + 7) * self.niveau) / 100) + 5) * 1
        self.defense = ((((2 * self.poke.defense + 31 + 7) * self.niveau) / 100) + 5) * 1
        self.specialAttack = ((((2 * self.poke.specialAttack + 31 + 7) * self.niveau) / 100) + 5) * 1
        self.specialDefense = ((((2 * self.poke.specialDefense + 31 + 7) * self.niveau) / 100) + 5) * 1
        self.speed = ((((2 * self.poke.speed + 31 + 7) * self.niveau) / 100) + 5) * 1

    # def damageTaken(self, defenseur:TeamPoke, move:Move):
    #     if self.move.damageClass == "physical":
    #         damage = (((self.niveau*0.4+2)*self.attack*move.power)/defenseur.defense*50)+2
    #     else:
    #         damage = (((self.niveau*0.4+2)*self.specialAttack*self.move.power)/defenseur.specialDefense*50)+2
    #     if random() < 0.2:
    #         damage *= 1.5
    #     defenseur.hp -= damage

    def action(self, defenseur:TeamPoke, action, reponse):
        if action == "attaque" and reponse == "attaque":
            damage = self.attack/4
            damageReponse = defenseur.attack/4
            self.hp -= damageReponse
            defenseur.hp -= damage
        if action == "attaque" and reponse == "defense":
            damage = self.attack/4 - defenseur.defense/4
            if damage > 0:
                defenseur.hp -= damage
        if action == "attaque" and reponse == "soin":
            damage = self.attack / 4
            heal = defenseur.specialAttack
            defenseur.hp += heal
            defenseur.hp -= damage



if __name__ == "__main__":
    Pokemon.initClass()
    lepoke = TeamPoke(241)
    print(lepoke.poke.name)
    print(lepoke.hp)
    print(lepoke.attack)
    print(lepoke.defense)
    print(lepoke.specialAttack)
    print(lepoke.specialDefense)
    print(lepoke.speed)



