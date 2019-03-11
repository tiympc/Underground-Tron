# Goal is to make dragging ingredient, turning it upside down, and putting it on conveyer belt. Generate an image get filenmae for image, return an Iengredient(image)

import pygame
from foodClasses import *

def IngredientclickedOn(event, data): # update the third to sixth ingredients w/
                                      # correct file name once completed
    if 300 < pygame.mouse.get_pos()[0] < 467 and \
    263 < pygame.mouse.get_pos()[1] < 414:
        return Ingredient("patty.png")

    elif 487 < pygame.mouse.get_pos()[0] < 603 and \
    270 < pygame.mouse.get_pos()[1] < 411:
        return Ingredient("mushroom.png")

    elif 623 < pygame.mouse.get_pos()[0] < 748 and \
    270 < pygame.mouse.get_pos()[1] < 411:
        return Ingredient("cheese.png")

    elif 778 < pygame.mouse.get_pos()[0] < 912 and \
    270 < pygame.mouse.get_pos()[1] < 411:
        return Ingredient("tomato.png")

    elif 942 < pygame.mouse.get_pos()[0] < 1081 and \
    270 < pygame.mouse.get_pos()[1] < 411:
        return Ingredient("fries.png")

    elif 1108 < pygame.mouse.get_pos()[0] < 1235 and \
    270 < pygame.mouse.get_pos()[1] < 411:
        return Ingredient("lettuce.png")

    elif 95 < pygame.mouse.get_pos()[0] < 147 and \
    260 < pygame.mouse.get_pos()[1] < 396:
        return Ingredient("greaseblob.png")

    elif 203 < pygame.mouse.get_pos()[0] < 256 and \
    260 < pygame.mouse.get_pos()[1] < 396:
        return Ingredient("ketchupblob.png")


    return None
