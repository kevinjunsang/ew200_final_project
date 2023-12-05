import pygame
import math
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/images/bullet.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, TILE_DIMENSIONS)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.speed = 8
        self.x_speed = 0
        self.y_speed = 0

    def get_direction(self, player1, player2):
        direction = math.atan2(player2.rect.centery - player1.rect.centery, player2.rect.centerx - player1.rect.centerx)
        self.x_speed = self.speed * math.cos(direction)
        self.y_speed = self.speed * math.sin(direction)

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


Bullets = pygame.sprite.Group()
