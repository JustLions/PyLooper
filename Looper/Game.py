from Views.Levels import *

class Game:

    def __init__(self):
        self.level1 = Level1()

    def run(self):
        self.level1.draw()
        self.level1.interactions()
        self.level1.update()
