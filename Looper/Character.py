# Sprite classes for platform game
import pygame as pg
import time
from Images import *
from Settings import *
vec = pg.math.Vector2

class Character(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = looper_char_right
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.pos = vec(0, 650)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.pos.y += -30
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        if hits:
            self.vel.y = -30
        self.acc = vec(0, 5)

    def update(self):
        self.acc = vec(0, charGrav)  # Entender bien
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -charAcc
            self.image = looper_char_left
        if keys[pg.K_RIGHT]:
            self.acc.x = charAcc
            self.image = looper_char_right
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        if keys[pg.K_SPACE] and hits:
            self.jump()
        # apply friction
        self.acc += self.vel * charFric
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > W:
            self.pos.x = 1600
        if self.pos.x < 0:
            self.pos.x = H

        self.rect.center = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((1600, 650), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


