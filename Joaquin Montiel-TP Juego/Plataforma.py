import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, path_imagen, size):
        super().__init__()

        self.plataforma = pygame.transform.scale(pygame.image.load(path_imagen), size)
        self.image = self.plataforma
        self.rect = self.image.get_rect()

    def update(self):
        pass
