import pygame
import sys

class Enemy(pygame.Rect):
    
    def __init__(self, screen, WIDTH, HEIGTH, color):
        super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self)