# Sprite classes for platform game
import pygame as pg
import time
import random
from Images import *
from Sounds import *
from Views.Levels import *
from Settings import *
vec = pg.math.Vector2


class Character(pg.sprite.Sprite):

    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = looper_char_right
        self.rect = self.image.get_rect()
        self.pos = vec(500, 650)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        self.acc = vec(0, charGrav)  # Entender bien
        hit_platform = pg.sprite.spritecollide(self, self.level1.platforms, 0)

        # The function event.pump() sends the events that are ocurring
        pg.event.pump()
        key = pg.key.get_pressed()
        if hit_platform:
            self.pos.y = 650
        if key[pg.K_SPACE] and hit_platform:
            self.jump(hit_platform)
        if key[pg.K_RIGHT]:
            self.pos.x += charAcc
            self.image = looper_char_right
        if key[pg.K_LEFT]:
            self.pos.x -= charAcc
            self.image = looper_char_left

        # Updates the rectangle position
        self.rect.center = self.pos

        # Apply friction
        self.acc += self.vel * charFric

        # Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.pos.x > W:
            self.pos.x = 1600
        if self.pos.x < 0:
            self.pos.x = 0

    def jump(self, hit_platform):
        jump_sound()
        self.pos.y += -35
        if hit_platform:
            self.vel.y = -30
        self.acc = vec(0, 5)






