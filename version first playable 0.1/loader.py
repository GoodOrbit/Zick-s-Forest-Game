import pygame as pg
import os

pg.init()

def loadImage(path, nameFile):
    try:
        path = os.path.join(path, nameFile)
        image = pg.image.load(path)
        return image
    except:
        print('Image could not be loaded')