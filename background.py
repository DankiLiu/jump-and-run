import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, settings):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_background_image(image_file, settings)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [0, 0]
        self.drawing_pos = [self.rect.x, self.rect.y]


def load_background_image(image_file, settings):
    image = pygame.image.load(image_file)
    scale = image.get_height() / settings.can_h
    platform_height = settings.can_h
    platform_width = int(image.get_width() / scale)
    settings.gd_width = platform_width
    print(f"background width {platform_width} height {platform_height}")
    return pygame.transform.scale(image, (platform_width, platform_height))