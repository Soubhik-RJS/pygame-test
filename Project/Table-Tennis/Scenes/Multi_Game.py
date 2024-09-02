import pygame
import sys
from Scenes.Scene import Scene
from GameObject.Player_Left import Player_Left
from GameObject.Player_Right import Player_Right
from GameObject.Ball import Ball

class MultiGame(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.gameOver = gameOver
        self.speed = 10
    
    def start(self):
        self.player_left_score = 0
        self.player_right_score = 0
        print('game scene start')
        self.player_left = Player_Left(self.screen,self.WIDTH, self.HEIGTH, self.BLACK)
        self.player_right = Player_Right(self.screen,self.WIDTH, self.HEIGTH, self.BLACK)
        self.ball = Ball(self.screen, self.WIDTH, self.HEIGTH, self.BLACK,self.player_left, self.player_right)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.ball.velocity = self.ball.speed
            self.player_left.move_ip(0,-self.speed)
        if keys[pygame.K_s]:
            self.ball.velocity = self.ball.speed
            self.player_left.move_ip(0,self.speed)
        
        if keys[pygame.K_UP]:
            self.ball.velocity = self.ball.speed
            self.player_right.move_ip(0,-self.speed)
        if keys[pygame.K_DOWN]:
            self.ball.velocity = self.ball.speed
            self.player_right.move_ip(0,self.speed)
        
        if self.ball.left <= 0 or self.ball.right >= self.WIDTH:
            # self.ball.x,self.ball.y = self.WIDTH/2-15,self.HEIGTH/2-15
            # self.ball.velocity = [0,0]
            self.gameOver.screen_from ="multigame"
            self.gameOver.run()

    
        
        self.player_left.update()
        self.player_right.update()
        ball = self.ball.update()

        if ball["name"] == "right":
            self.player_right_score += ball["score"]
        elif ball["name"] == "left":
            self.player_left_score += ball["score"]
        


        # if self.player.colliderect(self.enemy):
        #     self.gameOver.run()

    def draw(self):
        self.text_screen(f"Score: {self.player_left_score}",self.BLACK,5,5)
        self.text_screen(f"Score: {self.player_right_score}",self.BLACK,self.WIDTH-150,5)
        self.player_left.darw()
        self.player_right.darw()
        self.ball.draw()

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)