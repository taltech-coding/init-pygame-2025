"""This file holds all constants for the Fruit Ninja game."""

SCREEN_WIDTH = 1280              # Width and height measured in pixels.
SCREEN_HEIGHT = 720              # Changing these two might break things. Approach with caution!

# Colors used throughout the game
PRIMARY = (253, 231, 56)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game States
STATE_MENU = "menu"
STATE_MAP_SELECTION = "map_selection"
STATE_PLAYING = "playing"
STATE_GAME_OVER = "game_over"


# TODO: A gravity modifier needs to be defined.
# Bigger number -> Higher gravity. 
# A value of 0.3 should work well!
