import pygame
from .config import BoardSettings
from math import sqrt

class Board:
    def __init__(self):
        self.boardSettings = BoardSettings()
        self.windowSize = self.boardSettings.boardSize
        self.boardRow = 9
        self.boardCol = 8
        #self.xMargin = (self.windowWidth - (self.boardRow * self.rowSpaceSize)) // 2
        #self.yMargin = (self.windowHeight - (self.boardColumn * self.colSpaceSize)) // 2
        self.xMargin = 50
        self.yMargin = 50
        self.spaceHeight = (self.windowSize - self.xMargin - self.xMargin) // self.boardRow
        self.spaceWidth = (self.windowSize -self.yMargin - self.xMargin) // self.boardCol
        self.background_color = self.boardSettings.color

    def drawBoard(self):
        board_surface = pygame.display.set_mode((self.windowSize, self.windowSize))
        board_surface.fill(self.background_color)
        
        # Draw vertical lines
        for row in range(self.boardCol + 1):
            startX = (row * self.spaceWidth) + self.xMargin
            startY = self.yMargin
            endX = (row * self.spaceWidth) + self.xMargin
            endY = self.yMargin + (self.boardCol * self.spaceWidth)
            pygame.draw.line(board_surface, (0, 0, 0), (startX, startY), (endX, endY))
        # draw column lines
        for col in range(self.boardRow + 1):
            startX = self.xMargin
            startY = (col * self.spaceHeight) + self.yMargin
            endX = self.xMargin + (self.boardRow * self.spaceHeight)
            endY = (col * self.spaceHeight) + self.yMargin
            pygame.draw.line(board_surface, (0, 0, 0), (startX, startY), (endX, endY))
        

        # draw diagonal lines
        pygame.draw.line(board_surface, (0, 0, 0), (320, 50), (500, 210))
        pygame.draw.line(board_surface, (0, 0, 0), (500, 50), (320, 210))
        pygame.draw.line(board_surface, (0, 0, 0), (320, 610), (500, 770))
        pygame.draw.line(board_surface, (0, 0, 0), (320, 770), (500, 610))
        
        pygame.display.flip()

        return board_surface