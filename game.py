import pygame
import sys
import time
from player import Player, Players
from ghost import Ghost
import random
from birds import Bird, Birds
from key import Key, Keys
from wand import Wand, Wands
from sword import Sword, Swords
from bullet1 import Bullet1, Bullets1
from bullet2 import Bullet2, Bullets2
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
            GRASS_SIZE * i, HIGH_TOP_HEIGHT + GRASS_SIZE
        ))
    for i in range(0, LEFT_TOP_X_RANGE // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, HIGH_TOP_HEIGHT + GRASS_SIZE
        ))
    for i in range(MIDDLE_TOP_X_RANGE_LOW // GRASS_SIZE, MIDDLE_TOP_X_RANGE_HI // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, LOW_TOP_HEIGHT + GRASS_SIZE
        ))
    for i in range(LEFT_MID_X_RANGE_LOW // GRASS_SIZE, LEFT_MID_X_RANGE_HI // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, MIDDLE_TOP_HEIGHT + GRASS_SIZE
        ))
    for i in range(RIGHT_MID_X_RANGE_LOW // GRASS_SIZE, RIGHT_MID_X_RANGE_HI // GRASS_SIZE):
        background.blit(grass3, (
            GRASS_SIZE * i, MIDDLE_TOP_HEIGHT + GRASS_SIZE
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

my_player = Player(SCREEN_WIDTH - 3 * PLAYER_WIDTH, 'character_1')
my_ghost = Ghost(SCREEN_WIDTH - 3 * PLAYER_WIDTH)
ur_player = Player(4 * PLAYER_WIDTH, 'character_2')
ur_ghost = Ghost(4 * PLAYER_WIDTH)
Players.add(ur_player)
for key_pos in KEY_POSITIONS:
    Keys.add(Key(key_pos[0], key_pos[1]))
for wand_pos in WAND_POSITIONS:
    Wands.add(Wand(wand_pos[0], wand_pos[1]))
for sword_pos in SWORD_POSITIONS:
    Swords.add(Sword(sword_pos[0], sword_pos[1]))
bird_1 = Bird(2 * TILE_SIZE, 2, True, 3)
bird_2 = Bird(4 * TILE_SIZE, 3, False, 2)
bird_3 = Bird(6 * TILE_SIZE, 4, True, 1)
Birds.add(bird_1)
Birds.add(bird_2)
Birds.add(bird_3)
box_jump = Box(SCREEN_WIDTH // 2 - 3 * TILE_SIZE, LOW_TOP_HEIGHT, 1)
box_double = Box(SCREEN_WIDTH // 2 - TILE_SIZE // 2, LOW_TOP_HEIGHT, 2)
box_revive = Box(SCREEN_WIDTH // 2 + 2 * TILE_SIZE, LOW_TOP_HEIGHT, 3)
Cyclops_1 = Cyclops(SCREEN_WIDTH // 2, GRASS_HEIGHT, (0, SCREEN_WIDTH))
Cyclops_2 = Cyclops(0, HIGH_TOP_HEIGHT, (0, LEFT_TOP_X_RANGE))
Cyclops_3 = Cyclops(SCREEN_WIDTH - PLAYER_WIDTH, HIGH_TOP_HEIGHT, (RIGHT_TOP_X_RANGE, SCREEN_WIDTH))
Enemies.add(Cyclops_1)
Enemies.add(Cyclops_2)
Enemies.add(Cyclops_3)
menu_running = True
tick_num = 0
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
while my_player.health > 0 or my_ghost.revive is True or ur_player.health > 0 or ur_ghost.revive is True:
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
                    if pygame.Rect.colliderect(my_player.rect, box_jump.rect) and my_player.key_num > 0 and my_player.jump_strength != BUFF_JUMP:
                        my_player.jump_strength = BUFF_JUMP
                        my_player.key_num -= 1
                    if pygame.Rect.colliderect(my_player.rect, box_double.rect) and my_player.key_num > 0 and my_player.double_jump == 1:
                        my_player.double_jump = 2
                        my_player.key_num -= 1
                if event.key == pygame.K_UP:
                    my_player.jump = True
                    if my_player.rect.top == my_player.bottom:
                        my_player.jump_count = 0
                    if my_player.jump_count < my_player.double_jump:
                        my_player.vertical_speed = my_player.jump_strength
                        my_player.jump_count += 1
                if event.key == pygame.K_DOWN:
                    if my_player.bottom < GRASS_HEIGHT:
                        my_player.bottom = GRASS_HEIGHT
                    my_player.vertical_speed = 0
                if my_player.wand_count > 0:
                    if event.key == pygame.K_RCTRL:
                        Bullet_1 = Bullet1(my_player.rect.centerx, my_player.rect.top)
                        Bullets1.add(Bullet_1)
                        Bullet_1.get_direction(my_player, ur_player)
                        my_player.wand_count -= 1
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
            if ur_player.health > 0:
                if event.key == pygame.K_a:
                    ur_player.moving_left = True
                if event.key == pygame.K_d:
                    ur_player.moving_right = True
                if event.key == pygame.K_CAPSLOCK:
                    if pygame.Rect.colliderect(ur_player.rect,
                                               box_jump.rect) and ur_player.key_num > 0 and ur_player.jump_strength != BUFF_JUMP:
                        ur_player.jump_strength = BUFF_JUMP
                        ur_player.key_num -= 1
                    if pygame.Rect.colliderect(ur_player.rect,
                                               box_double.rect) and ur_player.key_num > 0 and ur_player.double_jump == 1:
                        ur_player.double_jump = 2
                        ur_player.key_num -= 1
                if event.key == pygame.K_w:
                    ur_player.jump = True
                    if ur_player.rect.top == ur_player.bottom:
                        ur_player.jump_count = 0
                    if ur_player.jump_count < ur_player.double_jump:
                        ur_player.vertical_speed = ur_player.jump_strength
                        ur_player.jump_count += 1
                if event.key == pygame.K_s:
                    if ur_player.bottom < GRASS_HEIGHT:
                        ur_player.bottom = GRASS_HEIGHT
                    ur_player.vertical_speed = 0
                if ur_player.wand_count > 0:
                    if event.key == pygame.K_f:
                        Bullet_2 = Bullet2(ur_player.rect.centerx, ur_player.rect.top)
                        Bullets2.add(Bullet_2)
                        Bullet_2.get_direction(ur_player, my_player)
                        ur_player.wand_count -= 1
            else:
                if event.key == pygame.K_CAPSLOCK:
                    if pygame.Rect.colliderect(ur_ghost.rect, box_revive.rect) and ur_ghost.key_num > 0:
                        ur_player.health = 6
                        ur_ghost.revive = False
                        ur_ghost.key_num = 0
                if event.key == pygame.K_a:
                    ur_ghost.moving_left = True
                if event.key == pygame.K_d:
                    ur_ghost.moving_right = True
                if event.key == pygame.K_w:
                    ur_ghost.moving_up = True
                if event.key == pygame.K_s:
                    ur_ghost.moving_down = True
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
            if ur_player.health > 0:
                if event.key == pygame.K_a:
                    ur_player.moving_left = False
                if event.key == pygame.K_d:
                    ur_player.moving_right = False
            else:
                if event.key == pygame.K_a:
                    ur_ghost.moving_left = False
                if event.key == pygame.K_d:
                    ur_ghost.moving_right = False
                if event.key == pygame.K_w:
                    ur_ghost.moving_up = False
                if event.key == pygame.K_s:
                    ur_ghost.moving_down = False
    ur_player.update()
    ur_ghost.update()
    my_player.update()
    my_ghost.update()
    Birds.update()
    Enemies.update()
    Wands.update()
    Swords.update()
    Bullets1.update()
    Bullets2.update()
    # check for collisions
    if pygame.sprite.spritecollide(my_player, Birds, True):
        my_player.health -= 1
    if pygame.sprite.spritecollide(my_player, Enemies, True):
        my_player.health -= 1
    if my_player.collected_keys < 2:
        if pygame.sprite.spritecollide(my_player, Keys, True):
            my_player.key_num += 1
            my_player.collected_keys += 1
    if pygame.sprite.spritecollide(my_player, Wands, True):
        my_player.wand_count = 3
        if len(Wands) == 0:
            for wand_pos in WAND_POSITIONS:
                Wands.add(Wand(wand_pos[0], wand_pos[1]))
    if pygame.sprite.spritecollide(my_player, Swords, True):
        my_player.have_sword = True
    if pygame.sprite.spritecollide(my_ghost, Keys, True):
        my_ghost.key_num += 1
    if pygame.sprite.spritecollide(ur_player, Birds, True):
        ur_player.health -= 1
    if pygame.sprite.spritecollide(ur_player, Enemies, True):
        ur_player.health -= 1
    if ur_player.collected_keys < 2:
        if pygame.sprite.spritecollide(ur_player, Keys, True):
            ur_player.key_num += 1
            ur_player.collected_keys += 1
    if pygame.sprite.spritecollide(ur_player, Wands, True):
        ur_player.wand_count = 3
        if len(Wands) == 0:
            for wand_pos in WAND_POSITIONS:
                Wands.add(Wand(wand_pos[0], wand_pos[1]))
    if pygame.sprite.spritecollide(ur_player, Swords, True):
        ur_player.have_sword = True
    if pygame.sprite.spritecollide(ur_ghost, Keys, True):
        ur_ghost.key_num += 1
    if COOLDOWN - tick_num < 0:
        if pygame.sprite.spritecollide(my_player, Players, False):
            if my_player.have_sword:
                ur_player.health -= 1
            if ur_player.have_sword:
                my_player.health -= 1
            tick_num = 0
    if pygame.sprite.spritecollide(my_player, Bullets2, True):
        my_player.health -= 1
    if pygame.sprite.spritecollide(ur_player, Bullets1, True):
        ur_player.health -= 1
    screen.blit(background, (0,0))
    Keys.draw(screen)
    box_jump.draw(screen)
    box_double.draw(screen)
    box_revive.draw(screen)
    Enemies.draw(screen)
    Wands.draw(screen)
    Swords.draw(screen)
    Bullets1.draw(screen)
    Bullets2.draw(screen)
    if my_player.health > 0:
        my_player.draw(screen, "MY_PLAYER")
    else:
        my_ghost.draw(screen, "MY_PLAYER")
    if ur_player.health > 0:
        ur_player.draw(screen, "UR_PLAYER")
    else:
        ur_ghost.draw(screen, "UR_PLAYER")
    Birds.draw(screen)
    if COOLDOWN - tick_num > 0:
        text = game_font.render(f"{COOLDOWN - tick_num}", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH - 2 * text.get_width(), 2 * TILE_SIZE))
    else:
        text = game_font.render("You can take damage", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH - 2 * text.get_width(), 2 * TILE_SIZE))
    pygame.display.flip()
    tick_num += 1
    clock.tick(60)
