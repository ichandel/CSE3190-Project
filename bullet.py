'''
title: Bullet
'''
from mySprite import MySprite
import pygame

class bullets(MySprite):
    def __init__(self, IMAGE_FILE):
        super().__init__()
        self.FILE_LOCA = IMAGE_FILE
        self.SCREEN = pygame.image.load(self.FILE_LOCA).convert_alpha()

    def setScale(self, SCALE_X, SCALE_Y=0):
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self.SCREEN = pygame.transform.scale(self.SCREEN, (int(self.getWidth()//SCALE_X), int(self.getHeight()//SCALE_Y)))

    def shooting(self,KEYPRESSES, X, Y):
        if KEYPRESSES[pygame.K_SPACE] == 1:
            self.X = X
            self.Y = Y
            self.updatePOS()

    def bulletMovement(self):
        self.Y -= self.MOVEMENTY



