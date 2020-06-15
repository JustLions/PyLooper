import pygame as pg
from Images import *


class CreateFloor(pg.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class CreatePlatform(pg.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = platform1
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)