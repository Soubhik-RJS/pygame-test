import pygame
import sys
from Scenes.Scene import Scene

class Welcome(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, singleGame, multiGame):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.singleGame = singleGame
        self.multiGame = multiGame
        self.font_sm = pygame.font.SysFont(None, 30)
    
    def start(self):
        print('welcome scene start')
    
    def event(self, e):
        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_SPACE:
        #         self.game_scene.run()
        
        # Check if the button is clicked
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.button_single.collidepoint(e.pos):
                self.singleGame.run()
            if self.button_multi.collidepoint(e.pos):
                self.multiGame.run()

    def draw(self):
        self.text_screen("Play Table Tennis",self.BLACK,self.WIDTH/2,self.HEIGTH/2-40,True)
        # self.text_screen("enter space to start",self.BLACK,self.WIDTH/2,self.HEIGTH/2+20,True)
        self.button_single = self.draw_button("Single Player",self.BLACK, (self.WIDTH/2-100, self.HEIGTH/2, 200, 50))  # x, y, width, height
        self.button_multi = self.draw_button("Multi Player",self.BLACK, (self.WIDTH/2-100, self.HEIGTH/2+20+50, 200, 50))
    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)
    
    def draw_button(self, text, color, rect):
        button_rect = pygame.Rect(rect)
        pygame.draw.rect(self.screen, color, button_rect)
        text_surface = self.font_sm.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(text_surface, text_rect)
        return button_rect