import pygame
import math
from settings import *


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/bullet.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, TILE_DIMENSIONS)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.speed = 10
        self.x_speed = 0
        self.y_speed = 0
        self.direction = 0

    def get_direction(self, player1, player2):
        (dx, dy) = (player2.rect.centerx - player1.rect.centerx, player2.rect.top - player1.rect.top)
        self.direction = math.atan2(dy, dx)
        self.x_speed = self.speed * math.cos(self.direction)
        self.y_speed = self.speed * math.sin(self.direction)

    def update(self):
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += self.speed * math.sin(self.direction)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


Bullets1 = pygame.sprite.Group()