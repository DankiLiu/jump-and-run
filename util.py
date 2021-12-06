import pygame.sprite

from settings import Settings
from jumping_bar import JumpingBar
from random import randrange
from figure import FigureRect

sets = Settings()


# Generate assets of the game
def generate_gd(settings):
    ground = JumpingBar([0, settings.gd_height],
                        size=[settings.can_w, settings.gd_thick],
                        color=settings.gd_color)

    return ground


def generate_bars(num, settings):
    group = pygame.sprite.Group()
    # The region that can place bars
    # The height of the bar is 5 in this function
    size = [70, 5]
    h = settings.can_h - settings.gd_thick - \
        settings.margin_v - size[1]
    h_dis = h / num

    # Place the bar
    for i in range(num):
        x = randrange(settings.can_w - size[0] -
                      settings.margin_h)
        y = h_dis * i + settings.margin_v + settings.gd_thick
        print(f"x:{x} y:{y} ")
        bar = JumpingBar([x, y], [70, 5],
                         color=(123, 29, 97))
        group.add(bar)
    return group


def generate_player(settings):
    size = 30
    x = settings.margin_h
    y = settings.gd_height - size
    return FigureRect([x, y], size=size)


def draw_ground(win, ground, settings):
    pygame.draw.rect(surface=win,
                     color=settings.gd_color,
                     rect=ground)


def draw_bars(win, group):
    for bar in group:
        pygame.draw.rect(win,
                         color=bar.color,
                         rect=bar.rect)


def draw_player(win, player):
    pygame.draw.rect(win,
                     color=player.color,
                     rect=player.rect)