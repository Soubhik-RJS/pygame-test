import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basic Game')

# Set up colors
black = (0, 0, 0)
red = (255, 0, 0)

# Set up player
player_size = 50
player_x = width // 2
player_y = height // 2
player_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Fill screen
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.flip()
