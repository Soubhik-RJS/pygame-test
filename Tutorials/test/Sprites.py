import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Sprite Example")

# Define a color
WHITE = (255, 255, 255)

# Create a Sprite class
class Player(pygame.sprite.Sprite):
    size = 50
    speed = 5
    def __init__(self, image_file, x, y):
        super().__init__()
        self.image = pygame.image.load(image_file)
        # Scale the image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        # You can add movement logic here, for example
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            # self.rect.x -= self.speed
            self.rect.move_ip(-self.speed,0)
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        
        self.rect.clamp_ip(0,0,screen_width,screen_height)

# Load the sprite image
player_image = "oops/asset/player.png"  # Replace with the path to your sprite image

# Create a sprite group and add the player
all_sprites = pygame.sprite.Group()
player = Player(player_image, 100, 100)
all_sprites.add(player)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # # Update and draw all sprites
    # all_sprites.update()
    # all_sprites.draw(screen)

    # Manually update the sprite
    player.update()
    # Manually draw the sprite on the screen
    screen.blit(player.image, player.rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
