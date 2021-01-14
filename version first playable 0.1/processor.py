import pygame as pg
from world.background.background import Background
from player.player import Player
from world.plataforms.plataforms import SpritePlataform

pg.init()

class Processor:
    def __init__(self):
        self.bg = pg.sprite.Group()

        self.allBg = pg.sprite.Group()

        self.playerGroup = pg.sprite.Group()

        self.plat = SpritePlataform()
        self.bg.add(self.plat.plataforms)

        self.bgf = Background()
        self.bg.add(self.bgf)

        self.bg.add(self.plat.plataformsT)

        self.player = Player()
        self.playerGroup.add(self.player, self.player.eyes)

        self.allBg.add(self.bg, self.player)
        
    def drawing(self, window):
        self.player.update(self.plat.plataforms, self.bg, self.bgf, self.allBg)
        self.bg.clear(window, self.bgf.image)
        self.bg.draw(window)
        self.playerGroup.draw(window)