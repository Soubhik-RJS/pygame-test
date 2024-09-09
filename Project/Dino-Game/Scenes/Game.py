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
        self.cactus_image = "./asset/cactus1.png"
    
    def start(self):
        print('game scene start')
        self.speed = 5
        self.dino = Dino(self.screen,self.WIDTH, self.HEIGTH, self.dino_image)
        self.cactus = []
        self.time = 2000
        self.isstart = False
        self.game_over = False
        self.clock_time = 0

        self.CLOCK_EVENT = pygame.USEREVENT + 1
        self.SPAWN_EVENT = pygame.USEREVENT + 2
        pygame.time.set_timer(self.CLOCK_EVENT, 100)
        pygame.time.set_timer(self.SPAWN_EVENT, self.time)
        # self.enemy = Enemy(self.screen, self.WIDTH, self.HEIGTH/2, self.cactus_image, self.speed)
    
    def event(self, e):
        if e.type == self.CLOCK_EVENT:
            self.clock_time+=1

        if e.type == self.SPAWN_EVENT:
                self.cactus.append(Enemy(self.screen, self.WIDTH, self.HEIGTH/2, self.cactus_image, self.speed))
                # self.speed += 1
                # if self.time > 50:
                #     self.time -= 50
                # pygame.time.set_timer(self.SPAWN_EVENT, self.time)
                # print(self.speed, self.time)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_KP_ENTER:
                self.run()

    def update(self):
        if not self.game_over:
            self.dino.update()
            i = 0
            while i < len(self.cactus):
                self.cactus[i].update()
                if self.cactus[i].rect.x <= -50:
                    del self.cactus[i]
                else:
                    i += 1
            
            if self.dino.rect.collidelist(self.cactus) >= 0:
                # print('game over')
                self.game_over = True
                pygame.time.set_timer(self.CLOCK_EVENT, 0)

        # if self.player.colliderect(self.enemy):
        #     self.gameOver.run()

    def draw(self):
        self.text_screen(f"{self.clock_time}",self.BLACK,5,5)
        self.dino.draw()
        for enemy in self.cactus:
            enemy.draw()
        pygame.draw.line(self.screen, self.BLACK, (0, (self.HEIGTH/2)+self.dino.size),(self.WIDTH, (self.HEIGTH/2)+self.dino.size),2)

        if self.game_over:
            self.text_screen("Game Over",self.BLACK, self.WIDTH/2, self.HEIGTH/2, True)

    
    def text_screen(self,text, color, x, y, center=False):
        screen_text = self.font.render(text, True, color)
        text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
        self.screen.blit(screen_text, text_rect)