from __future__ import annotations

from typing import List
from models.pokemon import Pokemon
from random import randint
from utils import *


class TeamPoke:
    font16 = pygame.font.Font('assets/Pixeled.ttf', 16)
    font12 = pygame.font.Font('assets/Pixeled.ttf', 12)
    joint_corp = scale(loadImg('sprite/joint_corp.png', convert=False), 2)
    joint_tete = scale(loadImg('sprite/joint_tete.png', convert=False), 2)

    def __init__(self, id_pok: int):
        self.poke = Pokemon.listPokemon[id_pok]
        self.shiny = ''
        self.sprites = [
            loadImg('sprite/pokemon/{:0>3}.png'.format(id_pok+1)),
            GIFImage('assets/sprite/pokestadium/dos{}/{:0>3}.gif'.format(self.shiny, id_pok+1), scale=1.5),
            GIFImage('assets/sprite/pokestadium/fas{}/{:0>3}.gif'.format(self.shiny, id_pok+1), scale=1.5),
        ]
        self.nameB = self.font16.render(self.poke.name, True, BLACK)
        self.nameW = self.font16.render(self.poke.name, True, WHITE)
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

    def actionAttaque(self, defenseur: TeamPoke, reponse: str):
        pvMax = self.hpMax
        pvMaxDefense = defenseur.hpMax
        if reponse == "attaque":
            damage = self.attack/4
            damageReponse = defenseur.attack/4
            if self.speed > defenseur.speed:
                defenseur.hp -= damage
                if defenseur.hp - damage <= 0:
                    statutDefenseur = "pokemon KO"
                    damageReponse = 0
                self.hp -= damageReponse
            else:
                self.hp -= damageReponse
                if self.hp - damageReponse <= 0:
                    statut = "pokemon KO"
                    damage = 0
                defenseur.hp -= damage
        if reponse == "defense":
            damage = self.attack/4 - defenseur.defense/4
            if damage > 0:
                defenseur.hp -= damage
            if defenseur.hp <= 0:
                statutDefenseur = "pokemon KO"
            self.hp -= defenseur.defense_spe/4
            if self.hp <= 0:
                statut = "Pokemon KO"
        if reponse == "soin":
            damage = self.attack / 4
            heal = defenseur.attack_spe
            if defenseur.hp + heal > pvMaxDefense:
                defenseur.hp = pvMaxDefense
            else:
                defenseur.hp += heal
            defenseur.hp -= damage
            if defenseur.hp <= 0:
                statutDefenseur = "pokemon KO"

    def actionDefense(self, defenseur: TeamPoke, reponse: str):
        pvMax = self.hpMax
        pvMaxDefense = defenseur.hpMax
        if reponse == "attaque":
            damageReponse = defenseur.attack/4 - self.defense/4
            if damageReponse > 0:
                self.hp -= damageReponse
            if self.hp <= 0:
                statut = "pokemon KO"
            else:
                defenseur.hp -= self.defense_spe/4
                if defenseur.hp <= 0:
                    statueDefenseur = "Pokemon KO"
        if reponse == "defense":
            text = "ça fait rien lol, combat de magicarpe"
        if reponse == "soin":
            heal = defenseur.attack_spe
            if defenseur.hp + heal > pvMaxDefense:
                defenseur.hp = pvMaxDefense
            else:
                defenseur.hp += heal

    def actionSoin(self, defenseur: TeamPoke, reponse: str):
        pvMax = self.hpMax
        heal = self.attack_spe
        pvMaxDefense = defenseur.hpMax
        if reponse == "attaque":
            if self.hp + heal > pvMax:
                self.hp = pvMax
            else:
                self.hp += heal
            damageReponse = defenseur.attack/4
            self.hp -= damageReponse
            if self.hp <= 0:
                statut = "pokemon KO"
        if reponse == "defense":
            if self.hp + heal > pvMax:
                self.hp = pvMax
            else:
                self.hp += heal
        if reponse == "soin":
            healDefenseur = defenseur.attack_spe
            if defenseur.hp + healDefenseur > pvMaxDefense:
                defenseur.hp = pvMaxDefense
            else:
                defenseur.hp += healDefenseur
            if self.hp + heal > pvMax:
                self.hp = pvMax
            else:
                self.hp += heal

    @classmethod
    def get_rmd_team(cls) -> List[TeamPoke]:
        last_pokemon = len(Pokemon.listPokemon) - 1
        if last_pokemon > 720:
            last_pokemon = 720
            print(last_pokemon)
        return [TeamPoke(randint(0, last_pokemon)) for _ in range(6)]

    def draw_bar_pv(self, bg, pos):
        if self.hp > 0:
            rect = self.joint_corp.get_rect()
            rect[2] = rect[2] * self.hp / self.hpMax
            drawOn(bg, self.joint_corp, pos,  origine=4, area=rect)
            drawOn(bg, self.joint_tete, (pos[0]+rect[2] - 2, pos[1]), origine=4)

    def draw_name(self, bg, pos):
        drawOn(bg, self.nameW, sumList(pos, (1, 1)), origine=1)
        drawOn(bg, self.nameB, pos, origine=1)

    def draw_pv(self, bg, pos):
        pv = "{} / {}".format(int(self.hp), int(self.hpMax))
        drawOn(bg, self.font12.render(pv, True, WHITE), sumList(pos, (1, 1)), origine=1)
        drawOn(bg, self.font12.render(pv, True, BLACK), pos, origine=1)

    def draw_pokemon(self, bg, pos, fas: int):
        drawOn(bg, self.sprites[fas], pos, origine=8)

    def draw_combat(self, bg, pos):
        self.draw_name(bg, pos)
        self.draw_bar_pv(bg, sumList(pos, (-5, 72)))
        self.draw_pv(bg, sumList(pos, (120, 50)))

    def draw_btn(self, bg, pos):
        self.draw_name(bg, pos)
        self.draw_bar_pv(bg, sumList(pos, (20, 20)))
        self.draw_pv(bg, sumList(pos, (40, 50)))

    def draw_btn2(self, bg, pos):
        self.draw_name(bg, pos)
        self.draw_bar_pv(bg, sumList(pos, (20, 20)))
        self.draw_pv(bg, sumList(pos, (40, 50)))


if __name__ == "__main__":
    lepoke = TeamPoke(241)
    print(lepoke.poke.name)
    print(lepoke.hp)
    print(lepoke.attack)
    print(lepoke.defense)
    print(lepoke.attack_spe)
    print(lepoke.defense_spe)
    print(lepoke.speed)



