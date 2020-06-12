from Views.Levels import *


class Game:

    def __init__(self):
        Level1()

    def run(self):
        level1.draw()
        level1.interactions()
        level1.update()
