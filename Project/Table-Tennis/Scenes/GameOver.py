import pygame
import sys
import json
from Scenes.Scene import Scene

class GameOver(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.color = self.RED
        self.screen_from = ""

    def set_load_scene(self, welcome, singleGame, multiGame):
        self.welcome = welcome
        self.singleGame = singleGame
        self.multiGame = multiGame
    
    def start(self):
        print("game over")
        with open("save.json", 'r') as file:
            self.save = json.loads(file.read())

    def event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_KP_ENTER:
                self.welcome.run()
    
    def draw(self):
        self.text_screen("Game Over", self.WHITE, self.WIDTH/2, self.HEIGTH/2-40, True)
        if self.screen_from == "singlegame":
            score = self.save["singlegame"]["score"]
            self.text_screen(f"Score: {self.singleGame.score} High Score: {score}", self.WHITE, self.WIDTH/2, self.HEIGTH/2, True)
        elif self.screen_from == "multigame":
            if self.multiGame.player_left_score == self.multiGame.player_right_score:
                win = "Match Draw"
            elif self.multiGame.player_left_score > self.multiGame.player_right_score:
                win = "Player Left Win"
            else:
                win = "Player Right Win"
            self.text_screen(f"Player Left Score: {self.multiGame.player_left_score} Player Right Score: {self.multiGame.player_right_score} {win}", self.WHITE, self.WIDTH/2, self.HEIGTH/2, True)
        self.text_screen("press enter to restart", self.WHITE, self.WIDTH/2, self.HEIGTH/2+40, True)

    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)