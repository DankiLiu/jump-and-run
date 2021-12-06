import pygame

FIG_SIZE = 30
FIG_POS = [30, 30]
FIG_COLOR = (222, 141, 124)
WEIGHT = 5


class Figure:
    def __init__(self, name="pat"):
        self.name = name
        self.velocity = 0.0
        self.is_jump = False
        self.on_ground = True


class FigureRect(Figure):
    def __init__(self, pos, size, name="Sha",
                 color=FIG_COLOR):
        super(FigureRect, self).__init__(name)
        self.rect_size = size
        self._x = pos[0]
        self._y = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.rect = pygame.Rect(self._x,
                                self._y,
                                self.width,
                                self.height)
        self.color = color

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self.rect.x = new_x
        self._x = self.rect.x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self.rect.y = new_y
        self._y = self.rect.y


class FigureCircle(Figure):
    def __init__(self, settings, name):
        super(FigureCircle, self).__init__(settings)
