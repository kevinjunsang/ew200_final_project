PLAYER_SIZE = (24, 24)
TILE_SIZE = 24
PLAYER_HEIGHT = 24
PLAYER_WIDTH = 24
GRASS_SIZE = 18
TILE_DIMENSIONS = (TILE_SIZE, TILE_SIZE)

BASE_JUMP = 12
BUFF_JUMP = 15
SCREEN_WIDTH = 36 * TILE_SIZE
SCREEN_HEIGHT = 24 * TILE_SIZE

HEART_1_POSITION = (SCREEN_WIDTH - 3 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
HEART_2_POSITION = (SCREEN_WIDTH - 2 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
HEART_3_POSITION = (SCREEN_WIDTH - 1 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
KEY_1_POSITION = (SCREEN_WIDTH - 3 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
KEY_2_POSITION = (SCREEN_WIDTH - 2 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
KEY_3_POSITION = (TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)

GRASS_HEIGHT = SCREEN_HEIGHT // 2 + 7 * GRASS_SIZE
RIGHT_TOP_HEIGHT = SCREEN_HEIGHT // 2 + 3 * GRASS_SIZE
RIGHT_TOP_X_RANGE = 3 * SCREEN_WIDTH // 4
MIDDLE_TOP_HEIGHT = SCREEN_HEIGHT // 2
MIDDLE_TOP_X_RANGE_LOW = SCREEN_WIDTH // 2
MIDDLE_TOP_X_RANGE_HI = RIGHT_TOP_X_RANGE - 2 * GRASS_SIZE
LEFT_TOP_HEIGHT = SCREEN_HEIGHT // 2 - 8 * GRASS_SIZE
LEFT_TOP_X_RANGE_LOW = SCREEN_WIDTH // 4
LEFT_TOP_X_RANGE_HI = MIDDLE_TOP_X_RANGE_LOW - 3 * GRASS_SIZE

BACKGROUND_CLOUD_COLOR = (223, 246, 245)
BACKGROUND_GROUND_COLOR = (194, 227, 232)
BLACK = (0, 0, 0)
