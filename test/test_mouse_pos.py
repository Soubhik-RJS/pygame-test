import pygame
import math
import sys

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
fps = 30

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basic Game')

# Set up colors
black = (0, 0, 0)
red = (255, 0, 0)

# Set up player
player_size = 20
player_x = width // 2
player_y = height // 2
player_speed = 10
angle = 90

speed_x = 0
speed_y = 0

mouse_pos = (player_x,player_y)
mouse_pressed = False

def move_towards_target(rect_x, rect_y, target_x, target_y, speed):
    dx = target_x - rect_x
    dy = target_y - rect_y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance < speed:
        return target_x, target_y

    ratio = speed / distance
    rect_x += dx * ratio
    rect_y += dy * ratio
    return rect_x, rect_y

def move_continuously(rect_x, rect_y, target_x, target_y, speed):
    dx = target_x - rect_x
    dy = target_y - rect_y
    distance = (dx ** 2 + dy ** 2) ** 0.5

    # If distance is zero, keep moving in the last direction
    if distance != 0:
        # Normalize the direction
        direction_x = dx / distance
        direction_y = dy / distance
    else:
        # Keep moving in the same direction
        direction_x = dx
        direction_y = dy

    # Update position
    rect_x += direction_x * speed
    rect_y += direction_y * speed

    return rect_x, rect_y

# Function to calculate the angle between rect and target
def calculate_angle(rect_pos, target_pos):
    dx = target_pos[0] - rect_pos[0]
    dy = target_pos[1] - rect_pos[1]
    angle = math.atan2(dy, dx)  # Returns the angle in radians
    return math.degrees(angle)  # Convert to degrees for easier understanding

def game_quit():
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_quit()
            if event.key == pygame.K_r:
                #reset player position
                player_x = width / 2
                player_y = height / 2
                speed_x = 0
                speed_y = 0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            angle = -calculate_angle((player_x, player_y), pygame.mouse.get_pos())
            # print(angle)
            speed_x = player_speed * math.cos(math.radians(angle))
            speed_y = -player_speed * math.sin(math.radians(angle))

    # Move player
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_a]:
    #     player_x -= player_speed
    # if keys[pygame.K_d]:
    #     player_x += player_speed
    # if keys[pygame.K_w]:
    #     player_y -= player_speed
    # if keys[pygame.K_s]:
    #     player_y += player_speed
    
    # if not pygame.mouse.get_focused():
    #     print("out")

    if pygame.mouse.get_pressed()[0]:
        # print(pygame.mouse.get_pos())

        # set player position to mouse position
        # player_x = pygame.mouse.get_pos()[0]
        # player_y = pygame.mouse.get_pos()[1]

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = True
    
    # if mouse_pressed:
    #     if not mouse_pos[0] == player_x:
    #         if abs(mouse_pos[0] - player_x) < 10:
    #             player_x += player_speed
    #         else:
    #             player_x -= player_speed
    #     if not abs(mouse_pos[0] - player_y) < 10:
    #         if mouse_pos[1] > player_y:
    #             player_y += player_speed
    #         else:
    #             player_y -= player_speed

    # move towards mouuse postion
    # player_x, player_y = move_towards_target(player_x,player_y,mouse_pos[0],mouse_pos[1],player_speed)
    # if mouse_pressed:
    # player_x, player_y = move_continuously(player_x,player_y,mouse_pos[0],mouse_pos[1],player_speed)

    # speed_x = player_speed * math.cos(math.radians(angle))
    # speed_y = -player_speed * math.sin(math.radians(angle))
    # print(speed_x, speed_y)

    # if keys[pygame.K_SPACE]:
    #     player_x += speed_x
    #     player_y += speed_y

    player_x += speed_x
    player_y += speed_y

    # Fill screen
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(fps)
