PLAYER_SIZE = (24, 24)
TILE_SIZE = 24
PLAYER_HEIGHT = 24
PLAYER_WIDTH = 24
GRASS_SIZE = 18
TILE_DIMENSIONS = (TILE_SIZE, TILE_SIZE)

BASE_JUMP = 28
BUFF_JUMP = 15
SCREEN_WIDTH = 36 * TILE_SIZE
SCREEN_HEIGHT = 24 * TILE_SIZE

MY_SWORD_POSITION = (SCREEN_WIDTH - 4 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
MY_HEART_1_POSITION = (SCREEN_WIDTH - 3 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
MY_HEART_2_POSITION = (SCREEN_WIDTH - 2 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
MY_HEART_3_POSITION = (SCREEN_WIDTH - 1 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
MY_WEAPON_1_POSITION = (SCREEN_WIDTH - 3 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
MY_WEAPON_2_POSITION = (SCREEN_WIDTH - 2 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
MY_WEAPON_3_POSITION = (SCREEN_WIDTH - 1 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
MY_KEY_1_POSITION = (SCREEN_WIDTH - 3 * TILE_SIZE, SCREEN_HEIGHT - 3 * TILE_SIZE)
MY_KEY_2_POSITION = (SCREEN_WIDTH - 2 * TILE_SIZE, SCREEN_HEIGHT - 3 * TILE_SIZE)
MY_KEY_3_POSITION = (SCREEN_WIDTH - 1 * TILE_SIZE, SCREEN_HEIGHT - 3 * TILE_SIZE)

UR_WORD_POSITION = (4 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
UR_HEART_1_POSITION = (3 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
UR_HEART_2_POSITION = (2 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
UR_HEART_3_POSITION = (1 * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)
UR_WEAPON_1_POSITION = (3 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
UR_WEAPON_2_POSITION = (2 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
UR_WEAPON_3_POSITION = (1 * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)
UR_KEY_1_POSITION = (3 * TILE_SIZE, SCREEN_HEIGHT - 3 * TILE_SIZE)
UR_KEY_2_POSITION = (2 * TILE_SIZE, SCREEN_HEIGHT - 3 * TILE_SIZE)
UR_KEY_3_POSITION = (1 * TILE_SIZE, SCREEN_HEIGHT - 3 * TILE_SIZE)


GRASS_HEIGHT = SCREEN_HEIGHT // 2 + 7 * GRASS_SIZE
LOW_TOP_HEIGHT = SCREEN_HEIGHT // 2 + 3 * GRASS_SIZE
MIDDLE_TOP_HEIGHT = SCREEN_HEIGHT // 2
HIGH_TOP_HEIGHT = SCREEN_HEIGHT // 2 - 8 * GRASS_SIZE

MIDDLE_TOP_X_RANGE_LOW = SCREEN_WIDTH // 2 - 4 * GRASS_SIZE
MIDDLE_TOP_X_RANGE_HI = SCREEN_WIDTH // 2 + 4 * GRASS_SIZE
RIGHT_TOP_X_RANGE = 4 * SCREEN_WIDTH // 5
LEFT_TOP_X_RANGE = SCREEN_WIDTH // 5
RIGHT_MID_X_RANGE_HI = RIGHT_TOP_X_RANGE - 3 * GRASS_SIZE
RIGHT_MID_X_RANGE_LOW = MIDDLE_TOP_X_RANGE_HI + 3 * GRASS_SIZE
LEFT_MID_X_RANGE_HI = MIDDLE_TOP_X_RANGE_LOW - 3 * GRASS_SIZE
LEFT_MID_X_RANGE_LOW = LEFT_TOP_X_RANGE + 3 * GRASS_SIZE

SWORD_1_BOX = ()

KEY_POSITIONS = [
    (2 * TILE_SIZE, GRASS_HEIGHT),
    (SCREEN_WIDTH - 2 * TILE_SIZE, GRASS_HEIGHT),
    (LEFT_MID_X_RANGE_HI - TILE_SIZE, MIDDLE_TOP_HEIGHT),
    (RIGHT_MID_X_RANGE_LOW, MIDDLE_TOP_HEIGHT),
    (LEFT_TOP_X_RANGE - 2 * TILE_SIZE, HIGH_TOP_HEIGHT),
    (RIGHT_TOP_X_RANGE + TILE_SIZE, HIGH_TOP_HEIGHT)
]
WAND_POSITIONS = [
    (LEFT_TOP_X_RANGE - 4 * TILE_SIZE, HIGH_TOP_HEIGHT),
    (RIGHT_TOP_X_RANGE + 3 * TILE_SIZE, HIGH_TOP_HEIGHT)
]
SWORD_POSITIONS = [
    (LEFT_MID_X_RANGE_HI - 3 * TILE_SIZE, MIDDLE_TOP_HEIGHT),
    (RIGHT_MID_X_RANGE_LOW + 2 * TILE_SIZE, MIDDLE_TOP_HEIGHT)
]

BACKGROUND_CLOUD_COLOR = (223, 246, 245)
BACKGROUND_GROUND_COLOR = (194, 227, 232)
BOX_COLOR = (30, 172, 223)
BLACK = (0, 0, 0)

COOLDOWN = 120
