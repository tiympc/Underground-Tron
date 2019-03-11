import pygame
from pygamegame import PygameGame #the framework

class myProject(PygameGame):
    def init(self):
        self.message = "World Helo"
    def mousepressed(self, x, y):
        print(self.message)
        screen.blit(bun,(0,0))
        #gameDisplay.blit(image.load('bkg.png'), (0,0))


#creating and running the game
game = myProject()
game.run()