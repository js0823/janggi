#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon
import sys
import pygame
from utils.settings import GameSettings
from utils.settings import BoardSettings
from utils.board import Board
from utils.piece import JanggiSet
import math

class JanggiGame:
    """
    Main class that starts the game.
    """
    def __init__(self):
        pygame.init()
        self.game_settings = GameSettings()
        self.board_settings = BoardSettings()
        self.logo = pygame.image.load('assets/logo.png')
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption(
            "{} Version: {}".format(self.game_settings.name, self.game_settings.version))

        self.board = Board()
        self.screen = self.board.drawBoard()
        self.clock = pygame.time.Clock()

        self.green_set = JanggiSet(self, 'Green', 'assets/green_pieces.png', 'assets/green_pieces.json')
        self.red_set = JanggiSet(self, 'Red', 'assets/red_pieces.png', 'assets/red_pieces.json')

        # mouse tracker
        self.mouseDown = False
        self.mouseReleased = False
        
        self.grabbed_piece = None
        self.moveList = []

        # player turn
        self.turn = "Red"
  
    def run_game(self):
        self.initialize_pieces()
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.game_settings.maxFPS)
   
    def check_events(self):
        cursor = pygame.mouse.get_pos() # cursor position
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # mouse clicked
                if not self.grabbed_piece: # piece is clicked to pick up the piece.
                    if self.turn == "Red":
                        self.grabbed_piece = self.grab_piece(cursor, self.red_set)
                    else:
                        self.grabbed_piece = self.grab_piece(cursor, self.green_set)
                    
                    if self.grabbed_piece:
                        self.fillAvailableMoves()
                elif self.grabbed_piece: # piece is currently grabbed and mouse is pressed to put the piece down.
                    placed = self.placePiece(cursor)
                    self.moveList = []
                    self.grabbed_piece = None
                    if placed:
                        if self.turn == "Red":
                            self.turn = "Green"
                        else:
                            self.turn = "Red"

    def update_screen(self):
        self.screen = self.board.drawBoard()

        for gPiece, rPiece in zip(self.green_set.pieces, self.red_set.pieces):
            gPiece.draw(gPiece.boardPos)
            rPiece.draw(rPiece.boardPos)

        if self.grabbed_piece:
            for x, y in self.moveList:
                if self.board.boardGrid[x][y] != 0 and self.turn not in self.board.boardGrid[x][y].name:
                    pygame.draw.circle(self.screen, (255, 0, 0), self.board.locCoord[x][y], 7)
                else:
                    pygame.draw.circle(self.screen, (0, 255, 0), self.board.locCoord[x][y], 7)
            cursor = pygame.mouse.get_pos()
            self.grabbed_piece.boardPos = [cursor[0], cursor[1]]

        pygame.display.update()
    
    def placePiece(self, cursor):
        # place piece. Returns true if placed, else return false.
        if not cursor:
            print("Error in calcDistance. Cursor information not available.")
        
        gridX, gridY = None, None
        minDist = float('inf')
        tolerance = min(self.board_settings.xMargin, self.board_settings.yMargin) // 2
        for x, y in self.moveList:
            coordX, coordY = self.board.locCoord[x][y][0], self.board.locCoord[x][y][1]
            dist = math.sqrt((coordX - cursor[0]) ** 2 + (coordY - cursor[1]) ** 2)
            if dist < tolerance and dist < minDist:
                minDist = dist
                gridX, gridY = x, y
        
        if gridX is not None and gridY is not None:
            self.board.boardGrid[gridX][gridY] = self.grabbed_piece
            self.board.boardGrid[self.grabbed_piece.gridPos[0]][self.grabbed_piece.gridPos[1]] = 0
            self.grabbed_piece.boardPos = self.board.locCoord[gridX][gridY]
            self.grabbed_piece.gridPos = [gridX, gridY]
            
            return True
        else:
            self.grabbed_piece.boardPos = self.board.locCoord[self.grabbed_piece.gridPos[0]][self.grabbed_piece.gridPos[1]]
            return False

    def grab_piece(self, cursorPos, janggiSet):
        for piece in janggiSet.pieces:
            if piece.rect.collidepoint(cursorPos):
                print("{} is grabbed.".format(piece.name))
                piece.grabbed = True
                return piece
        
        return
    
    def fillAvailableMoves(self):
        # returns all grid positions in which the piece is able to move.
        if not self.grabbed_piece:
            return []
        
        curPos = self.grabbed_piece.gridPos
        boardLenX = len(self.board.boardGrid)
        boardLenY = len(self.board.boardGrid[0])

        if "Zol" in self.grabbed_piece.name:
            directions = ()
            if self.turn == "Red":
                directions = ((0, -1), (0, 1), (-1, 0))
            elif self.turn == "Green":
                directions = ((0, -1), (0, 1), (1, 0))
            
            for x, y in directions:
                posX, posY = curPos[0] + x, curPos[1] + y
                if 0 <= posX < boardLenX and 0 <= posY < boardLenY:
                    if self.board.boardGrid[posX][posY] == 0:
                        self.moveList.append([posX, posY])
                    else:
                        if self.turn not in self.board.boardGrid[posX][posY].name:
                            self.moveList.append([posX, posY])
        elif "Cha" in self.grabbed_piece.name:
            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for x, y in directions:
                posX, posY = curPos[0] + x, curPos[1] + y
                while 0 <= posX < boardLenX and 0 <= posY < boardLenY and \
                            self.board.boardGrid[posX][posY] == 0:
                    self.moveList.append([posX, posY])
                    posX += x
                    posY += y
                if 0 <= posX < boardLenX and 0 <= posY < boardLenY and self.turn not in self.board.boardGrid[posX][posY].name:
                    self.moveList.append([posX, posY])
        elif "Ma" in self.grabbed_piece.name:
            directions = ((2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2), (-2, 1), (-2, -1))
            for x, y in directions:
                posX, posY = curPos[0] + x, curPos[1] + y
                if 0 <= posX < boardLenX and 0 <= posY < boardLenY:
                    if self.board.boardGrid[posX][posY] == 0:
                        self.moveList.append([posX, posY])
                    else:
                        if self.turn not in self.board.boardGrid[posX][posY].name:
                            self.moveList.append([posX, posY])
        elif "Sang" in self.grabbed_piece.name:
            directions = ((3, 2), (3, -2), (-3, 2), (-3, -2), (-2, 3), (2, 3), (-2, -3), (2, -3))
            for x, y in directions:
                posX, posY = curPos[0] + x, curPos[1] + y
                if 0 <= posX < boardLenX and 0 <= posY < boardLenY:
                    if self.board.boardGrid[posX][posY] == 0:
                        self.moveList.append([posX, posY])
                    else:
                        if self.turn not in self.board.boardGrid[posX][posY].name:
                            self.moveList.append([posX, posY])
        elif "Po" in self.grabbed_piece.name:
            # Po moves by jumping over other team's piece. Po cannot jump other team's Po.
            # When Po jumps, it can land on other team's piece and kill that piece.
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for x, y in directions:
                posX, posY = curPos[0] + x, curPos[1] + y
                while 0 <= posX < boardLenX and 0 <= posY < boardLenY and self.board.boardGrid[posX][posY] == 0:
                    posX, posY = posX + x, posY + y
                if 0 <= posX < boardLenX and 0 <= posY < boardLenY and "Po" in self.board.boardGrid[posX][posY].name:
                    continue
                else:
                    posX, posY = posX + x, posY + y
                    while 0 <= posX < boardLenX and 0 <= posY < boardLenY:
                        if self.board.boardGrid[posX][posY] != 0 and "Po" in self.board.boardGrid[posX][posY].name:
                            break
                        self.moveList.append([posX, posY])
                        posX, posY = posX + x, posY + y

        elif "Sa" in self.grabbed_piece.name or "King" in self.grabbed_piece.name:
            # Sa can only move within the square where king resides.
            lowX, highX, lowY, highY = 0, 0, 0, 0
            diagPos = []
            straightPos = []
            if self.turn == "Green":
                lowX, highX = 0, 2
                lowY, highY = 3, 5
                diagPos = [(0, 3), (0, 5), (2, 3), (2, 5), (1, 4)]
                straightPos = [(1, 3), (0, 4), (1, 5), (2, 4)]
            elif self.turn == "Red":
                lowX, highX = 7, 9
                lowY, highY = 3, 5
                diagPos = [(7, 3), (7, 5), (9, 3), (9, 5), (8, 4)]
                straightPos = [(8, 3), (8, 5), (7, 4), (9, 4)]
            
            directions = None
            if (curPos[0], curPos[1]) in diagPos:
                directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
            
            for x, y in directions:
                posX, posY = curPos[0] + x, curPos[1] + y
                if lowX <= posX <= highX and lowY <= posY <= highY:
                    if self.board.boardGrid[posX][posY] == 0:
                        self.moveList.append([posX, posY])
                    else:
                        if self.turn not in self.board.boardGrid[posX][posY].name:
                            self.moveList.append([posX, posY])
    
    def check_checkMate(self):
        # if checkmate, return True
        pass

    def check_check(self):
        # if check, next user must make sure the king is not checked.
        pass

    # def update_moveList(self, piece):
    #     if "Cha" in piece.name:
    #     elif "Ma" in piece.name:
    #     elif "Po" in piece.name:
    #     elif "Sa" in piece.name:
    #     elif "Sang" in piece.name:
    #     elif "Zol" in piece.name:
    #     else: # it is king

    def initialize_pieces(self):
        zolPos = 0
        chaPos = 0
        poPos = 1
        maPos = 1
        sangPos = 2
        saPos = 3
        for gPiece, rPiece in zip(self.green_set.pieces, self.red_set.pieces):
            if 'GreenZol' in gPiece.name and 'RedZol' in rPiece.name:
                self.board.boardGrid[3][zolPos] = gPiece
                self.board.boardGrid[6][zolPos] = rPiece
                gPiece.boardPos = self.board.locCoord[3][zolPos]
                rPiece.boardPos = self.board.locCoord[6][zolPos]
                gPiece.gridPos = [3, zolPos]
                rPiece.gridPos = [6, zolPos]
                zolPos += 2
            elif 'GreenCha' in gPiece.name and 'RedCha' in rPiece.name:
                self.board.boardGrid[0][chaPos] = gPiece
                self.board.boardGrid[9][chaPos] = rPiece
                gPiece.boardPos = self.board.locCoord[0][chaPos]
                rPiece.boardPos = self.board.locCoord[9][chaPos]
                gPiece.gridPos = [0, chaPos]
                rPiece.gridPos = [9, chaPos]
                chaPos = 8
            elif 'GreenPo' in gPiece.name and 'RedPo' in rPiece.name:
                self.board.boardGrid[2][poPos] = gPiece
                self.board.boardGrid[7][poPos] = rPiece
                gPiece.boardPos = self.board.locCoord[2][poPos]
                rPiece.boardPos = self.board.locCoord[7][poPos]
                gPiece.gridPos = [2, poPos]
                rPiece.gridPos = [7, poPos]
                poPos = 7
            elif 'GreenMa' in gPiece.name and 'RedMa' in rPiece.name:
                self.board.boardGrid[0][maPos] = gPiece
                self.board.boardGrid[9][maPos] = rPiece
                gPiece.boardPos = self.board.locCoord[0][maPos]
                rPiece.boardPos = self.board.locCoord[9][maPos]
                gPiece.gridPos = [0, maPos]
                rPiece.gridPos = [9, maPos]
                maPos = 7
            elif 'GreenSang' in gPiece.name and 'RedSang' in rPiece.name:
                self.board.boardGrid[0][sangPos] = gPiece
                self.board.boardGrid[9][sangPos] = rPiece
                gPiece.boardPos = self.board.locCoord[0][sangPos]
                rPiece.boardPos = self.board.locCoord[9][sangPos]
                gPiece.gridPos = [0, sangPos]
                rPiece.gridPos = [9, sangPos]
                sangPos = 6
            elif 'GreenSa' in gPiece.name and 'RedSa' in rPiece.name:
                self.board.boardGrid[0][saPos] = gPiece
                self.board.boardGrid[9][saPos] = rPiece
                gPiece.boardPos = self.board.locCoord[0][saPos]
                rPiece.boardPos = self.board.locCoord[9][saPos]
                gPiece.gridPos = [0, saPos]
                rPiece.gridPos = [9, saPos]
                saPos = 5
            elif 'GreenKing' in gPiece.name and 'RedKing' in rPiece.name:
                self.board.boardGrid[1][4] = gPiece
                self.board.boardGrid[8][4] = rPiece
                gPiece.boardPos = self.board.locCoord[1][4]
                rPiece.boardPos = self.board.locCoord[8][4]
                gPiece.gridPos = [1, 4]
                rPiece.gridPos = [8, 4]
            else:
                print("Initialize board failed. Check your pieces.")
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    janggi_game = JanggiGame()
    janggi_game.run_game()