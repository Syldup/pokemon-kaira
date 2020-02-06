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
        self.last_page = None

        self.fond_combat = scale(loadImg('bg/combat1.png'), 2.51)
        self.bot_combat = pygame.transform.scale(loadImg('bg/bot_combat.jpg'), (self.bg_rect[2], self.bg_rect[3]-self.combat_rect[3]))
        self.box_left = loadImg('sprite/brick-wallpaper250px.png')
        self.box_right = pygame.transform.rotate(loadImg('sprite/brick-wallpaper250px.png'), 180)

        self.joint_corp = scale(loadImg('sprite/joint_corp.png'), 2)
        self.joint_tete = scale(loadImg('sprite/joint_tete.png'), 2)

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
        self.pokemonFight1 = None  # self.joueur1.pokemons[0]
        self.pokemonFight2 = None  # self.joueur2.pokemons[0]

    def draw(self):
        drawOn(self.bg, self.fond_combat, (self.combat_rect.centerx, self.combat_rect[3]), origine=8)
        drawOn(self.bg, self.box_left, (0, 50), origine=1)
        self.draw_bar_pv((100, 100), 10, 10)
        drawOn(self.bg, self.box_right, (self.combat_rect[2], 220), origine=3)
        self.draw_bar_pv((self.combat_rect[2]-200, 270), 10, 10)

        drawOn(self.bg, self.bot_combat, (self.combat_rect.centerx, self.combat_rect[3]), origine=2)
        for btn, action in self.btns:
            btn.draw()

    def draw_bar_pv(self, pos, l, p):
        if p > 0:
            rect = self.joint_corp.get_rect()
            rect[2] = rect[2] * p / l
            drawOn(self.bg, self.joint_corp, pos,  origine=4, area=rect)
            drawOn(self.bg, self.joint_tete, (pos[0]+rect[2]-2, pos[1]), origine=4)

    def event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            for btn, action in self.btns:
                btn.update(action)

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg, (0, 0))

    def launchAction(self, actionJoueur1: str):
        actionJoueur2 = self.getRandomAction()

    def equipe(self):
        e = pygame.event.Event(CHANGEPAGE, {'page': 'Equi', 'source': 'Comb'})
        pygame.event.post(e)

    def getRandomAction(self):
        return ACTIONS[randint(0, 2)]
