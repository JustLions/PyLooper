import pygame as pg

# Character
looper_char_right_pre = pg.image.load("Images/Character/looper_char_right.png")
looper_char_right = pg.transform.scale(looper_char_right_pre, (100,100))
looper_char_left = pg.image.load("Images/Character/looper_char_left.png")
looper_char_left = pg.transform.scale(looper_char_left, (100, 100))

# Enemies
enemy_koopa_right_pre = pg.image.load("Images/Enemies/enemy_koopa_right.png")
enemy_koopa_right = pg.transform.scale(enemy_koopa_right_pre, (100, 100))
enemy_koopa_left_pre = pg.image.load("Images/Enemies/enemy_koopa_left.png")
enemy_koopa_left = pg.transform.scale(enemy_koopa_left_pre, (100, 100))


sun = pg.image.load("Images/Environment/sun.png")
sun = pg.transform.scale(sun, (150, 150))
floor = pg.image.load("Images/Environment/suelo.jpg")
floor = pg.transform.scale(floor, (1600, 200))
bg = pg.image.load("Images/Environment/background.gif")
bg = pg.transform.scale(bg, (1600, 700))

reset_button = pg.image.load("Images/reset_button.png")
reset_button = pg.transform.scale(bg, (100, 100))
