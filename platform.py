import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, image_file, loc, settings, scale=0.3):
        pygame.sprite.Sprite.__init__(self)
        self.scale = scale
        self.settings = settings
        self.image = self.load_platform_image(image_file)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = loc

        self.collision_rect = pygame.Rect(self.rect.x,
                                          self.rect.y + self.rect.height/2,
                                          self.rect.width,
                                          self.rect.height / 2)
        self.drawing_pos = [self.x, self.y]

    def load_platform_image(self, image_file):
        image = pygame.image.load(image_file)
        platform_height = int(image.get_height() * self.scale)
        platform_width = int(image.get_width() * self.scale)
        print(f"width {platform_width} height {platform_height}")
        return pygame.transform.scale(image, (platform_width, platform_height))

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def width(self):
        return self.image.get_width()

    @property
    def height(self):
        return self.image.get_height()

    @property
    def collision_height(self):
        return self.collision_rect.height

    @property
    def collision_y(self):
        return self.collision_rect.y


class Ground(Platform):
    def __init__(self, image_file, loc, settings):
        super(Ground, self).__init__(image_file, loc, settings, 1.0)
        self.resize_image(settings)
        self.relocate_image()

        self.collision_rect = pygame.Rect(self.rect.x,
                                          self.rect.y + self.rect.height/2,
                                          self.rect.width,
                                          self.rect.height / 2)

        self.drawing_pos = [self.x, self.y]

    def resize_image(self, settings):
        scale = self.image.get_width() / settings.gd_width
        image_width = settings.gd_width
        print(scale)
        image_height = int(self.image.get_height() / scale)
        print(f"ground after resize {image_width}, {image_height}")
        self.image = pygame.transform.scale(self.image, (image_width, image_height))

    def relocate_image(self):
        # locate in game coordinate (0, 0)
        gd_y = int(self.settings.can_h - self.image.get_height())
        self.rect.x, self.rect.y = [0, gd_y]
