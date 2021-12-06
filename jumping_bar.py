import pygame
from pygame.sprite import Sprite, AbstractGroup


class JumpingBar(Sprite):
    """This class defines a jumping bar given its position,
    size and color."""
    def __init__(self, pos, size, color):
        # Size should be a tuple or a list [width, height]
        Sprite.__init__(self)
        # Calculate the position of the rectangle
        self._x = float(pos[0])
        self._y = float(pos[1])
        self.bar_size = size
        self.rect = pygame.Rect((int(self._x), int(self._y)),
                                (self.bar_size[0],
                                 self.bar_size[1]))
        # Shape of the bar
        self.color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = float(new_x)
        self.rect.x = int(self._x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = float(new_y)
        self.rect.y = int(self._y)

    @property
    def width(self):
        return self.bar_size[0]

    @property
    def height(self):
        return self.bar_size[1]