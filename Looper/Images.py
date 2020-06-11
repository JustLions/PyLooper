import pygame as pg

# Character
looper_char_standing = pg.image.load("Images/Character/looper1_standing.png")
looper_char_standing = pg.transform.scale(looper_char_standing, (150, 150))

looper_char = []
looper_char1 = pg.image.load("Images/Character/looper_walk1.png")
looper_char2 = pg.image.load("Images/Character/looper_walk2.png")
looper_char3 = pg.image.load("Images/Character/looper_walk3.png")
looper_char1_resize = looper_char.append(pg.transform.scale(looper_char1, (150, 150)))
looper_char2_resize = looper_char.append(pg.transform.scale(looper_char2, (150, 150)))
looper_char3_resize = looper_char.append(pg.transform.scale(looper_char3, (150, 150)))


# UI
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

# Items
health_potion_50 = pg.image.load("Images/Items/health_potion_50.png")
health_potion_50 = pg.transform.scale(health_potion_50, (50, 75))

# Enemies
scorpion = pg.image.load("Images/Enemies/scorpion.png")
scorpion_resize = pg.transform.scale(scorpion, (200, 200))

wolf = pg.image.load("Images/Enemies/wolf.png")
wolf = pg.transform.scale(wolf, (200, 200))


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

floor = pg.image.load("Images/Environment/suelo.png")
floor = pg.transform.scale(floor, (1600, 450))
bg = pg.image.load("Images/Environment/background.png")
bg = pg.transform.scale(bg, (1600, 700))

reset_button = pg.image.load("Images/reset_button.png")
reset_button = pg.transform.scale(reset_button, (150, 125))

reset_button_onhover = pg.image.load("Images/reset_button_onhover.png")
reset_button_onhover = pg.transform.scale(reset_button_onhover, (150, 125))
