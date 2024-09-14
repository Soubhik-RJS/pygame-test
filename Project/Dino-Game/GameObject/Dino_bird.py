import pygame
import sys
import random

class Dinobird(pygame.sprite.Sprite):

    size = 40

    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.screen = screen
        self.speed = speed

        # Load explosion animation frames
        self.frames = [
            pygame.image.load(f'./asset/dino_bird/{i}.png') for i in range(1, 3)
        ]
        self.current_frame = 0
        self.frame_delay = 5  # Controls the speed of animation
        self.frame_counter = 0

        # Set the initial image and position
        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y-(random.randint(0,1)*25))
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        # Update the animation frame
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            self.current_frame += 1
            
            # # sig
            # if self.current_frame < len(self.frames):
            #     self.image = pygame.transform.scale(self.frames[self.current_frame], (self.size, self.size))
            # else:
            #     # print('done')
            #     self.kill()  # Remove the sprite when the animation is done
            #     # self.current_frame = 0

            # loop
            if self.current_frame >= len(self.frames):
                self.current_frame = 0  # Loop back to the first frame

            # Update the image to the current frame
            self.image = pygame.transform.scale(self.frames[self.current_frame], (self.size, self.size))

        self.rect.move_ip(-self.speed,0)

        if self.rect.x <= -70:
            self.kill()


    def draw(self):
        # Draw the current frame of the explosion
        self.screen.blit(self.image, self.rect)
