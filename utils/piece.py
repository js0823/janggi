import pygame
from .settings import BoardSettings
import json
import math

class Piece:
    def __init__(self, game, name, size, image):
        self.screen = game.screen
        self.name = name
        self.image = image
        self.size = size
        self.rect = self.image.get_rect()
        self.grabbed = False
        self.boardPos = None # board position in x y coordinate

    def draw(self, position):
        self.rect.center = position[0], position[1]
        self.screen.blit(self.image, self.rect)

class JanggiSet:
    def __init__(self, game, color, pieceImages, pieceData):
        self.game = game
        self.color = color
        self.pieces = []
        self.pieceImages = pieceImages
        self.pieceData = json.load(open(pieceData))
        self.load_pieces()
    
    def load_pieces(self):
        pieces_ss = SpriteSheet(self.pieceImages)
        black_transparency = (0, 0, 0) # for making pieces transparent

        for name in ('Cha', 'King', 'Ma', 'Po', 'Sa', 'Sang', 'Zol'):
            rect = (self.pieceData['frames'][self.color + '_' + name + '.png']['frame']['x'],
                        self.pieceData['frames'][self.color + '_' + name + '.png']['frame']['y'],
                        self.pieceData['frames'][self.color + '_' + name + '.png']['frame']['w'],
                        self.pieceData['frames'][self.color + '_' + name + '.png']['frame']['h'])
            size = (self.pieceData['frames'][self.color + '_' + name + '.png']['sourceSize']['w'],
                    self.pieceData['frames'][self.color + '_' + name + '.png']['sourceSize']['h'])
            
            num = None
            if name == 'Zol': # there are five Zol
                num = 5
            elif name == 'Cha' or name == 'Po' or name == 'Ma' or name == 'Sang' or name == 'Sa': # there are two of each
                num = 2
            else: # only 1 king
                num = 1

            for i in range(num):
                image = pieces_ss.image_at(rect, black_transparency)
                image = pygame.transform.smoothscale(image, (90, 80))
                piece = Piece(self.game, self.color + name + str(i), size, image)
                self.pieces.append(piece)


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