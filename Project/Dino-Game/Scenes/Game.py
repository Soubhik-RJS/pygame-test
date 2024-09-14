import pygame
import sys
import random
from Scenes.Scene import Scene
from GameObject.Dino import Dino
from GameObject.Cactus import Cactus1
from GameObject.Cactus import Cactus2
from GameObject.Cactus import Cactus3
from GameObject.Cactus import Cactus4
from GameObject.Cactus import Cactus5
from GameObject.Dino_bird import Dinobird
from GameObject.Cloud import Cloud

class Game(Scene):

    def __init__(self, screen, clock, fps, font, WIDTH, HEIGTH, gameOver):
        super().__init__(screen, clock, fps)
        self.font = font
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        # self.color = self.BLACK
        self.gameOver = gameOver
        self.welcome = True
        # self.dino_image = "./asset/dinosaur.png"
        # self.cactus_image = "./asset/backup/cactus1.png"

        self.start_image = pygame.image.load("./asset/start.png")
        self.start_image = pygame.transform.scale(self.start_image, (55, 55))

        self.ground = pygame.image.load("./asset/ground.png")
        self.ground = pygame.transform.scale(self.ground, (self.WIDTH, 20))
        self.ground_width, self.ground_height = self.ground.get_size()

        self.game_over_image = pygame.image.load("./asset/game_over.png")
        self.game_over_image = pygame.transform.scale(self.game_over_image, (250, 20))
        
        self.restart_image = pygame.image.load("./asset/restart.png")
        self.restart_image = pygame.transform.scale(self.restart_image, (30, 30))
    
    def start(self):
        print('game scene start')
        self.speed = 5
        self.dino = Dino(self.screen,self.WIDTH, self.HEIGTH)
        self.time = 2000
        self.isstart = False
        self.game_over = False
        self.clock_time = 0
        # self.bg_speed = 2
        self.bg_x1 = 0
        self.bg_x2 = self.ground_width

        self.enemys = pygame.sprite.Group()
        self.cloud = pygame.sprite.Group()

        self.CLOCK_EVENT = pygame.USEREVENT + 1
        self.SPAWN_EVENT = pygame.USEREVENT + 2
        self.CLOUD_SPAWN_EVENT = pygame.USEREVENT + 3
        pygame.time.set_timer(self.CLOCK_EVENT, 100)
        pygame.time.set_timer(self.SPAWN_EVENT, self.time)
        pygame.time.set_timer(self.CLOUD_SPAWN_EVENT, 3500)
        # self.enemy = Enemy(self.screen, self.WIDTH, self.HEIGTH/2, self.cactus_image, self.speed)
    
    def event(self, e):
        if e.type == self.CLOCK_EVENT:
            self.clock_time+=1
        if e.type == self.CLOUD_SPAWN_EVENT:
            self.cloud.add(Cloud(self.screen, self.WIDTH, random.randint(100, self.HEIGTH/2-100)))

        if e.type == self.SPAWN_EVENT:
            i = random.randint(1,6)
            if i == 1:
                self.enemys.add(Cactus3(self.screen, self.WIDTH, self.HEIGTH/2, self.speed))
            elif i == 2:
                self.enemys.add(Cactus4(self.screen, self.WIDTH, self.HEIGTH/2, self.speed))
            elif i == 3:
                self.enemys.add(Cactus1(self.screen, self.WIDTH, self.HEIGTH/2, self.speed))
            elif i == 4:
                self.enemys.add(Cactus2(self.screen, self.WIDTH, self.HEIGTH/2, self.speed))
            elif i == 5:
                self.enemys.add(Cactus5(self.screen, self.WIDTH, self.HEIGTH/2, self.speed))
            else:
                self.enemys.add(Dinobird(self.screen, self.WIDTH, self.HEIGTH/2, self.speed))

            # self.enemys.add(Dinobird(self.screen, self.WIDTH, self.HEIGTH/2, self.speed))

            # self.cactus.append(Enemy(self.screen, self.WIDTH, self.HEIGTH/2, self.cactus_image, self.speed))
            # self.speed += 1
            # if self.time > 50:
            #     self.time -= 50
            # pygame.time.set_timer(self.SPAWN_EVENT, self.time)
            # print(self.speed, self.time)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_KP_ENTER:
                if self.game_over:
                    self.run()
                elif self.welcome:
                    self.welcome = False

    def update(self):

        if not self.game_over and not self.welcome:

            self.bg_x1 -= self.speed
            self.bg_x2 -= self.speed

            if self.bg_x1 <= -self.ground_width:
                self.bg_x1 = self.ground_width
            if self.bg_x2 <= -self.ground_width:
                self.bg_x2 = self.ground_width

            self.dino.update()
            self.enemys.update()
            self.cloud.update()

            for enemy in self.enemys:
                offset_x = self.dino.rect.x - enemy.rect.x
                offset_y = self.dino.rect.y - enemy.rect.y
                if enemy.mask.overlap(self.dino.mask, (offset_x, offset_y)):
                    self.dino.image = pygame.transform.scale(self.dino.frames[5], (self.dino.size, self.dino.size))
                    self.game_over = True
                    pygame.time.set_timer(self.CLOCK_EVENT, 0)
                    pygame.time.set_timer(self.CLOUD_SPAWN_EVENT, 0)
                    pygame.time.set_timer(self.SPAWN_EVENT, 0)

            # i = 0
            # while i < len(self.cactus):
            #     self.cactus[i].update()
            #     if self.cactus[i].rect.x <= -50:
            #         del self.cactus[i]
            #     else:
            #         i += 1
            
            # if self.dino.rect.collidelist(self.cactus) >= 0:
            #     # print('game over')
            #     self.game_over = True
            #     pygame.time.set_timer(self.CLOCK_EVENT, 0)

        # if self.player.colliderect(self.enemy):
        #     self.gameOver.run()

    def draw(self):
        # self.screen.blit(self.ground, (0, (self.HEIGTH/2)+self.dino.size-20))
        self.screen.blit(self.ground, (self.bg_x1, (self.HEIGTH/2)+self.dino.size-20))
        self.screen.blit(self.ground, (self.bg_x2, (self.HEIGTH/2)+self.dino.size-20))
        if not self.welcome:
            self.text_screen(f"{self.clock_time}",self.BLACK,5,5)
            self.dino.draw()
            self.enemys.draw(self.screen)
            self.cloud.draw(self.screen)
        else:
            self.screen.blit(self.start_image, (self.dino.rect.x, self.dino.rect.y))
        # for enemy in self.cactus:
        #     enemy.draw()
        # pygame.draw.line(self.screen, self.BLACK, (0, (self.HEIGTH/2)+self.dino.size),(self.WIDTH, (self.HEIGTH/2)+self.dino.size),2)

        if self.game_over:
            # self.text_screen("Game Over",self.BLACK, self.WIDTH/2, self.HEIGTH/2, True)
            self.screen.blit(self.game_over_image, (self.WIDTH/2-250/2, self.HEIGTH/2-40))
            self.screen.blit(self.restart_image, (self.WIDTH/2-30/2, self.HEIGTH/2))

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)