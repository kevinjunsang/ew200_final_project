import pygame
from settings import *


class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/sword.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, TILE_DIMENSIONS)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

    def draw(self, screen):
        screen.blit(self.image, self.rect)


Swords = pygame.sprite.Group()