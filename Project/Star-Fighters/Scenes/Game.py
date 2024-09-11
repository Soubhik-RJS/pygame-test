import pygame
import sys
from Scenes.Scene import Scene
from GameObject.Player import Player
from GameObject.Enemy1 import Enemy1
from GameObject.player_bullet import PlayerBullet
from GameObject.enemy_bullet import EnemyBullet
from GameObject.explosion import Explosion
from GameObject.collocation import Collocation

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

        self.ENEMY_BULLET_EVENT = pygame.USEREVENT + 1
    
    def start(self):
        print('game scene start')
        self.player = Player(self.screen,self.WIDTH, self.HEIGTH)
        # self.enemyExplosion = Explosion(self.screen,self.WIDTH/2,self.HEIGTH/2)
        # self.playerBullets = []
        pygame.time.set_timer(self.ENEMY_BULLET_EVENT, 2000)

        self.enemys = pygame.sprite.Group()
        self.playerBullets = pygame.sprite.Group()
        self.enemyBullets = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.collocations = pygame.sprite.Group()

        self.enemys.add(Enemy1(self.screen, 50, 50, self.explosions))
        self.enemys.add(Enemy1(self.screen, self.WIDTH-100, 50, self.explosions))

    def event(self, e):
        if e.type == self.ENEMY_BULLET_EVENT:
            for enemy in self.enemys:
                self.enemyBullets.add(EnemyBullet(self.screen,enemy.rect.x+enemy.size/2-5, enemy.rect.y, self.player, self.collocations))
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                self.playerBullets.add(PlayerBullet(self.screen,self.player.rect.x+self.player.size/2-5,self.player.rect.y, self.enemys, self.collocations))

    def update(self):

        # Update the background position (moving down)
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        # Reset background position to create seamless loop
        if self.bg_y1 >= self.bg_height:
            self.bg_y1 = -self.bg_height
        if self.bg_y2 >= self.bg_height:
            self.bg_y2 = -self.bg_height

        self.player.update()
        self.enemys.update()

        self.playerBullets.update()
        # for bullet in self.playerBullets:
        #     result = bullet.update()
        #     if result:
        #         # self.explosions.add(Explosion(self.screen, bullet.rect.x-25, bullet.rect.y-25))
        #         self.collocations.add(Collocation(self.screen, bullet.rect.x-3, bullet.rect.y-10))
        #         bullet.kill()

        self.enemyBullets.update()

        self.explosions.update()
        self.collocations.update()
        
        # if self.player.colliderect(self.enemy):
        #     self.gameOver.run()

    def draw(self):
        # background scrolling fx
        self.screen.blit(self.bg, (0, self.bg_y1))
        self.screen.blit(self.bg, (0, self.bg_y2))
        # self.text_screen("MyGame Started",self.BLACK,5,5)

        self.playerBullets.draw(self.screen)
        self.enemyBullets.draw(self.screen)

        self.player.draw()
        self.enemys.draw(self.screen)

        # self.enemyExplosion.draw()

        self.explosions.draw(self.screen)
        self.collocations.draw(self.screen)

        if len(self.enemys) <= 0:
            self.text_screen("WIN",self.WHITE,self.WIDTH/2, self.HEIGTH/2, True)

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)