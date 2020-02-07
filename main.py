#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from pages.pageMenu import PageMenu
from pages.pageCombat import PageCombat
from pages.pageEquipe import PageEquipe
from utils import *

from models.pokemon import Pokemon

pygame.init()
clock = pygame.time.Clock()


class Game:
    def __init__(self, name):
        pygame.display.set_icon(loadImg('icon/icon.png', convert=False))
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption(name)

        self.loop = True
        self.allPages = {
            'Menu': PageMenu(self.screen),
            'Comb': PageCombat(self.screen),
            'Equi': PageEquipe(self.screen),
        }
        self.page = None

    def infinite_loop(self):
        while self.loop:
            if self.page is None:
                self.page = self.allPages['Menu']
            self.page.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamequit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    print(event.pos)
                elif event.type == CHANGEPAGE:
                    self.page = self.allPages[event.page]
                    self.page.last_page = event.source
                else:
                    self.page.event(event)

            self.page.update()

            # Ajout du fond dans la fenêtre
            self.page.display(self.screen)
            # Actualisation de l'affichage
            pygame.display.update()
            # 10 fps
            clock.tick(10)


if __name__ == '__main__':
    Pokemon.init_class()
    game = Game('Poké-KAIRA')
    game.infinite_loop()
