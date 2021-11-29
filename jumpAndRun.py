import pygame

from figure import FigureRect, FigureCircle
from settings import Settings

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump and Run")

settings = Settings(velocity=50, gravity=10)

t = 1

while settings.active:
    pygame.time.delay(100)
    events = pygame.event.get()

    # Create object
    figure = FigureRect(name="my_rect",
                        weight=5,
                        x=50,
                        y=400,
                        color=(255, 255, 255),
                        width=50,
                        height=50,
                        surface=win)

    for event in events:
        if event.type == pygame.QUIT:
            settings.active = False
    keys = pygame.key.get_pressed()

    if not figure.is_jump and keys[pygame.K_UP]:
        figure.is_jump = True
        figure.velocity = settings.v0
    if figure.is_jump:
        print("jump")
        s = figure.velocity * t + 0.5 * \
            settings.direction * \
            settings.gravity * (t ** 2)
        figure.velocity -= settings.direction * \
                           settings.gravity * t
        figure.y -= s
        t += 1
        print("y=", figure.y, " v=", figure.velocity)
        if figure.velocity <= 0:
            print("changed direction")
            settings.direction = -1
        if figure.velocity >= -settings.v0:
            print("stop")
            figure.is_jump = False
            figure.velocity = 0
            settings.direction = 1
            y = 400
            t = 1
        print("y=", figure.y, " v=", figure.velocity)
    win.fill((0, 0, 0))
    figure.draw_rect()
    pygame.display.update()

pygame.quit()
