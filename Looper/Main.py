import sys
import pygame as pg
import time
from Settings import *
from Character import *
from Images import *

# Inicializamos pygame


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(Title)
        self.screen = pg.display.set_mode((W, H))
        self.running = True

        self.clock = pg.time.Clock()

    def new(self):
        # Starts the game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        # Adds items to the sprite Group (characters, platforms, items)
        self.items = pg.sprite.Group()
        self.character = Character(self)
        self.all_sprites.add(self.character)
        for plat in Platforms:
            p = Platform(*plat)  # Falta entender
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            hits = pg.sprite.spritecollide(self.character, self.platforms, False)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and hits:
                    self.character.jump()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        if self.character.vel.y > 0:
            hits = pg.sprite.spritecollide(self.character, self.platforms, False)
            if hits:
                self.character.pos.y = hits[0].rect.top
                self.character.vel.y = 0

    def draw(self):
        # Game Loop - draw
        self.screen.blit(bg, (0, 0))
        self.screen.blit(sun, (150, 100))
        self.screen.blit(floor, (0, 700))
        self.all_sprites.draw(self.screen)
        pg.display.flip()


game = Game()

# Definimos las funciones

while game.running:
    game.new()
    pg.display.update()