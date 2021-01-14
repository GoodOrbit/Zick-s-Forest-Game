import pygame as pg
import constants as c
from PIL import Image

pg.init()

def scaleX(num):
    newScale = int((num * c.SIZE[0]) / 100)
    return newScale

def scaleY(num):
    newScale = int((num * c.SIZE[1]) / 100)
    return newScale

def scaleXFloat(num):
    newScale = (num * c.SIZE[0]) / 100
    return newScale

def scaleYFloat(num):
    newScale = (num * c.SIZE[1]) / 100
    return newScale

def scaleImage(url, urlsave, newSize):
    try:
        with Image.open(url) as im:
            im = im.resize((newSize[0], newSize[1]))
            im.save(urlsave, "PNG")
    except OSError:
        print("cannot create thumbnail for image")
        
def cutSprite(currentFrame, widthSprite, heightSprite, imageSprite):
    newArea = pg.Rect(currentFrame * widthSprite, 0, widthSprite, heightSprite)
    return imageSprite.subsurface(newArea)