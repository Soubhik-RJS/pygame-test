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
        self.font = pygame.font.SysFont(None, 40)

        self.eats = 0
        self.big = False
        self.big_color = (255, 132, 0)
        self.time = 10

        # Define a custom event
        self.CLOCK_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.CLOCK_EVENT, 1000)
    
    def event(self,e):
        if self.big:
            if e.type == self.CLOCK_EVENT:
                self.time -= 1

    def update(self):
        point = 0
        if self.colliderect(self.snake):
            self.x,self.y = random.randint(50, self.WIDTH-50),random.randint(50, self.HEIGTH-50)
            if self.big:
                point = 50
                self.big = False
                self.time = 10
            else:
                point = 10
                self.eats += 1
            self.snake.snake_length += 5
        
        if self.eats == 10:
            self.eats = 0
            self.big = True
        
        if self.time <= 0:
            self.big = False
            self.time = 10
        
        return point
        

    
    def draw(self):
        if self.big:
            self.text_screen(f"Time: {self.time}",(255, 255, 255),self.WIDTH-120,5)
            pygame.draw.rect(self.screen, self.big_color, (self.x,self.y,60,60))
        else:
            pygame.draw.rect(self.screen, self.color, self)

    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)