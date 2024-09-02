import pygame
import sys
import json
from Scenes.Scene import Scene
from GameObject.Player_Left import Player_Left
from GameObject.Player_Right import Player_Right
from GameObject.Ball import Ball

class SingleGame(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.gameOver = gameOver
        self.speed = 10
        self.score = 0
    
    def start(self):
        print('game scene start')
        self.player_left = Player_Left(self.screen,self.WIDTH, self.HEIGTH, self.BLACK)
        self.player_right = Player_Right(self.screen,self.WIDTH, self.HEIGTH, self.BLACK)
        self.ball = Ball(self.screen, self.WIDTH, self.HEIGTH, self.BLACK,self.player_left, self.player_right)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.ball.velocity = self.ball.speed
            self.player_left.move_ip(0,-self.speed)
            self.player_right.move_ip(0,-self.speed)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.ball.velocity = self.ball.speed
            self.player_left.move_ip(0,self.speed)
            self.player_right.move_ip(0,self.speed)
        
        if self.ball.left <= 0 or self.ball.right >= self.WIDTH:
            # self.ball.x,self.ball.y = self.WIDTH/2-15,self.HEIGTH/2-15
            # self.ball.velocity = [0,0]
            try:
                with open('save.json', 'r') as file:
                    save = file.read()
                    save = json.loads(save)
                    if int(self.score) > save["singlegame"]["score"]:
                        with open("save.json",'w') as file:
                            save["singlegame"]["score"] = int(self.score)
                            file.write(json.dumps(save))
            except Exception as e:
                print(e)
            self.gameOver.screen_from ="singlegame"
            self.gameOver.run()
    
        
        self.player_left.update()
        self.player_right.update()
        self.score += self.ball.update()['score']
        

    def draw(self):
        self.text_screen(f"Score: {self.score}",self.BLACK,self.WIDTH/2,30,True)
        self.player_left.darw()
        self.player_right.darw()
        self.ball.draw()

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)