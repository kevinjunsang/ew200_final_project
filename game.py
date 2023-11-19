import pygame
import sys
import player
import random
from birds import Bird, Birds
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = screen.copy()
background2 = screen.copy()
clock = pygame.time.Clock()


def draw_background():
    backdrop_cloud = pygame.image.load("assets/images/backdrop_cloud.png").convert()
    backdrop_cloud.set_colorkey(BLACK)
    backdrop1 = pygame.image.load("assets/images/backdrop1.png").convert()
    backdrop1.set_colorkey(BLACK)
    backdrop2 = pygame.image.load("assets/images/backdrop2.png").convert()
    backdrop2.set_colorkey(BLACK)
    backdrop3 = pygame.image.load("assets/images/backdrop3.png").convert()
    backdrop3.set_colorkey(BLACK)
    backdrop4 = pygame.image.load("assets/images/backdrop4.png").convert()
    backdrop4.set_colorkey(BLACK)
    backdrop_ground = pygame.image.load("assets/images/backdrop_ground.png").convert()
    backdrop_ground.set_colorkey(BLACK)
    grass1 = pygame.image.load("assets/images/grass1.png").convert()
    grass1.set_colorkey(BLACK)
    grass2 = pygame.image.load("assets/images/grass2.png").convert()
    grass2.set_colorkey(BLACK)
    grass3 = pygame.image.load("assets/images/grass3.png").convert()
    grass3.set_colorkey(BLACK)
    grass4 = pygame.image.load("assets/images/grass4.png").convert()
    grass4.set_colorkey(BLACK)
    dirt1 = pygame.image.load("assets/images/dirt1.png").convert()
    dirt1.set_colorkey(BLACK)
    dirt2 = pygame.image.load("assets/images/dirt2.png").convert()
    dirt2.set_colorkey(BLACK)
    background.fill(BACKGROUND_CLOUD_COLOR)
    for i in range(SCREEN_WIDTH // TILE_SIZE // 4):
        background.blit(backdrop1, (
            TILE_SIZE * i * 4, SCREEN_HEIGHT // 2
        ))
        background.blit(backdrop2, (
            TILE_SIZE * i * 4 + TILE_SIZE, SCREEN_HEIGHT // 2
        ))
        background.blit(backdrop3, (
            TILE_SIZE * i * 4 + 2 * TILE_SIZE, SCREEN_HEIGHT // 2
        ))
        background.blit(backdrop4, (
            TILE_SIZE * i * 4 + 3 * TILE_SIZE, SCREEN_HEIGHT // 2
        ))
    pygame.draw.rect(background, BACKGROUND_GROUND_COLOR, pygame.Rect(
        0, SCREEN_HEIGHT // 2 + TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
    ))
    for i in range(SCREEN_WIDTH // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, GRASS_HEIGHT + GRASS_SIZE
        ))
    for i in range(3 * SCREEN_WIDTH // GRASS_SIZE // 4, SCREEN_WIDTH // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, RIGHT_TOP_HEIGHT + GRASS_SIZE
        ))


draw_background()

my_player = player.Player()
bird_1 = Bird(2 * TILE_SIZE, 2, True)
bird_2 = Bird(4 * TILE_SIZE, 3, False)
bird_3 = Bird(6 * TILE_SIZE, 4, True)
Birds.add(bird_1)
Birds.add(bird_2)
Birds.add(bird_3)
screen.blit(background, (0, 0))
pygame.display.flip()
while True:
    # listen for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_player.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_player.moving_right = True
            if event.key == pygame.K_j:
                my_player.jump_strength = BUFF_JUMP
            if event.key == pygame.K_d:
                my_player.double_jump = 2
            if event.key == pygame.K_SPACE:
                if my_player.rect.top == my_player.bottom:
                    my_player.jump_count = 0
                if my_player.jump_count < my_player.double_jump:
                    my_player.vertical_speed = my_player.jump_strength
                    my_player.jump_count += 1
            if event.key == pygame.K_DOWN:
                if my_player.bottom < GRASS_HEIGHT:
                    my_player.bottom = GRASS_HEIGHT
                my_player.vertical_speed = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_player.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_player.moving_right = False

    my_player.update()
    Birds.update()
    # check for collisions
    if pygame.sprite.spritecollide(my_player, Birds, True):
        my_player.health -= 1
    if bird_1 not in Birds:
        Birds.add(bird_1)
        bird_1.rect.x = SCREEN_WIDTH
        bird_1.direction = random.randint(0,1)
    if bird_2 not in Birds:
        Birds.add(bird_2)
        bird_2.rect.x = SCREEN_WIDTH
        bird_2.direction = random.randint(0, 1)
    if bird_3 not in Birds:
        Birds.add(bird_3)
        bird_3.rect.x = SCREEN_WIDTH
        bird_3.direction = random.randint(0, 1)
    screen.blit(background, (0, 0))
    my_player.draw(screen)
    Birds.draw(screen)
    pygame.display.flip()
    clock.tick(60)
