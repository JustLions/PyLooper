from Views.Images import *
from Settings import *


class CreateFloor(pg.sprite.Sprite):

    def __init__(self, floorx, floory, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = (floorx, floory)


class CreatePlatform(pg.sprite.Sprite):

    def __init__(self, platx, platy, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = platform1
        self.rect = self.image.get_rect()
        self.rect.center = (platx, platy)


class CreateFireball(pg.sprite.Sprite):

    def __init__(self, fireb_x, fireb_y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = fireball_1
        self.x = fireb_x
        self.y = fireb_y
        self.rect = self.image.get_rect()
        self.rect.center = (fireb_x, fireb_y)

    def update(self):
        self.rect.y -= fireball_speed
        if self.rect.center < (self.x, 0):
            self.rect.center = (self.x, self.y + 25)


class CreateFireballExit(pg.sprite.Sprite):

    def __init__(self, fireexit_x, fireexit_y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = fireball_exit
        self.x = fireexit_x
        self.y = fireexit_y
        self.rect = self.image.get_rect(x=fireexit_x, y=fireexit_y)
