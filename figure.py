import os

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
    def __init__(self, pos, settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings

        self.velocity = 0
        self.is_jump = False
        self.left = False
        self.right = False

        self.animations = {'left': [], 'right': [],
                           'jump_left': [], 'jump_right': [], 'jump': [],
                           'stand': []}
        self.load_figure_assets()
        self.animation_speed = 0.1
        self.animation_index = 0
        self.image = self.animations['stand'][0]

        self.rect = self.image.get_rect()
        self.set_location(pos)
        self.drawing_pos = pos

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

    def load_figure_assets(self):
        self.load_assets_from_directory('jump_left')
        self.load_assets_from_directory('jump_right')
        self.load_assets_from_directory('jump')
        self.load_assets_from_directory('left')
        self.load_assets_from_directory('right')
        self.load_assets_from_directory('stand')

    def load_assets_from_directory(self, directory):
        path = os.getcwd() + '/assets/girl/' + directory + '/'
        files = [path + name for name in os.listdir(path)]

        for file in files:
            image = pygame.image.load(file)
            # scale = image.get_width() / self.settings.figure_width
            # figure_width = self.settings.figure_width
            figure_width = int(image.get_width() / 25)
            figure_height = int(image.get_height() / 25)
            self.animations[directory].append(pygame.transform.scale(image,
                                                                     (figure_width,
                                                                      figure_height)))

    def animation(self):
        status = self.status()
        self.animation_index += self.animation_speed
        if self.animation_index >= len(self.animations[status]):
            self.animation_index = 0
        self.image = self.animations[status][int(self.animation_index)]

    def status(self):
        if self.is_jump and self.left:
            return 'jump_left'
        if self.is_jump and self.right:
            return 'jump_right'
        if self.left:
            return 'left'
        if self.right:
            return 'right'
        if self.is_jump:
            return 'jump'
        return 'stand'


