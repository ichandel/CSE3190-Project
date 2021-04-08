"""
Title: Game Engine
Author: Ishaan Chandel
Date: 2021-03-04
"""

from loader import images
from loader import Colour
from window import Window
from text import Text
from imageSprite import ImageSprite
from enemies import alien
from bullet import bullets
from ships import Ships
import pygame
from random import randrange

class Game:

    pygame.init()

    def __init__(self):
        self.WINDOW = Window(WIDTH=1920, HEIGHT=1080, FPS=60)
        self.WINDOW.setBackgroundColor(Colour.GREY)
        self.PLAYER = Ships(images.SHIP1)
        self.OPTPLAYER = Ships(images.SHIP1)
        self.OPTPLAYER.setScale(1)
        self.OPTPLAYER2 = Ships(images.SHIP2)
        self.OPTPLAYER2.setScale(1)
        self.OPTPLAYER3 = Ships(images.SHIP3)
        self.OPTPLAYER3.setScale(1.2)
        self.ALIEN = alien(images.ALIEN_SHIP, 120, 102)
        self.ALIEN.setScale(1.8)
        self.ARROW = ImageSprite(images.UP_ARROW)
        self.ARROW.setScale(4)
        self.SCORE = 0
        self.SCORE_TEXT = Text(f"Score: {self.SCORE}")
        self.BULLET = bullets(images.BULLET, -1000, -1000, 0)
        self.BULLETS = []
        self.ENEMYBULLETS = []
        self.POSITIONARRAYS = [[],[],[],[],[]]
        self.COLUMN1X = ((self.WINDOW.getVirtualWidth() // 6) * 1) - self.ALIEN.getWidth() // 2
        self.COLUMN2X = ((self.WINDOW.getVirtualWidth() // 6) * 2) - self.ALIEN.getWidth() // 2
        self.COLUMN3X = (self.WINDOW.getVirtualWidth() // 2) - self.ALIEN.getWidth() // 2
        self.COLUMN4X = ((self.WINDOW.getVirtualWidth() // 6) * 4) - self.ALIEN.getWidth() // 2
        self.COLUMN5X = ((self.WINDOW.getVirtualWidth() // 6) * 5) - self.ALIEN.getWidth() // 2
        self.ROW1Y = (self.WINDOW.getVirtualHeight() // 12) * 1
        self.ROW2Y = (self.WINDOW.getVirtualHeight() // 12) * 2
        self.ROW3Y = (self.WINDOW.getVirtualHeight() // 12) * 3
        self.ROW4Y = (self.WINDOW.getVirtualHeight() // 12) * 4
        self.ROW5Y = (self.WINDOW.getVirtualHeight() // 12) * 5
        self.ROWYVALUES = []
        self.ROWYVALUES.append(self.ROW1Y)
        self.ROWYVALUES.append(self.ROW2Y)
        self.ROWYVALUES.append(self.ROW3Y)
        self.ROWYVALUES.append(self.ROW4Y)
        self.ROWYVALUES.append(self.ROW5Y)
        self.pressed = False
        self.FIRE = False
        self.TIMER = pygame.time.Clock()
        self.TIMER_MS1 = 400
        self.TIMER_MS2  = 300
        self.TIME_LEFT = 30

    def placeAliens(self):
        """
        places all aliens for level 1
        """
        for i in range(5):
            self.POSITIONARRAYS[0].append(alien(images.ALIEN_SHIP, self.COLUMN1X, self.ROWYVALUES[i]))
            self.POSITIONARRAYS[0][i].setScale(1.8)
        for i in range(5):
            self.POSITIONARRAYS[1].append(alien(images.ALIEN_SHIP, self.COLUMN2X, self.ROWYVALUES[i]))
            self.POSITIONARRAYS[1][i].setScale(1.8)
        for i in range(5):
            self.POSITIONARRAYS[2].append(alien(images.ALIEN_SHIP, self.COLUMN3X, self.ROWYVALUES[i]))
            self.POSITIONARRAYS[2][i].setScale(1.8)
        for i in range(5):
            self.POSITIONARRAYS[3].append(alien(images.ALIEN_SHIP, self.COLUMN4X, self.ROWYVALUES[i]))
            self.POSITIONARRAYS[3][i].setScale(1.8)
        for i in range(5):
            self.POSITIONARRAYS[4].append(alien(images.ALIEN_SHIP, self.COLUMN5X, self.ROWYVALUES[i]))
            self.POSITIONARRAYS[4][i].setScale(1.8)



    def getSpriteCollision(self, SPRITE1, SPRITE2):
        if pygame.Rect.colliderect(SPRITE1.getRect(), SPRITE2.getRect()):
            return True
        else:
            return False


    def startScreen(self):
        """
        makes start screen for game
        """

        self.ARROW.setPOS((self.WINDOW.getVirtualWidth() - self.ARROW.getWidth()) // 2 - 300, (self.WINDOW.getVirtualHeight() - self.ARROW.getHeight()) // 2 + 275)

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

        # the following code creates, positions and blits on various text objects for user readability

            self.WINDOW.clearScreen()
            self.TITLE = Text("Welcome To Space Invaders!")
            self.SUBTITLE = Text("Use the A and D keys to move your ship.", FONTSIZE=20)
            self.SUBTITLE4 = Text("Press SPACE to Fire The Ship!", FONTSIZE=20)
            self.SUBTITLE5 = Text("Press ENTER to continue.", FONTSIZE=20)
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
            self.WINDOW.getScreen().blit(self.ARROW.getScreen(), self.ARROW.getPOS())
            # processing
            # the following code allows the paddle object to change colour according to user needs

            if KEYPRESSES[pygame.K_1]:
                self.PLAYER = Ships(images.SHIP1)
                self.PLAYER.setScale(1)
                self.ARROW.setPOS((self.WINDOW.getVirtualWidth() - self.ARROW.getWidth()) // 2 - 300,(self.WINDOW.getVirtualHeight() - self.ARROW.getHeight()) // 2 + 275)
            if KEYPRESSES[pygame.K_2]:
                self.PLAYER = Ships(images.SHIP2)
                self.PLAYER.setScale(1)
                self.ARROW.setPOS((self.WINDOW.getVirtualWidth() - self.ARROW.getWidth()) // 2,(self.WINDOW.getVirtualHeight() - self.ARROW.getHeight()) // 2 + 275)
            if KEYPRESSES[pygame.K_3]:
                self.PLAYER = Ships(images.SHIP3)
                self.PLAYER.setScale(1.2)
                self.ARROW.setPOS((self.WINDOW.getVirtualWidth() - self.ARROW.getWidth()) // 2+300,(self.WINDOW.getVirtualHeight() - self.ARROW.getHeight()) // 2 + 325)

            self.WINDOW.updateFrame()


            if KEYPRESSES[pygame.K_RETURN]:  # this line runs the main game once the user is ready
                self.run()
            if KEYPRESSES[pygame.K_ESCAPE]:  # this exits the program when the user wishes to
                exit()

    def endScreen(self):

        self.TITLE2 = Text("Game Over!")
        self.SUBTITLE2 = Text("Press SPACE to play again.", FONTSIZE=20)
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

            if KEYPRESSES[pygame.K_SPACE]:
                self.startScreen()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def pauseScreen(self):  # screen between levels to allow for a break

        self.TITLE3 = Text("Level One Complete!")
        self.SUBTITLE7 = Text("Press ENTER to continue to Level 2.", FONTSIZE=20)
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
                self.bossTime()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def winScreen(self):  # screen displayed after completing level 2

        self.TITLE4 = Text("Game Complete!")
        self.SUBTITLE8 = Text("Press SPACE to play again.", FONTSIZE=20)
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

            if KEYPRESSES[pygame.K_SPACE]:
                self.startScreen()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def run(self):
        """
        contains code to create and run all of phase 1 and its roles
        """

        self.SCORE = 0
        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
        self.placeAliens()
        self.PLAYER.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.PLAYER.getWidth() // 2, self.WINDOW.getVirtualHeight() - self.PLAYER.getHeight() - 50)
        for item in self.BULLETS:
            self.BULLETS.pop(self.BULLETS.index(item))
        for item in self.ENEMYBULLETS:
            self.ENEMYBULLETS.pop(self.ENEMYBULLETS.index(item))


        while True:

            self.WINDOW.setBackgroundColor(Colour.BLACK)
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Processing

            TOTALALIENS = len(self.POSITIONARRAYS[0]) + len(self.POSITIONARRAYS[1]) + len(self.POSITIONARRAYS[2]) + len(self.POSITIONARRAYS[3]) + len(self.POSITIONARRAYS[4])

            KEYPRESSES = pygame.key.get_pressed()

            self.PLAYER.adMove(KEYPRESSES, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())
            for j in range(len(self.POSITIONARRAYS)):
                for i in range(len(self.POSITIONARRAYS[j])):
                    self.POSITIONARRAYS[j][i].enemyMovement()

            self.TIMER_MS1 += 5
            self.TIMER_MS2 += 5
            if self.TIMER_MS1 > 300:
                if KEYPRESSES[pygame.K_SPACE] == 1:
                    self.pressed = True
                    self.BULLETS.append(bullets(images.BULLET, (self.PLAYER.X + (self.PLAYER.getWidth() // 2)) - (self.BULLET.getWidth() // 2) + 37.5, self.PLAYER.Y, -1))
                    self.BULLETS[-1].setScale(4)
                    self.BULLETS[-1].updatePOS()
                    self.TIMER_MS1 = 0

            if self.TIMER_MS2 > 500:
                SHOOTVAR = randrange(5)
                while len(self.POSITIONARRAYS[SHOOTVAR]) <= 0:
                    SHOOTVAR = randrange(5)
                self.ENEMYBULLETS.append(bullets(images.ENEMYBULLET, (self.POSITIONARRAYS[SHOOTVAR][-1].X + (self.ALIEN.getWidth() // 2)) - (self.BULLET.getWidth() // 2) + 37.5, self.POSITIONARRAYS[SHOOTVAR][-1].Y + self.ALIEN.getHeight(), 1))
                self.ENEMYBULLETS[-1].setScale(4)
                self.ENEMYBULLETS[-1].updatePOS()
                self.TIMER_MS2 = 0



            for i in range(len(self.BULLETS)-1, -1, -1):
                self.BULLETS[i].bulletMovement()
                self.BULLETS[i].updatePOS()

            for i in range(len(self.ENEMYBULLETS)-1, -1, -1):
                self.ENEMYBULLETS[i].SPD = 5
                self.ENEMYBULLETS[i].bulletMovement()
                self.ENEMYBULLETS[i].updatePOS()

            for i in range(len(self.BULLETS) - 1, -1, -1):
                if self.BULLETS[i].X < (0 - self.BULLETS[i].getHeight()):
                    self.BULLETS.pop(i)


            for item in (self.ENEMYBULLETS):
                if self.getSpriteCollision(item, self.PLAYER):
                    for item in self.BULLETS:
                        self.BULLETS.pop(self.BULLETS.index(item))
                    for item in self.ENEMYBULLETS:
                        self.ENEMYBULLETS.pop(self.ENEMYBULLETS.index(item))

                    for i in range(len(self.POSITIONARRAYS[0]) -1, -1, -1):
                        self.POSITIONARRAYS[0].pop(i)
                    for i in range(len(self.POSITIONARRAYS[1]) -1, -1, -1):
                        self.POSITIONARRAYS[1].pop(i)
                    for i in range(len(self.POSITIONARRAYS[2]) -1, -1, -1):
                        self.POSITIONARRAYS[2].pop(i)
                    for i in range(len(self.POSITIONARRAYS[3]) -1, -1, -1):
                        self.POSITIONARRAYS[3].pop(i)
                    for i in range(len(self.POSITIONARRAYS[4]) -1, -1, -1):
                        self.POSITIONARRAYS[4].pop(i)

                    self.SCORE = 0
                    self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                    self.endScreen()

            if TOTALALIENS > 0:
                if self.pressed == True:
                    for j in range(len(self.POSITIONARRAYS) - 1, -1, -1):
                        for i in range(len(self.POSITIONARRAYS[j]) - 1, -1, -1):
                            for item in (self.BULLETS):
                                if self.getSpriteCollision(item, self.POSITIONARRAYS[j][i]):
                                    self.BULLETS.pop(self.BULLETS.index(item))
                                    self.POSITIONARRAYS[j].pop(i)
                                    self.SCORE += 10
                                    self.SCORE_TEXT.setText(f"Score: {self.SCORE}")

            if TOTALALIENS == 0 and self.SCORE == 250:
                self.pauseScreen()

            self.WINDOW.clearScreen()
            for item in self.BULLETS:
                self.WINDOW.getScreen().blit(item.getScreen(), item.getPOS())
            for item in self.ENEMYBULLETS:
                self.WINDOW.getScreen().blit(item.getScreen(), item.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())

            for j in range(len(self.POSITIONARRAYS)):
                for i in range(len(self.POSITIONARRAYS[j])):
                    self.WINDOW.getScreen().blit(self.POSITIONARRAYS[j][i].getScreen(), self.POSITIONARRAYS[j][i].getPOS())

            self.WINDOW.updateFrame()

    def bossTime(self):
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