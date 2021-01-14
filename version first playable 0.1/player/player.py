import pygame as pg
import operations as op
import constants as c
import loader
import random

pg.init()

class Player(pg.sprite.Sprite):
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.TOTALSPRITES = 10
        newWidth = op.scaleX(27.777777777777777777777777777778)
        addHeight = 0
        while True:
            if (newWidth % self.TOTALSPRITES) == 0:
                break
            else:
                newWidth += 1
                addHeight += 1
        addHeight = (addHeight * 100) / c.SIZE[1]
        newHeight = op.scaleY(8.2222222222222222222222222222222 + addHeight)
        newSize = newWidth, newHeight
        op.scaleImage('player/rs/player.png', 'player/rs/n_r_c/n_player.png', newSize)
        self.imageSprite = loader.loadImage('player/rs/n_r_c/', 'n_player.png')
        self.currentFrame = 0
        self.width = newWidth/10
        self.height = newHeight
        self.image = op.cutSprite(0, self.width, self.height, self.imageSprite)
        self.rect = self.image.get_rect()
        self.directionX = 0
        self.contMove = 0
        self.speedX = 0
        self.speedY = 0
        self.rect[1] = op.scaleY(44.444444444444444444444444444444)
        self.SPX = op.scaleXFloat(0.06944444444444444444444444444444)
        self.lastDirectionX = 0
        self.n = 0
        self.eyes = Eyes()
        self.pressed = 0
        self.G = op.scaleYFloat(0.25)
        self.lastSpeedY = 0
        self.JUMP = -(op.scaleYFloat(2.5))
        self.plat = None
        self.MIDDLEFT = op.scaleX(36.805555555555555555555555555556)
        self.MIDDLERIGHT = c.SIZE[0] - op.scaleX(36.805555555555555555555555555556)
        self.bg = None
        self.allBg = None
        self.SPXB = op.scaleXFloat(0.0439453125)
        self.contMoveB = 0
        self.speedXB = 0
        self.directionXB = 1
        self.h = 6
        self.limitB = 12
        self.lastDirectionXB = self.directionXB
        self.MIDDLEY = op.scaleY(75.555555555555555555555555555556)
        self.limitSpeedY = op.scaleYFloat(3.8888888888888888888888888888889)
        self.cont = 0

    def checkCollisionDown(self):
        if (((self.rect[1] - int(self.speedY)) + self.speedY) + self.rect[3]) > c.SIZE[1]:
            restP = (self.rect[1] + self.rect[3]) - c.SIZE[1] 
            self.rect[1] = self.rect[1] - restP
            self.speedY = 0
        
    def checkCollisionTop(self):
        if self.rect[1] < 0:
            sumP = -(self.rect[1])
            self.rect[1] += sumP
            self.speedY = 0

    def collisionPlatY(self):
        auxY = ((self.rect[1] - int(self.speedY)) + self.speedY)
        sumRectY = (auxY + self.rect[3])
        sumRectX = (self.rect[0] + self.rect[2])
        for i in self.plat: 
            if sumRectY >= i.rect[1] and sumRectY <= (i.rect[1] + i.rect[3]) and self.rect[0] >= i.rect[0] and \
                sumRectX <= (i.rect[0] + i.rect[2]) or sumRectY >= i.rect[1] and sumRectY <= (i.rect[1] + i.rect[3]) and \
                self.rect[0] < (i.rect[0] + i.rect[2]) and sumRectX >= (i.rect[0] + i.rect[2]) or \
                sumRectY >= i.rect[1] and sumRectY <= (i.rect[1] + i.rect[3]) and self.rect[0] <= i.rect[0] and sumRectX > i.rect[0]:
                restP = sumRectY - i.rect[1]
                if self.MIDDLEY >= self.rect[1] and self.MIDDLEY <= (self.rect[1] + self.rect[3]):
                    [i.moveY(restP) for i in self.bg]
                else:
                    self.rect[1] -= restP
                self.speedY = 0
                break
            elif auxY <= (i.rect[1] + i.rect[3]) and auxY >= i.rect[1] and self.rect[0] >= i.rect[0] and \
                sumRectX <= (i.rect[0] + i.rect[2]) or auxY <= (i.rect[1] + i.rect[3]) and auxY >= i.rect[1] and \
                self.rect[0] < (i.rect[0] + i.rect[2]) and sumRectX >= (i.rect[0] + i.rect[2]) or \
                auxY <= (i.rect[1] + i.rect[3]) and auxY >= i.rect[1] and self.rect[0] <= i.rect[0] and sumRectX > i.rect[0]: 
                sumP = (i.rect[1] + i.rect[3]) - auxY
                if self.MIDDLEY >= self.rect[1] and self.MIDDLEY <= (self.rect[1] + self.rect[3]):
                    [i.moveY(-sumP) for i in self.bg]
                else:
                    self.rect[1] += sumP
                self.speedY = 0 
                break
    
    def collisionPlatX(self):
        for i in self.plat:
            if self.rect.colliderect(i.rect):
                if self.directionX > 0: 
                    restP = (self.rect[0] + self.rect[2]) - i.rect[0]
                    if (self.bgf.rect[0] + c.SIZEBACKGROUND[0]) == c.SIZE[0] or self.bgf.rect[0] == 0:
                        self.rect[0] -= restP
                    else:
                        [i.moveX(restP) for i in self.bg]
                elif self.directionX < 0:
                    sumP = (i.rect[0] + i.rect[2]) - self.rect[0]
                    if self.bgf.rect[0] == 0 or (self.bgf.rect[0] + c.SIZEBACKGROUND[0]) == c.SIZE[0]:
                        self.rect[0] += sumP
                    else:
                        [i.moveX(-sumP) for i in self.bg]
                self.speedX = 0
                self.contMove = 0
                break
            
    def gravity(self):
        if self.speedY < self.limitSpeedY:
            self.speedY += self.G
        if self.MIDDLEY >= self.rect[1] and self.MIDDLEY <= (self.rect[1] + self.rect[3]) and self.speedY < 0 and self.bgf.rect[1] < 0 or \
            self.MIDDLEY >= self.rect[1] and self.MIDDLEY <= (self.rect[1] + self.rect[3]) and self.speedY > 0 and (self.bgf.rect[1] + self.bgf.rect[3]) != c.SIZE[1]:
            [i.moveY(-self.speedY) for i in self.bg]
            if (self.bgf.rect[1] + self.bgf.rect[3]) < c.SIZE[1]:
                sumP = c.SIZE[1] - (self.bgf.rect[1] + self.bgf.rect[3])
                [i.moveY(sumP) for i in self.bg]
            elif self.bgf.rect[1] > 0:
                restP = -self.bgf.rect[1] 
                [i.moveY(restP) for i in self.bg]
        else:
            self.rect = self.rect.move(0, int(self.speedY))
        self.checkCollisionTop()
        self.collisionPlatY()

    # Salto
    def jump(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP] and self.lastSpeedY >= 0:
            if self.speedY == 0:
                self.speedY = self.JUMP
        self.lastSpeedY = self.speedY

    def moveX(self, speedX):
        self.rect = self.rect.move(speedX, 0)

    def move(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_n]:
            if self.h == 20:
                self.h = 6
            elif self.h == 6:
                self.h = 20
        if (keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]) != 0:
            self.pressed = 1
            self.directionXB = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]
        else:
            self.pressed = 0
        if self.contMove == 0 or self.directionX != (keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]) \
            and (keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]) != 0: 
            self.directionX = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]
        if self.pressed == 1:
            if self.contMove < self.h:
                self.speedX += self.SPX
                self.contMove += 1
            self.currentFrame += 1
            if self.currentFrame >= self.TOTALSPRITES:
                self.currentFrame = 0
            self.image = op.cutSprite(self.currentFrame, self.width, self.height, self.imageSprite)
            if self.directionX < 0:
                self.image = pg.transform.flip(self.image, 1, 0)
        else: # Si la tecla no fue pulsada
            if self.lastDirectionX != 0:
                self.image = op.cutSprite(0, self.width, self.height, self.imageSprite)
                if self.lastDirectionX < 0: 
                    self.image = pg.transform.flip(self.image, 1, 0)
            if self.contMove != 0: 
                self.speedX -= self.SPX
                self.contMove -= 1
            else:
                self.speedX = 0
        self.lastDirectionX = self.directionX

        if self.rect[0] >= self.MIDDLEFT and self.directionX > 0 and (self.bgf.rect[0] + c.SIZEBACKGROUND[0]) > c.SIZE[0]:
            [i.moveX(-self.speedX) for i in self.bg] 
            if (self.bgf.rect[0] + c.SIZEBACKGROUND[0]) < c.SIZE[0]: 
                sumP = c.SIZE[0] - (self.bgf.rect[0] + c.SIZEBACKGROUND[0])
                [i.moveX(sumP) for i in self.bg]
        elif self.rect[0] <= self.MIDDLERIGHT and self.directionX < 0 and self.bgf.rect[0] < 0: 
            [i.moveX(self.speedX) for i in self.bg]
            if self.bgf.rect[0] > 0:
                restP = -self.bgf.rect[0]
                [i.moveX(restP) for i in self.bg]
        else:
            self.rect = self.rect.move(int(self.speedX * self.directionX), 0) 
        self.collisionPlatX()
        self.borderscreen()

        if self.rect[0] > self.MIDDLEFT and self.bgf.rect[0] < 0 and (self.bgf.rect[0] + c.SIZEBACKGROUND[0]) > c.SIZE[0] and self.directionXB > 0 or \
            self.rect[0] < self.MIDDLERIGHT and self.bgf.rect[0] < 0 and (self.bgf.rect[0] + c.SIZEBACKGROUND[0]) > c.SIZE[0] and self.directionXB < 0:
            if self.lastDirectionXB != self.directionXB:              
                self.restartB()
            self.lastDirectionXB = self.directionXB
            if self.pressed != 0:
                if self.contMoveB > 12:
                    self.contMoveB = 12 
                    self.limitB = self.contMoveB
                    self.speedXB = self.SPXB * self.contMoveB 
            else:
                if self.contMoveB <= 12: 
                    self.limitB = 23 
            if self.contMoveB < self.limitB:
                self.speedXB += self.SPXB
                self.contMoveB += 1
            [i.moveX(self.speedXB * -self.directionXB) for i in self.allBg]
            if self.rect[0] < self.MIDDLEFT and self.directionXB > 0:
                sumP = self.MIDDLEFT - self.rect[0]
                [i.moveX(sumP) for i in self.allBg]
                self.restartB()
            elif self.rect[0] > self.MIDDLERIGHT and self.directionXB < 0:
                restP = -(self.rect[0] - self.MIDDLERIGHT)
                [i.moveX(restP) for i in self.allBg]
                self.restartB()
            if (self.bgf.rect[0] + c.SIZEBACKGROUND[0]) < c.SIZE[0]: 
                sumP = c.SIZE[0] - (self.bgf.rect[0] + c.SIZEBACKGROUND[0])
                [i.moveX(sumP) for i in self.allBg] 
                self.restartB()
            elif self.bgf.rect[0] > 0:
                restP = -self.bgf.rect[0]
                [i.moveX(restP) for i in self.allBg]
                self.restartB()
            
    def restartB(self):
        self.contMoveB = 0
        self.speedXB = 0
        self.limitB = 12

    def borderscreen(self):
        self.rect = self.rect.clamp(c.SCREENRECT)

    def update(self, plat, bg, bgf, allBg):
        self.plat = plat
        self.bg = bg
        self.bgf = bgf
        self.allBg = allBg
        self.move()
        self.gravity()
        self.jump()
        self.eyes.update((self.rect[0], self.rect[1]), self.directionX)

class Eyes(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.TOTALSPRITES = 7
        newWidth = op.scaleX(17.013888888888888888888888888889) 
        addHeight = 0
        while True:
            if (newWidth % self.TOTALSPRITES) == 0:
                break
            else:
                newWidth += 1
                addHeight += 1
        addHeight = (addHeight * 100) / c.SIZE[1] 
        newHeight = op.scaleY(2.2 + addHeight) 
        newSize = newWidth, newHeight
        op.scaleImage('player/rs/eyes.png', 'player/rs/n_r_c/n_eyes.png', newSize) 
        self.imageSprite = loader.loadImage('player/rs/n_r_c/', 'n_eyes.png')
        self.currentFrame = 0
        self.width = newWidth/self.TOTALSPRITES
        self.height = newHeight
        self.image = op.cutSprite(0, self.width, self.height, self.imageSprite)
        self.rect = self.image.get_rect()
        self.contBlin = 0
        self.random = 0
        self.waitBlin = 70
        self.directionX = 1
        self.lastDirectionX = 1
        self.addXrest = op.scaleX(0.06944444444444444444444444444444) 
        self.addXsum = op.scaleX(0.48611111111111111111111111111111) 
        self.addY = op.scaleY(1)

    def blinking(self, directionX):
        if directionX != 0:
            self.directionX = directionX
        if self.contBlin != self.waitBlin: 
            self.contBlin += 1
            self.image = op.cutSprite(0, self.width, self.height, self.imageSprite)
        else:
            self.currentFrame += 1
            if self.currentFrame == self.TOTALSPRITES:
                self.currentFrame = 0
                self.contBlin = 0
                self.random = random.randrange(5) 
                if self.random == 0: 
                    self.waitBlin = 70
                elif self.random == 1:
                    self.waitBlin = 150
                elif self.random == 2:
                    self.waitBlin = 200
                elif self.random == 3:
                    self.waitBlin = 300
                else:
                    self.waitBlin = 400
            self.image = op.cutSprite(self.currentFrame, self.width, self.height, self.imageSprite)
        
        if self.directionX < 0:
            self.image = pg.transform.flip(self.image, 1, 0)
        self.lastDirectionX = self.directionX 

    def move(self, position):
        if self.directionX > 0:
            self.rect[0], self.rect[1] = position[0] - self.addXrest, (position[1] + self.addY)
        else:
            self.rect[0], self.rect[1] = position[0] + self.addXsum, (position[1] + self.addY)

    def update(self, position, directionX):
        self.blinking(directionX)
        self.move(position)