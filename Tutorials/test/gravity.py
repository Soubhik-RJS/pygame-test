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
gravity = 0.5  # Gravity acceleration
player_speed = 5  # Player movement speed
player_fall_speed = 0  # Player's vertical speed
jump_force = -10  # Upward force for jumping

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Set up player
player_size = 30
player_x = width // 2
player_y = 100

# Ground positions and sizes
ground_y = 500
ground_height = 100
ground_y_1 = 450
ground_1_width = 100

# Track if the player is on the ground
on_ground = False

def detect_collision(player_pos, player_size, platform_pos, platform_size):
    if (player_pos[0] < platform_pos[0] + platform_size[0] and
        player_pos[0] + player_size > platform_pos[0] and
        player_pos[1] < platform_pos[1] + platform_size[1] and
        player_pos[1] + player_size > platform_pos[1]):
        return True
    return False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Reset position
                player_x = width // 2
                player_y = 100
                player_fall_speed = 0
            if event.key == pygame.K_SPACE and on_ground:
                # Jump when space is pressed and the player is on the ground
                player_fall_speed = jump_force
                on_ground = False

    keys = pygame.key.get_pressed()

    # Horizontal movement
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Apply gravity
    player_fall_speed += gravity
    player_y += player_fall_speed

    # Check for collision with the first platform (ground)
    if detect_collision((player_x, player_y), player_size, (0, ground_y), (width, ground_height)):
        player_y = ground_y - player_size
        player_fall_speed = 0
        on_ground = True

    # Check for collision with the second platform (raised platform)
    elif detect_collision((player_x, player_y), player_size, (0, ground_y_1), (ground_1_width, ground_height)):
        player_y = ground_y_1 - player_size
        player_fall_speed = 0
        on_ground = True

    else:
        on_ground = False

    # Prevent player from moving off-screen
    if player_x < 0:
        player_x = 0
    if player_x + player_size > width:
        player_x = width - player_size

    # Fill screen
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, green, (0, ground_y, width, ground_height))
    pygame.draw.rect(screen, green, (0, ground_y_1, ground_1_width, ground_height))

    # Update display
    pygame.display.update()
    clock.tick(fps)
