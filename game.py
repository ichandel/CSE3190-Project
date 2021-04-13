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
from box import Box

class Game:

    pygame.init()

    def __init__(self):
        self.WINDOW = Window(WIDTH=1920, HEIGHT=1080, FPS=60)
        self.WINDOW.setBackgroundColor(Colour.BLACK)
        self.PLAYER = Ships(images.SHIP1)
        self.OPTPLAYER = Ships(images.SHIP1)
        self.OPTPLAYER.setScale(1)
        self.OPTPLAYER2 = Ships(images.SHIP2)
        self.OPTPLAYER2.setScale(1)
        self.OPTPLAYER3 = Ships(images.SHIP3)
        self.OPTPLAYER3.setScale(1.2)
        self.ALIEN = alien(images.ALIEN_SHIP, -1000, -1000)
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
        self.CHANGEDBORDERLEFT = 0
        self.CHANGEDBORDERRIGHT = 0
        self.chngleftmultiplier = 0
        self.checked = False
        self.TIMER = pygame.time.Clock()
        self.TIMER_MS1 = 400
        self.TIMER_MS2  = 300
        self.TIME_LEFT = 30
        self.STARS = []
        for i in range(100):
            SIZE = randrange(2, 10)
            self.STARS.append(Box(SIZE, SIZE, randrange(self.WINDOW.getVirtualWidth()), randrange(self.WINDOW.getVirtualHeight())))
        self.BARLENGTH = 200

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
            self.TITLE = Text("Welcome To Galactic Raiders!")
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
            for i in self.STARS:
                self.WINDOW.getScreen().blit(i.getBox(), i.getPOS())

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

        self.TITLE2 = Text("The Raiders Took Down Your Ship!")
        self.SUBTITLE2 = Text("Press LSHIFT to try and stop them again.", FONTSIZE=20)
        self.SUBTITLE3 = Text("Press ESC to give up.", FONTSIZE=20)
        self.TITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE2.getHeight()) // 2 - 50)
        self.SUBTITLE2.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE2.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE2.getHeight()) // 2 + 20)
        self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
        self.WINDOW.getScreen().blit(self.TITLE2.getScreen(), self.TITLE2.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE2.getScreen(), self.SUBTITLE2.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
        for i in self.STARS:
            self.WINDOW.getScreen().blit(i.getBox(), i.getPOS())
        self.WINDOW.updateFrame()

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            if KEYPRESSES[pygame.K_LSHIFT]:
                self.startScreen()
            if KEYPRESSES[pygame.K_ESCAPE]:
                exit()

    def breakScreen(self):  # screen between levels to allow for a break

        self.TITLE3 = Text("You Defeated The Raiders! Uh oh, looks like the Mothership is coming!")
        self.SUBTITLE7 = Text("Press ENTER to continue to face the Mothership.", FONTSIZE=20)
        self.TITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE3.getHeight()) // 2 - 50)
        self.SUBTITLE7.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE7.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE7.getHeight()) // 2 + 20)
        self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
        self.WINDOW.getScreen().blit(self.TITLE3.getScreen(), self.TITLE3.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE7.getScreen(), self.SUBTITLE7.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
        for i in self.STARS:
            self.WINDOW.getScreen().blit(i.getBox(), i.getPOS())
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

    def winScreen(self):  # screen displayed after completing level 2

        self.WINDOW.clearScreen()
        self.TITLE4 = Text("You Defeated All The Raiders!")
        self.SUBTITLE8 = Text("Press LSHIFT to play again.", FONTSIZE=20)
        self.SUBTITLE3 = Text("Press ESC to exit.", FONTSIZE=20)
        self.TITLE4.setPOS((self.WINDOW.getVirtualWidth() - self.TITLE4.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.TITLE4.getHeight()) // 2 - 50)
        self.SUBTITLE8.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE8.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE8.getHeight()) // 2 + 20)
        self.SUBTITLE3.setPOS((self.WINDOW.getVirtualWidth() - self.SUBTITLE3.getWidth()) // 2, (self.WINDOW.getVirtualHeight() - self.SUBTITLE3.getHeight()) // 2 + 50)
        self.WINDOW.getScreen().blit(self.TITLE4.getScreen(), self.TITLE4.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE8.getScreen(), self.SUBTITLE8.getPOS())
        self.WINDOW.getScreen().blit(self.SUBTITLE3.getScreen(), self.SUBTITLE3.getPOS())
        self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
        for i in self.STARS:
            self.WINDOW.getScreen().blit(i.getBox(), i.getPOS())
        self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())
        self.WINDOW.getScreen().blit(self.BAR.getBox(), self.BAR.getPOS())
        self.WINDOW.getScreen().blit(self.BARTOP.getBox(), self.BARTOP.getPOS())
        self.WINDOW.getScreen().blit(self.BARBOT.getBox(), self.BARBOT.getPOS())
        self.WINDOW.getScreen().blit(self.BARLFT.getBox(), self.BARLFT.getPOS())
        self.WINDOW.getScreen().blit(self.BARRGT.getBox(), self.BARRGT.getPOS())
        self.WINDOW.updateFrame()

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()

            if KEYPRESSES[pygame.K_LSHIFT]:
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


            for item in self.ENEMYBULLETS:
                for items in self.BULLETS:
                    if self.getSpriteCollision(item, items):
                        self.BULLETS.pop(self.BULLETS.index(items))
                        self.ENEMYBULLETS.pop(self.ENEMYBULLETS.index(item))

            for i in self.STARS:
                i.moveBoxWrap(KEYPRESSES, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())


            for item in self.ENEMYBULLETS:
                if self.getSpriteCollision(item, self.PLAYER):
                    for i in range(len(self.BULLETS)-1, -1, -1):
                        self.BULLETS.pop(i)
                    for i in range(len(self.ENEMYBULLETS)-1, -1, -1):
                        self.ENEMYBULLETS.pop(i)

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

            for j in range(len(self.POSITIONARRAYS) - 1, -1, -1):
                for i in range(len(self.POSITIONARRAYS[j]) - 1, -1, -1):
                        if self.getSpriteCollision(self.PLAYER, self.POSITIONARRAYS[j][i]):
                            for i in range(len(self.BULLETS) - 1, -1, -1):
                                self.BULLETS.pop(i)
                            for i in range(len(self.ENEMYBULLETS) - 1, -1, -1):
                                self.ENEMYBULLETS.pop(i)

                            for i in range(len(self.POSITIONARRAYS[0]) - 1, -1, -1):
                                self.POSITIONARRAYS[0].pop(i)
                            for i in range(len(self.POSITIONARRAYS[1]) - 1, -1, -1):
                                self.POSITIONARRAYS[1].pop(i)
                            for i in range(len(self.POSITIONARRAYS[2]) - 1, -1, -1):
                                self.POSITIONARRAYS[2].pop(i)
                            for i in range(len(self.POSITIONARRAYS[3]) - 1, -1, -1):
                                self.POSITIONARRAYS[3].pop(i)
                            for i in range(len(self.POSITIONARRAYS[4]) - 1, -1, -1):
                                self.POSITIONARRAYS[4].pop(i)
                            self.endScreen()

            for j in range(len(self.POSITIONARRAYS) - 1, -1, -1):
                for i in range(len(self.POSITIONARRAYS[j]) - 1, -1, -1):
                    if self.POSITIONARRAYS[j][i].Y > self.PLAYER.Y:
                        for i in range(len(self.BULLETS) - 1, -1, -1):
                            self.BULLETS.pop(i)
                        for i in range(len(self.ENEMYBULLETS) - 1, -1, -1):
                            self.ENEMYBULLETS.pop(i)

                        for i in range(len(self.POSITIONARRAYS[0]) - 1, -1, -1):
                            self.POSITIONARRAYS[0].pop(i)
                        for i in range(len(self.POSITIONARRAYS[1]) - 1, -1, -1):
                            self.POSITIONARRAYS[1].pop(i)
                        for i in range(len(self.POSITIONARRAYS[2]) - 1, -1, -1):
                            self.POSITIONARRAYS[2].pop(i)
                        for i in range(len(self.POSITIONARRAYS[3]) - 1, -1, -1):
                            self.POSITIONARRAYS[3].pop(i)
                        for i in range(len(self.POSITIONARRAYS[4]) - 1, -1, -1):
                            self.POSITIONARRAYS[4].pop(i)
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
                self.bossTime()

            self.WINDOW.clearScreen()
            for i in self.STARS:
                self.WINDOW.getScreen().blit(i.getBox(), i.getPOS())
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

        self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
        self.PLAYER.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.PLAYER.getWidth() // 2, self.WINDOW.getVirtualHeight() - self.PLAYER.getHeight() - 50)
        self.BOSS = alien(images.MOTHERSHIP, -1000, -1000)
        self.BOSS.setPOS((self.WINDOW.getVirtualWidth() // 2) - (self.BOSS.getWidth() // 2), 100)
        BOSSHEALTH = 200
        self.BARTOP = Box(1010, 1)
        self.BARBOT = Box(1010, 1)
        self.BARLFT = Box(1, 40)
        self.BARRGT = Box(1, 40)
        self.BAR = Box(1000, 25, COLOR=Colour.RED)
        self.BAR.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.BAR.getWidth() // 2, 17)
        self.BARTOP.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.BARTOP.getWidth() // 2, 10)
        self.BARBOT.setPOS(self.WINDOW.getVirtualWidth() // 2 - self.BARBOT.getWidth() // 2, 49)
        self.BARLFT.setPOS((self.WINDOW.getVirtualWidth() // 2 - self.BARTOP.getWidth() // 2) - 1, 10)
        self.BARRGT.setPOS(self.WINDOW.getVirtualWidth() // 2 + self.BARTOP.getWidth() // 2, 10)

        while True:
            # Inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            KEYPRESSES = pygame.key.get_pressed()
            self.PLAYER.adMove(KEYPRESSES, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())

            self.TIMER_MS1 += 5
            self.TIMER_MS2 += 5
            if self.TIMER_MS1 > 300:
                if KEYPRESSES[pygame.K_SPACE] == 1:
                    self.pressed = True
                    self.BULLETS.append(bullets(images.BULLET, (self.PLAYER.X + (self.PLAYER.getWidth() // 2)) - (
                                self.BULLET.getWidth() // 2) + 37.5, self.PLAYER.Y, -1))
                    self.BULLETS[-1].setScale(4)
                    self.BULLETS[-1].updatePOS()
                    self.TIMER_MS1 = 0

            if self.TIMER_MS2 > 500:
                self.ENEMYBULLETS.append(bullets(images.ENEMYBULLET, (self.BOSS.X + (self.BOSS.getWidth() // 2)) - (self.BULLET.getWidth() // 2) + 37.5, self.BOSS.Y + self.BOSS.getHeight(), 1))
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

            for i in self.STARS:
                i.moveBoxWrap(KEYPRESSES, self.WINDOW.getVirtualWidth(), self.WINDOW.getVirtualHeight())


            for items in self.BULLETS:
                if self.getSpriteCollision(self.BOSS, items):
                    self.BULLETS.pop(self.BULLETS.index(items))
                    self.BAR.setScaleX(50)
                    BOSSHEALTH -= 10
                    self.BAR.updateDimension()

            if BOSSHEALTH <= 0:
                self.SCORE += 300
                self.SCORE_TEXT.setText(f"Score: {self.SCORE}")
                for i in range(len(self.BULLETS) - 1, -1, -1):
                    self.BULLETS.pop(i)
                for i in range(len(self.ENEMYBULLETS) - 1, -1, -1):
                    self.ENEMYBULLETS.pop(i)

                for i in range(len(self.POSITIONARRAYS[0]) - 1, -1, -1):
                    self.POSITIONARRAYS[0].pop(i)
                for i in range(len(self.POSITIONARRAYS[1]) - 1, -1, -1):
                    self.POSITIONARRAYS[1].pop(i)
                for i in range(len(self.POSITIONARRAYS[2]) - 1, -1, -1):
                    self.POSITIONARRAYS[2].pop(i)
                for i in range(len(self.POSITIONARRAYS[3]) - 1, -1, -1):
                    self.POSITIONARRAYS[3].pop(i)
                for i in range(len(self.POSITIONARRAYS[4]) - 1, -1, -1):
                    self.POSITIONARRAYS[4].pop(i)
                self.winScreen()



            self.WINDOW.clearScreen()
            for item in self.BULLETS:
                self.WINDOW.getScreen().blit(item.getScreen(), item.getPOS())
            for i in self.STARS:
                self.WINDOW.getScreen().blit(i.getBox(), i.getPOS())
            for item in self.ENEMYBULLETS:
                self.WINDOW.getScreen().blit(item.getScreen(), item.getPOS())
            self.WINDOW.getScreen().blit(self.SCORE_TEXT.getScreen(), self.SCORE_TEXT.getPOS())
            self.WINDOW.getScreen().blit(self.PLAYER.getScreen(), self.PLAYER.getPOS())
            self.WINDOW.getScreen().blit(self.BOSS.getScreen(), self.BOSS.getPOS())
            self.WINDOW.getScreen().blit(self.BAR.getBox(), self.BAR.getPOS())
            self.WINDOW.getScreen().blit(self.BARTOP.getBox(), self.BARTOP.getPOS())
            self.WINDOW.getScreen().blit(self.BARBOT.getBox(), self.BARBOT.getPOS())
            self.WINDOW.getScreen().blit(self.BARLFT.getBox(), self.BARLFT.getPOS())
            self.WINDOW.getScreen().blit(self.BARRGT.getBox(), self.BARRGT.getPOS())
            self.WINDOW.updateFrame()



if __name__ == "__main__":
    GAME = Game()

    GAME.bossTime()