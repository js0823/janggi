import pygame
from .settings import BoardSettings
import json

data = json.load(open('assets/janggi_pieces.json'))


class Piece:
    def __init__(self, game, name, team, image):
        self.image = image
        self.name = name
        self.team = team
    
        self.screen = game.screen

        self.x = 0.0
        self.y = 0.0

    def blitme(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)

class JanggiSet:
    def __init__(self, game):
        self.game = game
        self.pieces = []
        self.load_pieces()
    
    def load_pieces(self):
        fileName = 'assets/janggi_pieces.png'
        pieces_ss = SpriteSheet(fileName)
        
        # load Green_Cha.png
        g_cha_rect = (data['frames']['Green_Cha.png']['frame']['x'],
                            data['frames']['Green_Cha.png']['frame']['y'],
                            data['frames']['Green_Cha.png']['frame']['w'],
                            data['frames']['Green_Cha.png']['frame']['h'])
        
        blackTransparency = (0, 0, 0)
        g_cha_image = pieces_ss.image_at(g_cha_rect, blackTransparency)
        g_cha = Piece(self.game, 'gCha', 'Green', g_cha_image)
        self.pieces.append(g_cha)

class SpriteSheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print("Unable to load spritesheet image.")
            raise SystemExit(e)
    
    def image_at(self, rectangle, colorkey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        
        return image
    
    def images_at(self, rects, colorkey=None):
        return [self.image_at(rect, colorkey) for rect in rects]
    
    def load_strip(self, rect, image_count, colorkey=None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(tups, colorkey)