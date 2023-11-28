import pygame

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, path_image:str, center:tuple, velocidad:int=3):
        super().__init__()

        self.asteroide = pygame.image.load(path_image).convert_alpha()
        self.image = self.asteroide
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.velocidad = velocidad
        self.aceleracion = 1.2

    def update(self):
        self.aceleracion += 0.1
        self.rect.y += self.velocidad * self.aceleracion


