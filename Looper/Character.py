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
    projectiles = pg.sprite.Group()
    items = pg.sprite.Group()
    dead = False
    potion = False

    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.projectile = Projectile(level1)
        self.item = Item(level1)
        self.level1 = level1
        self.enemies = level1.enemies
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
        hit_platform = pg.sprite.spritecollide(self, self.level1.platforms, 0)
        char_hit_enemy = pg.sprite.spritecollide(self, self.level1.enemies, 0)

        # Actions when hit occurs
        if hit_platform:
            self.pos.y = 690  # Aquí con más plataformas tendremos que decirle que se quede en pos.y de la plataforma
        if char_hit_enemy:
            self.die()

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
        if key[pg.K_SPACE] and hit_platform:
            self.jump(hit_platform)
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_w:
                self.shoot(self.level1)
                self.projectiles.add(self.projectile)
                self.projectile.pos = vec(self.pos.x + 50, self.pos.y)
        if self.potion and key[pg.K_1]:
            self.potion = False
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

    def jump(self, hit_platform):
        # jump_sound()
        self.pos.y += -jump_height
        if hit_platform:
            self.vel.y = -jump_height/2.5
        self.acc = vec(0, 5)

    def shoot(self, level1):
        self.level1 = level1
        level1.projectiles.add(Projectile(self))

    def drop(self):
        self.potion = True
        self.points += 1

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
        self.image = pg.transform.flip(wolf, True, False)
        self.rect = self.image.get_rect(x=1000 + self.level1.character.bgX, y=675)
        self.pos = vec(1000 + self.level1.character.bgX, 675)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        hit_platform = pg.sprite.spritecollide(self, self.level1.platforms, 0)
        if hit_platform:
            self.pos.y = 675
            self.pos.x = 1000 + self.level1.character.bgX

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
    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = health_potion_50
        self.rect = self.image.get_rect(x=920, y=700)
        self.pos = vec(900, 700)


class Projectile(pg.sprite.Sprite):
    def __init__(self, level1):
        pg.sprite.Sprite.__init__(self)
        self.level1 = level1
        self.image = bullet1
        self.rect = self.image.get_rect(x=-50, y=60)
        self.pos = vec(120, 645)

    def update(self):
        # Add the velocity to the position vector to move the sprite.
        self.pos += vec(bullet1Speed, 0)
        self.rect.center = self.pos
        projectile_hit_enemy = pg.sprite.spritecollide(self, self.level1.enemies, 1)
        if projectile_hit_enemy:
            self.kill()
            Character.drop(self.level1)







