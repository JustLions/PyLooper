import sys
import pygame as pg
import time
import random

# Inicializamos pygame
pg.init()

# Propiedades Ventana
W, H = 800, 600
size = pg.display.set_mode((W,H))
pg.display.set_caption("Looper")

looper_character = pg.image.load("looper_char.png")
looper_character = pg.transform.scale(looper_character, (90, 90))
sun = pg.image.load("sun.png")
sun = pg.transform.scale(sun, (80, 80))
floor = pg.image.load("suelo.jpg")
floor = pg.transform.scale(floor, (800, 100))
bg = pg.image.load("background.gif")
bg = pg.transform.scale(bg, (800, 500))
bgX = 0
bgX2 = bg.get_width()
size.blit(sun, (150, 100))
size.blit(floor, (0, 500))


# Propiedades Juego
intro = True
name = "Leon"
clock = pg.time.Clock()


class Character:
    dead = False

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.jumpCount = 0
        self.runCount = 0

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.top < -200:
            self.pos.bottom = 800


def game_score():
    points = 0
    timepassed = 0


def looper_char(x, y):
    size.blit(looper_character, (x, y))


def redraw_window():
    size.blit(bg, (bgX, 0))  # draws our first bg image
    size.blit(bg, (bgX2, 0))  # draws the seconf bg image
    pg.display.update()  # updates the screen


x = 0; y = 410; x_change = 0; y_change = 0
looper_char_speed = 0

# Texto al salir
white = (255, 255, 255); green = (0, 255, 0); blue = (0, 0, 128)
font = pg.font.Font('freesansbold.ttf', 32)
text = font.render('Goodbye ' + name + '!', True, green, blue)
textX = 200; textY = 200
textRect = text.get_rect(); textRect.center = (textX // 2, textY // 2)

while not Character.dead:
    if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x_change = 10
            if event.key == pg.K_LEFT:
                x_change = -10
            if event.key == pg.K_UP:
                y_change = -20
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                x_change = 0
        elif event.type == pg.QUIT:
            display_surface = pg.display.set_mode((textX, textY))
            display_surface.blit(text, textRect)
            time.sleep(1)
            pg.quit()
            sys.exit()
    size.fill((0, 0, 0))
    size.blit(bg, (0, 0))
    size.blit(sun, (150, 100))
    size.blit(floor, (0, 500))
    x += x_change
    y = 410 + y_change
    looper_char(x, y)
    clock.tick(60)
    pg.display.update()
