import pygame
import sys
from Scenes.Scene import Scene
from GameObject.Snake import Snake
from GameObject.Apple import Apple

class Game(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.color = self.BLACK
        self.gameOver = gameOver
    
    def start(self):
        self.point = 0
        print('game scene start',self.point)
        self.snake = Snake(self.screen,self.WIDTH, self.HEIGTH, self.GREEN, self.gameOver)
        self.apple = Apple(self.screen, self.WIDTH, self.HEIGTH, self.RED, self.snake)
    
    def event(self, e):
        self.snake.event(e)
        self.apple.event(e)

    def update(self):
        self.snake.update()
        self.point += self.apple.update()

        if self.snake.x < 0 or self.snake.x > self.WIDTH or self.snake.y < 0 or self.snake.y > self.HEIGTH:
            with open("save.txt", 'r') as f:
                try:
                    if self.point > int(f.read()):
                        with open("save.txt", 'w') as f:
                            f.write(str(self.point))
                except Exception as e:
                    print(e)
            self.gameOver.run()

    def draw(self):
        self.text_screen(f"Score: {self.point}",self.WHITE,5,5)
        self.snake.darw()
        self.apple.draw()

    def reset(self):
        self.__init__(self.screen,self.clock,self.fps,self.font,self.WIDTH,self.HEIGTH,self.gameOver)
    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)