import pygame


class Settings:
    """Class for store game settings."""
    def __init__(self, velocity, gravity):
        self.active = True
        # init velocity the object jumps
        self.v0 = velocity
        # direction == 1: object moves up
        # direction == -1: object moves down
        self.direction = 1
        self.gravity = gravity
