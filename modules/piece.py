import pygame
from .config import Config

class Piece(pygame.sprite.Sprite):
    def __init__(self, image, position, team):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.team = team
        self.square = position