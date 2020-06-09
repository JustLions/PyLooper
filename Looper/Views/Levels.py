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
        self.projectiles = pg.sprite.Group()

        self.character = Character(self); self.enemy = Enemy(self)
        self.all_sprites.add(self.character); self.all_sprites.add(self.enemy)
        self.characters.add(self.character); self.enemies.add(self.enemy)

        for i in Platforms:
            platform = CreatePlatform(*i)
            self.all_sprites.add(platform)
            self.platforms.add(platform)

    def draw(self):
        self.screen.blit(bg, (0, 0))
        self.screen.blit(sun, (150, 100))
        self.screen.blit(floor, (0, 700))
        if Character.dead:
            pg.event.pump()
            mouse = pg.mouse.get_pos()
            if 850 > mouse[0] > 700 and 575 > mouse[1] > 450:
                self.screen.blit(reset_button_onhover, (700, 450))
                if pg.mouse.get_pressed()[0] == 1:
                    Character.dead = False
                    self.character = Character(self)
                    self.all_sprites.add(self.character)
                    self.characters.add(self.character)
                    self.screen.blit(bg, (0, 0))
            else:
                self.screen.blit(reset_button, (700, 450))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def shoot(self):
        self.projectile = Projectile(self)
        self.projectile.pos = vec(self.character.pos.x, self.character.pos.y)
        self.projectiles.add(self.projectile)
        self.all_sprites.add(self.projectile)


    def update(self):
        self.all_sprites.update()


level1 = Level1()

