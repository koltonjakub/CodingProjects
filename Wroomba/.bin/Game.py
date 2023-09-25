import string
import pygame
import os
import random


class Game:
    def __init__(self):
        self.setGame()
        self.runGame()
        self.game.quit()

    # while loop
    def runGame(self):
        self.setRect()
        while self.run:
            self.clock.tick(self.FPS)
            for event in self.game.event.get():
                if event.type == self.game.QUIT:
                    self.run = False
            self.keysPressed()
            self.drawWindow(self.rect)
            self.gravity()

    # set methods
    def setGame(self):
        self.run = True
        self.game = pygame

        # set clock
        self.setClock()

        # set jump
        self.jump = 'no'
        self.jumpCounter = 0

        # set window
        self.setWindow()

        # set background
        self.setBackgroundDimensions( backgroundWidth = self.getDisplayWidth() , backgroundHeight = self.getDisplayHeight())
        self.setBackground()

        # set window
        self.setRat()
        self.setRect()
        self.setBlock()

        # set velocity of a rat
        self.setVelocity()

        #set blocks
        self.setBlockDim( blockWidth=50, blockHeight=50)
        self.setBlock()
        self.setBlockMesh()

    def setDisplayDimensions(self, winWidth = 900, winHeight = 500):
        self.WIN_WIDTH = winWidth
        self.WIN_HEIGHT = winHeight
        self.WIN_DIMENSIONS = (self.WIN_WIDTH, self.WIN_HEIGHT)

    def setRat(self, ratWidth = 50, ratHeight = 50):
        self.setRatDim(ratWidth, ratHeight)

        self.ratImg = self.game.image.load(os.path.join('images','spaceship_yellow.png'))
        self.rat = self.game.transform.rotate(self.game.transform.scale(self.ratImg, self.getRatDim()), 90)

    def setBackground(self):
        self.background = self.game.transform.scale(self.game.image.load(
            os.path.join('images', 'marioSky.jpg')), (self.getBackgroundDimensions()))

    def setBackgroundDimensions(self, backgroundWidth : int = 1200, backgroundHeight : int = 300):
        self.backgroundDimensions = (backgroundWidth, backgroundHeight)

    def setClock(self, fps_import : int = 60):
        self.clock = self.game.time.Clock()
        self.FPS = fps_import

    def setVelocity(self, velocity : int = 5):
        self.velocity = velocity

    def setTitle(self, title : string):
        self.title = title

    def setRatDim(self, ratWidth : int = 50, ratHeight : int = 50):
        self.ratDimensions = (ratWidth, ratHeight)

    def setBlockDim(self, blockWidth : int = 25, blockHeight : int = 25):
        self.blockDimensions = (blockWidth, blockHeight)

    def setRect(self):
        self.rect = self.game.Rect(100, 250, self.getRatDimeWidth(), self.getRatDimHeight())

    def setBlock(self):
        self.setBlockDim()
        self.blockImg = self.game.image.load(os.path.join('images','block.png'))
        self.block = self.game.transform.scale(self.blockImg, self.getBlockDim())

    def setWindow(self):
        self.setTitle("Labirynt Ciemiężyciela")
        self.game.display.set_caption(self.getTitle())

        self.setDisplayDimensions(winWidth=1200, winHeight=700)
        self.display = self.game.display.set_mode(self.getDisplayDimensions())

    def setBlockMesh(self):
        self.blockMesh = []
        for i in range(0, int(self.getBackgroundDimWidth() / self.getBlockDimWidth())):
            for j in range(0, 3):
                self.blockMesh.append((i, j))

    def setBlock(self):
        self.blockImg = self.game.image.load(os.path.join('images','block.png'))
        self.block = self.game.transform.scale(self.blockImg, self.getRatDim())

    def placeBlock(self, x : int, y : int):
        self.display.blit(self.block, (x * self.getBlockDimWidth(), self.getDisplayHeight() - (y + 1) * self.getBLockDimHeight()))

    # other methods
    def drawWindow(self, rat):
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.rat, (rat.x, rat.y))
        for x, y in self.blockMesh:
            self.placeBlock(x = x, y = y)
        self.game.display.update()

    def isAboveGround(self):
        if self.getDisplayHeight() - (self.getWorldHeight() + 1) * self.getBLockDimHeight() \
                >= self.rect.y + self.getRatDimHeight():
            return True
        return False

    def setKeysPressed(self):
        self.keys_pressed = self.game.key.get_pressed()

    def keysPressed(self):
        self.setKeysPressed()
        # Yellow
        if self.keys_pressed[pygame.K_a] and self.rect.x - self.getVelocity() >= 0:  # Left
            self.rect.x -= self.getVelocity()

        if self.keys_pressed[pygame.K_d] and \
                self.rect.x + self.getVelocity() + self.getRatDimeWidth() <= self.getDisplayWidth():  # Right
            self.rect.x += self.getVelocity()

        if self.keys_pressed[pygame.K_s] and \
                self.rect.y + self.getRatDimHeight() + self.getVelocity() <= self.getDisplayHeight():  # Down
            if self.isAboveGround():
                self.rect.y += self.getVelocity()

        if self.keys_pressed[pygame.K_w] and self.jump == 'no':  # Up
            self.jump = 'fly'

    def gravity(self):
        if self.jump == 'fly':
            if self.jumpCounter != 30:
                self.jumpCounter += 1
                self.rect.y -= self.getVelocity()
            else:
                self.jumpCounter = 0
                self.jump = 'fall'
        elif self.isAboveGround() and self.jump == 'fall':
            self.rect.y += self.getVelocity()
        else:
            self.jump = 'no'

    # get methods
    def getTitle(self):
        return self.title

    def getDisplayDimensions(self):
        return self.WIN_DIMENSIONS

    def getDisplayWidth(self):
        return self.WIN_WIDTH

    def getDisplayHeight(self):
        return self.WIN_HEIGHT

    def getVelocity(self):
        return self.velocity

    def getBackgroundDimensions(self):
        return self.backgroundDimensions

    def getBackgroundDimWidth(self):
        return self.backgroundDimensions[0]

    def getBackgroundDimHeight(self):
        return self.backgroundDimensions[1]

    def getRatDim(self):
        return self.ratDimensions

    def getRatDimeWidth(self):
        return self.ratDimensions[0]

    def getRatDimHeight(self):
        return self.ratDimensions[1]

    def getBlockDim(self):
        return self.blockDimensions

    def getBlockDimWidth(self):
        return self.blockDimensions[0]

    def getBLockDimHeight(self):
        return self.blockDimensions[1]

    def getBlockAmount(self):
        return self.blockAmount

    def getBlockMesh(self):
        return self.blockMesh

    def getBlockMeshX(self, index):
        return self.blockMesh[index][0]

    def getBLockMeshY(self, index):
        return self.blockMesh[index][1]

    def getWorldHeight(self, x : int = 0):
        heightOfWorldUnderPlayerAsList = [ value for key, value in self.blockMesh if key == x ]
        return max(heightOfWorldUnderPlayerAsList)

if __name__ == "__main__":
    instance = Game()
    print(instance.jump)
    print(instance.isAboveGround())