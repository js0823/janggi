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
        #self.red_set = JanggiSet(self, 'Red', 'assets/red_pieces.png', 'assets/red_pieces.json')
  
    def run_game(self):
        self.clock.tick(self.game_settings.maxFPS)
        self.initialize_board()
        while True:
            self.check_events()
            self.update_screen()
   
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    ask = messagebox.askyesno(message="Would you like to quit?")
                    if ask:
                        sys.exit()
    
    def initialize_board(self):
        zolPos = 0
        chaPos = 0
        poPos = 1
        maPos = 1
        sangPos = 2
        saPos = 3
        for piece in self.green_set.pieces:
            print(piece.name)
            if piece.name == 'Zol':
                piece.put(self.board.pieceLoc[3][zolPos])
                zolPos += 2
            elif piece.name == 'Cha':
                piece.put(self.board.pieceLoc[0][chaPos])
                chaPos = 8
            elif piece.name == 'Po':
                piece.put(self.board.pieceLoc[2][poPos])
                poPos = 7
            elif piece.name == 'Ma':
                piece.put(self.board.pieceLoc[0][maPos])
                maPos = 7
            elif piece.name == 'Sang':
                piece.put(self.board.pieceLoc[0][sangPos])
                sangPos = 6
            elif piece.name == 'Sa':
                piece.put(self.board.pieceLoc[0][saPos])
                saPos = 5
            elif piece.name == 'King':
                piece.put(self.board.pieceLoc[1][4])
   
    def update_screen(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (410, 450), 5)
        pygame.display.update()


if __name__ == '__main__':
    janggi_game = JanggiGame()
    janggi_game.run_game()