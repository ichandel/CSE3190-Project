'''
title: Alien class
'''

from mySprite import MySprite
import pygame

class alien(MySprite):
    def __init__(self, IMAGE_FILE, X, Y):
        super().__init__()
        self.FILE_LOCA = IMAGE_FILE
        self.SCREEN = pygame.image.load(self.FILE_LOCA).convert_alpha()
        self.X = X
        self.Y = Y
        self.RIGHTBORDER = X + 200
        self.LEFTBORDER = X - 200
        self.SPD = 1
        self.POS = (self.X, self.Y)
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

    def enemyMovement(self):
        self.X += self.SPD
        if self.X == self.RIGHTBORDER:
            self.Y += 20
            self.SPD = self.SPD*-1
        elif self.X == self.LEFTBORDER:
            self.Y += 20
            self.SPD = self.SPD*-1
        self.updatePOS()
