import pygame
import sys
from Scenes.Scene import Scene
from GameObject.Player import Player
from GameObject.Enemy import Enemy
from GameObject.Wall import Wall

# Level Map (W = Wall, P = Player)
level_map = [
    "W        W         W",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "W                  W",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "                    ",
    "W        W         W",
]

class Game(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.gameOver = gameOver
        self.Level_Layout = []
    
    def start(self):
        print('game scene start')
        for y, row in enumerate(level_map):
            for x, tile in enumerate(row):
                if tile == 'W':
                    self.Level_Layout.append(Wall(self.screen, x, y, self.BLUE))
        self.player = Player(self.screen,self.WIDTH, self.HEIGTH, self.RED)
        self.enemy = Enemy(self.screen, self.WIDTH, self.HEIGTH, self.BLACK)
    
    def update(self):
        self.player.update()

        if self.player.colliderect(self.enemy):
            self.gameOver.run()

    def draw(self):
        self.text_screen("MyGame Started",self.BLACK,5,5)
        self.player.darw()
        self.enemy.draw()
        
        for wall in self.Level_Layout:
            wall.draw()

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)