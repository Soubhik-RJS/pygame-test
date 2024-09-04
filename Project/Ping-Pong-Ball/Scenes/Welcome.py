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
        self.level_btn_color = (80, 80, 80)
        self.ui = 'home'
        self.last_level = 1
        self.btn_level = [0,1,2,3,4,5,6,7,8,9]
    
    def start(self):
        print('welcome scene start')
        with open('save.txt') as file:
            self.last_level = int(file.read())
    
    def event(self, e):
        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_SPACE:
        #         self.game_scene.run()
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.ui == "home":
                if self.start_btn.collidepoint(e.pos):
                    self.game_scene.set_level = 1
                    self.game_scene.run()
                if self.continue_btn.collidepoint(e.pos):
                    self.game_scene.set_level = 2
                    self.game_scene.run()
                if self.level_btn.collidepoint(e.pos):
                    self.ui = "level"

            elif self.ui == 'level':
                if self.back_btn.collidepoint(e.pos):
                    self.ui = "home"
                for i in range(len(self.btn_level)):
                    if self.btn_level[i].collidepoint(e.pos):
                        # print(f"Btn {i+1} is clicked")
                        self.game_scene.set_level = i+1
                        self.game_scene.run()

    def draw(self):
        if self.ui == "home":
            self.text_screen("Welcome to Ping Pong Ball",self.BLACK,self.WIDTH/2,30,True)
            # self.text_screen("enter space to start",self.BLACK,self.WIDTH/2,self.HEIGTH/2+20,True)
            self.start_btn = self.draw_button("Start", self.start_btn_color, (self.WIDTH/2-100, self.HEIGTH/2-20-50, 200, 50))
            self.continue_btn = self.draw_button("Continue", self.start_btn_color, (self.WIDTH/2-100, self.HEIGTH/2, 200, 50))
            self.level_btn = self.draw_button("Levels", self.BLACK, (self.WIDTH/2-100, self.HEIGTH/2+20+50, 200, 50))
        elif self.ui == 'level':
            self.screen.fill(self.BLACK)
            self.text_screen("All Levels",self.WHITE,self.WIDTH/2,30,True)
            # self.text_screen("enter space to start",self.BLACK,self.WIDTH/2,self.HEIGTH/2+20,True)
            self.back_btn = self.draw_button("Back", self.RED, (10, 10, 70, 40))

            btn_color = []
            for i in range(10):
                if self.last_level >= i+1:
                    btn_color.append(self.start_btn_color)
                else:
                    btn_color.append(self.level_btn_color)


            # 1st row
            self.btn_level[0] = self.draw_button("1", btn_color[0], (self.WIDTH/2-(40+150+100), self.HEIGTH/2-50-20, 100, 100))
            self.btn_level[1] = self.draw_button("2", btn_color[1], (self.WIDTH/2-(20+150), self.HEIGTH/2-50-20, 100, 100))
            self.btn_level[2] = self.draw_button("3", btn_color[2], (self.WIDTH/2-50, self.HEIGTH/2-50-20, 100, 100))
            self.btn_level[3] = self.draw_button("4", btn_color[3], (self.WIDTH/2+(20+50), self.HEIGTH/2-50-20, 100, 100))
            self.btn_level[4] = self.draw_button("5", btn_color[4], (self.WIDTH/2+(40+150), self.HEIGTH/2-50-20, 100, 100))
            # 2nd row
            self.btn_level[5] = self.draw_button("6", btn_color[5], (self.WIDTH/2-(40+150+100), self.HEIGTH/2+50+20, 100, 100))
            self.btn_level[6] = self.draw_button("7", btn_color[6], (self.WIDTH/2-(20+150), self.HEIGTH/2+50+20, 100, 100))
            self.btn_level[7] = self.draw_button("8", btn_color[7], (self.WIDTH/2-50, self.HEIGTH/2+50+20, 100, 100))
            self.btn_level[8] = self.draw_button("9", btn_color[8], (self.WIDTH/2+(20+50), self.HEIGTH/2+50+20, 100, 100))
            self.btn_level[9] = self.draw_button("10", btn_color[9], (self.WIDTH/2+(40+150), self.HEIGTH/2+50+20, 100, 100))

    
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