"""
title: Text Class
"""

from loader import Colour
import pygame
from mySprite import MySprite

class Text(MySprite): # a child class from the parent (MySprite) class. Example of inheritance

    def __init__(self, TEXT="HELLO WORLD", COLOUR=Colour.WHITE, FONTSIZE=36, FONT="Times New Roman"):
        """
        initializes text objects for output
        :param TEXT: string
        :param COLOUR: tuple
        :param FONTSIZE: int
        :param FONT: string
        """
        super().__init__()
        self.TEXT = TEXT
        self.COLOUR = COLOUR
        self.FONT = pygame.font.SysFont(FONT, FONTSIZE)
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOUR)

    def setText(self, NEW_TEXT):
        """
        a method to change text object's output
        :param NEW_TEXT: string
        :return: none
        """
        self.TEXT = NEW_TEXT
        self.SCREEN = self.FONT.render(self.TEXT, True, self.COLOUR)


if __name__ == "__main__":
    from window import Window
    import sys

    pygame.init()

    WINDOW = Window()
    TEXT1 = Text()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        WINDOW.getScreen().blit(TEXT1.getScreen(), TEXT1.getPOS())
        WINDOW.updateFrame()