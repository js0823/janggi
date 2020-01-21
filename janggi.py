#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon
import sys
import pygame
from utils.settings import GameSettings
from utils.board import Board
from tkinter import Tk, messagebox
from utils.piece import JanggiSet


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
  
    def run_game(self):
        self.initialize_pieces()
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(self.game_settings.maxFPS)
   
    def check_events(self):
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
            # elif event.type == pygame.MOUSEBUTTONDOWN and self.grabbed_piece is None: # no grabbed piece yet
            #     self.mouseDown = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cursorPos = pygame.mouse.get_pos()

                # grab the current player's piece
                if self.turn == 0:
                    self.grabbed_piece = self.grab_piece(cursorPos, self.red_set)
                else:
                    self.grabbed_piece = self.grab_piece(cursorPos, self.green_set)
            elif self.mouseDown == False and self.mouseReleased == False and self.grabbed_piece: # piece is grabbed and all mouse is released
                self.grabbed_piece.update(pygame.mouse.get_pos())

    def grab_piece(self, cursorPos, janggiSet):
        for piece in janggiSet.pieces:
            if piece.rect.collidepoint(cursorPos):
                print(piece.name)
                return piece
    
            
    def initialize_pieces(self):
        zolPos = 0
        chaPos = 0
        poPos = 1
        maPos = 1
        sangPos = 2
        saPos = 3
        for gPiece, rPiece in zip(self.green_set.pieces, self.red_set.pieces):
            if gPiece.name == 'Zol':
                gPiece.draw(self.board.pieceLoc[3][zolPos])
                rPiece.draw(self.board.pieceLoc[6][zolPos])
                zolPos += 2
            elif gPiece.name == 'Cha':
                gPiece.draw(self.board.pieceLoc[0][chaPos])
                rPiece.draw(self.board.pieceLoc[9][chaPos])
                chaPos = 8
            elif gPiece.name == 'Po':
                gPiece.draw(self.board.pieceLoc[2][poPos])
                rPiece.draw(self.board.pieceLoc[7][poPos])
                poPos = 7
            elif gPiece.name == 'Ma':
                gPiece.draw(self.board.pieceLoc[0][maPos])
                rPiece.draw(self.board.pieceLoc[9][maPos])
                maPos = 7
            elif gPiece.name == 'Sang':
                gPiece.draw(self.board.pieceLoc[0][sangPos])
                rPiece.draw(self.board.pieceLoc[9][sangPos])
                sangPos = 6
            elif gPiece.name == 'Sa':
                gPiece.draw(self.board.pieceLoc[0][saPos])
                rPiece.draw(self.board.pieceLoc[9][saPos])
                saPos = 5
            elif gPiece.name == 'King':
                gPiece.draw(self.board.pieceLoc[1][4])
                rPiece.draw(self.board.pieceLoc[8][4])
   
    def update_screen(self):
        #pygame.draw.circle(self.screen, (255, 0, 0), (410, 450), 7)
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