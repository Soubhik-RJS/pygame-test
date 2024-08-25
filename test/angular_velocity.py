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
pygame.display.set_caption('Test angular velocity Game')
font = pygame.font.SysFont(None, 40)

# Set up colors
black = (0, 0, 0)
red = (255, 0, 0)
w = (255,255,255)

# Set up player
player_size = 30
player_x = width // 2
player_y = height // 2
player_speed = 10

angle = 90

def text_screen(text, color, x, y, center=False):
    screen_text = font.render(text, True, color)
    text_rect = screen_text.get_rect(center=(x,y)) if center else [x,y]
    screen.blit(screen_text, text_rect)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    speed_x = 0
    speed_y = 0
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        # player_x -= player_speed
        angle += 10
    if keys[pygame.K_RIGHT]:
        # player_x += player_speed
        angle -= 10
    if keys[pygame.K_UP]:
        speed_x = player_speed * math.cos(math.radians(angle))
        speed_y = -player_speed * math.sin(math.radians(angle))
    if keys[pygame.K_DOWN]:
        speed_x = -player_speed * math.cos(math.radians(angle))
        speed_y = player_speed * math.sin(math.radians(angle))

    
    player_x += speed_x
    player_y += speed_y

    # Fill screen
    screen.fill(black)

    # Draw player
    text_screen(f"Angle: {angle}", w,5,5)
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.flip()
    clock.tick(fps)
