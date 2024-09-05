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

    set_level = 1

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver, final):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.win = False
        # self.color = self.BLACK
        self.gameOver = gameOver
        self.final = final
        self.Wall_Layout = []
        self.Block_Layout = []
        self.levels = []
        self.font_sm = pygame.font.SysFont(None, 30)

        # init levels
        for i in range(10):
            try:
                with open(f'levels/{i+1}.txt','r') as file:
                    self.levels.append(json.loads(file.read()))
            except Exception as e:
                print(e)
    
    def start(self):
        print('game scene start')
        for y, row in enumerate(self.levels[self.set_level-1]):
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
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.win:
                if self.next_btn.collidepoint(e.pos):
                    if not self.set_level == 10:
                        self.set_level += 1
                        self.run()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                self.ball.velocity = [-self.ball.speed, -self.ball.speed]

    def update(self):

        if self.ball.bottom >= self.HEIGTH:
            self.gameOver.run()
        
        self.player.update()
        self.Block_Layout = self.ball.update()

        # destory blocks
        # print(self.Block_Layout)
        # i = self.ball.colliderect(self.Block_Layout[0])
        # print(i)
        # if i >= 0:
        #     del self.Block_Layout[i]

    def draw(self):
        
        self.player.darw()
        self.ball.draw()
        
        for wall in self.Wall_Layout:
            wall.draw()
        for block in self.Block_Layout:
            block.draw()
        
        self.text_sm_screen(f"Level{self.set_level}",self.BLACK,self.WIDTH/2,20, True)
        # win
        if len(self.Block_Layout) <= 0:
            with open("save.txt", 'w') as file:
                file.write(str(self.set_level+1))
            if self.set_level == 10:
                self.final.run()
            else:
                self.win = True
                self.text_screen("WINNER WINNER CHICKEN DINNER",self.BLACK,self.WIDTH/2,self.HEIGTH/2,True)
                self.next_btn = self.draw_button("Next", self.BLACK, (self.WIDTH/2-75, self.HEIGTH/2+50, 150, 40))
                self.ball.velocity =[0,0]

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)

    def text_sm_screen(self,text, color, x, y, center=False):
        screen_text = self.font_sm.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)

    def draw_button(self, text, color, rect):
        button_rect = pygame.Rect(rect)
        pygame.draw.rect(self.screen, color, button_rect, border_radius=5)
        text_surface = self.font_sm.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(text_surface, text_rect)
        return button_rect