#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import sys
from utils import *

from pokemon import Pokemon

pygame.init()
clock = pygame.time.Clock()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
CIEL = 0, 200, 255
RED = 255, 0, 0
ORANGE = 255, 100, 0
GREEN = 0, 255, 0


class Button:
    sprites = list()

    @classmethod
    def init_sprite(cls):
        cls.sprites.append({False: scale(loadImg("icon/bt_black_off.png"), 0.4),
                            True: scale(loadImg("icon/bt_black_on.png"), 0.4)})

    def __init__(self, fond, text, pos):
        self.text = text
        self.state = False  # enable or not
        self.type = 0
        self.title = pygame.font.SysFont('freesans', 36).render(self.text, True, BLACK)
        textpos = self.title.get_rect()
        textpos.centerx = pos[0]
        textpos.centery = pos[1]
        self.textpos = [textpos[0], textpos[1], textpos[2], textpos[3]]
        self.rect = pygame.draw.rect(fond, (0, 0, 0), self.textpos)
        self.display_button(fond)

    def update_button(self, fond, action=None):
        over = self.rect.collidepoint(pygame.mouse.get_pos())
        if over:
            if action is not None:
                action()
            self.state = not self.state
        self.display_button(fond)

    def display_button(self, fond):
        btn_on = self.state != self.rect.collidepoint(pygame.mouse.get_pos())
        drawOn(fond, Button.sprites[self.type][btn_on], self.textpos, center=True)
        drawOn(fond, self.title, self.textpos, center=True)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        self.loop = True
        self.level = 1

        self.bg_menu = scale(loadImg("bg/menu2.jpg"), 0.7)
        self.logo_pokemon = scale(loadImg("logo/pokemon.png"), 0.3)
        self.logo_kaira = scale(loadImg("logo/kaira_bord.png"), 0.2)
        Button.init_sprite()
        # Définition de la police
        self.big = pygame.font.SysFont('freesans', 48)
        self.small = pygame.font.SysFont('freesans', 36)

        # Image de la taille de la fenêtre
        self.fond = pygame.Surface(self.screen.get_size())
        self.draw_bg()
        self.create_button()

    def update_textes(self):
        self.textes = [["Level", BLACK, self.small, 0, 150],
                       [str(self.level), BLACK, self.small, 0, 200]]

    def draw_bg(self):
        centre = xAll(self.fond.get_rect().size, 0.5)
        drawOn(self.fond, self.bg_menu, centre, center=True)
        drawOn(self.fond, self.logo_pokemon, (centre[0], 90), center=True)

        logo_kaira = pygame.transform.rotate(self.logo_kaira, 20)
        drawOn(self.fond, logo_kaira, (centre[0]+30, 20))

    def create_button(self):
        centerx = self.fond.get_rect().centerx
        self.btns = [
            (Button(self.fond, 'Pokemon', (centerx-100, 300)), self.plus),
            (Button(self.fond, 'Reset', (centerx+100, 300)), reset),
            (Button(self.fond, 'Start', (centerx, 360)), start),
            (Button(self.fond, 'Quit', (centerx, 420)), gamequit),
        ]

    def display_text(self, text, color, font, dx, dy):
        '''Ajout d'un texte sur fond. Décalage dx, dy par rapport au centre.
        '''
        mytext = font.render(text, True, color)  # True pour antialiasing
        textpos = mytext.get_rect()
        textpos.centerx = self.fond.get_rect().centerx + dx
        textpos.centery = dy
        self.fond.blit(mytext, textpos)

    def plus(self):
        self.level += 1
        if self.level == 6:
            self.level = 5

    def moins(self):
        self.level += -1
        if self.level == 0:
            self.level = 1

    def infinite_loop(self):
        while self.loop:
            self.draw_bg()

            for btn, action in self.btns:
                btn.display_button(self.fond)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gamequit()
                elif event.type == pygame.MOUSEMOTION:
                    for btn, action in self.btns:
                        btn.update_button(self.fond)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for btn, action in self.btns:
                        btn.update_button(self.fond, action=action)

            self.update_textes()
            for text in self.textes:
                self.display_text(text[0], text[1], text[2],
                                        text[3], text[4])

            # Ajout du fond dans la fenêtre
            self.screen.blit(self.fond, (0, 0))
            # Actualisation de l'affichage
            pygame.display.update()
            # 10 fps
            clock.tick(10)


def reset():
    print("reset")
    for p in Pokemon.listPokemon:
        print(str(p))


def start():
    print("start")


def gamequit():
    print("Quit")
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    Pokemon.initClass()
    game = Game()
    game.infinite_loop()
