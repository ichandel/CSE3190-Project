"""
title: Window
author: Ishaan Chandel
date-created: 2021-03-03
"""

import pygame
from loader import Colour
from imageSprite import ImageSprite

class Window:

    def __init__(self, TITLE="Pygame", WIDTH=640, HEIGHT=480, FPS=30):
        """
        initializes the window used for the main program
        :param TITLE: string
        :param WIDTH: int
        :param HEIGHT: int
        :param FPS: int
        """
        self.TITLE = TITLE
        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCREEN_DIMENSIONS = (self.WIDTH, self.HEIGHT)
        self.FRAME = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode(self.SCREEN_DIMENSIONS)
        self.BACKGROUND = Colour.GREY
        self.BACKGROUND_IMAGE = None
        self.SCREEN.fill(self.BACKGROUND)
        self.CAPTION = pygame.display.set_caption(self.TITLE)

    # --- MODIFIER METHODS (SETTER) --- #
    def updateFrame(self):
        self.FRAME.tick(self.FPS)
        pygame.display.flip()

    def clearScreen(self):
        if self.BACKGROUND_IMAGE == None:
            self.SCREEN.fill(self.BACKGROUND)
        else:
            self.SCREEN.blit(self.BACKGROUND_IMAGE.getScreen(), self.BACKGROUND_IMAGE.getPOS())

    def setBackgroundColor(self, COLOR):
        self.BACKGROUND = COLOR

    # --- ACCESSOR METHODS (GETTER) --- #
    def getScreen(self):
        return self.SCREEN

    def getVirtualWidth(self):
        # return self.WIDTH
        return self.SCREEN.get_rect().width

    def getVirtualHeight(self):
        return self.SCREEN.get_rect().height