import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Player vs Enemy')

# Set up clock for frame rate
clock = pygame.time.Clock()

# Set up colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up player
player_size = 50
player_x = width // 2
player_y = height - player_size * 2
player_speed = 5

# Set up enemy
total_enemy = 5
enemy_x = []
enemy_y = []
enemy_size = 50
enemy_speed = 5
# enemy_x = random.randint(0, width-enemy_size)
# enemy_y = 0

def detect_collision(player_x, player_y, enemy_x, enemy_y):
    if (player_x < enemy_x + enemy_size and
        player_x + player_size > enemy_x and
        player_y < enemy_y + enemy_size and
        player_y + player_size > enemy_y):
        return True
    return False

for i in range(total_enemy):
    enemy_x.append(random.randint(0+enemy_size+10, width-enemy_size))
    enemy_y.append(-random.randrange(0+enemy_size+10, 500))

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    # Move player
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed

    # Prevent player from moving off screen
    player_x = max(0, min(width - player_size, player_x))

    # Move enemy
    # enemy_y += enemy_speed
    for i in range(total_enemy):
        enemy_y[i] += enemy_speed

        # Check for collision with player
        if detect_collision(player_x, player_y, enemy_x[i], enemy_y[i]):
            print("Collision detected! Game Over.")
            pygame.quit()
            sys.exit()

    # Respawn enemy if it goes off screen
    # if enemy_y > height:
    #     enemy_y = 0
    #     enemy_x = random.randint(0, width - enemy_size)

    # for i in range(total_enemy):
        if enemy_y[i] > height:
            enemy_y[i] = 0
            enemy_x[i] = random.randint(0+enemy_size+10, width-enemy_size)

    # Fill screen
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Draw enemy
    # pygame.draw.rect(screen, green, (enemy_x, enemy_y, enemy_size, enemy_size))

    for i in range(total_enemy):
        pygame.draw.rect(screen, green, (enemy_x[i], enemy_y[i], enemy_size, enemy_size)) 

    # Update display
    pygame.display.flip()

    # Cap the frame rate at 60 frames per second
    clock.tick(60)
