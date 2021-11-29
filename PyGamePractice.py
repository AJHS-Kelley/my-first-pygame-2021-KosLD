# PyGame Practice, Bruce Smith, 11/29/21 9:00am, v0.2

import pygame, sys
from pygame.locals import *

# start PyGame
pygame.init()

# Create game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello, world!")