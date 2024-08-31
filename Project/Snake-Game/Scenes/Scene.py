import pygame
import sys

class Scene:

    def __init__(self, screen, clock, fps):
        # Set up screen
        self.screen = screen
        self.clock = clock
        self.fps = fps
        # Set up colors
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.BLACK = (0,0,0)
        # Set screen color
        self.color = self.WHITE

    def start(self):
        pass

    def event(self, e):
        pass

    def update(self):
        pass

    def draw(self):
        pass
    
    def run(self):
        self.start()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.event(event)
            self.update()
            self.screen.fill(self.color)
            self.draw()
            pygame.display.update()
            self.clock.tick(self.fps)