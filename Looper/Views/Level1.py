from Character import *
from Settings import *
from Views.Platform import *


class Level1:

    screen = pg.display.set_mode((W, H))

    def start(self):
        self.screen = pg.display.set_mode((W, H))
        self.all_sprites = pg.sprite.Group()
        self.character = Character()
        self.all_sprites.add(self.character)
        for i in Platforms:
            p = Platform(*i)
            self.all_sprites.add(p)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.draw()
            self.update()

    def draw(self):
        # Game Loop - draw
        self.screen.blit(bg, (0, 0))
        self.screen.blit(sun, (150, 100))
        self.screen.blit(floor, (0, 700))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def update(self):
        self.all_sprites.update()











    '''def __init__(self):
        self.all_sprites.add(character)
        for plat in Platforms:
            p = Platform(*plat)  # Falta entender
            all_sprites.add(p)
            platforms.add(p)'''
