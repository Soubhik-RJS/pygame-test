import pygame
import sys
from Scenes.Welcome import Welcome
from Scenes.Game import Game
from Scenes.GameOver import GameOver
from Scenes.Final import Final

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGTH = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Ping Pong Ball')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
fps = 60

final = Final(screen,clock,fps,font,WIDTH,HEIGTH)
gameOver = GameOver(screen,clock,fps,font,WIDTH,HEIGTH)
game = Game(screen,clock,fps,font,WIDTH,HEIGTH,gameOver, final)
welcome = Welcome(screen,clock,fps,font,WIDTH,HEIGTH,game)
gameOver.set_load_scene(welcome)
final.set_load_scene(welcome)
welcome.run()
