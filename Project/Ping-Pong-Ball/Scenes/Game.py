import pygame
import sys
import json
from Scenes.Scene import Scene
from GameObject.Player import Player
from GameObject.Ball import Ball
from GameObject.Wall import Wall
from GameObject.Block import Block

# Level Map (W = Wall, P = Player)
# level_map = [
#     "BRBGB B B              ",
#     "                       ",
#     "B B BRBUB              ",
#     "                       ",
#     "    B                  ",
#     "                       ",
#     "                       ",
#     "                       ",
#     "                       ",
#     "                       ",
#     "                       ",
#     "                       ",
#     "                       ",
#     "                       ",
#     "           P           ",
# ]

class Game(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.gameOver = gameOver
        self.Wall_Layout = []
        self.Block_Layout = []
        # self.level_map = []

        # init levels
        try:
            with open('levels/2.txt','r') as file:
                self.level_map = json.loads(file.read())
        except Exception as e:
            print(e)
    
    def start(self):
        print('game scene start')
        for y, row in enumerate(self.level_map):
            for x, tile in enumerate(row):
                if tile == 'W':
                    self.Wall_Layout.append(Wall(self.screen, x, y, (128, 44, 3)))
                if tile == 'R':
                    self.Block_Layout.append(Block(self.screen, x, y, self.RED))
                if tile == 'G':
                    self.Block_Layout.append(Block(self.screen, x, y, self.GREEN))
                if tile == 'B':
                    self.Block_Layout.append(Block(self.screen, x, y, self.BLUE))
        self.player = Player(self.screen,self.WIDTH, self.HEIGTH, self.RED)
        self.ball = Ball(self.screen, self.WIDTH, self.HEIGTH, self.BLACK, self.Block_Layout, self.Wall_Layout, self.player)
    
    def event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                self.gameOver.run()

    def update(self):

        if self.ball.bottom >= self.HEIGTH:
            self.gameOver.run()
        
        self.player.update()
        i = self.ball.update()
        # destory blocks
        if i >= 0:
            del self.Block_Layout[i]

    def draw(self):
        # self.text_screen("MyGame Started",self.BLACK,5,5)
        
        self.player.darw()
        self.ball.draw()
        
        for wall in self.Wall_Layout:
            wall.draw()
        for block in self.Block_Layout:
            block.draw()
        
        # win
        if len(self.Block_Layout) <= 0:
            self.text_screen("Game Winner",self.BLACK,self.WIDTH/2,self.HEIGTH/2,True)

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)