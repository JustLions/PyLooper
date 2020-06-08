from Character import *
from Settings import *
from Views.Platform import *


class Level1:

    screen = pg.display.set_mode((W, H))

    def __init__(self):
        self.screen = pg.display.set_mode((W, H))

        # We create the sprite groups for the specific level and add our character and enemy class to it
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.characters = pg.sprite.Group()
        self.enemies = pg.sprite.Group()

        self.character = Character(self)
        self.enemy = Enemy(self)

        self.all_sprites.add(self.character)
        self.all_sprites.add(self.enemy)

        self.characters.add(self.character)
        self.enemies.add(self.enemy)

        for i in Platforms:
            platform = CreatePlatform(*i)
            self.all_sprites.add(platform)
            self.platforms.add(platform)

    def draw(self):

        # We draw the static images and all sprites onto the screen
        self.screen.blit(bg, (0, 0))
        self.screen.blit(sun, (150, 100))
        self.screen.blit(floor, (0, 700))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def respawn(self):
        pg.sprite.Sprite.__init__(self)
        pg.draw.rect(self.screen, (255, 0, 255), (800, 450, 100, 100))

    def update(self):
        self.all_sprites.update()


level1 = Level1()
