import pygame.sprite

from figure import FigurePink
from jumping_bar import JumpingBar
from platform import Platform
from platform import Ground
from settings import Settings
import os, os.path

sets = Settings()


# Generate assets of the game
def generate_gd(settings):
    ground = JumpingBar([0, settings.gd_height],
                        size=[settings.can_w, settings.gd_thick],
                        color=settings.gd_color)

    return ground


def generate_gd_img(settings):
    bg = pygame.image.load("assets/bg.png")
    return bg


def generate_platforms(settings):
    group = pygame.sprite.Group()
    directory = os.getcwd()
    file_path = directory + '/assets/platforms/'
    file_names = [file_path + name for name in os.listdir(directory + '/assets/platforms/')]
    # Generate ground
    ground_path = directory + '/assets/foreground.png'
    group.add(Ground(ground_path, [0, 0], settings))
    # Place the bar
    for i in range(len(file_names)):
        x = 50 + i * 150
        y = 300
        print("filename = ", file_names[i])
        platform = Platform(file_names[i], [x, y], settings)
        group.add(platform)
    return group


def generate_player(settings):
    # initial height = can_h - ground_h - figure_h
    init_location = [20, 0]
    return FigurePink(image_file="assets/figure/pink1.png",
                      pos=init_location,
                      settings=settings)


def draw_platforms(win, group, settings):
    for platform in group:
        win.blit(platform.image, platform.drawing_pos)


def draw_player(win, player):
    win.blit(player.image, player.drawing_pos)


def locate(loc, ground_height, settings):
    '''Transform the location from left-bottom to left up.'''
    return loc[0], settings.can_h - ground_height - loc[1]


def screen(figure, settings, platforms, background):
    if figure.x < 200:
        settings.screen_x = 0
    else:
        settings.screen_x = figure.x - 200
    figure.drawing_pos = [figure.x - settings.screen_x, figure.y]
    for platform in platforms:
        platform.drawing_pos[0] = platform.x - settings.screen_x
    background.drawing_pos[0] = -settings.screen_x
