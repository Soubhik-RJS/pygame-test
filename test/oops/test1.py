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
# enemy = Enemy(screen, width, height)

enemy1 = Enemy(screen, 100, 200, width, height, [10,15],player)
enemy2 = Enemy(screen, 300, 100, width, height, [16,15],player)
enemy3 = Enemy(screen, 100, 500, width, height, [15,17],player)

enemy_list = [enemy1,enemy2,enemy3]
enemy_col_list = [enemy1.circle, enemy2.circle, enemy3.circle]

player.start(enemy_col_list)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.update()

    for enemy in enemy_list:
        enemy.update()

    # Fill screen
    screen.fill(white)

    # Draw player
    player.draw()
    for enemy in enemy_list:
        enemy.draw()

    # Update display
    pygame.display.update()
    clock.tick(fps)
