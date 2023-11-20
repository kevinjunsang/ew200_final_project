import pygame
from settings import *


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x=SCREEN_WIDTH // 2, y=GRASS_HEIGHT):
        super().__init__()
        self.image = pygame.image.load("assets/images/ghost.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.key = pygame.image.load("assets/images/key.png").convert()
        self.key.set_colorkey(BLACK)
        self.key = pygame.transform.scale(self.key, TILE_DIMENSIONS)
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.key_num = 0
        self.revive = True

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
        elif self.moving_right:
            self.rect.x += 2
        if self.moving_up:
            self.rect.y -= 2
        elif self.moving_down:
            self.rect.y += 2

        # make sure the ghost is in the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.key_num == 1:
            screen.blit(self.key, KEY_3_POSITION)
