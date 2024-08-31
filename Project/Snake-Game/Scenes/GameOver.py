import pygame
import sys
from Scenes.Scene import Scene

class GameOver(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.color = self.RED

    def set_load_scene(self, game):
        self.game = game
    
    def start(self):
        print("game over")

    def event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_KP_ENTER:
                self.game.run()
    
    def draw(self):
        self.text_screen("Game Over", self.WHITE, self.WIDTH/2, self.HEIGTH/2-20, True)
        self.text_screen("press enter to restart", self.WHITE, self.WIDTH/2, self.HEIGTH/2+20, True)

    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)