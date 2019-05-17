#!/usr/bin/env python3
# Main for the whole game.
# Author : Jongseo Yoon

import pygame
from pygame.locals import *

def main():
    pygame.init()
    logo = pygame.image.load('logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Janggi')

    screen = pygame.display.set_mode((800, 600))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()