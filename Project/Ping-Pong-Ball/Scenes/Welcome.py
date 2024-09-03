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
        self.font_sm = pygame.font.SysFont(None, 30)
        self.start_btn_color = (30, 150, 0)
        self.ui = 'home'
    
    def start(self):
        print('welcome scene start')
    
    def event(self, e):
        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_SPACE:
        #         self.game_scene.run()
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.ui == "home":
                if self.start_btn.collidepoint(e.pos):
                    print("start")
                if self.level_btn.collidepoint(e.pos):
                    self.ui = "level"
            elif self.ui == 'level':
                if self.back_btn.collidepoint(e.pos):
                    self.ui = "home"

    def draw(self):
        if self.ui == "home":
            self.text_screen("Welcome to Ping Pong Ball",self.BLACK,self.WIDTH/2,self.HEIGTH/2-40,True)
            # self.text_screen("enter space to start",self.BLACK,self.WIDTH/2,self.HEIGTH/2+20,True)
            self.start_btn = self.draw_button("Start", self.start_btn_color, (self.WIDTH/2-100, self.HEIGTH/2, 200, 50))
            self.level_btn = self.draw_button("Level", self.BLACK, (self.WIDTH/2-100, self.HEIGTH/2+20+50, 200, 50))
        elif self.ui == 'level':
            self.screen.fill(self.BLACK)
            self.text_screen("All Levels",self.WHITE,self.WIDTH/2,self.HEIGTH/2-40,True)
            # self.text_screen("enter space to start",self.BLACK,self.WIDTH/2,self.HEIGTH/2+20,True)
            self.back_btn = self.draw_button("Back", self.RED, (self.WIDTH/2-100, self.HEIGTH/2, 200, 50))

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)

    def draw_button(self, text, color, rect):
        button_rect = pygame.Rect(rect)
        pygame.draw.rect(self.screen, color, button_rect, border_radius=5)
        text_surface = self.font_sm.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(text_surface, text_rect)
        return button_rect