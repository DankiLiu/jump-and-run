import pygame

from settings import Settings
from controller import key_events, update_player
from background import Background
from util import generate_platforms, generate_player, \
    draw_player, draw_platforms, screen

pygame.init()
# Create a canvas
settings = Settings()
win = pygame.display.set_mode((settings.can_w,
                               settings.can_h))

pygame.display.set_caption("Jump and Run")

# Create bg
bg = Background("assets/background.png", settings)

# Create player
figure = generate_player(settings)
print("ground width settings ", settings.gd_width)
# Create bars
platforms = generate_platforms(settings)

while settings.active:
    pygame.time.delay(int(1000.0 / 60.0))
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            settings.active = False
    keys = pygame.key.get_pressed()
    key_events(keys, figure, settings, platforms, bg)

    update_player(figure, settings, platforms)

    # update screen
    screen(figure, settings, platforms, bg)

    win.fill((0, 0, 0))
    win.blit(bg.image, bg.drawing_pos)
    draw_platforms(win, platforms, settings)
    draw_player(win, figure)
    pygame.display.update()

pygame.quit()
