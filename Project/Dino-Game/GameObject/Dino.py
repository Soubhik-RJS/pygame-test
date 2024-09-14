import pygame
import sys

class Dino(pygame.sprite.Sprite):

    size = 50
    speed = 10
    vel = 5

    def __init__(self, screen, WIDTH, HEIGTH):
        super().__init__()
        # self.image = pygame.image.load(image)

        # Load explosion animation frames
        # self.frames = [
        #     pygame.image.load(f'./asset/collocation/{i}.png') for i in range(1, 4)
        # ]

        self.frames = [
            pygame.image.load(f'./asset/player/idle.png'),
            pygame.image.load(f'./asset/player/run_1.png'),
            pygame.image.load(f'./asset/player/run_2.png'),
            pygame.image.load(f'./asset/player/down_run_1.png'),
            pygame.image.load(f'./asset/player/down_run_2.png'),
            pygame.image.load(f'./asset/player/game_over.png'),
        ]
        self.current_frame = 0
        self.frame_delay = 5  # Controls the speed of animation
        self.frame_counter = 0

        # Scale the image
        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (50, HEIGTH//2)
        self.mask = pygame.mask.from_surface(self.image)
        self.screen = screen
        # self.color = color
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH

        self.isJump = False
        self.jumpCount = self.speed
    
    def start(self):
        pass

    def update(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.rect.move_ip(0,-self.speed)
        # if keys[pygame.K_s]:
        #     self.rect.move_ip(0,self.speed)
        # if keys[pygame.K_a]:
        #     self.rect.move_ip(-self.speed,0)
        # if keys[pygame.K_d]:
        #     self.rect.move_ip(self.speed,0)

        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            
            if not self.isJump:
                if keys[pygame.K_DOWN]:
                    self.current_frame += 1
                    if self.current_frame >= 5:
                        self.current_frame = 3
                else:
                    self.current_frame += 1
                    if self.current_frame >= 3:
                        self.current_frame = 1
            else:
                self.current_frame = 0
            # print(self.current_frame)
                
            
            # sig
            # if self.current_frame < len(self.frames):
            #     self.image = pygame.transform.scale(self.frames[self.current_frame], (self.size, self.size))
            # else:
            #     # print('done')
            #     self.kill()  # Remove the sprite when the animation is done
            #     # self.current_frame = 0
        

        if not self.isJump: 
            # if keys[pygame.K_UP] and player_y > vel:
            #     player_y -= vel

            # if keys[pygame.K_DOWN] and player_y < 500 - height - vel:
            #     player_y += vel

            if keys[pygame.K_SPACE]:
                self.isJump = True
        else:
            # print(self.rect.y)
            if self.jumpCount >= -self.speed:
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.2
                self.jumpCount -= 0.5
            else: 
                self.jumpCount = self.speed
                self.isJump = False
            
        self.rect.clamp_ip(0,0,self.WIDTH, self.HEIGTH)
        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self)
        self.screen.blit(self.image, self.rect)
