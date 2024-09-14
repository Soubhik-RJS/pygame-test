import pygame
import sys

class Cloud(pygame.sprite.Sprite):

    size_x = 70
    size_y = 20
    speed = 2

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('./asset/cloud.png')

        # Set the initial image and position
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.x <= -70:
            self.kill()


    def draw(self):
        # Draw the current frame of the explosion
        self.screen.blit(self.image, self.rect)
