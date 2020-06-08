import pygame as pg
import time
import random
from Images import *
from Sounds import *
from Views.Levels import *
from Settings import *
vec = pg.math.Vector2


class Character(pg.sprite.Sprite):

    dead = False

    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = looper_char_right
        self.rect = self.image.get_rect(x=50, y=650)
        self.pos = vec(50, 650)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        hit_platform = pg.sprite.spritecollide(self, self.level1.platforms, 0)
        char_hit_enemy = pg.sprite.spritecollide(self, self.level1.enemies, 0)

        # Actions when hit occurs
        if hit_platform:
            self.pos.y = 650  # Aquí con más plataformas tendremos que decirle que se quede en pos.y de la plataforma
        if char_hit_enemy:
            self.die()

        # The function event.pump() sends the events that are ocurring
        pg.event.pump()
        key = pg.key.get_pressed()

        if key[pg.K_SPACE] and hit_platform:
            self.jump(hit_platform, char_hit_enemy)
        if key[pg.K_q]:
            self.die()
        if key[pg.K_RIGHT]:
            self.pos.x += charAcc
            self.image = looper_char_right
        if key[pg.K_LEFT]:
            self.pos.x -= charAcc
            self.image = looper_char_left

        # Updates the rectangle position
        self.rect.center = self.pos

        # Apply friction
        self.acc = vec(0, charGrav)  # Entender bien
        self.acc += self.vel * charFric

        # Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.pos.x > W:
            self.pos.x = 1600
        if self.pos.x < 0:
            self.pos.x = 0

    def jump(self, hit_platform, char_hit_enemy):
        # jump_sound()
        self.pos.y += -45
        if hit_platform or char_hit_enemy:
            self.vel.y = -30
        self.acc = vec(0, 5)

    def die(self):
        pg.sprite.spritecollide(self, self.level1.characters, 1)
        Character.dead = True


class Enemy(pg.sprite.Sprite):

    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = enemy_koopa_left
        self.rect = self.image.get_rect(x=650)
        self.pos = vec(random.randint(0, 1600), 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        hit_platform = pg.sprite.spritecollide(self, self.level1.platforms, 0)

        if hit_platform:
            self.pos.y = 0
            self.pos.x = random.randint(0, 1600)

        # Updates the rectangle position
        self.rect.center = self.pos

        # Apply friction
        self.acc = vec(0, charGrav)
        self.acc += self.vel * charFric

        # Equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.pos.x > W:
            self.pos.x = 1600
        if self.pos.x < 0:
            self.pos.x = 0






