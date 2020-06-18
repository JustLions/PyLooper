from Views.Levels import *
from Settings import *
vec = pg.math.Vector2


class Item(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = health_potion_50
        self.rect = self.image.get_rect(x=920, y=700)
        self.pos = vec(900, 700)
