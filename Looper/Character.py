import pygame as pg
import time
import random
from Images import *
from Sounds import *
from Views.Levels import *
from Settings import *
vec = pg.math.Vector2

class Character(pg.sprite.Sprite):
    items = pg.sprite.Group()
    projectiles = pg.sprite.Group()
    dead = False
    spawned = True
    right = True
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
        if key[pg.K_RIGHT]:
            self.pos.x += charAcc
            self.frame_count += 1
            if self.frame_count > 2:
                self.index += 1
                self.frame_count = 0
            if self.index == len(looper_char):
                self.index = 0
            self.image = looper_char[self.index]
            self.right = True
            self.spawned = False
        if key[pg.K_LEFT]:
            self.pos.x -= charAcc
            self.frame_count += 1
            if self.frame_count > 2:
                self.index += 1
                self.frame_count = 0
            if self.index == len(looper_char):
                self.index = 0
            self.image = pg.transform.flip(looper_char[self.index], True, False)
            self.right = False
            self.spawned = False

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
        self.acc = vec(0, charGrav)
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
        projectile = Projectile(self.pos.x, self.pos.y, self.right, self.spawned)
        self.projectiles.add(projectile)
        self.shooting = True
    
    def drop(self):
        # 25% DropRate for a potion
        p = 0
        if random.randint(0, 3) == p:
            self.potion = True
        self.points += 1


class Projectile(pg.sprite.Sprite):

    def __init__(self, charx, chary, direction, spawned):
        pg.sprite.Sprite.__init__(self)
        self.image = bullet1
        self.direction = direction
        self.spawned = spawned
        self.rect = self.image.get_rect(x=-50)
        self.pos = vec(charx, chary)

    def update(self, charx):
        # Add the velocity to the position vector to move the sprite.
        if self.direction and not self.spawned:
            self.pos += vec(bullet1Speed, 0)
            self.rect.center = self.pos
        if not self.direction and not self.spawned:
            self.pos -= vec(bullet1Speed, 0)
            self.rect.center = self.pos
        if self.pos.x > charx + bullet_range and self.direction:
            self.kill()
        if self.pos.x < charx - bullet_range and not self.direction:
            self.kill()
