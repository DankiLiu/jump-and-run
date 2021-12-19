import pygame.sprite

from figure import FigurePink
from jumping_bar import JumpingBar
from platform import Platform
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
    print(os.listdir(directory + '/assets/platforms/'))
    print(file_names)

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


def draw_ground(win, ground, settings):
    pygame.draw.rect(surface=win,
                     color=settings.gd_color,
                     rect=ground)


def draw_platforms(win, group):
    for platform in group:
        win.blit(platform.image, [platform.rect.x, platform.rect.y])

def draw_player(win, player):
    win.blit(player.image, [player.x, player.y])


def locate(loc, ground_height, settings):
    '''Transform the location from left-bottom to left up.'''
    return loc[0], settings.can_h - ground_height - loc[1]
