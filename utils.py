import pygame
from pygame.rect import Rect
from models.GIFImage import GIFImage


BLACK = 0, 0, 0
WHITE = 255, 255, 255
GRIS = 128, 128, 128
CIEL = 0, 200, 255
RED = 255, 0, 0
ORANGE = 255, 100, 0
GREEN = 0, 255, 0
CHANGEPAGE = pygame.USEREVENT + 1


def gamequit():
    print("Quit")
    pygame.quit()
    import sys
    sys.exit()


def loadImg(path: str, convert: bool=True):
    img = pygame.image.load('assets/' + path)
    if convert:
        img.convert()
    return img


def xAll(l, n):
    return list(int(i*n) for i in l)


def sumList(*args):
    return list(sum(a) for a in zip(*args))


def scale(img, n):
    return pygame.transform.scale(img, xAll(img.get_rect().size, n))


def moveOrigine(rect, origine):
    d = 1 + origine // 10
    origine = origine % 10 - 1
    offset = list(-int(c/2 * (offset-1)) for c, offset in zip(rect.size, [origine % 3, origine // 3]))
    return rect.move(*xAll(offset, d))


def drawOn(surface, img, xy=(0, 0), origine=1, scal=1.0, *args, **kwargs):
    if scal != 1.0:
        img = scale(img, scal)
    if origine != 1:
        xy = moveOrigine(img.get_rect(center=xy[:2]), origine)[:2]

    if isinstance(img, GIFImage):
        return img.render(surface, xy)
    return surface.blit(img, xy, *args, **kwargs)


class Button:
    def __init__(self, conf, text, pos, origine=5, action=None):
        self.text = text
        self.overflew = conf['overflew']
        self.state = False  # enable or not
        self.action = action

        self.bg = conf['bg']
        self.sprite = conf['sprite'].copy()
        self.sprite['text'] = conf['font'].render(self.text, True, WHITE)

        if 'box_size' in conf:
            if conf['box_size'] in self.sprite:
                self.pos = self.sprite[conf['box_size']].get_rect(center=pos)
            else:
                self.pos = conf['box_size']
        else:
            self.pos = self.sprite[False].get_rect(center=pos)

        self.pos = moveOrigine(self.pos, origine)
        if conf['text_offset'] is None:
            pos_text = moveOrigine(self.pos, 1)
            pos_text.size = self.sprite['text'].get_size()
            self.pos_text = moveOrigine(pos_text, 9)
        else:
            self.pos_text = self.pos.move(conf['text_offset'])

    def draw(self):
        if self.overflew:
            self.state = self.pos.collidepoint(pygame.mouse.get_pos())
        if self.state in self.sprite:
            drawOn(self.bg, self.sprite[self.state], self.pos)
        drawOn(self.bg, self.sprite['text'], self.pos_text)

    def update(self):
        self.state = self.pos.collidepoint(pygame.mouse.get_pos())
        if self.state:
            if self.action:
                self.action[0](*self.action[1:])
