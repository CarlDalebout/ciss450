DELAY = 0 # delay between each frame update
SPEED = 2 # speed in pixels of digits
# For faster animation, set DELAY to 0 and SPEED to 100

TILE_WIDTH = 50
TILE_HEIGHT = 50

n = 10

FONT_SIZE = int(0.8*TILE_HEIGHT)

BLACK = (0,0,0)
WHITE = (100,255,255)
SIZE = (WIDTH,HEIGHT) = (n*TILE_WIDTH,(n+1)*(TILE_WIDTH))

TRIES_COLOR = [0,255,0]

import pygame
TRIES_FONT = pygame.font.Font(None, int(0.8*FONT_SIZE))
