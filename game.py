import pygame
from settings import *
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill(BACKGROUND_BOARD)

clock = pygame.time.Clock()


def draw_board():
    pygame.draw.rect(screen, BLACK_BOARD, (TILE_SIZE, TILE_SIZE,
                                           SCREEN_WIDTH - 2 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE))
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, WHITE_BOARD, (TILE_SIZE + 2 * i * TILE_SIZE,
                                                   TILE_SIZE + 2 * j * TILE_SIZE,
                                                   TILE_SIZE,
                                                   TILE_SIZE))
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, WHITE_BOARD, (2 * TILE_SIZE + 2 * i * TILE_SIZE,
                                                   2 * TILE_SIZE + 2 * j * TILE_SIZE,
                                                   TILE_SIZE,
                                                   TILE_SIZE))
    pygame.display.flip()


draw_board()
print(BOARD)

while True:
    # listen for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
