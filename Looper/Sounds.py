import pygame as pg
import random

jump_sounds = ["Sounds/Hop1.wav", "Sounds/Hop2.wav", "Sounds/Hop3.wav", "Sounds/Hop4.wav"]
punch_sounds = ["Sounds/punchAgain.wav"]

pg.mixer.init(44100, 16, 2, 4096)


def jump_sound():
    jump = pg.mixer.Sound(jump_sounds[random.randint(0, 4)])
    jump.play()

