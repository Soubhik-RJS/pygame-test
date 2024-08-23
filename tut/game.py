import pygame

# x = pygame.init()
pygame.init()

width = 900
height = 600

gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Fast Game")
pygame.display.update()

clock = pygame.time.Clock()

# color var
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

# game var
exit_game = False
game_over = False
fps = 30

snake_size = 50
snake_x = 55
snake_y = 55
snake_speed = 5

velocity_x = 0
velocity_y = 0

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                # velocity_x += 10
                velocity_x = 10
                velocity_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                # velocity_x -= 10
                velocity_x = -10
                velocity_y = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                # velocity_y -= 10
                velocity_x = 0
                velocity_y = -10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                # velocity_y += 10
                velocity_x = 0
                velocity_y = 10
    

    snake_x += velocity_x
    snake_y += velocity_y

    snake_x = max(0, min(width - snake_size, snake_x))
    snake_y = max(0, min(height - snake_size, snake_y))

    gameWindow.fill(white)

    pygame.draw.rect(gameWindow, green, [snake_x,snake_y,snake_size,snake_size])

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()