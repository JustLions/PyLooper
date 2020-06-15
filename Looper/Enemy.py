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
        self.pos = vec(2800, 725)
        self.rect = self.image.get_rect(x=self.pos.x-175, y=self.pos.y-148)
        self.hp = 100
