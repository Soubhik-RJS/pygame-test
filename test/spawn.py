import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Basic Game')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
fps = 30

# Set up colors
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

def text_screen(text, color, x, y, center=False):
    screen_text = font.render(text, True, color)
    text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
    screen.blit(screen_text, text_rect)

# Game loop
def game():
    game_over = False
    # Set up player
    player_size = 30
    player_x = width // 2
    player_y = height // 2
    player_speed = 10
    enemy_speed = [5,5]
    enemy_speeds = [
        [10,5],
        [5,6],
        [5,7],
        [2,5],
        [6,5],
        [5,9],
    ]

    player = pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
    # player = pygame.Rect(player_x, player_y, player_size, player_size)

    enemy_list = [
        pygame.Rect(random.randint(50, width-50), random.randint(50, height-50), player_size, player_size),
        pygame.Rect(random.randint(50, width-50), random.randint(50, height-50), player_size, player_size),
        pygame.Rect(random.randint(50, width-50), random.randint(50, height-50), player_size, player_size),
        pygame.Rect(random.randint(50, width-50), random.randint(50, height-50), player_size, player_size),
        pygame.Rect(random.randint(50, width-50), random.randint(50, height-50), player_size, player_size),
        pygame.Rect(random.randint(50, width-50), random.randint(50, height-50), player_size, player_size),
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    game()
        
        if not game_over:
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

            
            for i,enemy in enumerate(enemy_list):
                speed = enemy_speeds[i]
                enemy.move_ip(speed[0], speed[1])
                # also works
                # enemy.x += speed[0]
                # enemy.y += speed[1]

                # Check for boundary collision and reverse direction
                if enemy.left <= 0 or enemy.right >= width:
                    speed[0] = -speed[0]
                if enemy.top <= 0 or enemy.bottom >= height:
                    speed[1] = -speed[1]
            
            if player.collidelist(enemy_list) >= 0:
                # print('game over')
                game_over = True

            # Fill screen
            screen.fill(white)

            # Draw player
            # pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
            pygame.draw.rect(screen, black, player)

            for enemy in enemy_list:
                pygame.draw.rect(screen, red, enemy)
        else:
            screen.fill(red)
            text_screen("Game Over",white,width/2-50, height/2-50,True)
            text_screen("Press Enter to restart",white,width/2+50, height/2+50,True)

        # Update display
        pygame.display.update()
        clock.tick(fps)

game()