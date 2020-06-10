import pygame as pg

# Character
looper_char_right_pre = pg.image.load("Images/Character/looper_char_right.png")
looper_char_right = pg.transform.scale(looper_char_right_pre, (100, 100))
looper_char_left = pg.image.load("Images/Character/looper_char_left.png")
looper_char_left = pg.transform.scale(looper_char_left, (100, 100))


looper_char_R = []
looper_char1_R = pg.image.load("Images/Character/looper1_R.png")
looper_char2_R = pg.image.load("Images/Character/looper2_R.png")
looper_char3_R = pg.image.load("Images/Character/looper3_R.png")
looper_char1_resize_R = looper_char_R.append(pg.transform.scale(looper_char1_R, (150, 150)))
looper_char2_resize_R = looper_char_R.append(pg.transform.scale(looper_char2_R, (150, 150)))
looper_char3_resize_R = looper_char_R.append(pg.transform.scale(looper_char3_R, (150, 150)))

looper_char_L = []
looper_char1_L = pg.image.load("Images/Character/looper1_L.png")
looper_char2_L = pg.image.load("Images/Character/looper2_L.png")
looper_char3_L = pg.image.load("Images/Character/looper3_L.png")
looper_char1_resize_L = looper_char_L.append(pg.transform.scale(looper_char1_L, (150, 150)))
looper_char2_resize_L = looper_char_L.append(pg.transform.scale(looper_char2_L, (150, 150)))
looper_char3_resize_L = looper_char_L.append(pg.transform.scale(looper_char3_L, (150, 150)))

item_bar = pg.image.load("Images/Character/itembar.png")
item_bar = pg.transform.scale(item_bar, (350, 60))

health_bar_100 = pg.image.load("Images/Character/Health_bar_100.png")
health_bar_100 = pg.transform.scale(health_bar_100, (200, 50))
health_bar_75 = pg.image.load("Images/Character/Health_bar_75.png")
health_bar_75 = pg.transform.scale(health_bar_75, (200, 50))
health_bar_50 = pg.image.load("Images/Character/Health_bar_50.png")
health_bar_50 = pg.transform.scale(health_bar_50, (200, 50))
health_bar_25 = pg.image.load("Images/Character/Health_bar_25.png")
health_bar_25 = pg.transform.scale(health_bar_25, (200, 50))
health_bar_0 = pg.image.load("Images/Character/Health_bar_0.png")
health_bar_0 = pg.transform.scale(health_bar_0, (200, 50))


# Enemies
enemy_koopa_right_pre = pg.image.load("Images/Enemies/enemy_koopa_right.png")
enemy_koopa_right = pg.transform.scale(enemy_koopa_right_pre, (100, 100))
enemy_koopa_left_pre = pg.image.load("Images/Enemies/enemy_koopa_left.png")
enemy_koopa_left = pg.transform.scale(enemy_koopa_left_pre, (100, 100))

# Bullets
bullet1_pre = pg.image.load("Images/Character/bullet1.png")
bullet1 = pg.transform.scale(bullet1_pre, (25, 25))

# Environment
sun = pg.image.load("Images/Environment/sun.png")
sun = pg.transform.scale(sun, (150, 150))
tree1 = pg.image.load("Images/Environment/tree1.png")
tree1 = pg.transform.scale(tree1, (800, 350))
tree2 = pg.image.load("Images/Environment/tree2.png")
tree2 = pg.transform.scale(tree2, (500, 500))
tree3 = pg.image.load("Images/Environment/tree3.png")
tree3 = pg.transform.scale(tree3, (500, 500))

floor = pg.image.load("Images/Environment/suelo.jpg")
floor = pg.transform.scale(floor, (1600, 200))
bg = pg.image.load("Images/Environment/background.png")
bg = pg.transform.scale(bg, (1600, 700))

reset_button = pg.image.load("Images/reset_button.png")
reset_button = pg.transform.scale(reset_button, (150, 125))

reset_button_onhover = pg.image.load("Images/reset_button_onhover.png")
reset_button_onhover = pg.transform.scale(reset_button_onhover, (150, 125))
