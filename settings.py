import pygame
from random import randrange
# Game settings
CANVAS_W = 700
CANVAS_H = 400
BG_COLOR = (145, 202, 242)

# Ground settings
GD_H = 50
GD_W = CANVAS_W
GD_COLOR = (107, 214, 139)

# Bar settings
BAR_NUM = 7


class Settings:
    """Class for store game settings."""
    # Todo: can change settings in the setting-page
    def __init__(self):
        self.active = True
        # Jumping settings
        self.speed = 5
        self.acc = 1
        self.is_jump = False

        # Ground settings
        self.gd_height = CANVAS_H - GD_H
        self.gd_width = GD_W
        self.gd_color = GD_COLOR
        self.gd_thick = GD_H

        # Bar settings
        self.bar_num = BAR_NUM
        self.margin_h = 30
        self.margin_v = 30

        # Appearance settings
        self.can_w = CANVAS_W
        self.can_h = CANVAS_H
        self.bg_color = BG_COLOR

