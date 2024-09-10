import pygame
import sys
from Scenes.Scene import Scene
from GameObject.Player import Player
from GameObject.Enemy import Enemy
from GameObject.player_bullet import PlayerBullet
from GameObject.enemy_explosion import EnemyExplosion

class Game(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.gameOver = gameOver

        # Add background
        self.bg = pygame.image.load('./asset/background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.WIDTH, self.HEIGTH)).convert_alpha()
        self.bg_width, self.bg_height = self.bg.get_size()
        self.bg_speed = 2
        # Initial positions for the background (now using y-coordinates)
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height
    
    def start(self):
        print('game scene start')
        self.player = Player(self.screen,self.WIDTH, self.HEIGTH)
        self.enemy = Enemy(self.screen, self.WIDTH, self.HEIGTH, self.BLACK)
        self.enemyExplosion = EnemyExplosion(self.screen,self.WIDTH/2,self.HEIGTH/2)
        self.playerBullets = []
    
    def event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                self.playerBullets.append(PlayerBullet(self.screen,self.player.rect.x+self.player.size/2-5,self.player.rect.y))

    def update(self):

        # self.playerBullet.rect.x = self.player.rect.x+self.player.size/2-5
        # self.playerBullet.rect.y = self.player.rect.y-50

        # Update the background position (moving down)
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        # Reset background position to create seamless loop
        if self.bg_y1 >= self.bg_height:
            self.bg_y1 = -self.bg_height
        if self.bg_y2 >= self.bg_height:
            self.bg_y2 = -self.bg_height

        self.player.update()
        self.enemyExplosion.update()


        i = 0
        while i < len(self.playerBullets):
            self.playerBullets[i].update()
            if self.playerBullets[i].rect.y <= 0:
                del self.playerBullets[i]
            else:
                i += 1

        # if self.player.colliderect(self.enemy):
        #     self.gameOver.run()

    def draw(self):
        self.screen.blit(self.bg, (0, self.bg_y1))
        self.screen.blit(self.bg, (0, self.bg_y2))
        # self.text_screen("MyGame Started",self.BLACK,5,5)

        self.player.draw()
        self.enemyExplosion.draw()

        for playerBullet in self.playerBullets:
            playerBullet.update()
            playerBullet.draw()
        # self.enemy.draw()

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)