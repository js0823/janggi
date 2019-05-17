#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon

import pygame
from pygame.locals import *
from modules.game import Game

__version__ = '0.0.1'

def main():
    #pygame.init()
    logo = pygame.image.load('logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Janggi {}'.format(__version__))
    display = pygame.display.set_mode((800, 600))

    game = Game(display)
    game.loop()

if __name__ == '__main__':
    main()