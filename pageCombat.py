from utils import *


class PageCombat:
    def __init__(self, screen):
        self.bg_rect = screen.get_rect()
        self.combat_rect = screen.get_rect()
        self.combat_rect[3] = int(2*self.bg_rect[3]/3)
        self.bg = pygame.Surface(self.bg_rect.size)
        self.level = 10

        self.fond_combat = scale(loadImg('bg/combat1.png'), 2.51)
        self.bot_combat = pygame.transform.scale(loadImg('bg/bot_combat.jpg'), (self.bg_rect[2], self.bg_rect[3]-self.combat_rect[3]))
        self.box_left = loadImg('sprite/brick-wallpaper250px.png')
        self.box_right = pygame.transform.rotate(loadImg('sprite/brick-wallpaper250px.png'), 180)

        self.joint_corp = scale(loadImg('sprite/joint_corp.png'), 2)
        self.joint_tete = scale(loadImg('sprite/joint_tete.png'), 2)

        self.btn_conf = {
            'bg': self.bg,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 18),
            'text_offset': None,
            'sprite': {
                True: loadImg('icon/select_on.png'),
            },
            'box_size': True,
        }
        self.btns = [
            (Button(self.btn_conf, 'ATTAQUE', (self.bg_rect[2]-10, 5*self.bg_rect[3]/6-8), origine=9), self.attaque),
            (Button(self.btn_conf, 'POKEMON', (self.bg_rect[2]-10, 5*self.bg_rect[3]/6+8), origine=3), self.equpe),
        ]

    def draw(self):
        drawOn(self.bg, self.fond_combat, (self.combat_rect.centerx, self.combat_rect[3]), origine=8)
        drawOn(self.bg, self.box_left, (0, 50), origine=1)
        self.draw_bar_pv((100, 100), 10, self.level)
        drawOn(self.bg, self.box_right, (self.combat_rect[2], 220), origine=3)
        self.draw_bar_pv((self.combat_rect[2]-200, 270), 10, self.level)

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

    def attaque(self):
        self.level -= 1
        if self.level < 0:
            self.level = 10
        print("attaque")

    def equpe(self):
        print("equpe")

