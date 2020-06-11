import pygame as pg
import random

# Game Settings
W, H = 1600, 900
x = 0; y = 650; x_change = 0; y_change = 0
FPS = 60
Title = 'Looper'

# Colors and Font
black = (0, 0, 0); white = (255, 255, 255); green = (0, 255, 0); blue = (0, 0, 128)

# Player properties
charAcc = 8
charGrav = 3
charFric = -0.12
jump_height = 70
hp_loss = 5
start_hp = 100

# Map properties
scroll_speed = 10

# Projectile properties
bullet1Speed = 12

# Platforms (x, y, width, height)
Platforms = [(800, 775, 1600, 50)]
Projectiles = [(50, 600, 25, 25)]
Items = [(800, 700, 50, 75)]
Buttons = [(700, 450, 100, 100)]

# Items
ITEM_LIST = []
