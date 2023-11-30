import pygame
import sys
import time
from player import Player
from ghost import Ghost
import random
from birds import Bird, Birds
from key import Key, Keys
from box import Box
from cyclops import Cyclops, Enemies
from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 24)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = screen.copy()
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
    for i in range(RIGHT_TOP_X_RANGE // GRASS_SIZE, SCREEN_WIDTH // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, RIGHT_TOP_HEIGHT + GRASS_SIZE
        ))
    for i in range(MIDDLE_TOP_X_RANGE_LOW // GRASS_SIZE, MIDDLE_TOP_X_RANGE_HI // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, MIDDLE_TOP_HEIGHT + GRASS_SIZE
        ))
    for i in range(LEFT_TOP_X_RANGE_LOW // GRASS_SIZE, LEFT_TOP_X_RANGE_HI // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, LEFT_TOP_HEIGHT + GRASS_SIZE
        ))


draw_background()
menu = background.copy()


def draw_menu():
    player_text = game_font.render("The goal of the game is to kill the other player", True, BLACK)
    menu.blit(player_text, (SCREEN_WIDTH // 2 - player_text.get_width() // 2, GRASS_SIZE))
    player_text = game_font.render("Collect buffs and weapons", True, BLACK)
    menu.blit(player_text, (SCREEN_WIDTH // 2 - player_text.get_width() // 2, 3 * GRASS_SIZE))
    player_text = game_font.render("Take their lives before you lose yours", True, BLACK)
    menu.blit(player_text, (SCREEN_WIDTH // 2 - player_text.get_width() // 2, 5 * GRASS_SIZE))
    player_text = game_font.render("Press space to continue", True, BLACK)
    menu.blit(player_text, (SCREEN_WIDTH // 2 - player_text.get_width() // 2, 7 * GRASS_SIZE))


draw_menu()

my_player = Player()
my_ghost = Ghost()
key_1 = Key(2 * TILE_SIZE, GRASS_HEIGHT)
key_2 = Key(6 * TILE_SIZE, GRASS_HEIGHT)
key_3 = Key(SCREEN_WIDTH - 2 * TILE_SIZE, RIGHT_TOP_HEIGHT)
Keys.add(key_1)
Keys.add(key_2)
Keys.add(key_3)
bird_1 = Bird(2 * TILE_SIZE, 2, True, 3)
bird_2 = Bird(4 * TILE_SIZE, 3, False, 2)
bird_3 = Bird(6 * TILE_SIZE, 4, True, 1)
Birds.add(bird_1)
Birds.add(bird_2)
Birds.add(bird_3)
box_jump = Box(SCREEN_WIDTH // 2, MIDDLE_TOP_HEIGHT, 1)
box_double = Box(SCREEN_WIDTH // 2 + 3 * TILE_SIZE, MIDDLE_TOP_HEIGHT, 2)
box_revive = Box(SCREEN_WIDTH // 2 + 6 * TILE_SIZE, MIDDLE_TOP_HEIGHT, 3)
Cyclops_1 = Cyclops(0, GRASS_HEIGHT, (0, SCREEN_WIDTH))
Cyclops_2 = Cyclops(SCREEN_WIDTH - PLAYER_WIDTH, RIGHT_TOP_HEIGHT, (RIGHT_TOP_X_RANGE, SCREEN_WIDTH))
Cyclops_3 = Cyclops(LEFT_TOP_X_RANGE_HI - PLAYER_WIDTH, LEFT_TOP_HEIGHT, (LEFT_TOP_X_RANGE_LOW, LEFT_TOP_X_RANGE_HI))
Enemies.add(Cyclops_1)
Enemies.add(Cyclops_2)
Enemies.add(Cyclops_3)
menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_running = False
    screen.blit(menu, (0, 0))
    pygame.display.flip()
screen.blit(background, (0, 0))
pygame.display.flip()
while my_player.health > 0 or my_ghost.revive is True:
    # listen for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if my_player.health > 0:
                if event.key == pygame.K_LEFT:
                    my_player.moving_left = True
                if event.key == pygame.K_RIGHT:
                    my_player.moving_right = True
                if event.key == pygame.K_RETURN:
                    if pygame.Rect.colliderect(my_player.rect, box_jump.rect) and my_player.key_num > 0:
                        my_player.jump_strength = BUFF_JUMP
                        my_player.key_num -= 1
                    if pygame.Rect.colliderect(my_player.rect, box_double.rect) and my_player.key_num > 0:
                        my_player.double_jump = 2
                        my_player.key_num -= 1
                if event.key == pygame.K_UP:
                    if my_player.rect.top == my_player.bottom:
                        my_player.jump_count = 0
                    if my_player.jump_count < my_player.double_jump:
                        my_player.vertical_speed = my_player.jump_strength
                        my_player.jump_count += 1
                if event.key == pygame.K_DOWN:
                    if my_player.bottom < GRASS_HEIGHT:
                        my_player.bottom = GRASS_HEIGHT
                    my_player.vertical_speed = 0
            else:
                if event.key == pygame.K_RETURN:
                    if pygame.Rect.colliderect(my_ghost.rect, box_revive.rect) and my_ghost.key_num > 0:
                        my_player.health = 6
                        my_ghost.revive = False
                        my_ghost.key_num = 0
                if event.key == pygame.K_LEFT:
                    my_ghost.moving_left = True
                if event.key == pygame.K_RIGHT:
                    my_ghost.moving_right = True
                if event.key == pygame.K_UP:
                    my_ghost.moving_up = True
                if event.key == pygame.K_DOWN:
                    my_ghost.moving_down = True
        elif event.type == pygame.KEYUP:
            if my_player.health > 0:
                if event.key == pygame.K_LEFT:
                    my_player.moving_left = False
                if event.key == pygame.K_RIGHT:
                    my_player.moving_right = False
            else:
                if event.key == pygame.K_LEFT:
                    my_ghost.moving_left = False
                if event.key == pygame.K_RIGHT:
                    my_ghost.moving_right = False
                if event.key == pygame.K_UP:
                    my_ghost.moving_up = False
                if event.key == pygame.K_DOWN:
                    my_ghost.moving_down = False

    my_player.update()
    my_ghost.update()
    Birds.update()
    Enemies.update()
    # check for collisions
    if pygame.sprite.spritecollide(my_player, Birds, True):
        my_player.health -= 1
    if pygame.sprite.spritecollide(my_player, Enemies, True):
        my_player.health -= 1
    if my_player.collected_keys < 2:
        if pygame.sprite.spritecollide(my_player, Keys, True):
            my_player.key_num += 1
            my_player.collected_keys += 1
    if pygame.sprite.spritecollide(my_ghost, Keys, True):
        my_ghost.key_num += 1
    if bird_1 not in Birds:
        Birds.add(bird_1)
        bird_1.rect.x = SCREEN_WIDTH
        bird_1.direction = random.randint(0, 1)
        bird_1.speed = random.randint(2, 6)
    if bird_2 not in Birds:
        Birds.add(bird_2)
        bird_2.rect.x = SCREEN_WIDTH
        bird_2.direction = random.randint(0, 1)
        bird_2.speed = random.randint(2, 6)
    if bird_3 not in Birds:
        Birds.add(bird_3)
        bird_3.rect.x = SCREEN_WIDTH
        bird_3.direction = random.randint(0, 1)
        bird_3.speed = random.randint(2, 6)
    screen.blit(background, (0, 0))
    Keys.draw(screen)
    box_jump.draw(screen)
    box_double.draw(screen)
    box_revive.draw(screen)
    Enemies.draw(screen)
    if my_player.health > 0:
        my_player.draw(screen)
    else:
        my_ghost.draw(screen)
    Birds.draw(screen)
    text = game_font.render(f"{my_player.score // 6}", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH - 2 * text.get_width(), 2 * TILE_SIZE))
    pygame.display.flip()
    clock.tick(60)
