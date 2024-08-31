import pygame
import sys
from Scenes.Scene import Scene

class Welcome(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, game_scene):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.game_scene = game_scene
    
    def start(self):
        print('welcome scene start')
    
    def event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                self.game_scene.run()

    def draw(self):
        self.text_screen("Welcome to MyGame",self.BLACK,self.WIDTH/2,self.HEIGTH/2-20,True)
        self.text_screen("enter space to start",self.BLACK,self.WIDTH/2,self.HEIGTH/2+20,True)

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)