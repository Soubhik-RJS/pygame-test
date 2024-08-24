import pygame
import random

# x = pygame.init()
pygame.init()

width = 900
height = 600

gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Fast Game")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# color var
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, list, size):
    # print(list)
    for x,y in list:
        pygame.draw.rect(gameWindow, color, [x,y,size,size])

def game():

    # game var
    exit_game = False
    game_over = False
    fps = 30

    snake_size = 20
    snake_x = 55
    snake_y = 55
    snake_speed = 1
    snake_list = []
    snake_length = 1

    food_x = random.randint(snake_size, width//2)
    food_y = random.randint(snake_size, height//2)

    score = 0
    velocity = 10
    velocity_x = 0
    velocity_y = 0

    while not exit_game:

        if game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        game()
            
            gameWindow.fill(white)
            text_screen("Game Over\n Press Enter To Continue", red, width/2, height/2)
            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        # velocity_x += 10
                        velocity_x = velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        # velocity_x -= 10
                        velocity_x = -velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        # velocity_y -= 10
                        velocity_x = 0
                        velocity_y = -velocity
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        # velocity_y += 10
                        velocity_x = 0
                        velocity_y = velocity
            

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
                score += 1
                snake_length += 5
                # print(f"Score: {score}") 
                food_x = random.randint(0, width)
                food_y = random.randint(0, height)

            if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
                game_over = True
                # print("game over")

            # snake_x = max(0, min(width - snake_size, snake_x))
            # snake_y = max(0, min(height - snake_size, snake_y))

            
            gameWindow.fill(white)

            text_screen(f"Score: {score}", black, 5,5)

            pygame.draw.rect(gameWindow, red, [food_x,food_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over = True

            # pygame.draw.rect(gameWindow, green, [snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow, green, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

game()
pygame.quit()
quit()