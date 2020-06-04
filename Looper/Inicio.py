import sys
import pygame as pg
import time

# Inicializamos pygame
pg.init()

# Propiedades Ventana
W, H = 1600, 900
size = pg.display.set_mode((W, H))
pg.display.set_caption("Looper")

looper_character = pg.image.load("looper_char.png")
looper_character = pg.transform.scale(looper_character, (100, 100))
sun = pg.image.load("sun.png")
sun = pg.transform.scale(sun, (150, 150))
floor = pg.image.load("suelo.jpg")
floor = pg.transform.scale(floor, (1600, 200))
bg = pg.image.load("background.gif")
bg = pg.transform.scale(bg, (1600, 700))
bgX = 0
bgX2 = bg.get_width()
size.blit(sun, (150, 100))
size.blit(floor, (0, 900))


# Propiedades Juego
intro = True
name = "Leon"
clock = pg.time.Clock()


# Definimos las Clases


class Character:
    dead = False
    item_double_jump = False

    def __init__(self, char_x, char_y, width, height):
        self.char_x = char_x
        self.char_y = char_y
        self.width = width
        self.height = height
        self.jumping = False
        self.jumpCount = 0
        self.runCount = 0


# Definimos las funciones


def looper_char(char_x, char_y):
    size.blit(looper_character, (char_x, char_y))


def redraw_window():
    size.blit(bg, (bgX, 0))  # draws our first bg image
    size.blit(bg, (bgX2, 0))  # draws the seconf bg image


def map_update():
    size.fill((0, 0, 0))
    size.blit(bg, (0, 0))
    size.blit(sun, (150, 100))
    size.blit(floor, (0, 700))


x = 0; y = 600; x_change = 0; y_change = 0
looper_char_speed = 0

# Texto al salir
white = (255, 255, 255); green = (0, 255, 0); blue = (0, 0, 128)
font = pg.font.Font('freesansbold.ttf', 32)
text = font.render('Goodbye ' + name + '!', True, green, blue)
textX = 200; textY = 200
textRect = text.get_rect(); textRect.center = (textX // 2, textY // 2)

isJump = False
jumpCount = 10

while not Character.dead:
    if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x_change = 8
                bgX -= 20
                bgX2 -= 20

            if event.key == pg.K_LEFT:
                x_change = -8
                bgX -= -20
                bgX2 -= -20
            if not (isJump):
                if event.key == pg.K_UP:
                    y_change = -20
                if event.key == pg.K_DOWN:
                    y_change = 20
                if event.key == pg.K_SPACE:
                    isJump = True
        if isJump and event.type == pg.KEYUP:
            # Loop que ocurre mientras salta
            while jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                # Decimos que se mueva mientras salte
                if event.key == pg.K_RIGHT:
                    x_change = 8
                    bgX -= 20
                    bgX2 -= 20
                if event.key == pg.K_LEFT:
                    x_change = -8
                    bgX -= -20
                    bgX2 -= -20
                if 0 <= x <= 710:
                    x += x_change
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
                time.sleep(0.018)
                map_update()
                looper_char(x, y)
                pg.display.update()
            else:
                isJump = False
                jumpCount = 10
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                x_change = 0
        elif event.type == pg.QUIT:
            display_surface = pg.display.set_mode((textX, textY))
            display_surface.blit(text, textRect)
            time.sleep(1)
            pg.quit()
            sys.exit()
    # Actualizamos el mapa y frames
    map_update()
    if 0 <= x <= 1510:
        x += x_change
    if x < 0:
        x = 0
    if x > 1510:
        x = 1510
    looper_char(x, y)
    clock.tick(60)
    pg.display.update()
