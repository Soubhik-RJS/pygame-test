import pygame

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
TILE_SIZE = 40

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Level Map (W = Wall, P = Player)
level_map = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W            WW    W",
    "W     W            W",
    "W    WWW           W",
    "W     W            W",
    "W                  W",
    "W         P        W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W       W        WWW",
    "W     WWWWW      W W",
    "W                WWW",
    "WWWWWWWWWWWWWWWWWWWW"
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player setup
player = pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE)

# Load level
for y, row in enumerate(level_map):
    for x, tile in enumerate(row):
        if tile == 'W':
            pygame.draw.rect(screen, BLUE, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        elif tile == 'P':
            player.x = x * TILE_SIZE
            player.y = y * TILE_SIZE

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # Clear the screen

    # Redraw the level
    for y, row in enumerate(level_map):
        for x, tile in enumerate(row):
            if tile == 'W':
                pygame.draw.rect(screen, BLUE, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.flip()  # Update the screen

pygame.quit()
