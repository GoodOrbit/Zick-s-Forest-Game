import pygame as pg
import constants as c
import operations as op
import loader

pg.init()

class Plataform(pg.sprite.Sprite):
    def __init__(self, position, width, img, height):
        pg.sprite.Sprite.__init__(self)
        self.width = width
        self.height = op.scaleY(4.4444444444444444444444444444444) - height
        self.image = img
        self.rect = pg.Rect(position[0], position[1], self.width, self.height)

    def moveX(self, speedX):
        self.rect = self.rect.move(int(speedX), 0)
    
    def moveY(self, speedY):
        self.rect = self.rect.move(0, int(speedY))

class Line(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        imgload = loader.loadImage('world/plataforms/rs/', '1.png')
        self.image = pg.transform.scale(imgload, (1440, 1))
        self.rect = self.image.get_rect()
        self.rect[1] = op.scaleY(75.555555555555555555555555555556)

class PlataformTwo(pg.sprite.Sprite):
    def __init__(self, position, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect[0] = position[0]
        self.rect[1] = position[1]

    def moveX(self, speedX):
        self.rect = self.rect.move(int(speedX), 0)
    
    def moveY(self, speedY):
        self.rect = self.rect.move(0, int(speedY))

class SpritePlataform():
    plataforms = pg.sprite.Group()
    plataformsT = pg.sprite.Group()
    HEIGHT = op.scaleY(4.4444444444444444444444444444444)
    imgload = loader.loadImage('world/plataforms/rs/', '1.png')
    WIDTH = op.scaleX(8.3333333333333333333333333333333)
    newSize = (WIDTH, HEIGHT)
    op.scaleImage('world/plataforms/rs/2.1.png', 'world/plataforms/rs/n/2.1.png', newSize)
    imgloadt = loader.loadImage('world/plataforms/rs/n/', '2.1.png')
    x = 0

    newWidth = int(op.scaleXFloat(11.111111111111111111111111111111) - op.scaleXFloat(0.625)) 
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(8.1111111111111111111111111111111)), newWidth, imgload, 0))
    x += newWidth

    newWidth = int(op.scaleXFloat(16.666666666666666666666666666667) + op.scaleXFloat(1.83333333333333333333333333333)) 
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(3.6666666666666666666666666666667)), newWidth, imgload, 0))
    x += newWidth

    newWidth = int(op.scaleXFloat(2.7777777777777777777777777777778) + op.scaleXFloat(0.06944444444444444444444444444444))
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(8.1111111111111111111111111111111)), newWidth, imgload, 0))
    x += newWidth

    newWidth = int(op.scaleXFloat(2.7777777777777777777777777777778) + op.scaleXFloat(0.06944444444444444444444444444444))
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(12.555555555555555555555555555556)), newWidth, imgload, 0))
    x += newWidth

    newWidth = int(op.scaleXFloat(55.555555555555555555555555555556) - op.scaleXFloat(1.83333333333333333333333333333))
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(17)), newWidth, imgload, 0))
    x += newWidth

    newWidth = int(op.scaleXFloat(11.111111111111111111111111111111) + op.scaleXFloat(0.06944444444444444444444444444444))
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(12.555555555555555555555555555556)), newWidth, imgload, 0))
    x += newWidth

    newWidth = op.scaleX(2.7777777777777777777777777777778) 
    x -= newWidth
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(8.1111111111111111111111111111111)), newWidth, imgload, 0))
    x += newWidth

    newWidth = int(op.scaleXFloat(66.666666666666666666666666666667) + op.scaleXFloat(1.5277777777777777777777777777778))
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(3.6666666666666666666666666666667)), newWidth, imgload, 0))
    x += newWidth

    newWidth = int(op.scaleXFloat(36.111111111111111111111111111111) + op.scaleXFloat(0.06944444444444444444444444444444)) 
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(8.1111111111111111111111111111111)), newWidth, imgload, 0))
    x += newWidth

    newWidth = op.scaleX(19.444444444444444444444444444444)
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(12.555555555555555555555555555556)), newWidth, imgload, 0))
    x += newWidth

    newWidth = op.scaleX(16.666666666666666666666666666667)
    imgload = pg.transform.scale(imgload, (newWidth, HEIGHT))
    plataforms.add(Plataform((x, c.SIZE[1] - op.scaleY(17)), newWidth, imgload, 0))

    n = op.scaleX(4.1666666666666666666666666666667)
    m = op.scaleY(5)
    a = op.scaleX(1.8055555555555555555555555555556)
    b = op.scaleY(2.2222222222222222222222222222222)

    x = c.SIZEBACKGROUND[0] - (WIDTH - HEIGHT) 
    y = c.SIZE[1] - op.scaleY(27.777777777777777777777777777778)
    plataformsT.add(PlataformTwo((x, y), imgloadt))
    imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
    plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, 0))

    x = x - (WIDTH + n)
    y = y - (HEIGHT + m)
    plataformsT.add(PlataformTwo((x, y), imgloadt))
    imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
    plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, b))

    for i in range(3):
        x = x - (WIDTH + n)
        y = y - (HEIGHT + m)
        plataformsT.add(PlataformTwo((x, y), imgloadt))
        imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
        plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, 0))

    while x > (c.SIZEBACKGROUND[0] / 2):
        x = x - WIDTH
        plataformsT.add(PlataformTwo((x, y), imgloadt))
        imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
        plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, 0))

    y = y - (HEIGHT + m)

    while x > 0:
        x = x - WIDTH
        plataformsT.add(PlataformTwo((x, y), imgloadt))
        imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
        plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, 0))

    x = -HEIGHT
    y = y - HEIGHT*2
    plataformsT.add(PlataformTwo((x, y), imgloadt))
    imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
    plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, 0))

    x = x + (WIDTH + n)
    y = y - (HEIGHT + m)
    plataformsT.add(PlataformTwo((x, y), imgloadt))
    imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
    plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, b))

    for i in range(7):
        x = x + (WIDTH + n)
        y = y - (HEIGHT + m)
        plataformsT.add(PlataformTwo((x, y), imgloadt))
        imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
        plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, 0))

    while x < c.SIZEBACKGROUND[0]:
        x = x + WIDTH
        plataformsT.add(PlataformTwo((x, y), imgloadt))
        imgload = pg.transform.scale(imgload, (WIDTH - a, HEIGHT - b))
        plataforms.add(Plataform((x + int(a/2), y + int(b/2)), WIDTH - a, imgload, 0))
