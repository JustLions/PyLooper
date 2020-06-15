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
jump_height = 70
hp_loss = 5
start_hp = 100

# Enemy properties
EnemySpeed = 30

# Map properties
scroll_speed = 10

# Projectile properties
bullet1Speed = 20
bullet_range = 350

# Platforms (x, y, width, height)
Floor = [(800, 775, 5000, 50)]
Platforms = [(2300, 420, 293, 50), (2000, 500, 267, 50)]
Projectiles = [(50, 600, 25, 25)]
Items = [(800, 700, 50, 75)]
Buttons = [(700, 450, 100, 100)]

# Items
ITEM_LIST = []
