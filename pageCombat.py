import string

from Joueur import Joueur
from utils import *
from random import randint

ACTIONS = ['attaque', 'defense', 'soin']


class PageCombat:

    def __init__(self, screen):
        self.bg_rect = screen.get_rect()
        self.combat_rect = screen.get_rect()
        self.combat_rect[3] = int(2 * self.bg_rect[3] / 3)
        self.bg = pygame.Surface(self.bg_rect.size)
        self.loop = True
        self.level = 1

        self.fond_combat = scale(loadImg('bg/combat1.png'), 2.51)
        self.bot_combat = pygame.transform.scale(loadImg('bg/bot_combat.jpg'), self.combat_rect.size)
        self.box_left = loadImg('sprite/brick-wallpaper250px.png')
        self.box_right = pygame.transform.rotate(loadImg('sprite/brick-wallpaper250px.png'), 180)

        self.btn_conf = {
            'bg': self.bg,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 16),
            'text_offset': [0, 0],
            'sprite': {
                True: loadImg('icon/select_on.png'),
            },
            'box_size': 'text',
        }
        self.btnsMenu = [
            (Button(self.btn_conf, 'ATTAQUE', (60, self.bg_rect[3] - 105), origine=4),
             self.launchAction(ACTIONS[0])),
            (Button(self.btn_conf, 'DEFENSE', (60, self.bg_rect[3] - 60), origine=4),
             self.launchAction(ACTIONS[1])),
            (Button(self.btn_conf, 'SOIN', (60, self.bg_rect[3] - 15), origine=4),
             self.launchAction(ACTIONS[2])),
            (Button(self.btn_conf, 'POKEMON', (self.bg_rect[2] - 60, self.bg_rect[3] - 50), origine=6),
             self.equipe),
        ]
        self.btns = self.btnsMenu

        self.joueur1 = Joueur('pierre')
        self.joueur2 = Joueur('blond')
        self.pokemonFight1 = self.joueur1.pokemons[0]
        self.pokemonFight2 = self.joueur2.pokemons[0]

    def draw(self):
        drawOn(self.bg, self.fond_combat, (self.combat_rect.centerx, self.combat_rect[3]), origine=8)
        drawOn(self.bg, self.box_left, (0, 50), origine=1)
        drawOn(self.bg, self.box_right, (self.combat_rect[2], 220), origine=3)

        drawOn(self.bg, self.bot_combat, (self.combat_rect.centerx, self.combat_rect[3]), origine=2)
        for btn, action in self.btns:
            btn.draw()

    def event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            for btn, action in self.btns:
                btn.update(action)

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg, (0, 0))

    def launchAction(self, actionJoueur1: string):
        actionJoueur2 = self.getRandomAction()

    def equipe(self):
        print("equipe")

    def getRandomAction(self):
        return ACTIONS[randint(0, 3)]
