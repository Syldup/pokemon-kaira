from models.joueur import Joueur
from models.teamPoke import TeamPoke
from utils import *
from random import randint


class PageCombat:

    def __init__(self, screen, joueur):
        self.bg_rect = screen.get_rect()
        self.combat_rect = screen.get_rect()
        self.combat_rect[3] = int(2 * self.bg_rect[3] / 3)
        self.bg = pygame.Surface(self.bg_rect.size)
        self.last_page = None

        self.fond_combat = scale(loadImg('bg/combat1.png'), 2.51)
        self.box_left = loadImg('sprite/brick-wallpaper250px.png')
        self.box_right = pygame.transform.rotate(loadImg('sprite/brick-wallpaper250px.png'), 180)
        self.bot_combat = pygame.transform.scale(loadImg('bg/bot_combat.jpg'),
                                                 (self.bg_rect[2], self.bg_rect[3]-self.combat_rect[3]))

        self.btn_conf = {
            'bg': self.bg,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 16),
            'text_offset': (40, -7),
            'sprite': {
                True: loadImg('icon/select_on.png'),
            },
            'box_size': 'text',
        }

        self.btnsMenu = [
            Button(self.btn_conf, 'ATTAQUE', (50, self.combat_rect[3] + 45), origine=4, action=(self.exec, 'attaque')),
            Button(self.btn_conf, 'DEFENSE', (50, self.combat_rect[3] + 90), origine=4, action=(self.exec, 'defense')),
            Button(self.btn_conf, 'SOIN', (50, self.combat_rect[3] + 135), origine=4, action=(self.exec, 'soin')),
            Button(self.btn_conf, 'POKEMON', (520, self.combat_rect[3] + 63), origine=6, action=(self.change_page, 'Equi')),
            Button(self.btn_conf, 'EXIT', (520, self.combat_rect[3] + 108), origine=6, action=(self.exit, )),
        ]

        self.j1 = joueur
        self.j2 = Joueur('Blond')
        self.pokemonFight1: TeamPoke = self.j1.main_poke()
        self.pokemonFight2: TeamPoke = self.j2.main_poke()

    def draw(self):
        drawOn(self.bg, self.fond_combat, (self.combat_rect.centerx, self.combat_rect[3]), origine=8)

        drawOn(self.bg, self.box_right, (self.combat_rect[2], 220), origine=3)
        drawOn(self.bg, self.box_left, (0, 50), origine=1)

        main_poke_j1 = self.j1.main_poke()
        main_poke_j2 = self.j2.main_poke()

        main_poke_j1.draw_combat(self.bg, (430, 220))
        main_poke_j2.draw_combat(self.bg, (20, 50))

        main_poke_j1.draw_pokemon(self.bg, (140, 340), 1)
        main_poke_j2.draw_pokemon(self.bg, (480, 185), 2)

        drawOn(self.bg, self.bot_combat, (self.combat_rect.centerx, self.combat_rect[3]), origine=2)
        for btn in self.btnsMenu:
            btn.draw()

    def event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            for btn in self.btnsMenu:
                btn.update()

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg, (0, 0))

    def getRandomAction(self) -> str:
        return ['attaque', 'defense', 'soin'][randint(0, 2)]

    def exec(self, action_j1: str):
        main_poke_j1 = self.j1.main_poke()
        if main_poke_j1.hp == 0:
            self.j1.switch()
            action_j1 = 'switch'

        main_poke_j2 = self.j2.main_poke()
        if main_poke_j2.hp == 0:
            self.j2.switch()
            action_j2 = 'switch'
        else:
            action_j2 = self.getRandomAction()
        print(action_j1, action_j2)

        if action_j1 == "soin":
            main_poke_j1.soin()
        if action_j2 == "soin":
            main_poke_j2.soin()

        if main_poke_j1.speed < main_poke_j2.speed and action_j2 == "attaque":
            main_poke_j2.attaque(main_poke_j1, action_j2 == 'defense')

        if action_j1 == "attaque":
            main_poke_j1.attaque(main_poke_j2, action_j1 == 'defense')

        if main_poke_j1.speed >= main_poke_j2.speed and action_j2 == "attaque":
            main_poke_j2.attaque(main_poke_j1, action_j2 == 'defense')

        if self.j1.lose():
            print('Tous vos pokemon sont KO, vous avez PERDU !')
            self.exit()
        if self.j2.lose():
            print('Bravo, tous les pokemon adverse sont KO, vous avez GAGNER !')
            self.exit()

    def exit(self):
        self.j1.reset()
        self.j2.pokemons = TeamPoke.get_rmd_team()
        self.change_page('Menu')

    def change_page(self, page):
        e = pygame.event.Event(CHANGEPAGE, {'page': page, 'source': 'Comb'})
        pygame.event.post(e)
