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

    def drawBoard(self):
        board_surface = pygame.display.set_mode((self.windowSize, self.windowSize))
        board_surface.fill(self.background_color)
        
        # Draw vertical lines
        for row in range(self.boardCol + 1):
            start_x = (row * self.spaceWidth) + self.xMargin
            start_y = self.yMargin
            end_x = (row * self.spaceWidth) + self.xMargin
            end_y = self.yMargin + (self.boardCol * self.spaceWidth)
            pygame.draw.line(board_surface, (0, 0, 0), (start_x, start_y), (end_x, end_y))
        # draw column lines
        for col in range(self.boardRow + 1):
            start_x = self.xMargin
            start_y = (col * self.spaceHeight) + self.yMargin
            end_x = self.xMargin + (self.boardRow * self.spaceHeight)
            end_y = (col * self.spaceHeight) + self.yMargin
            pygame.draw.line(board_surface, (0, 0, 0), (start_x, start_y), (end_x, end_y))
        

        # draw diagonal lines
        pygame.draw.line(board_surface, (0, 0, 0), (320, 50), (500, 210))
        pygame.draw.line(board_surface, (0, 0, 0), (500, 50), (320, 210))
        pygame.draw.line(board_surface, (0, 0, 0), (320, 610), (500, 770))
        pygame.draw.line(board_surface, (0, 0, 0), (320, 770), (500, 610))
        
        pygame.display.flip()

        return board_surface