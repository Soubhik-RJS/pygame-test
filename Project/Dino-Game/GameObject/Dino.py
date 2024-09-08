import pygame
import sys

class Dino(pygame.sprite.Sprite):

    size = 50
    speed = 10
    vel = 5

    def __init__(self, screen, WIDTH, HEIGTH, image):
        self.image = pygame.image.load(image)
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, HEIGTH//2)
        self.screen = screen
        # self.color = color
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH

        self.isJump = False
        self.jumpCount = self.speed
    
    def start(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.rect.move_ip(0,-self.speed)
        # if keys[pygame.K_s]:
        #     self.rect.move_ip(0,self.speed)
        # if keys[pygame.K_a]:
        #     self.rect.move_ip(-self.speed,0)
        # if keys[pygame.K_d]:
        #     self.rect.move_ip(self.speed,0)
        

        if not self.isJump: 
            # if keys[pygame.K_UP] and player_y > vel:
            #     player_y -= vel

            # if keys[pygame.K_DOWN] and player_y < 500 - height - vel:
            #     player_y += vel

            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            # print(self.rect.y)
            if self.jumpCount >= -self.speed:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.2
                self.jumpCount -= 0.5
            else: 
                self.jumpCount = self.speed
                self.isJump = False
            
        self.rect.clamp_ip(0,0,self.WIDTH, self.HEIGTH)


    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)
