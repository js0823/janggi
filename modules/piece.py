import pygame
from .config import Config

class Piece(pygame.sprite.Sprite):
    def __init__(self, image, position, team):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.team = team
        self.square = position
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = position.topleft
        self.rect.center = position.center
    
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
    
    def drag(self, cursor):
        self.rect.center = cursor
    
    def update(self, position):
        self.square = position
        self.rect.center = position.center
    
    def movelist(self):
        pass

class Cha(Piece):
    def __init__(self, image, position, team):
        super().__init__(image, position, team)

class King(Piece):
    def __init__(self, image, position, team):
        super().__init__(image, position, team)

class Ma(Piece):
    def __init__(self, image, position, team):
        super().__init__(image, position, team)

class Po(Piece):
    def __init__(self, image, position, team):
        super().__init__(image, position, team)

class Sang(Piece):
    def __init__(self, image, position, team):
        super().__init__(image, position, team)

class Zol(Piece):
    def __init__(self, image, position, team):
        super().__init__(image, position, team)