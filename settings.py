# settings.py
import pygame
import os

NUM_ROWS_AND_COLS = 8
TILESIZE = 80
WIDTH = TILESIZE * NUM_ROWS_AND_COLS + 1
HEIGHT = TILESIZE * NUM_ROWS_AND_COLS + 1
TITLE = "Pente"
ALPHA = 'ABCDEFGHI'
TOKENS_TO_WIN = 10
IN_A_ROW_TO_WIN = 4

# Load and scale images
white_token = pygame.transform.scale(pygame.image.load(os.path.join("assets", "WhiteToken.png")), (TILESIZE, TILESIZE))
black_token = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BlackToken.png")), (TILESIZE, TILESIZE))
transitionWhiteToBlack = [pygame.transform.scale(pygame.image.load(os.path.join("assets", f"WhiteToBlack{i}.png")), (TILESIZE, TILESIZE)) for i in range(1, 4)]
transitionBlackToWhite = [pygame.transform.scale(pygame.image.load(os.path.join("assets", f"BlackToWhite{i}.png")), (TILESIZE, TILESIZE)) for i in range(1, 4)]


