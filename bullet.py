'''
title: Bullet
'''

from mySprite import MySprite
import pygame

class bullets(MySprite):
    def __init__(self, IMAGE_FILE, X, Y, DIR):
        """
        initializes bullets
        :param IMAGE_FILE: fileName
        :param X: int
        :param Y: int
        :param DIR: int
        """
        super().__init__()
        self.FILE_LOCA = IMAGE_FILE
        self.SCREEN = pygame.image.load(self.FILE_LOCA).convert_alpha()
        self.X = X
        self.Y = Y
        self.DIR = DIR  # vertical direction of bullet
        self.SPD = 10

    def setScale(self, SCALE_X, SCALE_Y=0):
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self.SCREEN = pygame.transform.scale(self.SCREEN, (int(self.getWidth()//SCALE_X), int(self.getHeight()//SCALE_Y)))

    def bulletMovement(self):
        """
        bullet movement
        :return:
        """
        self.Y += self.SPD * self.DIR



