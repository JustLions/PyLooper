import pygame as pg


class Platform(pg.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h), pg.SRCALPHA, 32 )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y