import pygame
import sys
from Scenes.Welcome import Welcome
from Scenes.Single_Game import SingleGame
from Scenes.Multi_Game import MultiGame
from Scenes.GameOver import GameOver

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGTH = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Table Tennis')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
fps = 60

gameOver = GameOver(screen,clock,fps,font,WIDTH,HEIGTH)
singleGame = SingleGame(screen,clock,fps,font,WIDTH,HEIGTH,gameOver)
multiGame = MultiGame(screen,clock,fps,font,WIDTH,HEIGTH,gameOver)
welcome = Welcome(screen,clock,fps,font,WIDTH,HEIGTH,singleGame, multiGame)
gameOver.set_load_scene(welcome, singleGame, multiGame)
welcome.run()
