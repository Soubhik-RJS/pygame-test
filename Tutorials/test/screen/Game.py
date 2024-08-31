import pygame
import sys
from Scene import Scene
from GameObject.Player import Player

class Game(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
    
    def start(self):
        print('game scene start')
        self.player = Player(self.screen,self.WIDTH, self.HEIGTH, self.RED)
    
    def update(self):
        self.player.update()

    def draw(self):
        self.text_screen("MyGame Started",self.GREEN,5,5)
        self.player.darw()

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)