#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from pageMenu import PageMenu
from pageCombat import PageCombat
from pageEquipe import PageEquipe
from utils import *

from pokemon import Pokemon

pygame.init()
clock = pygame.time.Clock()


class Game:
    def __init__(self, name):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption(name)

        self.loop = True
        self.page = None
        self.allPages = {
            'Menu': PageMenu(self.screen),
            'Comb': PageCombat(self.screen),
            'Equi': PageEquipe(self.screen),
        }
        self.page = None

    def infinite_loop(self):
        while self.loop:
            if self.page is None:
                self.page = self.allPages['Equi']
            self.page.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamequit()
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
    Pokemon.initClass()
    game = Game('Poké-KAIRA')
    game.infinite_loop()
