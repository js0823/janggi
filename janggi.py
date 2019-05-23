#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon

import pygame
from pygame.locals import *
from modules.game import Game
from modules.config import Config
from modules.board import Board

def main():
    pygame.init()
    logo = pygame.image.load('assets/logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption(Config['game']['caption'] + " Version " + Config['game']['version'])

    board = Board()
    display = board.draw_Board()
    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()