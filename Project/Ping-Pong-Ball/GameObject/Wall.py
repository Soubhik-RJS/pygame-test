import pygame
import sys

class Wall(pygame.Rect):

    TILE_SIZE = 40

    def __init__(self, screen, x, y, color):
        super().__init__(x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
        self.screen = screen
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self)