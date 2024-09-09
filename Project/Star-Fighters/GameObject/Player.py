import pygame
import sys

class Player(pygame.Rect):

    size = 30
    speed = 10

    def __init__(self, screen, WIDTH, HEIGTH, color):
        super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        self.screen = screen
        self.color = color
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
    
    def start(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move_ip(0,-self.speed)
        if keys[pygame.K_s]:
            self.move_ip(0,self.speed)
        if keys[pygame.K_a]:
            self.move_ip(-self.speed,0)
        if keys[pygame.K_d]:
            self.move_ip(self.speed,0)
        
        self.clamp_ip(0,0,self.WIDTH, self.HEIGTH)


    def darw(self):
        pygame.draw.rect(self.screen, self.color, self)
