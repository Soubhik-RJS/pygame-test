import pygame
import sys
import random

class Enemy:
    speed = 10
    color = (255,0,0)
    radius = 30
    speed = [5,5]
    def __init__(self,screen,x,y,width, height,speed, player):
        self.circle = pygame.draw.circle(screen, self.color, (x, y),self.radius)
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = screen
        self.speed = speed
        self.player = player

    def start(self):
        print("start")
    
    def update(self):
        self.circle.move_ip(self.speed[0], self.speed[1])

        if self.circle.left <= 0 or self.circle.right >= self.WIDTH:
            self.speed[0] = -self.speed[0]
        if self.circle.top <= 0 or self.circle.bottom >= self.HEIGHT:
            self.speed[1] = -self.speed[1]
        if abs(self.circle.x - self.player.x) < self.player.size[0] and abs(self.circle.y - self.player.y) < self.player.size[0]:
            self.speed[0] = -self.speed[0]
        # if self.circle.top <= self.player.top or self.circle.bottom >= self.player.bottom:
        #     self.speed[1] = -self.speed[1]

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.circle.center, self.radius)
