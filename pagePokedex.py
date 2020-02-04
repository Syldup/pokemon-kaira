from utils import *


class PageMenu:
    name = 'Menu'

    def __init__(self, screen):
        self.bg = pygame.Surface(screen.get_size())
        self.loop = True
        self.level = 1

        self.bg_menu = scale(loadImg('bg/menu2.jpg'), 0.7)
        self.logo_pokemon = scale(loadImg('logo/pokemon.png'), 0.3)
        self.logo_kaira = pygame.transform.rotate(scale(loadImg('logo/kaira_bord.png'), 0.2), 20)

        self.btn_conf = {
            'bg': self.bg,
            'overflew': True,
            'font': pygame.font.Font('assets/Pixeled.ttf', 18),
            'sprite': {
                True: scale(loadImg('icon/bt_black_on.png'), 0.4),
                False: scale(loadImg('icon/bt_black_off.png'), 0.4),
            },
        }
        centerx = self.bg.get_rect().centerx
        self.btns = [
            (Button(self.btn_conf, 'Pokemons', (centerx - 100, 300)), None),
            (Button(self.btn_conf, 'Equipe', (centerx + 120, 300)), self.reset),
            (Button(self.btn_conf, 'Start', (centerx - 100, 380)), self.start),
            (Button(self.btn_conf, '...', (centerx + 120, 380)), self.start),
            (Button(self.btn_conf, 'Quit', (centerx, 460)), gamequit),
        ]

    def draw(self):
        centerx = self.bg.get_rect().centerx
        centery = self.bg.get_rect().centery

        drawOn(self.bg, self.bg_menu, (centerx, centery), center=True)
        drawOn(self.bg, self.logo_pokemon, (centerx, 90), center=True)
        drawOn(self.bg, self.logo_kaira, (centerx+30, 20))

        for btn, action in self.btns:
            btn.display_button()

    def event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            for btn, action in self.btns:
                btn.update_button(action)

    def update(self):
        pass

    def reset(self):
        print("reset")

    def start(self):
        print("start")
