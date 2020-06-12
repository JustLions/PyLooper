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
    items = pg.sprite.Group()
    projectiles = pg.sprite.Group()
    dead = False
    potion = False
    shooting = False

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = looper_char_standing
        self.rect = self.image.get_rect(x=25, y=690)
        self.pos = vec(100, 650)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.points = 0
        self.hp = start_hp
        self.index = 0
        self.frame_count = 0

    def update(self):
        # The function event.pump() sends the events that are ocurring
        pg.event.pump()
        key = pg.key.get_pressed()

        # Movement
        if self.pos.x < 800 and self.bgX >= -bg.get_width() + 15:
            if key[pg.K_RIGHT]:
                self.pos.x += charAcc
                self.frame_count += 1
                if self.frame_count > 2:
                    self.index += 1
                    self.frame_count = 0
                if self.index == len(looper_char):
                    self.index = 0
                self.image = looper_char[self.index]
                self.bgX -= scroll_speed
                self.bgX2 -= scroll_speed
        if self.pos.x >= 800 and self.bgX >= -bg.get_width() + 15 and key[pg.K_RIGHT]:
            self.frame_count += 1
            if self.frame_count > 2:
                self.index += 1
                self.frame_count = 0
            if self.index == len(looper_char):
                self.index = 0
            self.image = looper_char[self.index]
            self.bgX -= scroll_speed
            self.bgX2 -= scroll_speed
        if self.bgX <= 0 and key[pg.K_LEFT]:
            self.frame_count += 1
            if self.frame_count > 2:
                self.index += 1
                self.frame_count = 0
            if self.index == len(looper_char):
                self.index = 0
            self.image = pg.transform.flip(looper_char[self.index], True, False)
            self.bgX += scroll_speed
            self.bgX2 += scroll_speed

        # Skills
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_w:
                self.shoot()
            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                self.jump()

        # Items
        if self.potion and key[pg.K_1]:
            self.potion = False
            if 50 <= self.hp < 100:
                self.hp = 100
            else:
                self.hp = self.hp + 50

        # Updates the rectangle position
        self.rect.center = self.pos

        # Apply friction and motion
        self.acc = vec(0, charGrav)  # Entender bien
        self.acc += self.vel * charFric

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.pos.x > W:
            self.pos.x = bg.get_width()
        if self.pos.x < 75:
            self.pos.x = 75

    def jump(self):
        # jump_sound()
        self.pos.y += -jump_height
        self.vel.y = -jump_height / 2.5
        self.acc = vec(0, 5)

    def shoot(self):
        projectile = Projectile(self.pos.x, self.pos.y)
        self.projectiles.add(projectile)
        self.shooting = True
    
    def drop(self):
        self.potion = True
        self.points += 1


class Enemy(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.flip(wolf, True, False)
        self.rect = self.image.get_rect(x=1000, y=675)
        self.pos = vec(1000, 675)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):

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


class Item(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = health_potion_50
        self.rect = self.image.get_rect(x=920, y=700)
        self.pos = vec(900, 700)


class Projectile(pg.sprite.Sprite):

    def __init__(self, charx, chary):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet1
        self.rect = self.image.get_rect()
        self.pos = vec(charx, chary)

    def update(self, charx):
        # Add the velocity to the position vector to move the sprite.
        self.pos += vec(bullet1Speed, 0)
        self.rect.center = self.pos
        if self.pos.x > charx + bullet_range:
            self.kill()






