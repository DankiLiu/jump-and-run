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


class FigurePink(pygame.sprite.Sprite):
    def __init__(self, image_file, pos, settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings

        self.velocity = 0
        self.is_jump = False
        self.image = self.load_figure_image(image_file)

        self.rect = self.image.get_rect()
        self.set_location(pos)

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, new_x):
        self.rect.x = new_x

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, new_y):
        self.rect.y = new_y

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def set_location(self, loc):
        self.x = loc[0]
        self.y = self.settings.can_h - self.height - self.settings.gd_thick

    def load_figure_image(self, image_file):
        image = pygame.image.load(image_file)
        scale = image.get_width() / self.settings.figure_width
        figure_width = self.settings.figure_width
        figure_height = image.get_height() / scale

        return pygame.transform.scale(image,
                                      (figure_width,
                                       figure_height))
