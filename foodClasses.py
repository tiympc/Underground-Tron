# Mckenna Brown
import pygame
from setup import *

class Food():
    def __init__(self, ingredients):
        self.recipe = []
        for ingr in ingredients:
            self.recipe.append(Ingredient(ingr))
        # self.recipe = ingredients  # a list. can have repeats
        # ordered. must be put on in this order
        self.ingredients = [self.recipe[0]]
        self.x = -100
        self.y = 550
        self.r = 66

    def __repr__(self):
        return "Food object, ingredients: " + str(self.ingredients)

    def __eq__(self, other):
        if not isinstance(other, Food):
            return False
        return self.ingredients == other.ingredients and \
        self.recipe == other.recipe

    def __hash__(self):
        return hash(tuple(self.recipe))

    def addIngredient(self, ingredient):
        i = len(self.ingredients)
        if self.recipe[i] != ingredient:  # can't drag that
            return False
        else:
            self.ingredients.append(ingredient)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        for ingredient in self.ingredients:
            screen.blit(pygame.image.load(ingredient.name), \
            (self.x - self.r, self.y - self.r))


class Ingredient():
    def __init__(self, img):
        self.name = img
        self.img = pygame.image.load(img)
        self.r = 66

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return "Ingredient obj w img: " + self.name

    def draw(self, x, y):  # for when dragging the item
        screen.blit(self.img, (x, y))
