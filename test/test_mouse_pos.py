import pygame
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

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    
    # if not pygame.mouse.get_focused():
    #     print("out")

    if pygame.mouse.get_pressed()[0]:
        # print(pygame.mouse.get_pos())

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

    
    player_x, player_y = move_towards_target(player_x,player_y,mouse_pos[0],mouse_pos[1],player_speed)
    # if mouse_pressed:
    # player_x, player_y = move_continuously(player_x,player_y,mouse_pos[0],mouse_pos[1],player_speed)


    # Fill screen
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(fps)
