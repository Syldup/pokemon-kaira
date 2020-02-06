from utils import *


class PageCombat:
    def __init__(self, screen):
        w, h = screen.get_size()
        self.y_tier = int(h / 3)
        self.bg_combat = pygame.Surface((w, self.y_tier * 2))
        self.bg_menu = pygame.Surface((w, h - self.y_tier * 2))
        self.loop = True
        self.level = 1

        self.fond_combat = scale(loadImg('bg/combat1.png'), 2.51)
        self.bot_combat = pygame.transform.scale(loadImg('bg/bot_combat.jpg'), self.bg_menu.get_size())
        self.box_left = loadImg('sprite/brick-wallpaper250px.png')
        self.box_right = pygame.transform.rotate(loadImg('sprite/brick-wallpaper250px.png'), 180)

        self.btn_conf = {
            'bg': self.bg_menu,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 16),
            'text_offset': [0, 0],
            'sprite': {
                True: loadImg('icon/select_on.png'),
                False: loadImg('icon/select_off.png'),
            },
        }
        self.w, self.h = self.bg_menu.get_size()
        self.btnsMenu = [
            (Button(self.btn_conf, 'ATTAQUE', (self.w - 20, self.h / 2 - 10), origine=9), self.attaque),
            (Button(self.btn_conf, 'POKEMON', (self.w - 20, self.h / 2 + 10), origine=3), self.equipe),
        ]
        self.btns = self.btnsMenu

    def draw(self):
        centerx = self.bg_combat.get_rect().centerx
        centery = self.bg_combat.get_rect().centery
        w, h = self.bg_combat.get_rect().size

        drawOn(self.bg_combat, self.fond_combat, (centerx, h), origine=8)
        drawOn(self.bg_combat, self.box_left, (0, 50), origine=1)
        drawOn(self.bg_combat, self.box_right, (w, 220), origine=3)

        drawOn(self.bg_menu, self.bot_combat, (centerx, 0), origine=2)
        for btn, action in self.btns:
            btn.draw()

    def event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            for btn, action in self.btns:
                btn.update(action)

    def drawAttacks(self, nameAttacks):
        if len(nameAttacks) == 4:
            self.btns = [
                (Button(self.btn_conf, nameAttacks[0], (40, self.h / 2 - 10), origine=7), self.attaque),
                (Button(self.btn_conf, nameAttacks[1], (40, self.h / 2 + 10), origine=1), self.equipe),
                (Button(self.btn_conf, nameAttacks[2], (self.w - 40, self.h / 2 - 10), origine=6), self.attaque),
                (Button(self.btn_conf, nameAttacks[3], (self.w - 40, self.h / 2 + 10), origine=6), self.equipe),
                (Button(self.btn_conf, 'Retour', ((self.w / 2), self.h / 2 + 10), origine=5), self.goMainMenu)
            ]

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg_combat, (0, 0))
        screen.blit(self.bg_menu, (0, self.y_tier * 2))

    def attaque(self):
        self.drawAttacks([
            'force cachée', 'météore', 'pied de givre', 'sonicboom'
        ])

    def equipe(self):
        print("equpe")

    def goMainMenu(self):
        self.btns = self.btnsMenu