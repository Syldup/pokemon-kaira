"""GIFImage by Matthew Roe"""

from PIL import Image, ImageSequence
import pygame
from pygame.locals import *

import time


class GIFImage(object):
    def __init__(self, filename, scale=1):
        self.filename = filename
        self.scale = scale
        self.image = Image.open(filename)
        self.size = list(int(d*self.scale) for d in self.image.size)
        self.frames = []
        self.get_frames()

        self.cur = 0
        self.ptime = time.time()

        self.running = True
        self.breakpoint = len(self.frames)-1
        self.startpoint = 0
        self.reversed = False

    def get_rect(self, center=None):
        if center:
            return pygame.rect.Rect(list(i-j/2 for i, j in zip(center, self.size)), self.size)
        return pygame.rect.Rect((0, 0), self.size)

    def get_frames(self):
        for image in ImageSequence.Iterator(self.image):
            try:
                duration = image.info["duration"]
            except:
                duration = 100

            x0, y0, x1, y1 = (0, 0) + image.size
            if image.tile:
                tile = image.tile
            else:
                image.seek(0)
                tile = image.tile
            if len(tile) > 0:
                x0, y0, x1, y1 = tile[0][1]

            pal = image.getpalette()
            palette = []
            for i in range(0, len(pal), 3):
                rgb = pal[i:i + 3]
                palette.append(rgb)

            pi = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
            pi.set_palette(palette)
            if "transparency" in image.info:
                pi.set_colorkey(image.info["transparency"])
            pi2 = pygame.Surface(image.size, SRCALPHA)
            pi2.blit(pi, (x0, y0), (x0, y0, x1-x0, y1-y0))
            if self.scale != 1:
                pi2 = pygame.transform.scale(pi2, self.size)
            self.frames.append([pi2, duration*.001])

    def render(self, screen, pos):
        if self.running:
            if time.time() - self.ptime > self.frames[self.cur][1]:
                if self.reversed:
                    self.cur -= 1
                    if self.cur < self.startpoint:
                        self.cur = self.breakpoint
                else:
                    self.cur += 1
                    if self.cur > self.breakpoint:
                        self.cur = self.startpoint

                self.ptime = time.time()
        img = self.frames[self.cur][0]
        return screen.blit(img, pos)

    def seek(self, num):
        self.cur = num
        if self.cur < 0:
            self.cur = 0
        if self.cur >= len(self.frames):
            self.cur = len(self.frames)-1

    def set_bounds(self, start, end):
        if start < 0:
            start = 0
        if start >= len(self.frames):
            start = len(self.frames) - 1
        if end < 0:
            end = 0
        if end >= len(self.frames):
            end = len(self.frames) - 1
        if end < start:
            end = start
        self.startpoint = start
        self.breakpoint = end

    def pause(self):
        self.running = False

    def play(self):
        self.running = True

    def rewind(self):
        self.seek(0)

    def fastforward(self):
        self.seek(self.length()-1)

    def get_height(self):
        return self.size[1]

    def get_width(self):
        return self.size[0]

    def get_size(self):
        return self.size

    def length(self):
        return len(self.frames)

    def reverse(self):
        self.reversed = not self.reversed

    def reset(self):
        self.cur = 0
        self.ptime = time.time()
        self.reversed = False

    def copy(self):
        new = GIFImage(self.filename)
        new.running = self.running
        new.breakpoint = self.breakpoint
        new.startpoint = self.startpoint
        new.cur = self.cur
        new.ptime = self.ptime
        new.reversed = self.reversed
        return new


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    img1 = GIFImage("015.gif")
    img2 = GIFImage("002.gif")
    img3 = img2.copy()
    img3.reverse()
    img4 = img2.copy()
    img4.set_bounds(0, 2)
    img5 = GIFImage("003.gif")

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                loop = False

        screen.fill((255, 255, 255))
        img1.render(screen, (50, 0))
        img2.render(screen, (200, 50))
        img3.render(screen, (50, 150))
        img4.render(screen, (50, 300))
        img5.render(screen, (200, 150))
        pygame.display.flip()
