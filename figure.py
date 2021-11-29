import pygame

'''
        weight = 5
        init_x = 50
        init_y = 400
        color = (255, 255, 255)   
'''


class Figure:
    def __init__(self, name, weight, x, y,
                 color, surface):
        self.name = name
        self.weight = weight
        self.velocity = 0
        self.x = x
        self.y = y
        self.color = color
        self.surface = surface
        self.is_jump = False


class FigureRect(Figure):
    def __init__(self, name, weight, x, y,
                 color, width, height, surface):
        super(FigureRect, self).__init__(name,
                                         weight,
                                         x,
                                         y,
                                         color,
                                         surface)
        self.rect_width = width
        self.rect_height = height
        self.rect = pygame.Rect(self.x, self.y,
                                self.rect_width,
                                self.rect_height)

    def draw_rect(self):
        self.rect = pygame.Rect(self.x, self.y,
                                self.rect_width,
                                self.rect_height)
        pygame.draw.rect(self.surface,
                         self.color,
                         self.rect)


class FigureCircle(Figure):
    def __init__(self, name, weight, x, y,
                 color, radius, surface):
        super(FigureCircle, self).__init__(name,
                                           weight,
                                           x,
                                           y,
                                           color,
                                           surface)
        self.radius = radius
