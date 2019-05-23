import pygame
from .config import Config

class Board:
    def __init__(self):
        self.windowSize = 1000
        self.boardRow = 9
        self.boardCol = 8
        #self.xMargin = (self.windowWidth - (self.boardRow * self.rowSpaceSize)) // 2
        #self.yMargin = (self.windowHeight - (self.boardColumn * self.colSpaceSize)) // 2
        self.xMargin = 50
        self.yMargin = 50
        self.spaceHeight = (self.windowSize - self.xMargin - self.xMargin) // self.boardRow
        self.spaceWidth = (self.windowSize -self.yMargin - self.xMargin) // self.boardCol
        self.background_Color = Config['board']['color'] # Background color is yellowish

    def draw_Board(self):

        #surface_Size = 800
        #width_No, height_No = 8, 9 # height and weight number of squares
        
        #wSquare_Size = surface_Size // width_No
        #hSquare_Size = surface_Size // height_No
        #wSurface_Size = wSquare_Size * width_No
        #hSurface_Size = hSquare_Size * height_No

        board_surface = pygame.display.set_mode((self.windowSize, self.windowSize))
        board_surface.fill(self.background_Color)
        
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
        
        pygame.display.flip()

        return board_surface