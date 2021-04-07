"""
title: Abstract Sprite Class
author: Ishaan Chandel
date-created: 2021-03-03
"""

import pygame


class MySprite:
    """
    class used to construct a sprite and its necessary attributes
    """

    def __init__(self):
        """
        attributes that are necessary to construct a sprite object and then manipulate it afterwards
        """
        self.WIDTH = 0
        self.HEIGHT = 0
        self.DIMENSION = (self.WIDTH, self.HEIGHT)
        self.SCREEN = None
        self.X = 0
        self.Y = 0
        self.POS = (self.X, self.Y)
        self.SPD = 5
        self.MOVEMENTY = 50
        self.MOVEMENTX = 2

    # Setters

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

    def updatePOS(self):
        self.POS = (self.X, self.Y)

    def updateDimension(self):
        """
        a method used to update the width and height after a change has been made
        :return: none
        """
        self.DIMENSION = (self.WIDTH, self.HEIGHT)

    def wasdMove(self, KEYPRESSES):
        # CHECK KEYPRESSES
        if KEYPRESSES[pygame.K_d] == 1:
            self.X = self.X + self.SPD
        if KEYPRESSES[pygame.K_a] == 1:
            self.X -= self.SPD
        if KEYPRESSES[pygame.K_w] == 1:
            self.Y -= self.SPD
        if KEYPRESSES[pygame.K_s] == 1:
            self.Y += self.SPD

        self.POS = (self.X, self.Y)

    def adMove(self, KEYPRESSES):
        # CHECK KEYPRESSES
        if KEYPRESSES[pygame.K_d] == 1:
            self.X = self.X + self.SPD
        if KEYPRESSES[pygame.K_a] == 1:
            self.X -= self.SPD
        self.POS = (self.X, self.Y)

    # Getters

    """
    The following methods are all examples of polymorphism where they will return a different 
    value for every child class that is created utilizng the parent, MySprite, class.
    """

    def getScreen(self):
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

    def getRect(self):
        self.RECT = self.SCREEN.get_rect()
        self.RECT.x = self.X
        self.RECT.y = self.Y
        return self.RECT

    def checkBounds(self, MAXWIDTH, MAXHEIGHT, MINWIDTH=0, MINHEIGHT=0):
        """
        a subroutine used to check boundaries of the screen
        :param MAXWIDTH: int
        :param MAXHEIGHT: int
        :param MINWIDTH: int
        :param MINHEIGHT: int
        :return: None
        """
        if self.X > MAXWIDTH - self.getWidth():
            self.X = MAXWIDTH - self.getWidth()
        elif self.X < MINWIDTH:
            self.X = MINWIDTH

        if self.Y > MAXHEIGHT - self.getHeight():
            self.Y = MAXHEIGHT - self.getHeight()
        elif self.Y < MINHEIGHT:
            self.Y = MINHEIGHT

        self.updatePOS()

    def wasdMoveChkBounds(self, KEYPRESSES, MAXWIDTH, MAXHEIGHT, MINWIDTH=0, MINHEIGHT=0):
        self.wasdMove(KEYPRESSES)
        self.checkBounds(MAXWIDTH, MAXHEIGHT, MINWIDTH, MINHEIGHT)
