import pygame as pg

# Character
looper_char_standing = pg.transform.scale(pg.image.load("Images/Character/looper1_standing.png"), (150, 150))

looper_char = []
looper_char1 = looper_char.append(pg.transform.scale(pg.image.load("Images/Character/looper_walk1.png"), (150, 150)))
looper_char2 = looper_char.append(pg.transform.scale(pg.image.load("Images/Character/looper_walk2.png"), (150, 150)))
looper_char3 = looper_char.append(pg.transform.scale(pg.image.load("Images/Character/looper_walk3.png"), (150, 150)))

# UI
item_bar = pg.transform.scale(pg.image.load("Images/Character/itembar.png"), (350, 60))
health_bar_100 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_100.png"), (200, 50))
health_bar_75 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_75.png"), (200, 50))
health_bar_50 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_50.png"), (200, 50))
health_bar_25 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_25.png"), (200, 50))
health_bar_0 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_0.png"), (200, 50))

enemy_health_bar_100 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_100.png"), (100, 30))
enemy_health_bar_75 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_75.png"), (100, 30))
enemy_health_bar_50 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_50.png"), (100, 30))
enemy_health_bar_25 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_25.png"), (100, 30))
enemy_health_bar_0 = pg.transform.scale(pg.image.load("Images/Character/Health_bar_0.png"), (100, 30))

# Events
fireball_1 = pg.transform.rotate(pg.transform.scale(pg.image.load("Images/Events/fireball_1.png"), (50, 50)), 270)

# Items
health_potion_50 = pg.transform.scale(pg.image.load("Images/Items/health_potion_50.png"), (50, 60))

# Enemies
scorpion = pg.transform.scale(pg.image.load("Images/Enemies/scorpion.png"), (200, 200))
wolf = pg.transform.scale(pg.image.load("Images/Enemies/wolf.png"), (200, 200))

# Bullets
bullet1= pg.transform.scale(pg.image.load("Images/Character/bullet1.png"), (25, 25))

# Environment
sun = pg.transform.scale(pg.image.load("Images/Environment/sun.png"), (150, 150))
tree1 = pg.transform.scale(pg.image.load("Images/Environment/tree1.png"), (800, 350))
tree2 = pg.transform.scale(pg.image.load("Images/Environment/tree2.png"), (500, 500))
tree3 = pg.transform.scale(pg.image.load("Images/Environment/tree3.png"), (500, 500))
fireball_exit = pg.transform.scale(pg.image.load("Images/Events/fireball_exit.gif"), (75, 50))

floor = pg.transform.scale(pg.image.load("Images/Environment/suelo.png"), (1600, 450))
bg = pg.transform.scale(pg.image.load("Images/Environment/background.png"), (1600, 700))

# Platforms

platform1 = pg.transform.scale(pg.image.load("Images/Environment/platform1.png"), (300, 50))

# Buttons
reset_button = pg.transform.scale(pg.image.load("Images/reset_button.png"), (150, 125))
reset_button_onhover = pg.transform.scale(pg.image.load("Images/reset_button_onhover.png"), (150, 125))
