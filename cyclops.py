import pygame
import math
import random
from settings import *


class Cyclops(pygame.sprite.Sprite):
    def __init__(self, x, y, bounds):
        super().__init__()
        self.right_image = pygame.image.load("assets/images/cyclops.png").convert()
        self.right_image.set_colorkey(BLACK)
        self.right_image = pygame.transform.scale(self.right_image, PLAYER_SIZE)
        self.image = self.right_image
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.bottom = y
        self.moving_right = True
        self.moving_left = False
        self.left_bound = bounds[0]
        self.right_bound = bounds[1]

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
            self.image = self.right_image
        elif self.moving_right:
            self.rect.x += 2
            self.image = self.left_image

        if self.rect.right > self.right_bound:
            self.moving_right = False
            self.moving_left = True
        if self.rect.left < self.left_bound:
            self.moving_right = True
            self.moving_left = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)


Enemies = pygame.sprite.Group()
