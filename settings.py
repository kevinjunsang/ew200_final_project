TILE_SIZE = 64
TILE_DIMENSIONS = (TILE_SIZE, TILE_SIZE)

SCREEN_WIDTH = 10 * TILE_SIZE
SCREEN_HEIGHT = 10 * TILE_SIZE

BLACK_BOARD = (110, 86, 16)
WHITE_BOARD = (242, 227, 184)
BACKGROUND_BOARD = (51, 38, 1)
BLACK = (0, 0, 0)

LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', "H")
NUMBERS = (1, 2, 3, 4, 5, 6, 7, 8)
BOARD = {}
for LETTER in LETTERS:
    for NUMBER in NUMBERS:
        BOARD[f'{LETTER}{NUMBER}'] = (TILE_SIZE + LETTERS.index(LETTER) * TILE_SIZE,
                                      SCREEN_HEIGHT - TILE_SIZE - NUMBER * TILE_SIZE)
