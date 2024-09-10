import pygame
import sys

class PlayerBullet(pygame.sprite.Sprite):

    size_x = 10
    size_y = 20
    speed = 5

    def __init__(self, screen, x, y):
        # super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        self.image = pygame.image.load('./asset/player_bullet.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.screen = screen
        # self.color = color
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
    
    def start(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.move_ip(0,-self.speed)
        
        # self.rect.clamp_ip(0,0,self.WIDTH, self.HEIGTH)


    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)
