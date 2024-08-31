import pygame
import sys

class Snake(pygame.Rect):

    size = 30
    # speed = 5
    # velocity = [0,0] # [x,y]
    # snake_list = []
    # snake_length = 1

    def __init__(self, screen, WIDTH, HEIGTH, color, gameOver):
        super().__init__(WIDTH/2, HEIGTH/2, self.size, self.size)
        self.screen = screen
        self.color = color
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.gameOver = gameOver

        # game var of reset
        self.size = 30
        self.speed = 5
        self.velocity = [0,0]
        self.snake_list = []
        self.snake_length = 1
    
    def start(self):
        pass

    def reset(self):
        self.__init__(self.screen, self.WIDTH, self.HEIGTH, self.color, self.gameOver)

    def event(self,e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                if self.velocity[1] == 0:
                    self.velocity = [0,-self.speed]
            if e.key == pygame.K_s:
                if self.velocity[1] == 0:
                    self.velocity = [0,self.speed]
            if e.key == pygame.K_a:
                if self.velocity[0] == 0:
                    self.velocity = [-self.speed,0]
            if e.key == pygame.K_d:
                if self.velocity[0] == 0:
                    self.velocity = [self.speed,0]

    def update(self):
        self.move_ip(self.velocity)

        head = []
        head.append(self.x)
        head.append(self.y)
        self.snake_list.append(head)

        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]
        
        if head in self.snake_list[:-1]:
            self.gameOver.run()


    def darw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        for x,y in self.snake_list:
            pygame.draw.rect(self.screen, self.color, [x,y,self.size,self.size])
