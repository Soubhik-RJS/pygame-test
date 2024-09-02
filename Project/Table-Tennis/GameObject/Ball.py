import pygame
import sys

class Ball(pygame.Rect):
    
    def __init__(self, screen, WIDTH, HEIGTH, color, player_left, player_right):
        super().__init__(WIDTH/2-15,HEIGTH/2-15,30,30)
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.color = color
        self.player_left = player_left
        self.player_right = player_right
        
        # Variable
        self.speed = [5,5]
        self.velocity = [0,0]


    def update(self):
        self.move_ip(self.velocity)

        if self.top <= 0 or self.bottom >= self.HEIGTH:
            self.velocity[1] = -self.velocity[1]

        # if self.left <= 0 or self.right >= self.WIDTH:
        #     self.velocity[0] = -self.velocity[0]

        # if self.colliderect(self.player_left) or self.colliderect(self.player_right):
        #     if ((self.left <= self.player_left.left or self.right >= self.player_left.right)
        #         or
        #         (self.left <= self.player_right.left or self.right >= self.player_right.right)):
        #         self.velocity[0] = -self.velocity[0]
        #     if ((self.top <= self.player_left.top or self.bottom >= self.player_left.bottom)
        #         or
        #         (self.top <= self.player_right.top or self.bottom >= self.player_right.bottom)):
        #         self.velocity[1] = -self.velocity[1]
        #     # self.speed[0] += 1
        #     # self.speed[1] += 1
        #     self.point += 1

        # if self.colliderect(self.player_left) or self.colliderect(self.player_right):
        #     self.velocity[0] = -self.velocity[0]
        #     # self.speed[0] += 1
        #     # self.speed[1] += 1
        #     self.point += 1

        # print(self.player_right.height)  
        # if (self.player_right.x <= self.x <= self.player_right.x + self.player_right.width
        # and self.player_right.y <= self.y <= self.player_right.y + self.player_right.height):
        #     self.velocity[0] = -self.velocity[0]
        #     self.point += 1

        # if (abs(self.x-self.player_right.x)<self.player_right.width and abs(self.y-self.player_right.y)<self.player_right.height
        #     or abs(self.x-self.player_left.x)<self.player_left.width and abs(self.y-self.player_left.y)<self.player_left.height):
        #     self.velocity[0] = -self.velocity[0]
        #     self.point += 1

        # Check collision with right player
        if (self.x + self.width > self.player_right.x and
            self.x < self.player_right.x + self.player_right.width and
            self.y + self.height > self.player_right.y and
            self.y < self.player_right.y + self.player_right.height):
            
            self.velocity[0] = -self.velocity[0]
            
            # Adjust the ball's position to be just outside the player's boundary
            self.x = self.player_right.x - self.width - 1  # Placing ball just outside the right player's left edge
            
            return {"name": "right", "score": 1}

        # Check collision with left player
        elif (self.x < self.player_left.x + self.player_left.width and
            self.x + self.width > self.player_left.x and
            self.y + self.height > self.player_left.y and
            self.y < self.player_left.y + self.player_left.height):
            
            self.velocity[0] = -self.velocity[0]
            
            # Adjust the ball's position to be just outside the player's boundary
            self.x = self.player_left.x + self.player_left.width + 1  # Placing ball just outside the left player's right edge
            
            return {"name": "left", "score": 1}



        # if ((self.left <= self.player_left.right and abs(self.y-self.player_left.y) < self.player_left.size[1])
        #     or 
        #     (self.right >= self.player_right.left and abs(self.y - self.player_right.y) < self.player_right.size[1])):
        #         self.velocity[0] = -self.velocity[0]
        #         self.point += 1
        return {"name": "none", "score": 0}

    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self, border_radius=999)