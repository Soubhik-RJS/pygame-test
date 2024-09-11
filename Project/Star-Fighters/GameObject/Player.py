import pygame
import sys

class Player(pygame.sprite.Sprite):

    size = 50
    speed = 10

    def __init__(self, screen, WIDTH, HEIGTH):
        # super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        super().__init__()
        self.image = pygame.image.load('./asset/player.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH/2-self.size/2, HEIGTH-100)
        self.mask = pygame.mask.from_surface(self.image)

        self.max_health = 10
        self.health = 10

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
        self.draw_health_bar(self.screen, self.rect.x-self.size/2, self.rect.y+self.size+20, 100, 10, self.health, self.max_health)

    def draw_health_bar(self, surface, x, y, width, height, current_health, max_health):
        # Calculate health ratio
        health_ratio = current_health / max_health
        
        # Background bar (gray)
        pygame.draw.rect(surface, (128, 128, 128), (x, y, width, height))
        
        # Health bar (green)
        pygame.draw.rect(surface, (0, 255, 0), (x, y, width * health_ratio, height))
        
        # Optional: Draw a border around the health bar
        pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 2)

