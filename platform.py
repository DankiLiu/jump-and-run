import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, image_file, loc, settings):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_platform_image(image_file)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = loc


def load_platform_image(image_file):
    image = pygame.image.load(image_file)
    scale = 0.3
    platform_height = image.get_height() * scale
    platform_width = image.get_width() * scale
    print(f"width {platform_width} height {platform_height}")
    return pygame.transform.scale(image, (platform_width, platform_height))
