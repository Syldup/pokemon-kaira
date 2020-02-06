from utils import *


class PageCombat:
    def __init__(self, screen):
        w, h = screen.get_size()
        self.y_tier = int(h/3)
        self.bg_combat = pygame.Surface((w, self.y_tier*2))
        self.bg_menu = pygame.Surface((w, h-self.y_tier*2))
        self.loop = True
        self.level = 1

        self.fond_combat = scale(loadImg('bg/combat1.png'), 2.51)
        self.bot_combat = pygame.transform.scale(loadImg('bg/bot_combat.jpg'), self.bg_menu.get_size())
        self.box_left = loadImg('sprite/brick-wallpaper250px.png')
        self.box_right = pygame.transform.rotate(loadImg('sprite/brick-wallpaper250px.png'), 180)

        self.btn_conf = {
            'bg': self.bg_menu,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 18),
            'text_offset': None,
            'sprite': {
                True: loadImg('icon/select_on.png'),
                False: loadImg('icon/select_off.png'),
            },
        }
        w, h = self.bg_menu.get_size()
        self.btns = [
            (Button(self.btn_conf, 'ATTAQUE', (w-20, h/2-10), origine=9), self.attaque),
            (Button(self.btn_conf, 'POKEMON', (w-20, h/2+10), origine=3), self.equpe),
        ]

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

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg_combat, (0, 0))
        screen.blit(self.bg_menu, (0, self.y_tier*2))

    def attaque(self):
        print("attaque")

    def equpe(self):
        print("equpe")
