import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mesh Collider Example with Masks")

# Define a color
WHITE = (255, 255, 255)

# Create a Sprite class with a mask for pixel-perfect collisions
class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y, scale_width, scale_height):
        super().__init__()
        # Load and scale the image
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (scale_width, scale_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Create a mask for pixel-perfect collision detection
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Create a simple obstacle sprite to collide with
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y, scale_width, scale_height):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (scale_width, scale_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # Create a mask for the obstacle
        self.mask = pygame.mask.from_surface(self.image)

# Load the sprite images
player_image = "oops/asset/player.png"  # Replace with your sprite image path
obstacle_image = "oops/asset/obstacle.png"  # Replace with your obstacle image path

# Create the player and obstacle
player = Player(player_image, 100, 100, 100, 150)
obstacle = Obstacle(obstacle_image, 300, 300, 100, 150)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update the player position
    player.update()

    # Check for pixel-perfect collision
    offset_x = obstacle.rect.x - player.rect.x
    offset_y = obstacle.rect.y - player.rect.y
    if player.mask.overlap(obstacle.mask, (offset_x, offset_y)):
        print("Collision detected!")

    # Draw the sprites
    screen.blit(player.image, player.rect)
    screen.blit(obstacle.image, obstacle.rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
