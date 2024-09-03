import pygame
import noise
import numpy as np

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 40
ROWS, COLS = SCREEN_HEIGHT // TILE_SIZE, SCREEN_WIDTH // TILE_SIZE

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Generate level using Perlin noise
def generate_level(rows, cols, scale=10):
    level = np.zeros((rows, cols))
    for y in range(rows):
        for x in range(cols):
            value = noise.pnoise2(x/scale, y/scale, octaves=6, persistence=0.5, lacunarity=2.0, repeatx=cols, repeaty=rows)
            level[y][x] = 1 if value > 0 else 0
    return level

# Create a level map
level_map = generate_level(ROWS, COLS)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen

    # Draw the level
    for y in range(ROWS):
        for x in range(COLS):
            color = (255, 255, 255) if level_map[y][x] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.flip()  # Update the screen

pygame.quit()
