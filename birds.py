import pygame
import math
import random
from settings import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, y, speed, direction, amplitude, x=SCREEN_WIDTH):
        super().__init__()
        self.image_1 = pygame.image.load("assets/images/bird1.png").convert()
        self.image_1.set_colorkey(BLACK)
        self.image_2 = pygame.image.load("assets/images/bird2.png").convert()
        self.image_2.set_colorkey(BLACK)
        self.image_3 = pygame.image.load("assets/images/bird3.png").convert()
        self.image_3.set_colorkey(BLACK)
        self.rect = pygame.rect.Rect(x, y, self.image_1.get_width(), self.image_1.get_height())
        self.height = self.rect.y
        self.angle_counter = 0
        self.moving_right = direction
        self.moving_left = not direction
        self.speed = speed
        self.images = []
        for _ in range(30):
            self.images.append(self.image_1)
        for _ in range(30):
            self.images.append(self.image_2)
        for _ in range(30):
            self.images.append(self.image_3)
        for _ in range(30):
            self.images.append(self.image_2)
        self.image_counter = 0
        self.image = self.images[self.image_counter]
        self.amplitude = amplitude

    def update(self):
        self.image_counter += 1
        self.image = self.images[self.image_counter % len(self.images)]
        if self.moving_right:
            self.rect.x += self.speed
        elif self.moving_left:
            self.rect.x -= self.speed
        self.angle_counter += math.pi / 60
        self.rect.y = self.height + TILE_SIZE * self.amplitude * math.sin(self.angle_counter)

        # make sure this puts the bird in a valid position
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -self.image.get_width()
            self.speed = random.randint(2, 6)
        elif self.rect.x < -self.image.get_width():
            self.rect.x = SCREEN_WIDTH
            self.speed = random.randint(2, 6)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


Birds = pygame.sprite.Group()
