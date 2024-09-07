import pygame
import sys
from Scenes.Scene import Scene
from GameObject.Dino import Dino
from GameObject.Enemy import Enemy

class Game(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.gameOver = gameOver
        self.dino_image = "./asset/dinosaur.png"
        self.cactus_image = "./asset/cactus.png"
    
    def start(self):
        print('game scene start')
        self.dino = Dino(self.screen,self.WIDTH, self.HEIGTH, self.dino_image)
        self.enemy = Enemy(self.screen, self.WIDTH, self.HEIGTH/2, self.cactus_image)
    
    def update(self):
        self.dino.update()
        self.enemy.update()

        # if self.player.colliderect(self.enemy):
        #     self.gameOver.run()

    def draw(self):
        # self.text_screen("MyGame Started",self.BLACK,5,5)
        self.dino.darw()
        self.enemy.draw()
        pygame.draw.line(self.screen, self.BLACK, (0, (self.HEIGTH/2)+self.dino.size),(self.WIDTH, (self.HEIGTH/2)+self.dino.size),2)

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)