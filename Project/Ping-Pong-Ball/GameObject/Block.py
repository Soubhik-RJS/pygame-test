import pygame
import sys

class Block(pygame.Rect):

    TILE_SIZE_X = 100
    TILE_SIZE_Y = 40

    def __init__(self, screen, x, y, color):
        super().__init__(x * self.TILE_SIZE_X, y * self.TILE_SIZE_Y, self.TILE_SIZE_X, self.TILE_SIZE_Y)
        self.screen = screen
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self)