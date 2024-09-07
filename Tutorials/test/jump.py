import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basic Game')
clock = pygame.time.Clock()
fps = 60

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
vel = 5

# These go near the top of your program, outside the while loop
isJump = False
jumpCount = 10

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    # if keys[pygame.K_w]:
    #     player_y -= player_speed
    # if keys[pygame.K_s]:
    #     player_y += player_speed

    # # Goes inside the while loop, under event for moving down
    # if keys[pygame.K_SPACE]:
    #     isJump = True
    
    if not isJump: 
        # if keys[pygame.K_UP] and player_y > vel:
        #     player_y -= vel

        # if keys[pygame.K_DOWN] and player_y < 500 - height - vel:
        #     player_y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        print(player_y)
        if jumpCount >= -10:
            player_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    # Fill screen
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
    pygame.draw.line(screen, white, (0, (height/2)+player_size),(width, (height/2)+player_size),10)

    # Update display
    pygame.display.update()
    clock.tick(fps)
