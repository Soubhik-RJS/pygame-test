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
    
    def event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
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

        self.text_screen("Star Fighters", self.WHITE, self.WIDTH/2, self.HEIGTH/2 - 20, True)
        self.text_screen("enter space to start", self.WHITE, self.WIDTH/2, self.HEIGTH/2 + 20, True)

    def text_screen(self, text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x, y)) if center else [x, y]
        self.screen.blit(screen_text, text_rect)
