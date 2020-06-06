from Character import *
from Settings import *
from Views.Platform import *


class Level1:

    screen = pg.display.set_mode((W, H))

    def __init__(self):
        self.screen = pg.display.set_mode((W, H))

        # We create the sprite groups for the specific level and add our character properties to it
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.character = Character(self)
        self.all_sprites.add(self.character)

        # We add every platform to each sprite group
        platform = Platform()
        self.all_sprites.add(platform)
        self.platforms.add(platform)

        self.run()

    # Active Game Loop from here on

    def run(self):
        playing = True
        while playing:
            self.draw()
            self.update()

    def draw(self):

        # We draw the static images and all sprites onto the screen
        self.screen.blit(bg, (0, 0))
        self.screen.blit(sun, (150, 100))
        self.screen.blit(floor, (0, 700))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def update(self):
        self.all_sprites.update()


level1 = Level1()
