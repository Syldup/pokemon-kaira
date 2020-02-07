from utils import *


class PageMenu:
    name = 'Menu'

    def __init__(self, screen):
        self.bg = pygame.Surface(screen.get_size())
        self.last_page = None
        self.loop = True

        self.bg_menu = scale(loadImg('bg/menu2.jpg'), 0.7)
        self.logo_pokemon = scale(loadImg('logo/pokemon.png'), 0.3)
        self.logo_kaira = pygame.transform.rotate(scale(loadImg('logo/kaira_bord.png'), 0.2), 20)

        self.btn_conf = {
            'bg': self.bg,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 18),
            'text_offset': None,
            'sprite': {
                True: scale(loadImg('icon/bt_black_on.png'), 0.4),
                False: scale(loadImg('icon/bt_black_off.png'), 0.4),
            },
        }
        xpos, h = self.bg.get_rect().centerx-90, self.bg.get_rect().centery*2
        self.btns = [
            Button(self.btn_conf, 'Pokemons', (xpos - 10, h-180), origine=9),
            Button(self.btn_conf, 'Equipe', (xpos + 10, h-180), origine=7, action=(self.change_page, 'Equi')),
            Button(self.btn_conf, 'Start', (xpos - 10, h-100), origine=9, action=(self.change_page, 'Comb')),
            Button(self.btn_conf, '...', (xpos + 10, h-100), origine=7, action=(self.change_page, 'Comb')),
            Button(self.btn_conf, 'Quit', (xpos, h-20), origine=8, action=(gamequit, )),
        ]

    def draw(self):
        centerx = self.bg.get_rect().centerx
        centery = self.bg.get_rect().centery

        drawOn(self.bg, self.bg_menu, (centerx, centery), origine=5)
        drawOn(self.bg, self.logo_pokemon, (centerx, 90), origine=5)
        drawOn(self.bg, self.logo_kaira, (centerx+30, 20))

        for btn in self.btns:
            btn.draw()

    def event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            for btn in self.btns:
                btn.update()

    def update(self):
        pass

    def display(self, screen):
        screen.blit(self.bg, (0, 0))

    def change_page(self, page):
        e = pygame.event.Event(CHANGEPAGE, {'page': page, 'source': 'Menu'})
        pygame.event.post(e)
