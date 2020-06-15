from Character import *
from Enemy import *
from Items import *
from Settings import *
from Views.Platform import *


class Level1:

    def __init__(self):
        self.screen = pg.display.set_mode((W, H))
        self.camera = Camera(map_x_size, map_y_size)  # Luego sustituir cons self.map.width, self.map.height

        # We create the sprite groups for the specific level and add our character and enemy class to it
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group(); self.characters = pg.sprite.Group(); self.enemies = pg.sprite.Group()

        self.character = Character(); self.enemy_wolf = Wolf();
        self.all_sprites.add(self.character, self.enemy_wolf)
        self.characters.add(self.character); self.enemies.add(self.enemy_wolf);

        for i in Floor:
            map_floor = CreateFloor(*i)
            self.platforms.add(map_floor)
            self.all_sprites.add(map_floor)

        for i in Platforms:
            platform = CreatePlatform(*i)
            self.platforms.add(platform)

    def draw(self):
        self.screen.blit(bg, (0, 0))

        # Environment
        self.screen.blit(tree3, (1300 - self.character.pos.x * 0.8, 175))
        self.screen.blit(floor, (0 - self.character.pos.x * 0.8, 450))
        self.screen.blit(floor, (1600 - self.character.pos.x * 0.8, 450))
        self.screen.blit(tree2, (740 - self.character.pos.x * 0.8, 250))
        self.screen.blit(tree1, (2400 - self.character.pos.x * 0.8, 400))
        self.screen.blit(sun, (150 - self.character.pos.x * 0.8, 100))

        # Health Bars
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
        if 75 < self.enemy_wolf.hp <= 100:
            self.screen.blit(enemy_health_bar_100, (Wolf().pos.x - self.character.pos.x + 260, 620))
        if 50 < self.enemy_wolf.hp <= 75:
            self.screen.blit(enemy_health_bar_75, (Wolf().pos.x - self.character.pos.x + 260, 620))
        if 25 < self.enemy_wolf.hp <= 50:
            self.screen.blit(enemy_health_bar_50, (Wolf().pos.x - self.character.pos.x + 260, 620))
        if 0 < self.enemy_wolf.hp <= 25:
            self.screen.blit(enemy_health_bar_25, (Wolf().pos.x - self.character.pos.x + 260, 620))

        # Item Bar
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

        # Updated Drawings
        for sprite in self.platforms:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.character.projectiles:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def interactions(self):
        char_hit_platform = pg.sprite.spritecollide(self.character, self.platforms, 0)
        char_hit_enemy = pg.sprite.spritecollide(self.character, self.enemies, 0)
        enemies_hit_platform = pg.sprite.groupcollide(self.enemies, self.platforms, False, False)
        proj_hit_enemies = pg.sprite.groupcollide(self.enemies, self.character.projectiles, False, False)

        # Enemy Aggro
        if abs(self.enemy_wolf.pos.x - self.character.pos.x) < 500:
            pass

        print(self.platforms.rect.colliderect)
        # Actions when hit occurs
        if char_hit_platform:
            self.character.pos.y = char_hit_platform[0].rect.top - 55
            if Character.jumping:
                # jump_sound()
                self.character.pos.y += -jump_height
                self.character.vel.y = -jump_height / 2.5
                self.character.acc = vec(0, 5)
                Character.jumping = False

        if char_hit_enemy:
            if self.character.hp > 0:
                self.character.hp = self.character.hp - hp_loss
            else:
                pg.sprite.spritecollide(self.enemy_wolf, self.characters, 1)
                Character.dead = True
        if enemies_hit_platform:
            self.enemy_wolf.pos.y = 675
            self.enemy_wolf.pos.x = 1000
        if proj_hit_enemies:
            pg.sprite.groupcollide(self.enemies, self.character.projectiles, False, True)
            if 0 < self.enemy_wolf.hp <= 100:
                self.enemy_wolf.hp -= 25
            if self.enemy_wolf.hp == 0:
                self.enemy_wolf.kill()
                self.character.drop()

    def update(self):
        self.character.projectiles.update(self.character.pos.x)
        self.platforms.update()
        self.all_sprites.update()
        self.camera.update(self.character)


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        cam_x = -target.pos.x + 400
        cam_y = -target.pos.y + 100
        # Limit scrolling to map size
        cam_x = min(0, cam_x)
        cam_y = min(0, cam_y)
        cam_x = max(-(self.width - W), cam_x)  # right
        cam_y = max(-(self.height - H), cam_y)  # bottom
        self.camera = pg.Rect(cam_x, cam_y, self.width, self.height)
