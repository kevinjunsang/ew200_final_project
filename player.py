import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y = GROUND_HEIGHT):
        super().__init__()
        self.image = pygame.image.load("assets/images/character.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.jump = False
        self.jump_strength = BASE_JUMP
        self.jump_count = self.jump_strength
        self.health = 3

    def update(self):
        if self.jump:
            if self.jump_count >= -self.jump_strength:
                self.rect.y -= (self.jump_count * abs(self.jump_count)) * 0.25
                self.jump_count -= 1
            else:
                self.jump_count = self.jump_strength
                self.jump = False
        if self.moving_left:
            self.rect.x -= 2
        elif self.moving_right:
            self.rect.x += 2

        # make sure the player is in a valid position
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top > GROUND_HEIGHT:
            self.rect.top = GROUND_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)
