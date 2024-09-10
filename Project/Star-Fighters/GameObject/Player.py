import pygame
import sys

class Player(pygame.sprite.Sprite):

    size = 50
    speed = 10

    def __init__(self, screen, WIDTH, HEIGTH):
        # super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        self.image = pygame.image.load('./asset/player.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH/2-self.size/2, HEIGTH-100)

        self.screen = screen
        # self.color = color
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
    
    def start(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.rect.move_ip(0,-self.speed)
        # if keys[pygame.K_s]:
        #     self.rect.move_ip(0,self.speed)
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.speed,0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed,0)
        
        self.rect.clamp_ip(0,0,self.WIDTH, self.HEIGTH)


    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)
