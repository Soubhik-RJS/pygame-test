import pygame
import sys

class Ball(pygame.Rect):
    
    radius= 10

    def __init__(self, screen, WIDTH, HEIGTH, color, blocks, walls, player):
        super().__init__(WIDTH/2,HEIGTH/2+100,20,20)
        self.screen = screen
        # self = pygame.draw.circle(screen,color,(WIDTH/2,HEIGTH/2+100),self.radius)
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.color = color
        self.blocks = blocks
        self.walls = walls
        self.player = player
        # var
        self.speed = 5
        self.velocity = [-self.speed,-self.speed]
    
    def collide(self,blocks):
        i = self.collidelist(blocks)
        if i >= 0:
            # Determine the overlap distances
            overlap_left = self.right - blocks[i].left
            overlap_right = blocks[i].right - self.left
            overlap_top = self.bottom - blocks[i].top
            overlap_bottom = blocks[i].bottom - self.top
            
            # Determine the minimum overlap and reverse the appropriate velocity component
            if min(overlap_left, overlap_right) < min(overlap_top, overlap_bottom):
                # Horizontal collision
                self.velocity[0] = -self.velocity[0]
                # Correct position to prevent sticking
                if overlap_left < overlap_right:
                    self.right = blocks[i].left
                else:
                    self.left = blocks[i].right
            else:
                # Vertical collision
                self.velocity[1] = -self.velocity[1]
                # Correct position to prevent sticking
                if overlap_top < overlap_bottom:
                    self.bottom = blocks[i].top
                else:
                    self.top = blocks[i].bottom
        return i
    
    def update(self):
        self.move_ip(self.velocity)

        if self.left <= 0 or self.right >= self.WIDTH:
            self.velocity[0] = -self.velocity[0]
        if self.top <= 0:
            self.velocity[1] = -self.velocity[1]

        self.collide(self.walls)
        self.collide([self.player])
        return self.collide(self.blocks)
        
    def draw(self):
        pygame.draw.rect(self.screen,self.color,self,border_radius=999)
        # pygame.draw.circle(self.screen, self.color, (self.x, self.y),self.radius)