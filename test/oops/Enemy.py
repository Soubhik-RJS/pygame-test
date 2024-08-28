import pygame
import sys

class Enemy:
    speed = 10
    color = (255,0,0)
    radius = 30
    def __init__(self,screen,width, height):
        self.circle = pygame.draw.circle(screen, self.color, (width // 2+200, height // 2+200),self.radius)
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = screen

    def start(self):
        print("start")
    
    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.circle.center, self.radius)
