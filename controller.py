import pygame

is_upon = False
COLL_COLOR = (237, 66, 86)
ORI_COLOR = (123, 29, 97)


def key_events(keys, figure, settings, bars):
    """Events for key-pressing."""
    if keys[pygame.K_UP]:
        figure.is_jump = True
        figure.velocity = settings.speed
        jump_up(figure, settings)
    if keys[pygame.K_LEFT]:
        move_left(figure, settings)
    if keys[pygame.K_RIGHT]:
        move_right(figure, settings)
    if keys[pygame.K_q]:
        settings.active = False


def update_player(figure, settings, bars):
    """
    If the player collides with the jumping bar on the top surface,
    then it will stays on the bar, otherwise it will fall.
    :param figure: player object
    :param settings: game settings
    :param bars: jumping bars
    :return: None
    """
    '''
    Is player is on the surface, velocity=0, if it is not on the surface,
    apply gravity.
    If it jumps, velocity=speed, apply gravity
    '''
    if figure.y + figure.rect_size >= settings.gd_height:
        # Player touches the ground, horizontal position does not move.
        figure.velocity = 0
        settings.is_jump = False
        return

    diff, is_collide = check_collision_next_step(figure, settings, bars)
    if is_collide:
        figure.velocity = 0
        figure.y -= diff
        figure.is_jump = False
    else:
        jump_up(figure, settings)


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
    print(diff)
    return diff, collision


def move_left(figure, settings):
    figure.x -= settings.speed


def move_right(figure, settings):
    figure.x += settings.speed


def check_collision(y, velocity, figure, bars):
    for bar in bars:
        # Figure x should be in the range of bar width
        # Figure y should be in the range of bar height or a little bit above
        left = bar.x - figure.width / 2
        right = bar.x + bar.width - figure.width / 2
        # print(f"range is {left} {right}")
        if right >= figure.x >= left:
            if bar.height + bar.y >= y + figure.rect_size >= bar.y and velocity <= 0:
                bar.color = COLL_COLOR
                return True
        bar.color = ORI_COLOR
    return False

