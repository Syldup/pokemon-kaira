import pygame


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
    surface.blit(img, xy if not center else list(int(p-o/2) for p, o in zip(xy, img.get_rect().size)))
