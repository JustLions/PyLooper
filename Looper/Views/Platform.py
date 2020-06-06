import pygame as pg
import random


class Platform(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1600, 50), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (800, 724)

    def update(self):
        self.rect.x += 0
        if self.rect.x > 1600:
            self.rect.x = 0
