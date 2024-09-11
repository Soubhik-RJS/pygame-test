import pygame
import sys
from GameObject.collocation import Collocation

class EnemyBullet(pygame.sprite.Sprite):

    size_x = 10
    size_y = 20
    speed = 5

    def __init__(self, screen, x, y, player, collocations):
        # super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        super().__init__()
        self.image = pygame.image.load('./asset/enemy_bullet.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.screen = screen
        self.player = player
        self.collocations = collocations
        # self.color = color
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
    
    def start(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.move_ip(0,self.speed)
        if self.rect.y >= 600:
            self.kill()
            # return True
        
        offset_x = self.player.rect.x - self.rect.x
        offset_y = self.player.rect.y - self.rect.y
        if self.mask.overlap(self.player.mask, (offset_x, offset_y)):
            self.player.health -= 1
            self.collocations.add(Collocation(self.screen, self.rect.x-3, self.rect.y-10))
            self.kill()
            # return True
        
        # return False
        
        # self.rect.clamp_ip(0,0,self.WIDTH, self.HEIGTH)


    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)
