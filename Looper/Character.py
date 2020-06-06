# Sprite classes for platform game
import pygame as pg
import time
from Images import *
from Views.Level1 import *
from Settings import *
vec = pg.math.Vector2


class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = looper_char_right
        self.rect = self.image.get_rect(x = 0, y = 600)
        self.pos = vec(50, 650)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, charGrav)  # Entender bien

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.pos.x += 10
                    self.rect.center = self.pos


        '''# apply friction
        self.acc += self.vel * charFric

        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # wrap around the sides of the screen
        if self.pos.x > W:
            self.pos.x = 1600
        if self.pos.x < 0:
            self.pos.x = 0'''






