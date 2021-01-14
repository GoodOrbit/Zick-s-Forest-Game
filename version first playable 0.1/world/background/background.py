import pygame as pg
import loader
import operations as op
import constants as c

pg.init()

class Background(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = loader.loadImage('world/background/rs', 'bg_forest.png').convert()
        self.image = pg.transform.scale(self.image, c.SIZEBACKGROUND)
        self.rect = self.image.get_rect()
        self.rect[1] = -(c.SIZEBACKGROUND[1] - c.SIZE[1])

    def moveX(self, speedX):
        self.rect = self.rect.move(int(speedX), 0)
    
    def moveY(self, speedY):
        self.rect = self.rect.move(0, int(speedY))