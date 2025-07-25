'''
title: Ships class
'''

import pygame
from mySprite import MySprite

class Ships(MySprite):

    def __init__(self, IMAGE_FILE):
        """
        initializes ships
        :param IMAGE_FILE: fileName
        """
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
        """
        flips image when turning left or right
        :param KEY_PRESSES: object
        :return:
        """
        if KEY_PRESSES[pygame.K_d] == 1 and self.X_FLIP:
            self.SCREEN = pygame.transform.flip(self.SCREEN, True, False)
            self.X_FLIP = False
        if KEY_PRESSES[pygame.K_a] == 1 and not self.X_FLIP:
            self.SCREEN = pygame.transform.flip(self.SCREEN, True, False)
            self.X_FLIP = True

    def adMove(self, KEYPRESSES, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        """
        horizontal movement
        :param KEYPRESSES: object
        :param MAX_WIDTH: int
        :param MAX_HEIGHT: int
        :param MIN_WIDTH: int
        :param MIN_HEIGHT: int
        :return: none
        """
        super().adMove(KEYPRESSES)
        self.checkBoundaries(MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT)
        self.flipImageX(KEYPRESSES)

    def checkBoundaries(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT):
        """
        checks movement boundaries
        :param MAX_WIDTH: int
        :param MAX_HEIGHT: int
        :param MIN_WIDTH: int
        :param MIN_HEIGHT: int
        :return: none
        """
        if self.X > MAX_WIDTH - self.getWidth():
            self.X = MAX_WIDTH - self.getWidth()
        elif self.X < MIN_WIDTH:
            self.X = MIN_WIDTH
        if self.Y > MAX_HEIGHT - self.getHeight():
            self.Y = MAX_HEIGHT - self.getHeight()
        elif self.Y < MIN_HEIGHT:
            self.Y = MIN_HEIGHT
        self.updatePOS()