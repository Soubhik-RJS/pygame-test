import pygame
import sys
from Scenes.Welcome import Welcome
from Scenes.Game import Game
from Scenes.GameOver import GameOver

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGTH = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('pygame-framework')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
fps = 60

gameOver = GameOver(screen,clock,fps,font,WIDTH,HEIGTH)
game = Game(screen,clock,fps,font,WIDTH,HEIGTH,gameOver)
welcome = Welcome(screen,clock,fps,font,WIDTH,HEIGTH,game)
gameOver.set_load_scene(game)
welcome.run()
