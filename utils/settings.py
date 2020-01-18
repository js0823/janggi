class GameSettings:
    def __init__(self):
        self.name = 'Janggi'
        self.version = '0.0.1'
        self.maxFPS = 30


class BoardSettings:
    def __init__(self):
        self.color = (226, 173, 47)
        self.boardSize = 820 # original value = 820
        self.boardRow = 9
        self.boardCol = 8
        self.xMargin = 50
        self.yMargin = 50