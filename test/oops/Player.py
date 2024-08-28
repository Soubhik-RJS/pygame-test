import pygame
import sys

class Player (pygame.Rect):
    speed = 10
    color = (255,0,0)
    def __init__(self,screen,width, height):
        super().__init__(width // 2, height // 2, 50, 50)
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = screen

    def start(self, enemy_list):
        print("start")
        self.enemy_list = enemy_list
        # self.image = pygame.image.load("asset/player.png")
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))
    
    def update(self):
        keys = pygame.key.get_pressed()
    
        # Move player
        if keys[pygame.K_a]:
            self.move_ip(-self.speed, 0)
            # also works
            # self.x -= self.speed
        if keys[pygame.K_d]:
            self.move_ip(self.speed, 0)
        if keys[pygame.K_w]:
            self.move_ip(0, -self.speed)
        if keys[pygame.K_s]:
            self.move_ip(0, self.speed)

        # prevent to out of screen
        # print(self.width)
        self.clamp_ip(0,0,self.WIDTH,self.HEIGHT)

        if self.collidelist(self.enemy_list) > -1:
            print('done')
        

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self, border_radius=999)
        pygame.draw.rect(self.screen, self.color, self)
        # self.screen.blit(self.image, (self.x,self.y))
