from Game import *
from Character import *
running = True


class Main:

    def __init__(self):
        pg.init()
        pg.display.set_caption(Title)
        pg.time.Clock().tick(FPS)
        Game()
        pg.display.flip()


# Setup functions, run only once.
Main()
game = Game()

while running:
    game.run()
    event = pg.event.poll()
    if event.type == pg.QUIT:
        running = False
    pg.display.update()
