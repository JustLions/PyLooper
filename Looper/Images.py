import pygame as pg

looper_char_right = pg.image.load("looper_char_right.png")
looper_char_right = pg.transform.scale(looper_char_right, (100, 100))
looper_char_left = pg.image.load("looper_char_left.png")
looper_char_left = pg.transform.scale(looper_char_left, (100, 100))
sun = pg.image.load("sun.png")
sun = pg.transform.scale(sun, (150, 150))
floor = pg.image.load("suelo.jpg")
floor = pg.transform.scale(floor, (1600, 200))
bg = pg.image.load("background.gif")
bg = pg.transform.scale(bg, (1600, 700))