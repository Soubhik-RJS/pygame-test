import pygame
import sys

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
player = pygame.Rect(width // 2, height // 2, 30, 30)
player_speed = 10

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    # Move player
    if keys[pygame.K_a]:
        player = player.move(-player_speed, 0)
    if keys[pygame.K_d]:
        player = player.move(player_speed, 0)
    if keys[pygame.K_w]:
        player = player.move(0, -player_speed)
    if keys[pygame.K_s]:
        player = player.move(0, player_speed)
    
    # prevent to out of screen
    player = player.clamp(0,0,width,height)

    # Fill screen
    screen.fill(white)

    # Draw player
    pygame.draw.rect(screen, red, player)

    # Update display
    pygame.display.update()
    clock.tick(fps)
