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
        self.gameSettings = GameSettings()
        self.logo = pygame.image.load('assets/logo.png')
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption(
            "{} Version: {}".format(self.gameSettings.name, self.gameSettings.version))

        self.board = Board()
        self.screen = self.board.drawBoard()
        self.clock = pygame.time.Clock()

        self.janggiSet = JanggiSet(self)
  
    def run_game(self):
        self.clock.tick(self.gameSettings.maxFPS)
        while True:
            self.check_events()
            self.update_screen()
   
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
   
    def update_screen(self):
        self.janggiSet.pieces[0].blitme()
        pygame.display.update()


if __name__ == '__main__':
    janggi_game = JanggiGame()
    janggi_game.run_game()