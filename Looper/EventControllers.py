import pygame as pg
from Character import *


class Controller:
    def events(self, character):
        keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                Character.move()
