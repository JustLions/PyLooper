import pygame as pg
import random

# Game Settings
W, H = 1600, 900
x = 0; y = 650; x_change = 0; y_change = 0
FPS = 60
Title = 'Looper'

# Map Settings

map_x_size = 5000
map_y_size = 900

# Colors and Font
black = (0, 0, 0); white = (255, 255, 255); green = (0, 255, 0); blue = (0, 0, 128)

# Player properties
charAcc = 15
charGrav = 3
charFric = -0.12
jump_height = 120
hp_loss = 5
start_hp = 100

# Enemy properties
EnemySpeed = 30

# Map properties
scroll_speed = 10

# Event properties
fireball_speed = 30
fireball_damage = 7

# Projectile properties
bullet1Speed = 20
bullet_range = 350

# Platforms (x, y, width, height)
Floor = [(800, 775, 10000, 50)]
Platforms = [(2000, 600, 267, 50), (2500, 520, 293, 50), (3000, 450, 267, 50)]
Objects = [(2266, 730, 200, 200), (2750, 730, 200, 200)]
Projectiles = [(50, 600, 25, 25)]
Fireballs = [(2300, 700, 50, 50), (2788, 700, 50, 50)]
Items = [(800, 700, 50, 75)]
Buttons = [(700, 450, 100, 100)]

# Items
ITEM_LIST = []
