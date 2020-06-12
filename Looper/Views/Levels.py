from Character import *
from Settings import *
from Views.Platform import *


class Level1:

    def __init__(self):
        self.screen = pg.display.set_mode((W, H))

        # We create the sprite groups for the specific level and add our character and enemy class to it
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.characters = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()

        self.character = Character(); self.enemy = Enemy();
        self.all_sprites.add(self.character); self.all_sprites.add(self.enemy)
        self.characters.add(self.character); self.enemies.add(self.enemy);

        for i in Platforms:
            platform = CreatePlatform(*i)
            self.all_sprites.add(platform)
            self.platforms.add(platform)

    def draw(self):
        self.screen.blit(bg, (self.character.bgX * 0.6, 0))
        self.screen.blit(bg, (self.character.bgX2 * 0.6, 0))
        self.screen.blit(tree3, (1300 + self.character.bgX, 175))
        self.screen.blit(floor, (self.character.bgX, 450))
        self.screen.blit(floor, (self.character.bgX2, 450))
        self.screen.blit(tree2, (740 + self.character.bgX, 250))
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

        self.screen.blit(item_bar, (600, 820))
        if self.character.potion:
            self.screen.blit(health_potion_50, (625, 833))

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
                    self.character = Character()
                    self.all_sprites.add(self.character)
                    self.characters.add(self.character)
                    self.screen.blit(bg, (0, 0))
            else:
                self.screen.blit(reset_button, (700, 450))
        self.character.projectiles.draw(self.screen)
        self.projectiles.draw(self.screen)
        self.items.draw(self.screen)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    def interactions(self):
        char_hit_platform = pg.sprite.spritecollide(self.character, self.platforms, 0)
        char_hit_enemy = pg.sprite.spritecollide(self.character, self.enemies, 0)
        enemy_hit_platform = pg.sprite.spritecollide(self.enemy, self.platforms, 0)
        proj_hit_enemy = pg.sprite.groupcollide(self.enemies, self.character.projectiles, True, True)

        # Actions when hit occurs
        if char_hit_platform:
            self.character.pos.y = 690
        if char_hit_enemy:
            if self.character.hp > 0:
                self.character.hp = self.character.hp - hp_loss
            else:
                pg.sprite.spritecollide(self.enemy, self.characters, 1)
                Character.dead = True
        if enemy_hit_platform:
            self.enemy.pos.y = 675
            self.enemy.pos.x = 1000 + self.character.bgX
        if proj_hit_enemy:
            self.character.drop()

    def update(self):
        self.character.projectiles.update(self.character.pos.x)
        self.projectiles.update()
        self.items.update()
        self.all_sprites.update()


level1 = Level1()
