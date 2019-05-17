#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon

import pygame
from pygame.locals import *
from modules.game import Game
from modules.config import Config

__version__ = '0.0.1'

def main():
    pygame.init()
    logo = pygame.image.load('assets/logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption(Config['game']['caption'] + Config['game']['version'])
    display = pygame.display.set_mode((Config['game']['width'], Config['game']['height']))
    display.fill(Config['board']['color'])

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()