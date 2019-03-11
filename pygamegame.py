import pygame
from setup import *
from foodClasses import *
from dragstuff import *

class PygameGame(object):

    def init(self):
        pygame.font.init()
        self.burger = Food(["bun.png", "greaseblob.png", "ketchupblob.png",\
         "patty.png", "mushroom.png",\
         "cheese.png", "tomato.png", "fries.png", "lettuce.png"])
        self.currFood = self.burger
        self.state = "homeScreen"
        self.bkg = bkg
        self.ingr = None
        self.toDraw = dict()
        self.toDraw[self.currFood] = self.currFood
        self.score = 0
        self.bunSpeed = 5


    def mousePressed(self, x, y):
        if self.state == "homeScreen":
            if 123 < x < 372 and 617 < y < 698:
                pass # draw instructions
            elif 123 < x < 372 and 529 < y < 610:
                self.state = "play"
                self.bkg = gamebkg
                self.toDraw[bkg] = (gamebkg, (0, 0))
                peachColor = (255, 189,140)
                screen.fill(peachColor)
                screen.blit(self.bkg,(0,0))

        elif self.state == "play":
            # screen.blit(bun,(0,0))
            # screen.blit(patty,(0,0))
            # screen.blit(mRoom,(10,10))
            if x > 1200 and y < 100:
                self.init()
                self.toDraw[bkg] = (self.bkg,(0,0))

    def mouseReleased(self, x, y):
        if self.ingr == None:
            return
        currFood = self.burger  #TODO generalize
        i = len(currFood.ingredients)
        currIngr = currFood.recipe[i]
        r = currFood.r
        ingX = currFood.x
        ingY = currFood.y
        if ingX - r < x < ingX + r and ingY - r < y < ingY + r:
            # drop it like it's hot
            # make sure it's the right ingredient:
            if currIngr == self.ingr:  # else you done fucked up
                self.currFood.ingredients.append(self.ingr)
            del self.toDraw[self.ingr]
            self.ingr = None
            return
        del self.toDraw[self.ingr]
        self.ingr = None

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        if self.ingr == None:
            self.ingr = IngredientclickedOn(None, None)
            if self.ingr == None:
                return  # no ingr clicked on
        self.toDraw[self.ingr] = (self.ingr.name, (x - 33, y - 33))


    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        if self.score < 0:
            self.init()
            self.toDraw[bkg] = (self.bkg,(0,0))
        peachColor = (255, 189,140)
        screen.fill(peachColor)
        for item in self.toDraw:
            if not isinstance(self.toDraw[item], tuple):
                # has its own draw function
                item.draw()
            else:
                img = self.toDraw[item][0]
                if type(img) == str: img = pygame.image.load(img)
                coords = self.toDraw[item][1]
                screen.blit(img, coords)
        if self.state == "play":
            self.burger.draw()
            self.burger.move(self.bunSpeed, 0)
            if self.burger.x >= 1350:
                if self.burger.ingredients == self.burger.recipe:
                    self.score += 1
                    self.bunSpeed += 1
                else:
                    self.score -= 1
                self.burger.draw()
                self.burger.ingredients = [self.burger.recipe[0]]
                self.burger.x = -100

            scoretext = pygame.font.SysFont("monospace", 100).\
            render("Score: " + str(self.score), 1, (0, 0, 0))
            screen.blit(scoretext, (750, 90))
        # draw draggable last:
        if self.ingr == None: return
        img = pygame.image.load(self.ingr.name)
        screen.blit(img, coords)

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
        self.toDraw[bkg] = (self.bkg,(0,0))
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)

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
