import pygame
import sys

class Player_Left(pygame.Rect):

    size = [15, 100]
    speed = 10

    def __init__(self, screen, WIDTH, HEIGTH, color):
        super().__init__(10, HEIGTH/2-self.size[1]/2, self.size[0], self.size[1])
        self.screen = screen
        self.color = color
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
    
    def start(self):
        pass

    def update(self):
        self.clamp_ip(0,0,self.WIDTH, self.HEIGTH)


    def darw(self):
        pygame.draw.rect(self.screen, self.color, self)
