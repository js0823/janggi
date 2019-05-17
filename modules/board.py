from .config import Config

class Board:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX # janggi has 9 x 8 boxes
        self.sizeY = sizeY
        self.cellSize = Config['board']['cellSize']
    
    def draw_board(self):
        background_color = Config['board']['color']
        