#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon

import pygame
from modules.config import GameSettings
from modules.board import Board

class JanggiGame:
    def __init__(self):
        pygame.init()
        self.gameSettings = GameSettings()
        self.logo = pygame.image.load('assets/logo.png')
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("{} Version: {}".format(self.gameSettings.name, self.gameSettings.version))
        
        self.board = Board()
        self.display = self.board.drawBoard()
        self.clock = pygame.time.Clock()
  
    def run_game(self):
        self.clock.tick(self.gameSettings.maxFPS)
        while True:
            self.check_events()
            self.update_screen()
   
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
   
    def update_screen(self):
        pygame.display.update()


if __name__ == '__main__':
    janggi_game = JanggiGame()
    janggi_game.run_game()