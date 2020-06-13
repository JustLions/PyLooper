import pygame as pg
import time
import random
from Images import *
from Sounds import *
from Views.Levels import *
from Settings import *
vec = pg.math.Vector2


class Wolf(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.flip(wolf, True, False)
        self.rect = self.image.get_rect(x=1000, y=675)
        self.pos = vec(1000, 675)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.hp = 100
        self.rect.center = self.pos

    def update(self):
        self.pos.x -= 10

    def jump(self):
        self.pos -= vec(-10, 0)
