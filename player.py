import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x=SCREEN_WIDTH // 2, y=GRASS_HEIGHT):
        super().__init__()
        self.image = pygame.image.load("assets/images/character.png").convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.full_heart = pygame.image.load("assets/images/full_heart.png").convert()
        self.full_heart.set_colorkey(BLACK)
        self.full_heart = pygame.transform.scale(self.full_heart, TILE_DIMENSIONS)
        self.half_heart = pygame.image.load("assets/images/half_heart.png").convert()
        self.half_heart.set_colorkey(BLACK)
        self.half_heart = pygame.transform.scale(self.half_heart, TILE_DIMENSIONS)
        self.empty_heart = pygame.image.load("assets/images/empty_heart.png").convert()
        self.empty_heart.set_colorkey(BLACK)
        self.empty_heart = pygame.transform.scale(self.empty_heart, TILE_DIMENSIONS)
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.key = pygame.image.load("assets/images/key.png").convert()
        self.key.set_colorkey(BLACK)
        self.key = pygame.transform.scale(self.key, TILE_DIMENSIONS)
        self.key_num = 0
        self.moving_left = False
        self.moving_right = False
        self.jump = False
        self.jump_strength = BASE_JUMP
        self.vertical_speed = 0
        self.double_jump = 1
        self.jump_count = 0
        self.bottom = GRASS_HEIGHT
        self.health = 6

    def update(self):
        if self.rect.top <= self.bottom:
            self.rect.y -= self.vertical_speed
            self.vertical_speed -= 1
        if self.moving_left:
            self.rect.x -= 2
        elif self.moving_right:
            self.rect.x += 2

        # make sure the player is in a valid position
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.right > RIGHT_TOP_X_RANGE and self.rect.top < RIGHT_TOP_HEIGHT:
            self.bottom = RIGHT_TOP_HEIGHT
        if MIDDLE_TOP_X_RANGE_LOW < self.rect.left < MIDDLE_TOP_X_RANGE_HI and self.rect.top < MIDDLE_TOP_HEIGHT:
            self.bottom = MIDDLE_TOP_HEIGHT
        if LEFT_TOP_X_RANGE_LOW < self.rect.left < LEFT_TOP_X_RANGE_HI and self.rect.top < LEFT_TOP_HEIGHT:
            self.bottom = LEFT_TOP_HEIGHT
        if MIDDLE_TOP_X_RANGE_HI < self.rect.left < RIGHT_TOP_X_RANGE - PLAYER_WIDTH:
            self.bottom = GRASS_HEIGHT
        if LEFT_TOP_X_RANGE_HI < self.rect.left < LEFT_TOP_X_RANGE_LOW - PLAYER_WIDTH:
            self.bottom = GRASS_HEIGHT
            # need to figure out how to make sure that when he falls off of the platform his initial velo is 0
        if self.rect.top > self.bottom:
            self.rect.top = self.bottom
            self.vertical_speed = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.key_num == 1:
            screen.blit(self.key, KEY_1_POSITION)
        if self.key_num == 2:
            screen.blit(self.key, KEY_1_POSITION)
            screen.blit(self.key, KEY_2_POSITION)
        if self.health == 6:
            screen.blit(self.full_heart, HEART_1_POSITION)
            screen.blit(self.full_heart, HEART_2_POSITION)
            screen.blit(self.full_heart, HEART_3_POSITION)
        if self.health == 5:
            screen.blit(self.full_heart, HEART_1_POSITION)
            screen.blit(self.full_heart, HEART_2_POSITION)
            screen.blit(self.half_heart, HEART_3_POSITION)
        if self.health == 4:
            screen.blit(self.full_heart, HEART_1_POSITION)
            screen.blit(self.full_heart, HEART_2_POSITION)
            screen.blit(self.empty_heart, HEART_3_POSITION)
        if self.health == 3:
            screen.blit(self.full_heart, HEART_1_POSITION)
            screen.blit(self.half_heart, HEART_2_POSITION)
            screen.blit(self.empty_heart, HEART_3_POSITION)
        if self.health == 2:
            screen.blit(self.full_heart, HEART_1_POSITION)
            screen.blit(self.empty_heart, HEART_2_POSITION)
            screen.blit(self.empty_heart, HEART_3_POSITION)
        if self.health == 1:
            screen.blit(self.half_heart, HEART_1_POSITION)
            screen.blit(self.empty_heart, HEART_2_POSITION)
            screen.blit(self.empty_heart, HEART_3_POSITION)
        if self.health <= 0:
            screen.blit(self.empty_heart, HEART_1_POSITION)
            screen.blit(self.empty_heart, HEART_2_POSITION)
            screen.blit(self.empty_heart, HEART_3_POSITION)