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
        self.all_sprites.add(self.character); # self.all_sprites.add(self.enemy)
        self.characters.add(self.character); self.enemies.add(self.enemy)

        for i in Platforms:
            platform = CreatePlatform(*i)
            self.all_sprites.add(platform)
            self.platforms.add(platform)

    def draw(self):
        self.screen.blit(bg, (self.character.bgX * 0.6, 0))
        self.screen.blit(bg, (self.character.bgX2 * 0.6, 0))
        self.screen.blit(floor, (self.character.bgX, 450))
        self.screen.blit(floor, (self.character.bgX2, 450))
        self.screen.blit(tree2, (700 + self.character.bgX, 250))
        self.screen.blit(tree3, (1300 + self.character.bgX, 250))
        self.screen.blit(tree1, (2400 + self.character.bgX, 400))
        self.screen.blit(sun, (150 + self.character.bgX, 100))


        if 75 < self.character.hp <= 100:
            self.screen.blit(health_bar_100, (20, 20))
        if 50 < self.character.hp <= 75:
            self.screen.blit(health_bar_75, (20, 20))
        if 25 < self.character.hp <= 50:
            self.screen.blit(health_bar_50, (20, 20))
        if 0 < self.character.hp <= 25:
            self.screen.blit(health_bar_25, (20, 20))
        if 0 == self.character.hp:
            self.screen.blit(health_bar_0, (20, 20))

        self.screen.blit(item_bar, (625, 800))
        font = pg.font.SysFont("Calibri", 25)
        char_points_ui = font.render("Points:", 1, black)
        char_points = font.render(str(self.character.points), 1, black)
        self.screen.blit(char_points_ui, (25, 80))
        self.screen.blit(char_points, (105, 80))

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
        self.projectile.pos = vec(self.character.pos.x + 60, self.character.pos.y + 27)
        self.image = bullet1
        self.rect = self.image.get_rect(x=self.character.pos.x, y=self.character.rect.y)
        self.projectiles.add(self.projectile)
        self.all_sprites.add(self.projectile)

    def update(self):
        self.all_sprites.update()


level1 = Level1()

