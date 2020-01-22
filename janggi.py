#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon
import sys
import pygame
from utils.settings import GameSettings
from utils.board import Board
from tkinter import Tk, messagebox
from utils.piece import JanggiSet
import math

class JanggiGame:
    """
    Main class that starts the game.
    """
    def __init__(self):
        pygame.init()
        self.game_settings = GameSettings()
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

        # player turn
        self.turn = 0 # 0 is red, 1 is green

        # game board piece positions. 0 is empty.
        self.boardGrid = [[0] * len(self.board.pieceLoc[0]) for _ in range(len(self.board.pieceLoc))]
  
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
                ask = messagebox.askyesno(message="Would you like to quit?")
                if ask:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ask = messagebox.askyesno(message="Would you like to quit?")
                    if ask:
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP: # mouse click on the piece
                if not self.grabbed_piece:
                # grab the current player's piece
                    if self.turn == 0:
                        self.grabbed_piece = self.grab_piece(cursor, self.red_set)
                    else:
                        self.grabbed_piece = self.grab_piece(cursor, self.green_set)
                elif self.grabbed_piece:
                    # check the distance of all available places piece can be put, and put the piece on the
                    # closest position on the board.
                    self.grabbed_piece.boardPos = self.getClosestPosition(cursor)
                    self.grabbed_piece = None

    
    def getClosestPosition(self, cursor):
        if not cursor:
            print("Error in calcDistance. Cursor information not available.")

        xCoord, yCoord = 0, 0
        shortestDist = float('inf')
        for i in range(len(self.board.pieceLoc)):
            for j in range(len(self.board.pieceLoc[i])):
                dist = math.sqrt((self.board.pieceLoc[i][j][0] - cursor[0]) ** 2 + (self.board.pieceLoc[i][j][1] - cursor[1]) ** 2)
                if shortestDist > dist:
                    xCoord, yCoord = self.board.pieceLoc[i][j][0], self.board.pieceLoc[i][j][1]
                    shortestDist = dist
        
        return [xCoord, yCoord]


    def grab_piece(self, cursorPos, janggiSet):
        for piece in janggiSet.pieces:
            if piece.rect.collidepoint(cursorPos):
                print(piece.name)
                piece.grabbed = True
                return piece
        
        return
            
    def initialize_pieces(self):
        zolPos = 0
        chaPos = 0
        poPos = 1
        maPos = 1
        sangPos = 2
        saPos = 3
        for gPiece, rPiece in zip(self.green_set.pieces, self.red_set.pieces):
            if 'GreenZol' in gPiece.name and 'RedZol' in rPiece.name:
                gPiece.draw(self.board.pieceLoc[3][zolPos])
                rPiece.draw(self.board.pieceLoc[6][zolPos])
                self.boardGrid[3][zolPos] = gPiece
                self.boardGrid[6][zolPos] = rPiece
                gPiece.boardPos = self.board.pieceLoc[3][zolPos]
                rPiece.boardPos = self.board.pieceLoc[6][zolPos]
                zolPos += 2
            elif 'GreenCha' in gPiece.name and 'RedCha' in rPiece.name:
                gPiece.draw(self.board.pieceLoc[0][chaPos])
                rPiece.draw(self.board.pieceLoc[9][chaPos])
                self.boardGrid[0][chaPos] = gPiece
                self.boardGrid[9][chaPos] = rPiece
                gPiece.boardPos = self.board.pieceLoc[0][chaPos]
                rPiece.boardPos = self.board.pieceLoc[9][chaPos]
                chaPos = 8
            elif 'GreenPo' in gPiece.name and 'RedPo' in rPiece.name:
                gPiece.draw(self.board.pieceLoc[2][poPos])
                rPiece.draw(self.board.pieceLoc[7][poPos])
                self.boardGrid[2][poPos] = gPiece
                self.boardGrid[7][poPos] = rPiece
                gPiece.boardPos = self.board.pieceLoc[2][poPos]
                rPiece.boardPos = self.board.pieceLoc[7][poPos]
                poPos = 7
            elif 'GreenMa' in gPiece.name and 'RedMa' in rPiece.name:
                gPiece.draw(self.board.pieceLoc[0][maPos])
                rPiece.draw(self.board.pieceLoc[9][maPos])
                self.boardGrid[0][maPos] = gPiece
                self.boardGrid[9][maPos] = rPiece
                gPiece.boardPos = self.board.pieceLoc[0][maPos]
                rPiece.boardPos = self.board.pieceLoc[9][maPos]
                maPos = 7
            elif 'GreenSang' in gPiece.name and 'RedSang' in rPiece.name:
                gPiece.draw(self.board.pieceLoc[0][sangPos])
                rPiece.draw(self.board.pieceLoc[9][sangPos])
                self.boardGrid[0][sangPos] = gPiece
                self.boardGrid[9][sangPos] = rPiece
                gPiece.boardPos = self.board.pieceLoc[0][sangPos]
                rPiece.boardPos = self.board.pieceLoc[9][sangPos]
                sangPos = 6
            elif 'GreenSa' in gPiece.name and 'RedSa' in rPiece.name:
                gPiece.draw(self.board.pieceLoc[0][saPos])
                rPiece.draw(self.board.pieceLoc[9][saPos])
                self.boardGrid[0][saPos] = gPiece
                self.boardGrid[9][saPos] = rPiece
                gPiece.boardPos = self.board.pieceLoc[0][saPos]
                rPiece.boardPos = self.board.pieceLoc[9][saPos]
                saPos = 5
            elif 'GreenKing' in gPiece.name and 'RedKing' in rPiece.name:
                gPiece.draw(self.board.pieceLoc[1][4])
                rPiece.draw(self.board.pieceLoc[8][4])
                self.boardGrid[1][4] = gPiece
                self.boardGrid[8][4] = rPiece
                gPiece.boardPos = self.board.pieceLoc[1][4]
                rPiece.boardPos = self.board.pieceLoc[8][4]
            else:
                print("Initialize board failed. Check your pieces.")
                pygame.quit()
                sys.exit()
   
    def update_screen(self):
        #pygame.draw.circle(self.screen, (255, 0, 0), (410, 450), 7)
        if self.grabbed_piece:
            cursor = pygame.mouse.get_pos()
            self.grabbed_piece.boardPos = [cursor[0], cursor[1]]
        
        self.screen = self.board.drawBoard()
        for gPiece, rPiece in zip(self.green_set.pieces, self.red_set.pieces):
            gPiece.draw(gPiece.boardPos)
            rPiece.draw(rPiece.boardPos)

        pygame.display.update()
    
    def check_checkMate(self):
        # if checkmate, return True
        pass

    def check_check(self):
        # if check, next user must make sure the king is not checked.
        pass

    def check_game_status(self):
        pass


if __name__ == '__main__':
    janggi_game = JanggiGame()
    janggi_game.run_game()