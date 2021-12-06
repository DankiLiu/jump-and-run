import pygame

IS_UP = False
COLL_COLOR = (237, 66, 86)
ORI_COLOR = (123, 29, 97)


def key_events(keys, figure, settings, bars):
    """Events for key-pressing."""
    if keys[pygame.K_UP]:
        if not figure.is_jump:
            figure.is_jump = True
            figure.velocity = settings.speed
            jump_up(figure, settings)
    if keys[pygame.K_LEFT]:
        move_left(figure, settings)
    if keys[pygame.K_RIGHT]:
        move_right(figure, settings)
    if keys[pygame.K_q]:
        settings.active = False


def update_player(figure, settings, bars, ground):
    """
    If the player collides with the jumping bar on the top surface,
    then it will stays on the bar, otherwise it will fall.
    :param figure: player object
    :param settings: game settings
    :param bars: jumping bars
    :return: None
    """
    scroll_vertical(figure, settings, bars, ground)
    bars.add(ground)
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
    return diff, collision


def move_left(figure, settings):
    figure.x -= settings.h_speed


def move_right(figure, settings):
    figure.x += settings.h_speed


def check_collision(y, velocity, figure, bars):
    for bar in bars:
        # Figure x should be in the range of bar width
        # Figure y should be in the range of bar height or a little bit above
        left = bar.x - figure.width / 2
        right = bar.x + bar.width - figure.width / 2
        # print(f"range is {left} {right}")
        if right >= figure.x >= left:
            if bar.height + bar.y >= y + figure.height >= bar.y and velocity <= 0:
                return True
    return False


def scroll_vertical(figure, settings, bars, ground):
    """When the player reaches the top of the screen, scroll the screen up."""
    # If figure.y <= 100, move everything down 100
    if figure.y <= 50:
        scroll_up(figure, settings, bars, ground)

    if settings.scrolled_up and figure.y >= 200:
        scroll_down(figure, settings, bars, ground)


def scroll_up(figure, settings, bars, ground):
    # Scroll all the objects down
    bars.add(ground)

    for i in range(settings.scroll_dis):
        for obj in bars:
            obj.y += 1
        figure.y += 1
    settings.scrolled_up = True


def scroll_down(figure, settings, bars, ground):
    bars.add(ground)

    for i in range(settings.scroll_dis):
        if ground.y <= settings.gd_height:
            return
        for obj in bars:
            obj.y -= 1
        figure.y -= 1