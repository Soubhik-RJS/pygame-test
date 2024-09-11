import pygame
import sys
from GameObject.explosion import Explosion

class Enemy2(pygame.sprite.Sprite):

    size = 50
    speed = 5

    def __init__(self, screen, x, y, explosions, player):
        # super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        super().__init__()
        self.image = pygame.image.load('./asset/enemy_2.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

        self.health = 5

        self.screen = screen
        self.explosions = explosions
        self.player = player
        # self.color = color
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH

        self.p1 = self.rect.x-50
        self.p2 = self.rect.x+50
        self.p_shift = False

        # self.MOVE_EVENT = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.MOVE_EVENT, 4000)
    
    def start(self):
        pass
        
    def event(self, e):
        self.p_shift = True
        # self.p_shift = False if self.p_shift else True
        # if e.type == self.MOVE_EVENT:

    def update(self):
        if self.health <= 0:
            self.explosions.add(Explosion(self.screen, self.rect.x, self.rect.y))
            self.kill()
        # self.rect.clamp_ip(0,0,self.WIDTH, self.HEIGTH)

        if self.rect.x == self.player.rect.x:
            self.p_shift = False

        if self.p_shift:
            self.move_towards_target(self.player.rect.x, self.rect.y)
        


    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)

    def move_towards_target(self, target_x, target_y):
        dx = target_x - self.rect.x
        dy = target_y - self.rect.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < self.speed:
            return target_x, target_y

        ratio = self.speed / distance
        self.rect.x += dx * ratio
        self.rect.y += dy * ratio
        # return rect_x, rect_y