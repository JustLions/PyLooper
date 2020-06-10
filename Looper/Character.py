import pygame as pg
import time
import random
from Images import *
from Sounds import *
from Views.Levels import *
from Settings import *
vec = pg.math.Vector2


class Character(pg.sprite.Sprite):
    bgX = 0; bgX2 = bg.get_width()
    dead = False
    image = looper_char_right

    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = looper_char_R[0]
        self.rect = self.image.get_rect(x=50, y=625)
        self.pos = vec(50, 625)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.points = 0
        self.hp = start_hp
        self.index = 0
        self.frame_count = 0

    def update(self):
        hit_platform = pg.sprite.spritecollide(self, self.level1.platforms, 0)
        char_hit_enemy = pg.sprite.spritecollide(self, self.level1.enemies, 0)

        # Actions when hit occurs
        if hit_platform:
            self.pos.y = 625  # Aquí con más plataformas tendremos que decirle que se quede en pos.y de la plataforma
        if char_hit_enemy:
            self.die()

        # The function event.pump() sends the events that are ocurring
        pg.event.pump()
        key = pg.key.get_pressed()

        if key[pg.K_SPACE] and hit_platform:
            self.jump(hit_platform, char_hit_enemy)
        if key[pg.K_q]:
            self.die()
        if self.pos.x < 800:
            if key[pg.K_RIGHT]:
                self.pos.x += charAcc
                self.frame_count += 1
                if self.frame_count > 2:
                    self.index += 1
                    self.frame_count = 0
                if self.index == len(looper_char_R):
                    self.index = 0
                self.image = looper_char_R[self.index]
                self.bgX -= scroll_speed
                self.bgX2 -= scroll_speed
        if self.pos.x >= 800:
            self.frame_count += 1
            if self.frame_count > 2:
                self.index += 1
                self.frame_count = 0
            if self.index == len(looper_char_R):
                self.index = 0
            self.image = looper_char_R[self.index]
            self.bgX -= scroll_speed
            self.bgX2 -= scroll_speed
        if key[pg.K_LEFT]:
            self.pos.x -= charAcc
            self.frame_count += 1
            if self.frame_count > 2:
                self.index += 1
                self.frame_count = 0
            if self.index == len(looper_char_L):
                self.index = 0
            self.image = looper_char_L[self.index]
            self.bgX += scroll_speed
            self.bgX2 += scroll_speed
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_w:
                self.level1.shoot()
                self.points += 1

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
            self.pos.x = bg.get_width()
        if self.pos.x < 0:
            self.pos.x = 0

    def jump(self, hit_platform, char_hit_enemy):
        # jump_sound()
        self.pos.y += -jump_height
        if hit_platform or char_hit_enemy:
            self.vel.y = -jump_height/2.5
        self.acc = vec(0, 5)

    def die(self):
        if self.hp > 0:
            self.hp = self.hp - hp_loss
        else:
            pg.sprite.spritecollide(self, self.level1.characters, 1)
            Character.dead = True


class Enemy(pg.sprite.Sprite):

    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = enemy_koopa_left
        self.rect = self.image.get_rect(x=1000, y=650)
        self.pos = vec(1000, 650)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        hit_platform = pg.sprite.spritecollide(self, self.level1.platforms, 0)

        if hit_platform:
            self.pos.y = 650
            self.pos.x = 1000

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
            self.pos.x = bg.get_width()
        if self.pos.x < 0:
            self.pos.x = 0


class Projectile(pg.sprite.Sprite):
    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = bullet1
        character = Character(self)
        self.rect = self.image.get_rect(x=-50, y=character.pos.y)
        self.pos = vec(50, 650)

    def update(self):
        self.pos.x += bullet1Speed
        self.rect.center = self.pos







