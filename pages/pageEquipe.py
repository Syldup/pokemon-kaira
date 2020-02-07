from utils import *


class PageEquipe:

    def __init__(self, screen, joueur):
        self.bg_rect = screen.get_rect()
        self.last_page = None
        self.bg = pygame.Surface(self.bg_rect.size)
        self.joueur = joueur

        self.fond_combat = scale(loadImg('bg/menu_team.png'), 3)

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
            True: scale(loadImg('icon/bt_pok2_on.png'), 2.75),
            False: scale(loadImg('icon/bt_pok2_off.png'), 2.75),
        }
        self.btns = [
            Button(self.btn_conf2, '', (10, 150), origine=4, action=(self.retour, )),
            Button(self.btn_conf, '', (self.bg_rect.centerx-70, 80), origine=4, action=(self.joueur.switch, 1)),
            Button(self.btn_conf, '', (self.bg_rect.centerx-70, 160), origine=4, action=(self.joueur.switch, 2)),
            Button(self.btn_conf, '', (self.bg_rect.centerx-70, 240), origine=4, action=(self.joueur.switch, 3)),
            Button(self.btn_conf, '', (self.bg_rect.centerx-70, 320), origine=4, action=(self.joueur.switch, 4)),
            Button(self.btn_conf, '', (self.bg_rect.centerx-70, 400), origine=4, action=(self.joueur.switch, 5)),
        ]

    def draw(self):
        drawOn(self.bg, self.fond_combat, (self.bg_rect.centerx, self.bg_rect.centery), origine=5)
        for btn, p in zip(self.btns, self.joueur.pokemons):
            btn.draw()
            if btn.pos[0] == 10:
                p.draw_btn2(self.bg, btn.pos)
            else:
                p.draw_btn(self.bg, btn.pos)

    def event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            for btn in self.btns:
                btn.update()

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg, (0, 0))

    def retour(self):
        e = pygame.event.Event(CHANGEPAGE, {'page': self.last_page if self.last_page else 'Menu', 'source': 'Equi'})
        pygame.event.post(e)
