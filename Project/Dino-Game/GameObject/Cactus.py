import pygame
import sys

class Cactus1(pygame.sprite.Sprite):

    size_x = 70
    size_y = 50
    
    def __init__(self, screen, x, y, speed):
        # super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        super().__init__()
        self.image = pygame.image.load('./asset/cactus/1.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.speed = speed
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        # self.color = color

    def update(self):
        self.rect.move_ip(-self.speed,0)

        if self.rect.x <= -70:
            self.kill()

        # print(self.rect.x)

        # if self.rect.x == -50:
        #     self.rect.x = 800
    
    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)

class Cactus2(pygame.sprite.Sprite):

    size_x = 70
    size_y = 50
    
    def __init__(self, screen, x, y, speed):
        # super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        super().__init__()
        self.image = pygame.image.load('./asset/cactus/2.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.speed = speed
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        # self.color = color

    def update(self):
        self.rect.move_ip(-self.speed,0)

        if self.rect.x <= -70:
            self.kill()

        # print(self.rect.x)

        # if self.rect.x == -50:
        #     self.rect.x = 800
    
    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)

class Cactus3(pygame.sprite.Sprite):

    size_x = 25
    size_y = 50
    
    def __init__(self, screen, x, y, speed):
        # super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        super().__init__()
        self.image = pygame.image.load('./asset/cactus/3.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.speed = speed
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        # self.color = color

    def update(self):
        self.rect.move_ip(-self.speed,0)

        if self.rect.x <= -25:
            self.kill()

        # print(self.rect.x)

        # if self.rect.x == -50:
        #     self.rect.x = 800
    
    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)

class Cactus4(pygame.sprite.Sprite):

    size_x = 50
    size_y = 50
    
    def __init__(self, screen, x, y, speed):
        # super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        super().__init__()
        self.image = pygame.image.load('./asset/cactus/4.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.speed = speed
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        # self.color = color

    def update(self):
        self.rect.move_ip(-self.speed,0)

        if self.rect.x <= -50:
            self.kill()

        # print(self.rect.x)

        # if self.rect.x == -50:
        #     self.rect.x = 800
    
    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)

class Cactus5(pygame.sprite.Sprite):

    size_x = 80
    size_y = 50
    
    def __init__(self, screen, x, y, speed):
        # super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        super().__init__()
        self.image = pygame.image.load('./asset/cactus/5.png')
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        self.speed = speed
        # self.WIDTH = WIDTH
        # self.HEIGTH = HEIGTH
        # self.color = color

    def update(self):
        self.rect.move_ip(-self.speed,0)

        if self.rect.x <= -100:
            self.kill()

        # print(self.rect.x)

        # if self.rect.x == -50:
        #     self.rect.x = 800
    
    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)