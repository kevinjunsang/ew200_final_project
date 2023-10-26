import pygame
from settings import *

class Pawns:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/chess_pawn.png").convert()
        self.image.set_colorkey(BLACK)
        self.x = x
        self.y = y
        self.capture = False
        self.double = True






