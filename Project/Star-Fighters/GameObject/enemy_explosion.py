import pygame
import sys

class EnemyExplosion(pygame.sprite.Sprite):

    size = 50

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen

        # Load explosion animation frames
        self.frames = [
            pygame.image.load(f'./asset/enemy_explosion/{i}.png') for i in range(1, 4)
        ]
        self.current_frame = 0
        self.frame_delay = 10  # Controls the speed of animation
        self.frame_counter = 0

        # Set the initial image and position
        self.image = pygame.transform.scale(self.frames[self.current_frame], (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def update(self):
        # Update the animation frame
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.frame_counter = 0
            self.current_frame += 1
            
            # sig
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


    def draw(self):
        # Draw the current frame of the explosion
        self.screen.blit(self.image, self.rect)
