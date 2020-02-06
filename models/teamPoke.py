from __future__ import annotations

from typing import List
from models.pokemon import Pokemon
from random import randint
from utils import *


class TeamPoke:
    joint_corp = scale(loadImg('sprite/joint_corp.png', convert=False), 2)
    joint_tete = scale(loadImg('sprite/joint_tete.png', convert=False), 2)

    def __init__(self, id_pok: int):
        self.poke = Pokemon.listPokemon[id_pok]
        # self.move = Move.listMove[id]
        self.niveau = 50
        self.hp = 0
        self.hpMax = 0
        self.speed = 0
        self.attack = 0
        self.defense = 0
        self.attack_spe = 0
        self.defense_spe = 0

        self.init_stats()

    def comput_stat(self, stat):
        return ((((2 * stat + 31 + 7) * self.niveau) / 100) + 5) * 1

    def init_stats(self):
        self.hpMax = (((2 * self.poke.hp + 31 + 7) * 50) / 100) + self.niveau + 10
        self.hp = self.hpMax
        self.speed = self.comput_stat(self.poke.speed)
        self.attack = self.comput_stat(self.poke.attack)
        self.defense = self.comput_stat(self.poke.defense)
        self.attack_spe = self.comput_stat(self.poke.specialAttack)
        self.defense_spe = self.comput_stat(self.poke.specialDefense)

    # def damageTaken(self, defenseur:TeamPoke, move:Move):
    #     if self.move.damageClass == "physical":
    #         damage = (((self.niveau*0.4+2)*self.attack*move.power)/defenseur.defense*50)+2
    #     else:
    #         damage = (((self.niveau*0.4+2)*self.specialAttack*self.move.power)/defenseur.specialDefense*50)+2
    #     if random() < 0.2:
    #         damage *= 1.5
    #     defenseur.hp -= damage

    def action(self, defenseur: TeamPoke, action: str, reponse: str):
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
            heal = defenseur.attack_spe
            defenseur.hp += heal
            defenseur.hp -= damage

    @classmethod
    def get_rmd_team(cls) -> List[TeamPoke]:
        last_pokemon = len(Pokemon.listPokemon) - 1
        return [TeamPoke(randint(0, last_pokemon)) for _ in range(6)]

    def draw_bar_pv(self, bg, pos):
        if self.hp > 0:
            rect = self.joint_corp.get_rect()
            rect[2] = rect[2] * self.hp / self.hpMax
            drawOn(bg, self.joint_corp, pos,  origine=4, area=rect)
            pos[0] += rect[2] - 2
            drawOn(bg, self.joint_tete, pos, origine=4)

    def draw_combat(self, bg, pos):
        self.draw_bar_pv(bg, pos)


if __name__ == "__main__":
    lepoke = TeamPoke(241)
    print(lepoke.poke.name)
    print(lepoke.hp)
    print(lepoke.attack)
    print(lepoke.defense)
    print(lepoke.attack_spe)
    print(lepoke.defense_spe)
    print(lepoke.speed)



