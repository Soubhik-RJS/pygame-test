import pygame

# x = pygame.init()
pygame.init()

width = 1200
height = 600

gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Fast Game")

exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("K_RIGHT")


pygame.quit()
quit()