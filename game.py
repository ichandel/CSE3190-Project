"""
Title: Game Engine
Author: Ishaan Chandel
Date: 2021-03-04
"""

from loader import imageShips
from loader import Colour
from window import Window
from text import Text
from imageSprite import ImageSprite
from positionArrays import PositionArrays
from bullets import Bullets
from enemies import alien
from ships import Ships
import pygame

class Game:

    pygame.init()

    def __init__(self):
        self.WINDOW = Window(WIDTH=1920, HEIGHT=1080, FPS=60)
        self.WINDOW.setBackgroundColor(Colour.GREY)
        self.PLAYER = Ships(imageShips.SHIP1)
        self.OPTPLAYER = Ships(imageShips.SHIP1)
        self.OPTPLAYER.setScale(1)
        self.OPTPLAYER2 = Ships(imageShips.SHIP2)
        self.OPTPLAYER2.setScale(1)
        self.OPTPLAYER3 = Ships(imageShips.SHIP3)
        self.OPTPLAYER3.setScale(1.2)
        self.POSITIONARRAYS = PositionArrays()
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"Score: {self.SCORE}")


    def placeAliensPhase1(self):
        """
        places all aliens for level 1
        """
        STARTX = 0
        STARTY = 50
        for j in range(6):
            for i in range(5):
                if STARTX < (self.WINDOW.getVirtualWidth() // 10) * 8:
                    STARTX = STARTX + self.WINDOW.getVirtualWidth() // 10
                else:
                    STARTX = self.WINDOW.getVirtualWidth() // 10
                    STARTY = STARTY + 120
                NEWALIEN = alien(imageShips.ALIEN_SHIP, STARTX, STARTY)
                #self.POSITIONARRAYS.COLUMNS[j][i].append(NEWALIEN)



    def getSpriteCollision(self, SPRITE1, SPRITE2):
        if pygame.Rect.colliderect(SPRITE1.getRect(), SPRITE2.getRect()):
            return True
        else:
            return False

    def startScreen(self):
        """
        makes start screen for game
        """

        # the following code creates, positions and blits on various text objects for user readability

        self.TITLE = Text("Welcome To Space Invaders!")
        self.SUBTITLE = Text("Use the A and D keys to move your ship.", FONTSIZE=20)
        self.SUBTITLE4 = Text("Press Space to Fire The Ship!", FONTSIZE=20)
        self.SUBTITLE5 = Text("Press enter to continue.", FONTSIZE=20)
        self.SUBTITLE6 = Text("Press ESC to exit.", FONTSIZE=20)
        self.SUBTITLE9 = Text("Which ship would you like to use?", FONTSIZE=20)
        self.OPT1 = Text("[1] Default: ", FONTSIZE=15)
        self.OPT2 = Text("[2]: ", FONTSIZE=15)
        self.OPT3 = Text("[3]: ", FONTSIZE=15)
        self.OPT4 = Text("[4]: ", FONTSIZE=15)
        self.OPT5 = Text("[5]: ", FONTSIZE=15)
        self.TITLE.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE.getHeight()) // 2 - 200)
        self.SUBTITLE.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE.getHeight()) // 2 - 130)
        self.SUBTITLE4.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE4.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE4.getHeight()) // 2 - 100)
        self.SUBTITLE5.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE5.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE5.getHeight()) // 2 - 70)
        self.SUBTITLE6.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE6.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE6.getHeight()) // 2 - 40)
        self.SUBTITLE9.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE9.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE9.getHeight()) // 2 - 10)
        self.OPT1.setPOS((self.WINDOW.getVirtualWidth() - self.OPT1.getWidth()) // 2-300, (self.WINDOW.getVirtualHeight() - self.OPT1.getHeight()) // 2 + 15)
        self.OPT2.setPOS((self.WINDOW.getVirtualWidth() - self.OPT2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.OPT2.getHeight()) // 2 + 15)
        self.OPT3.setPOS((self.WINDOW.getVirtualWidth() - self.OPT3.getWidth()) // 2+300, (self.WINDOW.getVirtualHeight() - self.OPT3.getHeight()) // 2 +15)
        self.OPTPLAYER.setPOS((self.WINDOW.getVirtualWidth() - self.OPTPLAYER.getWidth()) // 2 - 300, (self.WINDOW.getVirtualHeight() - self.OPTPLAYER.getHeight()) // 2 + 125)
        self.OPTPLAYER2.setPOS((self.WINDOW.getVirtualWidth() - self.OPTPLAYER2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.OPTPLAYER2.getHeight()) // 2 + 125)
        self.OPTPLAYER3.setPOS((self.WINDOW.getVirtualWidth() - self.OPTPLAYER3.getWidth()) // 2 + 300, (self.WINDOW.getVirtualHeight() - self.OPTPLAYER3.getHeight()) // 2 + 150)
        self.WINDOW.getScreen().blit(self.TITLE.getScreen(), self.TITLE.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE.getScreen(), self.SUBTITLE.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE4.getScreen(), self.SUBTITLE4.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE5.getScreen(), self.SUBTITLE5.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE6.getScreen(), self.SUBTITLE6.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE9.getScreen(), self.SUBTITLE9.getPOS())
        self.WINDOW.getScreen().blit(self.OPT1.getScreen(), self.OPT1.getPOS())
        self.WINDOW.getScreen().blit(self.OPT2.getScreen(), self.OPT2.getPOS())
        self.WINDOW.getScreen().blit(self.OPT3.getScreen(), self.OPT3.getPOS())
        self.WINDOW.getScreen().blit(self.OPTPLAYER.getScreen(), self.OPTPLAYER.getPOS())
        self.WINDOW.getScreen().blit(self.OPTPLAYER2.getScreen(), self.OPTPLAYER2.getPOS())
        self.WINDOW.getScreen().blit(self.OPTPLAYER3.getScreen(), self.OPTPLAYER3.getPOS())

        self.WINDOW.updateFrame()

        # processing

        # the following code allows the paddle object to change colour according to user needs

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            if KEYPRESSES[pygame.K_1]:
                self.PLAYER = Ships(imageShips.SHIP1)
                self.PLAYER.setScale(1)
            if KEYPRESSES[pygame.K_2]:
                self.PLAYER = Ships(imageShips.SHIP2)
                self.PLAYER.setScale(1)
            if KEYPRESSES[pygame.K_3]:
                self.PLAYER = Ships(imageShips.SHIP3)
                self.PLAYER.setScale(1.2)

            if KEYPRESSES[pygame.K_RETURN]:  # this line runs the main game once the user is ready
                self.runPhase1()
            if KEYPRESSES[pygame.K_ESCAPE]:  # this exits the program when the user wishes to
                exit()

    def endScreen(self):

        self.TITLE2 = Text("Game Over!")
        self.SUBTITLE2 = Text("Press enter to play again.", FONTSIZE=20)
        self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
        self.TITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE2.getHeight()) // 2 - 50)
        self.SUBTITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE2.getHeight()) // 2 + 20)
        self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
        self.WINDOW.getScreen().blit(self.TITLE2.getScreen(), self.TITLE2.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE2.getScreen(), self.SUBTITLE2.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
        self.WINDOW.updateFrame()

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runPhase1()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def pauseScreen(self):  # screen between levels to allow for a break

        self.TITLE3 = Text("Level One Complete!")
        self.SUBTITLE7 = Text("Press enter to continue to Level 2.", FONTSIZE=20)
        self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
        self.TITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE3.getHeight()) // 2 - 50)
        self.SUBTITLE7.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE7.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE7.getHeight()) // 2 + 20)
        self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
        self.WINDOW.getScreen().blit(self.TITLE3.getScreen(), self.TITLE3.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE7.getScreen(), self.SUBTITLE7.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
        self.WINDOW.updateFrame()

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runPhase2()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def winScreen(self):  # screen displayed after completing level 2

        self.TITLE4 = Text("Game Complete!")
        self.SUBTITLE8 = Text("Press enter to play again.", FONTSIZE=20)
        self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
        self.TITLE4.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE4.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE4.getHeight()) // 2 - 50)
        self.SUBTITLE8.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE8.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE8.getHeight()) // 2 + 20)
        self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
        self.WINDOW.getScreen().blit(self.TITLE4.getScreen(), self.TITLE4.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE8.getScreen(), self.SUBTITLE8.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
        self.WINDOW.updateFrame()

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            if KEYPRESSES[pygame.K_RETURN]:
                self.runPhase1()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def runPhase1(self):
        """
        contains code to create and run all of phase 1 and its roles
        """

        self.SCORE = 0
        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
        self.placeAliensPhase1()
        self.PLAYER.setPOS(self.WINDOW.getVirtualWidth() // 2,self.WINDOW.getVirtualHeight() - self.PLAYER.getHeight() - 50)


        while True:

            self.WINDOW.setBackgroundColor(Colour.BLACK)
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Processing

            KEYPRESSES = pygame.key.get_pressed()

            self.PLAYER.adMove(KEYPRESSES, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())
            #self.ALIEN.enemyMovement((self.WINDOW.getVirtualWidth() - self.ALIEN.getWidth() - 50), self.WINDOW.getVirtualHeight(), 50)



            self.WINDOW.clearScreen()
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())
            #self.WINDOW.getScreen().blit(self.ALIEN.getScreen(), self.ALIEN.getPOS())
            self.WINDOW.updateFrame()

    def runPhase2(self):
        """
        contains code to create and run all of phase 2 and its roles
        """

        self.SCORE = 0
        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Processing

            KEYPRESSES = pygame.key.get_pressed()

            self.WINDOW.clearScreen()
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.updateFrame()



if __name__ == "__main__":
    GAME = Game()

    GAME.startScreen()