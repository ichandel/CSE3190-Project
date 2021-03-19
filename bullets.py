"""
title: bullets
"""

import pygame
from mySprite import MySprite

class Bullets(MySprite):
    def __init__(self):
        super().__init__()
        self.WIDTH = 10
        self.HEIGHT = 40
        self.SPD = 10