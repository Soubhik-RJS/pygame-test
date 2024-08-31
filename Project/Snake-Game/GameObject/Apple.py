import pygame
import sys
import random

class Apple(pygame.Rect):
    
    def __init__(self, screen, WIDTH, HEIGTH, color, snake):
        super().__init__(WIDTH/2,HEIGTH/2+100,30,30)
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.color = color
        self.snake = snake
    
    def update(self):
        point = 0
        if self.colliderect(self.snake):
            self.x,self.y = random.randint(50, self.WIDTH-50),random.randint(50, self.HEIGTH-50)
            point = 1
            self.snake.snake_length += 5
        
        return point
        

    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self)