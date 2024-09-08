import pygame
import sys

class Enemy(pygame.sprite.Sprite):

    size_x = 25
    size_y = 50
    
    def __init__(self, screen, x, y, image, speed):
        # super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        self.image = pygame.image.load(image)
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self.speed = speed
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        # self.color = color

    def update(self):
        self.rect.move_ip(-self.speed,0)
        # print(self.rect.x)

        # if self.rect.x == -50:
        #     self.rect.x = 800
    
    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)