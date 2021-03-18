'''
title: Image Sprites
'''

import pygame
from mySprite import MySprite

class ImageSprite(MySprite):

    def __init__(self, IMAGE_FILE):
        super().__init__()
        self.FILE_LOCA = IMAGE_FILE
        self.SCREEN = pygame.image.load(self.FILE_LOCA).convert_alpha()
        self.X_FLIP = False

    # --- MODIFIER METHODS --- #

    def setScale(self, SCALE_X, SCALE_Y=0):
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self.SCREEN = pygame.transform.scale(self.SCREEN, (int(self.getWidth()//SCALE_X), int(self.getHeight()//SCALE_Y)))

    def flipImageX(self, KEY_PRESSES):
        if KEY_PRESSES[pygame.K_d] == 1 and self.X_FLIP:
            self.SCREEN = pygame.transform.flip(self.SCREEN, True, False)
            self.X_FLIP = False
        if KEY_PRESSES[pygame.K_a] == 1 and not self.X_FLIP:
            self.SCREEN = pygame.transform.flip(self.SCREEN, True, False)
            self.X_FLIP = True

    def wasdMove(self, KEYPRESSES):
        super().wasdMove(KEYPRESSES)
        self.flipImageX(KEYPRESSES)

    def adMove(self, KEYPRESSES, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        super().adMove(KEYPRESSES)
        self.checkBoundaries(MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT)
        self.flipImageX(KEYPRESSES)

    def enemieMovement(self,MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH = 0, MIN_HEIGHT =0):
        self.X += self.MOVEMENTX
        if self.X == MAX_WIDTH:
            self.Y += self.MOVEMENTY
            self.MOVEMENTX = self.MOVEMENTX*-1
        elif self.X == MIN_WIDTH:
            self.Y += self.MOVEMENTY
            self.MOVEMENTX = self.MOVEMENTX*-1
        self.updatePOS()

    def checkBoundaries(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT):
        if self.X > MAX_WIDTH - self.getWidth():
            self.X = MAX_WIDTH - self.getWidth()
        elif self.X < MIN_WIDTH:
            self.X = MIN_WIDTH
        if self.Y > MAX_HEIGHT - self.getHeight():
            self.Y = MAX_HEIGHT - self.getHeight()
        elif self.Y < MIN_HEIGHT:
            self.Y = MIN_HEIGHT
        self.updatePOS()

