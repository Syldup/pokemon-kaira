from utils import *


class PageEquipe:
    def __init__(self, screen):
        self.bg_rect = screen.get_rect()
        self.bg = pygame.Surface(self.bg_rect.size)

        self.fond_combat = scale(loadImg('bg/menu_team.png'), 3)

        self.joint_corp = scale(loadImg('sprite/joint_corp.png'), 2)
        self.joint_tete = scale(loadImg('sprite/joint_tete.png'), 2)

        self.btn_conf = {
            'bg': self.bg,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 18),
            'text_offset': None,
            'sprite': {
                True: scale(loadImg('icon/bt_pok_on.png'), 2.75),
                False: scale(loadImg('icon/bt_pok_off.png'), 2.75),
            },
            'box_size': True,
        }
        self.btn_conf2 = self.btn_conf.copy()
        self.btn_conf2['sprite'] = {
            True: scale(loadImg('icon/bt_pok2_on.png'), 2.6),
            False: scale(loadImg('icon/bt_pok2_off.png'), 2.6),
        }
        self.btns = [
            (Button(self.btn_conf2, '', (10, 150), origine=4), self.equpe),
            (Button(self.btn_conf, '', (self.bg_rect.centerx-70, 80), origine=4), self.attaque),
            (Button(self.btn_conf, '', (self.bg_rect.centerx-70, 160), origine=4), self.attaque),
            (Button(self.btn_conf, '', (self.bg_rect.centerx-70, 240), origine=4), self.attaque),
            (Button(self.btn_conf, '', (self.bg_rect.centerx-70, 320), origine=4), self.attaque),
            (Button(self.btn_conf, '', (self.bg_rect.centerx-70, 400), origine=4), self.attaque),
        ]

    def draw(self):
        drawOn(self.bg, self.fond_combat, (self.bg_rect.centerx, self.bg_rect.centery), origine=5)
        for btn, action in self.btns:
            btn.draw()
            self.draw_bar_pv(list(i+j for i, j in zip(btn.pos[:2], (70, 45))), 10, 10)

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
                self.draw_bar_pv(list(i+j for i, j in zip(btn.pos[:2], (70, 45))), 10, 10)

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg, (0, 0))

    def attaque(self):
        print("attaque")

    def equpe(self):
        print("equpe")

