import pygame

IS_UP = False
COLL_COLOR = (237, 66, 86)
ORI_COLOR = (123, 29, 97)


def key_events(keys, figure, settings, platforms, background):
    """Events for key-pressing."""
    if keys[pygame.K_SPACE]:
        if not figure.is_jump:
            figure.is_jump = True
            figure.velocity = settings.jump_speed
            jump_up(figure, settings)
    if keys[pygame.K_LEFT]:
        move_left(figure, settings)
    if keys[pygame.K_RIGHT]:
        move_right(figure, settings)
    if keys[pygame.K_q]:
        settings.active = False


def update_player(figure, settings, platforms):
    """
    If the player collides with the jumping bar on the top surface,
    then it will stay on the bar, otherwise apply gravity.
    """
    figure.animation()
    diff, collision = check_collision_next_step(figure, settings, platforms)
    if collision:
        figure.is_jump = False
    else:
        jump_up(figure, settings)

    figure.left = False
    figure.right = False


def jump_up(figure, settings, diffn=1):
    figure.velocity -= settings.acc
    sign = -1 if figure.velocity <= 0 else 1
    diff = abs(figure.velocity)
    while diff >= diffn:
        figure.y -= sign
        diff -= 1


def check_collision_next_step(figure, settings, bars):
    velocity = figure.velocity - settings.acc
    y = figure.y
    sign = -1 if figure.velocity <= 0 else 1
    diff = abs(velocity)
    collision = False
    while diff >= 1:
        y -= sign
        diff -= 1
        collision = check_collision(y, velocity, figure, bars)
        if collision:
            break
    return diff, collision


def move_left(figure, settings):
    figure.left = True
    figure.x -= settings.h_speed


def move_right(figure, settings):
    figure.right = True
    figure.x += settings.h_speed


def check_collision(y, velocity, figure, bars):
    for bar in bars:
        # Figure x should be in the range of bar width
        # Figure y should be in the range of bar height or a little bit above
        left = bar.x - figure.width / 2
        right = bar.x + bar.width - figure.width / 2
        # print(f"range is {left} {right}")
        if right >= figure.x >= left:
            if bar.collision_height + bar.collision_y >= y + figure.height >= bar.collision_y and velocity <= 0:
                return True
    return False
