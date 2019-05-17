import pygame
from .config import Config
from .board import Board

class Game:
    def __init__(self, display):
        self.display = display

    def loop(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

        pygame.display.update()
        clock.tick(Config['game']['fps'])
