import pygame
import sys
from Welcome import Welcome
from Game import Game

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGTH = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Basic Game')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
fps = 30

game = Game(screen,clock,fps,font,WIDTH,HEIGTH)
welcome = Welcome(screen,clock,fps,font,WIDTH,HEIGTH, game)
welcome.run()