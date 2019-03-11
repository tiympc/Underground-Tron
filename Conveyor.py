import pygame
from setup import *
from foodClasses import *

class PygameGame(object):

    def init(self):
        self.burger = Food(["bun.png", "grease.png", "mushroom.png"])
        self.state = "homeScreen"
        self.bkg = bkg
        self.score = 0
        self.bunSpeed = 15

    def mousePressed(self, x, y):
        print(x,y)
        if self.state == "homeScreen":
            if 123 < x < 372 and 617 < y < 698:
                pass # draw instructions
            elif 123 < x < 372 and 529 < y < 610:
                self.state = "play"
                self.bkg = gamebkg


    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1280, height=800, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        # screen.blit(self.bkg,(0,0))
        playing = True
        while playing:
            peachColor = (255, 189,140)
            screen.fill(peachColor)
            screen.blit(self.bkg,(0,0))
            time = clock.tick(self.fps)
            self.timerFired(time)
            if self.state == "play":
                self.burger.draw()
                self.burger.move(self.bunSpeed, 0)
                if self.burger.x >= 1350:
                    if self.burger.ingredients == self.burger.recipe:
                        self.score += 1
                        self.bunSpeed += 2
                    self.burger.draw()
                    self.burger.ingredients = [self.burger.recipe[0]]
                    self.burger.x = -100
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            self.redrawAll(screen)
            pygame.display.flip()
        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
