import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y=SCREEN_HEIGHT // 2 + 2 * GRASS_SIZE):
        super().__init__()
        self.image = pygame.image.load("assets/images/character.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.health = 3

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
        elif self.moving_right:
            self.rect.x += 2

        # make sure the player is in a valid position
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)
