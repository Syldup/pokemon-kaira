import pygame


BLACK = 0, 0, 0
WHITE = 255, 255, 255
CIEL = 0, 200, 255
RED = 255, 0, 0
ORANGE = 255, 100, 0
GREEN = 0, 255, 0


def gamequit():
    print("Quit")
    pygame.quit()
    import sys
    sys.exit()


def loadImg(path, convert=True):
    img = pygame.image.load('assets/' + path)
    if convert:
        img.convert()
    return img


def xAll(l, n):
    return list(int(i*n) for i in l)


def scale(img, n):
    return pygame.transform.scale(img, xAll(img.get_rect().size, n))


def drawOn(surface, img, xy=(0, 0), center=False, scal=1.0):
    if scal != 1.0:
        img = scale(img, scal)
    return surface.blit(img, xy if not center else list(int(p-o/2) for p, o in zip(xy, img.get_rect().size)))


class Button:
    def __init__(self, conf, text, pos):
        self.text = text
        self.overflew = False
        self.state = False  # enable or not

        self.bg = conf['bg']
        self.sprite = conf['sprite'].copy()
        self.sprite['text'] = conf['font'].render(self.text, True, WHITE)

        self.pos = self.sprite[self.state].get_rect()
        self.pos.centerx, self.pos.centery = pos

        self.rect = self.display_button()
        self.overflew = conf['overflew']

    def update_button(self, action=None):
        self.state = self.rect.collidepoint(pygame.mouse.get_pos())
        if self.state:
            if action is not None:
                action()
        self.display_button()

    def display_button(self):
        if self.overflew:
            self.state = self.rect.collidepoint(pygame.mouse.get_pos())
        rect = drawOn(self.bg, self.sprite[self.state], self.pos, center=True)
        drawOn(self.bg, self.sprite['text'], self.pos, center=True)
        return rect
