import pygame
from random import randrange
# Game settings
CANVAS_W = 700
CANVAS_H = 400
BG_COLOR = (145, 202, 242)

# Ground settings
GD_H = 50
GD_W = CANVAS_W
GD_COLOR = (34, 133, 4)
GD_COLOR_L = (45, 158, 11)

# Bar settings
BAR_NUM = 7


class Settings:
    """Class for store game settings."""
    # Todo: can change settings in the setting-page
    def __init__(self):
        self.active = True
        # Jumping settings
        self.speed = 20
        self.h_speed = 5
        self.acc = 1
        self.is_jump = False

        # Ground settings
        self.gd_height = CANVAS_H - GD_H
        self.gd_width = GD_W
        self.gd_color = GD_COLOR
        self.gd_color_l = GD_COLOR_L
        self.gd_thick = GD_H

        # Bar settings
        self.bar_num = BAR_NUM
        self.margin_h = 30
        self.margin_v = 30

        self.bar_c = (78, 9, 156)
        self.bar_c_s = (136, 11, 158)

        # Appearance settings
        self.can_w = CANVAS_W
        self.can_h = CANVAS_H
        self.bg_color = BG_COLOR

        # Scrolling settings
        self.scrolled_up = False
        self.scroll_speed = 5
        self.scroll_dis = 50
