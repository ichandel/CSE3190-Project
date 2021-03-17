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