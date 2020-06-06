from Game import *
from Views.Level1 import *
from Character import *
running = True

class Main:

    def __init__(self):
        pg.init()
        pg.display.set_caption(Title)
        pg.time.Clock().tick(FPS)
        Game()
        pg.display.flip()


while running:
    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = False
    Main()
    pg.display.update()
