import pygame
from .config import Config
from .board import Board
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP

squareCenters = []

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

class Game:
    def __init__(self, display):
        self.display = display

    def loop(self):
        clock = pygame.time.Clock()

        while True:
            checkQuit()

        pygame.display.update()
        clock.tick(Config['game']['fps'])
