import pygame as pg
import constants as c
import sys
from processor import Processor 

pg.init()

class Main:
    window = pg.display.set_mode(c.SIZE, pg.FULLSCREEN)
    clock = pg.time.Clock()
    ps = Processor()

    def quit():
        pg.quit()
        sys.exit()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    quit()
            elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        quit()
        ps.drawing(window)
        pg.display.flip()
        clock.tick(c.FPS)      