import pygame
import sys
from Player import Player
from Enemy import Enemy

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basic Game')
clock = pygame.time.Clock()
fps = 30

# Set up colors
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

# Set up player
player = Player(screen, width, height)
player.start()

enemy = Enemy(screen, width, height)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update()

    # Fill screen
    screen.fill(white)

    # Draw player
    player.draw()
    enemy.draw()

    # Update display
    pygame.display.update()
    clock.tick(fps)
