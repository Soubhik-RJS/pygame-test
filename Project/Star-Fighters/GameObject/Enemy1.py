import pygame
import sys
from GameObject.explosion import Explosion

class Enemy1(pygame.sprite.Sprite):

    size = 50
    # speed = 10

    def __init__(self, screen, x, y, explosions):
        # super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        super().__init__()
        self.image = pygame.image.load('./asset/enemy_1.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.health = 3

        self.screen = screen
        self.explosions = explosions
        # self.color = color
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
    
    def start(self):
        pass
        
    def event(self, e):
        pass

    def update(self):
        if self.health <= 0:
            self.explosions.add(Explosion(self.screen, self.rect.x, self.rect.y))
            self.kill()
        # self.rect.clamp_ip(0,0,self.WIDTH, self.HEIGTH)


    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)