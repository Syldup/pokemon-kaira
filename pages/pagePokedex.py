from utils import *


class PagePokedex:
    name = 'Menu'

    def __init__(self, screen):
        self.bg = pygame.Surface(screen.get_size())
        self.loop = True

        self.bg_menu = scale(loadImg('bg/menu2.jpg'), 0.7)
        self.logo_pokemon = scale(loadImg('logo/pokemon.png'), 0.3)
        self.logo_kaira = pygame.transform.rotate(scale(loadImg('logo/kaira_bord.png'), 0.2), 20)

        self.btn_conf = {
            'bg': self.bg,
            'overflew': True,
            'origine': 9,
            'font': pygame.font.Font('../assets/Pixeled.ttf', 18),
            'text_offset': None,
            'sprite': {
                True: scale(loadImg('icon/bt_black_on.png'), 0.4),
                False: scale(loadImg('icon/bt_black_off.png'), 0.4),
            },
        }
        centerx, h = self.bg.get_rect().centerx, self.bg.get_rect().centery*2
        self.btns = [
            (Button(self.btn_conf, 'Pokemons', (centerx - 100, h-180)), None),
            (Button(self.btn_conf, 'Equipe', (centerx + 120, h-180)), self.equipe),
            (Button(self.btn_conf, 'Start', (centerx - 100, h-100)), self.start),
            (Button(self.btn_conf, '...', (centerx+120, h-100)), self.start),
            (Button(self.btn_conf, 'Quit', (centerx, h-20)), gamequit),
        ]

    def draw(self):
        centerx = self.bg.get_rect().centerx
        centery = self.bg.get_rect().centery

        drawOn(self.bg, self.bg_menu, (centerx, centery), origine=5)
        drawOn(self.bg, self.logo_pokemon, (centerx, 90), origine=5)
        drawOn(self.bg, self.logo_kaira, (centerx+30, 20))

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

    def equipe(self):
        print("equipe")

    def start(self):
        print("start")
