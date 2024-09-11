import pygame
import sys
import pygame.locals
from Scenes.Scene import Scene

class Welcome(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, game_scene):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.game_scene = game_scene
        self.font_sm = pygame.font.SysFont(None, 30)
        self.start_btn_color = (0, 36, 107)
        self.level_btn_color = (80, 80, 80)

        # Add player image
        self.player_image = pygame.image.load('./asset/player.png')
        self.player_image = pygame.transform.scale(self.player_image, (50, 50)).convert_alpha()
        # Add background
        self.bg = pygame.image.load('./asset/background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGTH)).convert_alpha()
        self.bg_width, self.bg_height = self.bg.get_size()
        self.bg_speed = 2
        # Initial positions for the background (now using y-coordinates)
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
    
    def start(self):
        print('welcome scene start')
        with open('save.txt') as file:
            self.last_level = int(file.read())
    
    def event(self, e):
        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_SPACE:
        #         self.game_scene.run()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.collidepoint(e.pos):
                self.game_scene.set_level = 1
                self.game_scene.run()
            if self.continue_btn.collidepoint(e.pos):
                self.game_scene.set_level = self.last_level
                self.game_scene.run()
    
    def update(self):
        # Update the background position (moving down)
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        # Reset background position to create seamless loop
        if self.bg_y1 >= self.bg_height:
            self.bg_y1 = -self.bg_height
        if self.bg_y2 >= self.bg_height:
            self.bg_y2 = -self.bg_height

    def draw(self):
        self.screen.blit(self.bg, (0, self.bg_y1))
        self.screen.blit(self.bg, (0, self.bg_y2))
        self.screen.blit(self.player_image,(self.WIDTH/2-25,self.HEIGTH-100))

        self.text_screen("Star Fighters", self.WHITE, self.WIDTH/2, 100, True)
        # self.text_screen("enter space to start", self.WHITE, self.WIDTH/2, self.HEIGTH/2 + 20, True)
        self.start_btn = self.draw_button("Start", self.start_btn_color, (self.WIDTH/2-100, self.HEIGTH/2-30, 200, 50))
        self.continue_btn = self.draw_button("Continue", self.start_btn_color, (self.WIDTH/2-100, self.HEIGTH/2+30, 200, 50))

    def text_screen(self, text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x, y)) if center else [x, y]
        self.screen.blit(screen_text, text_rect)
    
    def draw_button(self, text, color, rect):
        button_rect = pygame.Rect(rect)
        pygame.draw.rect(self.screen, color, button_rect, border_radius=5)
        text_surface = self.font_sm.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
        self.screen.blit(text_surface, text_rect)
        return button_rect
