"""
title: Boxes
author: Ishaan Chandel
date-created: 2021-03-02
"""

import pygame
from window import Window
from loader import Colour

class Box:
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, COLOR=Colour.WHITE):
        """
        initializes box
        :param WIDTH: int
        :param HEIGHT: int
        :param X: int
        :param Y: int
        :param COLOR: object
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.X = X
        self.Y = Y
        self.POS = (self.X, self.Y)
        self.SCREEN = pygame.Surface(self.DIMENSION, pygame.SRCALPHA, 32)
        self.COLOR = COLOR
        self.SCREEN.fill(self.COLOR)
        self.SPD = 5

    # --- MODIFIER METHODS (SETTER) --- #
    def moveBox(self, KEYPRESSES):
        """
        moves box
        :param KEYPRESSES: object
        :return: none
        """
        # CHECK KEYPRESSES
        if KEYPRESSES[pygame.K_d] == 1:
            self.X = self.X + 1
        if KEYPRESSES[pygame.K_a] == 1:
            self.X -= 1
        self.Y += 3

        self.POS = (self.X, self.Y)


    def wrapBox(self, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        """
        wraps box around screen when it moves out of sight
        :param MAX_WIDTH: int
        :param MAX_HEIGHT: int
        :param MIN_WIDTH: int
        :param MIN_HEIGHT: int
        :return: none
        """
        if self.X > MAX_WIDTH:
            self.X = -self.SCREEN.get_rect().width
        elif self.X < MIN_WIDTH - self.SCREEN.get_rect().width:
            self.X = MAX_WIDTH
        if self.Y > MAX_HEIGHT:
            self.Y = -self.SCREEN.get_rect().height
        elif self.Y < MIN_HEIGHT - self.SCREEN.get_rect().height:
            self.Y = MAX_HEIGHT

    def moveBoxWrap(self, KEYPRESSES, MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH=0, MIN_HEIGHT=0):
        """
        combines moveBox and wrapBox
        :param KEYPRESSES: object
        :param MAX_WIDTH: int
        :param MAX_HEIGHT: int
        :param MIN_WIDTH: int
        :param MIN_HEIGHT: int
        :return: none
        """
        self.moveBox(KEYPRESSES)
        self.wrapBox(MAX_WIDTH, MAX_HEIGHT, MIN_WIDTH, MIN_HEIGHT)

    def updateDimension(self):
        """
        a method used to update the width and height after a change has been made
        :return: none
        """
        self.DIMENSION = (self.WIDTH, self.HEIGHT)

    def updatePOS(self):
        self.POS = (self.X, self.Y)

    def setPOS(self, X, Y):
        """
        a setter method used to change the location of a sprite on screen
        :param X: int
        :param Y: int
        :return: none
        """
        self.X = X
        self.Y = Y
        self.updatePOS()

    def setScaleX (self, SCALE_X):
        self.SCREEN = pygame.transform.scale(self.SCREEN, (int(self.getWidth()-SCALE_X), int(self.getHeight())))

    # --- ACCESSOR METHODS (GETTER) --- #
    def getBox(self):
        return self.SCREEN

    def getPOS(self):
        return self.POS

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getWidth(self):
        return self.SCREEN.get_rect().width

    def getHeight(self):
        return self.SCREEN.get_rect().height