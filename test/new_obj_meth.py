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
player_size = 30
player_x = width // 2
player_y = height // 2
player_speed = 10

# player = pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
player = pygame.Rect(player_x, player_y, player_size, player_size)
enemy_list = [
    pygame.Rect(player_x+100, player_y+100, player_size, player_size),
    pygame.Rect(player_x+200, player_y+100, player_size, player_size),
    pygame.Rect(player_x-100, player_y-200, player_size, player_size)
]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    # Move player
    if keys[pygame.K_a]:
        # player_x -= player_speed
        player = player.move(-player_speed, 0)
    if keys[pygame.K_d]:
        # player_x += player_speed
        player = player.move(+player_speed, 0)
    if keys[pygame.K_w]:
        # player_y -= player_speed
        player = player.move(0, -player_speed)
    if keys[pygame.K_s]:
        # player_y += player_speed
        player = player.move(0, player_speed)
    
    # print(player.bottom)
    # print(player.bottomleft)
    # print(player.center)
    # player = player.clip(0,0,width,height)

    # Clamping
    # player.x = max(0, min(width - player.size[0], player.x))
    # player.y = max(0, min(height - player.size[0], player.y))

    # Advance Clamping
    # player = player.clamp(0,0,width,height)
    # player = player.clamp(0,0,width,player.y+player_size)

    # if player.left <= 0:
    #     player.x = 100
    # if player.right >= width:
    #     player.x = 0

    # if not player.collidelist([enemy]):
    #     print("game over")

    collision = player.collidelist(enemy_list)
    if collision >= 0 :
        print(f"game over collide with {enemy_list[collision]}")
        del enemy_list[collision]



    # if player.left <= 0 or player.right >= width:
    #     player.x = -player.x


    # Fill screen
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, green, player)
    
    for enemy in enemy_list:
        pygame.draw.rect(screen, red, enemy)

    # Update display
    pygame.display.update()
    clock.tick(fps)
