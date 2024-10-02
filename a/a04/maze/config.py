#==============================================================================
# Maze
#
# Some options:
#
# ROWS = 20
# COLS = 20
# CELLWIDTH = 32
#
# ROWS = 40
# COLS = 80
# CELLWIDTH = 16
#==============================================================================
ROWS = 20                  # number of rows in maze
COLS = 20                  # number of columns in maze

PUNCHES = (ROWS * COLS) * 0.1   # number of punches in wall after maze is generated
                           # (to create loops).
                         
CELLWIDTH = 32             # assume each cell is a square

WALLWIDTH =  CELLWIDTH // 8 # Approximately CELLWIDTH/8
if WALLWIDTH <= 1:
    WALLWIDTH = 2

X,Y = 0,0                   # relative top-left for whole maze

#==============================================================================
# Bot
#==============================================================================
BOT_RADIUS = (CELLWIDTH - WALLWIDTH) // 2 - 1
if BOT_RADIUS < 2:
    BOT_RADIUS = 2
SPEED = 8                   # If too large, will fail tolerance test.
BOT_COLOR = (0, 0, 0)

#==============================================================================
# PATH
#==============================================================================
PATH_COLOR = (0, 0, 0)
PATH_LINEWIDTH = CELLWIDTH // 4

#==============================================================================
# ANIMATION
#==============================================================================
DELAY = 2
