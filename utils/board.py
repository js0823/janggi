import pygame
from .settings import BoardSettings


class Board:
    """
    Everything that has to do with boards.
    """
    def __init__(self):
        self.boardSettings = BoardSettings()
        self.windowSize = self.boardSettings.boardSize
        self.boardRow = self.boardSettings.boardRow
        self.boardCol = self.boardSettings.boardCol
        #self.xMargin = (self.windowWidth - (self.boardRow * self.rowSpaceSize)) // 2
        #self.yMargin = (self.windowHeight - (self.boardColumn * self.colSpaceSize)) // 2
        self.xMargin = self.boardSettings.xMargin
        self.yMargin = self.boardSettings.yMargin
        self.spaceHeight = (self.windowSize - self.xMargin - self.xMargin) // self.boardRow
        self.spaceWidth = (self.windowSize -self.yMargin - self.xMargin) // self.boardCol
        self.background_color = self.boardSettings.color
        self.pieceLoc = [] # location of where pieces can go. format = [[(x, y), (x + 1, y), (x + 2, y) ...], [(x, y + 1), (x + 1, y + 1)]] ...
        self.calcPieceLoc()

    def drawBoard(self):
        board_surface = pygame.display.set_mode((self.windowSize, self.windowSize))
        board_surface.fill(self.background_color)
        
        # draw horizontal lines
        for row in range(self.boardRow + 1):
            start_x = self.xMargin
            start_y = (row * self.spaceHeight) + self.yMargin
            end_x = self.xMargin + (self.boardRow * self.spaceHeight)
            end_y = (row * self.spaceHeight) + self.yMargin
            pygame.draw.line(board_surface, (0, 0, 0), (start_x, start_y), (end_x, end_y))
        # Draw vertical lines
        for col in range(self.boardCol + 1):
            start_x = (col * self.spaceWidth) + self.xMargin
            start_y = self.yMargin
            end_x = (col * self.spaceWidth) + self.xMargin
            end_y = self.yMargin + (self.boardCol * self.spaceWidth)
            pygame.draw.line(board_surface, (0, 0, 0), (start_x, start_y), (end_x, end_y))


        # draw diagonal lines
        pygame.draw.line(board_surface, (0, 0, 0), 
                        (self.xMargin + 3 * self.spaceWidth, self.yMargin), (self.xMargin + 5 * self.spaceWidth, self.yMargin + 2 * self.spaceHeight))
        pygame.draw.line(board_surface, (0, 0, 0), 
                        (self.xMargin + 3 * self.spaceWidth, self.yMargin + 2 * self.spaceHeight), (self.xMargin + 5 * self.spaceWidth, self.yMargin))
        pygame.draw.line(board_surface, (0, 0, 0), 
                        (self.xMargin + 3 * self.spaceWidth, self.yMargin + 7 * self.spaceHeight), (self.xMargin + 5 * self.spaceWidth, self.yMargin + 9 * self.spaceHeight))
        pygame.draw.line(board_surface, (0, 0, 0), 
                        (self.xMargin + 3 * self.spaceWidth, self.yMargin + 9 * self.spaceHeight), (self.xMargin + 5 * self.spaceWidth, self.yMargin + 7 * self.spaceHeight))
        
        pygame.display.flip()

        return board_surface
    
    def calcPieceLoc(self):
        for row in range(self.boardRow + 1):
            thisRow = []
            y = self.yMargin + row * self.spaceHeight
            for col in range(self.boardCol + 1):
                x = self.xMargin + col * self.spaceWidth
                thisRow.append((x, y))
            self.pieceLoc.append(thisRow)