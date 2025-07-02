# Setting parameters
import pygame
import pygame.mixer
GRID_SIZE = 6
BASE_CELL_SIZE = 80 # Base cell size
MIN_CELL_SIZE = 40 # Minimum size when zoomed out
MAX_CELL_SIZE = 160 # Maximum size when zoomed in
MARGIN = 50

# Calculate initial window size
initial_cell_size = BASE_CELL_SIZE
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
ASPHALT = (50, 50, 50)  # Dark gray for road
BROWN = (139, 69, 19)  # For tree trunks

MAROON = (128, 0, 0)
OLIVE = (0, 128, 0)
CYAN = (0, 255, 255)
COLORS = [RED, BLUE, GREEN, YELLOW, PURPLE, PINK, ORANGE, CYAN, MAROON, OLIVE]

#level game
LEVELS = [
    pygame.image.load("button/lv1.png"),
    pygame.image.load("button/lv2.png"),
    pygame.image.load("button/lv3.png"),
    pygame.image.load("button/lv4.png"),
    pygame.image.load("button/lv5.png"),
    pygame.image.load("button/lv6.png"),
    pygame.image.load("button/lv7.png"),
    pygame.image.load("button/lv8.png"),
    pygame.image.load("button/lv9.png"),
    pygame.image.load("button/lv10.png"),
]

start_button = pygame.image.load("button/start.png")
quit_button = pygame.image.load("button/end.png")
forest_green = ((0,50,0))

pygame.mixer.init()
move_sound = pygame.mixer.Sound("music/moves.mp3")
space_sound = pygame.mixer.Sound("music/space.mp3")
i_sound = pygame.mixer.Sound("music/button_I.mp3")
menu_sound = pygame.mixer.Sound("music/menu_sound.mp3")
level_sound = pygame.mixer.Sound("music/level.mp3")
traffic_sound = pygame.mixer.Sound("music/traffic.mp3")